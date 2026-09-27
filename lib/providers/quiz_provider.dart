import 'dart:async';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/question.dart';
import '../models/quiz_session.dart';
import 'questions_provider.dart';

class QuizStateNotifier extends StateNotifier<QuizSession?> {
  final Ref _ref;
  Timer? _timer;

  QuizStateNotifier(this._ref) : super(null);

  /// Start a timed practice quiz for a subject
  Future<void> startQuiz({
    required Subject subject,
    int durationMinutes = 5,
  }) async {
    _timer?.cancel();

    // Fetch approved questions for this subject
    final questions = await _ref
        .read(questionRepositoryProvider)
        .fetchApprovedQuestions(subject: subject);

    // Filter MCQ questions
    final mcqQuestions = questions.where((q) => q.isMCQ).toList();
    if (mcqQuestions.isEmpty) {
      return;
    }

    final totalSeconds = durationMinutes * 60;

    state = QuizSession(
      id: 'quiz-${DateTime.now().millisecondsSinceEpoch}',
      subject: subject,
      questions: mcqQuestions,
      selectedAnswers: {},
      totalDurationSeconds: totalSeconds,
      remainingSeconds: totalSeconds,
      isCompleted: false,
      startedAt: DateTime.now(),
    );

    _startTimer();
  }

  void _startTimer() {
    _timer?.cancel();
    _timer = Timer.periodic(const Duration(seconds: 1), (timer) {
      if (state == null || state!.isCompleted) {
        timer.cancel();
        return;
      }

      if (state!.remainingSeconds <= 1) {
        timer.cancel();
        submitQuiz();
      } else {
        state = state!.copyWith(
          remainingSeconds: state!.remainingSeconds - 1,
        );
      }
    });
  }

  /// Select answer option for a question
  void selectOption(String questionId, String optionId) {
    if (state == null || state!.isCompleted) return;

    final updatedAnswers = Map<String, String>.from(state!.selectedAnswers);
    updatedAnswers[questionId] = optionId;

    state = state!.copyWith(
      selectedAnswers: updatedAnswers,
    );
  }

  /// Submit the quiz and lock answers
  void submitQuiz() {
    if (state == null || state!.isCompleted) return;
    _timer?.cancel();

    state = state!.copyWith(
      isCompleted: true,
      completedAt: DateTime.now(),
    );
  }

  /// Reset / exit quiz
  void resetQuiz() {
    _timer?.cancel();
    state = null;
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }
}

final quizSessionProvider =
    StateNotifierProvider<QuizStateNotifier, QuizSession?>((ref) {
  return QuizStateNotifier(ref);
});
