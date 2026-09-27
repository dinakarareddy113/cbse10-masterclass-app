import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/question.dart';
import '../services/question_repository.dart';
import 'auth_provider.dart';
import 'questions_provider.dart';

/// Admin subject filter tab provider
final adminSelectedSubjectProvider = StateProvider<Subject>((ref) => Subject.math);

class AdminModerationState {
  final List<Question> pendingQuestions;
  final bool isLoading;
  final String? errorMessage;
  final String? successMessage;

  const AdminModerationState({
    required this.pendingQuestions,
    this.isLoading = false,
    this.errorMessage,
    this.successMessage,
  });

  AdminModerationState copyWith({
    List<Question>? pendingQuestions,
    bool? isLoading,
    String? errorMessage,
    String? successMessage,
  }) {
    return AdminModerationState(
      pendingQuestions: pendingQuestions ?? this.pendingQuestions,
      isLoading: isLoading ?? this.isLoading,
      errorMessage: errorMessage,
      successMessage: successMessage,
    );
  }
}

class AdminModerationNotifier extends StateNotifier<AdminModerationState> {
  final QuestionRepository _repository;
  final Ref _ref;

  AdminModerationNotifier(this._repository, this._ref)
      : super(const AdminModerationState(pendingQuestions: [], isLoading: true)) {
    loadPendingQuestions();
  }

  Future<void> loadPendingQuestions() async {
    final subject = _ref.read(adminSelectedSubjectProvider);
    state = state.copyWith(isLoading: true, errorMessage: null);
    try {
      final items = await _repository.fetchPendingQuestions(subject: subject);
      state = state.copyWith(pendingQuestions: items, isLoading: false);
    } catch (e) {
      state = state.copyWith(
        isLoading: false,
        errorMessage: 'Failed to fetch pending questions: $e',
      );
    }
  }

  /// Approve Question Action: sets status = 'approved', reviewed_by = current_admin_id
  Future<bool> approveQuestion(String questionId) async {
    final currentAdmin = _ref.read(authNotifierProvider).value;
    final adminId = currentAdmin?.id ?? '00000000-0000-0000-0000-000000000001';

    try {
      final success = await _repository.approveQuestion(
        questionId: questionId,
        adminId: adminId,
      );

      if (success) {
        final updatedList = state.pendingQuestions.where((q) => q.id != questionId).toList();
        state = state.copyWith(
          pendingQuestions: updatedList,
          successMessage: 'Question approved and published live to students!',
        );
        // Invalidate student feed so they immediately see the new question
        _ref.invalidate(approvedQuestionsProvider);
        return true;
      }
      return false;
    } catch (e) {
      state = state.copyWith(errorMessage: 'Approval failed: $e');
      return false;
    }
  }

  /// Reject Question Action: sets status = 'rejected' with optional feedback note
  Future<bool> rejectQuestion(String questionId, {String? feedback}) async {
    final currentAdmin = _ref.read(authNotifierProvider).value;
    final adminId = currentAdmin?.id ?? '00000000-0000-0000-0000-000000000001';

    try {
      final success = await _repository.rejectQuestion(
        questionId: questionId,
        adminId: adminId,
        feedback: feedback,
      );

      if (success) {
        final updatedList = state.pendingQuestions.where((q) => q.id != questionId).toList();
        state = state.copyWith(
          pendingQuestions: updatedList,
          successMessage: 'Question rejected with feedback saved.',
        );
        return true;
      }
      return false;
    } catch (e) {
      state = state.copyWith(errorMessage: 'Rejection failed: $e');
      return false;
    }
  }

  /// Edit & Approve Modal Action: updates fields & approves in a single transaction
  Future<bool> editAndApproveQuestion({
    required String questionId,
    required String updatedQuestionText,
    required List<QuestionOption>? updatedOptions,
    required String updatedSolution,
    required DifficultyLevel updatedDifficulty,
  }) async {
    final currentAdmin = _ref.read(authNotifierProvider).value;
    final adminId = currentAdmin?.id ?? '00000000-0000-0000-0000-000000000001';

    try {
      final success = await _repository.editAndApproveQuestion(
        questionId: questionId,
        adminId: adminId,
        updatedQuestionText: updatedQuestionText,
        updatedOptions: updatedOptions,
        updatedSolution: updatedSolution,
        updatedDifficulty: updatedDifficulty,
      );

      if (success) {
        final updatedList = state.pendingQuestions.where((q) => q.id != questionId).toList();
        state = state.copyWith(
          pendingQuestions: updatedList,
          successMessage: 'Changes saved & question published successfully!',
        );
        _ref.invalidate(approvedQuestionsProvider);
        return true;
      }
      return false;
    } catch (e) {
      state = state.copyWith(errorMessage: 'Edit & Approve failed: $e');
      return false;
    }
  }

  /// Pipeline Demo: Ingest sample question into pending queue
  Future<void> ingestSampleExtractedQuestion(Subject subject) async {
    final currentAdmin = _ref.read(authNotifierProvider).value;
    final submittedBy = currentAdmin?.id ?? '00000000-0000-0000-0000-000000000002';

    final sampleQuestion = switch (subject) {
      Subject.math => await _repository.submitQuestion(
          subject: Subject.math,
          chapterId: 'ch_06_triangles',
          questionText:
              'In ΔABC, DE || BC. If AD = 3 cm, DB = 5 cm, and AE = 4.5 cm, calculate the length of EC using Thales Theorem.',
          options: [
            const QuestionOption(id: 'A', text: '6.5 cm', isCorrect: false),
            const QuestionOption(id: 'B', text: '7.5 cm', isCorrect: true),
            const QuestionOption(id: 'C', text: '8.0 cm', isCorrect: false),
            const QuestionOption(id: 'D', text: '5.5 cm', isCorrect: false),
          ],
          stepByStepSolution:
              'Step 1: By Thales Theorem (BPT), AD/DB = AE/EC.\nStep 2: Substitute values: 3 / 5 = 4.5 / EC.\nStep 3: Cross-multiply: 3 * EC = 5 * 4.5 = 22.5.\nStep 4: EC = 22.5 / 3 = 7.5 cm.',
          difficultyLevel: DifficultyLevel.medium,
          submittedBy: submittedBy,
        ),
      Subject.science => await _repository.submitQuestion(
          subject: Subject.science,
          chapterId: 'sci_ch_12_electricity',
          questionText:
              'A piece of wire having resistance R is cut into 5 equal parts. These parts are then connected in parallel. If the equivalent resistance of this combination is R\', what is the ratio R / R\'?',
          options: [
            const QuestionOption(id: 'A', text: '1/25', isCorrect: false),
            const QuestionOption(id: 'B', text: '1/5', isCorrect: false),
            const QuestionOption(id: 'C', text: '5', isCorrect: false),
            const QuestionOption(id: 'D', text: '25', isCorrect: true),
          ],
          stepByStepSolution:
              'Step 1: Resistance of each cut piece = r = R/5.\nStep 2: Connected in parallel: 1/R\' = 1/r + 1/r + 1/r + 1/r + 1/r = 5/r.\nStep 3: 1/R\' = 5 / (R/5) = 25/R.\nStep 4: Therefore, R / R\' = 25.',
          difficultyLevel: DifficultyLevel.hots,
          submittedBy: submittedBy,
        ),
      Subject.socialScience => await _repository.submitQuestion(
          subject: Subject.socialScience,
          chapterId: 'sst_eco_ch_03_money_and_credit',
          questionText:
              'Which body in India supervises the functioning of formal sources of loans including commercial banks?',
          options: [
            const QuestionOption(id: 'A', text: 'State Bank of India', isCorrect: false),
            const QuestionOption(id: 'B', text: 'Reserve Bank of India (RBI)', isCorrect: true),
            const QuestionOption(id: 'C', text: 'Ministry of Finance', isCorrect: false),
            const QuestionOption(id: 'D', text: 'NITI Aayog', isCorrect: false),
          ],
          stepByStepSolution:
              'Step 1: The Reserve Bank of India (RBI) monitors the Cash Reserve Ratio (CRR) maintained by commercial banks.\nStep 2: RBI ensures banks give loans not just to profit-making businesses but also to small cultivators, cottage industries, and small borrowers.',
          difficultyLevel: DifficultyLevel.easy,
          submittedBy: submittedBy,
        ),
    };

    final updated = [sampleQuestion, ...state.pendingQuestions];
    state = state.copyWith(
      pendingQuestions: updated,
      successMessage: 'Ingestion pipeline: New question pushed to pending queue!',
    );
  }
}

final adminModerationProvider =
    StateNotifierProvider<AdminModerationNotifier, AdminModerationState>((ref) {
  final repository = ref.watch(questionRepositoryProvider);
  return AdminModerationNotifier(repository, ref);
});
