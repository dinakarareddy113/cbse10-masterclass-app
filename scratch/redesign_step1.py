import json
import re

with open("assets/data/ncert_science_ch1.json", encoding="utf-8") as f:
    sci_ch1_data = json.load(f)

with open("assets/data/ncert_science_ch2.json", encoding="utf-8") as f:
    sci_ch2_data = json.load(f)

with open("assets/data/ncert_math_ch1.json", encoding="utf-8") as f:
    math_ch1_data = json.load(f)

with open("mobile_test/index.html", encoding="utf-8") as f:
    html = f.read()

print("Initial HTML size:", len(html))

# 1. Update State variables around line 70-95
old_state_marker = "let adminTargetChapterId = 'math_ch_02_polynomials';"
new_state_vars = """let adminTargetClass = 'Class 10';
    let adminTargetSubject = 'science'; // Default to Science
    let adminTargetChapterId = 'sci_ch_02_acids_bases_salts'; // Matches 2.NCERT-Class-10-Science_2nd Chapter.pdf
    let adminCatalogTab = 'science'; // 'science', 'math', 'sst'
    let adminDetectedMeta = null;
    let activeScienceChapterFilter = 'All'; // Chapter filter for student Science tab"""

if old_state_marker in html:
    html = html.replace(old_state_marker, new_state_vars)
    print("Replaced adminTargetChapterId state variables successfully.")
else:
    print("Could not find old_state_marker!")

# 2. Add scienceChapters and sstChapters after mathChapters
math_ch_end = html.find("    ];\n\n    let questions = [")
if math_ch_end == -1:
    math_ch_end = html.find("    ];\n    let questions = [")

if math_ch_end != -1:
    ch_insert = """
    // 13 CBSE Class 10 NCERT Science Chapters (Bilingual English + Kannada)
    const scienceChapters = [
      {
        id: 'sci_ch_01_chemical_reactions',
        num: 1,
        titleEn: 'Chemical Reactions and Equations',
        titleKn: 'ರಾಸಾಯನಿಕ ಕ್ರಿಯೆಗಳು ಮತ್ತು ಸಮೀಕರಣಗಳು',
        summary: 'Balancing chemical equations, combination, decomposition, displacement, double displacement, redox reactions, corrosion, and rancidity.',
        questionCount: 47
      },
      {
        id: 'sci_ch_02_acids_bases_salts',
        num: 2,
        titleEn: 'Acids, Bases and Salts',
        titleKn: 'ಆಮ್ಲಗಳು, ಪ್ರತ್ಯಾಮ್ಲಗಳು ಮತ್ತು ಲವಣಗಳು',
        summary: 'Indicators, reactions with metals and carbonates, pH scale, acid dilution principles, and salts preparation (bleaching powder, baking soda, washing soda, POP).',
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
    html = html[:math_ch_end + 6] + ch_insert + html[math_ch_end + 6:]
    print("Inserted scienceChapters and sstChapters successfully.")
else:
    print("Could not find math_ch_end insertion point!")

with open("scratch/redesign_step1.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Step 1 written to scratch/redesign_step1.html")
