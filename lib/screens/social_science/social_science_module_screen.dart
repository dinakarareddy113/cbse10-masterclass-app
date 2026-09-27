import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/constants/cbse_curriculum.dart';
import '../../core/theme/app_theme.dart';
import '../../models/question.dart';
import '../../providers/questions_provider.dart';
import '../../widgets/offline_status_badge.dart';
import '../../widgets/solution_toggle_card.dart';

class SocialScienceModuleScreen extends ConsumerStatefulWidget {
  const SocialScienceModuleScreen({super.key});

  @override
  ConsumerState<SocialScienceModuleScreen> createState() => _SocialScienceModuleScreenState();
}

class _SocialScienceModuleScreenState extends ConsumerState<SocialScienceModuleScreen>
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
        title: const Text('CBSE Class 10 • Social Science'),
        actions: const [
          Padding(
            padding: EdgeInsets.only(right: 12.0),
            child: Center(child: OfflineStatusBadge()),
          ),
        ],
        bottom: TabBar(
          controller: _tabController,
          isScrollable: true,
          labelColor: AppTheme.socialScienceColor,
          unselectedLabelColor: AppTheme.textSecondary,
          indicatorColor: AppTheme.socialScienceColor,
          indicatorWeight: 3,
          tabs: const [
            Tab(icon: Icon(Icons.timeline_outlined), text: 'History: Timeline'),
            Tab(icon: Icon(Icons.map_outlined), text: 'Geography: Map Guide'),
            Tab(icon: Icon(Icons.gavel_outlined), text: 'Civics: Amendments'),
            Tab(icon: Icon(Icons.quiz_outlined), text: 'Question Bank'),
          ],
        ),
      ),
      body: TabBarView(
        controller: _tabController,
        children: [
          _buildHistoryTimelineTab(),
          _buildGeographyMapGuideTab(),
          _buildCivicsAmendmentsTab(),
          _buildSstQuestionsTab(),
        ],
      ),
    );
  }

  /// 1. History: Interactive Historical Timeline
  Widget _buildHistoryTimelineTab() {
    return ListView.builder(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
      itemCount: CbseCurriculum.sstHistoryTimelines.length,
      itemBuilder: (context, index) {
        final event = CbseCurriculum.sstHistoryTimelines[index];
        final isLast = index == CbseCurriculum.sstHistoryTimelines.length - 1;

        return IntrinsicHeight(
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Timeline Column (Dot and Line)
              Column(
                children: [
                  Container(
                    width: 16,
                    height: 16,
                    decoration: BoxDecoration(
                      color: AppTheme.socialScienceColor,
                      shape: BoxShape.circle,
                      border: Border.all(color: Colors.white, width: 3),
                      boxShadow: [
                        BoxShadow(
                          color: AppTheme.socialScienceColor.withOpacity(0.4),
                          blurRadius: 4,
                        ),
                      ],
                    ),
                  ),
                  if (!isLast)
                    Expanded(
                      child: Container(
                        width: 2,
                        color: AppTheme.socialScienceColor.withOpacity(0.3),
                      ),
                    ),
                ],
              ),
              const SizedBox(width: 14),

              // Content Card
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.only(bottom: 20.0),
                  child: Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: AppTheme.borderSubtle),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                          decoration: BoxDecoration(
                            color: AppTheme.socialScienceColor.withOpacity(0.12),
                            borderRadius: BorderRadius.circular(4),
                          ),
                          child: Text(
                            event['year'] as String,
                            style: const TextStyle(
                              fontSize: 11,
                              fontWeight: FontWeight.bold,
                              color: AppTheme.socialScienceColor,
                            ),
                          ),
                        ),
                        const SizedBox(height: 6),
                        Text(
                          event['title'] as String,
                          style: const TextStyle(
                            fontSize: 14.5,
                            fontWeight: FontWeight.bold,
                            color: AppTheme.textPrimary,
                          ),
                        ),
                        const SizedBox(height: 4),
                        Text(
                          event['description'] as String,
                          style: const TextStyle(
                            fontSize: 12.5,
                            color: AppTheme.textSecondary,
                            height: 1.4,
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ],
          ),
        );
      },
    );
  }

  /// 2. Geography: Map-pointing Study Guides
  Widget _buildGeographyMapGuideTab() {
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: CbseCurriculum.sstMapStudyGuide.length,
      itemBuilder: (context, index) {
        final category = CbseCurriculum.sstMapStudyGuide[index];
        final items = List<Map<String, dynamic>>.from(category['items'] as List);

        return Card(
          margin: const EdgeInsets.only(bottom: 16),
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    const Icon(Icons.pin_drop_outlined, color: AppTheme.socialScienceColor),
                    const SizedBox(width: 8),
                    Expanded(
                      child: Text(
                        category['category'] as String,
                        style: const TextStyle(fontSize: 15.5, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ],
                ),
                const Divider(height: 20),
                ...items.map((item) {
                  return Container(
                    margin: const EdgeInsets.only(bottom: 10),
                    padding: const EdgeInsets.all(10),
                    decoration: BoxDecoration(
                      color: AppTheme.neutralBg,
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text(
                              item['name'] as String,
                              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 13),
                            ),
                            Container(
                              padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 2),
                              decoration: BoxDecoration(
                                color: Colors.blueGrey.shade100,
                                borderRadius: BorderRadius.circular(4),
                              ),
                              child: Text(
                                item['state'] as String,
                                style: TextStyle(fontSize: 10.5, color: Colors.blueGrey.shade800),
                              ),
                            ),
                          ],
                        ),
                        if (item.containsKey('river')) ...[
                          const SizedBox(height: 2),
                          Text(
                            'River: ${item['river']}',
                            style: const TextStyle(fontSize: 11.5, color: AppTheme.textSecondary),
                          ),
                        ],
                        if (item.containsKey('significance')) ...[
                          const SizedBox(height: 4),
                          Text(
                            item['significance'] as String,
                            style: const TextStyle(fontSize: 11.5, color: Color(0xFF334155)),
                          ),
                        ],
                      ],
                    ),
                  );
                }),
              ],
            ),
          ),
        );
      },
    );
  }

  /// 3. Civics: Constitutional Amendments & Federalism
  Widget _buildCivicsAmendmentsTab() {
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: CbseCurriculum.sstCivicsAmendments.length,
      itemBuilder: (context, index) {
        final item = CbseCurriculum.sstCivicsAmendments[index];
        final points = List<String>.from(item['key_points'] as List);

        return Card(
          margin: const EdgeInsets.only(bottom: 16),
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    const Icon(Icons.account_balance_outlined, color: AppTheme.socialScienceColor),
                    const SizedBox(width: 8),
                    Expanded(
                      child: Text(
                        item['title'] as String,
                        style: const TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 4),
                Text(
                  'Core Focus: ${item['focus']}',
                  style: const TextStyle(
                    fontSize: 12,
                    fontWeight: FontWeight.w600,
                    color: AppTheme.socialScienceColor,
                  ),
                ),
                const Divider(height: 20),
                ...points.map(
                  (pt) => Padding(
                    padding: const EdgeInsets.symmetric(vertical: 4.0),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Icon(Icons.check_circle_outline, size: 16, color: AppTheme.socialScienceColor),
                        const SizedBox(width: 8),
                        Expanded(
                          child: Text(
                            pt,
                            style: const TextStyle(fontSize: 12.5, height: 1.4),
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        );
      },
    );
  }

  /// 4. Social Science Questions Bank
  Widget _buildSstQuestionsTab() {
    final questionsAsync = ref.watch(approvedQuestionsProvider);

    return questionsAsync.when(
      data: (questions) {
        final sstQuestions = questions.where((q) => q.subject == Subject.socialScience).toList();
        if (sstQuestions.isEmpty) {
          return const Center(child: Text('No Social Science questions available.'));
        }

        return ListView.builder(
          padding: const EdgeInsets.all(16),
          itemCount: sstQuestions.length,
          itemBuilder: (context, index) {
            return SolutionToggleCard(
              question: sstQuestions[index],
              index: index + 1,
            );
          },
        );
      },
      loading: () => const Center(child: CircularProgressIndicator()),
      error: (e, st) => Center(child: Text('Error: $e')),
    );
  }
}
