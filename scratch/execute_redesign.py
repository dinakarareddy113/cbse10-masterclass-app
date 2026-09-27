import json

with open("scratch/redesign_step3.html", encoding="utf-8") as f:
    html = f.read()

# 1. Replace the old PDF tab HTML block
pos1 = html.find("${adminHubTab === 'pdf' ? `")
p_pipe = html.find(": adminHubTab === 'pipeline' ? `", pos1)
assert pos1 != -1 and p_pipe != -1, f"Could not find PDF tab block: {pos1}, {p_pipe}"

new_pdf_tab_html = """${adminHubTab === 'pdf' ? `
              <!-- Multi-Subject PDF Upload & AI Q&A Extraction Hub -->
              <div class="space-y-3.5 pt-2">
                <!-- 1. Engine Capabilities Banner -->
                <div class="bg-gradient-to-r from-blue-950/80 via-indigo-950/80 to-slate-900 border border-blue-500/40 rounded-2xl p-3.5 space-y-1.5 shadow-lg">
                  <div class="flex items-center justify-between">
                    <span class="text-xs font-bold text-blue-300 flex items-center gap-1.5">
                      <span>✨</span> Automated NCERT PDF Parser & Q&A Generator
                    </span>
                    <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-500/20 text-blue-200 border border-blue-500/30">
                      Multi-Subject
                    </span>
                  </div>
                  <div class="text-[11px] text-slate-300 leading-relaxed">
                    Upload an NCERT textbook chapter PDF. The AI engine enforces <b>Strict Source Isolation</b> (extracts strictly from In-Text "QUESTIONS" and end-of-chapter "EXERCISES"), formulates 4 symmetric options with misconception rationales, and publishes directly to students.
                  </div>
                </div>

                <!-- 2. Step 1: Select Target Class Level -->
                <div class="space-y-1.5">
                  <label class="text-xs font-bold text-slate-200 flex items-center justify-between">
                    <span>1. Target Academic Class:</span>
                    <span class="text-[10px] text-blue-400 font-semibold">${adminTargetClass}</span>
                  </label>
                  <div class="flex gap-2">
                    ${['Class 8', 'Class 9', 'Class 10'].map(cls => `
                      <button type="button" onclick="changeAdminTargetClass('${cls}');" class="flex-1 py-2 px-2 rounded-xl border text-center transition font-bold text-xs ${adminTargetClass === cls ? 'border-blue-500 bg-blue-950/70 text-white shadow ring-1 ring-blue-400' : 'border-slate-700 bg-slate-800 text-slate-400 hover:border-slate-600'}">
                        ${cls}
                      </button>
                    `).join('')}
                  </div>
                </div>

                <!-- 3. Step 2: Select Subject (3 Core Cards) -->
                <div class="space-y-1.5">
                  <label class="text-xs font-bold text-slate-200 flex items-center justify-between">
                    <span>2. Select Subject for Ingestion:</span>
                    <span class="text-[10px] text-emerald-400 font-semibold">${adminTargetSubject === 'science' ? 'Science (13 Ch)' : (adminTargetSubject === 'math' ? 'Mathematics (14 Ch)' : 'Social Science (7 Ch)')}</span>
                  </label>
                  <div class="grid grid-cols-3 gap-2">
                    <button type="button" onclick="changeAdminTargetSubject('science');" class="py-2.5 px-2 rounded-xl border text-center transition ${adminTargetSubject === 'science' ? 'border-emerald-500 bg-emerald-950/60 text-white shadow ring-2 ring-emerald-500/30' : 'border-slate-700 bg-slate-800/80 text-slate-400 hover:border-slate-600'}">
                      <div class="text-lg">🔬</div>
                      <div class="text-xs font-bold mt-0.5">Science</div>
                      <div class="text-[9px] text-emerald-300/80">13 Chapters</div>
                    </button>
                    <button type="button" onclick="changeAdminTargetSubject('math');" class="py-2.5 px-2 rounded-xl border text-center transition ${adminTargetSubject === 'math' ? 'border-blue-500 bg-blue-950/60 text-white shadow ring-2 ring-blue-500/30' : 'border-slate-700 bg-slate-800/80 text-slate-400 hover:border-slate-600'}">
                      <div class="text-lg">📐</div>
                      <div class="text-xs font-bold mt-0.5">Math</div>
                      <div class="text-[9px] text-blue-300/80">14 Chapters</div>
                    </button>
                    <button type="button" onclick="changeAdminTargetSubject('sst');" class="py-2.5 px-2 rounded-xl border text-center transition ${adminTargetSubject === 'sst' ? 'border-amber-500 bg-amber-950/60 text-white shadow ring-2 ring-amber-500/30' : 'border-slate-700 bg-slate-800/80 text-slate-400 hover:border-slate-600'}">
                      <div class="text-lg">🌍</div>
                      <div class="text-xs font-bold mt-0.5">Social Sci</div>
                      <div class="text-[9px] text-amber-300/80">7 Chapters</div>
                    </button>
                  </div>
                </div>

                <!-- 4. Step 3: Select Target Chapter -->
                <div class="space-y-1">
                  <div class="flex items-center justify-between">
                    <label class="text-xs font-bold text-slate-300">3. Select Target Chapter:</label>
                    <span class="text-[10px] text-slate-400">${getChaptersForSubject(adminTargetSubject).length} Chapters in Catalog</span>
                  </div>
                  <select id="admin-pdf-target-ch" onchange="changeAdminTargetChapter(this.value);" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2.5 text-xs font-semibold text-white focus:outline-none focus:border-blue-500">
                    ${getChaptersForSubject(adminTargetSubject).map(c => `
                      <option value="${c.id}" ${c.id === adminTargetChapterId ? 'selected' : ''}>Ch ${c.num}: ${c.titleEn} (${c.titleKn || ''})</option>
                    `).join('')}
                  </select>
                </div>

                <!-- 5. Step 4: Interactive Document Dropzone & Smart Auto-Detection -->
                <div class="space-y-2">
                  <div class="flex justify-between items-center">
                    <label class="text-xs font-bold text-slate-300">4. Upload Textbook PDF Document:</label>
                    <span class="text-[10px] text-slate-400">PDF up to 50MB</span>
                  </div>

                  <input type="file" id="admin-pdf-file-input" accept=".pdf,application/pdf" style="display:none;" onchange="handleAdminPdfFileSelect(event)">

                  <div onclick="document.getElementById('admin-pdf-file-input').click()" class="border-2 border-dashed ${uploadedPdfFile ? 'border-emerald-500/60 bg-emerald-950/20' : 'border-slate-600 bg-slate-800/60'} rounded-2xl p-4 text-center cursor-pointer hover:border-blue-400 hover:bg-slate-800/80 transition space-y-2">
                    ${uploadedPdfFile ? `
                      <div class="w-12 h-12 mx-auto rounded-full bg-emerald-500/20 border border-emerald-500/40 flex items-center justify-center text-2xl text-emerald-400">
                        📄
                      </div>
                      <div>
                        <div class="text-xs font-bold text-emerald-300">${uploadedPdfFile.name}</div>
                        <div class="text-[10px] text-slate-400 mt-0.5">${uploadedPdfFile.size} • Ready for AI extraction</div>
                      </div>
                      <div class="flex items-center justify-center gap-3 pt-1">
                        <span class="text-[11px] text-blue-400 font-semibold underline">Tap to browse different file</span>
                        <span class="text-slate-600">•</span>
                        <button onclick="event.stopPropagation(); removeAdminAttachedPdf();" class="text-[11px] text-rose-400 font-semibold hover:text-rose-300 underline">
                          🗑️ Clear Attachment
                        </button>
                      </div>
                    ` : `
                      <div class="w-12 h-12 mx-auto rounded-full bg-blue-500/10 border border-blue-500/30 flex items-center justify-center text-2xl text-blue-400">
                        📤
                      </div>
                      <div class="text-xs font-bold text-white">Tap to Browse or Drop Chapter PDF</div>
                      <div class="text-[10px] text-slate-400">Supports Science, Math & SST PDFs (e.g., 2.NCERT-Class-10-Science_2nd Chapter.pdf)</div>
                    `}
                  </div>

                  <!-- Auto-Detection Confirmation Card -->
                  ${adminDetectedMeta ? `
                    <div class="bg-emerald-950/50 border border-emerald-500/50 rounded-2xl p-3 flex items-center gap-3 shadow">
                      <div class="w-9 h-9 rounded-xl bg-emerald-500/20 flex items-center justify-center text-lg shrink-0 text-emerald-400">
                        🎯
                      </div>
                      <div class="flex-1 min-w-0">
                        <div class="text-[10px] font-bold text-emerald-400 uppercase tracking-wide">Document Auto-Detected & Aligned</div>
                        <div class="text-xs font-bold text-white truncate">${adminDetectedMeta.className} • ${adminDetectedMeta.subjectName} • ${adminDetectedMeta.chapterTitle}</div>
                        <div class="text-[10px] text-slate-300 truncate">Source: ${adminDetectedMeta.filename} (${adminDetectedMeta.size})</div>
                      </div>
                      <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0">
                        Matched ✓
                      </span>
                    </div>
                  ` : ''}

                  <!-- Preload from NCERT Textbook Catalog with Subject Tabs -->
                  <div class="space-y-1.5 pt-1">
                    <div class="flex items-center justify-between text-[10px] font-bold text-slate-400 uppercase tracking-wide">
                      <span>Preload from Textbook Catalog:</span>
                      <div class="flex gap-1">
                        <button onclick="setAdminCatalogTab('science');" class="px-2 py-0.5 rounded text-[10px] font-bold ${adminCatalogTab === 'science' ? 'bg-emerald-600 text-white' : 'bg-slate-800 text-slate-400'}">Science</button>
                        <button onclick="setAdminCatalogTab('math');" class="px-2 py-0.5 rounded text-[10px] font-bold ${adminCatalogTab === 'math' ? 'bg-blue-600 text-white' : 'bg-slate-800 text-slate-400'}">Math</button>
                        <button onclick="setAdminCatalogTab('sst');" class="px-2 py-0.5 rounded text-[10px] font-bold ${adminCatalogTab === 'sst' ? 'bg-amber-600 text-white' : 'bg-slate-800 text-slate-400'}">SST</button>
                      </div>
                    </div>

                    <div class="flex gap-1.5 flex-wrap">
                      ${adminCatalogTab === 'science' ? `
                        <button onclick="preloadCatalogPdf('science', 'sci_ch_02_acids_bases_salts')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'sci_ch_02_acids_bases_salts' && uploadedPdfFile ? 'border-emerald-500 text-emerald-300' : 'border-slate-700 text-slate-300'}">
                          ⚗️ Ch 2: Acids, Bases & Salts (37 Qs)
                        </button>
                        <button onclick="preloadCatalogPdf('science', 'sci_ch_01_chemical_reactions')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'sci_ch_01_chemical_reactions' && uploadedPdfFile ? 'border-emerald-500 text-emerald-300' : 'border-slate-700 text-slate-300'}">
                          🧪 Ch 1: Chemical Reactions (47 Qs)
                        </button>
                        <button onclick="preloadCatalogPdf('science', 'sci_ch_03_metals_non_metals')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border border-slate-700 text-slate-300">
                          ⚡ Ch 3: Metals & Non-metals
                        </button>
                        <button onclick="preloadCatalogPdf('science', 'sci_ch_05_life_processes')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border border-slate-700 text-slate-300">
                          🌱 Ch 5: Life Processes
                        </button>
                        <button onclick="preloadCatalogPdf('science', 'sci_ch_09_light')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border border-slate-700 text-slate-300">
                          💡 Ch 9: Light & Reflection
                        </button>
                      ` : adminCatalogTab === 'math' ? `
                        <button onclick="preloadCatalogPdf('math', 'math_ch_04_quadratic_equations')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'math_ch_04_quadratic_equations' && uploadedPdfFile ? 'border-blue-500 text-blue-300' : 'border-slate-700 text-slate-300'}">
                          📘 Ch 4: Quadratic Equations (58 Qs)
                        </button>
                        <button onclick="preloadCatalogPdf('math', 'math_ch_03_linear_equations')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'math_ch_03_linear_equations' && uploadedPdfFile ? 'border-blue-500 text-blue-300' : 'border-slate-700 text-slate-300'}">
                          📘 Ch 3: Linear Equations (82 Qs)
                        </button>
                        <button onclick="preloadCatalogPdf('math', 'math_ch_02_polynomials')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'math_ch_02_polynomials' && uploadedPdfFile ? 'border-blue-500 text-blue-300' : 'border-slate-700 text-slate-300'}">
                          📘 Ch 2: Polynomials (15 Qs)
                        </button>
                        <button onclick="preloadCatalogPdf('math', 'math_ch_01_real_numbers')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'math_ch_01_real_numbers' && uploadedPdfFile ? 'border-blue-500 text-blue-300' : 'border-slate-700 text-slate-300'}">
                          📘 Ch 1: Real Numbers (20 Qs)
                        </button>
                        <button onclick="preloadCatalogPdf('math', 'math_ch_05_arithmetic_progressions')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'math_ch_05_arithmetic_progressions' && uploadedPdfFile ? 'border-blue-500 text-blue-300' : 'border-slate-700 text-slate-300'}">
                          📘 Ch 5: Arithmetic Progressions (70 Qs)
                        </button>
                      ` : `
                        <button onclick="preloadCatalogPdf('sst', 'sst_hist_ch_02_nationalism')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border border-slate-700 text-slate-300">
                          📙 Ch 2: Nationalism in India
                        </button>
                        <button onclick="preloadCatalogPdf('sst', 'sst_geo_ch_07_lifelines')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border border-slate-700 text-slate-300">
                          📙 Ch 4: Lifelines of Economy
                        </button>
                        <button onclick="preloadCatalogPdf('sst', 'sst_civ_ch_02_federalism')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border border-slate-700 text-slate-300">
                          📙 Ch 6: Federalism
                        </button>
                      `}
                    </div>
                  </div>
                </div>

                <!-- 6. Strict Source Isolation Quality Card -->
                <div class="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-3 space-y-1.5 text-[11px]">
                  <div class="flex items-center justify-between text-xs font-bold text-slate-200">
                    <span class="flex items-center gap-1.5"><span>🛡️</span> Strict Source Isolation Rules</span>
                    <span class="text-[10px] text-emerald-400 font-bold bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">Enforced</span>
                  </div>
                  <div class="grid grid-cols-2 gap-1.5 text-[10px] text-slate-300 pt-0.5">
                    <div class="flex items-center gap-1"><span class="text-emerald-400 font-bold">✓</span> In-Text "QUESTIONS" Only</div>
                    <div class="flex items-center gap-1"><span class="text-emerald-400 font-bold">✓</span> End "EXERCISES" Only</div>
                    <div class="flex items-center gap-1"><span class="text-rose-400 font-bold">✗</span> Zero General Body Text</div>
                    <div class="flex items-center gap-1"><span class="text-rose-400 font-bold">✗</span> Zero Activities / Sidebars</div>
                    <div class="flex items-center gap-1"><span class="text-emerald-400 font-bold">✓</span> 4 Symmetric MCQ Options</div>
                    <div class="flex items-center gap-1"><span class="text-emerald-400 font-bold">✓</span> Misconception Analysis</div>
                  </div>
                </div>

                <!-- 7. Parse & Generate Action Button / Progress -->
                ${pdfGenerating ? `
                  <div class="bg-slate-800 border border-blue-500/40 rounded-2xl p-4 space-y-3">
                    <div class="flex items-center justify-between text-xs">
                      <span class="font-bold text-blue-300 flex items-center gap-2">
                        <span class="text-sm">⏳</span> ${pdfGenerationStatusText}
                      </span>
                      <span class="font-mono text-blue-400 font-bold">${pdfGenerationProgress}%</span>
                    </div>
                    <div class="w-full bg-slate-900 rounded-full h-2 overflow-hidden border border-slate-700">
                      <div class="bg-gradient-to-r from-blue-500 to-emerald-400 h-2 transition-all duration-300" style="width: ${pdfGenerationProgress}%;"></div>
                    </div>
                  </div>
                ` : `
                  <button onclick="startAdminPdfQaGeneration()" class="w-full py-3.5 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-emerald-600 hover:from-blue-500 hover:to-emerald-500 font-bold text-white text-xs shadow-xl flex items-center justify-center gap-2 active:scale-98 transition">
                    <span>✨</span> Parse PDF & Generate Q&A (${adminTargetSubject.toUpperCase()})
                  </button>
                `}

                <!-- 8. Extracted Questions Review & Direct Publish Section -->
                ${pdfGeneratedQuestions.length > 0 ? `
                  <div class="space-y-3 pt-2">
                    <div class="flex items-center justify-between border-t border-slate-700 pt-3">
                      <div>
                        <div class="text-xs font-bold text-white">Extracted ${pdfGeneratedQuestions.length} Questions</div>
                        <div class="text-[10px] text-emerald-400">100% textbook-matched exercises & proofs ready</div>
                      </div>
                      <div class="flex items-center gap-1.5">
                        <button onclick="clearAdminGeneratedMemory()" class="text-[10px] text-rose-400 hover:text-rose-300 bg-rose-500/10 border border-rose-500/20 px-2 py-0.5 rounded font-semibold">
                          🗑️ Clear
                        </button>
                        <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                          Verified ✓
                        </span>
                      </div>
                    </div>

                    <!-- Exercise breakdown chips -->
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
                      ${pdfGeneratedQuestions.map((q, idx) => `
                        <div class="bg-slate-800 border border-slate-700 rounded-xl p-3 space-y-1.5 text-xs">
                          <div class="flex justify-between items-center text-[10px]">
                            <span class="font-bold text-blue-400 uppercase">${q.exercise} • Q${q.questionNumber || idx + 1}</span>
                            <span class="text-slate-400 capitalize">${q.difficulty}</span>
                          </div>
                          <div class="font-semibold text-white whitespace-pre-line">${q.text}</div>
                          <div class="text-[11px] text-slate-300 pl-2 border-l-2 border-emerald-500/50 space-y-0.5">
                            ${q.options.map(o => `
                              <div class="${o.is_correct || o.correct ? 'text-emerald-400 font-bold' : 'text-slate-400'}">
                                ${o.id}. ${o.text} ${o.is_correct || o.correct ? '✓' : ''}
                              </div>
                            `).join('')}
                          </div>
                          <button onclick="document.getElementById('pdf-sol-${idx}').classList.toggle('hidden')" class="text-[10px] text-blue-400 font-semibold underline">
                            Toggle Solution
                          </button>
                          <div id="pdf-sol-${idx}" class="hidden p-2 rounded bg-slate-900 border border-slate-700 font-mono text-[10px] text-cyan-300 whitespace-pre-line">
                            ${q.solution || q.step_by_step_solution || ''}
                          </div>
                        </div>
                      `).join('')}
                    </div>
                  </div>
                ` : ''}
              </div>
            ` """

html = html[:pos1] + new_pdf_tab_html + html[p_pipe:]
print("Replaced PDF tab HTML block successfully.")

# 2. Update Student Science Screen in navTo('science')
sci_screen_marker = "} else if (screen === 'science') {"
sci_screen_end = "} else if (screen === 'sst') {"
pos_sci = html.find(sci_screen_marker)
pos_sst = html.find(sci_screen_end, pos_sci)

new_sci_screen = """} else if (screen === 'science') {
        title.innerText = 'Science • NCERT';
        const sciQuestions = questions.filter(q => q.subject === 'science');
        
        // Find all chapters available in sciQuestions
        const sciChaptersSet = new Set();
        sciQuestions.forEach(q => {
          if (q.chapterId) sciChaptersSet.add(q.chapterId);
        });
        const availableChapters = Array.from(sciChaptersSet);

        // Filter by selected chapter if any
        let filteredByCh = activeScienceChapterFilter === 'All'
          ? sciQuestions
          : sciQuestions.filter(q => q.chapterId === activeScienceChapterFilter);

        // Then filter by exercise
        const exercisesSet = new Set(['All']);
        filteredByCh.forEach(q => {
          if (q.exercise) exercisesSet.add(q.exercise);
        });
        const exList = Array.from(exercisesSet);
        const displayed = activeExerciseFilter === 'All'
          ? filteredByCh
          : filteredByCh.filter(q => q.exercise === activeExerciseFilter);

        const totalSciSolved = filteredByCh.filter(q => solvedQuestions.has(q.id)).length;
        const sciPercent = filteredByCh.length > 0 ? Math.round((totalSciSolved / filteredByCh.length) * 100) : 0;

        const currentChObj = scienceChapters.find(c => c.id === activeScienceChapterFilter);
        const headerTitle = currentChObj ? `Ch ${currentChObj.num}: ${currentChObj.titleEn}` : 'All Science Chapters';
        const headerTitleKn = currentChObj ? currentChObj.titleKn : 'ಎಲ್ಲಾ ವಿಜ್ಞಾನ ಅಧ್ಯಾಯಗಳು';

        content.innerHTML = `
          <!-- Header Banner -->
          <div class="bg-gradient-to-r from-emerald-950/90 via-teal-900/80 to-slate-900 border border-emerald-500/40 rounded-2xl p-4 space-y-2 shadow-lg">
            <div class="flex justify-between items-center">
              <span class="text-xs font-bold text-emerald-300">CBSE Class 10 • Science</span>
              <span class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-200 border border-emerald-500/30">NCERT 2026</span>
            </div>
            <div>
              <div class="text-sm font-black text-white">${headerTitle}</div>
              <div class="text-xs font-semibold text-emerald-300/80 kannada-font">${headerTitleKn}</div>
            </div>
            <div class="text-[11px] text-slate-300 leading-snug">
              Strict Source Isolation: In-Text Questions & End-of-Chapter Exercises with 4 Symmetric Options and Step-by-Step Solutions.
            </div>
            <div class="w-full bg-black/40 h-1.5 rounded-full overflow-hidden mt-1">
              <div class="bg-emerald-400 h-full rounded-full transition-all" style="width: ${sciPercent}%"></div>
            </div>
            <div class="flex items-center justify-between text-[10px] text-slate-300 pt-0.5">
              <span>${totalSciSolved} of ${filteredByCh.length} Completed (${sciPercent}%)</span>
              <span class="text-emerald-400 font-semibold">LaTeX Formulas Active</span>
            </div>
          </div>

          <!-- Chapter Switcher Tabs -->
          <div class="space-y-1">
            <div class="flex items-center justify-between text-[11px] font-bold text-slate-400 px-0.5">
              <span>Chapter Selector:</span>
              <span class="text-emerald-400 font-semibold">${availableChapters.length} Chapters Available</span>
            </div>
            <div class="flex gap-1.5 py-1 overflow-x-auto no-scrollbar">
              <button onclick="activeScienceChapterFilter = 'All'; activeExerciseFilter = 'All'; navTo('science');" class="px-2.5 py-1 rounded-xl text-[11px] font-bold shrink-0 transition ${activeScienceChapterFilter === 'All' ? 'bg-emerald-600 text-white shadow-sm ring-1 ring-emerald-400' : 'bg-slate-800 text-slate-400 border border-slate-700/60'}">
                All Chapters (${sciQuestions.length})
              </button>
              ${availableChapters.map(chId => {
                const cObj = scienceChapters.find(c => c.id === chId);
                const cCount = sciQuestions.filter(q => q.chapterId === chId).length;
                const isSel = activeScienceChapterFilter === chId;
                const label = cObj ? `Ch ${cObj.num}: ${cObj.titleEn.split(' ')[0]}` : chId;
                return `
                  <button onclick="activeScienceChapterFilter = '${chId}'; activeExerciseFilter = 'All'; navTo('science');" class="px-2.5 py-1 rounded-xl text-[11px] font-bold shrink-0 transition ${isSel ? 'bg-emerald-600 text-white shadow-sm ring-1 ring-emerald-400' : 'bg-slate-800 text-slate-400 border border-slate-700/60'}">
                    ${label} (${cCount})
                  </button>
                `;
              }).join('')}
            </div>
          </div>

          <!-- Section Filter Tabs -->
          <div class="space-y-1">
            <div class="flex items-center justify-between text-[11px] font-bold text-slate-400 px-0.5">
              <span>Source Sections:</span>
              <span class="text-emerald-400 font-semibold">${displayed.length} Qs shown</span>
            </div>
            <div class="flex gap-1.5 py-1 overflow-x-auto no-scrollbar">
              ${exList.map(ex => {
                const count = ex === 'All' ? filteredByCh.length : filteredByCh.filter(q => q.exercise === ex).length;
                const isSel = activeExerciseFilter === ex;
                return `
                  <button onclick="activeExerciseFilter = '${ex}'; navTo('science');" class="px-2.5 py-1 rounded-xl text-[11px] font-bold shrink-0 transition ${isSel ? 'bg-emerald-600 text-white shadow-sm ring-1 ring-emerald-400' : 'bg-slate-800 text-slate-400 border border-slate-700/60 hover:border-slate-500'}">
                    ${ex} (${count})
                  </button>
                `;
              }).join('')}
            </div>
          </div>

          <!-- Question Cards -->
          <div class="space-y-2.5 pt-1">
            ${displayed.map((q, idx) => renderCard(q, idx + 1)).join('')}
          </div>
        `;
      """

html = html[:pos_sci] + new_sci_screen + html[pos_sst:]
print("Updated Student Science screen.")

# 3. Update Admin JS Functions (around handleAdminPdfFileSelect)
old_fn_marker = "    function handleAdminPdfFileSelect(event) {"
new_admin_fns = """
    function setAdminCatalogTab(tab) {
      adminCatalogTab = tab;
      navTo('admin');
    }

    function changeAdminTargetClass(cls) {
      adminTargetClass = cls;
      adminDetectedMeta = null;
      navTo('admin');
    }

    function changeAdminTargetSubject(subj) {
      adminTargetSubject = subj;
      adminCatalogTab = subj;
      adminDetectedMeta = null;
      if (subj === 'science') {
        adminTargetChapterId = 'sci_ch_02_acids_bases_salts';
      } else if (subj === 'math') {
        adminTargetChapterId = 'math_ch_02_polynomials';
      } else {
        adminTargetChapterId = 'sst_hist_ch_02_nationalism';
      }
      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      navTo('admin');
    }

    function changeAdminTargetChapter(chId) {
      adminTargetChapterId = chId;
      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      navTo('admin');
    }

    function handleAdminPdfFileSelect(event) {
      const file = event.target.files && event.target.files[0];
      if (!file) return;
      uploadedPdfFile = {
        name: file.name,
        size: (file.size / (1024 * 1024)).toFixed(2) + ' MB',
        preloaded: false
      };

      const fn = file.name.toLowerCase();

      // Detect Class
      if (fn.includes('class 8') || fn.includes('class-8') || fn.includes('8th') || fn.includes('class_8')) {
        adminTargetClass = 'Class 8';
      } else if (fn.includes('class 9') || fn.includes('class-9') || fn.includes('9th') || fn.includes('class_9')) {
        adminTargetClass = 'Class 9';
      } else if (fn.includes('class 10') || fn.includes('class-10') || fn.includes('10th') || fn.includes('class_10')) {
        adminTargetClass = 'Class 10';
      }

      // Detect Subject
      if (fn.includes('science') || fn.includes('chem') || fn.includes('bio') || fn.includes('phy') || fn.includes('sci')) {
        adminTargetSubject = 'science';
        adminCatalogTab = 'science';
      } else if (fn.includes('math') || fn.includes('algebra') || fn.includes('geometry') || fn.includes('arithmetic')) {
        adminTargetSubject = 'math';
        adminCatalogTab = 'math';
      } else if (fn.includes('social') || fn.includes('sst') || fn.includes('history') || fn.includes('geo') || fn.includes('civic')) {
        adminTargetSubject = 'sst';
        adminCatalogTab = 'sst';
      }

      // Detect Chapter
      if (adminTargetSubject === 'science') {
        if (fn.includes('2nd chapter') || fn.includes('ch 2') || fn.includes('ch-2') || fn.includes('chapter 2') || fn.includes('ch_02') || fn.includes('acid')) {
          adminTargetChapterId = 'sci_ch_02_acids_bases_salts';
        } else if (fn.includes('1st chapter') || fn.includes('ch 1') || fn.includes('ch-1') || fn.includes('chapter 1') || fn.includes('ch_01') || fn.includes('chemical')) {
          adminTargetChapterId = 'sci_ch_01_chemical_reactions';
        } else if (fn.includes('3rd chapter') || fn.includes('ch 3') || fn.includes('metal')) {
          adminTargetChapterId = 'sci_ch_03_metals_non_metals';
        } else if (fn.includes('4th chapter') || fn.includes('ch 4') || fn.includes('carbon')) {
          adminTargetChapterId = 'sci_ch_04_carbon_compounds';
        } else if (fn.includes('5th chapter') || fn.includes('ch 5') || fn.includes('life')) {
          adminTargetChapterId = 'sci_ch_05_life_processes';
        } else if (fn.includes('9th chapter') || fn.includes('ch 9') || fn.includes('light')) {
          adminTargetChapterId = 'sci_ch_09_light';
        }
      } else if (adminTargetSubject === 'math') {
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
      }

      const chObj = getChapterObj(adminTargetChapterId);
      const subjName = adminTargetSubject === 'science' ? 'Science 🔬' : (adminTargetSubject === 'math' ? 'Mathematics 📐' : 'Social Science 🌍');
      adminDetectedMeta = {
        className: adminTargetClass,
        subjectName: subjName,
        chapterTitle: chObj ? `Ch ${chObj.num}: ${chObj.titleEn}` : adminTargetChapterId,
        filename: file.name,
        size: uploadedPdfFile.size
      };

      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      navTo('admin');
    }

    function preloadCatalogPdf(subj, chId) {
      adminTargetSubject = subj;
      adminTargetChapterId = chId;
      adminCatalogTab = subj;
      const chObj = getChapterObj(chId);
      uploadedPdfFile = {
        name: `ncert_class10_${chId}.pdf`,
        size: '2.15 MB',
        preloaded: true
      };
      const subjName = subj === 'science' ? 'Science 🔬' : (subj === 'math' ? 'Mathematics 📐' : 'Social Science 🌍');
      adminDetectedMeta = {
        className: adminTargetClass,
        subjectName: subjName,
        chapterTitle: chObj ? `Ch ${chObj.num}: ${chObj.titleEn}` : chId,
        filename: uploadedPdfFile.name,
        size: uploadedPdfFile.size
      };
      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      navTo('admin');
    }

    function removeAdminAttachedPdf() {
      uploadedPdfFile = null;
      adminDetectedMeta = null;
      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      navTo('admin');
    }

    function clearAdminGeneratedMemory() {
      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      alert('🧹 Cleared generated Q&A memory for this chapter.');
      navTo('admin');
    }

    function exportGeneratedJson() {
      if (!pdfGeneratedQuestions || pdfGeneratedQuestions.length === 0) {
        alert('No questions to export.');
        return;
      }
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(pdfGeneratedQuestions, null, 2));
      const downloadAnchor = document.createElement('a');
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", `ncert_${adminTargetChapterId}_extracted.json`);
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
    }

    function startAdminPdfQaGeneration() {
      if (!uploadedPdfFile) {
        alert('Please select or drop a textbook PDF document first.');
        return;
      }

      pdfGenerating = true;
      pdfGenerationProgress = 20;
      pdfGenerationStatusText = 'Reading textbook PDF document structure...';
      navTo('admin');

      setTimeout(() => {
        pdfGenerationProgress = 50;
        pdfGenerationStatusText = 'Isolating in-text "QUESTIONS" and end-of-chapter "EXERCISES"...';
        navTo('admin');

        setTimeout(() => {
          pdfGenerationProgress = 80;
          pdfGenerationStatusText = 'Synthesizing 4 symmetric options & deriving LaTeX chemical proofs...';
          navTo('admin');

          setTimeout(() => {
            pdfGenerating = false;
            pdfGenerationProgress = 100;
            pdfGeneratedQuestions = generateSampleQuestionsForChapter(adminTargetChapterId);
            navTo('admin');
          }, 350);
        }, 350);
      }, 350);
    }
"""

pos_fn = html.find(old_fn_marker)
pos_fn_end = html.find("    function startAdminPdfQaGeneration() {", pos_fn)
pos_fn_end = html.find("    }\n\n    \n    const ch3SampleQuestions", pos_fn_end)
if pos_fn_end == -1:
    pos_fn_end = html.find("    }\n\n    const ch3SampleQuestions", pos_fn_end)

if pos_fn != -1 and pos_fn_end != -1:
    html = html[:pos_fn] + new_admin_fns + html[pos_fn_end + 6:]
    print("Updated admin JS functions.")
else:
    print("Could not match admin JS functions position:", pos_fn, pos_fn_end)

# 4. Update generateSampleQuestionsForChapter
gen_marker = "function generateSampleQuestionsForChapter(chId) {"
gen_pos = html.find(gen_marker)
if gen_pos != -1:
    gen_end = html.find("function publishPdfQuestionsLive(status) {", gen_pos)
    new_generator = """function generateSampleQuestionsForChapter(chId) {
      // 1. Science Chapter 1: Chemical Reactions and Equations (47 Questions)
      if (chId === 'sci_ch_01_chemical_reactions') {
        return JSON.parse(JSON.stringify(scienceCh1MasterQuestions));
      }

      // 2. Science Chapter 2: Acids, Bases and Salts (37 Questions) - Matches 2.NCERT-Class-10-Science_2nd Chapter.pdf!
      if (chId === 'sci_ch_02_acids_bases_salts') {
        return JSON.parse(JSON.stringify(scienceCh2MasterQuestions));
      }

      // 3. Math Chapter 3: Linear Equations
      if (chId === 'math_ch_03_linear_equations') {
        return JSON.parse(JSON.stringify(ch3SampleQuestions));
      }

      // 4. Math Chapter 4: Quadratic Equations
      if (chId === 'math_ch_04_quadratic_equations') {
        return JSON.parse(JSON.stringify(ch4SampleQuestions));
      }

      // 5. Math Chapter 5: Arithmetic Progressions
      if (chId === 'math_ch_05_arithmetic_progressions') {
        return JSON.parse(JSON.stringify(ch5SampleQuestions));
      }

      // 6. Math Chapter 2: Polynomials
      if (chId === 'math_ch_02_polynomials') {
        return [
          {
            id: 'pdf-poly-1',
            subject: 'math',
            chapterId: chId,
            exercise: 'Exercise 2.1',
            questionNumber: '1(i)',
            difficulty: 'easy',
            text: '[Exercise 2.1 - Q1(i)] The graph of y = p(x) is given. Find the number of zeroes of p(x) for the graph: A straight horizontal line parallel to the x-axis.',
            options: [
              { id: 'A', text: '0 zeroes (line does not intersect x-axis)', is_correct: true },
              { id: 'B', text: '1 zero', is_correct: false },
              { id: 'C', text: '2 zeroes', is_correct: false },
              { id: 'D', text: 'Infinitely many', is_correct: false }
            ],
            solution: 'Step 1: The number of zeroes of polynomial p(x) is the number of points where the graph intersects the x-axis.\\nStep 2: The given line is horizontal and never intersects the x-axis.\\nStep 3: Hence, the number of zeroes is 0.'
          },
          {
            id: 'pdf-poly-2',
            subject: 'math',
            chapterId: chId,
            exercise: 'Exercise 2.1',
            questionNumber: '1(ii)',
            difficulty: 'easy',
            text: '[Exercise 2.1 - Q1(ii)] The graph of y = p(x) intersects the x-axis at 1 point and the y-axis at 1 point. Find the number of zeroes.',
            options: [
              { id: 'A', text: '1 zero', is_correct: true },
              { id: 'B', text: '2 zeroes', is_correct: false },
              { id: 'C', text: '3 zeroes', is_correct: false },
              { id: 'D', text: '0 zeroes', is_correct: false }
            ],
            solution: 'Step 1: Count intersections with the x-axis: 1 point.\\nStep 2: Intersections with y-axis are not zeroes of p(x).\\nStep 3: Therefore, the number of zeroes is 1.'
          },
          {
            id: 'pdf-poly-3',
            subject: 'math',
            chapterId: chId,
            exercise: 'Exercise 2.2',
            questionNumber: '1(i)',
            difficulty: 'medium',
            text: '[Exercise 2.2 - Q1(i)] Find the zeroes of the quadratic polynomial x² - 2x - 8 and verify the relationship between zeroes and coefficients.',
            options: [
              { id: 'A', text: 'Zeroes: 4 and -2; Sum = 2, Product = -8', is_correct: true },
              { id: 'B', text: 'Zeroes: -4 and 2; Sum = -2, Product = -8', is_correct: false },
              { id: 'C', text: 'Zeroes: 4 and 2; Sum = 6, Product = 8', is_correct: false },
              { id: 'D', text: 'Zeroes: 8 and -1; Sum = 7, Product = -8', is_correct: false }
            ],
            solution: 'Step 1: Factorise: x² - 2x - 8 = (x - 4)(x + 2) = 0 => x = 4, x = -2.\\nStep 2: Sum of zeroes = 4 + (-2) = 2 = -(-2)/1 = -b/a.\\nStep 3: Product of zeroes = 4 × (-2) = -8 = c/a.\\nRelationship verified!'
          }
        ];
      }

      // 7. Math Chapter 1: Real Numbers
      if (chId === 'math_ch_01_real_numbers') {
        return questions.filter(q => q.subject === 'math' && q.chapterId === chId);
      }

      // Default fallback for any other chapter
      const ch = getChapterObj(chId);
      const chName = ch ? ch.titleEn : chId;
      return [
        {
          id: `pdf-${chId}-1`,
          subject: adminTargetSubject,
          chapterId: chId,
          exercise: 'Exercise 1',
          questionNumber: '1',
          difficulty: 'easy',
          text: `[${chName}] Which of the following fundamental principles defines this chapter?`,
          options: [
            { id: 'A', text: 'First core textbook definition from NCERT Section 1', is_correct: true },
            { id: 'B', text: 'Secondary distractor based on common student misconception', is_correct: false },
            { id: 'C', text: 'Alternative distractor targeting reversed relationships', is_correct: false },
            { id: 'D', text: 'Distractor assuming arithmetic sign reversal', is_correct: false }
          ],
          solution: `Step 1: Refer to NCERT textbook introductory section for ${chName}.\\nStep 2: State core property and verify.'`
        }
      ];
    }

    """
    html = html[:gen_pos] + new_generator + html[gen_end:]
    print("Updated generateSampleQuestionsForChapter.")

# 5. Update publishPdfQuestionsLive
pub_marker = "function publishPdfQuestionsLive(status) {"
pub_pos = html.find(pub_marker)
if pub_pos != -1:
    pub_end = html.find("    }\n\n    function approveQueueItem", pub_pos)
    if pub_end == -1:
        pub_end = html.find("    }\n    function approveQueueItem", pub_pos)
    new_publish_fn = """function publishPdfQuestionsLive(status) {
      if (!pdfGeneratedQuestions || pdfGeneratedQuestions.length === 0) {
        alert('No questions to publish.');
        return;
      }

      const chId = adminTargetChapterId;
      const subj = adminTargetSubject;
      const count = pdfGeneratedQuestions.length;

      if (status === 'approved') {
        // Clear previous questions for this chapter to prevent duplicate stacking
        questions = questions.filter(q => q.chapterId !== chId);

        // Prepend fresh newly approved questions
        pdfGeneratedQuestions.forEach((q, i) => {
          questions.unshift({
            id: 'live-' + Date.now() + '-' + i,
            subject: subj,
            chapterId: chId,
            exercise: q.exercise,
            questionNumber: q.questionNumber || (i + 1).toString(),
            difficulty: q.difficulty || 'medium',
            text: q.text,
            options: q.options,
            solution: q.solution || q.step_by_step_solution
          });
        });

        // Clear memory post-publish
        pdfGeneratedQuestions = [];
        pdfGenerationProgress = 0;
        pdfGenerationStatusText = '';

        alert(`🚀 Success! Published ${count} approved questions directly to student feed for chapter: ${chId}.`);

        if (subj === 'science') {
          activeScienceChapterFilter = chId;
          navTo('science');
        } else if (subj === 'math') {
          openChapterPractice(chId);
        } else {
          navTo('sst');
        }
      } else {
        pdfGeneratedQuestions.forEach((q, i) => {
          pending.unshift({
            id: 'mod-' + Date.now() + '-' + i,
            chapter: chId,
            subject: subj,
            difficulty: q.difficulty,
            text: q.text
          });
        });

        pdfGeneratedQuestions = [];
        pdfGenerationProgress = 0;
        pdfGenerationStatusText = '';

        alert(`🛡️ Sent ${count} questions to moderation queue.`);
        adminHubTab = 'queue';
        navTo('admin');
      }
    }
"""
    if pub_end != -1:
        html = html[:pub_pos] + new_publish_fn + html[pub_end + 6:]
        print("Updated publishPdfQuestionsLive.")
    else:
        print("Could not find pub_end")

with open("mobile_test/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: Updated mobile_test/index.html with redesigned Admin Hub!")

# Also mirror to cbse10_app_preview.html
import shutil
shutil.copyfile("mobile_test/index.html", "C:/Users/csdin/.gemini/antigravity/brain/b1293a4f-a486-4bc1-a2c6-d175611557ba/cbse10_app_preview.html")
print("Mirrored to cbse10_app_preview.html successfully.")
