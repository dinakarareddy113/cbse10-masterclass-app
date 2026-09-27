import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/constants/cbse_curriculum.dart';
import '../../core/theme/app_theme.dart';
import '../../models/question.dart';
import '../../providers/questions_provider.dart';
import '../../widgets/offline_status_badge.dart';
import '../../widgets/solution_toggle_card.dart';

class ScienceModuleScreen extends ConsumerStatefulWidget {
  const ScienceModuleScreen({super.key});

  @override
  ConsumerState<ScienceModuleScreen> createState() => _ScienceModuleScreenState();
}

class _ScienceModuleScreenState extends ConsumerState<ScienceModuleScreen>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 4, vsync: this);
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
        title: const Text('CBSE Class 10 • Science'),
        actions: const [
          Padding(
            padding: EdgeInsets.only(right: 12.0),
            child: Center(child: OfflineStatusBadge()),
          ),
        ],
        bottom: TabBar(
          controller: _tabController,
          isScrollable: true,
          labelColor: AppTheme.scienceColor,
          unselectedLabelColor: AppTheme.textSecondary,
          indicatorColor: AppTheme.scienceColor,
          indicatorWeight: 3,
          tabs: const [
            Tab(icon: Icon(Icons.flash_on_outlined), text: 'Physics: Ray Diagrams'),
            Tab(icon: Icon(Icons.science_outlined), text: 'Chemistry: Equations'),
            Tab(icon: Icon(Icons.biotech_outlined), text: 'Biology: Flowcharts'),
            Tab(icon: Icon(Icons.quiz_outlined), text: 'Questions Bank'),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          _buildPhysicsRayDiagramsTab(),
          _buildChemistryEquationsTab(),
          _buildBiologyFlowchartsTab(),
          _buildScienceQuestionsTab(),
        ],
      ),
    );
  }

  /// 1. Physics: Ray Diagrams & Conceptual Checks
  Widget _buildPhysicsRayDiagramsTab() {
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: CbseCurriculum.sciencePhysicsRayDiagrams.length,
      itemBuilder: (context, index) {
        final item = CbseCurriculum.sciencePhysicsRayDiagrams[index];
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
                      padding: const EdgeInsets.all(8),
                      decoration: BoxDecoration(
                        color: AppTheme.scienceColor.withOpacity(0.12),
                        borderRadius: BorderRadius.circular(8),
                      ),
                      child: const Icon(Icons.remove_red_eye_outlined, color: AppTheme.scienceColor, size: 20),
                    ),
                    const SizedBox(width: 10),
                    Expanded(
                      child: Text(
                        item['title'] as String,
                        style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14.5),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 12),
                Container(
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: const Color(0xFF0F172A),
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Text(
                    item['ascii_ray'] as String,
                    style: const TextStyle(
                      fontFamily: 'monospace',
                      fontSize: 12,
                      color: Color(0xFF38BDF8),
                      height: 1.4,
                    ),
                  ),
                ),
                const SizedBox(height: 12),
                _buildInfoRow('Object Position:', item['position_object'] as String),
                _buildInfoRow('Image Position:', item['position_image'] as String),
                _buildInfoRow('Nature of Image:', item['nature_image'] as String),
                _buildInfoRow('Magnification:', item['magnification'] as String),
                _buildInfoRow('Real-life Application:', item['application'] as String),
              ],
            ),
          ),
        );
      },
    );
  }

  /// 2. Chemistry: Equation Lookups & Balancer
  Widget _buildChemistryEquationsTab() {
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: CbseCurriculum.scienceChemistryEquations.length,
      itemBuilder: (context, index) {
        final item = CbseCurriculum.scienceChemistryEquations[index];
        return Card(
          margin: const EdgeInsets.only(bottom: 16),
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                  decoration: BoxDecoration(
                    color: AppTheme.scienceColor.withOpacity(0.1),
                    borderRadius: BorderRadius.circular(6),
                  ),
                  child: Text(
                    item['reaction_type'] as String,
                    style: const TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.bold,
                      color: AppTheme.scienceColor,
                    ),
                  ),
                ),
                const SizedBox(height: 8),
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(12),
                  decoration: BoxDecoration(
                    color: const Color(0xFFF1F5F9),
                    borderRadius: BorderRadius.circular(8),
                    border: Border.all(color: const Color(0xFFCBD5E1)),
                  ),
                  child: Text(
                    item['equation'] as String,
                    style: const TextStyle(
                      fontFamily: 'monospace',
                      fontSize: 14,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFF0F172A),
                    ),
                  ),
                ),
                const SizedBox(height: 10),
                _buildInfoRow('Reactants:', item['reactants'] as String),
                _buildInfoRow('Products:', item['products'] as String),
                _buildInfoRow('Key Observation:', item['observation'] as String),
              ],
            ),
          ),
        );
      },
    );
  }

  /// 3. Biology: Process Flowcharts
  Widget _buildBiologyFlowchartsTab() {
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: CbseCurriculum.scienceBiologyFlowcharts.length,
      itemBuilder: (context, index) {
        final item = CbseCurriculum.scienceBiologyFlowcharts[index];
        final steps = List<String>.from(item['steps'] as List);

        return Card(
          margin: const EdgeInsets.only(bottom: 16),
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    const Icon(Icons.account_tree_outlined, color: AppTheme.scienceColor),
                    const SizedBox(width: 8),
                    Expanded(
                      child: Text(
                        item['topic'] as String,
                        style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 6),
                Text(
                  item['summary'] as String,
                  style: const TextStyle(fontSize: 12.5, color: AppTheme.textSecondary),
                ),
                const Divider(height: 20),
                ...steps.map((step) => Padding(
                      padding: const EdgeInsets.symmetric(vertical: 4.0),
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Icon(Icons.arrow_right_alt, color: AppTheme.scienceColor, size: 20),
                          const SizedBox(width: 6),
                          Expanded(
                            child: Text(
                              step,
                              style: const TextStyle(fontSize: 13, height: 1.4),
                            ),
                          ),
                        ],
                      ),
                    )),
              ],
            ),
          ),
        );
      },
    );
  }

  /// 4. Science Questions Bank
  Widget _buildScienceQuestionsTab() {
    final questionsAsync = ref.watch(approvedQuestionsProvider);

    return questionsAsync.when(
      data: (questions) {
        final sciQuestions = questions.where((q) => q.subject == Subject.science).toList();
        if (sciQuestions.isEmpty) {
          return const Center(child: Text('No Science questions available.'));
        }

        return ListView.builder(
          padding: const EdgeInsets.all(16),
          itemCount: sciQuestions.length,
          itemBuilder: (context, index) {
            return SolutionToggleCard(
              question: sciQuestions[index],
              index: index + 1,
            );
          },
        );
      },
      loading: () => const Center(child: CircularProgressIndicator()),
      error: (e, st) => Center(child: Text('Error: $e')),
    );
  }

  Widget _buildInfoRow(String label, String value) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 3.0),
      child: RichText(
        text: TextSpan(
          text: '$label ',
          style: const TextStyle(
            fontSize: 12.5,
            fontWeight: FontWeight.bold,
            color: AppTheme.textPrimary,
          ),
          children: [
            TextSpan(
              text: value,
              style: const TextStyle(
                fontWeight: FontWeight.normal,
                color: AppTheme.textSecondary,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
