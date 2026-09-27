import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/theme/app_theme.dart';
import '../../models/chapter.dart';
import '../../models/question.dart';
import '../../providers/chapter_provider.dart';
import '../../providers/questions_provider.dart';
import '../../widgets/offline_status_badge.dart';
import '../../widgets/solution_toggle_card.dart';
import 'chapter_formula_screen.dart';

/// Interactive Practice Screen for a Specific Mathematics Chapter
/// Displays approved questions with exercise filtering (Exercise 1.1, Exercise 1.2),
/// step-by-step solutions, MCQ selection, progress recording, and empty state.
class ChapterPracticeScreen extends ConsumerStatefulWidget {
  final Chapter chapter;

  const ChapterPracticeScreen({super.key, required this.chapter});

  @override
  ConsumerState<ChapterPracticeScreen> createState() => _ChapterPracticeScreenState();
}

class _ChapterPracticeScreenState extends ConsumerState<ChapterPracticeScreen> {
  String _activeFilter = 'All';

  @override
  Widget build(BuildContext context) {
    final questionsAsync = ref.watch(approvedQuestionsProvider);
    final progressMap = ref.watch(chapterProgressProvider);
    final solvedIds = progressMap[widget.chapter.id] ??
        ref.read(chapterProgressProvider.notifier).getSolvedForChapter(widget.chapter.id);

    return Scaffold(
      appBar: AppBar(
        title: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(widget.chapter.titleEn, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
            Text(
              '${widget.chapter.titleKn} • Practice Q&A',
              style: const TextStyle(fontSize: 11, color: AppTheme.textSecondary, fontWeight: FontWeight.normal),
            ),
          ],
        ),
        actions: const [
          Padding(
            padding: EdgeInsets.only(right: 14.0),
            child: Center(child: OfflineStatusBadge()),
          ),
        ],
      ),
      body: questionsAsync.when(
        data: (allQuestions) {
          // Filter questions belonging to this chapter
          final chapterQuestions = allQuestions.where((q) {
            return q.subject == Subject.math &&
                (q.chapterId == widget.chapter.id ||
                    q.chapterId == widget.chapter.id.replaceFirst('math_', '') ||
                    widget.chapter.id == 'math_${q.chapterId}');
          }).toList();

          if (chapterQuestions.isEmpty) {
            return _buildEmptyState(context);
          }

          // Detect exercises present in question text (e.g., Exercise 1.1, Exercise 1.2)
          final Set<String> detectedExercises = {'All'};
          for (final q in chapterQuestions) {
            final match = RegExp(r'\[(Exercise\s+\d+\.\d+)').firstMatch(q.questionText);
            if (match != null) {
              detectedExercises.add(match.group(1)!);
            }
          }
          final exerciseFilters = detectedExercises.toList();

          // Filter by active exercise tab
          final displayedQuestions = _activeFilter == 'All'
              ? chapterQuestions
              : chapterQuestions.where((q) => q.questionText.contains(_activeFilter)).toList();

          final solvedCount = chapterQuestions.where((q) => solvedIds.contains(q.id)).length;
          final progressPercent = chapterQuestions.isNotEmpty ? (solvedCount / chapterQuestions.length) : 0.0;

          return Column(
            children: [
              // Chapter Progress Bar Header
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                color: Colors.white,
                child: Column(
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text(
                          '$solvedCount of ${chapterQuestions.length} Questions Completed',
                          style: const TextStyle(fontSize: 12.5, fontWeight: FontWeight.bold),
                        ),
                        Text(
                          '${(progressPercent * 100).toInt()}%',
                          style: const TextStyle(
                            fontSize: 12.5,
                            fontWeight: FontWeight.bold,
                            color: AppTheme.mathColor,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 6),
                    ClipRRect(
                      borderRadius: BorderRadius.circular(4),
                      child: LinearProgressIndicator(
                        value: progressPercent,
                        backgroundColor: Colors.grey.shade200,
                        valueColor: const AlwaysStoppedAnimation<Color>(AppTheme.mathColor),
                        minHeight: 6,
                      ),
                    ),
                  ],
                ),
              ),

              // Exercise Filter Chips (if multiple exercises exist)
              if (exerciseFilters.length > 1)
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                  decoration: const BoxDecoration(
                    color: Color(0xFFF1F5F9),
                    border: Border(bottom: BorderSide(color: Color(0xFFE2E8F0))),
                  ),
                  child: SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Row(
                      children: exerciseFilters.map((ex) {
                        final isSelected = _activeFilter == ex;
                        final count = ex == 'All'
                            ? chapterQuestions.length
                            : chapterQuestions.where((q) => q.questionText.contains(ex)).length;

                        return Padding(
                          padding: const EdgeInsets.only(right: 8.0),
                          child: ChoiceChip(
                            label: Text(
                              '$ex ($count)',
                              style: TextStyle(
                                fontSize: 11.5,
                                fontWeight: FontWeight.bold,
                                color: isSelected ? Colors.white : const Color(0xFF334155),
                              ),
                            ),
                            selected: isSelected,
                            selectedColor: AppTheme.mathColor,
                            backgroundColor: Colors.white,
                            onSelected: (selected) {
                              if (selected) setState(() => _activeFilter = ex);
                            },
                          ),
                        );
                      }).toList(),
                    ),
                  ),
                ),

              // Questions List
              Expanded(
                child: ListView.builder(
                  padding: const EdgeInsets.all(16),
                  itemCount: displayedQuestions.length,
                  itemBuilder: (context, index) {
                    final question = displayedQuestions[index];
                    final isSolved = solvedIds.contains(question.id);

                    return Padding(
                      padding: const EdgeInsets.only(bottom: 14.0),
                      child: Stack(
                        children: [
                          SolutionToggleCard(
                            question: question,
                            index: index + 1,
                            onSolutionRevealed: () {
                              ref.read(chapterProgressProvider.notifier).markSolved(question.id, widget.chapter.id);
                            },
                          ),
                          if (isSolved)
                            Positioned(
                              top: 12,
                              right: 12,
                              child: Container(
                                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                                decoration: BoxDecoration(
                                  color: const Color(0xFF10B981).withOpacity(0.12),
                                  borderRadius: BorderRadius.circular(12),
                                  border: Border.all(color: const Color(0xFF10B981).withOpacity(0.3)),
                                ),
                                child: const Row(
                                  mainAxisSize: MainAxisSize.min,
                                  children: [
                                    Icon(Icons.check_circle, size: 14, color: Color(0xFF10B981)),
                                    SizedBox(width: 4),
                                    Text(
                                      'Solved',
                                      style: TextStyle(
                                        fontSize: 10.5,
                                        fontWeight: FontWeight.bold,
                                        color: Color(0xFF10B981),
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            ),
                        ],
                      ),
                    );
                  },
                ),
              ),
            ],
          );
        },
        loading: () => const Center(
          child: CircularProgressIndicator(color: AppTheme.mathColor),
        ),
        error: (e, st) => Center(
          child: Padding(
            padding: const EdgeInsets.all(24.0),
            child: Text('Error loading chapter questions: $e', style: const TextStyle(color: AppTheme.dangerRose)),
          ),
        ),
      ),
    );
  }

  /// Informative, friendly empty state when a chapter has not yet been seeded
  Widget _buildEmptyState(BuildContext context) {
    return Center(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(28.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Container(
              width: 80,
              height: 80,
              decoration: BoxDecoration(
                color: Colors.amber.shade50,
                shape: BoxShape.circle,
                border: Border.all(color: Colors.amber.shade200, width: 2),
              ),
              child: Icon(Icons.auto_stories_outlined, size: 40, color: Colors.amber.shade800),
            ),
            const SizedBox(height: 20),
            Text(
              'Questions Under Preparation',
              style: TextStyle(
                fontSize: 18,
                fontWeight: FontWeight.bold,
                color: const Color(0xFF1E293B),
              ),
            ),
            const SizedBox(height: 8),
            Text(
              'The question bank for ${widget.chapter.titleEn} (${widget.chapter.titleKn}) is currently being seeded and reviewed by the academic faculty.\n\nApproved questions will appear here automatically. In the meantime, you can master all key identities in the Formula Cheat-Sheet!',
              textAlign: TextAlign.center,
              style: const TextStyle(
                fontSize: 13.5,
                color: AppTheme.textSecondary,
                height: 1.5,
              ),
            ),
            const SizedBox(height: 24),
            ElevatedButton.icon(
              style: ElevatedButton.styleFrom(
                backgroundColor: AppTheme.mathColor,
                padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 12),
                shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
              ),
              onPressed: () {
                Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(builder: (_) => ChapterFormulaScreen(chapter: widget.chapter)),
                );
              },
              icon: const Icon(Icons.functions, size: 18),
              label: const Text('Open Chapter Formulas', style: TextStyle(fontWeight: FontWeight.bold)),
            ),
          ],
        ),
      ),
    );
  }
}
