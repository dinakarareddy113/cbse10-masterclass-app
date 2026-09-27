import 'package:flutter_test/flutter_test.dart';
import 'package:cbse_class10_masterclass/models/question.dart';

void main() {
  group('Question & QuestionOption Model Tests', () {
    test('Question serialization and deserialization retains fidelity', () {
      final question = Question(
        id: 'test-q-1',
        subject: Subject.math,
        chapterId: 'ch_04_quadratic_equations',
        questionText: 'What is the discriminant of 2x^2 + 5x + 2 = 0?',
        options: const [
          QuestionOption(id: 'A', text: '9', isCorrect: true),
          QuestionOption(id: 'B', text: '16', isCorrect: false),
          QuestionOption(id: 'C', text: '-9', isCorrect: false),
          QuestionOption(id: 'D', text: '0', isCorrect: false),
        ],
        stepByStepSolution: 'D = b^2 - 4ac = 25 - 4(2)(2) = 25 - 16 = 9',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.approved,
        submittedBy: 'user-teacher-1',
        reviewedBy: 'user-admin-1',
        createdAt: DateTime(2026, 9, 25),
      );

      final json = question.toJson();
      final fromJson = Question.fromJson(json);

      expect(fromJson.id, 'test-q-1');
      expect(fromJson.subject, Subject.math);
      expect(fromJson.difficultyLevel, DifficultyLevel.easy);
      expect(fromJson.status, QuestionStatus.approved);
      expect(fromJson.isMCQ, isTrue);
      expect(fromJson.correctOption?.id, 'A');
      expect(fromJson.correctOption?.text, '9');
    });

    test('Enum fallback parsing handles edge case strings gracefully', () {
      expect(Subject.fromString('MATH'), Subject.math);
      expect(Subject.fromString('sst'), Subject.socialScience);
      expect(Subject.fromString('unknown'), Subject.math);

      expect(DifficultyLevel.fromString('hots'), DifficultyLevel.hots);
      expect(DifficultyLevel.fromString('EASY'), DifficultyLevel.easy);
      expect(DifficultyLevel.fromString('invalid'), DifficultyLevel.medium);

      expect(QuestionStatus.fromString('approved'), QuestionStatus.approved);
      expect(QuestionStatus.fromString('rejected'), QuestionStatus.rejected);
      expect(QuestionStatus.fromString('other'), QuestionStatus.pendingReview);
    });
  });
}
