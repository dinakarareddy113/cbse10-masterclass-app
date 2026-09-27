# -*- coding: utf-8 -*-
"""
Integrate Class 10 Geography Chapter 1 (Resources and Development)
questions into mobile_test/index.html and cbse10_app_preview.html.
"""

import json
import re

def main():
    with open('assets/data/ncert_sst_geo_ch1.json', 'r', encoding='utf-8') as f:
        sst_geo_questions = json.load(f)

    print(f"Loaded {len(sst_geo_questions)} questions from ncert_sst_geo_ch1.json.")

    with open('mobile_test/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Define const sstGeoCh1MasterQuestions right before scienceCh1MasterQuestions
    js_array = f"const sstGeoCh1MasterQuestions = {json.dumps(sst_geo_questions, indent=2, ensure_ascii=False)};\n\n    "
    
    if "const sstGeoCh1MasterQuestions" not in html:
        target_marker = "const scienceCh1MasterQuestions = ["
        html = html.replace(target_marker, js_array + target_marker, 1)
        print("1. Injected const sstGeoCh1MasterQuestions.")
    else:
        print("1. sstGeoCh1MasterQuestions already injected.")

    # 2. Wire into questions.push(...)
    target_push = "questions.push(...scienceCh5MasterQuestions);"
    replacement_push = "questions.push(...scienceCh5MasterQuestions);\n    questions.push(...sstGeoCh1MasterQuestions);"
    if target_push in html and "questions.push(...sstGeoCh1MasterQuestions);" not in html:
        html = html.replace(target_push, replacement_push, 1)
        print("2. Seeded sstGeoCh1MasterQuestions into student questions feed.")

    # 3. Wire into generateSampleQuestionsForChapter
    target_gen = "function generateSampleQuestionsForChapter(chId) {"
    replacement_gen = """function generateSampleQuestionsForChapter(chId) {
      // 0. Social Science Geography Chapter 1: Resources and Development (39 Questions)
      if (chId === 'sst_geo_ch_01_resources') {
        return JSON.parse(JSON.stringify(sstGeoCh1MasterQuestions));
      }
"""
    if target_gen in html and "sst_geo_ch_01_resources" not in html[html.find("function generateSampleQuestionsForChapter(chId)"):]:
        html = html.replace(target_gen, replacement_gen, 1)
        print("3. Wired sst_geo_ch_01_resources into generateSampleQuestionsForChapter.")

    # 4. Wire into handleAdminPdfFileSelect for SST
    target_file_select = """      } else if (adminTargetSubject === 'math') {
        if (fn.includes('2nd chapter') || fn.includes('ch 2') || fn.includes('polynomial')) {
          adminTargetChapterId = 'math_ch_02_polynomials';
        } else if (fn.includes('1st chapter') || fn.includes('ch 1') || fn.includes('real number')) {
          adminTargetChapterId = 'math_ch_01_real_numbers';
        } else if (fn.includes('3rd chapter') || fn.includes('ch 3') || fn.includes('linear')) {
          adminTargetChapterId = 'math_ch_03_linear_equations';
        } else if (fn.includes('4th chapter') || fn.includes('ch 4') || fn.includes('quadratic')) {
          adminTargetChapterId = 'math_ch_04_quadratic_equations';
        } else if (fn.includes('5th chapter') || fn.includes('ch 5') || fn.includes('arithmetic')) {
          adminTargetChapterId = 'math_ch_05_arithmetic_progressions';
        }
      }"""

    replacement_file_select = """      } else if (adminTargetSubject === 'math') {
        if (fn.includes('2nd chapter') || fn.includes('ch 2') || fn.includes('polynomial')) {
          adminTargetChapterId = 'math_ch_02_polynomials';
        } else if (fn.includes('1st chapter') || fn.includes('ch 1') || fn.includes('real number')) {
          adminTargetChapterId = 'math_ch_01_real_numbers';
        } else if (fn.includes('3rd chapter') || fn.includes('ch 3') || fn.includes('linear')) {
          adminTargetChapterId = 'math_ch_03_linear_equations';
        } else if (fn.includes('4th chapter') || fn.includes('ch 4') || fn.includes('quadratic')) {
          adminTargetChapterId = 'math_ch_04_quadratic_equations';
        } else if (fn.includes('5th chapter') || fn.includes('ch 5') || fn.includes('arithmetic')) {
          adminTargetChapterId = 'math_ch_05_arithmetic_progressions';
        }
      } else if (adminTargetSubject === 'sst') {
        if (fn.includes('resource') || fn.includes('development') || fn.includes('geo 1') || fn.includes('geo_01') || fn.includes('geography 1') || fn.includes('contemporary india') || fn.includes('ch 1') || fn.includes('ch_01') || fn.includes('chapter 1') || fn.includes('1st chapter')) {
          adminTargetChapterId = 'sst_geo_ch_01_resources';
          if (fn.includes('exercise') || fn.includes('ex')) {
            adminExtractionScope = 'exercises';
          }
        } else if (fn.includes('lifeline') || fn.includes('geo 7') || fn.includes('geo 4')) {
          adminTargetChapterId = 'sst_geo_ch_07_lifelines';
        } else if (fn.includes('power') || fn.includes('sharing') || fn.includes('civic 1')) {
          adminTargetChapterId = 'sst_civ_ch_01_power_sharing';
        } else if (fn.includes('federal') || fn.includes('civic 2')) {
          adminTargetChapterId = 'sst_civ_ch_02_federalism';
        } else if (fn.includes('europe') || fn.includes('history 1')) {
          adminTargetChapterId = 'sst_hist_ch_01_europe';
        } else if (fn.includes('nationalism') || fn.includes('history 2')) {
          adminTargetChapterId = 'sst_hist_ch_02_nationalism';
        }
      }"""

    if target_file_select in html and "adminTargetChapterId = 'sst_geo_ch_01_resources'" not in html:
        html = html.replace(target_file_select, replacement_file_select, 1)
        print("4. Added SST chapter routing to handleAdminPdfFileSelect.")

    # 5. Add SST Quick Buttons in Admin Hub Preloader
    target_sst_btns = """                        <button onclick="preloadCatalogPdf('sst', 'sst_geo_ch_07_lifelines')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border border-slate-700 text-slate-300">
                          📙 Ch 4: Lifelines of Economy
                        </button>"""

    replacement_sst_btns = """                        <button onclick="preloadCatalogPdf('sst', 'sst_geo_ch_01_resources'); adminExtractionScope = 'all';" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'sst_geo_ch_01_resources' && uploadedPdfFile && adminExtractionScope === 'all' ? 'border-amber-500 text-amber-300' : 'border-slate-700 text-slate-300'}">
                          🌍 Ch 1: Resources & Development (39 Qs)
                        </button>
                        <button onclick="preloadCatalogPdf('sst', 'sst_geo_ch_01_resources'); adminExtractionScope = 'exercises';" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-amber-950/50 border ${adminTargetChapterId === 'sst_geo_ch_01_resources' && uploadedPdfFile && adminExtractionScope === 'exercises' ? 'border-amber-400 text-amber-300 ring-1 ring-amber-400' : 'border-amber-600/50 text-amber-300'}">
                          📝 Ch 1: Exercises Only (17 Qs)
                        </button>
                        <button onclick="preloadCatalogPdf('sst', 'sst_geo_ch_07_lifelines')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border border-slate-700 text-slate-300">
                          📙 Ch 4: Lifelines of Economy
                        </button>"""

    if target_sst_btns in html and "Ch 1: Resources & Development" not in html:
        html = html.replace(target_sst_btns, replacement_sst_btns, 1)
        print("5. Added Ch 1 quick buttons to SST catalog preloader.")

    # 6. Update sstChapters array questionCount
    # Find sst_geo_ch_01_resources in sstChapters
    old_ch_pattern = re.search(r'{\s*id:\s*[\'"]sst_geo_ch_01_resources[\'"].*?questionCount:\s*\d+', html, re.DOTALL)
    if old_ch_pattern:
        old_ch_str = old_ch_pattern.group(0)
        new_ch_str = re.sub(r'questionCount:\s*\d+', 'questionCount: 39', old_ch_str)
        html = html.replace(old_ch_str, new_ch_str, 1)
        print("6. Updated sstChapters questionCount to 39 for sst_geo_ch_01_resources.")

    with open('mobile_test/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("mobile_test/index.html written successfully!")

    with open('cbse10_app_preview.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("cbse10_app_preview.html mirrored successfully!")

if __name__ == '__main__':
    main()
