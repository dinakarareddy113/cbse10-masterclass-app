/// CBSE Class 10 Curriculum Catalog & Rich Study Content Data
class CbseCurriculum {
  // ---------------------------------------------------------------------------
  // Subject Definitions
  // ---------------------------------------------------------------------------
  static const Map<String, String> subjects = {
    'math': 'Mathematics',
    'science': 'Science',
    'social_science': 'Social Science',
  };

  // ---------------------------------------------------------------------------
  // Mathematics Chapters (CBSE Class 10 NCERT)
  // ---------------------------------------------------------------------------
  static const List<Map<String, dynamic>> mathChapters = [
    {
      'id': 'math_ch_01_real_numbers',
      'chapter_number': 1,
      'title': 'Chapter 1: Real Numbers',
      'title_en': 'Real Numbers',
      'title_kn': 'ವಾಸ್ತವ ಸಂಖ್ಯೆಗಳು',
      'summary': 'Fundamental Theorem of Arithmetic, irrationality proofs, prime factorization, and HCF-LCM relationships.',
      'formulas': [
        'HCF(a, b) × LCM(a, b) = a × b',
        'Fundamental Theorem: Every composite number can be uniquely expressed as a product of primes.',
        'Proof by contradiction: Assume √p is rational = a/b where gcd(a,b)=1.',
        'Decimal expansions: x = p/q terminates iff q = 2ⁿ · 5ᵐ (n, m ≥ 0).'
      ]
    },
    {
      'id': 'math_ch_02_polynomials',
      'chapter_number': 2,
      'title': 'Chapter 2: Polynomials',
      'title_en': 'Polynomials',
      'title_kn': 'ಬಹುಪದೋಕ್ತಿಗಳು',
      'summary': 'Relationship between zeroes and coefficients of quadratic polynomials.',
      'formulas': [
        'Quadratic: p(x) = ax² + bx + c (a ≠ 0)',
        'Sum of zeroes: α + β = -b / a',
        'Product of zeroes: α · β = c / a',
        'Forming polynomial: k[x² - (α + β)x + αβ]'
      ]
    },
    {
      'id': 'math_ch_03_linear_equations',
      'chapter_number': 3,
      'title': 'Chapter 3: Pair of Linear Equations in Two Variables',
      'title_en': 'Pair of Linear Equations in Two Variables',
      'title_kn': 'ಎರಡು ಚರಾಕ್ಷರಗಳಿರುವ ರೇಖಾತ್ಮಕ ಸಮೀಕರಣಗಳ ಜೋಡಿಗಳು',
      'summary': 'Graphical and algebraic methods: substitution, elimination, and consistency condition ratios.',
      'formulas': [
        'Intersecting (Unique solution): a₁/a₂ ≠ b₁/b₂ (Consistent)',
        'Coincident (Infinitely many solutions): a₁/a₂ = b₁/b₂ = c₁/c₂ (Consistent & Dependent)',
        'Parallel (No solution): a₁/a₂ = b₁/b₂ ≠ c₁/c₂ (Inconsistent)'
      ]
    },
    {
      'id': 'math_ch_04_quadratic_equations',
      'chapter_number': 4,
      'title': 'Chapter 4: Quadratic Equations',
      'title_en': 'Quadratic Equations',
      'title_kn': 'ವರ್ಗ ಸಮೀಕರಣಗಳು',
      'summary': 'Standard form, factorization, quadratic formula, nature of roots.',
      'formulas': [
        'Standard Form: ax² + bx + c = 0 (a ≠ 0)',
        'Discriminant: D = b² - 4ac',
        'Quadratic Formula: x = (-b ± √D) / (2a)',
        'Nature of Roots: D > 0 (two distinct real roots), D = 0 (two equal real roots: -b/2a), D < 0 (no real roots)'
      ]
    },
    {
      'id': 'math_ch_05_arithmetic_progressions',
      'chapter_number': 5,
      'title': 'Chapter 5: Arithmetic Progressions',
      'title_en': 'Arithmetic Progressions',
      'title_kn': 'ಸಮಾಂತರ ಶ್ರೇಢಿಗಳು',
      'summary': 'nth term of an AP, sum of first n terms, real-world application problems.',
      'formulas': [
        'nth term: a_n = a + (n - 1)d',
        'Common difference: d = a_(k+1) - a_k',
        'Sum of n terms: S_n = (n / 2) [2a + (n - 1)d]',
        'Alternative Sum: S_n = (n / 2) [a + l], where l is the last term',
        'nth term from sum: a_n = S_n - S_(n-1)'
      ]
    },
    {
      'id': 'math_ch_06_triangles',
      'chapter_number': 6,
      'title': 'Chapter 6: Triangles',
      'title_en': 'Triangles',
      'title_kn': 'ತ್ರಿಭುಜಗಳು',
      'summary': 'Basic Proportionality Theorem (Thales), similarity criteria (AAA, SSS, SAS).',
      'formulas': [
        'BPT (Thales Theorem): If a line is drawn parallel to one side of a triangle intersecting other two sides: AD/DB = AE/EC',
        'Converse of BPT: If a line divides any two sides proportionally, it is parallel to the third side.',
        'Similarity Criteria: AAA, SSS, SAS rules'
      ]
    },
    {
      'id': 'math_ch_07_coordinate_geometry',
      'chapter_number': 7,
      'title': 'Chapter 7: Coordinate Geometry',
      'title_en': 'Coordinate Geometry',
      'title_kn': 'ನಿರ್ದೇಶಾಂಕ ರೇಖಾಗಣಿತ',
      'summary': 'Distance formula, Section formula, midpoint coordinates.',
      'formulas': [
        'Distance Formula: d = √[(x₂ - x₁)² + (y₂ - y₁)²]',
        'Distance from Origin: d = √(x² + y²)',
        'Section Formula: ((m₁x₂ + m₂x₁) / (m₁ + m₂), (m₁y₂ + m₂y₁) / (m₁ + m₂))',
        'Midpoint: ((x₁ + x₂) / 2, (y₁ + y₂) / 2)'
      ]
    },
    {
      'id': 'math_ch_08_intro_trigonometry',
      'chapter_number': 8,
      'title': 'Chapter 8: Introduction to Trigonometry',
      'title_en': 'Introduction to Trigonometry',
      'title_kn': 'ತ್ರಿಕೋನಮಿತಿಯ ಪ್ರಸ್ತಾವನೆ',
      'summary': 'Trigonometric ratios, values of standard angles (0°, 30°, 45°, 60°, 90°), trigonometric identities.',
      'formulas': [
        'sin θ = P / H, cos θ = B / H, tan θ = P / B',
        'sin² θ + cos² θ = 1',
        '1 + tan² θ = sec² θ',
        '1 + cot² θ = cosec² θ',
        'Standard values: sin 30° = 1/2, sin 45° = 1/√2, sin 60° = √3/2, cos 60° = 1/2, tan 45° = 1'
      ]
    },
    {
      'id': 'math_ch_09_applications_trigonometry',
      'chapter_number': 9,
      'title': 'Chapter 9: Some Applications of Trigonometry',
      'title_en': 'Some Applications of Trigonometry',
      'title_kn': 'ತ್ರಿಕೋನಮಿತಿಯ ಕೆಲವು ಅನ್ವಯಗಳು',
      'summary': 'Heights and distances, angles of elevation and depression, line of sight.',
      'formulas': [
        'Angle of Elevation: Angle made by line of sight with horizontal looking upwards.',
        'Angle of Depression: Angle made by line of sight with horizontal looking downwards.',
        'Height = Distance × tan θ (in right-angled triangle where adjacent base is known)'
      ]
    },
    {
      'id': 'math_ch_10_circles',
      'chapter_number': 10,
      'title': 'Chapter 10: Circles',
      'title_en': 'Circles',
      'title_kn': 'ವೃತ್ತಗಳು',
      'summary': 'Tangents to a circle, properties and theorem of tangent length from external point.',
      'formulas': [
        'Theorem 1: Radius is perpendicular to tangent at point of contact (OP ⊥ AB).',
        'Theorem 2: Lengths of tangents drawn from an external point to a circle are equal (PQ = PR).',
        'Angle between two tangents from external point is supplementary to angle subtended at the centre.'
      ]
    },
    {
      'id': 'math_ch_11_areas_related_to_circles',
      'chapter_number': 11,
      'title': 'Chapter 11: Areas Related to Circles',
      'title_en': 'Areas Related to Circles',
      'title_kn': 'ವೃತ್ತಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ವಿಸ್ತೀರ್ಣಗಳು',
      'summary': 'Perimeter and area of circle, area of sector and segment of circle.',
      'formulas': [
        'Circumference = 2πr; Area = πr²',
        'Area of Sector = (θ / 360°) × πr²',
        'Length of Arc = (θ / 360°) × 2πr',
        'Area of Segment = Area of Sector - Area of corresponding Triangle'
      ]
    },
    {
      'id': 'math_ch_12_surface_areas_volumes',
      'chapter_number': 12,
      'title': 'Chapter 12: Surface Areas and Volumes',
      'title_en': 'Surface Areas and Volumes',
      'title_kn': 'ಮೇಲ್ಮೈ ವಿಸ್ತೀರ್ಣಗಳು ಮತ್ತು ಘನಫಲಗಳು',
      'summary': 'Surface areas and volumes of combinations of solids (cuboid, cylinder, cone, sphere, hemisphere).',
      'formulas': [
        'Cylinder: CSA = 2πrh, TSA = 2πr(r + h), Volume = πr²h',
        'Cone: Slant height l = √(r² + h²), CSA = πrl, Volume = (1/3)πr²h',
        'Sphere: Surface Area = 4πr², Volume = (4/3)πr³',
        'Hemisphere: CSA = 2πr², TSA = 3πr², Volume = (2/3)πr³'
      ]
    },
    {
      'id': 'math_ch_13_statistics',
      'chapter_number': 13,
      'title': 'Chapter 13: Statistics',
      'title_en': 'Statistics',
      'title_kn': 'ಸಂಖ್ಯಾಶಾಸ್ತ್ರ',
      'summary': 'Mean (Direct, Assumed Mean, Step Deviation), Median, Mode of grouped data, Empirical relation.',
      'formulas': [
        'Direct Mean: x̄ = Σ(fᵢxᵢ) / Σfᵢ',
        'Assumed Mean: x̄ = a + [Σ(fᵢdᵢ) / Σfᵢ], where dᵢ = xᵢ - a',
        'Mode = l + [(f₁ - f₀) / (2f₁ - f₀ - f₂)] × h',
        'Median = l + [((n/2) - cf) / f] × h',
        'Empirical Formula: 3 Median = Mode + 2 Mean'
      ]
    },
    {
      'id': 'math_ch_14_probability',
      'chapter_number': 14,
      'title': 'Chapter 14: Probability',
      'title_en': 'Probability',
      'title_kn': 'ಸಂಭವನೀಯತೆ',
      'summary': 'Classical definition of probability, elementary and complementary events, sure and impossible events.',
      'formulas': [
        'P(E) = (Number of outcomes favourable to E) / (Total number of possible outcomes)',
        'Range: 0 ≤ P(E) ≤ 1',
        'Complementary: P(E) + P(not E) = 1',
        'Impossible Event: P = 0; Sure Event: P = 1'
      ]
    }
  ];


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
        'Snell\'s Law: n = sin i / sin r',
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
        'Ohm\'s Law: V = I × R; Resistance: R = ρ(l / A)',
        'Series: R_s = R₁ + R₂ + ...; Parallel: 1/R_p = 1/R₁ + 1/R₂ + ...',
        'Joule\'s Law of Heating: H = I²Rt = VIt = (V²/R)t',
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
        'Fleming\'s Left-Hand Rule: Thumb = Force, Forefinger = Field, Middle = Current',
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
        'Lindeman\'s 10% Energy Law: Only 10% energy transferred to next trophic level',
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

  // ---------------------------------------------------------------------------
  // Science Modules (Physics, Chemistry, Biology)
  // ---------------------------------------------------------------------------
  static const List<Map<String, dynamic>> sciencePhysicsRayDiagrams = [
    {
      'title': 'Concave Mirror: Object between Focus (F) and Pole (P)',
      'position_object': 'Between Focus and Pole',
      'position_image': 'Behind the mirror',
      'nature_image': 'Virtual, Erect, and Magnified',
      'magnification': 'm > +1',
      'application': 'Used by dentists, shaving mirror, torch reflector.',
      'ascii_ray': '''
             Concave Mirror Surface
                 )  |
      Object [A] )  |  Virtual Image [A']
        |        )  |     |
      --+---+----+--+-----+-------- Principal Axis
        F   P   C
      '''
    },
    {
      'title': 'Concave Mirror: Object at Center of Curvature (C)',
      'position_object': 'At C',
      'position_image': 'At C',
      'nature_image': 'Real, Inverted, and Same Size',
      'magnification': 'm = -1',
      'application': 'Laser collimators, headlight reflections.',
      'ascii_ray': '''
      Object at C (2f) ----> Ray parallel reflects through F
      Ray through F ------> Reflects parallel to axis
      Image forms inverted at C of identical height.
      '''
    },
    {
      'title': 'Convex Lens: Object at 2F₁',
      'position_object': 'At 2F₁',
      'position_image': 'At 2F₂',
      'nature_image': 'Real, Inverted, and Same Size',
      'magnification': 'm = -1',
      'application': 'Photocopier lens, terrestrial telescopes.',
      'ascii_ray': '''
      Lens Center O: Ray 1 parallel to axis -> passes through F₂
      Ray 2 passes through Optical Center O undeflected.
      Intersect at 2F₂.
      '''
    }
  ];

  static const List<Map<String, dynamic>> scienceChemistryEquations = [
    {
      'reaction_type': 'Combination & Exothermic',
      'equation': 'CaO(s) + H₂O(l) → Ca(OH)₂(aq) + Heat',
      'reactants': 'Quicklime (Calcium oxide) + Water',
      'products': 'Slaked lime (Calcium hydroxide)',
      'observation': 'Vigorous bubbling, beaker heats up significantly. Solution is used for whitewashing walls.'
    },
    {
      'reaction_type': 'Thermal Decomposition',
      'equation': '2FeSO₄(s) --[Heat]--> Fe₂O₃(s) + SO₂(g) + SO₃(g)',
      'reactants': 'Ferrous sulphate heptahydrate (Green crystals)',
      'products': 'Ferric oxide (Reddish brown) + Sulphur dioxide + Sulphur trioxide',
      'observation': 'Green color changes to reddish-brown; characteristic suffocating odor of burning sulphur emitted.'
    },
    {
      'reaction_type': 'Displacement Reaction',
      'equation': 'Fe(s) + CuSO₄(aq) → FeSO₄(aq) + Cu(s)',
      'reactants': 'Iron nail (Grey) + Copper sulphate (Blue solution)',
      'products': 'Ferrous sulphate (Pale green) + Copper deposit (Reddish-brown)',
      'observation': 'Blue color fades to light green; brown coating of copper deposits on iron nail.'
    },
    {
      'reaction_type': 'Neutralization & Precipitate',
      'equation': 'Na₂SO₄(aq) + BaCl₂(aq) → BaSO₄(s)↓ + 2NaCl(aq)',
      'reactants': 'Sodium sulphate + Barium chloride',
      'products': 'Barium sulphate (White precipitate) + Sodium chloride',
      'observation': 'Immediate formation of insoluble white precipitate of BaSO₄.'
    },
    {
      'reaction_type': 'Saponification (Carbon)',
      'equation': 'CH₃COOC₂H₅ + NaOH → CH₃COONa + C₂H₅OH',
      'reactants': 'Ethyl ethanoate (Ester) + Sodium hydroxide',
      'products': 'Sodium ethanoate + Ethanol',
      'observation': 'Sweet smell of ester replaced; base of commercial soap preparation.'
    }
  ];

  static const List<Map<String, dynamic>> scienceBiologyFlowcharts = [
    {
      'topic': 'Human Double Circulation',
      'summary': 'Blood passes through the heart twice during each complete cycle.',
      'steps': [
        '1. Deoxygenated blood from body tissues collects in Right Atrium via Vena Cava.',
        '2. Pushed into Right Ventricle -> pumped via Pulmonary Artery to Lungs for oxygenation.',
        '3. Oxygenated blood from Lungs enters Left Atrium via Pulmonary Veins.',
        '4. Left Ventricle pumps oxygenated blood under high pressure via Aorta to entire body.'
      ]
    },
    {
      'topic': 'Nephron Filtration & Urine Formation',
      'summary': 'Functional excretory unit of kidney.',
      'steps': [
        '1. Glomerular Ultrafiltration: Blood under high pressure filtered into Bowman’s capsule.',
        '2. Selective Tubular Reabsorption: Glucose, amino acids, Na+, and 99% water reabsorbed in PCT and Henle’s loop.',
        '3. Tubular Secretion: Extra ions and creatinine secreted into filtrate.',
        '4. Collection: Concentrated urine enters Collecting Duct -> Ureter -> Urinary Bladder.'
      ]
    },
    {
      'topic': 'Aerobic vs Anaerobic Breakdown of Glucose',
      'summary': 'Cellular respiration pathways in cytoplasm and mitochondria.',
      'steps': [
        'Step 1 (Cytoplasm): Glucose (6-C) → Pyruvate (3-C) + Energy',
        'Path A (Yeast / Absence of O₂): Ethanol + CO₂ + Energy (2 ATP)',
        'Path B (Human Muscle / Lack of O₂): Lactic acid + Energy (leads to muscle cramps)',
        'Path C (Mitochondria / Presence of O₂): CO₂ + H₂O + Energy (36-38 ATP)'
      ]
    }
  ];

  // ---------------------------------------------------------------------------
  // Social Science Modules (History Timelines, Map Guides, Civics Amendments)
  // ---------------------------------------------------------------------------
  static const List<Map<String, dynamic>> sstHistoryTimelines = [
    {
      'year': '1915',
      'title': 'Return of Mahatma Gandhi',
      'description': 'Mahatma Gandhi returned to India from South Africa, introducing the novel method of mass agitation: Satyagraha.'
    },
    {
      'year': '1917',
      'title': 'Champaran Satyagraha (Bihar)',
      'description': 'Gandhi led peasants against the oppressive plantation system forcing indigo cultivation (Teen-Kathia system).'
    },
    {
      'year': '1918',
      'title': 'Kheda & Ahmedabad Mill Strike (Gujarat)',
      'description': 'Kheda: Revenue remission due to crop failure and plague epidemic. Ahmedabad: 35% wage hike for cotton mill workers.'
    },
    {
      'year': '1919 (April)',
      'title': 'Rowlatt Act & Jallianwala Bagh Massacre',
      'description': 'Rowlatt Act allowed detention without trial. On April 13, General Dyer opened fire on peaceful gathering at Amritsar.'
    },
    {
      'year': '1920-1922',
      'title': 'Non-Cooperation Khilafat Movement',
      'description': 'Boycott of foreign cloth, courts, and schools. Abruptly withdrawn in Feb 1922 after the Chauri Chaura incident.'
    },
    {
      'year': '1928',
      'title': 'Simon Commission Arrival',
      'description': 'All-British commission boycotted with "Go Back Simon" banners across India. Lala Lajpat Rai assaulted.'
    },
    {
      'year': '1929 (Dec)',
      'title': 'Lahore Congress & Purna Swaraj',
      'description': 'Under Jawaharlal Nehru’s presidency, the declaration of complete independence (Purna Swaraj) was formalized.'
    },
    {
      'year': '1930 (March)',
      'title': 'Salt March & Civil Disobedience Movement',
      'description': 'Dandi March: 240 miles from Sabarmati to Dandi. Gandhi broke the salt law on 6 April 1930.'
    },
    {
      'year': '1932',
      'title': 'Poona Pact',
      'description': 'Signed between Dr. B.R. Ambedkar and Mahatma Gandhi, reserving seats for Depressed Classes within general electorates.'
    }
  ];

  static const List<Map<String, dynamic>> sstMapStudyGuide = [
    {
      'category': 'Major Sea Ports (Lifelines of Economy)',
      'items': [
        {'name': 'Kandla (Deendayal)', 'state': 'Gujarat', 'significance': 'Tidal port developed to reduce pressure on Mumbai.'},
        {'name': 'Mumbai', 'state': 'Maharashtra', 'significance': 'Biggest port with spacious natural harbor.'},
        {'name': 'Marmagao', 'state': 'Goa', 'significance': 'Premier iron-ore exporting port (accounts for ~50% export).'},
        {'name': 'New Mangalore', 'state': 'Karnataka', 'significance': 'Exports Kudremukh iron-ore concentrates.'},
        {'name': 'Kochi', 'state': 'Kerala', 'significance': 'Extreme south-western port located at lagoon entrance.'},
        {'name': 'Tuticorin', 'state': 'Tamil Nadu', 'significance': 'Natural harbor on south-east coast trading with Sri Lanka.'},
        {'name': 'Chennai', 'state': 'Tamil Nadu', 'significance': 'One of the oldest artificial ports in India.'},
        {'name': 'Visakhapatnam', 'state': 'Andhra Pradesh', 'significance': 'Deepest landlocked and protected port.'},
        {'name': 'Paradip', 'state': 'Odisha', 'significance': 'Specializes in export of iron ore from Odisha-Jharkhand belt.'},
        {'name': 'Haldia', 'state': 'West Bengal', 'significance': 'Subsidiary port built to relieve pressure on Kolkata.'}
      ]
    },
    {
      'category': 'Major Dams (Water Resources)',
      'items': [
        {'name': 'Salal Dam', 'river': 'Chenab', 'state': 'Jammu & Kashmir'},
        {'name': 'Bhakra Nangal Dam', 'river': 'Satluj', 'state': 'Himachal / Punjab'},
        {'name': 'Tehri Dam', 'river': 'Bhagirathi', 'state': 'Uttarakhand (highest dam in India)'},
        {'name': 'Rana Pratap Sagar', 'river': 'Chambal', 'state': 'Rajasthan'},
        {'name': 'Sardar Sarovar Dam', 'river': 'Narmada', 'state': 'Gujarat'},
        {'name': 'Hirakud Dam', 'river': 'Mahanadi', 'state': 'Odisha (longest earthen dam)'},
        {'name': 'Nagarjuna Sagar', 'river': 'Krishna', 'state': 'Andhra Pradesh / Telangana'},
        {'name': 'Tungabhadra Dam', 'river': 'Tungabhadra', 'state': 'Karnataka'}
      ]
    }
  ];

  static const List<Map<String, dynamic>> sstCivicsAmendments = [
    {
      'title': '73rd Constitutional Amendment Act (1992)',
      'focus': 'Panchayati Raj (Rural Local Government)',
      'key_points': [
        'Mandatory regular elections to local government bodies every 5 years.',
        'At least one-third (33%) of all positions reserved for women.',
        'Reservation of seats for Scheduled Castes (SC) and Scheduled Tribes (ST).',
        'Establishment of an independent State Election Commission in each state.',
        'State governments required to share revenue and specified powers with local bodies.'
      ]
    },
    {
      'title': '74th Constitutional Amendment Act (1992)',
      'focus': 'Municipalities (Urban Local Government)',
      'key_points': [
        'Empowered Nagar Panchayats, Municipal Councils, and Municipal Corporations.',
        'Direct representation and democratic urban development planning.'
      ]
    },
    {
      'title': 'Federal Power Sharing (Three-Fold Distribution)',
      'focus': 'Constitutional Lists (7th Schedule)',
      'key_points': [
        'Union List (97+ subjects): Defense, Foreign Affairs, Banking, Currency. Only Parliament legislates.',
        'State List (66 subjects): Police, Trade, Commerce, Agriculture, Irrigation. State Legislature decides.',
        'Concurrent List (47 subjects): Education, Forests, Trade Unions, Marriage. Both can legislate (Union prevails on conflict).',
        'Residuary Subjects: E.g., Computer software, AI, Cyber law. Parliament possesses exclusive power.'
      ]
    }
  ];
}
