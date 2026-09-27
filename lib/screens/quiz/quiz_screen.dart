import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/theme/app_theme.dart';
import '../../models/question.dart';
import '../../providers/quiz_provider.dart';
import 'quiz_result_screen.dart';

class QuizScreen extends ConsumerStatefulWidget {
  final Subject subject;

  const QuizScreen({super.key, required this.subject});

  @override
  ConsumerState<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends ConsumerState<QuizScreen> {
  int _currentQuestionIndex = 0;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      ref.read(quizSessionProvider.notifier).startQuiz(subject: widget.subject);
    });
  }

  String _formatTime(int seconds) {
    final m = seconds ~/ 60;
    final s = seconds % 60;
    return '${m.toString().padLeft(2, '0')}:${s.toString().padLeft(2, '0')}';
  }

  @override
  Widget build(BuildContext context) {
    final session = ref.watch(quizSessionProvider);

    if (session == null) {
      return const Scaffold(
        body: Center(child: CircularProgressIndicator()),
      );
    }

    if (session.isCompleted) {
      return QuizResultScreen(session: session);
    }

    if (session.questions.isEmpty) {
      return Scaffold(
        appBar: AppBar(title: Text('${widget.subject.displayName} Quiz')),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Icon(Icons.info_outline, size: 48, color: Colors.grey),
              const SizedBox(height: 12),
              const Text('No MCQ questions currently available for this quiz.'),
              const SizedBox(height: 16),
              ElevatedButton(
                onPressed: () => Navigator.pop(context),
                child: const Text('Back to Modules'),
              ),
            ],
          ),
        ),
      );
    }

    final currentQuestion = session.questions[_currentQuestionIndex];
    final selectedOptionId = session.selectedAnswers[currentQuestion.id];
    final isLowTime = session.remainingSeconds < 60;

    return PopScope(
      canPop: false,
      onPopInvoked: (didPop) {
        if (didPop) return;
        _showExitConfirmationDialog();
      },
      child: Scaffold(
        appBar: AppBar(
          title: Text(
            '${widget.subject.displayName} Practice Quiz',
            style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
          ),
          actions: [
            // Timer Badge
            Container(
              margin: const EdgeInsets.only(right: 16),
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
              decoration: BoxDecoration(
                color: isLowTime ? AppTheme.dangerRose.withOpacity(0.12) : AppTheme.primaryBlue.withOpacity(0.1),
                borderRadius: BorderRadius.circular(20),
                border: Border.all(
                  color: isLowTime ? AppTheme.dangerRose : AppTheme.primaryBlue,
                ),
              ),
              child: Row(
                children: [
                  Icon(
                    Icons.timer_outlined,
                    size: 16,
                    color: isLowTime ? AppTheme.dangerRose : AppTheme.primaryBlue,
                  ),
                  const SizedBox(width: 4),
                  Text(
                    _formatTime(session.remainingSeconds),
                    style: TextStyle(
                      fontWeight: FontWeight.bold,
                      fontSize: 13,
                      color: isLowTime ? AppTheme.dangerRose : AppTheme.primaryBlue,
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
        body: SafeArea(
          child: Column(
            children: [
              // Progress Bar
              LinearProgressIndicator(
                value: (session.answeredCount) / session.totalQuestions,
                backgroundColor: AppTheme.borderSubtle,
                valueColor: AlwaysStoppedAnimation<Color>(widget.subject.themeColor),
              ),

              Expanded(
                child: SingleChildScrollView(
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // Question tracker header
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Text(
                            'Question ${_currentQuestionIndex + 1} of ${session.totalQuestions}',
                            style: const TextStyle(
                              fontSize: 14,
                              fontWeight: FontWeight.bold,
                              color: AppTheme.textSecondary,
                            ),
                          ),
                          Text(
                            'Answered: ${session.answeredCount}/${session.totalQuestions}',
                            style: const TextStyle(
                              fontSize: 12,
                              fontWeight: FontWeight.w600,
                              color: AppTheme.successEmerald,
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 12),

                      // Question Text Box
                      Container(
                        width: double.infinity,
                        padding: const EdgeInsets.all(16),
                        decoration: BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.circular(14),
                          border: Border.all(color: AppTheme.borderSubtle),
                        ),
                        child: Text(
                          currentQuestion.questionText,
                          style: const TextStyle(
                            fontSize: 15.5,
                            fontWeight: FontWeight.w600,
                            height: 1.45,
                            color: AppTheme.textPrimary,
                          ),
                        ),
                      ),
                      const SizedBox(height: 20),

                      // MCQ Options
                      if (currentQuestion.options != null) ...[
                        ...currentQuestion.options!.map((option) {
                          final isSelected = selectedOptionId == option.id;

                          return Padding(
                            padding: const EdgeInsets.only(bottom: 10.0),
                            child: InkWell(
                              onTap: () {
                                ref.read(quizSessionProvider.notifier).selectOption(
                                      currentQuestion.id,
                                      option.id,
                                    );
                              },
                              borderRadius: BorderRadius.circular(12),
                              child: Container(
                                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
                                decoration: BoxDecoration(
                                  color: isSelected ? widget.subject.themeColor.withOpacity(0.08) : Colors.white,
                                  borderRadius: BorderRadius.circular(12),
                                  border: Border.all(
                                    color: isSelected ? widget.subject.themeColor : AppTheme.borderSubtle,
                                    width: isSelected ? 2 : 1,
                                  ),
                                ),
                                child: Row(
                                  children: [
                                    Container(
                                      width: 28,
                                      height: 28,
                                      alignment: Alignment.center,
                                      decoration: BoxDecoration(
                                        color: isSelected ? widget.subject.themeColor : Colors.white,
                                        shape: BoxShape.circle,
                                        border: Border.all(
                                          color: isSelected ? widget.subject.themeColor : AppTheme.borderSubtle,
                                        ),
                                      ),
                                      child: Text(
                                        option.id,
                                        style: TextStyle(
                                          fontSize: 12.5,
                                          fontWeight: FontWeight.bold,
                                          color: isSelected ? Colors.white : AppTheme.textSecondary,
                                        ),
                                      ),
                                    ),
                                    const SizedBox(width: 12),
                                    Expanded(
                                      child: Text(
                                        option.text,
                                        style: TextStyle(
                                          fontSize: 14,
                                          fontWeight: isSelected ? FontWeight.w600 : FontWeight.normal,
                                          color: AppTheme.textPrimary,
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          );
                        }),
                      ],
                    ],
                  ),
                ),
              ),

              // Navigation Controls Bottom Bar
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                decoration: const BoxDecoration(
                  color: Colors.white,
                  border: Border(top: BorderSide(color: AppTheme.borderSubtle)),
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    OutlinedButton(
                      onPressed: _currentQuestionIndex > 0
                          ? () {
                              setState(() {
                                _currentQuestionIndex--;
                              });
                            }
                          : null,
                      child: const Text('Previous'),
                    ),
                    if (_currentQuestionIndex < session.totalQuestions - 1)
                      ElevatedButton(
                        onPressed: () {
                          setState(() {
                            _currentQuestionIndex++;
                          });
                        },
                        child: const Text('Next Question'),
                      )
                    else
                      ElevatedButton(
                        style: ElevatedButton.styleFrom(
                          backgroundColor: AppTheme.successEmerald,
                        ),
                        onPressed: _showSubmitConfirmationDialog,
                        child: const Text('Submit Quiz'),
                      ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _showSubmitConfirmationDialog() {
    final session = ref.read(quizSessionProvider);
    final unattempted = session != null ? session.unattemptedCount : 0;

    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Submit Quiz?'),
        content: Text(
          unattempted > 0
              ? 'You have $unattempted unattempted question(s). Are you sure you want to finalize and evaluate now?'
              : 'All questions attempted! Ready to view your detailed scorecard?',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text('Review Answers'),
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.pop(ctx);
              ref.read(quizSessionProvider.notifier).submitQuiz();
            },
            child: const Text('Submit & Finish'),
          ),
        ],
      ),
    );
  }

  void _showExitConfirmationDialog() {
    showDialog(
      context: context,
      builder: (ctx) => AlertDialog(
        title: const Text('Abandon Quiz?'),
        content: const Text('Your current progress will not be evaluated if you leave.'),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(ctx),
            child: const Text('Resume Quiz'),
          ),
          ElevatedButton(
            style: ElevatedButton.styleFrom(backgroundColor: AppTheme.dangerRose),
            onPressed: () {
              Navigator.pop(ctx);
              ref.read(quizSessionProvider.notifier).resetQuiz();
              Navigator.pop(context);
            },
            child: const Text('Leave'),
          ),
        ],
      ),
    );
  }
}
