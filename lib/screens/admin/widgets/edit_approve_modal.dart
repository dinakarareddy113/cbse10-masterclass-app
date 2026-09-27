import 'package:flutter/material.dart';
import '../../../core/theme/app_theme.dart';
import '../../../models/question.dart';

typedef EditAndApproveCallback = void Function({
  required String updatedQuestionText,
  required List<QuestionOption>? updatedOptions,
  required String updatedSolution,
  required DifficultyLevel updatedDifficulty,
});

class EditApproveModal extends StatefulWidget {
  final Question question;
  final EditAndApproveCallback onSaveAndApprove;

  const EditApproveModal({
    super.key,
    required this.question,
    required this.onSaveAndApprove,
  });

  static Future<void> show({
    required BuildContext context,
    required Question question,
    required EditAndApproveCallback onSaveAndApprove,
  }) {
    return showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.white,
      shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(20)),
      ),
      builder: (ctx) => EditApproveModal(
        question: question,
        onSaveAndApprove: onSaveAndApprove,
      ),
    );
  }

  @override
  State<EditApproveModal> createState() => _EditApproveModalState();
}

class _EditApproveModalState extends State<EditApproveModal> {
  final _formKey = GlobalKey<FormState>();
  late TextEditingController _questionTextController;
  late TextEditingController _solutionController;
  late DifficultyLevel _selectedDifficulty;

  late List<TextEditingController> _optionControllers;
  String _correctOptionId = 'A';

  @override
  void initState() {
    super.initState();
    _questionTextController = TextEditingController(text: widget.question.questionText);
    _solutionController = TextEditingController(text: widget.question.stepByStepSolution);
    _selectedDifficulty = widget.question.difficultyLevel;

    _optionControllers = [];
    if (widget.question.options != null) {
      for (final opt in widget.question.options!) {
        _optionControllers.add(TextEditingController(text: opt.text));
        if (opt.isCorrect) {
          _correctOptionId = opt.id;
        }
      }
    }
  }

  @override
  void dispose() {
    _questionTextController.dispose();
    _solutionController.dispose();
    for (final c in _optionControllers) {
      c.dispose();
    }
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final bottomInset = MediaQuery.of(context).viewInsets.bottom;

    return Padding(
      padding: EdgeInsets.only(
        left: 20,
        right: 20,
        top: 20,
        bottom: bottomInset + 20,
      ),
      child: Form(
        key: _formKey,
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            mainAxisSize: MainAxisSize.min,
            children: [
              // Header
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  const Row(
                    children: [
                      Icon(Icons.edit_note_outlined, color: AppTheme.primaryBlue, size: 24),
                      SizedBox(width: 8),
                      Text(
                        'Edit & Publish Question',
                        style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                      ),
                    ],
                  ),
                  IconButton(
                    icon: const Icon(Icons.close),
                    onPressed: () => Navigator.pop(context),
                  ),
                ],
              ),
              const Divider(height: 16),

              // Difficulty Selector
              Row(
                children: [
                  const Text('Difficulty Level: ', style: TextStyle(fontWeight: FontWeight.w600)),
                  const SizedBox(width: 10),
                  DropdownButton<DifficultyLevel>(
                    value: _selectedDifficulty,
                    underline: const SizedBox.shrink(),
                    items: DifficultyLevel.values.map((lvl) {
                      return DropdownMenuItem(
                        value: lvl,
                        child: Text(lvl.label, style: TextStyle(color: lvl.badgeColor, fontWeight: FontWeight.bold)),
                      );
                    }).toList(),
                    onChanged: (val) {
                      if (val != null) setState(() => _selectedDifficulty = val);
                    },
                  ),
                ],
              ),
              const SizedBox(height: 14),

              // Question Text Field
              const Text('Question Text & LaTeX Equations', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
              const SizedBox(height: 6),
              TextFormField(
                controller: _questionTextController,
                maxLines: 3,
                decoration: const InputDecoration(
                  hintText: 'Enter complete question text...',
                ),
                validator: (val) => val == null || val.trim().isEmpty ? 'Question text is required' : null,
              ),
              const SizedBox(height: 16),

              // MCQ Options Editor
              if (widget.question.options != null && _optionControllers.length == widget.question.options!.length) ...[
                const Text('MCQ Options (Select the correct answer button)',
                    style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
                const SizedBox(height: 6),
                ...widget.question.options!.asMap().entries.map((entry) {
                  final idx = entry.key;
                  final opt = entry.value;
                  final isCorrect = _correctOptionId == opt.id;

                  return Padding(
                    padding: const EdgeInsets.only(bottom: 8.0),
                    child: Row(
                      children: [
                        IconButton(
                          icon: Icon(
                            isCorrect ? Icons.radio_button_checked : Icons.radio_button_off,
                            color: isCorrect ? AppTheme.successEmerald : Colors.grey,
                          ),
                          onPressed: () {
                            setState(() => _correctOptionId = opt.id);
                          },
                        ),
                        Text('${opt.id}: ', style: const TextStyle(fontWeight: FontWeight.bold)),
                        const SizedBox(width: 6),
                        Expanded(
                          child: TextFormField(
                            controller: _optionControllers[idx],
                            decoration: InputDecoration(
                              isDense: true,
                              contentPadding: const EdgeInsets.symmetric(horizontal: 10, vertical: 8),
                              hintText: 'Option ${opt.id} text',
                            ),
                            validator: (val) => val == null || val.trim().isEmpty ? 'Option required' : null,
                          ),
                        ),
                      ],
                    ),
                  );
                }),
                const SizedBox(height: 12),
              ],

              // Step-by-Step Solution Editor
              const Text('Step-by-Step Verified Solution', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
              const SizedBox(height: 6),
              TextFormField(
                controller: _solutionController,
                maxLines: 5,
                style: const TextStyle(fontFamily: 'monospace', fontSize: 13),
                decoration: const InputDecoration(
                  hintText: 'Step 1: ...\nStep 2: ...',
                ),
                validator: (val) => val == null || val.trim().isEmpty ? 'Solution is required' : null,
              ),
              const SizedBox(height: 20),

              // Action Buttons
              Row(
                children: [
                  Expanded(
                    child: OutlinedButton(
                      onPressed: () => Navigator.pop(context),
                      child: const Text('Cancel'),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: ElevatedButton.icon(
                      style: ElevatedButton.styleFrom(
                        backgroundColor: AppTheme.successEmerald,
                      ),
                      onPressed: _handleSaveAndApprove,
                      icon: const Icon(Icons.check_circle_outline),
                      label: const Text('Save & Publish Live'),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _handleSaveAndApprove() {
    if (_formKey.currentState?.validate() ?? false) {
      List<QuestionOption>? updatedOptions;
      if (widget.question.options != null) {
        updatedOptions = [];
        for (int i = 0; i < widget.question.options!.length; i++) {
          final originalOpt = widget.question.options![i];
          updatedOptions.add(
            QuestionOption(
              id: originalOpt.id,
              text: _optionControllers[i].text.trim(),
              isCorrect: originalOpt.id == _correctOptionId,
            ),
          );
        }
      }

      widget.onSaveAndApprove(
        updatedQuestionText: _questionTextController.text.trim(),
        updatedOptions: updatedOptions,
        updatedSolution: _solutionController.text.trim(),
        updatedDifficulty: _selectedDifficulty,
      );

      Navigator.pop(context);
    }
  }
}
