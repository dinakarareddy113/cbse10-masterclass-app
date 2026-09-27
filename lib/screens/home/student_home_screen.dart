import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/theme/app_theme.dart';
import '../../models/question.dart';
import '../../models/user_profile.dart';
import '../../providers/auth_provider.dart';
import '../../widgets/offline_status_badge.dart';
import '../admin/admin_review_screen.dart';
import '../math/math_chapter_list_screen.dart';
import '../quiz/quiz_screen.dart';
import '../science/science_module_screen.dart';
import '../social_science/social_science_module_screen.dart';

class StudentHomeScreen extends ConsumerWidget {
  const StudentHomeScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final authProfile = ref.watch(authNotifierProvider).value;
    final isAdmin = ref.watch(isAdminProvider);

    return Scaffold(
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('CBSE Class 10 Masterclass', style: TextStyle(fontSize: 18, fontWeight: FontWeight.w800)),
            Text(
              'Board Exam Success Suite • NCERT 2026',
              style: TextStyle(fontSize: 11, color: Colors.grey.shade600, fontWeight: FontWeight.normal),
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
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // User Persona & Role Bar
            _buildUserPersonaBanner(context, ref, authProfile),
            const SizedBox(height: 16),

            // Admin Moderation Hub Banner (Visible to Admin role or prompt to switch)
            if (isAdmin)
              _buildAdminModerationBanner(context)
            else
              _buildTeacherAdminTesterBanner(context, ref),

            const SizedBox(height: 20),

            // Section Title
            const Text(
              'Core Academic Disciplines',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: AppTheme.textPrimary,
                letterSpacing: -0.3,
              ),
            ),
            const SizedBox(height: 12),

            // Subject Cards
            _buildSubjectCard(
              context: context,
              title: 'Mathematics • ಗಣಿತ',
              subtitle: '14 Chapters • Bilingual Index • Practice Q&A • Formula Cheat-Sheets',
              icon: Icons.calculate_outlined,
              accentColor: AppTheme.mathColor,
              badgeText: '14 Chapters • NCERT',
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const MathChapterListScreen()),
                );
              },
            ),
            _buildSubjectCard(
              context: context,
              title: 'Science',
              subtitle: 'Physics Ray Diagrams • Chemistry Balancer • Biology Flowcharts',
              icon: Icons.science_outlined,
              accentColor: AppTheme.scienceColor,
              badgeText: 'Physics • Chemistry • Biology',
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const ScienceModuleScreen()),
                );
              },
            ),
            _buildSubjectCard(
              context: context,
              title: 'Social Science',
              subtitle: 'Nationalism Timelines • Map Pointing Guide • Civics Amendments',
              icon: Icons.public_outlined,
              accentColor: AppTheme.socialScienceColor,
              badgeText: 'History • Geography • Civics',
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (_) => const SocialScienceModuleScreen()),
                );
              },
            ),

            const SizedBox(height: 24),

            // Timed Practice Engine Quick Launcher
            _buildPracticeQuizLauncher(context),
            const SizedBox(height: 24),
          ],
        ),
      ),
    );
  }

  Widget _buildUserPersonaBanner(BuildContext context, WidgetRef ref, UserProfile? profile) {
    final role = profile?.role ?? UserRole.student;
    final fullName = profile?.fullName ?? 'Aarav Sharma';
    final classLevel = profile?.classLevel ?? 'Class 10';
    final schoolName = profile?.schoolName ?? 'Delhi Public School, Bangalore';

    return Column(
      children: [
        // Student Profile Hero Banner
        Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              colors: [Color(0xFF1E3A8A), Color(0xFF1E1B4B)],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
            borderRadius: BorderRadius.circular(20),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withOpacity(0.12),
                blurRadius: 10,
                offset: const Offset(0, 4),
              ),
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  CircleAvatar(
                    radius: 22,
                    backgroundColor: Colors.white.withOpacity(0.2),
                    child: Text(
                      fullName.isNotEmpty ? fullName[0].toUpperCase() : 'S',
                      style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 18),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text(
                          '👋 Welcome Back,',
                          style: TextStyle(color: Color(0xFF93C5FD), fontSize: 11.5, fontWeight: FontWeight.w600),
                        ),
                        Text(
                          fullName,
                          style: const TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 16),
                          overflow: TextOverflow.ellipsis,
                        ),
                      ],
                    ),
                  ),
                  // Persona Switcher Popup Menu
                  PopupMenuButton<UserRole>(
                    tooltip: 'Switch Persona Role',
                    initialValue: role,
                    onSelected: (newRole) {
                      ref.read(authNotifierProvider.notifier).switchRole(newRole);
                    },
                    itemBuilder: (ctx) => [
                      const PopupMenuItem(
                        value: UserRole.student,
                        child: Row(
                          children: [
                            Icon(Icons.person, size: 18, color: AppTheme.primaryBlue),
                            SizedBox(width: 8),
                            Text('Student Persona'),
                          ],
                        ),
                      ),
                      const PopupMenuItem(
                        value: UserRole.teacher,
                        child: Row(
                          children: [
                            Icon(Icons.school, size: 18, color: AppTheme.scienceColor),
                            SizedBox(width: 8),
                            Text('Teacher Persona'),
                          ],
                        ),
                      ),
                      const PopupMenuItem(
                        value: UserRole.admin,
                        child: Row(
                          children: [
                            Icon(Icons.admin_panel_settings, size: 18, color: AppTheme.hotsColor),
                            SizedBox(width: 8),
                            Text('Admin Persona'),
                          ],
                        ),
                      ),
                    ],
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                      decoration: BoxDecoration(
                        color: Colors.white.withOpacity(0.15),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      child: Row(
                        children: [
                          Text(role.value.toUpperCase(), style: const TextStyle(fontSize: 10.5, fontWeight: FontWeight.bold, color: Colors.white)),
                          const Icon(Icons.arrow_drop_down, size: 16, color: Colors.white),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 12),
              // Student Badges
              Wrap(
                spacing: 6,
                runSpacing: 6,
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                    decoration: BoxDecoration(
                      color: Colors.blue.withOpacity(0.25),
                      borderRadius: BorderRadius.circular(8),
                      border: Border.all(color: Colors.blue.shade300.withOpacity(0.4)),
                    ),
                    child: Text('🎓 $classLevel', style: const TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold)),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                    decoration: BoxDecoration(
                      color: Colors.indigo.withOpacity(0.25),
                      borderRadius: BorderRadius.circular(8),
                      border: Border.all(color: Colors.indigo.shade300.withOpacity(0.4)),
                    ),
                    child: Text('🏫 $schoolName', style: const TextStyle(color: Color(0xFFE0E7FF), fontSize: 11)),
                  ),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                    decoration: BoxDecoration(
                      color: const Color(0xFF10B981).withOpacity(0.25),
                      borderRadius: BorderRadius.circular(8),
                      border: Border.all(color: Colors.greenAccent.withOpacity(0.4)),
                    ),
                    child: const Text('✓ Board Ready', style: TextStyle(color: Color(0xFF86EFAC), fontSize: 11, fontWeight: FontWeight.bold)),
                  ),
                ],
              ),
            ],
          ),
        ),
        const SizedBox(height: 12),

        // Academic Learning KPIs 2x2 Grid
        Row(
          children: [
            Expanded(
              child: _buildKpiCard(
                title: '🎯 Board Target',
                value: '100 / 100',
                subtitle: 'Centum Grade Aim',
                accentColor: AppTheme.primaryBlue,
              ),
            ),
            const SizedBox(width: 8),
            Expanded(
              child: _buildKpiCard(
                title: '📊 Accuracy',
                value: '95%',
                subtitle: 'Practice First-Try',
                accentColor: const Color(0xFF16A34A),
              ),
            ),
          ],
        ),
        const SizedBox(height: 8),
        Row(
          children: [
            Expanded(
              child: _buildKpiCard(
                title: '🏆 Mastered',
                value: '14 Chapters',
                subtitle: 'NCERT Curriculum',
                accentColor: const Color(0xFF7C3AED),
              ),
            ),
            const SizedBox(width: 8),
            Expanded(
              child: _buildKpiCard(
                title: '🔥 Active Streak',
                value: '5 Days',
                subtitle: 'Daily Board Prep',
                accentColor: const Color(0xFFD97706),
              ),
            ),
          ],
        ),
      ],
    );
  }

  Widget _buildKpiCard({
    required String title,
    required String value,
    required String subtitle,
    required Color accentColor,
  }) {
    return Container(
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: AppTheme.borderSubtle),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: const TextStyle(fontSize: 11, fontWeight: FontWeight.w600, color: AppTheme.textSecondary)),
          const SizedBox(height: 4),
          Text(value, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: accentColor)),
          const SizedBox(height: 2),
          Text(subtitle, style: TextStyle(fontSize: 10, color: Colors.grey.shade500)),
        ],
      ),
    );
  }

  Widget _buildAdminModerationBanner(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors: [Color(0xFF4C1D95), Color(0xFF6D28D9)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(
            color: const Color(0xFF6D28D9).withOpacity(0.3),
            blurRadius: 8,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      child: Row(
        children: [
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: Colors.white.withOpacity(0.2),
              shape: BoxShape.circle,
            ),
            child: const Icon(Icons.security, color: Colors.white, size: 28),
          ),
          const SizedBox(width: 14),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: const [
                Text(
                  'Admin Moderation Dashboard',
                  style: TextStyle(
                    fontSize: 15,
                    fontWeight: FontWeight.bold,
                    color: Colors.white,
                  ),
                ),
                SizedBox(height: 2),
                Text(
                  'Approve, reject, or edit pending questions submitted to Supabase.',
                  style: TextStyle(fontSize: 11.5, color: Colors.white70),
                ),
              ],
            ),
          ),
          const SizedBox(width: 8),
          ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: Colors.white,
              foregroundColor: const Color(0xFF4C1D95),
              padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
            ),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (_) => const AdminReviewScreen()),
              );
            },
            child: const Text('Open Hub', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
          ),
        ],
      ),
    );
  }

  Widget _buildTeacherAdminTesterBanner(BuildContext context, WidgetRef ref) {
    return InkWell(
      onTap: () {
        ref.read(authNotifierProvider.notifier).switchRole(UserRole.admin);
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('Switched to Admin Persona! Moderation tools unlocked.'),
            duration: Duration(seconds: 2),
            behavior: SnackBarBehavior.floating,
          ),
        );
      },
      borderRadius: BorderRadius.circular(12),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
        decoration: BoxDecoration(
          color: Colors.indigo.shade50,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: Colors.indigo.shade200),
        ),
        child: Row(
          children: [
            Icon(Icons.shield_moon_outlined, size: 20, color: Colors.indigo.shade800),
            const SizedBox(width: 10),
            Expanded(
              child: Text(
                'Moderation Pipeline: Tap to switch to Admin and review pending questions.',
                style: TextStyle(fontSize: 11.5, color: Colors.indigo.shade900, fontWeight: FontWeight.w600),
              ),
            ),
            Icon(Icons.chevron_right, size: 18, color: Colors.indigo.shade800),
          ],
        ),
      ),
    );
  }

  Widget _buildSubjectCard({
    required BuildContext context,
    required String title,
    required String subtitle,
    required IconData icon,
    required Color accentColor,
    required String badgeText,
    required VoidCallback onTap,
  }) {
    return Card(
      margin: const EdgeInsets.only(bottom: 14),
      child: InkWell(
        onTap: onTap,
        borderRadius: BorderRadius.circular(16),
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Row(
            children: [
              Container(
                width: 52,
                height: 52,
                decoration: BoxDecoration(
                  color: accentColor.withOpacity(0.12),
                  borderRadius: BorderRadius.circular(14),
                ),
                child: Icon(icon, color: accentColor, size: 28),
              ),
              const SizedBox(width: 14),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      children: [
                        Text(
                          title,
                          style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                        ),
                        const Spacer(),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                          decoration: BoxDecoration(
                            color: accentColor.withOpacity(0.08),
                            borderRadius: BorderRadius.circular(6),
                          ),
                          child: Text(
                            badgeText,
                            style: TextStyle(
                              fontSize: 10.5,
                              fontWeight: FontWeight.bold,
                              color: accentColor,
                            ),
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 4),
                    Text(
                      subtitle,
                      style: const TextStyle(fontSize: 12, color: AppTheme.textSecondary),
                    ),
                  ],
                ),
              ),
              const SizedBox(width: 8),
              Icon(Icons.chevron_right, color: Colors.grey.shade400),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildPracticeQuizLauncher(BuildContext context) {
    return Container(
      width: double.infinity,
      padding: const EdgeInsets.all(18),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: AppTheme.borderSubtle),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: const [
              Icon(Icons.timer_outlined, color: AppTheme.primaryBlue, size: 22),
              SizedBox(width: 8),
              Text(
                'Timed Exam Practice Engine',
                style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              ),
            ],
          ),
          const SizedBox(height: 6),
          const Text(
            'Experience real CBSE board test conditions with instant automated scoring, timer countdown, and detailed step-by-step explanations.',
            style: TextStyle(fontSize: 12.5, color: AppTheme.textSecondary, height: 1.4),
          ),
          const SizedBox(height: 16),
          Row(
            children: [
              Expanded(
                child: ElevatedButton.icon(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppTheme.mathColor,
                    padding: const EdgeInsets.symmetric(vertical: 12),
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (_) => const QuizScreen(subject: Subject.math),
                      ),
                    );
                  },
                  icon: const Icon(Icons.play_arrow, size: 18),
                  label: const Text('Math Quiz', style: TextStyle(fontSize: 12.5)),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: ElevatedButton.icon(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppTheme.scienceColor,
                    padding: const EdgeInsets.symmetric(vertical: 12),
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (_) => const QuizScreen(subject: Subject.science),
                      ),
                    );
                  },
                  icon: const Icon(Icons.play_arrow, size: 18),
                  label: const Text('Science Quiz', style: TextStyle(fontSize: 12.5)),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: ElevatedButton.icon(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppTheme.socialScienceColor,
                    padding: const EdgeInsets.symmetric(vertical: 12),
                  ),
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (_) => const QuizScreen(subject: Subject.socialScience),
                      ),
                    );
                  },
                  icon: const Icon(Icons.play_arrow, size: 18),
                  label: const Text('SST Quiz', style: TextStyle(fontSize: 12.5)),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
