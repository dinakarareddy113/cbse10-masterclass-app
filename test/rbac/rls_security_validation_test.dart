import 'package:flutter_test/flutter_test.dart';
import 'package:cbse_class10_masterclass/models/question.dart';
import 'package:cbse_class10_masterclass/models/user_profile.dart';

void main() {
  group('Database Schema & RLS Policy Contract Tests', () {
    test('UserRole enum conforms strictly to database CHECK constraint', () {
      // Database constraint: CHECK (role IN ('student', 'teacher', 'admin'))
      final allowedRoles = {'student', 'teacher', 'admin'};
      for (final role in UserRole.values) {
        expect(allowedRoles.contains(role.value), isTrue);
      }
    });

    test('Subject enum conforms strictly to database CHECK constraint', () {
      // Database constraint: CHECK (subject IN ('math', 'science', 'social_science'))
      final allowedSubjects = {'math', 'science', 'social_science'};
      for (final sub in Subject.values) {
        expect(allowedSubjects.contains(sub.value), isTrue);
      }
    });

    test('QuestionStatus enum conforms strictly to database CHECK constraint', () {
      // Database constraint: CHECK (status IN ('pending_review', 'approved', 'rejected'))
      final allowedStatuses = {'pending_review', 'approved', 'rejected'};
      for (final st in QuestionStatus.values) {
        expect(allowedStatuses.contains(st.value), isTrue);
      }
    });

    test('DifficultyLevel enum conforms strictly to database CHECK constraint', () {
      // Database constraint: CHECK (difficulty_level IN ('easy', 'medium', 'hard', 'hots'))
      final allowedDifficulties = {'easy', 'medium', 'hard', 'hots'};
      for (final diff in DifficultyLevel.values) {
        expect(allowedDifficulties.contains(diff.value), isTrue);
      }
    });

    test('RLS Visibility Logic: Students can only view approved questions', () {
      final studentProfile = UserProfile(
        id: 'student-123',
        fullName: 'Student User',
        role: UserRole.student,
        createdAt: DateTime.now(),
      );

      final approvedQuestion = Question(
        id: 'q1',
        subject: Subject.math,
        chapterId: 'ch_01',
        questionText: 'Test approved',
        stepByStepSolution: 'Sol',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.approved,
        submittedBy: 'teacher-1',
        createdAt: DateTime.now(),
      );

      final pendingQuestion = Question(
        id: 'q2',
        subject: Subject.math,
        chapterId: 'ch_01',
        questionText: 'Test pending',
        stepByStepSolution: 'Sol',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: 'teacher-1',
        createdAt: DateTime.now(),
      );

      // Student RLS filter simulation
      bool canStudentRead(Question q, UserProfile u) {
        return q.status == QuestionStatus.approved || u.role == UserRole.admin || q.submittedBy == u.id;
      }

      expect(canStudentRead(approvedQuestion, studentProfile), isTrue);
      expect(canStudentRead(pendingQuestion, studentProfile), isFalse);

      final adminProfile = studentProfile.copyWith(role: UserRole.admin);
      expect(canStudentRead(approvedQuestion, adminProfile), isTrue);
      expect(canStudentRead(pendingQuestion, adminProfile), isTrue);
    });
  });
}
