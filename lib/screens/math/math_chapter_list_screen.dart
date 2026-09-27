import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/theme/app_theme.dart';
import '../../models/chapter.dart';
import '../../providers/chapter_provider.dart';
import '../../widgets/offline_status_badge.dart';
import 'chapter_hub_screen.dart';

/// Clean, high-performance Chapter Index Screen for CBSE Class 10 Mathematics
/// Displays all 14 NCERT chapters with bilingual titles (English + Kannada) & progress tracking
class MathChapterListScreen extends ConsumerWidget {
  const MathChapterListScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final chaptersAsync = ref.watch(mathChaptersProvider);

    return Scaffold(
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: const [
            Text(
              'CBSE Mathematics • ಗಣಿತ',
              style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold),
            ),
            Text(
              'Class 10 NCERT • 14 Syllabus Chapters',
              style: TextStyle(fontSize: 11, color: AppTheme.textSecondary, fontWeight: FontWeight.normal),
            ),
          ],
        ),
        actions: const [
          Padding(
            padding: EdgeInsets.only(right: 14.0),
            child: Center(child: OfflineStatusBadge()),
          ),
        ],
      ),
      body: chaptersAsync.when(
        data: (chapters) => _buildChapterList(context, ref, chapters),
        loading: () => const Center(
          child: CircularProgressIndicator(color: AppTheme.mathColor),
        ),
        error: (e, st) => Center(
          child: Padding(
            padding: const EdgeInsets.all(24.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Icon(Icons.error_outline, size: 48, color: AppTheme.dangerRose),
                const SizedBox(height: 12),
                Text('Error loading syllabus: $e', textAlign: TextAlign.center),
                const SizedBox(height: 12),
                ElevatedButton(
                  onPressed: () => ref.invalidate(mathChaptersProvider),
                  child: const Text('Retry'),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildChapterList(BuildContext context, WidgetRef ref, List<Chapter> chapters) {
    // Calculate global stats across all 14 chapters
    final totalQuestions = chapters.fold<int>(0, (sum, ch) => sum + ch.totalQuestions);
    final totalSolved = chapters.fold<int>(0, (sum, ch) => sum + ch.solvedQuestions);
    final overallProgress = totalQuestions > 0 ? (totalSolved / totalQuestions) : 0.0;

    return ListView(
      padding: const EdgeInsets.all(16.0),
      children: [
        // Syllabus Header Overview Card
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(16.0),
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              colors: [Color(0xFF1E3A8A), Color(0xFF2563EB)],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            borderRadius: BorderRadius.circular(16),
            boxShadow: [
              BoxShadow(
                color: const Color(0xFF2563EB).withOpacity(0.25),
                blurRadius: 10,
                offset: const Offset(0, 4),
              ),
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Text(
                    'Class 10 Board Curriculum',
                    style: TextStyle(
                      color: Colors.white,
                      fontSize: 15,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.2),
                      borderRadius: BorderRadius.circular(20),
                    ),
                    child: Text(
                      '${chapters.length} Chapters',
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 11.5,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 12),
              Row(
                children: [
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          '$totalSolved / $totalQuestions Questions Mastered',
                          style: const TextStyle(color: Colors.white70, fontSize: 12),
                        ),
                        const SizedBox(height: 6),
                        ClipRRect(
                          borderRadius: BorderRadius.circular(4),
                          child: LinearProgressIndicator(
                            value: overallProgress,
                            backgroundColor: Colors.white.withOpacity(0.2),
                            valueColor: const AlwaysStoppedAnimation<Color>(Color(0xFF34D399)),
                            minHeight: 6,
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(width: 16),
                  Text(
                    '${(overallProgress * 100).toInt()}%',
                    style: const TextStyle(
                      color: Colors.white,
                      fontSize: 18,
                      fontWeight: FontWeight.w800,
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),

        const SizedBox(height: 18),

        const Text(
          'Mathematics Chapters • ಅಧ್ಯಾಯಗಳು',
          style: TextStyle(
            fontSize: 15,
            fontWeight: FontWeight.bold,
            color: AppTheme.textPrimary,
          ),
        ),
        const SizedBox(height: 10),

        // 14 Chapter Cards
        ...chapters.map((chapter) => _buildChapterCard(context, ref, chapter)),
      ],
    );
  }

  Widget _buildChapterCard(BuildContext context, WidgetRef ref, Chapter chapter) {
    final hasQuestions = chapter.totalQuestions > 0;
    final progress = chapter.progressPercentage;

    return Card(
      margin: const EdgeInsets.only(bottom: 12),
      elevation: 0,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: const BorderSide(color: AppTheme.borderSubtle),
      ),
      child: InkWell(
        borderRadius: BorderRadius.circular(14),
        onTap: () {
          // Frictionless Navigation to Chapter Hub
          ref.read(currentChapterProvider.notifier).state = chapter;
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (_) => ChapterHubScreen(chapter: chapter),
            ),
          );
        },
        child: Padding(
          padding: const EdgeInsets.all(14.0),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Chapter Number Badge
              Container(
                width: 44,
                height: 44,
                decoration: BoxDecoration(
                  color: AppTheme.mathColor.withOpacity(0.1),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: AppTheme.mathColor.withOpacity(0.2)),
                ),
                child: Center(
                  child: Text(
                    chapter.paddedNumber,
                    style: const TextStyle(
                      color: AppTheme.mathColor,
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),

              const SizedBox(width: 14),

              // Title and Badges
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Bilingual Title: English Title
                    Text(
                      chapter.titleEn,
                      style: const TextStyle(
                        fontSize: 15,
                        fontWeight: FontWeight.w700,
                        color: AppTheme.textPrimary,
                      ),
                    ),
                    const SizedBox(height: 2),

                    // Bilingual Title: Kannada Regional Title
                    Text(
                      chapter.titleKn,
                      style: const TextStyle(
                        fontSize: 12.5,
                        fontWeight: FontWeight.w600,
                        color: Color(0xFF475569),
                      ),
                    ),

                    const SizedBox(height: 8),

                    // Badges Row: Question count & Progress
                    Row(
                      children: [
                        // Question Count Badge
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2.5),
                          decoration: BoxDecoration(
                            color: hasQuestions
                                ? AppTheme.mathColor.withOpacity(0.08)
                                : Colors.amber.shade50,
                            borderRadius: BorderRadius.circular(6),
                            border: Border.all(
                              color: hasQuestions
                                  ? AppTheme.mathColor.withOpacity(0.2)
                                  : Colors.amber.shade200,
                            ),
                          ),
                          child: Text(
                            hasQuestions ? '${chapter.totalQuestions} Questions' : 'Seeding Soon',
                            style: TextStyle(
                              fontSize: 10.5,
                              fontWeight: FontWeight.bold,
                              color: hasQuestions ? AppTheme.mathColor : Colors.amber.shade800,
                            ),
                          ),
                        ),

                        const SizedBox(width: 8),

                        // Formulas badge
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2.5),
                          decoration: BoxDecoration(
                            color: const Color(0xFFF1F5F9),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: Text(
                            '${chapter.formulas.length} Formulas',
                            style: const TextStyle(
                              fontSize: 10.5,
                              fontWeight: FontWeight.w600,
                              color: Color(0xFF64748B),
                            ),
                          ),
                        ),

                        if (hasQuestions) ...[
                          const Spacer(),
                          Text(
                            chapter.progressFraction,
                            style: const TextStyle(
                              fontSize: 10.5,
                              fontWeight: FontWeight.w600,
                              color: Color(0xFF059669),
                            ),
                          ),
                        ],
                      ],
                    ),

                    if (hasQuestions && progress > 0) ...[
                      const SizedBox(height: 6),
                      ClipRRect(
                        borderRadius: BorderRadius.circular(3),
                        child: LinearProgressIndicator(
                          value: progress,
                          backgroundColor: Colors.grey.shade200,
                          valueColor: const AlwaysStoppedAnimation<Color>(Color(0xFF059669)),
                          minHeight: 4,
                        ),
                      ),
                    ],
                  ],
                ),
              ),

              const SizedBox(width: 6),
              const Icon(Icons.chevron_right, color: Colors.grey, size: 20),
            ],
          ),
        ),
      ),
    );
  }
}
