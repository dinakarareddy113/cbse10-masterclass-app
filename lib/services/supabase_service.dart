import 'package:flutter/foundation.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import '../core/constants/supabase_constants.dart';
import '../models/user_profile.dart';

/// Supabase Client & Authentication Service
class SupabaseService {
  static final SupabaseService instance = SupabaseService._internal();
  SupabaseService._internal();

  bool _isInitialized = false;
  bool get isInitialized => _isInitialized;

  // Active mock session fallback for instant preview and offline development
  UserProfile? _mockActiveProfile;

  Future<void> init() async {
    try {
      await Supabase.initialize(
        url: SupabaseConstants.supabaseUrl,
        anonKey: SupabaseConstants.supabaseAnonKey,
        debug: kDebugMode,
      );
      _isInitialized = true;
      debugPrint('SupabaseService: Supabase initialized successfully.');
    } catch (e) {
      debugPrint('SupabaseService: Could not connect to remote Supabase ($e). Running in resilient offline/emulated mode.');
      _isInitialized = false;
    }
  }

  SupabaseClient? get client {
    if (_isInitialized) {
      try {
        return Supabase.instance.client;
      } catch (_) {
        return null;
      }
    }
    return null;
  }

  User? get currentAuthUser => client?.auth.currentUser;

  /// Fetch user profile from public.profiles
  Future<UserProfile?> fetchUserProfile(String userId) async {
    if (_mockActiveProfile != null && _mockActiveProfile!.id == userId) {
      return _mockActiveProfile;
    }

    if (client != null) {
      try {
        final response = await client!
            .from(SupabaseConstants.profilesTable)
            .select()
            .eq('id', userId)
            .maybeSingle();

        if (response != null) {
          return UserProfile.fromJson(response);
        }
      } catch (e) {
        debugPrint('Error fetching profile from Supabase: $e');
      }
    }

    // Default fallback profile if offline or mock
    return _mockActiveProfile;
  }

  /// Demo helper to switch roles (Student / Teacher / Admin) in dev/emulation mode
  void setMockActiveRole(UserRole role, {String? name}) {
    final mockId = switch (role) {
      UserRole.admin => '00000000-0000-0000-0000-000000000001',
      UserRole.teacher => '00000000-0000-0000-0000-000000000002',
      UserRole.student => '00000000-0000-0000-0000-000000000003',
    };

    _mockActiveProfile = UserProfile(
      id: mockId,
      fullName: name ?? switch (role) {
        UserRole.admin => 'Lead Examiner (Admin)',
        UserRole.teacher => 'Prof. R.K. Sharma (Teacher)',
        UserRole.student => 'Aarav Patel (Student)',
      },
      role: role,
      createdAt: DateTime.now(),
    );
  }

  /// Sign In with Email & Password
  Future<UserProfile?> signIn({required String email, required String password}) async {
    if (client != null) {
      try {
        final response = await client!.auth.signInWithPassword(
          email: email,
          password: password,
        );
        if (response.user != null) {
          return await fetchUserProfile(response.user!.id);
        }
      } catch (e) {
        debugPrint('Supabase signIn error: $e');
        rethrow;
      }
    }
    return _mockActiveProfile;
  }

  /// Sign Up with Email, Password, Name, and Role
  Future<UserProfile?> signUp({
    required String email,
    required String password,
    required String fullName,
    UserRole role = UserRole.student,
  }) async {
    if (client != null) {
      try {
        final response = await client!.auth.signUp(
          email: email,
          password: password,
          data: {
            'full_name': fullName,
            'role': role.value,
          },
        );
        if (response.user != null) {
          return await fetchUserProfile(response.user!.id);
        }
      } catch (e) {
        debugPrint('Supabase signUp error: $e');
        rethrow;
      }
    }

    _mockActiveProfile = UserProfile(
      id: 'demo-user-id-${DateTime.now().millisecondsSinceEpoch}',
      fullName: fullName,
      role: role,
      createdAt: DateTime.now(),
    );
    return _mockActiveProfile;
  }

  /// Sign Out
  Future<void> signOut() async {
    if (client != null) {
      try {
        await client!.auth.signOut();
      } catch (e) {
        debugPrint('Supabase signOut error: $e');
      }
    }
    _mockActiveProfile = null;
  }
}
