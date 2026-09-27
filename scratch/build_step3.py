import json
import re

# Load datasets
with open("assets/data/ncert_science_ch1.json", encoding="utf-8") as f:
    sci_ch1_data = json.load(f)

with open("assets/data/ncert_science_ch2.json", encoding="utf-8") as f:
    sci_ch2_data = json.load(f)

with open("mobile_test/index.html", encoding="utf-8") as f:
    html = f.read()

print("Original length:", len(html))

# 1. Update State Variables
old_state = "let adminTargetChapterId = 'math_ch_02_polynomials';"
new_state = """let adminTargetClass = 'Class 10';
    let adminTargetSubject = 'science'; // Default to Science as in user's prompt
    let adminTargetChapterId = 'sci_ch_02_acids_bases_salts'; // Matches 2.NCERT-Class-10-Science_2nd Chapter.pdf
    let adminCatalogTab = 'science'; // 'science', 'math', 'sst'
    let adminDetectedMeta = null;
    let activeScienceChapterFilter = 'All'; // Chapter filter for student Science tab"""

if old_state in html:
    html = html.replace(old_state, new_state)
    print("Replaced state variables.")
elif "let adminTargetSubject = 'science';" not in html:
    print("WARNING: Could not find old_state marker")

# 2. Insert scienceChapters and sstChapters after mathChapters
math_end_marker = "    ];\n\n    let questions = ["
if math_end_marker not in html:
    math_end_marker = "    ];\n    let questions = ["

if "const scienceChapters = [" not in html:
    pos = html.find(math_end_marker)
    if pos != -1:
        insert_code = """
    // 13 CBSE Class 10 NCERT Science Chapters (Bilingual English + Kannada)
    const scienceChapters = [
      {
        id: 'sci_ch_01_chemical_reactions',
        num: 1,
        titleEn: 'Chemical Reactions and Equations',
        titleKn: 'ರಾಸಾಯನಿಕ ಕ್ರಿಯೆಗಳು ಮತ್ತು ಸಮೀಕರಣಗಳು',
        summary: 'Balancing chemical equations, combination, decomposition, displacement, double displacement, redox, and rancidity.',
        questionCount: 47
      },
      {
        id: 'sci_ch_02_acids_bases_salts',
        num: 2,
        titleEn: 'Acids, Bases and Salts',
        titleKn: 'ಆಮ್ಲಗಳು, ಪ್ರತ್ಯಾಮ್ಲಗಳು ಮತ್ತು ಲವಣಗಳು',
        summary: 'Indicators, reactions with metals & carbonates, pH scale, dilution principles, salts (bleaching powder, baking soda, washing soda, POP).',
        questionCount: 37
      },
      {
        id: 'sci_ch_03_metals_non_metals',
        num: 3,
        titleEn: 'Metals and Non-metals',
        titleKn: 'ಲೋಹಗಳು ಮತ್ತು ಅಲೋಹಗಳು',
        summary: 'Physical & chemical properties, reactivity series, ionic compounds, extraction of metals, and prevention of corrosion.',
        questionCount: 25
      },
      {
        id: 'sci_ch_04_carbon_compounds',
        num: 4,
        titleEn: 'Carbon and its Compounds',
        titleKn: 'ಕಾರ್ಬನ್ ಮತ್ತು ಅದರ ಸಂಯುಕ್ತಗಳು',
        summary: 'Covalent bonding, versatile nature, homologous series, functional groups, chemical properties of carbon, soaps and detergents.',
        questionCount: 28
      },
      {
        id: 'sci_ch_05_life_processes',
        num: 5,
        titleEn: 'Life Processes',
        titleKn: 'ಜೀವ ಕ್ರಿಯೆಗಳು',
        summary: 'Nutrition (autotrophic & heterotrophic), respiration (aerobic & anaerobic), transportation in humans/plants, and excretion.',
        questionCount: 32
      },
      {
        id: 'sci_ch_06_control_coordination',
        num: 6,
        titleEn: 'Control and Coordination',
        titleKn: 'ನಿಯಂತ್ರಣ ಮತ್ತು ಸಮನ್ವಯ',
        summary: 'Nervous system, reflex arc, human brain, plant hormones (tropisms), and endocrine glands.',
        questionCount: 22
      },
      {
        id: 'sci_ch_07_reproduction',
        num: 7,
        titleEn: 'How do Organisms Reproduce?',
        titleKn: 'ಜೀವಿಗಳು ಹೇಗೆ ಸಂತಾನೋತ್ಪತ್ತಿ ನಡೆಸುತ್ತವೆ?',
        summary: 'Asexual reproduction modes, sexual reproduction in flowering plants, human reproductive systems, and reproductive health.',
        questionCount: 24
      },
      {
        id: 'sci_ch_08_heredity',
        num: 8,
        titleEn: 'Heredity',
        titleKn: 'ಅನುವಂಶೀಯತೆ',
        summary: 'Mendel’s laws of inheritance, monohybrid & dihybrid crosses, and chromosomal sex determination in humans.',
        questionCount: 18
      },
      {
        id: 'sci_ch_09_light',
        num: 9,
        titleEn: 'Light – Reflection and Refraction',
        titleKn: 'ಬೆಳಕು – ಪ್ರತಿಫಲನ ಮತ್ತು ವಕ್ರೀಭವನ',
        summary: 'Spherical mirrors, ray diagrams, mirror formula, magnification, refraction through glass slab, lens formula, and power of a lens.',
        questionCount: 30
      },
      {
        id: 'sci_ch_10_human_eye',
        num: 10,
        titleEn: 'The Human Eye and Colourful World',
        titleKn: 'ಮಾನವನ ಕಣ್ಣು ಮತ್ತು ವರ್ಣರಂಜಿತ ಜಗತ್ತು',
        summary: 'Eye structure, defects of vision (myopia, hypermetropia, presbyopia), dispersion through prism, atmospheric refraction, and scattering.',
        questionCount: 20
      },
      {
        id: 'sci_ch_11_electricity',
        num: 11,
        titleEn: 'Electricity',
        titleKn: 'ವಿದ್ಯುಚ್ಛಕ್ತಿ',
        summary: 'Ohm’s law, resistance factors, series & parallel resistor circuits, Joule’s heating law, and electric power.',
        questionCount: 28
      },
      {
        id: 'sci_ch_12_magnetic_effects',
        num: 12,
        titleEn: 'Magnetic Effects of Electric Current',
        titleKn: 'ವಿದ್ಯುತ್ ಪ್ರವಾಹದ ಕಾಂತೀಯ ಪರಿಣಾಮಗಳು',
        summary: 'Magnetic field lines, right-hand thumb rule, solenoid, Fleming’s left-hand rule, and domestic electric circuits.',
        questionCount: 22
      },
      {
        id: 'sci_ch_13_our_environment',
        num: 13,
        titleEn: 'Our Environment',
        titleKn: 'ನಮ್ಮ ಪರಿಸರ',
        summary: 'Ecosystem components, food chains & food webs, 10% energy law, biological magnification, and ozone layer depletion.',
        questionCount: 18
      }
    ];

    // 7 CBSE Class 10 NCERT Social Science Chapters (Bilingual English + Kannada)
    const sstChapters = [
      {
        id: 'sst_hist_ch_01_europe',
        num: 1,
        subject: 'History',
        titleEn: 'The Rise of Nationalism in Europe',
        titleKn: 'ಯುರೋಪಿನಲ್ಲಿ ರಾಷ್ಟ್ರೀಯತೆಯ ಉದಯ'
      },
      {
        id: 'sst_hist_ch_02_nationalism',
        num: 2,
        subject: 'History',
        titleEn: 'Nationalism in India',
        titleKn: 'ಭಾರತದಲ್ಲಿ ರಾಷ್ಟ್ರೀಯತೆ'
      },
      {
        id: 'sst_geo_ch_01_resources',
        num: 3,
        subject: 'Geography',
        titleEn: 'Resources and Development',
        titleKn: 'ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಅಭಿವೃದ್ಧಿ'
      },
      {
        id: 'sst_geo_ch_07_lifelines',
        num: 4,
        subject: 'Geography',
        titleEn: 'Lifelines of National Economy',
        titleKn: 'ರಾಷ್ಟ್ರೀಯ ಆರ್ಥಿಕತೆಯ ಜೀವನಾಡಿಗಳು'
      },
      {
        id: 'sst_civ_ch_01_power_sharing',
        num: 5,
        subject: 'Civics',
        titleEn: 'Power Sharing',
        titleKn: 'ಅಧಿಕಾರ ಹಂಚಿಕೆ'
      },
      {
        id: 'sst_civ_ch_02_federalism',
        num: 6,
        subject: 'Civics',
        titleEn: 'Federalism',
        titleKn: 'ಸಂಯುಕ್ತ ವ್ಯವಸ್ಥೆ'
      },
      {
        id: 'sst_econ_ch_01_development',
        num: 7,
        subject: 'Economics',
        titleEn: 'Development',
        titleKn: 'ಅಭಿವೃದ್ಧಿ'
      }
    ];

    function getChaptersForSubject(subject) {
      if (subject === 'science') return scienceChapters;
      if (subject === 'sst') return sstChapters;
      return mathChapters;
    }

    function getChapterObj(chId) {
      return scienceChapters.find(c => c.id === chId) || 
             mathChapters.find(c => c.id === chId) || 
             sstChapters.find(c => c.id === chId) || 
             null;
    }
"""
        html = html[:pos + 6] + insert_code + html[pos + 6:]
        print("Inserted scienceChapters and sstChapters.")

# 3. Embed Master Questions arrays
if "const scienceCh1MasterQuestions = " not in html:
    # Find insertion point before generateSampleQuestionsForChapter or before ch3SampleQuestions
    m_pos = html.find("const ch3SampleQuestions = [")
    if m_pos != -1:
        master_qs_code = f"""
    const scienceCh1MasterQuestions = {json.dumps(sci_ch1_data, indent=2, ensure_ascii=False)};
    const scienceCh2MasterQuestions = {json.dumps(sci_ch2_data, indent=2, ensure_ascii=False)};
"""
        html = html[:m_pos] + master_qs_code + html[m_pos:]
        print("Embedded scienceCh1MasterQuestions and scienceCh2MasterQuestions.")

# 4. Make sure questions array has both Ch1 and Ch2
q_start = html.find("let questions = [")
if q_start == -1:
    q_start = html.find("questions = [")
    q_start_len = len("questions = [")
else:
    q_start_len = len("let questions = [")

q_end = html.find("];\n", q_start)
if q_end == -1:
    q_end = html.find("];", q_start)

existing_qs = json.loads(html[q_start + q_start_len - 1 : q_end + 1])
non_sci = [q for q in existing_qs if q.get("subject") != "science"]
all_qs = non_sci + sci_ch1_data + sci_ch2_data

new_qs_json = json.dumps(all_qs, indent=2, ensure_ascii=False)
html = html[:q_start + q_start_len - 1] + new_qs_json + html[q_end + 1:]
print("Seeded questions array with 84 Science questions.")

with open("scratch/redesign_step3.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Step 3 complete. Length:", len(html))
