import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../core/theme/app_theme.dart';
import '../providers/auth_provider.dart';
import 'admin/admin_review_screen.dart';
import 'home/student_home_screen.dart';
import 'math/math_chapter_list_screen.dart';
import 'science/science_chapter_list_screen.dart';
import 'social_science/social_science_chapter_list_screen.dart';

/// Global active tab provider for programmatic navigation across screens
final activeBottomNavTabProvider = StateProvider<int>((ref) => 0);

/// Primary App Shell featuring standard 5-tab Bottom Navigation Bar:
/// 1. Home Dashboard
/// 2. Mathematics (14 Chapters)
/// 3. Science (13 Chapters)
/// 4. Social Science (7 Chapters)
/// 5. Admin Hub
class MainShellScreen extends ConsumerWidget {
  const MainShellScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final activeTab = ref.watch(activeBottomNavTabProvider);
    final isAdmin = ref.watch(isAdminProvider);

    final List<Widget> screens = [
      const StudentHomeScreen(),
      const MathChapterListScreen(),
      const ScienceChapterListScreen(),
      const SocialScienceChapterListScreen(),
      const AdminReviewScreen(),
    ];

    return Scaffold(
      body: IndexedStack(
        index: activeTab,
        children: screens,
      ),
      bottomNavigationBar: Container(
        decoration: BoxDecoration(
          color: Colors.white,
          border: const Border(
            top: BorderSide(color: Color(0xFFE2E8F0), width: 1),
          ),
          boxShadow: [
            BoxShadow(
              color: Colors.black.withOpacity(0.04),
              blurRadius: 10,
              offset: const Offset(0, -2),
            ),
          ],
        ),
        child: NavigationBar(
          selectedIndex: activeTab,
          onDestinationSelected: (index) {
            ref.read(activeBottomNavTabProvider.notifier).state = index;
          },
          backgroundColor: Colors.white,
          elevation: 0,
          indicatorColor: _getIndicatorColor(activeTab),
          labelBehavior: NavigationDestinationLabelBehavior.alwaysShow,
          destinations: [
            const NavigationDestination(
              icon: Icon(Icons.home_outlined),
              selectedIcon: Icon(Icons.home, color: Colors.white),
              label: 'Home',
            ),
            const NavigationDestination(
              icon: Icon(Icons.calculate_outlined),
              selectedIcon: Icon(Icons.calculate, color: Colors.white),
              label: 'Math (14)',
            ),
            const NavigationDestination(
              icon: Icon(Icons.science_outlined),
              selectedIcon: Icon(Icons.science, color: Colors.white),
              label: 'Science (13)',
            ),
            const NavigationDestination(
              icon: Icon(Icons.public_outlined),
              selectedIcon: Icon(Icons.public, color: Colors.white),
              label: 'Social (7)',
            ),
            NavigationDestination(
              icon: Icon(isAdmin ? Icons.admin_panel_settings_outlined : Icons.shield_outlined),
              selectedIcon: const Icon(Icons.admin_panel_settings, color: Colors.white),
              label: 'Admin',
            ),
          ],
        ),
      ),
    );
  }

  Color _getIndicatorColor(int tabIndex) {
    switch (tabIndex) {
      case 0:
        return AppTheme.primaryBlue;
      case 1:
        return AppTheme.mathColor;
      case 2:
        return AppTheme.scienceColor;
      case 3:
        return AppTheme.socialScienceColor;
      case 4:
        return AppTheme.hotsColor;
      default:
        return AppTheme.primaryBlue;
    }
  }
}
