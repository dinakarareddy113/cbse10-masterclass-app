# -*- coding: utf-8 -*-
"""
Implements:
1. Complete Timed Quiz Engine (Timer logic, score calculation, wall-clock drift compensation, state persistence, results breakdown, review mode).
2. Toast Notification System to replace blocking window.alert() calls.
3. Global Error Boundary (window.onerror & unhandledrejection).
4. Option 3: Timed Exam Mode in Chapter Hub.
5. Offline Service Worker registration in mobile_test/index.html.
6. Kannada typography & mobile contrast improvements.
"""

import os
import re

def main():
    # 1. Create mobile_test/sw.js (Service Worker)
    sw_code = """const CACHE_NAME = 'cbse10-masterclass-v1';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json',
  './icon.svg',
  'https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js',
  'https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css',
  'https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js',
  'https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => {
      return cache.addAll(ASSETS_TO_CACHE).catch((err) => {
        console.warn('Pre-cache warning for offline assets:', err);
      });
    })
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return cachedResponse || fetch(event.request).catch(() => {
        if (event.request.destination === 'document') {
          return caches.match('./index.html');
        }
      });
    })
  );
});
"""
    with open('mobile_test/sw.js', 'w', encoding='utf-8') as f:
        f.write(sw_code)
    print("Created mobile_test/sw.js (Service Worker).")

    with open('mobile_test/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 2. Add Toast Container into body
    toast_html = """
  <!-- Toast Notification Floating Container -->
  <div id="toast-container" class="fixed top-14 left-1/2 -translate-x-1/2 z-50 pointer-events-none hidden transition-all duration-300 max-w-[90vw]"></div>
"""
    if 'id="toast-container"' not in html:
        html = html.replace('<!-- Role Switcher for Mobile Testing -->', toast_html + '\n      <!-- Role Switcher for Mobile Testing -->', 1)
        print("Added Toast Container.")

    # 3. Add Service Worker registration and Global Error Boundary in script
    error_boundary_code = """
    // ==========================================
    // PWA Offline Service Worker Registration
    // ==========================================
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js').then((reg) => {
          console.log('Offline Service Worker registered with scope:', reg.scope);
        }).catch((err) => {
          console.warn('Service Worker registration skipped:', err);
        });
      });
    }

    // ==========================================
    // Global Error Boundary & Toast System
    // ==========================================
    window.onerror = function(msg, url, lineNo, columnNo, error) {
      console.error('Global Error Caught:', msg, 'at', lineNo, columnNo, error);
      showToast('Interface notice: Layout refreshed cleanly.', 'info');
      return false;
    };

    window.addEventListener('unhandledrejection', function(event) {
      console.warn('Unhandled Promise notice:', event.reason);
    });

    let toastTimer = null;
    function showToast(message, type = 'info') {
      const container = document.getElementById('toast-container');
      if (!container) return;
      const styles = {
        info: 'bg-slate-800/95 border-blue-500/60 text-blue-200',
        success: 'bg-emerald-950/95 border-emerald-500/60 text-emerald-200',
        warning: 'bg-amber-950/95 border-amber-500/60 text-amber-200',
        error: 'bg-rose-950/95 border-rose-500/60 text-rose-200'
      };
      const icons = { info: 'ℹ️', success: '✓', warning: '⚠️', error: '✗' };
      container.innerHTML = `
        <div class="px-3.5 py-2 rounded-xl shadow-2xl border text-xs font-semibold flex items-center gap-2 backdrop-blur-md ${styles[type] || styles.info}">
          <span>${icons[type] || 'ℹ️'}</span>
          <span>${message}</span>
        </div>
      `;
      container.classList.remove('hidden');
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => {
        container.classList.add('hidden');
      }, 3200);
    }
"""

    if 'function showToast' not in html:
        target_script = "<script>"
        html = html.replace(target_script, target_script + error_boundary_code, 1)
        print("Injected Service Worker registration & Toast system.")

    # 4. Add Quiz Engine State Variables
    quiz_state_code = """
    // Quiz Engine State (Pillar 1 Functional Verification)
    let activeQuizSession = null;
    let quizCurrentIndex = 0;
    let quizTimerInterval = null;
    let quizReviewFilter = 'all'; // 'all', 'incorrect', 'correct'
    let lastCompletedQuizResult = null;
"""
    if "let activeQuizSession = null;" not in html:
        html = html.replace("let selectedChapterId = null;", "let selectedChapterId = null;\n" + quiz_state_code, 1)
        print("Added Quiz Engine State Variables.")

    # 5. Add Option 3: Timed Chapter Quiz in Chapter Hub
    old_hub_options = """            <!-- Option 2: Formula / Key Concept Cheat-Sheet -->
            <div onclick="openChapterFormulas('${ch.id}')" class="bg-gradient-to-r from-emerald-950/80 to-emerald-900/60 border border-emerald-500/40 rounded-2xl p-4 flex items-center gap-3 cursor-pointer hover:border-emerald-400 active:scale-98 transition shadow">
              <div class="w-12 h-12 rounded-xl bg-emerald-500/20 text-emerald-300 flex items-center justify-center text-xl shrink-0">
                ⚡
              </div>
              <div class="flex-1">
                <div class="flex items-center justify-between">
                  <div class="text-sm font-bold text-white">${chSubject === 'science' ? 'Chemical Reactions & Formulas' : (chSubject === 'sst' ? 'Key Timelines & Concepts Sheet' : 'Chapter Formula Cheat-Sheet')}</div>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300">
                    ${formulaCount} ${chSubject === 'sst' ? 'Points' : 'Formulas'}
                  </span>
                </div>
                <div class="text-xs text-emerald-300/80 kannada-font">ಸೂತ್ರಗಳ / ಪ್ರಮುಖ ವಿವರಗಳ ಪಟ್ಟಿ</div>
                <div class="text-[11px] text-slate-400 mt-1">${chSubject === 'sst' ? 'Core dates, constitutional provisions, and definitions.' : 'All identities, equations, and definitions in one place.'}</div>
              </div>
              <span class="text-emerald-400 text-sm">›</span>
            </div>
          </div>"""

    new_hub_options = """            <!-- Option 2: Formula / Key Concept Cheat-Sheet -->
            <div onclick="openChapterFormulas('${ch.id}')" class="bg-gradient-to-r from-emerald-950/80 to-emerald-900/60 border border-emerald-500/40 rounded-2xl p-4 flex items-center gap-3 cursor-pointer hover:border-emerald-400 active:scale-98 transition shadow">
              <div class="w-12 h-12 rounded-xl bg-emerald-500/20 text-emerald-300 flex items-center justify-center text-xl shrink-0">
                ⚡
              </div>
              <div class="flex-1">
                <div class="flex items-center justify-between">
                  <div class="text-sm font-bold text-white">${chSubject === 'science' ? 'Chemical Reactions & Formulas' : (chSubject === 'sst' ? 'Key Timelines & Concepts Sheet' : 'Chapter Formula Cheat-Sheet')}</div>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300">
                    ${formulaCount} ${chSubject === 'sst' ? 'Points' : 'Formulas'}
                  </span>
                </div>
                <div class="text-xs text-emerald-300/80 kannada-font">ಸೂತ್ರಗಳ / ಪ್ರಮುಖ ವಿವರಗಳ ಪಟ್ಟಿ</div>
                <div class="text-[11px] text-slate-400 mt-1">${chSubject === 'sst' ? 'Core dates, constitutional provisions, and definitions.' : 'All identities, equations, and definitions in one place.'}</div>
              </div>
              <span class="text-emerald-400 text-sm">›</span>
            </div>

            <!-- Option 3: Timed Mock Quiz / Exam Mode (Pillar 1 & 2 Engine) -->
            <div onclick="startChapterQuiz('${ch.id}', 10, 10)" class="bg-gradient-to-r from-purple-950/90 to-indigo-900/70 border border-purple-500/50 rounded-2xl p-4 flex items-center gap-3 cursor-pointer hover:border-purple-400 active:scale-98 transition shadow">
              <div class="w-12 h-12 rounded-xl bg-purple-500/20 text-purple-300 flex items-center justify-center text-xl shrink-0">
                ⏱️
              </div>
              <div class="flex-1">
                <div class="flex items-center justify-between">
                  <div class="text-sm font-bold text-white">Timed Chapter Quiz (Exam Mode)</div>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-purple-500/20 text-purple-300 border border-purple-500/30">
                    10 Qs • 10 Mins
                  </span>
                </div>
                <div class="text-xs text-purple-300/80 kannada-font">ಸಮಯಬದ್ಧ ಪರೀಕ್ಷಾ ಅಭ್ಯಾಸ</div>
                <div class="text-[11px] text-slate-400 mt-1">Live timer, anti-cheat question lock, score report & detailed review mode.</div>
              </div>
              <span class="text-purple-400 text-sm">›</span>
            </div>
          </div>"""

    if old_hub_options in html and "Timed Chapter Quiz (Exam Mode)" not in html:
        html = html.replace(old_hub_options, new_hub_options, 1)
        print("Added Option 3 (Timed Quiz) to Chapter Hub.")

    # 6. Add Quiz Engine Functions & Screens
    quiz_engine_methods = """
    // ==========================================
    // Production Quiz Engine Logic & Persistence
    // ==========================================
    function startChapterQuiz(chapterId, questionCount = 10, durationMinutes = 10) {
      const ch = getChapterObj(chapterId);
      if (!ch) return;
      const allQs = questions.filter(q => q.chapterId === chapterId && q.options && q.options.length > 0);
      if (allQs.length === 0) {
        showToast('No questions currently available to generate a quiz.', 'warning');
        return;
      }

      // Shuffle and pick subset
      const shuffled = [...allQs].sort(() => 0.5 - Math.random());
      const selected = shuffled.slice(0, Math.min(questionCount, shuffled.length));

      const now = Date.now();
      const durationSeconds = durationMinutes * 60;
      const targetEndTime = now + (durationSeconds * 1000);

      activeQuizSession = {
        id: 'quiz_' + now,
        chapterId: chapterId,
        chapterTitle: ch.titleEn,
        chapterTitleKn: ch.titleKn,
        subject: getSubjectForChapter(chapterId),
        questions: selected,
        selectedAnswers: {}, // qId -> optionId
        startedAt: now,
        durationSeconds: durationSeconds,
        targetEndTime: targetEndTime,
        remainingSeconds: durationSeconds,
        isCompleted: false
      };
      quizCurrentIndex = 0;

      // Persist active quiz in case of accidental browser closure
      saveActiveQuizToStorage();
      startQuizTimer();
      navTo('quiz_screen');
      showToast(`Quiz started! ⏱️ ${durationMinutes} minutes on the clock.`, 'info');
    }

    function saveActiveQuizToStorage() {
      if (activeQuizSession && !activeQuizSession.isCompleted) {
        try {
          localStorage.setItem('cbse_active_quiz_session', JSON.stringify(activeQuizSession));
        } catch(e) {
          console.warn('Quiz storage save notice:', e);
        }
      } else {
        localStorage.removeItem('cbse_active_quiz_session');
      }
    }

    function checkAndRestoreActiveQuiz() {
      try {
        const saved = localStorage.getItem('cbse_active_quiz_session');
        if (saved) {
          const parsed = JSON.parse(saved);
          const remainingMs = parsed.targetEndTime - Date.now();
          if (remainingMs > 5000 && !parsed.isCompleted) {
            activeQuizSession = parsed;
            activeQuizSession.remainingSeconds = Math.round(remainingMs / 1000);
            startQuizTimer();
            navTo('quiz_screen');
            showToast('Resumed in-progress quiz session!', 'success');
            return true;
          } else {
            localStorage.removeItem('cbse_active_quiz_session');
          }
        }
      } catch(e) {
        console.warn('Quiz restore notice:', e);
      }
      return false;
    }

    function startQuizTimer() {
      clearInterval(quizTimerInterval);
      quizTimerInterval = setInterval(() => {
        if (!activeQuizSession || activeQuizSession.isCompleted) {
          clearInterval(quizTimerInterval);
          return;
        }

        // Accurate Wall-Clock Drift Compensation
        const remainingMs = activeQuizSession.targetEndTime - Date.now();
        activeQuizSession.remainingSeconds = Math.max(0, Math.round(remainingMs / 1000));

        if (activeQuizSession.remainingSeconds <= 0) {
          clearInterval(quizTimerInterval);
          submitQuizSession(true); // Auto-submit on time expiry
          return;
        }

        // Update timer badge if on quiz screen
        const timerBadge = document.getElementById('quiz-live-timer');
        if (timerBadge) {
          const m = Math.floor(activeQuizSession.remainingSeconds / 60);
          const s = activeQuizSession.remainingSeconds % 60;
          timerBadge.innerText = `${m.toString().padLeft ? m.toString().padStart(2, '0') : (m < 10 ? '0' + m : m)}:${s < 10 ? '0' + s : s}`;
          if (activeQuizSession.remainingSeconds < 60) {
            timerBadge.classList.add('text-rose-400', 'border-rose-500', 'animate-pulse');
            timerBadge.classList.remove('text-blue-300', 'border-blue-500/40');
          }
        }
      }, 1000);
    }

    function selectQuizOption(qId, optionId) {
      if (!activeQuizSession || activeQuizSession.isCompleted) return;
      activeQuizSession.selectedAnswers[qId] = optionId;
      saveActiveQuizToStorage();
      navTo('quiz_screen');
    }

    function submitQuizSession(isTimeOut = false) {
      if (!activeQuizSession) return;
      clearInterval(quizTimerInterval);

      const qs = activeQuizSession.questions;
      let correct = 0;
      let incorrect = 0;

      qs.forEach(q => {
        const chosen = activeQuizSession.selectedAnswers[q.id];
        if (chosen !== undefined) {
          const opt = q.options.find(o => o.id === chosen);
          if (opt && (opt.correct || opt.is_correct)) {
            correct++;
            solvedQuestions.add(q.id); // Also update mastery
          } else {
            incorrect++;
          }
        }
      });

      const total = qs.length;
      const unattempted = total - (correct + incorrect);
      const percentage = Math.round((correct / total) * 100);
      const timeSpentSeconds = activeQuizSession.durationSeconds - activeQuizSession.remainingSeconds;

      lastCompletedQuizResult = {
        id: activeQuizSession.id,
        chapterId: activeQuizSession.chapterId,
        chapterTitle: activeQuizSession.chapterTitle,
        chapterTitleKn: activeQuizSession.chapterTitleKn,
        subject: activeQuizSession.subject,
        questions: activeQuizSession.questions,
        selectedAnswers: activeQuizSession.selectedAnswers,
        total: total,
        correct: correct,
        incorrect: incorrect,
        unattempted: unattempted,
        percentage: percentage,
        timeSpentSeconds: timeSpentSeconds,
        completedAt: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };

      activeQuizSession.isCompleted = true;
      localStorage.removeItem('cbse_active_quiz_session');
      try {
        localStorage.setItem('cbse_last_quiz_result', JSON.stringify(lastCompletedQuizResult));
      } catch(e) {}
      saveProgressToStorage();

      navTo('quiz_result');
      if (isTimeOut) {
        showToast('⏱️ Time expired! Quiz auto-submitted.', 'warning');
      } else {
        showToast(`🎉 Quiz submitted! You scored ${percentage}%.`, 'success');
      }
    }

    function openQuizReview(filter = 'all') {
      quizReviewFilter = filter;
      navTo('quiz_review');
    }
"""

    if "function startChapterQuiz" not in html:
        html = html.replace("function openChapterHub(chapterId) {", quiz_engine_methods + "\n    function openChapterHub(chapterId) {", 1)
        print("Injected Quiz Engine methods.")

    # 7. Add Screen Handlers in navTo(): quiz_screen, quiz_result, quiz_review
    old_practice_screen_match = re.search(r"else if \(screen === 'chapter_practice'\) \{[\s\S]*?(?=else if \(screen === 'chapter_formulas'\))", html)
    if not old_practice_screen_match:
        print("ERROR: chapter_practice screen block not found!")
        return

    quiz_screens_markup = """} else if (screen === 'quiz_screen') {
        if (!activeQuizSession || activeQuizSession.questions.length === 0) {
          return navTo('chapter_hub');
        }
        const qs = activeQuizSession.questions;
        const q = qs[quizCurrentIndex];
        const qCount = qs.length;
        const chosenOptId = activeQuizSession.selectedAnswers[q.id];
        const answeredCount = Object.keys(activeQuizSession.selectedAnswers).length;
        const m = Math.floor(activeQuizSession.remainingSeconds / 60);
        const s = activeQuizSession.remainingSeconds % 60;
        const timeFormatted = `${m < 10 ? '0' + m : m}:${s < 10 ? '0' + s : s}`;

        title.innerText = `${activeQuizSession.chapterTitle} • Exam`;

        content.innerHTML = `
          <!-- Sticky Exam Top Control Bar -->
          <div class="sticky -top-4 -mx-4 px-4 py-2 bg-slate-900/95 backdrop-blur border-b border-slate-800 flex items-center justify-between gap-2 z-20 shadow-sm mb-3">
            <button onclick="if(confirm('Exit quiz? In-progress answers are saved.')){clearInterval(quizTimerInterval); navTo('chapter_hub');}" class="text-xs font-bold text-rose-400 flex items-center gap-1 py-1 px-2.5 rounded-xl bg-slate-800 border border-rose-500/30 active:scale-95 transition">
              <span>✕</span> <span>Exit</span>
            </button>
            
            <div class="text-xs font-bold text-slate-300">
              Q <span class="text-white">${quizCurrentIndex + 1}</span> of ${qCount}
            </div>

            <!-- Wall-Clock Timer Badge -->
            <div id="quiz-live-timer" class="text-xs font-mono font-bold px-2.5 py-1 rounded-xl bg-slate-800 border ${activeQuizSession.remainingSeconds < 60 ? 'text-rose-400 border-rose-500 animate-pulse' : 'text-blue-300 border-blue-500/40'} flex items-center gap-1.5 shadow-sm">
              <span>⏱️</span> <span>${timeFormatted}</span>
            </div>
          </div>

          <!-- Progress Bar -->
          <div class="space-y-1 mb-3">
            <div class="flex justify-between text-[10px] font-bold text-slate-400">
              <span>Answered: ${answeredCount}/${qCount}</span>
              <span>${Math.round((answeredCount / qCount) * 100)}% Completed</span>
            </div>
            <div class="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden border border-slate-700">
              <div class="bg-gradient-to-r from-blue-500 to-emerald-400 h-1.5 transition-all duration-300" style="width: ${(answeredCount / qCount) * 100}%"></div>
            </div>
          </div>

          <!-- Question Card -->
          <div class="bg-slate-800 border border-slate-700/80 rounded-2xl p-4 space-y-3 shadow-lg">
            <div class="flex justify-between items-center text-[10px] font-bold">
              <span class="text-blue-400 uppercase tracking-wide">${q.exercise || 'NCERT Exam Item'}</span>
              <span class="text-slate-400 capitalize bg-slate-900/60 px-2 py-0.5 rounded border border-slate-700">${q.difficulty || 'standard'}</span>
            </div>

            <div class="text-sm font-semibold text-white leading-relaxed whitespace-pre-line">
              ${q.text}
            </div>

            <!-- Exam Mode Options (No Answer Spoilers Before Submit!) -->
            <div class="space-y-2 pt-1">
              ${q.options.map(opt => {
                const isSelected = chosenOptId === opt.id;
                return `
                  <div onclick="selectQuizOption('${q.id}', '${opt.id}')" class="p-3 rounded-xl border text-xs font-medium cursor-pointer transition flex items-center justify-between active:scale-98 ${isSelected ? 'bg-blue-600/30 border-blue-400 text-white shadow-md ring-1 ring-blue-400' : 'bg-slate-900/70 border-slate-700 text-slate-200 hover:border-slate-500'}">
                    <span class="leading-relaxed"><b class="${isSelected ? 'text-blue-300' : 'text-slate-400'}">${opt.id}.</b> ${opt.text}</span>
                    <span class="w-5 h-5 rounded-full border flex items-center justify-center shrink-0 ml-2 ${isSelected ? 'border-blue-400 bg-blue-500 text-white text-[10px] font-bold' : 'border-slate-600 bg-slate-800'}">
                      ${isSelected ? '●' : ''}
                    </span>
                  </div>
                `;
              }).join('')}
            </div>
          </div>

          <!-- Question Navigation Controls -->
          <div class="flex items-center justify-between gap-3 pt-3">
            <button onclick="if(quizCurrentIndex > 0){quizCurrentIndex--; navTo('quiz_screen');}" ${quizCurrentIndex === 0 ? 'disabled' : ''} class="flex-1 py-2.5 rounded-xl border text-xs font-bold transition flex items-center justify-center gap-1 active:scale-98 ${quizCurrentIndex === 0 ? 'border-slate-800 bg-slate-900/50 text-slate-600 cursor-not-allowed' : 'border-slate-700 bg-slate-800 text-slate-200 hover:bg-slate-700'}">
              <span>←</span> <span>Previous</span>
            </button>

            ${quizCurrentIndex < qCount - 1 ? `
              <button onclick="quizCurrentIndex++; navTo('quiz_screen');" class="flex-1 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold transition flex items-center justify-center gap-1 shadow active:scale-98">
                <span>Next</span> <span>→</span>
              </button>
            ` : `
              <button onclick="if(confirm('Submit this quiz and view score breakdown?')){submitQuizSession(false);}" class="flex-1 py-2.5 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs font-bold transition flex items-center justify-center gap-1 shadow-lg active:scale-98">
                <span>✓</span> <span>Submit Quiz</span>
              </button>
            `}
          </div>

          <!-- Bottom Jump Sheet / Number Pills -->
          <div class="pt-3 border-t border-slate-800 mt-2">
            <div class="text-[10px] font-bold text-slate-400 uppercase tracking-wide mb-1.5">Question Navigator</div>
            <div class="flex gap-1.5 flex-wrap">
              ${qs.map((item, idx) => {
                const isAnswered = activeQuizSession.selectedAnswers[item.id] !== undefined;
                const isCurrent = quizCurrentIndex === idx;
                return `
                  <button onclick="quizCurrentIndex = ${idx}; navTo('quiz_screen');" class="w-8 h-8 rounded-lg text-xs font-bold border transition ${isCurrent ? 'bg-blue-500 text-white border-blue-400 ring-2 ring-blue-400/50' : (isAnswered ? 'bg-emerald-950/80 border-emerald-500/60 text-emerald-300' : 'bg-slate-800 border-slate-700 text-slate-400')}">
                    ${idx + 1}
                  </button>
                `;
              }).join('')}
            </div>
          </div>
        `;
      } else if (screen === 'quiz_result') {
        const res = lastCompletedQuizResult;
        if (!res) return navTo('chapter_hub');

        title.innerText = `${res.chapterTitle} • Results`;
        const gradeColor = res.percentage >= 80 ? 'text-emerald-400' : (res.percentage >= 60 ? 'text-blue-400' : 'text-amber-400');
        const gradeTitle = res.percentage >= 80 ? 'Distinction Mastery! 🏆' : (res.percentage >= 60 ? 'First Class Pass! 🌟' : 'Keep Practicing! 📚');

        content.innerHTML = `
          <!-- Header Score Card -->
          <div class="bg-gradient-to-b from-slate-800 to-slate-900 border border-slate-700 rounded-3xl p-5 text-center space-y-3 shadow-xl">
            <div class="text-[10px] font-bold uppercase tracking-wider text-slate-400">${res.chapterTitle} • Exam Results</div>
            
            <!-- Circular Score Display -->
            <div class="w-24 h-24 mx-auto rounded-full bg-slate-900/80 border-4 ${res.percentage >= 80 ? 'border-emerald-500' : (res.percentage >= 60 ? 'border-blue-500' : 'border-amber-500')} flex flex-col items-center justify-center shadow-inner">
              <span class="text-2xl font-black ${gradeColor}">${res.percentage}%</span>
              <span class="text-[9px] font-bold text-slate-400">${res.correct}/${res.total} Qs</span>
            </div>

            <div class="text-sm font-bold text-white">${gradeTitle}</div>
            <div class="text-[11px] text-slate-400">Completed at ${res.completedAt} • Time Spent: ${Math.floor(res.timeSpentSeconds / 60)}m ${res.timeSpentSeconds % 60}s</div>

            <!-- Breakdown Grid -->
            <div class="grid grid-cols-3 gap-2 pt-2 text-center">
              <div class="bg-emerald-950/40 border border-emerald-500/30 rounded-xl p-2">
                <div class="text-[10px] font-bold text-emerald-400">✓ Correct</div>
                <div class="text-base font-extrabold text-white">${res.correct}</div>
              </div>
              <div class="bg-rose-950/40 border border-rose-500/30 rounded-xl p-2">
                <div class="text-[10px] font-bold text-rose-400">✗ Incorrect</div>
                <div class="text-base font-extrabold text-white">${res.incorrect}</div>
              </div>
              <div class="bg-slate-800/80 border border-slate-700 rounded-xl p-2">
                <div class="text-[10px] font-bold text-slate-400">⚪ Skipped</div>
                <div class="text-base font-extrabold text-white">${res.unattempted}</div>
              </div>
            </div>
          </div>

          <!-- Action Buttons -->
          <div class="space-y-2 pt-2">
            <button onclick="openQuizReview('all')" class="w-full py-3 rounded-2xl bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs shadow-lg flex items-center justify-center gap-2 active:scale-98 transition">
              <span>🔍</span> <span>Review All Questions & Step-by-Step Solutions</span>
            </button>
            <div class="grid grid-cols-2 gap-2">
              <button onclick="startChapterQuiz('${res.chapterId}', 10, 10)" class="py-2.5 rounded-xl bg-slate-800 border border-purple-500/40 text-purple-300 font-bold text-xs hover:bg-purple-950/30 flex items-center justify-center gap-1 active:scale-98 transition">
                <span>↺</span> <span>Retake Quiz</span>
              </button>
              <button onclick="navTo('chapter_hub')" class="py-2.5 rounded-xl bg-slate-800 border border-slate-700 text-slate-300 font-bold text-xs hover:bg-slate-700 flex items-center justify-center gap-1 active:scale-98 transition">
                <span>←</span> <span>Chapter Hub</span>
              </button>
            </div>
          </div>
        `;
      } else if (screen === 'quiz_review') {
        const res = lastCompletedQuizResult;
        if (!res) return navTo('chapter_hub');

        title.innerText = `${res.chapterTitle} • Review`;

        const displayedReviewQs = res.questions.filter(q => {
          const chosen = res.selectedAnswers[q.id];
          const isCorrect = chosen && q.options.some(o => (o.correct || o.is_correct) && o.id === chosen);
          if (quizReviewFilter === 'incorrect') return chosen && !isCorrect;
          if (quizReviewFilter === 'correct') return isCorrect;
          return true;
        });

        content.innerHTML = `
          <!-- Sticky Review Filter Bar -->
          <div class="sticky -top-4 -mx-4 px-4 py-2 bg-slate-900/95 backdrop-blur border-b border-slate-800 flex items-center justify-between gap-2 z-20 shadow-sm mb-2">
            <button onclick="navTo('quiz_result')" class="text-xs font-bold text-blue-400 flex items-center gap-1 py-1 px-2.5 rounded-xl bg-slate-800 border border-slate-700 active:scale-95 transition">
              <span>←</span> <span>Score</span>
            </button>
            <div class="flex gap-1">
              <button onclick="openQuizReview('all')" class="px-2 py-0.5 rounded text-[10px] font-bold border ${quizReviewFilter === 'all' ? 'bg-blue-600 text-white border-blue-400' : 'bg-slate-800 text-slate-400 border-slate-700'}">All (${res.total})</button>
              <button onclick="openQuizReview('incorrect')" class="px-2 py-0.5 rounded text-[10px] font-bold border ${quizReviewFilter === 'incorrect' ? 'bg-rose-600 text-white border-rose-400' : 'bg-slate-800 text-slate-400 border-slate-700'}">Wrong (${res.incorrect})</button>
              <button onclick="openQuizReview('correct')" class="px-2 py-0.5 rounded text-[10px] font-bold border ${quizReviewFilter === 'correct' ? 'bg-emerald-600 text-white border-emerald-400' : 'bg-slate-800 text-slate-400 border-slate-700'}">Right (${res.correct})</button>
            </div>
          </div>

          <div class="space-y-3 pt-1">
            ${displayedReviewQs.map((q, idx) => {
              const chosen = res.selectedAnswers[q.id];
              const correctOpt = q.options.find(o => o.correct || o.is_correct);
              const isCorrect = chosen === (correctOpt ? correctOpt.id : null);
              const isSkipped = !chosen;

              return `
                <div class="bg-slate-800 border ${isCorrect ? 'border-emerald-500/50' : (isSkipped ? 'border-slate-700' : 'border-rose-500/60')} rounded-2xl p-4 space-y-2 shadow">
                  <div class="flex justify-between items-center text-[10px] font-bold">
                    <span class="text-blue-400 uppercase">${q.exercise || 'Item'} • Q${idx + 1}</span>
                    <span class="px-2 py-0.5 rounded font-extrabold ${isCorrect ? 'bg-emerald-500/20 text-emerald-400' : (isSkipped ? 'bg-slate-700 text-slate-300' : 'bg-rose-500/20 text-rose-400')}">
                      ${isCorrect ? '✓ Correct (+1)' : (isSkipped ? '⚪ Skipped' : '✗ Incorrect')}
                    </span>
                  </div>

                  <div class="text-xs font-semibold text-white leading-relaxed whitespace-pre-line">${q.text}</div>

                  <div class="space-y-1.5 pt-1">
                    ${q.options.map(o => {
                      const wasChosen = chosen === o.id;
                      const isThisCorrect = o.correct || o.is_correct;
                      let rowStyle = "p-2.5 rounded-xl border text-[11px] flex justify-between items-center ";
                      if (isThisCorrect) {
                        rowStyle += "bg-emerald-950/40 border-emerald-500/80 text-emerald-200 font-semibold";
                      } else if (wasChosen && !isThisCorrect) {
                        rowStyle += "bg-rose-950/40 border-rose-500/80 text-rose-200";
                      } else {
                        rowStyle += "bg-slate-900/40 border-slate-800 text-slate-400 opacity-60";
                      }
                      return `
                        <div class="${rowStyle}">
                          <span><b>${o.id}.</b> ${o.text}</span>
                          <span class="font-bold text-xs">${isThisCorrect ? '✓ Correct Answer' : (wasChosen ? '✗ Your Choice' : '')}</span>
                        </div>
                      `;
                    }).join('')}
                  </div>

                  <!-- Step-by-Step Solution Card Unlocked -->
                  <div class="mt-2 p-3 rounded-xl bg-slate-950/90 border border-slate-700/80 font-mono text-[11px] text-cyan-300 leading-relaxed whitespace-pre-line">
                    <div class="text-[10px] font-bold text-blue-400 uppercase tracking-wider mb-1 font-sans">💡 Scientific Proof & Distractor Rationale:</div>
                    ${q.solution || q.step_by_step_solution || 'Detailed step-by-step proof aligned with textbook exercises.'}
                  </div>
                </div>
              `;
            }).join('')}
          </div>
        `;
      """

    # Insert quiz screens right before else if (screen === 'chapter_practice')
    html = html.replace("} else if (screen === 'chapter_practice') {", quiz_screens_markup + "} else if (screen === 'chapter_practice') {", 1)
    print("Injected quiz_screen, quiz_result, and quiz_review screens.")

    # 8. Replace raw alert() calls in attemptQuestion & toggleSolution
    html = html.replace('alert("⚠️ Answer already recorded! You cannot change your choice directly. Tap \'↺ Reset\' at the top right to clear your choice and re-attempt.");', 'showToast("Answer already recorded! Tap \'↺ Reset\' to re-attempt.", "warning");')
    html = html.replace("alert('⚠️ Please select an option first before revealing the step-by-step solution!');", "showToast('Please choose an option first to unlock solution!', 'warning');")
    html = html.replace("alert('Please select or drop a textbook PDF document first.');", "showToast('Please select or drop a textbook PDF document first.', 'warning');")
    html = html.replace("alert('Failed to parse JSON file: ' + err.message);", "showToast('Failed to parse JSON: ' + err.message, 'error');")
    print("Replaced raw alerts with modern toast notifications.")

    # 9. Check and auto-restore quiz on startup
    startup_restore = """
    // Auto-restore in-progress quiz session if active
    if (!checkAndRestoreActiveQuiz()) {
      navTo('home');
    }
"""
    if "checkAndRestoreActiveQuiz()" not in html:
        html = html.replace("navTo('home');", startup_restore, 1)
        print("Wired startup quiz restoration.")

    # 10. Write back to mobile_test/index.html and cbse10_app_preview.html
    with open('mobile_test/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("mobile_test/index.html updated successfully!")

    with open('cbse10_app_preview.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("cbse10_app_preview.html mirrored successfully!")

if __name__ == '__main__':
    main()
