import 'package:flutter_test/flutter_test.dart';
import 'package:cbse_class10_masterclass/models/question.dart';
import 'package:cbse_class10_masterclass/models/quiz_session.dart';

void main() {
  group('QuizSession & Evaluation Engine Tests', () {
    test('Calculates score percentage and analytics accurately', () {
      final q1 = Question(
        id: 'q1',
        subject: Subject.science,
        chapterId: 'sci_01',
        questionText: 'Question 1',
        options: const [
          QuestionOption(id: 'A', text: 'Option A', isCorrect: true),
          QuestionOption(id: 'B', text: 'Option B', isCorrect: false),
        ],
        stepByStepSolution: 'Sol 1',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.approved,
        submittedBy: 'teacher-1',
        createdAt: DateTime.now(),
      );

      final q2 = Question(
        id: 'q2',
        subject: Subject.science,
        chapterId: 'sci_01',
        questionText: 'Question 2',
        options: const [
          QuestionOption(id: 'A', text: 'Option A', isCorrect: false),
          QuestionOption(id: 'B', text: 'Option B', isCorrect: true),
        ],
        stepByStepSolution: 'Sol 2',
        difficultyLevel: DifficultyLevel.medium,
        status: QuestionStatus.approved,
        submittedBy: 'teacher-1',
        createdAt: DateTime.now(),
      );

      final session = QuizSession(
        id: 'session-1',
        subject: Subject.science,
        questions: [q1, q2],
        selectedAnswers: {
          'q1': 'A', // Correct
          'q2': 'A', // Incorrect (Correct is B)
        },
        totalDurationSeconds: 300,
        remainingSeconds: 180,
        startedAt: DateTime.now(),
      );

      expect(session.totalQuestions, 2);
      expect(session.answeredCount, 2);
      expect(session.correctCount, 1);
      expect(session.incorrectCount, 1);
      expect(session.unattemptedCount, 0);
      expect(session.scorePercentage, 50.0);
      expect(session.timeSpentSeconds, 120);
    });
  });
}
