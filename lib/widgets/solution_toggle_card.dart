import 'package:flutter/material.dart';
import '../core/theme/app_theme.dart';
import '../models/question.dart';
import 'difficulty_chip.dart';

class SolutionToggleCard extends StatefulWidget {
  final Question question;
  final int index;
  final VoidCallback? onSolutionRevealed;

  const SolutionToggleCard({
    super.key,
    required this.question,
    required this.index,
    this.onSolutionRevealed,
  });

  @override
  State<SolutionToggleCard> createState() => _SolutionToggleCardState();
}

class _SolutionToggleCardState extends State<SolutionToggleCard> {
  bool _isSolutionVisible = false;
  String? _selectedOptionId;

  @override
  Widget build(BuildContext context) {
    final q = widget.question;

    return Card(
      margin: const EdgeInsets.only(bottom: 16),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // Header Row: Question number, Subject chip, Difficulty
            Row(
              children: [
                CircleAvatar(
                  radius: 14,
                  backgroundColor: AppTheme.primaryBlue.withOpacity(0.1),
                  child: Text(
                    'Q${widget.index}',
                    style: const TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.bold,
                      color: AppTheme.primaryBlue,
                    ),
                  ),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    q.chapterId.replaceAll('_', ' ').toUpperCase(),
                    style: const TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.w600,
                      color: AppTheme.textSecondary,
                    ),
                    overflow: TextOverflow.ellipsis,
                  ),
                ),
                DifficultyChip(level: q.difficultyLevel),
              ],
            ),
            const SizedBox(height: 12),

            // Question Text
            Text(
              q.questionText,
              style: const TextStyle(
                fontSize: 15,
                fontWeight: FontWeight.w600,
                color: AppTheme.textPrimary,
                height: 1.45,
              ),
            ),
            const SizedBox(height: 12),

            // MCQ Options if present
            if (q.isMCQ) ...[
              ...q.options!.map((option) {
                final isSelected = _selectedOptionId == option.id;
                final isAttempted = _selectedOptionId != null;
                final isAnswerRevealed = _isSolutionVisible;
                Color optBgColor = AppTheme.neutralBg;
                Color optBorderColor = AppTheme.borderSubtle;
                Widget? optTrailing;

                if (isAttempted || isAnswerRevealed) {
                  if (isSelected && option.isCorrect) {
                    optBgColor = const Color(0xFFDCFCE7);
                    optBorderColor = const Color(0xFF16A34A);
                    optTrailing = const Icon(Icons.check_circle, color: Color(0xFF16A34A), size: 20);
                  } else if (isSelected && !option.isCorrect) {
                    optBgColor = const Color(0xFFFEE2E2);
                    optBorderColor = AppTheme.dangerRose;
                    optTrailing = const Icon(Icons.cancel, color: AppTheme.dangerRose, size: 20);
                  } else if (!isSelected && option.isCorrect && (isAttempted || isAnswerRevealed)) {
                    optBgColor = const Color(0xFFDCFCE7).withOpacity(0.5);
                    optBorderColor = const Color(0xFF16A34A).withOpacity(0.6);
                    optTrailing = const Icon(Icons.check_circle_outline, color: Color(0xFF16A34A), size: 20);
                  }
                }

                return Padding(
                  padding: const EdgeInsets.only(bottom: 8.0),
                  child: InkWell(
                    onTap: () {
                      if (_selectedOptionId != null) {
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(
                            content: Text("⚠️ Answer already recorded! Tap 'Reset Choice' to clear and retry."),
                            duration: Duration(seconds: 2),
                          ),
                        );
                        return;
                      }
                      setState(() {
                        _selectedOptionId = option.id;
                      });
                      widget.onSolutionRevealed?.call();
                    },
                    borderRadius: BorderRadius.circular(10),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                      decoration: BoxDecoration(
                        color: optBgColor,
                        borderRadius: BorderRadius.circular(10),
                        border: Border.all(color: optBorderColor),
                      ),
                      child: Row(
                        children: [
                          Container(
                            width: 26,
                            height: 26,
                            alignment: Alignment.center,
                            decoration: BoxDecoration(
                              color: isSelected
                                  ? (option.isCorrect ? const Color(0xFF16A34A) : AppTheme.dangerRose)
                                  : Colors.white,
                              shape: BoxShape.circle,
                              border: Border.all(
                                color: isSelected
                                    ? (option.isCorrect ? const Color(0xFF16A34A) : AppTheme.dangerRose)
                                    : AppTheme.borderSubtle,
                              ),
                            ),
                            child: Text(
                              option.id,
                              style: TextStyle(
                                fontSize: 12,
                                fontWeight: FontWeight.bold,
                                color: isSelected ? Colors.white : AppTheme.textSecondary,
                              ),
                            ),
                          ),
                          const SizedBox(width: 10),
                          Expanded(
                            child: Text(
                              option.text,
                              style: const TextStyle(
                                fontSize: 13.5,
                                color: AppTheme.textPrimary,
                              ),
                            ),
                          ),
                          if (optTrailing != null) optTrailing,
                        ],
                      ),
                    ),
                  ),
                );
              }),
              if (_selectedOptionId != null)
                Padding(
                  padding: const EdgeInsets.only(bottom: 4.0),
                  child: Align(
                    alignment: Alignment.centerRight,
                    child: TextButton.icon(
                      onPressed: () {
                        setState(() {
                          _selectedOptionId = null;
                          _isSolutionVisible = false;
                        });
                      },
                      icon: const Icon(Icons.refresh, size: 14, color: AppTheme.textSecondary),
                      label: const Text('Reset Choice', style: TextStyle(fontSize: 11, color: AppTheme.textSecondary)),
                    ),
                  ),
                ),
              const SizedBox(height: 8),
            ],

            // Solution Toggle Button with Option Selection Guard
            Center(
              child: TextButton.icon(
                onPressed: () {
                  if (widget.question.isMCQ && _selectedOptionId == null) {
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                        content: Text('⚠️ Please attempt by selecting an option first before revealing the solution!'),
                        duration: Duration(seconds: 2),
                        backgroundColor: AppTheme.dangerRose,
                      ),
                    );
                    return;
                  }
                  setState(() {
                    _isSolutionVisible = !_isSolutionVisible;
                  });
                  if (_isSolutionVisible) {
                    widget.onSolutionRevealed?.call();
                  }
                },
                icon: Icon(
                  (widget.question.isMCQ && _selectedOptionId == null)
                      ? Icons.lock_outline
                      : (_isSolutionVisible ? Icons.visibility_off_outlined : Icons.visibility_outlined),
                  size: 18,
                  color: (widget.question.isMCQ && _selectedOptionId == null)
                      ? Colors.grey.shade500
                      : AppTheme.primaryBlue,
                ),
                label: Text(
                  (widget.question.isMCQ && _selectedOptionId == null)
                      ? 'Select an option above to unlock solution'
                      : (_isSolutionVisible ? 'Hide Step-by-Step Solution' : 'Reveal Step-by-Step Solution'),
                  style: TextStyle(
                    fontSize: 13,
                    fontWeight: FontWeight.w600,
                    color: (widget.question.isMCQ && _selectedOptionId == null)
                        ? Colors.grey.shade500
                        : AppTheme.primaryBlue,
                  ),
                ),
              ),
            ),

            // Animated Revealed Solution Panel
            AnimatedCrossFade(
              firstChild: const SizedBox.shrink(),
              secondChild: Container(
                width: double.infinity,
                margin: const EdgeInsets.only(top: 8),
                padding: const EdgeInsets.all(14),
                decoration: BoxDecoration(
                  color: const Color(0xFFF1F5F9),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: const Color(0xFFCBD5E1)),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Row(
                      children: [
                        Icon(Icons.verified_outlined, size: 16, color: Color(0xFF0F766E)),
                        SizedBox(width: 6),
                        Text(
                          'Verified NCERT Board Solution',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.bold,
                            color: Color(0xFF0F766E),
                          ),
                        ),
                      ],
                    ),
                    const Divider(height: 16),
                    Text(
                      q.stepByStepSolution,
                      style: const TextStyle(
                        fontSize: 13.5,
                        height: 1.5,
                        color: Color(0xFF1E293B),
                        fontFamily: 'monospace',
                      ),
                    ),
                  ],
                ),
              ),
              crossFadeState: _isSolutionVisible ? CrossFadeState.showSecond : CrossFadeState.showFirst,
              duration: const Duration(milliseconds: 250),
            ),
          ],
        ),
      ),
    );
  }
}
