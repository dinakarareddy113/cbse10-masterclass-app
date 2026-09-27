/// Core Application Constants
class AppConstants {
  static const String appName = 'CBSE Class 10 Masterclass';
  static const String appVersion = '1.0.0';
  static const String appTagline = 'Master NCERT Concepts, Board Exam Questions & Timed Quizzes';

  // Hive Box Names
  static const String questionsBox = 'cbse10_cached_questions';
  static const String userBox = 'cbse10_user_session';
  static const String studyMaterialBox = 'cbse10_study_materials';
  static const String syncMetadataBox = 'cbse10_sync_metadata';

  // Cache validity duration
  static const Duration cacheValidityDuration = Duration(hours: 12);

  // Practice Quiz Settings
  static const int defaultQuizDurationSeconds = 600; // 10 minutes
  static const int defaultQuizQuestionCount = 10;
}
