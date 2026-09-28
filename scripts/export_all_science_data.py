import re
import json
import os

with open('mobile_test/index.html', encoding='utf-8') as f:
    html = f.read()

def extract_js_array(var_name):
    start_str = f"const {var_name} = ["
    start_idx = html.find(start_str)
    if start_idx == -1:
        print(f"Could not find {var_name}")
        return []
    start_bracket = html.find("[", start_idx)
    count = 0
    in_string = False
    escape = False
    quote_char = ''
    end_idx = -1
    for i in range(start_bracket, len(html)):
        c = html[i]
        if escape:
            escape = False
            continue
        if c == '\\':
            escape = True
            continue
        if in_string:
            if c == quote_char:
                in_string = False
            continue
        if c in ('"', "'"):
            in_string = True
            quote_char = c
            continue
        if c == '[':
            count += 1
        elif c == ']':
            count -= 1
            if count == 0:
                end_idx = i + 1
                break
    raw_json = html[start_bracket:end_idx]
    try:
        return json.loads(raw_json)
    except Exception:
        cleaned = re.sub(r',\s*([}\]])', r'\1', raw_json)
        return json.loads(cleaned)


def dart_str_literal(s):
    if s is None:
        return "''"
    dumped = json.dumps(str(s), ensure_ascii=False)
    dumped = dumped.replace('$', r'\$')
    return dumped


def convert_to_dart(var_name, questions, class_name, chapter_id):
    lines = []
    lines.append("import '../models/question.dart';")
    lines.append("")
    lines.append(f"/// Pre-seeded NCERT-verified questions for {class_name}")
    lines.append(f"class {class_name} {{")
    lines.append("  static List<Question> get questions => [")
    
    for i, q in enumerate(questions):
        qid = q.get('id', f'{chapter_id}_q{i+1}')
        qtext = q.get('text') or q.get('question_text') or ''
        section = q.get('section') or q.get('exercise') or ''
        if section and not qtext.startswith('['):
            qtext = f"[{section}] {qtext}"
            
        sol = q.get('solution') or q.get('step_by_step_solution') or ''
        diff = q.get('difficulty', 'medium')
        diff_enum = 'DifficultyLevel.easy' if diff == 'easy' else ('DifficultyLevel.hots' if diff in ('hots', 'hard') else 'DifficultyLevel.medium')
        
        lines.append("    Question(")
        lines.append(f"      id: {dart_str_literal(qid)},")
        lines.append("      subject: Subject.science,")
        lines.append(f"      chapterId: {dart_str_literal(chapter_id)},")
        lines.append(f"      questionText: {dart_str_literal(qtext)},")
        lines.append("      options: const [")
        
        for opt in q.get('options', []):
            oid = opt.get('id', 'A')
            otext = opt.get('text', '')
            is_cor = 'true' if (opt.get('is_correct') or opt.get('correct')) else 'false'
            lines.append(f"        QuestionOption(id: {dart_str_literal(oid)}, text: {dart_str_literal(otext)}, isCorrect: {is_cor}),")
            
        lines.append("      ],")
        lines.append(f"      stepByStepSolution: {dart_str_literal(sol)},")
        lines.append(f"      difficultyLevel: {diff_enum},")
        lines.append("      status: QuestionStatus.approved,")
        lines.append("      submittedBy: '00000000-0000-0000-0000-000000000001',")
        lines.append("      reviewedBy: '00000000-0000-0000-0000-000000000001',")
        lines.append(f"      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + {i * 1000}),")
        lines.append("    ),")
        
    lines.append("  ];")
    lines.append("}")
    lines.append("")
    return '\n'.join(lines)


# Process Science Chapter 2
ch2_q = extract_js_array('scienceCh2MasterQuestions')
print(f"Extracted Ch2: {len(ch2_q)} questions")
if ch2_q:
    dart_code = convert_to_dart('scienceCh2MasterQuestions', ch2_q, 'NcertScienceCh2Data', 'sci_ch_02_acids_bases_salts')
    with open('lib/services/ncert_science_ch2_data.dart', 'w', encoding='utf-8') as out:
        out.write(dart_code)
    print("Wrote lib/services/ncert_science_ch2_data.dart")

# Process Science Chapter 3
ch3_q = extract_js_array('scienceCh3MasterQuestions')
print(f"Extracted Ch3: {len(ch3_q)} questions")
if ch3_q:
    dart_code = convert_to_dart('scienceCh3MasterQuestions', ch3_q, 'NcertScienceCh3Data', 'sci_ch_03_metals_non_metals')
    with open('lib/services/ncert_science_ch3_data.dart', 'w', encoding='utf-8') as out:
        out.write(dart_code)
    print("Wrote lib/services/ncert_science_ch3_data.dart")

# Process Science Chapter 4
ch4_q = extract_js_array('scienceCh4MasterQuestions')
print(f"Extracted Ch4: {len(ch4_q)} questions")
if ch4_q:
    dart_code = convert_to_dart('scienceCh4MasterQuestions', ch4_q, 'NcertScienceCh4Data', 'sci_ch_04_carbon_compounds')
    with open('lib/services/ncert_science_ch4_data.dart', 'w', encoding='utf-8') as out:
        out.write(dart_code)
    print("Wrote lib/services/ncert_science_ch4_data.dart")

# Process Science Chapter 5
ch5_q = extract_js_array('scienceCh5MasterQuestions')
print(f"Extracted Ch5: {len(ch5_q)} questions")
if ch5_q:
    dart_code = convert_to_dart('scienceCh5MasterQuestions', ch5_q, 'NcertScienceCh5Data', 'sci_ch_05_life_processes')
    with open('lib/services/ncert_science_ch5_data.dart', 'w', encoding='utf-8') as out:
        out.write(dart_code)
    print("Wrote lib/services/ncert_science_ch5_data.dart")
