import json

with open("mobile_test/index.html", encoding="utf-8") as f:
    html = f.read()

pos_fn = html.find("function handleAdminPdfFileSelect(event) {")
pos_end = html.find("const scienceCh1MasterQuestions = ", pos_fn)
assert pos_fn != -1 and pos_end != -1

new_admin_fns = """function setAdminCatalogTab(tab) {
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

html = html[:pos_fn] + new_admin_fns + html[pos_end:]

with open("mobile_test/index.html", "w", encoding="utf-8") as f:
    f.write(html)

import shutil
shutil.copyfile("mobile_test/index.html", "C:/Users/csdin/.gemini/antigravity/brain/b1293a4f-a486-4bc1-a2c6-d175611557ba/cbse10_app_preview.html")
print("SUCCESS: Fixed admin JS functions and mirrored to cbse10_app_preview.html!")
