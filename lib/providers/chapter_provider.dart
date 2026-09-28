import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/chapter.dart';
import '../models/question.dart';
import '../services/local_cache_service.dart';
import 'questions_provider.dart';

/// Provider for loading the 14 Mathematics syllabus chapters with dynamic question counts & progress
final mathChaptersProvider = FutureProvider.autoDispose<List<Chapter>>((ref) async {
  final repository = ref.watch(questionRepositoryProvider);
  ref.watch(approvedQuestionsProvider);
  return repository.fetchChapters(subject: Subject.math);
});

/// Provider for loading the 13 Science syllabus chapters with dynamic question counts & progress
final scienceChaptersProvider = FutureProvider.autoDispose<List<Chapter>>((ref) async {
  final repository = ref.watch(questionRepositoryProvider);
  ref.watch(approvedQuestionsProvider);
  return repository.fetchChapters(subject: Subject.science);
});

/// Provider for loading the 7 Social Science syllabus chapters with dynamic question counts & progress
final sstChaptersProvider = FutureProvider.autoDispose<List<Chapter>>((ref) async {
  final repository = ref.watch(questionRepositoryProvider);
  ref.watch(approvedQuestionsProvider);
  return repository.fetchChapters(subject: Subject.socialScience);
});

/// Currently active chapter for ChapterHub / Practice view
final currentChapterProvider = StateProvider<Chapter?>((ref) => null);

/// State notifier to manage and update solved question counts per chapter
class ChapterProgressNotifier extends StateNotifier<Map<String, Set<String>>> {
  final LocalCacheService _cacheService;
  final Ref _ref;

  ChapterProgressNotifier(this._cacheService, this._ref) : super({});

  Set<String> getSolvedForChapter(String chapterId) {
    return _cacheService.getSolvedQuestionIdsForChapter(chapterId);
  }

  Future<void> markSolved(String questionId, String chapterId) async {
    await _cacheService.markQuestionSolved(questionId, chapterId);
    _ref.invalidate(mathChaptersProvider);
    _ref.invalidate(scienceChaptersProvider);
    _ref.invalidate(sstChaptersProvider);
    state = {
      ...state,
      chapterId: _cacheService.getSolvedQuestionIdsForChapter(chapterId),
    };
  }
}

final chapterProgressProvider =
    StateNotifierProvider<ChapterProgressNotifier, Map<String, Set<String>>>((ref) {
  final cache = ref.watch(localCacheServiceProvider);
  return ChapterProgressNotifier(cache, ref);
});
