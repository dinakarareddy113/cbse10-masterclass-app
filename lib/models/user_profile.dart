import 'package:flutter/foundation.dart';

enum UserRole {
  student('student'),
  teacher('teacher'),
  admin('admin');

  final String value;
  const UserRole(this.value);

  static UserRole fromString(String? roleStr) {
    return switch (roleStr?.toLowerCase().trim()) {
      'admin' => UserRole.admin,
      'teacher' => UserRole.teacher,
      _ => UserRole.student,
    };
  }

  bool get isAdmin => this == UserRole.admin;
  bool get isTeacher => this == UserRole.teacher;
  bool get isStudent => this == UserRole.student;
}

@immutable
class UserProfile {
  final String id;
  final String fullName;
  final UserRole role;
  final String? email;
  final String? schoolName;
  final String? classLevel;
  final DateTime createdAt;

  const UserProfile({
    required this.id,
    required this.fullName,
    required this.role,
    this.email,
    this.schoolName,
    this.classLevel,
    required this.createdAt,
  });

  factory UserProfile.fromJson(Map<String, dynamic> json) {
    return UserProfile(
      id: json['id'] as String? ?? '',
      fullName: json['full_name'] as String? ?? 'Student User',
      role: UserRole.fromString(json['role'] as String?),
      email: json['email'] as String?,
      schoolName: json['school_name'] as String?,
      classLevel: json['class_level'] as String? ?? 'Class 10',
      createdAt: json['created_at'] != null
          ? DateTime.tryParse(json['created_at'].toString()) ?? DateTime.now()
          : DateTime.now(),
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'full_name': fullName,
      'role': role.value,
      'email': email,
      'school_name': schoolName,
      'class_level': classLevel,
      'created_at': createdAt.toIso8601String(),
    };
  }

  UserProfile copyWith({
    String? id,
    String? fullName,
    UserRole? role,
    String? email,
    String? schoolName,
    String? classLevel,
    DateTime? createdAt,
  }) {
    return UserProfile(
      id: id ?? this.id,
      fullName: fullName ?? this.fullName,
      role: role ?? this.role,
      email: email ?? this.email,
      schoolName: schoolName ?? this.schoolName,
      classLevel: classLevel ?? this.classLevel,
      createdAt: createdAt ?? this.createdAt,
    );
  }

  @override
  String toString() =>
      'UserProfile(id: $id, fullName: $fullName, role: ${role.value}, class: $classLevel, school: $schoolName)';

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is UserProfile &&
          runtimeType == other.runtimeType &&
          id == other.id &&
          fullName == other.fullName &&
          role == other.role;

  @override
  int get hashCode => id.hashCode ^ fullName.hashCode ^ role.hashCode;
}
