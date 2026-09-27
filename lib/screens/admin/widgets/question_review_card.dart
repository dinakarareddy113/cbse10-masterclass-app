import 'package:flutter/material.dart';
import '../../../core/theme/app_theme.dart';
import '../../../models/question.dart';
import '../../../widgets/difficulty_chip.dart';
import 'edit_approve_modal.dart';

class QuestionReviewCard extends StatelessWidget {
  final Question question;
  final VoidCallback onApprove;
  final void Function(String? feedback) onReject;
  final EditAndApproveCallback onEditAndApprove;

  const QuestionReviewCard({
    super.key,
    required this.question,
    required this.onApprove,
    required this.onReject,
    required this.onEditAndApprove,
  });

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(14),
        side: BorderSide(
          color: question.status == QuestionStatus.pendingReview
              ? AppTheme.accentAmber.withOpacity(0.5)
              : AppTheme.borderSubtle,
          width: 1.5,
        ),
      ),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header Row: Status badge, Chapter, Difficulty
            Row(
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  decoration: BoxDecoration(
                    color: question.status.color.withOpacity(0.12),
                    borderRadius: BorderRadius.circular(6),
                    border: Border.all(color: question.status.color.withOpacity(0.4)),
                  ),
                  child: Row(
                    children: [
                      Icon(Icons.pending_actions, size: 13, color: question.status.color),
                      const SizedBox(width: 4),
                      Text(
                        question.status.label,
                        style: TextStyle(
                          fontSize: 11,
                          fontWeight: FontWeight.bold,
                          color: question.status.color,
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: Text(
                    question.chapterId.replaceAll('_', ' ').toUpperCase(),
                    style: const TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w600,
                      color: AppTheme.textSecondary,
                    ),
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
                DifficultyChip(level: question.difficultyLevel),
              ],
            ),
            const SizedBox(height: 12),

            // Question Text
            Text(
              question.questionText,
              style: const TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w600,
                color: AppTheme.textPrimary,
                height: 1.4,
              ),
            ),
            const SizedBox(height: 12),

            // MCQ Options preview
            if (question.options != null) ...[
              ...question.options!.map((opt) {
                return Container(
                  margin: const EdgeInsets.only(bottom: 6),
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                  decoration: BoxDecoration(
                    color: opt.isCorrect ? const Color(0xFFDCFCE7) : AppTheme.neutralBg,
                    borderRadius: BorderRadius.circular(6),
                    border: Border.all(
                      color: opt.isCorrect ? const Color(0xFF16A34A) : AppTheme.borderSubtle,
                    ),
                  ),
                  child: Row(
                    children: [
                      Text(
                        '${opt.id}. ',
                        style: TextStyle(
                          fontWeight: FontWeight.bold,
                          color: opt.isCorrect ? const Color(0xFF16A34A) : AppTheme.textPrimary,
                        ),
                      ),
                      Expanded(
                        child: Text(
                          opt.text,
                          style: TextStyle(
                            fontSize: 13,
                            color: opt.isCorrect ? const Color(0xFF15803D) : AppTheme.textPrimary,
                          ),
                        ),
                      ),
                      if (opt.isCorrect)
                        const Text(
                          'Correct Key',
                          style: TextStyle(
                            fontSize: 10.5,
                            fontWeight: FontWeight.bold,
                            color: Color(0xFF16A34A),
                          ),
                        ),
                    ],
                  ),
                );
              }),
              const SizedBox(height: 8),
            ],

            // Step-by-Step Solution preview
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
                    'Step-by-Step Solution Draft:',
                    style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.bold,
                      color: AppTheme.textSecondary,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(
                    question.stepByStepSolution,
                    style: const TextStyle(
                      fontFamily: 'monospace',
                      fontSize: 12,
                      height: 1.4,
                      color: Color(0xFF334155),
                    ),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 16),

            // Metadata info
            Text(
              'Submitted by: ${question.submittedBy.substring(0, 8)}... | ID: ${question.id.substring(0, 8)}...',
              style: const TextStyle(fontSize: 10.5, color: Colors.grey),
            ),
            const Divider(height: 20),

            // Action Buttons Bar
            Row(
              children: [
                // Edit & Approve Button
                OutlinedButton.icon(
                  style: OutlinedButton.styleFrom(
                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
                  ),
                  onPressed: () {
                    EditApproveModal.show(
                      context: context,
                      question: question,
                      onSaveAndApprove: onEditAndApprove,
                    );
                  },
                  icon: const Icon(Icons.edit_outlined, size: 16),
                  label: const Text('Edit & Approve', style: TextStyle(fontSize: 12)),
                ),
                const Spacer(),

                // Reject Button
                IconButton.filledTonal(
                  style: IconButton.styleFrom(
                    backgroundColor: AppTheme.dangerRose.withOpacity(0.12),
                    foregroundColor: AppTheme.dangerRose,
                  ),
                  icon: const Icon(Icons.close, size: 18),
                  tooltip: 'Reject Question',
                  onPressed: () => _showRejectDialog(context),
                ),
                const SizedBox(width: 8),

                // Approve Button
                ElevatedButton.icon(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppTheme.successEmerald,
                    padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                  ),
                  onPressed: onApprove,
                  icon: const Icon(Icons.check, size: 16),
                  label: const Text('Approve', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold)),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  void _showRejectDialog(BuildContext context) {
    final feedbackController = TextEditingController();

    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Reject Question'),
        content: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text(
              'Specify rejection feedback to help the educator revise the question:',
              style: TextStyle(fontSize: 13, color: AppTheme.textSecondary),
            ),
            const SizedBox(height: 12),
            TextField(
              controller: feedbackController,
              maxLines: 3,
              decoration: const InputDecoration(
                hintText: 'e.g. Ambiguous option C, incorrect step 2 calculation...',
              ),
            ),
          ],
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text('Cancel'),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(backgroundColor: AppTheme.dangerRose),
            onPressed: () {
              Navigator.pop(ctx);
              onReject(feedbackController.text.trim().isNotEmpty ? feedbackController.text.trim() : null);
            },
            child: const Text('Confirm Reject'),
          ),
        ],
      ),
    );
  }
}
