import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/theme/app_theme.dart';
import '../../models/chapter.dart';
import '../../providers/chapter_provider.dart';
import '../../widgets/offline_status_badge.dart';
import '../math/chapter_hub_screen.dart';
import 'science_module_screen.dart';

/// Clean, high-performance Chapter Index Screen for CBSE Class 10 Science
/// Displays all 13 NCERT chapters with bilingual titles (English + Kannada) & progress tracking
class ScienceChapterListScreen extends ConsumerWidget {
  const ScienceChapterListScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final chaptersAsync = ref.watch(scienceChaptersProvider);

    return Scaffold(
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: const [
            Text(
              'CBSE Science • ವಿಜ್ಞಾನ',
              style: TextStyle(fontSize: 17, fontWeight: FontWeight.bold),
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
            ),
            Text(
              'Class 10 NCERT • 13 Syllabus Chapters',
              style: TextStyle(fontSize: 11, color: AppTheme.textSecondary, fontWeight: FontWeight.normal),
              maxLines: 1,
              overflow: TextOverflow.ellipsis,
            ),
          ],
        ),
        actions: [
          IconButton(
            tooltip: 'Ray Diagrams & Equations',
            icon: const Icon(Icons.menu_book_outlined, color: AppTheme.scienceColor),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (_) => const ScienceModuleScreen()),
              );
            },
          ),
          const Padding(
            padding: EdgeInsets.only(right: 14.0),
            child: Center(child: OfflineStatusBadge()),
          ),
        ],
      ),
      body: chaptersAsync.when(
        data: (chapters) => _buildChapterList(context, ref, chapters),
        loading: () => const Center(
          child: CircularProgressIndicator(color: AppTheme.scienceColor),
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
                  onPressed: () => ref.invalidate(scienceChaptersProvider),
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
              colors: [Color(0xFF065F46), Color(0xFF059669)],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            borderRadius: BorderRadius.circular(16),
            boxShadow: [
              BoxShadow(
                color: const Color(0xFF059669).withOpacity(0.25),
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
                    'CBSE Class 10 Syllabus',
                    style: TextStyle(
                      fontSize: 13,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFFA7F3D0),
                    ),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                    decoration: BoxDecoration(
                      color: Colors.white.withOpacity(0.2),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Text(
                      '${chapters.length} Chapters',
                      style: const TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                        color: Colors.white,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 6),
              Text(
                '$totalSolved of $totalQuestions Questions Completed (${(overallProgress * 100).toInt()}%)',
                style: const TextStyle(
                  fontSize: 13.5,
                  fontWeight: FontWeight.w600,
                  color: Colors.white,
                ),
              ),
              const SizedBox(height: 10),
              ClipRRect(
                borderRadius: BorderRadius.circular(6),
                child: LinearProgressIndicator(
                  value: overallProgress,
                  backgroundColor: Colors.white.withOpacity(0.2),
                  valueColor: const AlwaysStoppedAnimation<Color>(Colors.white),
                  minHeight: 8,
                ),
              ),
            ],
          ),
        ),

        const SizedBox(height: 20),

        // Quick Lab Explorer banner
        InkWell(
          onTap: () {
            Navigator.push(
              context,
              MaterialPageRoute(builder: (_) => const ScienceModuleScreen()),
            );
          },
          borderRadius: BorderRadius.circular(12),
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
            decoration: BoxDecoration(
              color: const Color(0xFFECFDF5),
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: const Color(0xFFA7F3D0)),
            ),
            child: Row(
              children: const [
                Icon(Icons.biotech, color: AppTheme.scienceColor, size: 22),
                SizedBox(width: 10),
                Expanded(
                  child: Text(
                    'Explore Ray Diagrams, Chemical Balancer & Flowcharts →',
                    style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Color(0xFF065F46)),
                  ),
                ),
              ],
            ),
          ),
        ),

        const SizedBox(height: 16),

        const Text(
          'ALL 13 SYLLABUS CHAPTERS',
          style: TextStyle(
            fontSize: 12,
            fontWeight: FontWeight.bold,
            letterSpacing: 1.1,
            color: AppTheme.textSecondary,
          ),
        ),
        const SizedBox(height: 8),

        // List of all 13 Science Chapters
        ...chapters.map((chapter) => _buildChapterCard(context, ref, chapter)),
      ],
    );
  }

  Widget _buildChapterCard(BuildContext context, WidgetRef ref, Chapter chapter) {
    return Card(
      margin: const EdgeInsets.only(bottom: 12.0),
      child: InkWell(
        onTap: () {
          ref.read(currentChapterProvider.notifier).state = chapter;
          Navigator.push(
            context,
            MaterialPageRoute(
              builder: (_) => ChapterHubScreen(chapter: chapter),
            ),
          );
        },
        borderRadius: BorderRadius.circular(16),
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  // Chapter Number Badge
                  Container(
                    width: 44,
                    height: 44,
                    decoration: BoxDecoration(
                      color: AppTheme.scienceColor.withOpacity(0.1),
                      borderRadius: BorderRadius.circular(12),
                    ),
                    alignment: Alignment.center,
                    child: Text(
                      chapter.paddedNumber,
                      style: const TextStyle(
                        fontSize: 16,
                        fontWeight: FontWeight.w800,
                        color: AppTheme.scienceColor,
                      ),
                    ),
                  ),
                  const SizedBox(width: 14),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          chapter.titleEn,
                          style: const TextStyle(
                            fontSize: 15,
                            fontWeight: FontWeight.bold,
                            color: AppTheme.textPrimary,
                          ),
                          maxLines: 2,
                          overflow: TextOverflow.ellipsis,
                        ),
                        if (chapter.titleKn.isNotEmpty) ...[
                          const SizedBox(height: 2),
                          Text(
                            chapter.titleKn,
                            style: const TextStyle(
                              fontSize: 12.5,
                              fontWeight: FontWeight.w600,
                              color: Color(0xFF64748B),
                            ),
                          ),
                        ],
                      ],
                    ),
                  ),
                  const Icon(
                    Icons.chevron_right,
                    color: Color(0xFF94A3B8),
                  ),
                ],
              ),
              const SizedBox(height: 12),
              // Chapter Summary
              Text(
                chapter.summary,
                style: const TextStyle(
                  fontSize: 12.5,
                  color: AppTheme.textSecondary,
                  height: 1.35,
                ),
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
              ),
              const SizedBox(height: 12),
              // Badges Row
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                    decoration: BoxDecoration(
                      color: AppTheme.scienceColor.withOpacity(0.08),
                      borderRadius: BorderRadius.circular(6),
                      border: Border.all(color: AppTheme.scienceColor.withOpacity(0.2)),
                    ),
                    child: Text(
                      '${chapter.totalQuestions} Questions',
                      style: const TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                        color: AppTheme.scienceColor,
                      ),
                    ),
                  ),
                  const SizedBox(width: 8),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                    decoration: BoxDecoration(
                      color: Colors.grey.shade100,
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Text(
                      '${chapter.formulas.length} Reactions',
                      style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.w600,
                        color: Colors.grey.shade700,
                      ),
                    ),
                  ),
                  const Spacer(),
                  if (chapter.solvedQuestions > 0)
                    Text(
                      chapter.progressFraction,
                      style: const TextStyle(
                        fontSize: 11.5,
                        fontWeight: FontWeight.bold,
                        color: AppTheme.scienceColor,
                      ),
                    ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
