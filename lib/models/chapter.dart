import 'package:flutter/material.dart';
import 'question.dart';

@immutable
class Chapter {
  final String id;
  final int chapterNumber;
  final Subject subject;
  final String titleEn;
  final String titleKn;
  final String summary;
  final List<String> formulas;
  final int totalQuestions;
  final int solvedQuestions;

  const Chapter({
    required this.id,
    required this.chapterNumber,
    required this.subject,
    required this.titleEn,
    required this.titleKn,
    required this.summary,
    required this.formulas,
    this.totalQuestions = 0,
    this.solvedQuestions = 0,
  });

  /// Dual-script bilingual display title
  String get bilingualTitle => '$titleEn • $titleKn';

  /// Padded chapter number string (e.g. "01", "12")
  String get paddedNumber => chapterNumber.toString().padLeft(2, '0');

  /// Completion percentage from 0.0 to 1.0
  double get progressPercentage {
    if (totalQuestions <= 0) return 0.0;
    final ratio = solvedQuestions / totalQuestions;
    return ratio > 1.0 ? 1.0 : ratio;
  }

  /// Formatted progress fraction e.g. "3/5 Solved" or "0 Solved"
  String get progressFraction => '$solvedQuestions / $totalQuestions Solved';

  factory Chapter.fromJson(Map<String, dynamic> json) {
    List<String> parsedFormulas = [];
    if (json['formulas'] != null) {
      if (json['formulas'] is List) {
        parsedFormulas = (json['formulas'] as List).map((f) => f.toString()).toList();
      }
    }

    return Chapter(
      id: json['id'] as String? ?? '',
      chapterNumber: (json['chapter_number'] as num?)?.toInt() ?? 1,
      subject: Subject.fromString(json['subject'] as String?),
      titleEn: json['title_en'] as String? ?? '',
      titleKn: json['title_kn'] as String? ?? '',
      summary: json['summary'] as String? ?? '',
      formulas: parsedFormulas,
      totalQuestions: (json['total_questions'] as num?)?.toInt() ?? 0,
      solvedQuestions: (json['solved_questions'] as num?)?.toInt() ?? 0,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'chapter_number': chapterNumber,
      'subject': subject.value,
      'title_en': titleEn,
      'title_kn': titleKn,
      'summary': summary,
      'formulas': formulas,
      'total_questions': totalQuestions,
      'solved_questions': solvedQuestions,
    };
  }

  Chapter copyWith({
    String? id,
    int? chapterNumber,
    Subject? subject,
    String? titleEn,
    String? titleKn,
    String? summary,
    List<String>? formulas,
    int? totalQuestions,
    int? solvedQuestions,
  }) {
    return Chapter(
      id: id ?? this.id,
      chapterNumber: chapterNumber ?? this.chapterNumber,
      subject: subject ?? this.subject,
      titleEn: titleEn ?? this.titleEn,
      titleKn: titleKn ?? this.titleKn,
      summary: summary ?? this.summary,
      formulas: formulas ?? this.formulas,
      totalQuestions: totalQuestions ?? this.totalQuestions,
      solvedQuestions: solvedQuestions ?? this.solvedQuestions,
    );
  }
}
