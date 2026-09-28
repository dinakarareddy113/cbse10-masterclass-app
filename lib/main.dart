import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'core/constants/app_constants.dart';
import 'core/theme/app_theme.dart';
import 'screens/main_shell_screen.dart';
import 'services/local_cache_service.dart';
import 'services/supabase_service.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Initialize Local Offline Cache (Hive)
  await LocalCacheService.instance.init();

  // Initialize Supabase Client
  await SupabaseService.instance.init();

  runApp(
    const ProviderScope(
      child: CbseClass10MasterclassApp(),
    ),
  );
}

class CbseClass10MasterclassApp extends StatelessWidget {
  const CbseClass10MasterclassApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: AppConstants.appName,
      debugShowCheckedModeBanner: false,
      theme: AppTheme.lightTheme,
      home: const MainShellScreen(),
    );
  }
}
