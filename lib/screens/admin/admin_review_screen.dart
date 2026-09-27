import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/theme/app_theme.dart';
import '../../models/question.dart';
import '../../providers/admin_moderation_provider.dart';
import 'admin_bulk_ingest_screen.dart';
import 'admin_guard.dart';
import 'widgets/question_review_card.dart';

class AdminReviewScreen extends ConsumerStatefulWidget {
  const AdminReviewScreen({super.key});

  @override
  ConsumerState<AdminReviewScreen> createState() => _AdminReviewScreenState();
}

class _AdminReviewScreenState extends ConsumerState<AdminReviewScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
    _tabController.addListener(_onTabChanged);
  }

  void _onTabChanged() {
    if (_tabController.indexIsChanging) return;
    final subject = switch (_tabController.index) {
      0 => Subject.math,
      1 => Subject.science,
      2 => Subject.socialScience,
      _ => Subject.math,
    };
    ref.read(adminSelectedSubjectProvider.notifier).state = subject;
    ref.read(adminModerationProvider.notifier).loadPendingQuestions();
  }

  @override
  void dispose() {
    _tabController.removeListener(_onTabChanged);
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Route guard wrapping the review screen
    return AdminGuard(
      child: Scaffold(
        appBar: AppBar(
          title: const Row(
            children: [
              Icon(Icons.verified_user, color: AppTheme.primaryBlue, size: 22),
              SizedBox(width: 8),
              Text('Admin Moderation Hub'),
            ],
          ),
          actions: [
            // Bulk Ingest & Direct Publish Button
            IconButton(
              icon: const Icon(Icons.rocket_launch_outlined, color: Color(0xFF10B981)),
              tooltip: 'Bulk Ingest & Publish to Student Feed',
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const AdminBulkIngestScreen()),
                );
              },
            ),
            // Pipeline Ingestion Trigger Button
            IconButton(
              icon: const Icon(Icons.add_to_photos_outlined),
              tooltip: 'Ingest Sample Q&A via Pipeline',
              onPressed: () {
                final currentSubject = ref.read(adminSelectedSubjectProvider);
                ref.read(adminModerationProvider.notifier).ingestSampleExtractedQuestion(currentSubject);
              },
            ),
            IconButton(
              icon: const Icon(Icons.refresh),
              tooltip: 'Refresh Queue',
              onPressed: () {
                ref.read(adminModerationProvider.notifier).loadPendingQuestions();
              },
            ),
          ],
          bottom: TabBar(
            controller: _tabController,
            labelColor: AppTheme.primaryBlue,
            unselectedLabelColor: AppTheme.textSecondary,
            indicatorColor: AppTheme.primaryBlue,
            indicatorWeight: 3,
            tabs: const [
              Tab(icon: Icon(Icons.calculate_outlined), text: 'Mathematics'),
              Tab(icon: Icon(Icons.science_outlined), text: 'Science'),
              Tab(icon: Icon(Icons.public_outlined), text: 'Social Science'),
            ],
          ),
        ),
        body: Consumer(
          builder: (context, ref, _) {
            final modState = ref.watch(adminModerationProvider);
            final currentSubject = ref.watch(adminSelectedSubjectProvider);

            // Listen for feedback messages
            ref.listen<AdminModerationState>(adminModerationProvider, (prev, next) {
              if (next.successMessage != null && next.successMessage != prev?.successMessage) {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text(next.successMessage!),
                    backgroundColor: AppTheme.successEmerald,
                    behavior: SnackBarBehavior.floating,
                  ),
                );
              }
              if (next.errorMessage != null && next.errorMessage != prev?.errorMessage) {
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text(next.errorMessage!),
                    backgroundColor: AppTheme.dangerRose,
                    behavior: SnackBarBehavior.floating,
                  ),
                );
              }
            });

            if (modState.isLoading) {
              return const Center(child: CircularProgressIndicator());
            }

            final pendingItems = modState.pendingQuestions
                .where((q) => q.subject == currentSubject)
                .toList();

            return Column(
              children: [
                // Ingestion Pipeline Summary Banner
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  color: AppTheme.primaryBlue.withOpacity(0.06),
                  child: Row(
                    children: [
                      const Icon(Icons.bolt, color: AppTheme.primaryBlue, size: 20),
                      const SizedBox(width: 8),
                      Expanded(
                        child: Text(
                          'Moderation Pipeline: ${pendingItems.length} question(s) pending review for ${currentSubject.displayName}.',
                          style: const TextStyle(
                            fontSize: 12.5,
                            fontWeight: FontWeight.w600,
                            color: AppTheme.primaryBlue,
                          ),
                        ),
                      ),
                      TextButton.icon(
                        onPressed: () {
                          ref.read(adminModerationProvider.notifier).ingestSampleExtractedQuestion(currentSubject);
                        },
                        icon: const Icon(Icons.downloading, size: 16),
                        label: const Text('+ Ingest Test Q&A', style: TextStyle(fontSize: 12)),
                      ),
                    ],
                  ),
                ),

                // Question List
                Expanded(
                  child: pendingItems.isEmpty
                      ? Center(
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Container(
                                padding: const EdgeInsets.all(16),
                                decoration: BoxDecoration(
                                  color: AppTheme.successEmerald.withOpacity(0.1),
                                  shape: BoxShape.circle,
                                ),
                                child: const Icon(
                                  Icons.check_circle_outline,
                                  size: 48,
                                  color: AppTheme.successEmerald,
                                ),
                              ),
                              const SizedBox(height: 16),
                              Text(
                                'All caught up for ${currentSubject.displayName}!',
                                style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                              ),
                              const SizedBox(height: 6),
                              const Text(
                                'No pending submissions awaiting review.',
                                style: TextStyle(color: AppTheme.textSecondary, fontSize: 13),
                              ),
                              const SizedBox(height: 20),
                              ElevatedButton.icon(
                                onPressed: () {
                                  ref
                                      .read(adminModerationProvider.notifier)
                                      .ingestSampleExtractedQuestion(currentSubject);
                                },
                                icon: const Icon(Icons.playlist_add),
                                label: const Text('Simulate Ingesting New Item'),
                              ),
                            ],
                          ),
                        )
                      : ListView.builder(
                          padding: const EdgeInsets.all(16),
                          itemCount: pendingItems.length,
                          itemBuilder: (context, index) {
                            final question = pendingItems[index];

                            return QuestionReviewCard(
                              question: question,
                              onApprove: () {
                                ref.read(adminModerationProvider.notifier).approveQuestion(question.id);
                              },
                              onReject: (feedback) {
                                ref
                                    .read(adminModerationProvider.notifier)
                                    .rejectQuestion(question.id, feedback: feedback);
                              },
                              onEditAndApprove: ({
                                required DifficultyLevel updatedDifficulty,
                                required List<QuestionOption>? updatedOptions,
                                required String updatedQuestionText,
                                required String updatedSolution,
                              }) {
                                ref.read(adminModerationProvider.notifier).editAndApproveQuestion(
                                      questionId: question.id,
                                      updatedQuestionText: updatedQuestionText,
                                      updatedOptions: updatedOptions,
                                      updatedSolution: updatedSolution,
                                      updatedDifficulty: updatedDifficulty,
                                    );
                              },
                            );
                          },
                        ),
                ),
              ],
            );
          },
        ),
      ),
    );
  }
}
