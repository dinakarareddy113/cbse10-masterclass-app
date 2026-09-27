import re
import sys

def main():
    with open('mobile_test/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add state variables around activeScienceChapterFilter
    target_state = "let activeScienceChapterFilter = 'All'; // Chapter filter for student Science tab"
    replacement_state = """let activeScienceChapterFilter = 'All'; // Chapter filter for student Science tab
    let adminGeneratedFilterExercise = 'All'; // Section filter for extracted questions in Admin review
    let adminExtractionScope = 'all'; // 'all', 'intext_p40', 'intext_all', 'exercises'"""
    
    if target_state in html and "adminExtractionScope" not in html:
        html = html.replace(target_state, replacement_state, 1)
        print("1. Added adminExtractionScope and adminGeneratedFilterExercise state variables.")
    else:
        print("1. State variables already present or target not found.")

    # 2. Add setAdminGeneratedFilter function
    target_fn = "function startAdminPdfQaGeneration() {"
    replacement_fn = """function setAdminGeneratedFilter(ex) {
      adminGeneratedFilterExercise = ex;
      navTo('admin');
    }

    function startAdminPdfQaGeneration() {"""
    
    if target_fn in html and "function setAdminGeneratedFilter" not in html:
        html = html.replace(target_fn, replacement_fn, 1)
        print("2. Added setAdminGeneratedFilter function.")
    else:
        print("2. setAdminGeneratedFilter already present or target not found.")

    # 3. Update startAdminPdfQaGeneration generation logic
    old_gen = "pdfGeneratedQuestions = generateSampleQuestionsForChapter(adminTargetChapterId);"
    new_gen = """const allQs = generateSampleQuestionsForChapter(adminTargetChapterId);
            if (adminExtractionScope === 'intext_p40') {
              pdfGeneratedQuestions = allQs.filter(q => (q.exercise && q.exercise.includes('Page 40')) || (q.section && q.section.includes('Page 40')));
            } else if (adminExtractionScope === 'intext_all') {
              pdfGeneratedQuestions = allQs.filter(q => (q.exercise && q.exercise.toLowerCase().includes('in-text')) || (q.section && q.section.toLowerCase().includes('questions')));
            } else if (adminExtractionScope === 'exercises') {
              pdfGeneratedQuestions = allQs.filter(q => (q.exercise && q.exercise.toLowerCase().includes('exercise')) || (q.section && q.section.toLowerCase().includes('exercise')));
            } else {
              pdfGeneratedQuestions = allQs;
            }
            adminGeneratedFilterExercise = 'All';"""
    
    if old_gen in html:
        html = html.replace(old_gen, new_gen, 1)
        print("3. Updated startAdminPdfQaGeneration with adminExtractionScope filtering.")
    else:
        print("3. startAdminPdfQaGeneration already updated or old_gen not found.")

    # 4. Update handleAdminPdfFileSelect for Chapter 3 & Scope detection
    old_select = "} else if (fn.includes('3rd chapter') || fn.includes('ch 3') || fn.includes('metal')) {\n          adminTargetChapterId = 'sci_ch_03_metals_non_metals';"
    new_select = """} else if (fn.includes('chapter 3') || fn.includes('chapter-3') || fn.includes('chapter_3') || fn.includes('ch-3') || fn.includes('ch_3') || fn.includes('ch_03') || fn.includes('3rd chapter') || fn.includes('ch 3') || fn.includes('metal') || fn.includes('metals')) {
          adminTargetChapterId = 'sci_ch_03_metals_non_metals';
          if (fn.includes('p40') || fn.includes('page 40') || fn.includes('page_40') || fn.includes('questions section')) {
            adminExtractionScope = 'intext_p40';
          }"""
    
    if old_select in html:
        html = html.replace(old_select, new_select, 1)
        print("4. Updated handleAdminPdfFileSelect with robust Ch 3 patterns.")
    else:
        print("4. handleAdminPdfFileSelect already updated or old_select not found.")

    # 5. Add Extraction Scope UI Selector in Admin Hub
    target_step3 = """                  <select id="admin-pdf-target-ch" onchange="changeAdminTargetChapter(this.value);" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2.5 text-xs font-semibold text-white focus:outline-none focus:border-blue-500">
                    ${getChaptersForSubject(adminTargetSubject).map(c => `
                      <option value="${c.id}" ${c.id === adminTargetChapterId ? 'selected' : ''}>Ch ${c.num}: ${c.titleEn} (${c.titleKn || ''})</option>
                    `).join('')}
                  </select>
                </div>"""

    new_step3 = """                  <select id="admin-pdf-target-ch" onchange="changeAdminTargetChapter(this.value);" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2.5 text-xs font-semibold text-white focus:outline-none focus:border-blue-500">
                    ${getChaptersForSubject(adminTargetSubject).map(c => `
                      <option value="${c.id}" ${c.id === adminTargetChapterId ? 'selected' : ''}>Ch ${c.num}: ${c.titleEn} (${c.titleKn || ''})</option>
                    `).join('')}
                  </select>
                </div>

                <!-- 4b. Step 3b: Extraction Scope & Source Isolation Selector -->
                <div class="space-y-1">
                  <div class="flex items-center justify-between">
                    <label class="text-xs font-bold text-slate-300">Extraction Scope & Source Isolation:</label>
                    <span class="text-[10px] text-emerald-400 font-bold bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">
                      ${adminExtractionScope === 'all' ? 'Full Chapter' : (adminExtractionScope === 'intext_p40' ? '📸 Page 40 Only (Screenshot)' : (adminExtractionScope === 'intext_all' ? 'In-Text Only' : 'Exercises Only'))}
                    </span>
                  </div>
                  <select id="admin-extraction-scope" onchange="adminExtractionScope = this.value; navTo('admin');" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2.5 text-xs font-semibold text-white focus:outline-none focus:border-blue-500">
                    <option value="all" ${adminExtractionScope === 'all' ? 'selected' : ''}>Full Chapter (All In-Text QUESTIONS + EXERCISES - 50 Qs)</option>
                    <option value="intext_p40" ${adminExtractionScope === 'intext_p40' ? 'selected' : ''}>📸 In-Text "QUESTIONS" (Page 40 - As in Screenshot) (6 Qs)</option>
                    <option value="intext_all" ${adminExtractionScope === 'intext_all' ? 'selected' : ''}>All In-Text "QUESTIONS" Only (Pages 40–55 - 29 Qs)</option>
                    <option value="exercises" ${adminExtractionScope === 'exercises' ? 'selected' : ''}>End-of-Chapter "EXERCISES" Only (Pages 56–57 - 21 Qs)</option>
                  </select>
                </div>"""

    if target_step3 in html and "admin-extraction-scope" not in html:
        html = html.replace(target_step3, new_step3, 1)
        print("5. Added Extraction Scope Selector to Admin Hub Step 3.")
    else:
        print("5. Extraction Scope Selector already added or target_step3 not found.")

    # 6. Update Science preloader catalog buttons to include Page 40 quick button
    old_ch3_btn = """                        <button onclick="preloadCatalogPdf('science', 'sci_ch_03_metals_non_metals')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'sci_ch_03_metals_non_metals' && uploadedPdfFile ? 'border-emerald-500 text-emerald-300' : 'border-slate-700 text-slate-300'}">
                          ⚡ Ch 3: Metals & Non-metals (50 Qs)
                        </button>"""

    new_ch3_btn = """                        <button onclick="preloadCatalogPdf('science', 'sci_ch_03_metals_non_metals'); adminExtractionScope = 'all';" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'sci_ch_03_metals_non_metals' && uploadedPdfFile && adminExtractionScope === 'all' ? 'border-emerald-500 text-emerald-300' : 'border-slate-700 text-slate-300'}">
                          ⚡ Ch 3: All 50 Qs
                        </button>
                        <button onclick="preloadCatalogPdf('science', 'sci_ch_03_metals_non_metals'); adminExtractionScope = 'intext_p40';" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-emerald-950/50 border ${adminTargetChapterId === 'sci_ch_03_metals_non_metals' && uploadedPdfFile && adminExtractionScope === 'intext_p40' ? 'border-emerald-400 text-emerald-300 ring-1 ring-emerald-400' : 'border-emerald-600/50 text-emerald-300'}">
                          📸 Ch 3: Page 40 "QUESTIONS" (Screenshot - 6 Qs)
                        </button>"""

    if old_ch3_btn in html:
        html = html.replace(old_ch3_btn, new_ch3_btn, 1)
        print("6. Added Page 40 quick button to Catalog Preloader.")
    else:
        print("6. Catalog Preloader buttons already updated or old_ch3_btn not found.")

    # 7. Update Extracted Questions Review to have interactive Section Filter Buttons
    old_review_block = """                    <!-- Exercise breakdown chips -->
                    <div class="flex gap-1.5 flex-wrap">
                      ${Array.from(new Set(pdfGeneratedQuestions.map(q => q.exercise))).map(ex => `
                        <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-500/10 text-blue-300 border border-blue-500/20">
                          ${ex} (${pdfGeneratedQuestions.filter(q => q.exercise === ex).length})
                        </span>
                      `).join('')}
                    </div>

                    <!-- Action Buttons -->
                    <div class="grid grid-cols-3 gap-2 pt-1">
                      <button onclick="publishPdfQuestionsLive('approved')" class="py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow flex items-center justify-center gap-1 active:scale-98 transition">
                        🚀 Publish Live
                      </button>
                      <button onclick="exportGeneratedJson()" class="py-2.5 rounded-xl bg-slate-800 border border-blue-500/40 text-blue-300 hover:bg-blue-500/10 text-xs font-bold flex items-center justify-center gap-1 active:scale-98 transition">
                        💾 Export JSON
                      </button>
                      <button onclick="clearAdminGeneratedMemory()" class="py-2.5 rounded-xl bg-slate-800 border border-rose-500/40 text-rose-300 hover:bg-rose-500/10 text-xs font-bold flex items-center justify-center gap-1 active:scale-98 transition" title="Clear memory for this chapter">
                        🗑️ Clear
                      </button>
                    </div>

                    <!-- Question Preview Cards -->
                    <div class="space-y-2.5 pt-1 max-h-[420px] overflow-y-auto pr-1">
                      ${pdfGeneratedQuestions.map((q, idx) => `"""

    new_review_block = """                    <!-- Exercise breakdown interactive filter buttons -->
                    <div class="space-y-1.5 pt-1">
                      <div class="flex items-center justify-between text-[10px] font-bold text-slate-400 uppercase tracking-wide">
                        <span>Filter Preview by Section:</span>
                        <span class="text-emerald-400 lowercase font-semibold">${displayedAdminQsCount} shown</span>
                      </div>
                      <div class="flex gap-1.5 flex-wrap items-center">
                        <button onclick="setAdminGeneratedFilter('All')" class="px-2 py-0.5 rounded text-[10px] font-bold border transition ${adminGeneratedFilterExercise === 'All' ? 'bg-blue-600 text-white border-blue-400 shadow' : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-white'}">
                          All (${pdfGeneratedQuestions.length})
                        </button>
                        ${Array.from(new Set(pdfGeneratedQuestions.map(q => q.exercise))).map(ex => {
                          const isP40 = ex && ex.includes('Page 40');
                          const isSel = adminGeneratedFilterExercise === ex;
                          const cnt = pdfGeneratedQuestions.filter(q => q.exercise === ex).length;
                          return `
                            <button onclick="setAdminGeneratedFilter('${ex}')" class="px-2 py-0.5 rounded text-[10px] font-bold border transition ${isSel ? 'bg-emerald-600 text-white border-emerald-400 shadow' : (isP40 ? 'bg-emerald-950/60 text-emerald-300 border-emerald-500/60 hover:bg-emerald-900/40' : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-white')}">
                              ${isP40 ? '📸 ' : ''}${ex} (${cnt})
                            </button>
                          `;
                        }).join('')}
                      </div>
                    </div>

                    <!-- Action Buttons -->
                    <div class="grid grid-cols-3 gap-2 pt-1">
                      <button onclick="publishPdfQuestionsLive('approved')" class="py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow flex items-center justify-center gap-1 active:scale-98 transition">
                        🚀 Publish Live
                      </button>
                      <button onclick="exportGeneratedJson()" class="py-2.5 rounded-xl bg-slate-800 border border-blue-500/40 text-blue-300 hover:bg-blue-500/10 text-xs font-bold flex items-center justify-center gap-1 active:scale-98 transition">
                        💾 Export JSON
                      </button>
                      <button onclick="clearAdminGeneratedMemory()" class="py-2.5 rounded-xl bg-slate-800 border border-rose-500/40 text-rose-300 hover:bg-rose-500/10 text-xs font-bold flex items-center justify-center gap-1 active:scale-98 transition" title="Clear memory for this chapter">
                        🗑️ Clear
                      </button>
                    </div>

                    <!-- Question Preview Cards -->
                    <div class="space-y-2.5 pt-1 max-h-[420px] overflow-y-auto pr-1">
                      ${displayedAdminQuestions.map((q, idx) => `"""

    # We also need displayedAdminQuestions and displayedAdminQsCount calculated right before rendering the review card
    # Let's inspect where pdfGeneratedQuestions.length > 0 starts:
    old_start_review = """                <!-- 8. Extracted Questions Review & Direct Publish Section -->
                ${pdfGeneratedQuestions.length > 0 ? `"""
    
    new_start_review = """                <!-- 8. Extracted Questions Review & Direct Publish Section -->
                ${(() => {
                  if (pdfGeneratedQuestions.length === 0) return '';
                  const displayedAdminQuestions = adminGeneratedFilterExercise === 'All' 
                    ? pdfGeneratedQuestions 
                    : pdfGeneratedQuestions.filter(q => q.exercise === adminGeneratedFilterExercise);
                  const displayedAdminQsCount = displayedAdminQuestions.length;
                  return `"""

    # And closing the IIFE before the trailing : ''
    old_end_review = """                      `).join('')}
                    </div>
                  </div>
                ` : ''}"""

    new_end_review = """                      `).join('')}
                    </div>
                  </div>
                  `;
                })()}"""

    if old_review_block in html and old_start_review in html:
        html = html.replace(old_start_review, new_start_review, 1)
        html = html.replace(old_review_block, new_review_block, 1)
        html = html.replace(old_end_review, new_end_review, 1)
        print("7. Replaced static review block with interactive section filter buttons and IIFE!")
    else:
        print("7. Review block targets not found or already replaced.")

    with open('mobile_test/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("mobile_test/index.html successfully updated!")

    # Mirror to cbse10_app_preview.html
    with open('cbse10_app_preview.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("cbse10_app_preview.html successfully mirrored!")

if __name__ == '__main__':
    main()
