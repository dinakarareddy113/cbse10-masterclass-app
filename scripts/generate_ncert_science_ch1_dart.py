import json
import os

def escape_dart_str(val):
    if val is None:
        return "''"
    # Format as a clean raw multi-line string if it contains newlines or LaTeX $ symbols
    val_clean = str(val).replace('\r\n', '\n')
    # If using r'''...''', ensure no ''' inside
    val_clean = val_clean.replace("'''", "\\'\\'\\'")
    if val_clean.endswith("'"):
        val_clean += " "
    return f"r'''{val_clean}'''"

def escape_dart_single_line(val):
    if val is None:
        return "''"
    val_clean = str(val).replace('\r\n', ' ').replace('\n', ' ').strip()
    val_clean = val_clean.replace('\\', '\\\\').replace("'", "\\'").replace('$', '\\$')
    return f"'{val_clean}'"

def generate():
    with open('assets/data/ncert_science_ch1.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)

    lines = [
        "import '../models/question.dart';",
        "",
        "/// Pre-seeded 100% NCERT-verified questions for CBSE Class 10 Science Chapter 1 (Chemical Reactions and Equations)",
        "/// In-Text Questions (Pages 6, 10, 13) and End-of-Chapter Exercises (Pages 14-16)",
        "class NcertScienceCh1Data {",
        "  static List<Question> get questions => [",
    ]

    for idx, q in enumerate(questions):
        qid = q.get('id', f'sci_ch1_q_{idx+1}')
        qtext = escape_dart_str(q.get('text', q.get('question_text', '')))
        sol = escape_dart_str(q.get('step_by_step_solution', q.get('solution', '')))
        diff = q.get('difficulty', q.get('difficulty_level', 'medium')).lower()
        if diff not in ['easy', 'medium', 'hard', 'hots']:
            diff = 'medium'

        lines.append("    Question(")
        lines.append(f"      id: '{qid}',")
        lines.append("      subject: Subject.science,")
        lines.append("      chapterId: 'sci_ch_01_chemical_reactions_equations',")
        lines.append(f"      questionText: {qtext},")
        
        # Options
        opts = q.get('options', [])
        if opts:
            lines.append("      options: const [")
            for opt in opts:
                opt_id = opt.get('id', 'A')
                opt_text = escape_dart_single_line(opt.get('text', ''))
                is_correct = 'true' if opt.get('is_correct', False) else 'false'
                lines.append(f"        QuestionOption(id: '{opt_id}', text: {opt_text}, isCorrect: {is_correct}),")
            lines.append("      ],")
        else:
            lines.append("      options: null,")
            
        lines.append(f"      stepByStepSolution: {sol},")
        lines.append(f"      difficultyLevel: DifficultyLevel.{diff},")
        lines.append("      status: QuestionStatus.approved,")
        lines.append("      submittedBy: '00000000-0000-0000-0000-000000000001',")
        lines.append("      reviewedBy: '00000000-0000-0000-0000-000000000001',")
        lines.append(f"      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + {idx * 1000}),")
        lines.append("    ),")

    lines.append("  ];")
    lines.append("}")
    lines.append("")

    out_path = 'lib/services/ncert_science_ch1_data.dart'
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Generated {len(questions)} clean questions in {out_path}")

if __name__ == '__main__':
    generate()
