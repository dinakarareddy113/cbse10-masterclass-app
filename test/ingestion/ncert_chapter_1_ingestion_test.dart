import 'package:flutter_test/flutter_test.dart';
import 'package:cbse_class10_masterclass/models/question.dart';
import 'package:cbse_class10_masterclass/services/question_repository.dart';

void main() {
  group('NCERT Chapter 1 Ingestion & Moderation Queue Tests', () {
    late QuestionRepository repository;

    setUp(() {
      repository = QuestionRepository();
    });

    test('All extracted Chapter 1 questions enter pending_review queue by default', () async {
      final pendingQuestions = await repository.fetchPendingQuestions(subject: Subject.science);
      
      final ch1Questions = pendingQuestions
          .where((q) => q.chapterId == 'science_ch_1_chemical_reactions')
          .toList();

      expect(ch1Questions.isNotEmpty, isTrue);
      expect(ch1Questions.length, greaterThanOrEqualTo(15));

      for (final q in ch1Questions) {
        expect(q.subject, Subject.science);
        expect(q.chapterId, 'science_ch_1_chemical_reactions');
        expect(q.status, QuestionStatus.pendingReview,
            reason: 'Critical Rule: Every extracted question must require admin review');
        expect(q.stepByStepSolution.isNotEmpty, isTrue,
            reason: 'Every question must have a verified step-by-step solution');
        expect(q.isMCQ, isTrue,
            reason: 'MCQ options must be properly structured');
      }
    });

    test('Non-approved Chapter 1 questions are strictly invisible to students', () async {
      final studentVisible = await repository.fetchApprovedQuestions(
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
      );

      // Since all Chapter 1 questions are currently pending review, student feed should return 0
      expect(studentVisible.isEmpty, isTrue,
          reason: 'Students must not see questions before admin moderation');
    });

    test('Admin approval pushes question live to student feed', () async {
      final pending = await repository.fetchPendingQuestions(subject: Subject.science);
      final target = pending.firstWhere((q) => q.chapterId == 'science_ch_1_chemical_reactions');

      final success = await repository.approveQuestion(
        questionId: target.id,
        adminId: '00000000-0000-0000-0000-000000000001',
      );
      expect(success, isTrue);

      // Now student should be able to see the approved question
      final studentApproved = await repository.fetchApprovedQuestions(
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
      );
      expect(studentApproved.any((q) => q.id == target.id), isTrue);
    });
  });
}
