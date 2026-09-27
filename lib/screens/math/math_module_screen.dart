import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/constants/cbse_curriculum.dart';
import '../../core/theme/app_theme.dart';
import '../../models/question.dart';
import '../../providers/questions_provider.dart';
import '../../widgets/offline_status_badge.dart';
import '../../widgets/solution_toggle_card.dart';

class MathModuleScreen extends ConsumerStatefulWidget {
  const MathModuleScreen({super.key});

  @override
  ConsumerState<MathModuleScreen> createState() => _MathModuleScreenState();
}

class _MathModuleScreenState extends ConsumerState<MathModuleScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
  }

  @override
  void dispose() {
    _tabController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('CBSE Class 10 • Mathematics'),
        actions: const [
          Padding(
            padding: EdgeInsets.only(right: 12.0),
            child: Center(child: OfflineStatusBadge()),
          ),
        ],
        bottom: TabBar(
          controller: _tabController,
          labelColor: AppTheme.mathColor,
          unselectedLabelColor: AppTheme.textSecondary,
          indicatorColor: AppTheme.mathColor,
          indicatorWeight: 3,
          tabs: const [
            Tab(icon: Icon(Icons.menu_book_outlined), text: 'Formula Sheet'),
            Tab(icon: Icon(Icons.quiz_outlined), text: 'Question Bank'),
            Tab(icon: Icon(Icons.local_fire_department_outlined), text: 'HOTS Vault'),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          _buildFormulaCheatSheetTab(),
          _buildQuestionBankTab(onlyHots: false),
          _buildQuestionBankTab(onlyHots: true),
        ],
      ),
    );
  }

  /// Tab 1: Formula Cheat-Sheet & Chapter Summaries
  Widget _buildFormulaCheatSheetTab() {
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: CbseCurriculum.mathChapters.length,
      itemBuilder: (context, index) {
        final chapter = CbseCurriculum.mathChapters[index];
        final formulas = List<String>.from(chapter['formulas'] as List);

        return Card(
          margin: const EdgeInsets.only(bottom: 16),
          child: ExpansionTile(
            initiallyExpanded: index == 0 || index == 2, // Expand Real Numbers & Quadratic by default
            leading: CircleAvatar(
              backgroundColor: AppTheme.mathColor.withOpacity(0.12),
              child: Text(
                '${index + 1}',
                style: const TextStyle(
                  color: AppTheme.mathColor,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            title: Text(
              chapter['title'] as String,
              style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 15),
            ),
            subtitle: Text(
              chapter['summary'] as String,
              style: const TextStyle(fontSize: 12.5, color: AppTheme.textSecondary),
            ),
            children: [
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(16),
                decoration: const BoxDecoration(
                  color: Color(0xFFF8FAFC),
                  borderRadius: BorderRadius.vertical(bottom: Radius.circular(16)),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Row(
                      children: [
                        Icon(Icons.functions, size: 16, color: AppTheme.mathColor),
                        SizedBox(width: 6),
                        Text(
                          'Essential Formulas & Theorems',
                          style: TextStyle(
                            fontSize: 12,
                            fontWeight: FontWeight.bold,
                            color: AppTheme.mathColor,
                            letterSpacing: 0.5,
                          ),
                        ),
                      ],
                    ),
                    const SizedBox(height: 8),
                    ...formulas.map(
                      (formula) => Padding(
                        padding: const EdgeInsets.symmetric(vertical: 4.0),
                        child: Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Text('• ', style: TextStyle(fontWeight: FontWeight.bold, color: AppTheme.mathColor)),
                            Expanded(
                              child: Text(
                                formula,
                                style: const TextStyle(
                                  fontSize: 13,
                                  fontFamily: 'monospace',
                                  fontWeight: FontWeight.w600,
                                  color: Color(0xFF1E293B),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  /// Tab 2 & 3: Mathematics Questions (with toggle solutions) & HOTS Questions
  Widget _buildQuestionBankTab({required bool onlyHots}) {
    final questionsAsync = ref.watch(approvedQuestionsProvider);

    return questionsAsync.when(
      data: (questions) {
        final mathQuestions = questions.where((q) => q.subject == Subject.math).toList();
        final filteredList = onlyHots
            ? mathQuestions.where((q) => q.difficultyLevel == DifficultyLevel.hots).toList()
            : mathQuestions;

        if (filteredList.isEmpty) {
          return Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  onlyHots ? Icons.local_fire_department : Icons.menu_book,
                  size: 48,
                  color: Colors.grey.shade400,
                ),
                const SizedBox(height: 12),
                Text(
                  onlyHots
                      ? 'No High Order Thinking Skills (HOTS) questions yet.'
                      : 'No approved Mathematics questions found.',
                  style: const TextStyle(color: AppTheme.textSecondary),
                ),
              ],
            ),
          );
        }

        return ListView.builder(
          padding: const EdgeInsets.all(16),
          itemCount: filteredList.length,
          itemBuilder: (context, index) {
            return SolutionToggleCard(
              question: filteredList[index],
              index: index + 1,
            );
          },
        );
      },
      loading: () => const Center(child: CircularProgressIndicator()),
      error: (e, st) => Center(
        child: Padding(
          padding: const EdgeInsets.all(24.0),
          child: Text('Error loading questions: $e', style: const TextStyle(color: AppTheme.dangerRose)),
        ),
      ),
    );
  }
}
