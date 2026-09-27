import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def main():
    base_dir = "g:/My Drive/AI_Projects/AntiGravity_Exam_Guide"
    json_path = os.path.join(base_dir, "assets/data/ncert_math_ch1.json")
    mobile_html_path = os.path.join(base_dir, "mobile_test/index.html")
    preview_html_path = "C:/Users/csdin/.gemini/antigravity/brain/b1293a4f-a486-4bc1-a2c6-d175611557ba/cbse10_app_preview.html"

    with open(json_path, "r", encoding="utf-8") as f:
        ch1_questions = json.load(f)

    print(f"Loaded {len(ch1_questions)} NCERT questions from {json_path}")

    # Format into javascript objects
    js_questions_list = []
    for q in ch1_questions:
        js_questions_list.append({
            "id": q["id"],
            "subject": "math",
            "chapterId": q["chapter_id"],
            "exercise": q["exercise"],
            "questionNumber": q["question_number"],
            "difficulty": q["difficulty_level"],
            "text": q["question_text"],
            "options": q["options"],
            "solution": q["step_by_step_solution"]
        })

    # Other subject questions
    other_questions = [
        {
            "id": "m_poly_1",
            "subject": "math",
            "chapterId": "math_ch_02_polynomials",
            "exercise": "Exercise 2.1",
            "questionNumber": "1",
            "difficulty": "easy",
            "text": "If one zero of the quadratic polynomial p(x) = x² + 3x + k is 2, then the value of k is:",
            "options": [
                {"id": "A", "text": "10", "correct": False},
                {"id": "B", "text": "-10", "correct": True},
                {"id": "C", "text": "-7", "correct": False},
                {"id": "D", "text": "-2", "correct": False}
            ],
            "solution": "Step 1: p(2) = 0 => (2)² + 3(2) + k = 0 => 4 + 6 + k = 0 => k = -10."
        },
        {
            "id": "m_quad_1",
            "subject": "math",
            "chapterId": "math_ch_04_quadratic_equations",
            "exercise": "Exercise 4.4",
            "questionNumber": "2",
            "difficulty": "hots",
            "text": "Find the value of k for which (k - 12)x² + 2(k - 12)x + 2 = 0 has two equal real roots, given k ≠ 12.",
            "options": [
                {"id": "A", "text": "k = 12", "correct": False},
                {"id": "B", "text": "k = 14", "correct": True},
                {"id": "C", "text": "k = 10", "correct": False},
                {"id": "D", "text": "k = 16", "correct": False}
            ],
            "solution": "Step 1: D = b² - 4ac = 0.\nStep 2: [2(k-12)]² - 4(k-12)(2) = 0.\nStep 3: 4(k-12)[k - 14] = 0 => k = 14 (k ≠ 12)."
        },
        {
            "id": "s1",
            "subject": "science",
            "chapterId": "sci_ch_09_light",
            "exercise": "NCERT In-Text",
            "questionNumber": "1",
            "difficulty": "medium",
            "text": "An object is placed at 10 cm in front of a concave mirror of focal length 15 cm. What are the image characteristics?",
            "options": [
                {"id": "A", "text": "Real and diminished", "correct": False},
                {"id": "B", "text": "Virtual, erect, and magnified", "correct": True},
                {"id": "C", "text": "Real and inverted", "correct": False},
                {"id": "D", "text": "Same size", "correct": False}
            ],
            "solution": "Step 1: f = -15 cm, u = -10 cm (Object between F and Pole P).\nStep 2: 1/v = -1/15 + 1/10 = +1/30 => v = +30 cm (Behind mirror).\nStep 3: m = +3 => Virtual, erect, magnified."
        },
        {
            "id": "sst1",
            "subject": "sst",
            "chapterId": "sst_ch_02_nationalism",
            "exercise": "NCERT In-Text",
            "questionNumber": "1",
            "difficulty": "easy",
            "text": "Why did Mahatma Gandhi withdraw the Non-Cooperation Movement in February 1922?",
            "options": [
                {"id": "A", "text": "Rowlatt Act", "correct": False},
                {"id": "B", "text": "Chauri Chaura violent clash", "correct": True},
                {"id": "C", "text": "Simon Commission", "correct": False},
                {"id": "D", "text": "Poona Pact", "correct": False}
            ],
            "solution": "Step 1: In Feb 1922 at Chauri Chaura, protestors set fire to a police station, killing 22 policemen.\nStep 2: Gandhi called off the movement to train satyagrahis in strict non-violence."
        }
    ]

    all_questions = js_questions_list + other_questions
    json_serialized = json.dumps(all_questions, indent=2, ensure_ascii=False)

    # Update mobile_test/index.html
    with open(mobile_html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace questions array in script
    pattern_start = "let questions = ["
    pattern_end = "let pending = ["

    start_idx = content.find(pattern_start)
    end_idx = content.find(pattern_end)

    if start_idx != -1 and end_idx != -1:
        new_content = (
            content[:start_idx]
            + f"let questions = {json_serialized};\n\n    "
            + content[end_idx:]
        )
        
        # Add exercise filter support in render
        if "let activeExerciseFilter = 'All';" not in new_content:
            new_content = new_content.replace(
                "let activeHubMode = null;",
                "let activeHubMode = null;\n    let activeExerciseFilter = 'All';"
            )

        # Update openChapterPractice to reset filter
        new_content = new_content.replace(
            "function openChapterPractice(chapterId) {\n      selectedChapterId = chapterId;\n      navTo('chapter_practice');\n    }",
            "function openChapterPractice(chapterId) {\n      selectedChapterId = chapterId;\n      activeExerciseFilter = 'All';\n      navTo('chapter_practice');\n    }"
        )

        with open(mobile_html_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {mobile_html_path} with {len(all_questions)} questions!")

        # Also write to preview_html_path
        with open(preview_html_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {preview_html_path} with {len(all_questions)} questions!")

if __name__ == "__main__":
    main()
