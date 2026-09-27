import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/theme/app_theme.dart';
import '../../models/user_profile.dart';
import '../../providers/auth_provider.dart';

/// Secure Route Guard ensuring only users with role == 'admin' access moderation screens
class AdminGuard extends ConsumerWidget {
  final Widget child;

  const AdminGuard({super.key, required this.child});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final authState = ref.watch(authNotifierProvider);

    return authState.when(
      data: (profile) {
        if (profile != null && profile.role == UserRole.admin) {
          return child;
        }

        // Access Denied Screen
        return Scaffold(
          appBar: AppBar(
            title: const Text('Access Denied'),
          ),
          body: Center(
            child: Padding(
              padding: const EdgeInsets.all(24.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Container(
                    padding: const EdgeInsets.all(20),
                    decoration: BoxDecoration(
                      color: AppTheme.dangerRose.withOpacity(0.1),
                      shape: BoxShape.circle,
                    ),
                    child: const Icon(
                      Icons.shield_outlined,
                      size: 56,
                      color: AppTheme.dangerRose,
                    ),
                  ),
                  const SizedBox(height: 20),
                  const Text(
                    'Admin Privileges Required',
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: AppTheme.textPrimary,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    'Your current active role is "${profile?.role.value.toUpperCase() ?? 'UNAUTHENTICATED'}". '
                    'Only accounts with "admin" role can access the moderation pipeline.',
                    textAlign: TextAlign.center,
                    style: const TextStyle(
                      fontSize: 14,
                      color: AppTheme.textSecondary,
                      height: 1.4,
                    ),
                  ),
                  const SizedBox(height: 24),
                  // Persona switcher for testing
                  ElevatedButton.icon(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppTheme.primaryBlue,
                    ),
                    onPressed: () {
                      ref.read(authNotifierProvider.notifier).switchRole(UserRole.admin);
                    },
                    icon: const Icon(Icons.admin_panel_settings),
                    label: const Text('Switch to Admin Persona (Test Mode)'),
                  ),
                  const SizedBox(height: 12),
                  OutlinedButton(
                    onPressed: () => Navigator.pop(context),
                    child: const Text('Return to Student Dashboard'),
                  ),
                ],
              ),
            ),
          ),
        );
      },
      loading: () => const Scaffold(
        body: Center(child: CircularProgressIndicator()),
      ),
      error: (err, st) => Scaffold(
        body: Center(child: Text('Authentication error: $err')),
      ),
    );
  }
}
