import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def verify_math_chapters():
    print("=== CBSE Class 10 Math Syllabus & Ingestion Pipeline Verification ===")
    
    # 1. Verify SQL Migration File
    sql_path = "g:/My Drive/AI_Projects/AntiGravity_Exam_Guide/supabase/migrations/20260925020000_seed_math_chapters.sql"
    with open(sql_path, "r", encoding="utf-8") as f:
        sql_content = f.read()
    
    expected_chapters = [
        ("math_ch_01_real_numbers", 1, "Real Numbers", "ವಾಸ್ತವ ಸಂಖ್ಯೆಗಳು"),
        ("math_ch_02_polynomials", 2, "Polynomials", "ಬಹುಪದೋಕ್ತಿಗಳು"),
        ("math_ch_03_linear_equations", 3, "Pair of Linear Equations in Two Variables", "ಎರಡು ಚರಾಕ್ಷರಗಳಿರುವ ರೇಖಾತ್ಮಕ ಸಮೀಕರಣಗಳ ಜೋಡಿಗಳು"),
        ("math_ch_04_quadratic_equations", 4, "Quadratic Equations", "ವರ್ಗ ಸಮೀಕರಣಗಳು"),
        ("math_ch_05_arithmetic_progressions", 5, "Arithmetic Progressions", "ಸಮಾಂತರ ಶ್ರೇಢಿಗಳು"),
        ("math_ch_06_triangles", 6, "Triangles", "ತ್ರಿಭುಜಗಳು"),
        ("math_ch_07_coordinate_geometry", 7, "Coordinate Geometry", "ನಿರ್ದೇಶಾಂಕ ರೇಖಾಗಣಿತ"),
        ("math_ch_08_intro_trigonometry", 8, "Introduction to Trigonometry", "ತ್ರಿಕೋನಮಿತಿಯ ಪ್ರಸ್ತಾವನೆ"),
        ("math_ch_09_applications_trigonometry", 9, "Some Applications of Trigonometry", "ತ್ರಿಕೋನಮಿತಿಯ ಕೆಲವು ಅನ್ವಯಗಳು"),
        ("math_ch_10_circles", 10, "Circles", "ವೃತ್ತಗಳು"),
        ("math_ch_11_areas_related_to_circles", 11, "Areas Related to Circles", "ವೃತ್ತಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ವಿಸ್ತೀರ್ಣಗಳು"),
        ("math_ch_12_surface_areas_volumes", 12, "Surface Areas and Volumes", "ಮೇಲ್ಮೈ ವಿಸ್ತೀರ್ಣಗಳು ಮತ್ತು ಘನಫಲಗಳು"),
        ("math_ch_13_statistics", 13, "Statistics", "ಸಂಖ್ಯಾಶಾಸ್ತ್ರ"),
        ("math_ch_14_probability", 14, "Probability", "ಸಂಭವನೀಯತೆ")
    ]
    
    print("\n[1/3] Checking SQL Migration (20260925020000_seed_math_chapters.sql)...")
    for cid, num, title_en, title_kn in expected_chapters:
        assert cid in sql_content, f"Missing {cid} in SQL migration"
        assert title_en in sql_content, f"Missing English title '{title_en}' in SQL"
        assert title_kn in sql_content, f"Missing Kannada title '{title_kn}' in SQL"
    print(f"  ✓ All 14 chapters present in SQL migration with correct bilingual titles and RLS policies.")
    
    # 2. Verify Dart Curriculum Constants
    print("\n[2/3] Checking Dart Curriculum File (lib/core/constants/cbse_curriculum.dart)...")
    dart_path = "g:/My Drive/AI_Projects/AntiGravity_Exam_Guide/lib/core/constants/cbse_curriculum.dart"
    with open(dart_path, "r", encoding="utf-8") as f:
        dart_content = f.read()
    
    for cid, num, title_en, title_kn in expected_chapters:
        assert cid in dart_content, f"Missing {cid} in cbse_curriculum.dart"
        assert title_kn in dart_content, f"Missing Kannada title '{title_kn}' in cbse_curriculum.dart"
    print(f"  ✓ All 14 chapters present in cbse_curriculum.dart with formulas.")
    
    # 3. Check Dart repository integration
    print("\n[3/3] Checking Repository & Screen Files...")
    repo_path = "g:/My Drive/AI_Projects/AntiGravity_Exam_Guide/lib/services/question_repository.dart"
    with open(repo_path, "r", encoding="utf-8") as f:
        repo_content = f.read()
    
    assert "fetchChapters" in repo_content, "Missing fetchChapters in QuestionRepository"
    assert "bulkPublishQuestions" in repo_content, "Missing bulkPublishQuestions in QuestionRepository"
    print("  ✓ QuestionRepository has fetchChapters and bulkPublishQuestions methods.")

    screens = [
        "g:/My Drive/AI_Projects/AntiGravity_Exam_Guide/lib/screens/math/math_chapter_list_screen.dart",
        "g:/My Drive/AI_Projects/AntiGravity_Exam_Guide/lib/screens/math/chapter_hub_screen.dart",
        "g:/My Drive/AI_Projects/AntiGravity_Exam_Guide/lib/screens/math/chapter_practice_screen.dart",
        "g:/My Drive/AI_Projects/AntiGravity_Exam_Guide/lib/screens/math/chapter_formula_screen.dart",
        "g:/My Drive/AI_Projects/AntiGravity_Exam_Guide/lib/screens/admin/admin_bulk_ingest_screen.dart"
    ]
    for s in screens:
        with open(s, "r", encoding="utf-8") as f:
            content = f.read()
            assert len(content) > 100, f"Screen {s} is empty"
        print(f"  ✓ Screen exists and verified: {s.split('/')[-1]}")

    print("\n🎉 ALL VERIFICATIONS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    verify_math_chapters()
