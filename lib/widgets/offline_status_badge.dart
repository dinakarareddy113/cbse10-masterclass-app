import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../providers/questions_provider.dart';

class OfflineStatusBadge extends ConsumerWidget {
  const OfflineStatusBadge({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final isOffline = ref.watch(isOfflineModeProvider);
    final cachedCount = ref.watch(cachedQuestionsCountProvider);

    return InkWell(
      onTap: () {
        // Toggle offline simulation
        final current = ref.read(isOfflineModeProvider);
        ref.read(isOfflineModeProvider.notifier).state = !current;
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(
              !current
                  ? 'Simulated Offline Mode Enabled (Serving from Hive cache)'
                  : 'Online Mode Enabled (Connected to Supabase RLS backend)',
            ),
            duration: const Duration(seconds: 2),
            behavior: SnackBarBehavior.floating,
          ),
        );
      },
      borderRadius: BorderRadius.circular(20),
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
        decoration: BoxDecoration(
          color: isOffline ? Colors.amber.shade100 : const Color(0xFFDCFCE7),
          borderRadius: BorderRadius.circular(20),
          border: Border.all(
            color: isOffline ? Colors.amber.shade700 : const Color(0xFF16A34A),
            width: 1,
          ),
        ),
        child: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              isOffline ? Icons.cloud_off_rounded : Icons.cloud_done_rounded,
              size: 14,
              color: isOffline ? Colors.amber.shade900 : const Color(0xFF15803D),
            ),
            const SizedBox(width: 5),
            Text(
              isOffline ? 'Offline Cache ($cachedCount)' : 'Live ($cachedCount Cached)',
              style: TextStyle(
                fontSize: 11,
                fontWeight: FontWeight.w600,
                color: isOffline ? Colors.amber.shade900 : const Color(0xFF15803D),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
