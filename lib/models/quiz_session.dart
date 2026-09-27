import 'package:flutter/foundation.dart';
import 'question.dart';

@immutable
class QuizSession {
  final String id;
  final Subject subject;
  final List<Question> questions;
  final Map<String, String> selectedAnswers; // questionId -> optionId ('A', 'B', ...)
  final int totalDurationSeconds;
  final int remainingSeconds;
  final bool isCompleted;
  final DateTime startedAt;
  final DateTime? completedAt;

  const QuizSession({
    required this.id,
    required this.subject,
    required this.questions,
    required this.selectedAnswers,
    required this.totalDurationSeconds,
    required this.remainingSeconds,
    this.isCompleted = false,
    required this.startedAt,
    this.completedAt,
  });

  int get totalQuestions => questions.length;
  int get answeredCount => selectedAnswers.length;

  int get correctCount {
    int count = 0;
    for (final q in questions) {
      final selected = selectedAnswers[q.id];
      if (selected != null && q.correctOption?.id == selected) {
        count++;
      }
    }
    return count;
  }

  int get incorrectCount {
    int count = 0;
    for (final q in questions) {
      final selected = selectedAnswers[q.id];
      if (selected != null && q.correctOption?.id != selected) {
        count++;
      }
    }
    return count;
  }

  int get unattemptedCount => totalQuestions - answeredCount;

  double get scorePercentage {
    if (totalQuestions == 0) return 0.0;
    return (correctCount / totalQuestions) * 100.0;
  }

  int get timeSpentSeconds => totalDurationSeconds - remainingSeconds;

  QuizSession copyWith({
    String? id,
    Subject? subject,
    List<Question>? questions,
    Map<String, String>? selectedAnswers,
    int? totalDurationSeconds,
    int? remainingSeconds,
    bool? isCompleted,
    DateTime? startedAt,
    DateTime? completedAt,
  }) {
    return QuizSession(
      id: id ?? this.id,
      subject: subject ?? this.subject,
      questions: questions ?? this.questions,
      selectedAnswers: selectedAnswers ?? this.selectedAnswers,
      totalDurationSeconds: totalDurationSeconds ?? this.totalDurationSeconds,
      remainingSeconds: remainingSeconds ?? this.remainingSeconds,
      isCompleted: isCompleted ?? this.isCompleted,
      startedAt: startedAt ?? this.startedAt,
      completedAt: completedAt ?? this.completedAt,
    );
  }
}
