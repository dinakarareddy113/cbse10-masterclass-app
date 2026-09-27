import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/theme/app_theme.dart';
import '../../models/quiz_session.dart';
import '../../providers/quiz_provider.dart';

class QuizResultScreen extends ConsumerWidget {
  final QuizSession session;

  const QuizResultScreen({super.key, required this.session});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final percentage = session.scorePercentage;
    final isPassed = percentage >= 50.0;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Performance & Evaluation'),
        automaticallyImplyLeading: false,
        actions: [
          IconButton(
            icon: const Icon(Icons.close),
            onPressed: () {
              ref.read(quizSessionProvider.notifier).resetQuiz();
              Navigator.pop(context);
            },
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            // Score Summary Card
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(24),
              decoration: BoxDecoration(
                gradient: LinearGradient(
                  colors: isPassed
                      ? [const Color(0xFF065F46), const Color(0xFF047857)]
                      : [const Color(0xFF991B1B), const Color(0xFFB91C1C)],
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                ),
                borderRadius: BorderRadius.circular(16),
                boxShadow: [
                  BoxShadow(
                    color: (isPassed ? Colors.green : Colors.red).withOpacity(0.3),
                    blurRadius: 10,
                    offset: const Offset(0, 4),
                  ),
                ],
              ),
              child: Column(
                children: [
                  Icon(
                    isPassed ? Icons.emoji_events : Icons.replay_outlined,
                    size: 48,
                    color: Colors.white,
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '${percentage.toStringAsFixed(1)}%',
                    style: const TextStyle(
                      fontSize: 36,
                      fontWeight: FontWeight.w900,
                      color: Colors.white,
                      letterSpacing: -1,
                    ),
                  ),
                  Text(
                    isPassed ? 'Outstanding Mastery!' : 'Keep Practicing!',
                    style: const TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: Colors.white70,
                    ),
                  ),
                  const SizedBox(height: 16),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceAround,
                    children: [
                      _buildMetric(label: 'Correct', count: session.correctCount, color: Colors.greenAccent),
                      _buildMetric(label: 'Incorrect', count: session.incorrectCount, color: Colors.redAccent),
                      _buildMetric(label: 'Skipped', count: session.unattemptedCount, color: Colors.orangeAccent),
                    ],
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),

            // Time Spent Summary
            Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: AppTheme.borderSubtle),
              ),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Row(
                    children: [
                      Icon(Icons.schedule, size: 20, color: AppTheme.textSecondary),
                      SizedBox(width: 8),
                      Text('Time Expended:', style: TextStyle(fontWeight: FontWeight.w600)),
                    ],
                  ),
                  Text(
                    '${session.timeSpentSeconds ~/ 60}m ${session.timeSpentSeconds % 60}s',
                    style: const TextStyle(fontWeight: FontWeight.bold, color: AppTheme.primaryBlue),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 24),

            // Question by Question Detailed Review
            const Align(
              alignment: Alignment.centerLeft,
              child: Text(
                'Comprehensive Solution Review',
                style: TextStyle(
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                  color: AppTheme.textPrimary,
                ),
              ),
            ),
            const SizedBox(height: 12),

            ...session.questions.asMap().entries.map((entry) {
              final idx = entry.key;
              final question = entry.value;
              final selectedOptId = session.selectedAnswers[question.id];
              final isCorrect = question.correctOption?.id == selectedOptId;
              final isSkipped = selectedOptId == null;

              return Card(
                margin: const EdgeInsets.only(bottom: 16),
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                            decoration: BoxDecoration(
                              color: isSkipped
                                  ? Colors.grey.shade100
                                  : isCorrect
                                      ? const Color(0xFFDCFCE7)
                                      : const Color(0xFFFEE2E2),
                              borderRadius: BorderRadius.circular(6),
                            ),
                            child: Row(
                              children: [
                                Icon(
                                  isSkipped
                                      ? Icons.remove_circle_outline
                                      : isCorrect
                                          ? Icons.check_circle
                                          : Icons.cancel,
                                  size: 14,
                                  color: isSkipped
                                      ? Colors.grey
                                      : isCorrect
                                          ? const Color(0xFF16A34A)
                                          : AppTheme.dangerRose,
                                ),
                                const SizedBox(width: 4),
                                Text(
                                  isSkipped
                                      ? 'Skipped'
                                      : isCorrect
                                          ? 'Correct'
                                          : 'Incorrect',
                                  style: TextStyle(
                                    fontSize: 11,
                                    fontWeight: FontWeight.bold,
                                    color: isSkipped
                                        ? Colors.grey.shade700
                                        : isCorrect
                                            ? const Color(0xFF16A34A)
                                            : AppTheme.dangerRose,
                                  ),
                                ),
                              ],
                            ),
                          ),
                          const Spacer(),
                          Text(
                            'Q${idx + 1}',
                            style: const TextStyle(fontWeight: FontWeight.bold, color: AppTheme.textSecondary),
                          ),
                        ],
                      ),
                      const SizedBox(height: 10),
                      Text(
                        question.questionText,
                        style: const TextStyle(fontSize: 14.5, fontWeight: FontWeight.w600),
                      ),
                      const SizedBox(height: 12),

                      // Options breakdown
                      if (question.options != null) ...[
                        ...question.options!.map((opt) {
                          final isStudentChoice = opt.id == selectedOptId;
                          final isActualCorrect = opt.isCorrect;

                          Color bg = Colors.transparent;
                          Color border = AppTheme.borderSubtle;
                          if (isActualCorrect) {
                            bg = const Color(0xFFDCFCE7);
                            border = const Color(0xFF16A34A);
                          } else if (isStudentChoice) {
                            bg = const Color(0xFFFEE2E2);
                            border = AppTheme.dangerRose;
                          }

                          return Container(
                            margin: const EdgeInsets.only(bottom: 6),
                            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                            decoration: BoxDecoration(
                              color: bg,
                              borderRadius: BorderRadius.circular(8),
                              border: Border.all(color: border),
                            ),
                            child: Row(
                              children: [
                                Text(
                                  '${opt.id}. ',
                                  style: const TextStyle(fontWeight: FontWeight.bold),
                                ),
                                Expanded(child: Text(opt.text, style: const TextStyle(fontSize: 13))),
                                if (isActualCorrect)
                                  const Text('✓ Correct',
                                      style: TextStyle(
                                          fontSize: 11,
                                          fontWeight: FontWeight.bold,
                                          color: Color(0xFF16A34A))),
                                if (isStudentChoice && !isActualCorrect)
                                  const Text('✗ Your Choice',
                                      style: TextStyle(
                                          fontSize: 11,
                                          fontWeight: FontWeight.bold,
                                          color: AppTheme.dangerRose)),
                              ],
                            ),
                          );
                        }),
                      ],
                      const SizedBox(height: 10),

                      // Step-by-Step Solution
                      Container(
                        width: double.infinity,
                        padding: const EdgeInsets.all(12),
                        decoration: BoxDecoration(
                          color: const Color(0xFFF8FAFC),
                          borderRadius: BorderRadius.circular(8),
                          border: Border.all(color: AppTheme.borderSubtle),
                        ),
                        child: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Text(
                              'Verified NCERT Solution:',
                              style: TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: AppTheme.primaryBlue),
                            ),
                            const SizedBox(height: 4),
                            Text(
                              question.stepByStepSolution,
                              style: const TextStyle(fontSize: 12.5, height: 1.4, fontFamily: 'monospace'),
                            ),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              );
            }),
            const SizedBox(height: 24),
            ElevatedButton.icon(
              onPressed: () {
                ref.read(quizSessionProvider.notifier).resetQuiz();
                Navigator.pop(context);
              },
              icon: const Icon(Icons.arrow_back),
              label: const Text('Back to Home Dashboard'),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildMetric({required String label, required int count, required Color color}) {
    return Column(
      children: [
        Text(
          '$count',
          style: TextStyle(
            fontSize: 22,
            fontWeight: FontWeight.bold,
            color: color,
          ),
        ),
        Text(
          label,
          style: const TextStyle(fontSize: 12, color: Colors.white70),
        ),
      ],
    );
  }
}
