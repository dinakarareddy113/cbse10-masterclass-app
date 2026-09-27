import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:hive_flutter/hive_flutter.dart';
import '../core/constants/app_constants.dart';
import '../models/question.dart';

/// Local Storage Service using Hive for caching questions and offline access
class LocalCacheService {
  static final LocalCacheService instance = LocalCacheService._internal();
  LocalCacheService._internal();

  Box<dynamic>? _questionsBox;
  Box<dynamic>? _syncBox;
  Box<dynamic>? _progressBox;

  // In-memory fallback for test and non-Hive environments
  final Set<String> _inMemorySolved = {};

  Future<void> init() async {
    try {
      await Hive.initFlutter();
      _questionsBox = await Hive.openBox<dynamic>(AppConstants.questionsBox);
      _syncBox = await Hive.openBox<dynamic>(AppConstants.syncMetadataBox);
      _progressBox = await Hive.openBox<dynamic>('cbse10_student_progress');
      debugPrint('LocalCacheService: Hive initialized successfully.');
    } catch (e) {
      debugPrint('LocalCacheService initialization error: $e');
    }
  }

  /// Cache a list of approved questions locally
  Future<void> cacheQuestions(List<Question> questions) async {
    if (_questionsBox == null) return;
    final Map<String, String> dataToStore = {};
    for (final q in questions) {
      dataToStore[q.id] = jsonEncode(q.toJson());
    }
    await _questionsBox!.putAll(dataToStore);
    await setLastSyncTime(DateTime.now());
  }

  /// Retrieve all cached approved questions, optionally filtered by subject
  List<Question> getCachedQuestions({Subject? subject}) {
    if (_questionsBox == null) return [];
    final List<Question> results = [];
    for (final key in _questionsBox!.keys) {
      final raw = _questionsBox!.get(key);
      if (raw != null) {
        try {
          final Map<String, dynamic> json = jsonDecode(raw as String) as Map<String, dynamic>;
          final q = Question.fromJson(json);
          if (subject == null || q.subject == subject) {
            results.add(q);
          }
        } catch (e) {
          debugPrint('Error decoding cached question $key: $e');
        }
      }
    }
    return results;
  }

  /// Get count of cached questions
  int get cachedQuestionsCount => _questionsBox?.length ?? 0;

  /// Record sync timestamp
  Future<void> setLastSyncTime(DateTime time) async {
    await _syncBox?.put('last_sync_timestamp', time.toIso8601String());
  }

  /// Get last sync timestamp
  DateTime? getLastSyncTime() {
    final str = _syncBox?.get('last_sync_timestamp') as String?;
    if (str != null) {
      return DateTime.tryParse(str);
    }
    return null;
  }

  /// Record that a student has answered/reviewed a question
  Future<void> markQuestionSolved(String questionId, String chapterId) async {
    _inMemorySolved.add('$chapterId::$questionId');
    if (_progressBox != null) {
      final List<String> current = List<String>.from(
        (_progressBox!.get(chapterId) as List<dynamic>?) ?? <dynamic>[],
      );
      if (!current.contains(questionId)) {
        current.add(questionId);
        await _progressBox!.put(chapterId, current);
      }
    }
  }

  /// Get solved question IDs for a specific chapter
  Set<String> getSolvedQuestionIdsForChapter(String chapterId) {
    if (_progressBox != null) {
      final list = (_progressBox!.get(chapterId) as List<dynamic>?) ?? <dynamic>[];
      return list.map((e) => e.toString()).toSet();
    }
    return _inMemorySolved
        .where((k) => k.startsWith('$chapterId::'))
        .map((k) => k.split('::').last)
        .toSet();
  }

  /// Clear cache
  Future<void> clearCache() async {
    await _questionsBox?.clear();
    await _syncBox?.clear();
    await _progressBox?.clear();
    _inMemorySolved.clear();
  }
}
