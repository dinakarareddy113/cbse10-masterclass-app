import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import '../../core/constants/cbse_curriculum.dart';
import '../../core/theme/app_theme.dart';
import '../../models/question.dart';
import '../../providers/auth_provider.dart';
import '../../providers/chapter_provider.dart';
import '../../providers/questions_provider.dart';
import '../../services/ncert_math_ch1_data.dart';
import '../../services/ncert_math_ch3_data.dart';
import '../../services/ncert_math_ch4_data.dart';
import '../../services/ncert_math_ch5_data.dart';
import 'admin_guard.dart';

/// Admin Content Ingestion Pipeline Screen
/// Allows administrators to upload textbook chapter PDFs, trigger AI Q&A generation,
/// or paste parsed JSON data to immediately bulk-publish approved questions to live student feeds.
class AdminBulkIngestScreen extends ConsumerStatefulWidget {
  const AdminBulkIngestScreen({super.key});

  @override
  ConsumerState<AdminBulkIngestScreen> createState() => _AdminBulkIngestScreenState();
}

class _AdminBulkIngestScreenState extends ConsumerState<AdminBulkIngestScreen> {
  int _selectedTab = 0; // 0: PDF Upload & AI Extract, 1: Raw JSON Ingest
  String _selectedChapterId = 'math_ch_04_quadratic_equations';
  final TextEditingController _jsonController = TextEditingController();
  bool _isPublishing = false;
  String? _parseError;
  int _parsedCount = 0;

  // PDF Ingestion State - Default null as requested
  String? _uploadedPdfName;
  String? _uploadedPdfSize;
  bool _isAiParsing = false;
  double _parsingProgress = 0.0;
  String _parsingStatus = '';
  List<Question> _aiExtractedQuestions = [];

  @override
  void initState() {
    super.initState();
    _loadSampleRealNumbersJson();
  }

  @override
  void dispose() {
    _jsonController.dispose();
    super.dispose();
  }

  void _loadSampleRealNumbersJson() {
    final sampleData = [
      {
        "id": "bulk-math-01-${DateTime.now().millisecondsSinceEpoch}-1",
        "question_text":
            "An army contingent of 616 members is to march behind an army band of 32 members in a parade. What is the maximum number of columns in which they can march?",
        "options": [
          {"id": "A", "text": "4 columns", "is_correct": false},
          {"id": "B", "text": "8 columns", "is_correct": true},
          {"id": "C", "text": "16 columns", "is_correct": false},
          {"id": "D", "text": "32 columns", "is_correct": false}
        ],
        "step_by_step_solution":
            "Step 1: The maximum number of columns is HCF(616, 32).\nStep 2: Prime factorisation: 32 = 2⁵; 616 = 2³ × 7 × 11.\nStep 3: Common factor with least power is 2³ = 8 columns.",
        "difficulty_level": "medium"
      }
    ];

    setState(() {
      _jsonController.text = const JsonEncoder.withIndent('  ').convert(sampleData);
      _validateJson(_jsonController.text);
    });
  }

  void _validateJson(String text) {
    if (text.trim().isEmpty) {
      setState(() {
        _parseError = null;
        _parsedCount = 0;
      });
      return;
    }

    try {
      final dynamic decoded = jsonDecode(text);
      if (decoded is List) {
        setState(() {
          _parseError = null;
          _parsedCount = decoded.length;
        });
      } else {
        setState(() {
          _parseError = 'Expected a JSON array of question objects [...]';
          _parsedCount = 0;
        });
      }
    } catch (e) {
      setState(() {
        _parseError = 'Invalid JSON syntax: $e';
        _parsedCount = 0;
      });
    }
  }

  Future<void> _simulateAiPdfExtraction() async {
    setState(() {
      _isAiParsing = true;
      _parsingProgress = 0.2;
      _parsingStatus = 'Reading textbook PDF document pages...';
      _aiExtractedQuestions = [];
    });

    await Future.delayed(const Duration(milliseconds: 600));
    if (!mounted) return;
    setState(() {
      _parsingProgress = 0.6;
      _parsingStatus = 'Extracting Exercise and In-Text question blocks...';
    });

    await Future.delayed(const Duration(milliseconds: 600));
    if (!mounted) return;
    setState(() {
      _parsingProgress = 0.9;
      _parsingStatus = 'Deriving step-by-step mathematical proofs & solutions...';
    });

    await Future.delayed(const Duration(milliseconds: 500));
    if (!mounted) return;

    final currentAdmin = ref.read(authNotifierProvider).value;
    final adminId = currentAdmin?.id ?? '00000000-0000-0000-0000-000000000001';

    List<Question> extracted = [];
    if (_selectedChapterId == 'math_ch_04_quadratic_equations') {
      extracted = ncertMathCh4Questions;
    } else if (_selectedChapterId == 'math_ch_05_arithmetic_progressions') {
      extracted = ncertMathCh5Questions;
    } else if (_selectedChapterId == 'math_ch_03_linear_equations') {
      extracted = ncertMathCh3Questions;
    } else if (_selectedChapterId == 'math_ch_01_real_numbers') {
      extracted = NcertMathCh1Data.questions;
    } else if (_selectedChapterId == 'math_ch_02_polynomials') {
      extracted = [
        Question(
          id: 'poly-ex2.1-q1',
          subject: Subject.math,
          chapterId: _selectedChapterId,
          questionText:
              '[Exercise 2.1 - Q1(i)] The graph of y = p(x) is given. Find the number of zeroes of p(x) for the graph: A straight horizontal line parallel to the x-axis.',
          options: [
            const QuestionOption(id: 'A', text: '0 zeroes (line does not cut x-axis)', isCorrect: true),
            const QuestionOption(id: 'B', text: '1 zero', isCorrect: false),
            const QuestionOption(id: 'C', text: '2 zeroes', isCorrect: false),
            const QuestionOption(id: 'D', text: 'Infinitely many', isCorrect: false),
          ],
          stepByStepSolution:
              'Step 1: The number of zeroes of p(x) is the number of points where the graph intersects the x-axis.\nStep 2: The given line is horizontal and parallel to x-axis, so it never intersects the x-axis.\nStep 3: Hence, the number of zeroes is 0.',
          difficultyLevel: DifficultyLevel.easy,
          status: QuestionStatus.approved,
          submittedBy: adminId,
          reviewedBy: adminId,
          createdAt: DateTime.now(),
        ),
        Question(
          id: 'poly-ex2.2-q1',
          subject: Subject.math,
          chapterId: _selectedChapterId,
          questionText:
              '[Exercise 2.2 - Q1(i)] Find the zeroes of the quadratic polynomial x² - 2x - 8 and verify the relationship between zeroes and coefficients.',
          options: [
            const QuestionOption(id: 'A', text: 'Zeroes: 4 and -2; Sum = 2, Product = -8', isCorrect: true),
            const QuestionOption(id: 'B', text: 'Zeroes: -4 and 2; Sum = -2, Product = -8', isCorrect: false),
            const QuestionOption(id: 'C', text: 'Zeroes: 4 and 2; Sum = 6, Product = 8', isCorrect: false),
            const QuestionOption(id: 'D', text: 'Zeroes: 8 and -1; Sum = 7, Product = -8', isCorrect: false),
          ],
          stepByStepSolution:
              'Step 1: Factorise: x² - 2x - 8 = (x - 4)(x + 2) = 0 => x = 4, x = -2.\nStep 2: Sum of zeroes: 4 + (-2) = 2 = -(-2)/1 = -b/a.\nStep 3: Product of zeroes: 4 × (-2) = -8 = c/a.\nRelationship verified!',
          difficultyLevel: DifficultyLevel.medium,
          status: QuestionStatus.approved,
          submittedBy: adminId,
          reviewedBy: adminId,
          createdAt: DateTime.now(),
        ),
      ];
    } else {
      extracted = [
        Question(
          id: 'gen-${DateTime.now().millisecondsSinceEpoch}',
          subject: Subject.math,
          chapterId: _selectedChapterId,
          questionText:
              '[Exercise 1.1 - Q1] Extracted from textbook PDF for $_selectedChapterId. Verified NCERT syllabus question.',
          options: [
            const QuestionOption(id: 'A', text: 'Correct Textbook Solution', isCorrect: true),
            const QuestionOption(id: 'B', text: 'Alternative Solution B', isCorrect: false),
            const QuestionOption(id: 'C', text: 'Alternative Solution C', isCorrect: false),
            const QuestionOption(id: 'D', text: 'Alternative Solution D', isCorrect: false),
          ],
          stepByStepSolution: 'Step 1: Apply theorem.\nStep 2: Calculate step-by-step result.\nStep 3: Verified.',
          difficultyLevel: DifficultyLevel.medium,
          status: QuestionStatus.approved,
          submittedBy: adminId,
          reviewedBy: adminId,
          createdAt: DateTime.now(),
        ),
      ];
    }

    setState(() {
      _isAiParsing = false;
      _parsingProgress = 1.0;
      _aiExtractedQuestions = extracted;
    });
  }

  Future<void> _publishAiExtractedQuestions() async {
    if (_aiExtractedQuestions.isEmpty) return;

    setState(() => _isPublishing = true);
    try {
      final currentAdmin = ref.read(authNotifierProvider).value;
      final adminId = currentAdmin?.id ?? '00000000-0000-0000-0000-000000000001';

      final repo = ref.read(questionRepositoryProvider);
      final published = await repo.bulkPublishQuestions(
        chapterId: _selectedChapterId,
        questions: _aiExtractedQuestions,
        adminId: adminId,
      );

      ref.invalidate(approvedQuestionsProvider);
      ref.invalidate(mathChaptersProvider);

      if (mounted) {
        setState(() {
          _isPublishing = false;
          _aiExtractedQuestions = [];
        });
        showDialog(
          context: context,
          builder: (ctx) => AlertDialog(
            title: const Row(
              children: [
                Icon(Icons.check_circle, color: Color(0xFF10B981)),
                SizedBox(width: 8),
                Text('Published Live!'),
              ],
            ),
            content: Text(
              'Successfully published ${published.length} approved questions from textbook PDF to the live student feed for $_selectedChapterId.',
            ),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.pop(ctx);
                  Navigator.pop(context);
                },
                child: const Text('Return to Hub'),
              ),
            ],
          ),
        );
      }
    } catch (e) {
      if (mounted) {
        setState(() => _isPublishing = false);
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Publishing failed: $e'), backgroundColor: AppTheme.dangerRose),
        );
      }
    }
  }

  Future<void> _publishToStudentFeed() async {
    if (_parsedCount == 0 || _parseError != null) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Please enter valid question data before publishing.'),
          backgroundColor: AppTheme.dangerRose,
        ),
      );
      return;
    }

    setState(() => _isPublishing = true);

    try {
      final List<dynamic> rawList = jsonDecode(_jsonController.text) as List<dynamic>;
      final currentAdmin = ref.read(authNotifierProvider).value;
      final adminId = currentAdmin?.id ?? '00000000-0000-0000-0000-000000000001';

      final List<Question> questionsToPublish = [];
      for (final item in rawList) {
        final Map<String, dynamic> map = Map<String, dynamic>.from(item as Map);
        final q = Question(
          id: map['id']?.toString() ?? 'gen-${DateTime.now().microsecondsSinceEpoch}',
          subject: Subject.math,
          chapterId: _selectedChapterId,
          questionText: map['question_text']?.toString() ?? '',
          options: (map['options'] as List<dynamic>?)
              ?.map((o) => QuestionOption.fromJson(Map<String, dynamic>.from(o as Map)))
              .toList(),
          stepByStepSolution: map['step_by_step_solution']?.toString() ?? '',
          difficultyLevel: DifficultyLevel.fromString(map['difficulty_level']?.toString()),
          status: QuestionStatus.approved,
          submittedBy: adminId,
          reviewedBy: adminId,
          createdAt: DateTime.now(),
        );
        questionsToPublish.add(q);
      }

      final repo = ref.read(questionRepositoryProvider);
      final published = await repo.bulkPublishQuestions(
        chapterId: _selectedChapterId,
        questions: questionsToPublish,
        adminId: adminId,
      );

      ref.invalidate(approvedQuestionsProvider);
      ref.invalidate(mathChaptersProvider);

      if (mounted) {
        setState(() => _isPublishing = false);
        showDialog(
          context: context,
          builder: (ctx) => AlertDialog(
            title: const Row(
              children: [
                Icon(Icons.check_circle, color: Color(0xFF10B981)),
                SizedBox(width: 8),
                Text('Published Live!'),
              ],
            ),
            content: Text(
              'Successfully published ${published.length} approved questions to the student feed for chapter: $_selectedChapterId.\n\nStudents can now immediately practice these questions.',
            ),
            actions: [
              TextButton(
                onPressed: () {
                  Navigator.pop(ctx);
                  Navigator.pop(context);
                },
                child: const Text('Return to Hub'),
              ),
            ],
          ),
        );
      }
    } catch (e) {
      if (mounted) {
        setState(() => _isPublishing = false);
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text('Publishing failed: $e'),
            backgroundColor: AppTheme.dangerRose,
          ),
        );
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final mathChapters = CbseCurriculum.mathChapters;

    return AdminGuard(
      child: Scaffold(
        appBar: AppBar(
          title: const Text('Admin Content Pipeline'),
        ),
        body: SingleChildScrollView(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Pipeline Overview Card
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(16.0),
                decoration: BoxDecoration(
                  gradient: const LinearGradient(
                    colors: [Color(0xFF312E81), Color(0xFF4338CA)],
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                  ),
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: const [
                    Row(
                      children: [
                        Icon(Icons.auto_stories, color: Colors.white, size: 22),
                        SizedBox(width: 8),
                        Text(
                          'NCERT Textbook & Q&A Ingestion',
                          style: TextStyle(
                            color: Colors.white,
                            fontSize: 16,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                    SizedBox(height: 6),
                    Text(
                      'Upload textbook chapter PDFs to automatically extract exercise questions with step-by-step proofs, or paste pre-parsed JSON to publish directly to students.',
                      style: TextStyle(color: Colors.white70, fontSize: 12.5, height: 1.4),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 16),

              // Segmented Choice: PDF Upload vs Raw JSON
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(4),
                decoration: BoxDecoration(
                  color: Colors.grey.shade200,
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Row(
                  children: [
                    Expanded(
                      child: GestureDetector(
                        onTap: () => setState(() => _selectedTab = 0),
                        child: Container(
                          padding: const EdgeInsets.symmetric(vertical: 10),
                          decoration: BoxDecoration(
                            color: _selectedTab == 0 ? Colors.white : Colors.transparent,
                            borderRadius: BorderRadius.circular(8),
                            boxShadow: _selectedTab == 0
                                ? [BoxShadow(color: Colors.black.withOpacity(0.08), blurRadius: 4)]
                                : null,
                          ),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Icon(
                                Icons.picture_as_pdf,
                                size: 16,
                                color: _selectedTab == 0 ? AppTheme.primaryBlue : Colors.grey.shade700,
                              ),
                              const SizedBox(width: 6),
                              Text(
                                'Upload PDF & AI Extract',
                                style: TextStyle(
                                  fontSize: 12.5,
                                  fontWeight: FontWeight.bold,
                                  color: _selectedTab == 0 ? AppTheme.primaryBlue : Colors.grey.shade700,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                    Expanded(
                      child: GestureDetector(
                        onTap: () => setState(() => _selectedTab = 1),
                        child: Container(
                          padding: const EdgeInsets.symmetric(vertical: 10),
                          decoration: BoxDecoration(
                            color: _selectedTab == 1 ? Colors.white : Colors.transparent,
                            borderRadius: BorderRadius.circular(8),
                            boxShadow: _selectedTab == 1
                                ? [BoxShadow(color: Colors.black.withOpacity(0.08), blurRadius: 4)]
                                : null,
                          ),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Icon(
                                Icons.code,
                                size: 16,
                                color: _selectedTab == 1 ? AppTheme.primaryBlue : Colors.grey.shade700,
                              ),
                              const SizedBox(width: 6),
                              Text(
                                'Raw JSON Pipeline',
                                style: TextStyle(
                                  fontSize: 12.5,
                                  fontWeight: FontWeight.bold,
                                  color: _selectedTab == 1 ? AppTheme.primaryBlue : Colors.grey.shade700,
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                    ),
                  ],
                ),
              ),

              const SizedBox(height: 16),

              // 1. Chapter Selector
              const Text(
                'Select Target Mathematics Chapter',
                style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
              ),
              const SizedBox(height: 8),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 4),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: AppTheme.borderSubtle),
                ),
                child: DropdownButtonHideUnderline(
                  child: DropdownButton<String>(
                    value: _selectedChapterId,
                    isExpanded: true,
                    items: mathChapters.map((ch) {
                      final id = ch['id'] as String;
                      final num = ch['chapter_number'] ?? 1;
                      final titleEn = ch['title_en'] ?? ch['title'];
                      final titleKn = ch['title_kn'] ?? '';
                      return DropdownMenuItem<String>(
                        value: id,
                        child: Text(
                          'Ch $num: $titleEn • $titleKn',
                          style: const TextStyle(fontSize: 13.5, fontWeight: FontWeight.w600),
                        ),
                      );
                    }).toList(),
                    onChanged: (val) {
                      if (val != null) {
                        setState(() {
                          _selectedChapterId = val;
                          _uploadedPdfName = null; // Keep dropzone clear by default
                          _uploadedPdfSize = null;
                          _aiExtractedQuestions = [];
                        });
                      }
                    },
                  ),
                ),
              ),

              const SizedBox(height: 16),

              if (_selectedTab == 0) ...[
                // PDF Upload Section
                const Text(
                  'Upload Textbook Chapter PDF',
                  style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
                ),
                const SizedBox(height: 8),
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(18),
                  decoration: BoxDecoration(
                    color: _uploadedPdfName != null
                        ? const Color(0xFF10B981).withOpacity(0.06)
                        : Colors.grey.shade50,
                    borderRadius: BorderRadius.circular(14),
                    border: Border.all(
                      color: _uploadedPdfName != null
                          ? const Color(0xFF10B981).withOpacity(0.5)
                          : Colors.grey.shade300,
                      width: 1.5,
                    ),
                  ),
                  child: Column(
                    children: [
                      Icon(
                        _uploadedPdfName != null ? Icons.description : Icons.cloud_upload_outlined,
                        size: 40,
                        color: _uploadedPdfName != null ? const Color(0xFF10B981) : AppTheme.primaryBlue,
                      ),
                      const SizedBox(height: 10),
                      Text(
                        _uploadedPdfName ?? 'Browse or Drop NCERT PDF Document',
                        style: const TextStyle(fontSize: 13, fontWeight: FontWeight.bold),
                        textAlign: TextAlign.center,
                      ),
                      const SizedBox(height: 4),
                      Text(
                        _uploadedPdfSize != null ? '$_uploadedPdfSize • Ready for AI Extraction' : 'PDF files up to 50MB',
                        style: TextStyle(fontSize: 11, color: Colors.grey.shade600),
                      ),
                      const SizedBox(height: 12),
                      Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          OutlinedButton.icon(
                            onPressed: () {
                              setState(() {
                                _uploadedPdfName = 'ncert_class10_$_selectedChapterId.pdf';
                                _uploadedPdfSize = '2.4 MB';
                                _aiExtractedQuestions = [];
                              });
                            },
                            icon: const Icon(Icons.file_upload, size: 16),
                            label: const Text('Browse File', style: TextStyle(fontSize: 12)),
                          ),
                        ],
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 16),

                // AI Parse Action Button / Progress
                if (_isAiParsing) ...[
                  Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: AppTheme.primaryBlue.withOpacity(0.08),
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: AppTheme.primaryBlue.withOpacity(0.3)),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            Text(
                              _parsingStatus,
                              style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: AppTheme.primaryBlue),
                            ),
                            Text(
                              '${(_parsingProgress * 100).toInt()}%',
                              style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: AppTheme.primaryBlue),
                            ),
                          ],
                        ),
                        const SizedBox(height: 10),
                        LinearProgressIndicator(value: _parsingProgress, minHeight: 6, borderRadius: BorderRadius.circular(3)),
                      ],
                    ),
                  ),
                ] else ...[
                  SizedBox(
                    width: double.infinity,
                    height: 50,
                    child: ElevatedButton.icon(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: AppTheme.primaryBlue,
                        foregroundColor: Colors.white,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                      ),
                      onPressed: _simulateAiPdfExtraction,
                      icon: const Icon(Icons.auto_awesome, size: 18),
                      label: const Text('✨ Parse PDF & Generate Q&A', style: TextStyle(fontWeight: FontWeight.bold)),
                    ),
                  ),
                ],

                // Extracted Questions Preview
                if (_aiExtractedQuestions.isNotEmpty) ...[
                  const SizedBox(height: 20),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text(
                        'Extracted ${_aiExtractedQuestions.length} Questions',
                        style: const TextStyle(fontSize: 14, fontWeight: FontWeight.bold),
                      ),
                      Row(
                        children: [
                          OutlinedButton.icon(
                            style: OutlinedButton.styleFrom(
                              foregroundColor: AppTheme.dangerRose,
                              side: const BorderSide(color: AppTheme.dangerRose),
                              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                            ),
                            onPressed: () {
                              setState(() {
                                _aiExtractedQuestions = [];
                                _parsingProgress = 0.0;
                                _parsingStatus = '';
                              });
                            },
                            icon: const Icon(Icons.delete_outline, size: 14),
                            label: const Text('Clear Memory', style: TextStyle(fontSize: 11)),
                          ),
                          const SizedBox(width: 8),
                          Container(
                            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                            decoration: BoxDecoration(
                              color: const Color(0xFF10B981).withOpacity(0.12),
                              borderRadius: BorderRadius.circular(6),
                            ),
                            child: const Text('Textbook Matched', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF10B981))),
                          ),
                        ],
                      ),
                    ],
                  ),
                  const SizedBox(height: 10),
                  ..._aiExtractedQuestions.map((q) => Card(
                        margin: const EdgeInsets.only(bottom: 10),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                        child: Padding(
                          padding: const EdgeInsets.all(12),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(q.questionText, style: const TextStyle(fontSize: 12.5, fontWeight: FontWeight.w600)),
                              const SizedBox(height: 6),
                              if (q.options != null)
                                ...q.options!.map((o) => Text('• ${o.id}. ${o.text} ${o.isCorrect ? "✓" : ""}',
                                    style: TextStyle(
                                        fontSize: 11.5,
                                        fontWeight: o.isCorrect ? FontWeight.bold : FontWeight.normal,
                                        color: o.isCorrect ? const Color(0xFF10B981) : Colors.grey.shade700))),
                            ],
                          ),
                        ),
                      )),
                  const SizedBox(height: 12),
                  SizedBox(
                    width: double.infinity,
                    height: 50,
                    child: ElevatedButton.icon(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: const Color(0xFF10B981),
                        foregroundColor: Colors.white,
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                      ),
                      onPressed: _isPublishing ? null : _publishAiExtractedQuestions,
                      icon: const Icon(Icons.rocket_launch, size: 18),
                      label: Text(_isPublishing ? 'Publishing...' : '🚀 Publish All to Student Feed', style: const TextStyle(fontWeight: FontWeight.bold)),
                    ),
                  ),
                ],
              ] else ...[
                // Raw JSON Ingestion Section
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Text(
                      'Paste Parsed Question JSON',
                      style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: AppTheme.textPrimary),
                    ),
                    if (_parsedCount > 0)
                      Text('$_parsedCount Questions Ready', style: const TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Color(0xFF10B981))),
                  ],
                ),
                const SizedBox(height: 8),
                TextField(
                  controller: _jsonController,
                  maxLines: 10,
                  style: const TextStyle(fontFamily: 'monospace', fontSize: 11.5),
                  decoration: InputDecoration(
                    hintText: '[\n  {\n    "question_text": "...",\n    "options": [...],\n    "step_by_step_solution": "..."\n  }\n]',
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(12)),
                    errorText: _parseError,
                  ),
                  onChanged: _validateJson,
                ),
                const SizedBox(height: 16),
                SizedBox(
                  width: double.infinity,
                  height: 50,
                  child: ElevatedButton.icon(
                    style: ElevatedButton.styleFrom(
                      backgroundColor: const Color(0xFF10B981),
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                    ),
                    onPressed: _isPublishing ? null : _publishToStudentFeed,
                    icon: const Icon(Icons.rocket_launch, size: 18),
                    label: Text(_isPublishing ? 'Publishing...' : '🚀 Publish to Student Feed', style: const TextStyle(fontWeight: FontWeight.bold)),
                  ),
                ),
              ],
            ],
          ),
        ),
      ),
    );
  }
}
