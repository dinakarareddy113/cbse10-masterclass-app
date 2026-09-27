"""
Inject Science Chapter 4 (Carbon and its Compounds) and Chapter 5 (Periodic Classification of Elements)
into mobile_test/index.html and cbse10_app_preview.html.
"""

import json

def main():
    with open("assets/data/ncert_science_ch4.json", "r", encoding="utf-8") as f:
        ch4_questions = json.load(f)

    with open("assets/data/ncert_science_ch5.json", "r", encoding="utf-8") as f:
        ch5_questions = json.load(f)

    with open("mobile_test/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Chapter 4 questionCount and add Periodic Classification of Elements
    # Locate Chapter 4 entry
    target_ch4 = "id: 'sci_ch_04_carbon_compounds',"
    assert target_ch4 in html, "Could not find sci_ch_04_carbon_compounds in html"
    
    # Replace questionCount: 28 -> 36
    old_qcount = "questionCount: 28,"
    idx_ch4 = html.find(target_ch4)
    idx_qcount = html.find(old_qcount, idx_ch4)
    assert idx_qcount != -1 and idx_qcount - idx_ch4 < 400, "Could not find questionCount: 28 for Ch 4"
    html = html[:idx_qcount] + "questionCount: 36," + html[idx_qcount + len(old_qcount):]

    # Insert Periodic Classification right before sci_ch_05_life_processes
    target_life = "id: 'sci_ch_05_life_processes',"
    idx_life = html.find(target_life)
    assert idx_life != -1, "Could not find sci_ch_05_life_processes in html"

    # Find the starting brace of sci_ch_05_life_processes
    idx_brace = html.rfind("{", 0, idx_life)
    assert idx_brace != -1, "Could not find starting brace of sci_ch_05_life_processes"

    periodic_entry = """      {
        id: 'sci_ch_05_periodic_classification',
        num: 5,
        titleEn: 'Periodic Classification of Elements',
        titleKn: 'ಧಾತುಗಳ ಆವರ್ತನೀಯ ವರ್ಗೀಕರಣ',
        summary: 'Döbereiner triads, Newlands octaves, Mendeléev periodic law & table, Modern periodic table trends (valency, atomic size, metallic character).',
        questionCount: 31,
        formulas: [
          "Mendeléev's Law: Properties of elements are periodic functions of atomic masses",
          "Modern Periodic Law: Properties of elements are periodic functions of atomic numbers (Z)",
          'Atomic Radius: Decreases across period (left to right), Increases down group (top to bottom)',
          'Metallic Character: Decreases across period, Increases down group',
          'Electronegativity: Increases across period, Decreases down group',
          'Valency: In period, increases 1 to 4 then decreases to 0; Constant in a group'
        ]
      },
"""
    # Also change num: 5 of life processes to num: 6
    old_life_num = "num: 5,"
    idx_life_num = html.find(old_life_num, idx_life)
    if idx_life_num != -1 and idx_life_num - idx_life < 60:
        html = html[:idx_life_num] + "num: 6," + html[idx_life_num + len(old_life_num):]

    html = html[:idx_brace] + periodic_entry + html[idx_brace:]

    # 2. Update Science header chapters badge to dynamic count
    old_sci_badge = '<span class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-200 border border-emerald-500/30">13 Chapters</span>'
    new_sci_badge = '<span class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-200 border border-emerald-500/30">${scienceChapters.length} Chapters</span>'
    if old_sci_badge in html:
        html = html.replace(old_sci_badge, new_sci_badge)

    old_sci_title = '<div class="text-xs font-bold text-slate-400 uppercase tracking-wider pt-2">All 13 Syllabus Chapters</div>'
    new_sci_title = '<div class="text-xs font-bold text-slate-400 uppercase tracking-wider pt-2">All ${scienceChapters.length} Syllabus Chapters</div>'
    if old_sci_title in html:
        html = html.replace(old_sci_title, new_sci_title)

    # 3. Update Admin Hub quick sample buttons for Science
    # Find the buttons block
    old_ch3_btn = """<button onclick="preloadCatalogPdf('science', 'sci_ch_03_metals_non_metals')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'sci_ch_03_metals_non_metals' && uploadedPdfFile ? 'border-emerald-500 text-emerald-300' : 'border-slate-700 text-slate-300'}">
                          ⚡ Ch 3: Metals & Non-metals (50 Qs)
                        </button>"""
    new_ch4_ch5_buttons = """<button onclick="preloadCatalogPdf('science', 'sci_ch_03_metals_non_metals')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'sci_ch_03_metals_non_metals' && uploadedPdfFile ? 'border-emerald-500 text-emerald-300' : 'border-slate-700 text-slate-300'}">
                          ⚡ Ch 3: Metals & Non-metals (50 Qs)
                        </button>
                        <button onclick="preloadCatalogPdf('science', 'sci_ch_04_carbon_compounds')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'sci_ch_04_carbon_compounds' && uploadedPdfFile ? 'border-emerald-500 text-emerald-300' : 'border-slate-700 text-slate-300'}">
                          💎 Ch 4: Carbon & Compounds (36 Qs)
                        </button>
                        <button onclick="preloadCatalogPdf('science', 'sci_ch_05_periodic_classification')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'sci_ch_05_periodic_classification' && uploadedPdfFile ? 'border-emerald-500 text-emerald-300' : 'border-slate-700 text-slate-300'}">
                          📊 Ch 5: Periodic Classification (31 Qs)
                        </button>"""
    assert old_ch3_btn in html, "Could not find old_ch3_btn in html"
    html = html.replace(old_ch3_btn, new_ch4_ch5_buttons)

    # 4. Insert scienceCh4MasterQuestions and scienceCh5MasterQuestions before const ch3SampleQuestions
    ch4_ch5_js = f"""
    const scienceCh4MasterQuestions = {json.dumps(ch4_questions, indent=2)};
    questions.push(...scienceCh4MasterQuestions);

    const scienceCh5MasterQuestions = {json.dumps(ch5_questions, indent=2)};
    questions.push(...scienceCh5MasterQuestions);

"""
    target_pos = "const ch3SampleQuestions = ["
    assert target_pos in html, "Could not find target_pos (const ch3SampleQuestions) in html"
    html = html.replace(target_pos, ch4_ch5_js + target_pos)

    # 5. Update generateSampleQuestionsForChapter
    old_gen_target = """      // 3. Science Chapter 3: Metals and Non-metals (50 Questions) - Matches 3.NCERT-Class-10-Science_3rd Chapter.pdf!
      if (chId === 'sci_ch_03_metals_non_metals') {
        return JSON.parse(JSON.stringify(scienceCh3MasterQuestions));
      }"""

    new_gen_target = """      // 3. Science Chapter 3: Metals and Non-metals (50 Questions) - Matches 3.NCERT-Class-10-Science_3rd Chapter.pdf!
      if (chId === 'sci_ch_03_metals_non_metals') {
        return JSON.parse(JSON.stringify(scienceCh3MasterQuestions));
      }

      // 4. Science Chapter 4: Carbon and its Compounds (36 Questions) - Matches 4.NCERT-Class-10-Science_4th Chapter.pdf!
      if (chId === 'sci_ch_04_carbon_compounds') {
        return JSON.parse(JSON.stringify(scienceCh4MasterQuestions));
      }

      // 5. Science Chapter 5: Periodic Classification of Elements (31 Questions) - Matches 5.NCERT-Class-10-Science_5th Chapter.pdf!
      if (chId === 'sci_ch_05_periodic_classification') {
        return JSON.parse(JSON.stringify(scienceCh5MasterQuestions));
      }"""

    assert old_gen_target in html, "Could not find old_gen_target in html"
    html = html.replace(old_gen_target, new_gen_target)

    # 6. Update handleAdminPdfFileSelect detection logic
    old_detection = """        } else if (fn.includes('4th chapter') || fn.includes('ch 4') || fn.includes('carbon')) {
          adminTargetChapterId = 'sci_ch_04_carbon_compounds';
        } else if (fn.includes('5th chapter') || fn.includes('ch 5') || fn.includes('life')) {
          adminTargetChapterId = 'sci_ch_05_life_processes';
        }"""

    new_detection = """        } else if (fn.includes('4th chapter') || fn.includes('ch 4') || fn.includes('ch-4') || fn.includes('carbon')) {
          adminTargetChapterId = 'sci_ch_04_carbon_compounds';
        } else if (fn.includes('periodic') || fn.includes('classification')) {
          adminTargetChapterId = 'sci_ch_05_periodic_classification';
        } else if (fn.includes('5th chapter') || fn.includes('ch 5') || fn.includes('ch-5')) {
          adminTargetChapterId = 'sci_ch_05_periodic_classification';
        } else if (fn.includes('life')) {
          adminTargetChapterId = 'sci_ch_05_life_processes';
        }"""

    assert old_detection in html, "Could not find old_detection in html"
    html = html.replace(old_detection, new_detection)

    # Write back to mobile_test/index.html
    with open("mobile_test/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully updated mobile_test/index.html with Ch 4 and Ch 5 questions!")

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
