import 'package:flutter/material.dart';

enum Subject {
  math('math', 'Mathematics', Icons.calculate_outlined, Color(0xFF2563EB)),
  science('science', 'Science', Icons.science_outlined, Color(0xFF059669)),
  socialScience('social_science', 'Social Science', Icons.public_outlined, Color(0xFFD97706));

  final String value;
  final String displayName;
  final IconData icon;
  final Color themeColor;

  const Subject(this.value, this.displayName, this.icon, this.themeColor);

  static Subject fromString(String? val) {
    return switch (val?.toLowerCase().trim()) {
      'math' || 'mathematics' => Subject.math,
      'science' => Subject.science,
      'social_science' || 'social science' || 'sst' => Subject.socialScience,
      _ => Subject.math,
    };
  }
}

enum DifficultyLevel {
  easy('easy', 'Easy', Color(0xFF10B981)),
  medium('medium', 'Medium', Color(0xFF3B82F6)),
  hard('hard', 'Hard', Color(0xFFF59E0B)),
  hots('hots', 'HOTS (High Order)', Color(0xFF8B5CF6));

  final String value;
  final String label;
  final Color badgeColor;

  const DifficultyLevel(this.value, this.label, this.badgeColor);

  static DifficultyLevel fromString(String? val) {
    return switch (val?.toLowerCase().trim()) {
      'easy' => DifficultyLevel.easy,
      'medium' => DifficultyLevel.medium,
      'hard' => DifficultyLevel.hard,
      'hots' => DifficultyLevel.hots,
      _ => DifficultyLevel.medium,
    };
  }
}

enum QuestionStatus {
  pendingReview('pending_review', 'Pending Review', Color(0xFFF59E0B)),
  approved('approved', 'Approved', Color(0xFF10B981)),
  rejected('rejected', 'Rejected', Color(0xFFEF4444));

  final String value;
  final String label;
  final Color color;

  const QuestionStatus(this.value, this.label, this.color);

  static QuestionStatus fromString(String? val) {
    return switch (val?.toLowerCase().trim()) {
      'approved' => QuestionStatus.approved,
      'rejected' => QuestionStatus.rejected,
      _ => QuestionStatus.pendingReview,
    };
  }
}

@immutable
class QuestionOption {
  final String id; // 'A', 'B', 'C', 'D'
  final String text;
  final bool isCorrect;

  const QuestionOption({
    required this.id,
    required this.text,
    required this.isCorrect,
  });

  factory QuestionOption.fromJson(Map<String, dynamic> json) {
    return QuestionOption(
      id: json['id'] as String? ?? '',
      text: json['text'] as String? ?? '',
      isCorrect: json['is_correct'] as bool? ?? false,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'text': text,
      'is_correct': isCorrect,
    };
  }

  QuestionOption copyWith({
    String? id,
    String? text,
    bool? isCorrect,
  }) {
    return QuestionOption(
      id: id ?? this.id,
      text: text ?? this.text,
      isCorrect: isCorrect ?? this.isCorrect,
    );
  }
}

@immutable
class Question {
  final String id;
  final Subject subject;
  final String chapterId;
  final String questionText;
  final List<QuestionOption>? options;
  final String stepByStepSolution;
  final DifficultyLevel difficultyLevel;
  final QuestionStatus status;
  final String? rejectionFeedback;
  final String submittedBy;
  final String? reviewedBy;
  final DateTime createdAt;

  const Question({
    required this.id,
    required this.subject,
    required this.chapterId,
    required this.questionText,
    this.options,
    required this.stepByStepSolution,
    required this.difficultyLevel,
    required this.status,
    this.rejectionFeedback,
    required this.submittedBy,
    this.reviewedBy,
    required this.createdAt,
  });

  bool get isMCQ => options != null && options!.isNotEmpty;

  QuestionOption? get correctOption {
    if (!isMCQ) return null;
    try {
      return options!.firstWhere((opt) => opt.isCorrect);
    } catch (_) {
      return options!.isNotEmpty ? options!.first : null;
    }
  }

  factory Question.fromJson(Map<String, dynamic> json) {
    List<QuestionOption>? parsedOptions;
    if (json['options'] != null) {
      if (json['options'] is List) {
        parsedOptions = (json['options'] as List<dynamic>)
            .map((item) => QuestionOption.fromJson(Map<String, dynamic>.from(item as Map)))
            .toList();
      }
    }

    return Question(
      id: json['id'] as String? ?? '',
      subject: Subject.fromString(json['subject'] as String?),
      chapterId: json['chapter_id'] as String? ?? '',
      questionText: json['question_text'] as String? ?? '',
      options: parsedOptions,
      stepByStepSolution: json['step_by_step_solution'] as String? ?? '',
      difficultyLevel: DifficultyLevel.fromString(json['difficulty_level'] as String?),
      status: QuestionStatus.fromString(json['status'] as String?),
      rejectionFeedback: json['rejection_feedback'] as String?,
      submittedBy: json['submitted_by'] as String? ?? '',
      reviewedBy: json['reviewed_by'] as String?,
      createdAt: json['created_at'] != null
          ? DateTime.tryParse(json['created_at'].toString()) ?? DateTime.now()
          : DateTime.now(),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'subject': subject.value,
      'chapter_id': chapterId,
      'question_text': questionText,
      'options': options?.map((opt) => opt.toJson()).toList(),
      'step_by_step_solution': stepByStepSolution,
      'difficulty_level': difficultyLevel.value,
      'status': status.value,
      'rejection_feedback': rejectionFeedback,
      'submitted_by': submittedBy,
      'reviewed_by': reviewedBy,
      'created_at': createdAt.toIso8601String(),
    };
  }

  Question copyWith({
    String? id,
    Subject? subject,
    String? chapterId,
    String? questionText,
    List<QuestionOption>? options,
    String? stepByStepSolution,
    DifficultyLevel? difficultyLevel,
    QuestionStatus? status,
    String? rejectionFeedback,
    String? submittedBy,
    String? reviewedBy,
    DateTime? createdAt,
  }) {
    return Question(
      id: id ?? this.id,
      subject: subject ?? this.subject,
      chapterId: chapterId ?? this.chapterId,
      questionText: questionText ?? this.questionText,
      options: options ?? this.options,
      stepByStepSolution: stepByStepSolution ?? this.stepByStepSolution,
      difficultyLevel: difficultyLevel ?? this.difficultyLevel,
      status: status ?? this.status,
      rejectionFeedback: rejectionFeedback ?? this.rejectionFeedback,
      submittedBy: submittedBy ?? this.submittedBy,
      reviewedBy: reviewedBy ?? this.reviewedBy,
      createdAt: createdAt ?? this.createdAt,
    );
  }
}
