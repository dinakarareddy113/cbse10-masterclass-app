import re

def update_file(path):
    print(f"Processing {path}...")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update <style> with enhanced polish
    old_style = """  <style>
    body { -webkit-tap-highlight-color: transparent; user-select: none; }
    .kannada-font { font-family: system-ui, -apple-system, sans-serif; }
    .katex { font-size: 1.05em; color: #67e8f9; }
    .katex-display { margin: 0.5em 0; overflow-x: auto; overflow-y: hidden; }
  </style>"""

    new_style = """  <style>
    body { -webkit-tap-highlight-color: transparent; user-select: none; -webkit-font-smoothing: antialiased; }
    .kannada-font { font-family: 'Noto Sans Kannada', system-ui, -apple-system, sans-serif; }
    .katex { font-size: 1.05em; color: #67e8f9; }
    .katex-display { margin: 0.5em 0; overflow-x: auto; overflow-y: hidden; max-width: 100%; padding: 0.25rem 0; }
    ::-webkit-scrollbar { width: 4px; height: 4px; }
    ::-webkit-scrollbar-thumb { background: rgba(148, 163, 184, 0.2); border-radius: 4px; }
  </style>"""

    if old_style in content:
        content = content.replace(old_style, new_style)
        print("  [x] Updated CSS styling & scrollbar polish")
    else:
        print("  [!] old_style not found exactly, checking fallback")

    # 2. Add pb-28 to mobile-main-content
    old_main = '<main id="mobile-main-content" class="flex-1 overflow-y-auto p-4 space-y-4">'
    new_main = '<main id="mobile-main-content" class="flex-1 overflow-y-auto p-4 pb-28 space-y-4">'
    if old_main in content:
        content = content.replace(old_main, new_main)
        print("  [x] Added pb-28 to #mobile-main-content")
    else:
        print("  [!] old_main not found or already updated")

    # 3. Inject SafeStorage wrapper and update initial persistent state
    old_storage_init = """    // Persistent Student Learning State
    let savedSolvedJson = localStorage.getItem('cbse_solved_questions');
    let solvedQuestions = new Set(savedSolvedJson ? JSON.parse(savedSolvedJson) : ['m1']);
    
    let savedChoicesJson = localStorage.getItem('cbse_user_choices');
    let userSelectedOptions = savedChoicesJson ? JSON.parse(savedChoicesJson) : {};
    
    let savedProfileJson = localStorage.getItem('cbse_student_profile');
    let studentProfile = savedProfileJson ? JSON.parse(savedProfileJson) : null;
    let selectedClassLevel = studentProfile ? (studentProfile.classLevel || 'Class 10') : 'Class 10';

    function saveProgressToStorage() {
      try {
        localStorage.setItem('cbse_solved_questions', JSON.stringify(Array.from(solvedQuestions)));
        localStorage.setItem('cbse_user_choices', JSON.stringify(userSelectedOptions));
      } catch (err) {
        console.warn('LocalStorage save failed:', err);
      }
    }

    function recordChapterAccess(chapterId) {
      if (!chapterId) return;
      const subj = getSubjectForChapter(chapterId);
      try {
        localStorage.setItem('cbse_last_studied_chapter', chapterId);
        localStorage.setItem('cbse_last_chapter_' + subj, chapterId);
      } catch (err) {
        console.warn('LocalStorage save failed:', err);
      }
    }"""

    new_storage_init = """    // SafeStorage Wrapper: Shields application against iOS Safari Incognito restrictions,
    // QuotaExceededError, or blocked 3rd-party storage by providing an in-memory fallback.
    const SafeStorage = {
      _mem: {},
      getItem(key) {
        try {
          return window.localStorage ? window.localStorage.getItem(key) : (this._mem[key] || null);
        } catch (e) {
          return this._mem[key] || null;
        }
      },
      setItem(key, value) {
        try {
          if (window.localStorage) window.localStorage.setItem(key, value);
        } catch (e) {
          console.warn('SafeStorage quota/restriction, fallback to memory:', e);
        }
        this._mem[key] = String(value);
      },
      removeItem(key) {
        try {
          if (window.localStorage) window.localStorage.removeItem(key);
        } catch (e) {}
        delete this._mem[key];
      },
      clear() {
        try {
          if (window.localStorage) window.localStorage.clear();
        } catch (e) {}
        this._mem = {};
      }
    };

    // Persistent Student Learning State
    let savedSolvedJson = SafeStorage.getItem('cbse_solved_questions');
    let solvedQuestions = new Set(savedSolvedJson ? JSON.parse(savedSolvedJson) : ['m1']);
    
    let savedChoicesJson = SafeStorage.getItem('cbse_user_choices');
    let userSelectedOptions = savedChoicesJson ? JSON.parse(savedChoicesJson) : {};
    
    let savedProfileJson = SafeStorage.getItem('cbse_student_profile');
    let studentProfile = savedProfileJson ? JSON.parse(savedProfileJson) : null;
    let selectedClassLevel = studentProfile ? (studentProfile.classLevel || 'Class 10') : 'Class 10';

    function saveProgressToStorage() {
      try {
        SafeStorage.setItem('cbse_solved_questions', JSON.stringify(Array.from(solvedQuestions)));
        SafeStorage.setItem('cbse_user_choices', JSON.stringify(userSelectedOptions));
      } catch (err) {
        console.warn('SafeStorage save failed:', err);
      }
    }

    function recordChapterAccess(chapterId) {
      if (!chapterId) return;
      const subj = getSubjectForChapter(chapterId);
      try {
        SafeStorage.setItem('cbse_last_studied_chapter', chapterId);
        SafeStorage.setItem('cbse_last_chapter_' + subj, chapterId);
      } catch (err) {
        console.warn('SafeStorage save failed:', err);
      }
    }"""

    if old_storage_init in content:
        content = content.replace(old_storage_init, new_storage_init)
        print("  [x] Injected SafeStorage wrapper and updated state functions")
    else:
        print("  [!] old_storage_init not matched directly")

    # 4. Replace other localStorage references
    replacements = [
        ("localStorage.setItem('cbse_student_profile', JSON.stringify(studentProfile));",
         "SafeStorage.setItem('cbse_student_profile', JSON.stringify(studentProfile));"),
        ("localStorage.removeItem('cbse_student_profile');",
         "SafeStorage.removeItem('cbse_student_profile');"),
        ("const lastGlobalChId = localStorage.getItem('cbse_last_studied_chapter') || 'math_ch_01_real_numbers';",
         "const lastGlobalChId = SafeStorage.getItem('cbse_last_studied_chapter') || 'math_ch_01_real_numbers';"),
        ("const lastMathChId = localStorage.getItem('cbse_last_chapter_math');",
         "const lastMathChId = SafeStorage.getItem('cbse_last_chapter_math');"),
        ("const lastSciChId = localStorage.getItem('cbse_last_chapter_science');",
         "const lastSciChId = SafeStorage.getItem('cbse_last_chapter_science');"),
        ("const lastSstChId = localStorage.getItem('cbse_last_chapter_sst');",
         "const lastSstChId = SafeStorage.getItem('cbse_last_chapter_sst');"),
        ("localStorage.setItem('cbse_active_quiz_session', JSON.stringify(activeQuizSession));",
         "SafeStorage.setItem('cbse_active_quiz_session', JSON.stringify(activeQuizSession));"),
        ("localStorage.removeItem('cbse_active_quiz_session');",
         "SafeStorage.removeItem('cbse_active_quiz_session');"),
        ("const saved = localStorage.getItem('cbse_active_quiz_session');",
         "const saved = SafeStorage.getItem('cbse_active_quiz_session');"),
        ("localStorage.setItem('cbse_last_quiz_result', JSON.stringify(lastCompletedQuizResult));",
         "SafeStorage.setItem('cbse_last_quiz_result', JSON.stringify(lastCompletedQuizResult));"),
    ]

    for old_r, new_r in replacements:
        if old_r in content:
            content = content.replace(old_r, new_r)
            print(f"  [x] Replaced: {old_r[:45]}...")

    # 5. Robust Error Boundary around handleAdminPdfFileSelect
    old_file_select = """    function handleAdminPdfFileSelect(event) {
      const file = event.target.files && event.target.files[0];
      if (!file) return;
      uploadedPdfFile = {
        name: file.name,
        size: (file.size / (1024 * 1024)).toFixed(2) + ' MB',
        preloaded: false
      };"""

    new_file_select = """    function handleAdminPdfFileSelect(event) {
      const file = event.target.files && event.target.files[0];
      if (!file) return;

      // Defensive File Boundary & Validation Check
      if (!file.name.toLowerCase().endsWith('.pdf') && file.type !== 'application/pdf') {
        showToast('Invalid file format. Please upload an authentic NCERT PDF document (.pdf).', 'error');
        if (event.target) event.target.value = '';
        return;
      }
      if (file.size === 0) {
        showToast('The selected file is empty (0 bytes).', 'error');
        if (event.target) event.target.value = '';
        return;
      }
      if (file.size > 50 * 1024 * 1024) {
        showToast('File size exceeds the 50MB mobile extraction limit.', 'error');
        if (event.target) event.target.value = '';
        return;
      }

      uploadedPdfFile = {
        name: file.name,
        size: (file.size / (1024 * 1024)).toFixed(2) + ' MB',
        preloaded: false
      };"""

    if old_file_select in content:
        content = content.replace(old_file_select, new_file_select)
        print("  [x] Enhanced handleAdminPdfFileSelect with file size & MIME boundaries")
    else:
        print("  [!] old_file_select not matched directly")

    # 6. startAdminPdfQaGeneration try-catch error boundary
    old_generation = """          setTimeout(() => {
            pdfGenerating = false;
            pdfGenerationProgress = 100;
            const allQs = generateSampleQuestionsForChapter(adminTargetChapterId);
            if (adminExtractionScope === 'intext_p40') {
              pdfGeneratedQuestions = allQs.filter(q => (q.exercise && q.exercise.includes('Page 40')) || (q.section && q.section.includes('Page 40')));
            } else if (adminExtractionScope === 'intext_all') {
              pdfGeneratedQuestions = allQs.filter(q => (q.exercise && q.exercise.toLowerCase().includes('in-text')) || (q.section && q.section.toLowerCase().includes('questions')));
            } else if (adminExtractionScope === 'exercises') {
              pdfGeneratedQuestions = allQs.filter(q => (q.exercise && q.exercise.toLowerCase().includes('exercise')) || (q.section && q.section.toLowerCase().includes('exercise')));
            } else {
              pdfGeneratedQuestions = allQs;
            }
            adminGeneratedFilterExercise = 'All';
            navTo('admin');
          }, 350);"""

    new_generation = """          setTimeout(() => {
            try {
              pdfGenerating = false;
              pdfGenerationProgress = 100;
              const allQs = generateSampleQuestionsForChapter(adminTargetChapterId);
              if (adminExtractionScope === 'intext_p40') {
                pdfGeneratedQuestions = allQs.filter(q => (q.exercise && q.exercise.includes('Page 40')) || (q.section && q.section.includes('Page 40')));
              } else if (adminExtractionScope === 'intext_all') {
                pdfGeneratedQuestions = allQs.filter(q => (q.exercise && q.exercise.toLowerCase().includes('in-text')) || (q.section && q.section.toLowerCase().includes('questions')));
              } else if (adminExtractionScope === 'exercises') {
                pdfGeneratedQuestions = allQs.filter(q => (q.exercise && q.exercise.toLowerCase().includes('exercise')) || (q.section && q.section.toLowerCase().includes('exercise')));
              } else {
                pdfGeneratedQuestions = allQs;
              }
              adminGeneratedFilterExercise = 'All';
              navTo('admin');
              showToast(`Extracted ${pdfGeneratedQuestions.length} isolated questions successfully!`, 'success');
            } catch (err) {
              pdfGenerating = false;
              console.error('Extraction error:', err);
              showToast('Extraction failed: ' + (err.message || 'Unknown parsing error'), 'error');
              navTo('admin');
            }
          }, 350);"""

    if old_generation in content:
        content = content.replace(old_generation, new_generation)
        print("  [x] Enhanced startAdminPdfQaGeneration with try-catch error boundary")
    else:
        print("  [!] old_generation not matched directly")

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Saved {path} successfully.\n")

if __name__ == "__main__":
    update_file("mobile_test/index.html")
    update_file("cbse10_app_preview.html")
