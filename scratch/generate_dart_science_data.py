import json
import re

with open("assets/data/ncert_science_ch1.json", encoding="utf-8") as f:
    questions = json.load(f)

def escape_dart_str(s):
    if not s:
        return ""
    # escape backslashes and single quotes and dollar signs
    s = s.replace('\\', '\\\\')
    s = s.replace("'", "\\'")
    s = s.replace('$', '\\$')
    return s

lines = []
lines.append("import '../models/question.dart';")
lines.append("")
lines.append("/// Pre-seeded 100% NCERT-verified questions for CBSE Class 10 Science Chapter 1 (Chemical Reactions and Equations)")
lines.append("/// In-Text Questions (Pages 6, 10, 13) and End-of-Chapter Exercises (Pages 14-16)")
lines.append("class NcertScienceCh1Data {")
lines.append("  static List<Question> get questions => [")

for idx, q in enumerate(questions, 1):
    qid = q["id"]
    qtext = escape_dart_str(q["text"])
    sol = escape_dart_str(q.get("solution", ""))
    diff = q.get("difficulty", "medium")
    if diff not in ["easy", "medium", "hard", "hots"]:
        diff = "medium"
        
    lines.append("    Question(")
    lines.append(f"      id: '{qid}',")
    lines.append("      subject: Subject.science,")
    lines.append("      chapterId: 'sci_ch_01_chemical_reactions_equations',")
    lines.append(f"      questionText: '{qtext}',")
    lines.append("      options: const [")
    for opt in q["options"]:
        oid = opt["id"]
        otext = escape_dart_str(opt["text"])
        is_c = "true" if opt.get("is_correct") or opt.get("correct") else "false"
        lines.append(f"        QuestionOption(id: '{oid}', text: '{otext}', isCorrect: {is_c}),")
    lines.append("      ],")
    lines.append(f"      stepByStepSolution: '{sol}',")
    lines.append(f"      difficultyLevel: DifficultyLevel.{diff},")
    lines.append("      status: QuestionStatus.approved,")
    lines.append("      submittedBy: '00000000-0000-0000-0000-000000000001',")
    lines.append("      reviewedBy: '00000000-0000-0000-0000-000000000001',")
    lines.append(f"      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + {idx * 1000}),")
    lines.append("    ),")

lines.append("  ];")
lines.append("}")
lines.append("")

out_file = "lib/services/ncert_science_ch1_data.dart"
with open(out_file, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"Generated {out_file} with {len(questions)} Dart Question definitions.")
