import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/theme/app_theme.dart';
import '../../models/chapter.dart';
import '../../widgets/offline_status_badge.dart';
import 'chapter_formula_screen.dart';
import 'chapter_practice_screen.dart';

/// Zero-Friction Chapter Hub for Students
/// Provides two prominent options:
/// 1. Practice Questions & Solutions
/// 2. Chapter Formula Cheat-Sheet
/// Strictly read-only for students with zero generation/modification controls
class ChapterHubScreen extends ConsumerWidget {
  final Chapter chapter;

  const ChapterHubScreen({super.key, required this.chapter});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          chapter.titleEn,
          maxLines: 1,
          overflow: TextOverflow.ellipsis,
        ),
        actions: const [
          Padding(
            padding: EdgeInsets.only(right: 14.0),
            child: Center(child: OfflineStatusBadge()),
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Chapter Header Card
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(18.0),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(16),
                border: Border.all(color: AppTheme.borderSubtle),
                boxShadow: [
                  BoxShadow(
                    color: Colors.black.withOpacity(0.04),
                    blurRadius: 10,
                    offset: const Offset(0, 4),
                  ),
                ],
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                        decoration: BoxDecoration(
                          color: AppTheme.mathColor.withOpacity(0.1),
                          borderRadius: BorderRadius.circular(8),
                        ),
                        child: Text(
                          'Chapter ${chapter.chapterNumber}',
                          style: const TextStyle(
                            color: AppTheme.mathColor,
                            fontWeight: FontWeight.bold,
                            fontSize: 12,
                          ),
                        ),
                      ),
                      const Spacer(),
                      Text(
                        '${chapter.totalQuestions} Questions Available',
                        style: const TextStyle(
                          color: AppTheme.textSecondary,
                          fontSize: 12,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 12),
                  Text(
                    chapter.titleEn,
                    style: const TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.w800,
                      color: AppTheme.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    chapter.titleKn,
                    style: const TextStyle(
                      fontSize: 15,
                      fontWeight: FontWeight.w600,
                      color: Color(0xFF475569),
                    ),
                  ),
                  const SizedBox(height: 10),
                  Text(
                    chapter.summary,
                    style: const TextStyle(
                      fontSize: 13,
                      color: AppTheme.textSecondary,
                      height: 1.45,
                    ),
                  ),
                ],
              ),
            ),

            const SizedBox(height: 24),

            const Text(
              'Select Study Mode',
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
                color: AppTheme.textPrimary,
              ),
            ),
            const SizedBox(height: 14),

            // Option 1: Practice Questions & Solutions
            _buildActionHubCard(
              context: context,
              title: 'Practice Questions & Solutions',
              kannadaTitle: 'ಪ್ರಶ್ನೋತ್ತರಗಳ ಅಭ್ಯಾಸ',
              subtitle: 'NCERT In-Text, Exercise Q&A, and High Order Thinking Skills with step-by-step solutions.',
              icon: Icons.quiz_outlined,
              badgeText: chapter.totalQuestions > 0 ? '${chapter.totalQuestions} Q&A' : 'Pending Review',
              badgeColor: chapter.totalQuestions > 0 ? const Color(0xFF2563EB) : Colors.amber.shade700,
              gradientColors: [const Color(0xFFEFF6FF), const Color(0xFFDBEAFE)],
              borderColor: const Color(0xFF93C5FD),
              iconColor: const Color(0xFF2563EB),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => ChapterPracticeScreen(chapter: chapter),
                  ),
                );
              },
            ),

            const SizedBox(height: 16),

            // Option 2: Chapter Formula Cheat-Sheet
            _buildActionHubCard(
              context: context,
              title: 'Chapter Formula Cheat-Sheet',
              kannadaTitle: 'ಸೂತ್ರಗಳ ಸಂಕ್ಷಿಪ್ತ ಪಟ್ಟಿ',
              subtitle: 'High-yield formulas, identities, theorems, and key exam revision points.',
              icon: Icons.functions_outlined,
              badgeText: '${chapter.formulas.length} Formulas',
              badgeColor: const Color(0xFF059669),
              gradientColors: [const Color(0xFFECFDF5), const Color(0xFFD1FAE5)],
              borderColor: const Color(0xFFA7F3D0),
              iconColor: const Color(0xFF059669),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => ChapterFormulaScreen(chapter: chapter),
                  ),
                );
              },
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildActionHubCard({
    required BuildContext context,
    required String title,
    required String kannadaTitle,
    required String subtitle,
    required IconData icon,
    required String badgeText,
    required Color badgeColor,
    required List<Color> gradientColors,
    required Color borderColor,
    required Color iconColor,
    required VoidCallback onTap,
  }) {
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: gradientColors,
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: borderColor),
      ),
      child: Material(
        color: Colors.transparent,
        child: InkWell(
          borderRadius: BorderRadius.circular(16),
          onTap: onTap,
          child: Padding(
            padding: const EdgeInsets.all(18.0),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  width: 52,
                  height: 52,
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.circular(14),
                    boxShadow: [
                      BoxShadow(
                        color: iconColor.withOpacity(0.15),
                        blurRadius: 8,
                        offset: const Offset(0, 3),
                      ),
                    ],
                  ),
                  child: Icon(icon, color: iconColor, size: 28),
                ),
                const SizedBox(width: 16),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Expanded(
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  title,
                                  style: const TextStyle(
                                    fontSize: 16,
                                    fontWeight: FontWeight.bold,
                                    color: Color(0xFF0F172A),
                                  ),
                                ),
                                const SizedBox(height: 2),
                                Text(
                                  kannadaTitle,
                                  style: TextStyle(
                                    fontSize: 12,
                                    fontWeight: FontWeight.w600,
                                    color: iconColor,
                                  ),
                                ),
                              ],
                            ),
                          ),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                            decoration: BoxDecoration(
                              color: Colors.white,
                              borderRadius: BorderRadius.circular(6),
                            ),
                            child: Text(
                              badgeText,
                              style: TextStyle(
                                fontSize: 11,
                                fontWeight: FontWeight.bold,
                                color: badgeColor,
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 8),
                      Text(
                        subtitle,
                        style: const TextStyle(
                          fontSize: 12.5,
                          color: Color(0xFF334155),
                          height: 1.4,
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(width: 8),
                const Icon(Icons.arrow_forward_ios, size: 16, color: Color(0xFF64748B)),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
