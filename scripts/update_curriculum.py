import re

with open('lib/core/constants/cbse_curriculum.dart', 'r', encoding='utf-8') as f:
    content = f.read()

science_and_sst_block = '''
  // ---------------------------------------------------------------------------
  // Science Chapters (CBSE Class 10 NCERT)
  // ---------------------------------------------------------------------------
  static const List<Map<String, dynamic>> scienceChapters = [
    {
      'id': 'sci_ch_01_chemical_reactions_equations',
      'chapter_number': 1,
      'title': 'Chapter 1: Chemical Reactions and Equations',
      'title_en': 'Chemical Reactions and Equations',
      'title_kn': 'ರಾಸಾಯನಿಕ ಕ್ರಿಯೆಗಳು ಮತ್ತು ಸಮೀಕರಣಗಳು',
      'summary': 'Balancing chemical equations, combination, decomposition, displacement, double displacement, redox, and rancidity.',
      'formulas': [
        'Combination: 2Mg(s) + O₂(g) → 2MgO(s)',
        'Thermal Decomposition: CaCO₃(s) → CaO(s) + CO₂(g)',
        'Ferrous Sulphate: 2FeSO₄(s) → Fe₂O₃(s) + SO₂(g) + SO₃(g)',
        'Displacement: Fe(s) + CuSO₄(aq) → FeSO₄(aq) + Cu(s)',
        'Double Displacement: Na₂SO₄(aq) + BaCl₂(aq) → BaSO₄(s)↓ + 2NaCl(aq)',
        'Respiration (Exothermic): C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + Energy'
      ]
    },
    {
      'id': 'sci_ch_02_acids_bases_salts',
      'chapter_number': 2,
      'title': 'Chapter 2: Acids, Bases and Salts',
      'title_en': 'Acids, Bases and Salts',
      'title_kn': 'ಆಮ್ಲಗಳು, ಪ್ರತ್ಯಾಮ್ಲಗಳು ಮತ್ತು ಲವಣಗಳು',
      'summary': 'Indicators, reactions with metals & carbonates, pH scale, dilution principles, salts (bleaching powder, baking soda, washing soda, POP).',
      'formulas': [
        'Acid + Metal: Zn + 2HCl → ZnCl₂ + H₂↑',
        'Acid + Carbonate: Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂↑',
        'Neutralization: NaOH + HCl → NaCl + H₂O',
        'pH Scale: pH = -log₁₀[H⁺]; pH < 7 (Acidic), pH = 7 (Neutral), pH > 7 (Basic)',
        'Bleaching Powder: Ca(OH)₂ + Cl₂ → CaOCl₂ + H₂O',
        'Baking Soda: NaCl + H₂O + CO₂ + NH₃ → NH₄Cl + NaHCO₃',
        'Plaster of Paris: CaSO₄ · ½H₂O + 1½H₂O → CaSO₄ · 2H₂O'
      ]
    },
    {
      'id': 'sci_ch_03_metals_non_metals',
      'chapter_number': 3,
      'title': 'Chapter 3: Metals and Non-metals',
      'title_en': 'Metals and Non-metals',
      'title_kn': 'ಲೋಹಗಳು ಮತ್ತು ಅಲೋಹಗಳು',
      'summary': 'Physical & chemical properties, reactivity series, ionic compounds, extraction of metals, and prevention of corrosion.',
      'formulas': [
        'Reactivity Series: K > Na > Ca > Mg > Al > Zn > Fe > Pb > [H] > Cu > Hg > Ag > Au',
        'Amphoteric Oxides: Al₂O₃ + 6HCl → 2AlCl₃ + 3H₂O',
        'Roasting (Sulphide): 2ZnS + 3O₂ → 2ZnO + 2SO₂↑',
        'Calcination (Carbonate): ZnCO₃ → ZnO + CO₂↑',
        'Thermite Reaction: Fe₂O₃(s) + 2Al(s) → 2Fe(l) + Al₂O₃(s) + Heat',
        'Corrosion Prevention: Galvanization (Zn coating), Alloying'
      ]
    },
    {
      'id': 'sci_ch_04_carbon_compounds',
      'chapter_number': 4,
      'title': 'Chapter 4: Carbon and its Compounds',
      'title_en': 'Carbon and its Compounds',
      'title_kn': 'ಕಾರ್ಬನ್ ಮತ್ತು ಅದರ ಸಂಯುಕ್ತಗಳು',
      'summary': 'Covalent bonding, versatile nature, homologous series, functional groups, chemical properties of carbon, soaps and detergents.',
      'formulas': [
        'Alkanes: CₙH₂ₙ₊₂; Alkenes: CₙH₂ₙ; Alkynes: CₙH₂ₙ₋₂',
        'Combustion: CH₄ + 2O₂ → CO₂ + 2H₂O + Heat & Light',
        'Esterification: CH₃COOH + C₂H₅OH → CH₃COOC₂H₅ + H₂O (Sweet smell)',
        'Saponification: CH₃COOC₂H₅ + NaOH → CH₃COONa + C₂H₅OH'
      ]
    },
    {
      'id': 'sci_ch_05_life_processes',
      'chapter_number': 5,
      'title': 'Chapter 5: Life Processes',
      'title_en': 'Life Processes',
      'title_kn': 'ಜೀವ ಕ್ರಿಯೆಗಳು',
      'summary': 'Nutrition (autotrophic & heterotrophic), respiration (aerobic & anaerobic), transportation in humans/plants, and excretion.',
      'formulas': [
        'Photosynthesis: 6CO₂ + 12H₂O → C₆H₁₂O₆ + 6O₂ + 6H₂O',
        'Aerobic Respiration: Glucose → Pyruvate → 6CO₂ + 6H₂O + 38 ATP',
        'Anaerobic (Yeast): Glucose → Ethanol + CO₂ + 2 ATP',
        'Anaerobic (Muscle): Glucose → Lactic Acid + 2 ATP'
      ]
    },
    {
      'id': 'sci_ch_06_control_coordination',
      'chapter_number': 6,
      'title': 'Chapter 6: Control and Coordination',
      'title_en': 'Control and Coordination',
      'title_kn': 'ನಿಯಂತ್ರಣ ಮತ್ತು ಸಮನ್ವಯ',
      'summary': 'Nervous system, reflex arc, human brain, plant hormones (tropisms), and endocrine glands.',
      'formulas': [
        'Reflex Arc Path: Receptor → Sensory Neuron → Spinal Cord Relay → Motor Neuron → Effector',
        'Plant Hormones: Auxin (elongation), Gibberellin (growth), Cytokinin (division), ABA (wilting)',
        'Human Endocrine: Insulin (Pancreas - regulates glucose), Thyroxine (Thyroid - metabolism)'
      ]
    },
    {
      'id': 'sci_ch_07_reproduction',
      'chapter_number': 7,
      'title': 'Chapter 7: How do Organisms Reproduce?',
      'title_en': 'How do Organisms Reproduce?',
      'title_kn': 'ಜೀವಿಗಳು ಹೇಗೆ ಸಂತಾನೋತ್ಪತ್ತಿ ನಡೆಸುತ್ತವೆ?',
      'summary': 'Asexual reproduction modes, sexual reproduction in flowering plants, human reproductive systems, and reproductive health.',
      'formulas': [
        'Asexual Modes: Binary Fission (Amoeba), Budding (Hydra), Spore Formation (Rhizopus)',
        'Flower Organs: Stamen (Male: Anther + Filament), Carpel (Female: Stigma + Style + Ovary)',
        'Human Karyotype: 22 Autosome pairs + 1 Pair Sex Chromosomes (XX Female, XY Male)'
      ]
    },
    {
      'id': 'sci_ch_08_heredity',
      'chapter_number': 8,
      'title': 'Chapter 8: Heredity',
      'title_en': 'Heredity',
      'title_kn': 'ಅನುವಂಶೀಯತೆ',
      'summary': 'Mendel’s laws of inheritance, monohybrid & dihybrid crosses, and chromosomal sex determination in humans.',
      'formulas': [
        'Monohybrid F2 Phenotypic Ratio = 3 : 1 (Tall : Dwarf)',
        'Monohybrid F2 Genotypic Ratio = 1 : 2 : 1 (TT : Tt : tt)',
        'Dihybrid F2 Phenotypic Ratio = 9 : 3 : 3 : 1',
        'Human Sex Determination: Father produces 50% X and 50% Y sperm'
      ]
    },
    {
      'id': 'sci_ch_09_light',
      'chapter_number': 9,
      'title': 'Chapter 9: Light – Reflection and Refraction',
      'title_en': 'Light – Reflection and Refraction',
      'title_kn': 'ಬೆಳಕು – ಪ್ರತಿಫಲನ ಮತ್ತು ವಕ್ರೀಭವನ',
      'summary': 'Spherical mirrors, ray diagrams, mirror formula, magnification, refraction through glass slab, lens formula, and power of a lens.',
      'formulas': [
        'Spherical Mirror Formula: 1/f = 1/v + 1/u',
        'Mirror Magnification: m = -v / u',
        'Snell\\'s Law: n = sin i / sin r',
        'Spherical Lens Formula: 1/f = 1/v - 1/u',
        'Power of Lens: P = 1 / f (in metres) [Dioptre, D]'
      ]
    },
    {
      'id': 'sci_ch_10_human_eye',
      'chapter_number': 10,
      'title': 'Chapter 10: The Human Eye and Colourful World',
      'title_en': 'The Human Eye and Colourful World',
      'title_kn': 'ಮಾನವನ ಕಣ್ಣು ಮತ್ತು ವರ್ಣರಂಜಿತ ಜಗತ್ತು',
      'summary': 'Eye structure, defects of vision (myopia, hypermetropia, presbyopia), dispersion through prism, atmospheric refraction, and scattering.',
      'formulas': [
        'Near Point: D = 25 cm; Far Point = Infinity',
        'Myopia: Corrected by Concave Lens (f < 0, P < 0)',
        'Hypermetropia: Corrected by Convex Lens (f > 0, P > 0)',
        'Power Combination: P = P₁ + P₂ + P₃'
      ]
    },
    {
      'id': 'sci_ch_11_electricity',
      'chapter_number': 11,
      'title': 'Chapter 11: Electricity',
      'title_en': 'Electricity',
      'title_kn': 'ವಿದ್ಯುಚ್ಛಕ್ತಿ',
      'summary': 'Ohm’s law, resistance factors, series & parallel resistor circuits, Joule’s heating law, and electric power.',
      'formulas': [
        'Current: I = Q / t; Potential Difference: V = W / Q',
        'Ohm\\'s Law: V = I × R; Resistance: R = ρ(l / A)',
        'Series: R_s = R₁ + R₂ + ...; Parallel: 1/R_p = 1/R₁ + 1/R₂ + ...',
        'Joule\\'s Law of Heating: H = I²Rt = VIt = (V²/R)t',
        'Electric Power: P = VI = I²R = V²/R; 1 kWh = 3.6 × 10⁶ J'
      ]
    },
    {
      'id': 'sci_ch_12_magnetic_effects',
      'chapter_number': 12,
      'title': 'Chapter 12: Magnetic Effects of Electric Current',
      'title_en': 'Magnetic Effects of Electric Current',
      'title_kn': 'ವಿದ್ಯುತ್ ಪ್ರವಾಹದ ಕಾಂತೀಯ ಪರಿಣಾಮಗಳು',
      'summary': 'Magnetic field lines, right-hand thumb rule, solenoid, Fleming’s left-hand rule, and domestic electric circuits.',
      'formulas': [
        'Right-Hand Thumb Rule: Thumb = Current, Curled fingers = Field lines',
        'Magnetic Force: F = B I l sin θ (Maximum at 90°)',
        'Fleming\\'s Left-Hand Rule: Thumb = Force, Forefinger = Field, Middle = Current',
        'Domestic Supply: 220 V, 50 Hz AC; Live (Red), Neutral (Black), Earth (Green)'
      ]
    },
    {
      'id': 'sci_ch_13_our_environment',
      'chapter_number': 13,
      'title': 'Chapter 13: Our Environment',
      'title_en': 'Our Environment',
      'title_kn': 'ನಮ್ಮ ಪರಿಸರ',
      'summary': 'Ecosystem components, food chains & food webs, 10% energy law, biological magnification, and ozone layer depletion.',
      'formulas': [
        'Lindeman\\'s 10% Energy Law: Only 10% energy transferred to next trophic level',
        'Biomagnification: Non-biodegradable chemicals concentrate up food chains',
        'Ozone Formation: O₂ + UV → O + O; O + O₂ → O₃ (Stratospheric shield)'
      ]
    }
  ];

  // ---------------------------------------------------------------------------
  // Social Science Chapters (CBSE Class 10 NCERT)
  // ---------------------------------------------------------------------------
  static const List<Map<String, dynamic>> sstChapters = [
    {
      'id': 'sst_hist_ch_01_europe',
      'chapter_number': 1,
      'subject_sub': 'History',
      'title': 'Chapter 1: The Rise of Nationalism in Europe',
      'title_en': 'The Rise of Nationalism in Europe',
      'title_kn': 'ಯುರೋಪಿನಲ್ಲಿ ರಾಷ್ಟ್ರೀಯತೆಯ ಉದಯ',
      'summary': 'French Revolution, Civil Code of 1804 (Napoleonic Code), Congress of Vienna 1815, Unification of Germany and Italy.',
      'formulas': [
        'Civil Code of 1804 (Napoleonic Code): Equality before law, abolished feudal system.',
        'Treaty of Vienna (1815): Restored conservative monarchies.',
        'German Unification (1871): Led by Otto von Bismarck ("Blood & Iron").',
        'Italian Unification (1861): Mazzini, Cavour, Garibaldi, Victor Emmanuel II.'
      ]
    },
    {
      'id': 'sst_hist_ch_02_nationalism',
      'chapter_number': 2,
      'subject_sub': 'History',
      'title': 'Chapter 2: Nationalism in India',
      'title_en': 'Nationalism in India',
      'title_kn': 'ಭಾರತದಲ್ಲಿ ರಾಷ್ಟ್ರೀಯತೆ',
      'summary': 'Satyagraha movements, Rowlatt Act & Jallianwala Bagh (1919), Non-Cooperation Movement (1920-22), Civil Disobedience Movement (1930), Poona Pact.',
      'formulas': [
        'Rowlatt Act (1919): Detention without trial for 2 years.',
        'Jallianwala Bagh (13 April 1919): General Dyer opened fire at Amritsar.',
        'Non-Cooperation Movement (1920-1922): Boycott of foreign goods and institutions.',
        'Dandi Salt March (12 March - 6 April 1930): 240 miles to break salt law.',
        'Poona Pact (1932): Reserved seats for Depressed Classes.'
      ]
    },
    {
      'id': 'sst_geo_ch_01_resources',
      'chapter_number': 3,
      'subject_sub': 'Geography',
      'title': 'Chapter 3: Resources and Development',
      'title_en': 'Resources and Development',
      'title_kn': 'ಸಂಪನ್ಮೂಲಗಳು ಮತ್ತು ಅಭಿವೃದ್ಧಿ',
      'summary': 'Resource classification, sustainable development, Agenda 21, land degradation, major Indian soil types (Alluvial, Black, Laterite).',
      'formulas': [
        'Sustainable Development: Meets present needs without compromising future.',
        'Rio Earth Summit (1992): Adopted Agenda 21.',
        'Alluvial Soil: Northern plains; Bangar (old) and Khadar (new).',
        'Black Soil (Regur): Deccan basalt lava; ideal for cotton.'
      ]
    },
    {
      'id': 'sst_geo_ch_07_lifelines',
      'chapter_number': 4,
      'subject_sub': 'Geography',
      'title': 'Chapter 4: Lifelines of National Economy',
      'title_en': 'Lifelines of National Economy',
      'title_kn': 'ರಾಷ್ಟ್ರೀಯ ಆರ್ಥಿಕತೆಯ ಜೀವನಾಡಿಗಳು',
      'summary': 'Transportation networks (Roadways, Railways, Pipelines, Waterways, Airways), communication, international trade.',
      'formulas': [
        'Golden Quadrilateral: 6-lane super highway connecting Delhi-Mumbai-Chennai-Kolkata.',
        'NW-1: Ganga river stretch between Allahabad and Haldia (1620 km).',
        'Kandla (Deendayal) Port: Major tidal port in Gulf of Kachchh.'
      ]
    },
    {
      'id': 'sst_civ_ch_01_power_sharing',
      'chapter_number': 5,
      'subject_sub': 'Civics',
      'title': 'Chapter 5: Power Sharing',
      'title_en': 'Power Sharing',
      'title_kn': 'ಅಧಿಕಾರ ಹಂಚಿಕೆ',
      'summary': 'Ethnic accommodation in Belgium vs Majoritarianism in Sri Lanka; horizontal, vertical, and coalition power-sharing structures.',
      'formulas': [
        'Belgium Model: Equal Dutch & French representation; Community Government.',
        'Horizontal Power Sharing: Legislature, Executive, Judiciary (Checks & Balances).',
        'Vertical Power Sharing: Union, State, and Local Panchayati Raj.'
      ]
    },
    {
      'id': 'sst_civ_ch_02_federalism',
      'chapter_number': 6,
      'subject_sub': 'Civics',
      'title': 'Chapter 6: Federalism',
      'title_en': 'Federalism',
      'title_kn': 'ಸಂಯುಕ್ತ ವ್ಯವಸ್ಥೆ',
      'summary': 'Features of federalism, Union/State/Concurrent legislative lists, linguistic reorganization, 1992 Panchayati Raj amendments.',
      'formulas': [
        'Union List (Defense, Foreign Affairs): Exclusive Union Parliament power.',
        'State List (Police, Agriculture): State Legislatures power.',
        'Concurrent List (Education, Forests): Both legislate (Union prevails on conflict).',
        '73rd & 74th Amendments (1992): Panchayati Raj & Municipalities.'
      ]
    },
    {
      'id': 'sst_econ_ch_01_development',
      'chapter_number': 7,
      'subject_sub': 'Economics',
      'title': 'Chapter 7: Development',
      'title_en': 'Development',
      'title_kn': 'ಅಭಿವೃದ್ಧಿ',
      'summary': 'Development aspirations, national income, per capita income, World Bank vs UNDP Human Development Index (HDI), sustainability.',
      'formulas': [
        'Per Capita Income: Total National Income / Total Population.',
        'UNDP HDI: Combines PCI, Life Expectancy at Birth, and Mean Schooling Years.',
        'BMI = Weight (kg) / [Height (m)]².'
      ]
    }
  ];
'''

# Insert before '  // ---------------------------------------------------------------------------\n  // Science Modules'
target = "  // ---------------------------------------------------------------------------\n  // Science Modules (Physics, Chemistry, Biology)"
if target in content:
    updated = content.replace(target, science_and_sst_block + "\n" + target)
    with open('lib/core/constants/cbse_curriculum.dart', 'w', encoding='utf-8') as f:
        f.write(updated)
    print("Successfully updated lib/core/constants/cbse_curriculum.dart with scienceChapters and sstChapters")
else:
    print("Target comment not found in cbse_curriculum.dart")
