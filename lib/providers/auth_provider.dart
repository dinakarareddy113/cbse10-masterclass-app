import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../models/user_profile.dart';
import '../services/supabase_service.dart';

final supabaseServiceProvider = Provider<SupabaseService>((ref) {
  return SupabaseService.instance;
});

class AuthStateNotifier extends StateNotifier<AsyncValue<UserProfile?>> {
  final SupabaseService _supabaseService;

  AuthStateNotifier(this._supabaseService) : super(const AsyncValue.loading()) {
    _initAuth();
  }

  Future<void> _initAuth() async {
    state = const AsyncValue.loading();
    try {
      // Default to student user for clean initial student experience
      _supabaseService.setMockActiveRole(UserRole.student);
      final profile = await _supabaseService.fetchUserProfile('00000000-0000-0000-0000-000000000003');
      state = AsyncValue.data(profile);
    } catch (e, st) {
      state = AsyncValue.error(e, st);
    }
  }

  /// Switch active role (Student, Teacher, Admin) for instant validation
  Future<void> switchRole(UserRole role) async {
    state = const AsyncValue.loading();
    try {
      _supabaseService.setMockActiveRole(role);
      final mockId = switch (role) {
        UserRole.admin => '00000000-0000-0000-0000-000000000001',
        UserRole.teacher => '00000000-0000-0000-0000-000000000002',
        UserRole.student => '00000000-0000-0000-0000-000000000003',
      };
      final profile = await _supabaseService.fetchUserProfile(mockId);
      state = AsyncValue.data(profile);
    } catch (e, st) {
      state = AsyncValue.error(e, st);
    }
  }

  Future<void> signIn(String email, String password) async {
    state = const AsyncValue.loading();
    try {
      final profile = await _supabaseService.signIn(email: email, password: password);
      state = AsyncValue.data(profile);
    } catch (e, st) {
      state = AsyncValue.error(e, st);
      rethrow;
    }
  }

  void setStudentProfile({
    required String name,
    required String email,
    required String schoolName,
    required String classLevel,
  }) {
    state = AsyncValue.data(UserProfile(
      id: '00000000-0000-0000-0000-000000000003',
      fullName: name,
      role: UserRole.student,
      email: email,
      schoolName: schoolName,
      classLevel: classLevel,
      createdAt: DateTime.now(),
    ));
  }

  Future<void> signOut() async {
    await _supabaseService.signOut();
    state = const AsyncValue.data(null);
  }
}

final authNotifierProvider =
    StateNotifierProvider<AuthStateNotifier, AsyncValue<UserProfile?>>((ref) {
  final service = ref.watch(supabaseServiceProvider);
  return AuthStateNotifier(service);
});

/// Convenience provider to directly check if current user is admin
final isAdminProvider = Provider<bool>((ref) {
  final authState = ref.watch(authNotifierProvider);
  return authState.value?.role == UserRole.admin;
});
