import 'package:flutter_test/flutter_test.dart';
import 'package:cbse_class10_masterclass/core/constants/cbse_curriculum.dart';
import 'package:cbse_class10_masterclass/core/utils/formula_formatter.dart';
import 'package:cbse_class10_masterclass/models/question.dart';
import 'package:cbse_class10_masterclass/services/question_repository.dart';

void main() {
  group('CBSE Class 10 Science & SST Curriculum Parity Tests', () {
    test('CbseCurriculum defines all 13 Science chapters', () {
      expect(CbseCurriculum.scienceChapters.length, equals(13));
      final ch3 = CbseCurriculum.scienceChapters.firstWhere(
        (c) => c['id'] == 'sci_ch_03_metals_non_metals',
      );
      expect(ch3['title_en'], equals('Metals and Non-metals'));
      expect(ch3['chapter_number'], equals(3));
    });

    test('CbseCurriculum defines all 7 Social Science chapters', () {
      expect(CbseCurriculum.sstChapters.length, equals(7));
      final ch1 = CbseCurriculum.sstChapters.firstWhere(
        (c) => c['id'] == 'sst_hist_ch_01_europe',
      );
      expect(ch1['chapter_number'], equals(1));
    });
  });

  group('Science Ingestion & Question Repository Tests', () {
    test('QuestionRepository loads all 50 questions for Science Chapter 3', () async {
      final repo = QuestionRepository();
      final ch3Questions = await repo.fetchApprovedQuestions(
        subject: Subject.science,
        chapterId: 'sci_ch_03_metals_non_metals',
      );

      expect(ch3Questions.length, equals(50));
      for (final q in ch3Questions) {
        expect(q.subject, equals(Subject.science));
        expect(q.chapterId, equals('sci_ch_03_metals_non_metals'));
        expect(q.questionText.isNotEmpty, isTrue);
        expect(q.stepByStepSolution.isNotEmpty, isTrue);
        expect(q.options, isNotNull);
        expect(q.options!.length, greaterThanOrEqualTo(2));
      }
    });

    test('QuestionRepository loads Science Chapters 2, 4, and 5 data', () async {
      final repo = QuestionRepository();
      final ch2 = await repo.fetchApprovedQuestions(
        subject: Subject.science,
        chapterId: 'sci_ch_02_acids_bases_salts',
      );
      final ch4 = await repo.fetchApprovedQuestions(
        subject: Subject.science,
        chapterId: 'sci_ch_04_carbon_compounds',
      );
      final ch5 = await repo.fetchApprovedQuestions(
        subject: Subject.science,
        chapterId: 'sci_ch_05_life_processes',
      );

      expect(ch2.length, equals(37));
      expect(ch4.length, equals(36));
      expect(ch5.length, equals(31));
    });

    test('fetchChapters calculates accurate question count for Science', () async {
      final repo = QuestionRepository();
      final chapters = await repo.fetchChapters(subject: Subject.science);

      expect(chapters.length, equals(13));
      final ch3 = chapters.firstWhere((c) => c.id == 'sci_ch_03_metals_non_metals');
      expect(ch3.totalQuestions, equals(50));
    });
  });

  group('FormulaFormatter & Chemical Notation Polish Tests', () {
    test('Transforms subscripts and arrows cleanly', () {
      final raw = '2H_2 + O_2 -> 2H_2O';
      final formatted = FormulaFormatter.format(raw);
      expect(formatted, contains('₂'));
      expect(formatted, contains('→'));
    });

    test('Strips raw LaTeX delimiters and formats symbols', () {
      final raw = r'Reaction: $\text{Mg} + \text{O}_2 \rightarrow \text{MgO}$';
      final formatted = FormulaFormatter.format(raw);
      expect(formatted.contains(r'$'), isFalse);
      expect(formatted.contains(r'\text'), isFalse);
      expect(formatted, contains('Mg'));
      expect(formatted, contains('O₂'));
      expect(formatted, contains('→'));
      expect(formatted, contains('MgO'));
    });

    test('Formats degree signs and exponents correctly', () {
      final raw = r'Temperature is 100^\circ C and area is x^2';
      final formatted = FormulaFormatter.format(raw);
      expect(formatted, contains('°'));
      expect(formatted, contains('²'));
    });
  });
}
