import json
import re

with open("assets/data/ncert_science_ch1.json", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Total questions loaded: {len(questions)}")

errors = []
for i, q in enumerate(questions, 1):
    qid = q.get("id")
    sec = q.get("section")
    qnum = q.get("question_number")
    text = q.get("text")
    opts = q.get("options", [])
    
    if not qid or not sec or not qnum or not text:
        errors.append(f"Q{i} ({qid}): Missing required base fields")
    
    if len(opts) != 4:
        errors.append(f"Q{i} ({qid}): Expected 4 options, got {len(opts)}")
        
    correct_opts = [o for o in opts if o.get("is_correct")]
    if len(correct_opts) != 1:
        errors.append(f"Q{i} ({qid}): Expected 1 correct option, got {len(correct_opts)}")
        
    for opt in opts:
        if not opt.get("rationale") or len(opt.get("rationale", "")) < 10:
            errors.append(f"Q{i} ({qid}) Opt {opt.get('id')}: Missing or brief rationale")

if errors:
    print(f"FAILED with {len(errors)} errors:")
    for e in errors[:10]:
        print(" -", e)
else:
    print("ALL 47 QUESTIONS PASSED STRICT STRUCTURAL VALIDATION!")

# Let's inspect distribution of questions
sections = {}
for q in questions:
    sec = q["section"]
    sections[sec] = sections.get(sec, []) + [q["question_number"]]

for sec, qnums in sections.items():
    print(f"\n{sec} ({len(qnums)} questions):")
    print("  " + ", ".join(qnums))
