"""
Inject Science Chapter 3 questions into mobile_test/index.html
"""

import json

def main():
    with open("assets/data/ncert_science_ch3.json", "r", encoding="utf-8") as f:
        ch3_questions = json.load(f)

    with open("mobile_test/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update questionCount in scienceChapters
    old_ch3_decl = "id: 'sci_ch_03_metals_non_metals',\n        num: 3,\n        titleEn: 'Metals and Non-metals',\n        titleKn: 'ಲೋಹಗಳು ಮತ್ತು ಅಲೋಹಗಳು',\n        summary: 'Physical & chemical properties, reactivity series, ionic compounds, extraction of metals, and prevention of corrosion.',\n        questionCount: 25,"
    new_ch3_decl = "id: 'sci_ch_03_metals_non_metals',\n        num: 3,\n        titleEn: 'Metals and Non-metals',\n        titleKn: 'ಲೋಹಗಳು ಮತ್ತು ಅಲೋಹಗಳು',\n        summary: 'Physical & chemical properties, reactivity series, ionic compounds, extraction of metals, and prevention of corrosion.',\n        questionCount: 50,"
    assert old_ch3_decl in html, "Could not find old_ch3_decl in html"
    html = html.replace(old_ch3_decl, new_ch3_decl)

    # 2. Update preload button for Ch 3
    old_btn = """<button onclick="preloadCatalogPdf('science', 'sci_ch_03_metals_non_metals')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border border-slate-700 text-slate-300">
                          ⚡ Ch 3: Metals & Non-metals
                        </button>"""
    new_btn = """<button onclick="preloadCatalogPdf('science', 'sci_ch_03_metals_non_metals')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'sci_ch_03_metals_non_metals' && uploadedPdfFile ? 'border-emerald-500 text-emerald-300' : 'border-slate-700 text-slate-300'}">
                          ⚡ Ch 3: Metals & Non-metals (50 Qs)
                        </button>"""
    assert old_btn in html, "Could not find old_btn in html"
    html = html.replace(old_btn, new_btn)

    # 3. Insert const scienceCh3MasterQuestions and questions.push
    ch3_js = f"\n    const scienceCh3MasterQuestions = {json.dumps(ch3_questions, indent=2)};\n    questions.push(...scienceCh3MasterQuestions);\n\n"
    target_pos = "const ch3SampleQuestions = ["
    assert target_pos in html, "Could not find target_pos (const ch3SampleQuestions) in html"
    html = html.replace(target_pos, ch3_js + target_pos)

    # 4. Update generateSampleQuestionsForChapter
    old_gen_target = """      // 2. Science Chapter 2: Acids, Bases and Salts (37 Questions) - Matches 2.NCERT-Class-10-Science_2nd Chapter.pdf!
      if (chId === 'sci_ch_02_acids_bases_salts') {
        return JSON.parse(JSON.stringify(scienceCh2MasterQuestions));
      }"""

    new_gen_target = """      // 2. Science Chapter 2: Acids, Bases and Salts (37 Questions) - Matches 2.NCERT-Class-10-Science_2nd Chapter.pdf!
      if (chId === 'sci_ch_02_acids_bases_salts') {
        return JSON.parse(JSON.stringify(scienceCh2MasterQuestions));
      }

      // 3. Science Chapter 3: Metals and Non-metals (50 Questions) - Matches 3.NCERT-Class-10-Science_3rd Chapter.pdf!
      if (chId === 'sci_ch_03_metals_non_metals') {
        return JSON.parse(JSON.stringify(scienceCh3MasterQuestions));
      }"""
    assert old_gen_target in html, "Could not find old_gen_target in html"
    html = html.replace(old_gen_target, new_gen_target)

    # Write back to mobile_test/index.html
    with open("mobile_test/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully updated mobile_test/index.html")

    # Mirror to cbse10_app_preview.html
    preview_path = "C:/Users/csdin/.gemini/antigravity/brain/b1293a4f-a486-4bc1-a2c6-d175611557ba/cbse10_app_preview.html"
    try:
        with open(preview_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("Successfully mirrored to cbse10_app_preview.html")
    except Exception as e:
        print(f"Could not mirror to cbse10_app_preview.html: {e}")

if __name__ == "__main__":
    main()
