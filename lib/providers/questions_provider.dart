import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/question.dart';
import '../services/local_cache_service.dart';
import '../services/question_repository.dart';

final questionRepositoryProvider = Provider<QuestionRepository>((ref) {
  return QuestionRepository();
});

final localCacheServiceProvider = Provider<LocalCacheService>((ref) {
  return LocalCacheService.instance;
});

/// Currently selected subject in student view (defaults to Math)
final selectedSubjectProvider = StateProvider<Subject>((ref) => Subject.math);

/// Currently selected chapter filter in student view (null means all chapters)
final selectedChapterProvider = StateProvider<String?>((ref) => null);

/// Simulated Offline Mode toggle for user to test offline resilience
final isOfflineModeProvider = StateProvider<bool>((ref) => false);

/// Count of questions stored in local Hive cache
final cachedQuestionsCountProvider = StateProvider<int>((ref) {
  final cache = ref.watch(localCacheServiceProvider);
  return cache.cachedQuestionsCount;
});

/// Auto-refreshing provider for approved questions
final approvedQuestionsProvider =
    FutureProvider.autoDispose<List<Question>>((ref) async {
  final repository = ref.watch(questionRepositoryProvider);
  final subject = ref.watch(selectedSubjectProvider);
  final chapter = ref.watch(selectedChapterProvider);
  final isOfflineMode = ref.watch(isOfflineModeProvider);

  if (isOfflineMode) {
    // Return exclusively from local cache
    final cached = ref.watch(localCacheServiceProvider).getCachedQuestions(subject: subject);
    if (chapter != null) {
      return cached.where((q) => q.chapterId == chapter && q.status == QuestionStatus.approved).toList();
    }
    return cached.where((q) => q.status == QuestionStatus.approved).toList();
  }

  final questions = await repository.fetchApprovedQuestions(
    subject: subject,
    chapterId: chapter,
  );

  // Update cached count in state
  ref.read(cachedQuestionsCountProvider.notifier).state =
      ref.read(localCacheServiceProvider).cachedQuestionsCount;

  return questions;
});

/// HOTS Questions Provider (High Order Thinking Skills for Math/Science)
final hotsQuestionsProvider =
    Provider.autoDispose<AsyncValue<List<Question>>>((ref) {
  final allQuestionsAsync = ref.watch(approvedQuestionsProvider);
  return allQuestionsAsync.whenData((questions) {
    return questions.where((q) => q.difficultyLevel == DifficultyLevel.hots).toList();
  });
});
