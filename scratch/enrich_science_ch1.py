import json

with open("assets/data/ncert_science_ch1.json", encoding="utf-8") as f:
    questions = json.load(f)

for q in questions:
    correct_opt = next(o for o in q["options"] if o["is_correct"])
    
    sol_lines = [
        f"Correct Answer: ({correct_opt['id']}) {correct_opt['text']}",
        f"\nScientific Principle / Key Concept:\n{correct_opt['rationale']}",
        "\nDetailed Distractor & Misconception Analysis:"
    ]
    for o in q["options"]:
        if not o["is_correct"]:
            sol_lines.append(f"• Option ({o['id']}): Incorrect. {o['rationale']}")
            
    solution_text = "\n".join(sol_lines)
    q["solution"] = solution_text
    q["step_by_step_solution"] = solution_text
    q["subject"] = "science"
    q["chapterId"] = "sci_ch_01_chemical_reactions"
    
    # Standardize exercise label
    sec = q.get("section", "")
    if "Page 6" in sec:
        q["exercise"] = "In-Text (Page 6)"
    elif "Page 10" in sec:
        q["exercise"] = "In-Text (Page 10)"
    elif "Page 13" in sec:
        q["exercise"] = "In-Text (Page 13)"
    else:
        q["exercise"] = "Exercises (Pages 14-16)"
        
    q["questionNumber"] = q.get("question_number", "")
    
    # Ensure options have both 'correct' and 'is_correct' for full cross-system compatibility
    for o in q["options"]:
        o["correct"] = o["is_correct"]

with open("assets/data/ncert_science_ch1.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Successfully enriched {len(questions)} questions in assets/data/ncert_science_ch1.json with comprehensive step-by-step solutions and metadata.")
