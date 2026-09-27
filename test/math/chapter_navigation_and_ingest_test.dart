import 'package:flutter_test/flutter_test.dart';
import 'package:cbse10masterclass/core/constants/cbse_curriculum.dart';
import 'package:cbse10masterclass/models/chapter.dart';
import 'package:cbse10masterclass/models/question.dart';
import 'package:cbse10masterclass/services/question_repository.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('CBSE Class 10 Math 14-Chapter Syllabus & Bilingual Verification', () {
    test('All 14 chapters must be seeded in curriculum catalog', () {
      expect(CbseCurriculum.mathChapters.length, equals(14));
      
      for (int i = 0; i < 14; i++) {
        final ch = CbseCurriculum.mathChapters[i];
        expect(ch['chapter_number'], equals(i + 1));
        expect(ch['title_en'], isNotNull);
        expect((ch['title_en'] as String).isNotEmpty, isTrue);
        expect(ch['title_kn'], isNotNull);
        expect((ch['title_kn'] as String).isNotEmpty, isTrue);
        expect(ch['formulas'], isA<List>());
        expect((ch['formulas'] as List).isNotEmpty, isTrue);
      }
    });

    test('Verify authentic Kannada regional names for all 14 chapters', () {
      final expectedKannada = [
        'ವಾಸ್ತವ ಸಂಖ್ಯೆಗಳು', // 1. Real Numbers
        'ಬಹುಪದೋಕ್ತಿಗಳು', // 2. Polynomials
        'ಎರಡು ಚರಾಕ್ಷರಗಳಿರುವ ರೇಖಾತ್ಮಕ ಸಮೀಕರಣಗಳ ಜೋಡಿಗಳು', // 3. Pair of Linear Equations
        'ವರ್ಗ ಸಮೀಕರಣಗಳು', // 4. Quadratic Equations
        'ಸಮಾಂತರ ಶ್ರೇಢಿಗಳು', // 5. Arithmetic Progressions
        'ತ್ರಿಭುಜಗಳು', // 6. Triangles
        'ನಿರ್ದೇಶಾಂಕ ರೇಖಾಗಣಿತ', // 7. Coordinate Geometry
        'ತ್ರಿಕೋನಮಿತಿಯ ಪ್ರಸ್ತಾವನೆ', // 8. Introduction to Trigonometry
        'ತ್ರಿಕೋನಮಿತಿಯ ಕೆಲವು ಅನ್ವಯಗಳು', // 9. Some Applications of Trigonometry
        'ವೃತ್ತಗಳು', // 10. Circles
        'ವೃತ್ತಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ವಿಸ್ತೀರ್ಣಗಳು', // 11. Areas Related to Circles
        'ಮೇಲ್ಮೈ ವಿಸ್ತೀರ್ಣಗಳು ಮತ್ತು ಘನಫಲಗಳು', // 12. Surface Areas and Volumes
        'ಸಂಖ್ಯಾಶಾಸ್ತ್ರ', // 13. Statistics
        'ಸಂಭವನೀಯತೆ', // 14. Probability
      ];

      for (int i = 0; i < 14; i++) {
        expect(CbseCurriculum.mathChapters[i]['title_kn'], equals(expectedKannada[i]));
      }
    });
  });

  group('Chapter Repository & Progress Tracking Tests', () {
    late QuestionRepository repository;

    setUp(() {
      repository = QuestionRepository();
    });

    test('fetchChapters returns all 14 chapters with computed question counts', () async {
      final chapters = await repository.fetchChapters(subject: Subject.math);
      expect(chapters.length, equals(14));

      // Real Numbers (ch 1) has initial seeded questions
      final ch1 = chapters.firstWhere((c) => c.id == 'math_ch_01_real_numbers');
      expect(ch1.titleEn, equals('Real Numbers'));
      expect(ch1.titleKn, equals('ವಾಸ್ತವ ಸಂಖ್ಯೆಗಳು'));
      expect(ch1.totalQuestions, greaterThanOrEqualTo(3));
    });

    test('Admin bulkPublishQuestions immediately publishes approved questions to student feed', () async {
      const targetChapter = 'math_ch_14_probability';
      final testQuestions = [
        Question(
          id: 'test-prob-1',
          subject: Subject.math,
          chapterId: targetChapter,
          questionText: 'A card is drawn from a well-shuffled deck of 52 cards. Find the probability of getting a king of red colour.',
          options: const [
            QuestionOption(id: 'A', text: '1/26', isCorrect: true),
            QuestionOption(id: 'B', text: '1/13', isCorrect: false),
            QuestionOption(id: 'C', text: '1/52', isCorrect: false),
            QuestionOption(id: 'D', text: '2/13', isCorrect: false),
          ],
          stepByStepSolution: 'Step 1: Total possible outcomes = 52.\nStep 2: Number of red kings (Diamond and Heart) = 2.\nStep 3: P(Red King) = 2/52 = 1/26.',
          difficultyLevel: DifficultyLevel.easy,
          status: QuestionStatus.pendingReview, // Should be promoted to approved
          submittedBy: '00000000-0000-0000-0000-000000000001',
          reviewedBy: null,
          createdAt: DateTime.now(),
        ),
      ];

      // Initial count for Probability
      final chaptersBefore = await repository.fetchChapters(subject: Subject.math);
      final probBefore = chaptersBefore.firstWhere((c) => c.id == targetChapter);
      final initialCount = probBefore.totalQuestions;

      // Admin executes bulk publish
      final published = await repository.bulkPublishQuestions(
        chapterId: targetChapter,
        questions: testQuestions,
        adminId: '00000000-0000-0000-0000-000000000001',
      );

      expect(published.length, equals(1));
      expect(published.first.status, equals(QuestionStatus.approved));

      // Verify that students now see this question in approved questions
      final studentApproved = await repository.fetchApprovedQuestions(
        subject: Subject.math,
        chapterId: targetChapter,
      );
      expect(studentApproved.any((q) => q.id == 'test-prob-1'), isTrue);

      // Verify that chapter count incremented
      final chaptersAfter = await repository.fetchChapters(subject: Subject.math);
      final probAfter = chaptersAfter.firstWhere((c) => c.id == targetChapter);
      expect(probAfter.totalQuestions, equals(initialCount + 1));
    });
  });
}
