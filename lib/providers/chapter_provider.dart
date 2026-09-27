import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/chapter.dart';
import '../models/question.dart';
import '../services/local_cache_service.dart';
import 'questions_provider.dart';

/// Provider for loading the 14 Mathematics syllabus chapters with dynamic question counts & progress
final mathChaptersProvider = FutureProvider.autoDispose<List<Chapter>>((ref) async {
  final repository = ref.watch(questionRepositoryProvider);
  // Invalidate or reload when approved questions change
  ref.watch(approvedQuestionsProvider);
  return repository.fetchChapters(subject: Subject.math);
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
