/// Supabase URL and Configuration Constants
class SupabaseConstants {
  // Production or Local Emulation Supabase URL & Anon Key
  // Default values can be overridden via environment variables
  static const String supabaseUrl = String.fromEnvironment(
    'SUPABASE_URL',
    defaultValue: 'https://cbse10-masterclass.supabase.co',
  );

  static const String supabaseAnonKey = String.fromEnvironment(
    'SUPABASE_ANON_KEY',
    defaultValue: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.e30.demo-anon-key',
  );

  // Table Names
  static const String profilesTable = 'profiles';
  static const String questionsTable = 'questions';

  // Questions Columns
  static const String colId = 'id';
  static const String colSubject = 'subject';
  static const String colChapterId = 'chapter_id';
  static const String colQuestionText = 'question_text';
  static const String colOptions = 'options';
  static const String colStepByStepSolution = 'step_by_step_solution';
  static const String colDifficultyLevel = 'difficulty_level';
  static const String colStatus = 'status';
  static const String colRejectionFeedback = 'rejection_feedback';
  static const String colSubmittedBy = 'submitted_by';
  static const String colReviewedBy = 'reviewed_by';
  static const String colCreatedAt = 'created_at';

  // Profiles Columns
  static const String colProfileFullName = 'full_name';
  static const String colProfileRole = 'role';
}
