
    let role = 'student';
    let currentTab = 'home';
    let offline = false;
    let selectedChapterId = null;
    let activeHubMode = null;
    let activeExerciseFilter = 'All'; // 'practice' or 'formula'
    let adminHubTab = 'pdf'; // 'pdf', 'pipeline', or 'queue'
    let uploadedPdfFile = null; // Clean dropzone by default
    let pdfGenerating = false;
    let pdfGenerationProgress = 0;
    let pdfGenerationStatusText = '';
    let pdfGeneratedQuestions = [];
    let adminTargetChapterId = 'math_ch_02_polynomials';
    let solvedQuestions = new Set(['m1']);
    let userSelectedOptions = {}; // Tracks student choice: { [qId]: optionId }
    let savedProfileJson = localStorage.getItem('cbse_student_profile');
    let studentProfile = savedProfileJson ? JSON.parse(savedProfileJson) : null;
    let selectedClassLevel = studentProfile ? (studentProfile.classLevel || 'Class 10') : 'Class 10';

    // 14 CBSE Class 10 NCERT Mathematics Chapters (Bilingual English + Kannada)
    const mathChapters = [
      {
        id: 'math_ch_01_real_numbers',
        num: 1,
        titleEn: 'Real Numbers',
        titleKn: 'ವಾಸ್ತವ ಸಂಖ್ಯೆಗಳು',
        summary: 'Fundamental Theorem of Arithmetic, irrationality proofs, prime factorization, and HCF-LCM relationships.',
        formulas: [
          'HCF(a, b) × LCM(a, b) = a × b',
          'Fundamental Theorem: Every composite number can be uniquely factored into primes.',
          'Proof by contradiction: Assume √p is rational = a/b where gcd(a,b)=1.',
          'Terminating decimals: Denominator prime factors must be of form 2ⁿ · 5ᵐ.'
        ]
      },
      {
        id: 'math_ch_02_polynomials',
        num: 2,
        titleEn: 'Polynomials',
        titleKn: 'ಬಹುಪದೋಕ್ತಿಗಳು',
        summary: 'Relationship between zeroes and coefficients of quadratic polynomials.',
        formulas: [
          'Quadratic: p(x) = ax² + bx + c (a ≠ 0)',
          'Sum of zeroes: α + β = -b / a',
          'Product of zeroes: α · β = c / a',
          'Forming polynomial: k[x² - (α + β)x + αβ]'
        ]
      },
      {
        id: 'math_ch_03_linear_equations',
        num: 3,
        titleEn: 'Pair of Linear Equations in Two Variables',
        titleKn: 'ಎರಡು ಚರಾಕ್ಷರಗಳಿರುವ ರೇಖಾತ್ಮಕ ಸಮೀಕರಣಗಳ ಜೋಡಿಗಳು',
        summary: 'Graphical and algebraic methods: substitution, elimination, and consistency condition ratios.',
        formulas: [
          'Intersecting lines (Unique solution): a₁/a₂ ≠ b₁/b₂ (Consistent)',
          'Coincident lines (Infinitely many solutions): a₁/a₂ = b₁/b₂ = c₁/c₂ (Dependent)',
          'Parallel lines (No solution): a₁/a₂ = b₁/b₂ ≠ c₁/c₂ (Inconsistent)'
        ]
      },
      {
        id: 'math_ch_04_quadratic_equations',
        num: 4,
        titleEn: 'Quadratic Equations',
        titleKn: 'ವರ್ಗ ಸಮೀಕರಣಗಳು',
        summary: 'Standard form, factorization, quadratic formula, and discriminant nature of roots.',
        formulas: [
          'Standard Form: ax² + bx + c = 0 (a ≠ 0)',
          'Discriminant: D = b² - 4ac',
          'Quadratic Formula: x = (-b ± √D) / (2a)',
          'Roots Nature: D > 0 (two distinct real), D = 0 (two equal real: -b/2a), D < 0 (no real)'
        ]
      },
      {
        id: 'math_ch_05_arithmetic_progressions',
        num: 5,
        titleEn: 'Arithmetic Progressions',
        titleKn: 'ಸಮಾಂತರ ಶ್ರೇಢಿಗಳು',
        summary: 'nth term of an AP, sum of first n terms, and real-world application problems.',
        formulas: [
          'nth term: a_n = a + (n - 1)d',
          'Common difference: d = a_(k+1) - a_k',
          'Sum of n terms: S_n = (n / 2) [2a + (n - 1)d]',
          'Alternative Sum: S_n = (n / 2) [a + l], where l is the last term',
          'nth term from sum: a_n = S_n - S_(n-1)'
        ]
      },
      {
        id: 'math_ch_06_triangles',
        num: 6,
        titleEn: 'Triangles',
        titleKn: 'ತ್ರಿಭುಜಗಳು',
        summary: 'Basic Proportionality Theorem (Thales), criteria for similarity (AAA, SSS, SAS).',
        formulas: [
          'BPT (Thales Theorem): If line parallel to one side intersects other two: AD/DB = AE/EC',
          'Converse of BPT: If a line divides two sides in same ratio, it is parallel to 3rd side.',
          'Similarity Criteria: AAA (or AA), SSS, and SAS similarity rules'
        ]
      },
      {
        id: 'math_ch_07_coordinate_geometry',
        num: 7,
        titleEn: 'Coordinate Geometry',
        titleKn: 'ನಿರ್ದೇಶಾಂಕ ರೇಖಾಗಣಿತ',
        summary: 'Distance formula, Section formula (internal division), and midpoint coordinates.',
        formulas: [
          'Distance Formula: d = √[(x₂ - x₁)² + (y₂ - y₁)²]',
          'Distance from Origin: d = √(x² + y²)',
          'Section Formula: ((m₁x₂ + m₂x₁) / (m₁ + m₂), (m₁y₂ + m₂y₁) / (m₁ + m₂))',
          'Midpoint Formula: ((x₁ + x₂) / 2, (y₁ + y₂) / 2)'
        ]
      },
      {
        id: 'math_ch_08_intro_trigonometry',
        num: 8,
        titleEn: 'Introduction to Trigonometry',
        titleKn: 'ತ್ರಿಕೋನಮಿತಿಯ ಪ್ರಸ್ತಾವನೆ',
        summary: 'Trigonometric ratios, values of standard angles (0°, 30°, 45°, 60°, 90°), and Pythagorean identities.',
        formulas: [
          'sin θ = P / H, cos θ = B / H, tan θ = P / B',
          'sin² θ + cos² θ = 1',
          '1 + tan² θ = sec² θ',
          '1 + cot² θ = cosec² θ',
          'Standard: sin 30° = 1/2, sin 45° = 1/√2, sin 60° = √3/2, cos 60° = 1/2, tan 45° = 1'
        ]
      },
      {
        id: 'math_ch_09_applications_trigonometry',
        num: 9,
        titleEn: 'Some Applications of Trigonometry',
        titleKn: 'ತ್ರಿಕೋನಮಿತಿಯ ಕೆಲವು ಅನ್ವಯಗಳು',
        summary: 'Heights and distances, angles of elevation and depression, line of sight.',
        formulas: [
          'Angle of Elevation: Angle above horizontal observed upwards.',
          'Angle of Depression: Angle below horizontal observed downwards.',
          'Height = Distance × tan θ (when base is known)'
        ]
      },
      {
        id: 'math_ch_10_circles',
        num: 10,
        titleEn: 'Circles',
        titleKn: 'ವೃತ್ತಗಳು',
        summary: 'Tangents to circle, properties, and theorem of equal tangent lengths from external point.',
        formulas: [
          'Theorem 1: Radius is perpendicular to tangent at point of contact (OP ⊥ AB).',
          'Theorem 2: Tangent lengths drawn from an external point to a circle are equal (PQ = PR).',
          'Angle between tangents is supplementary to angle subtended at circle center.'
        ]
      },
      {
        id: 'math_ch_11_areas_related_to_circles',
        num: 11,
        titleEn: 'Areas Related to Circles',
        titleKn: 'ವೃತ್ತಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ವಿಸ್ತೀರ್ಣಗಳು',
        summary: 'Perimeter and area of circle, area of sector and segment of circle.',
        formulas: [
          'Circumference = 2πr; Area = πr²',
          'Area of Sector = (θ / 360°) × πr²',
          'Length of Arc = (θ / 360°) × 2πr',
          'Area of Segment = Area of Sector - Area of corresponding Triangle'
        ]
      },
      {
        id: 'math_ch_12_surface_areas_volumes',
        num: 12,
        titleEn: 'Surface Areas and Volumes',
        titleKn: 'ಮೇಲ್ಮೈ ವಿಸ್ತೀರ್ಣಗಳು ಮತ್ತು ಘನಫಲಗಳು',
        summary: 'Surface areas and volumes of combinations of solids (cuboid, cylinder, cone, sphere, hemisphere).',
        formulas: [
          'Cylinder: CSA = 2πrh, TSA = 2πr(r + h), Volume = πr²h',
          'Cone: Slant height l = √(r² + h²), CSA = πrl, Volume = (1/3)πr²h',
          'Sphere: Surface Area = 4πr², Volume = (4/3)πr³',
          'Hemisphere: CSA = 2πr², TSA = 3πr², Volume = (2/3)πr³'
        ]
      },
      {
        id: 'math_ch_13_statistics',
        num: 13,
        titleEn: 'Statistics',
        titleKn: 'ಸಂಖ್ಯಾಶಾಸ್ತ್ರ',
        summary: 'Mean (Direct, Assumed Mean, Step Deviation), Median, Mode of grouped data, Empirical relation.',
        formulas: [
          'Direct Mean: x̄ = Σ(fᵢxᵢ) / Σfᵢ',
          'Assumed Mean: x̄ = a + [Σ(fᵢdᵢ) / Σfᵢ]',
          'Mode = l + [(f₁ - f₀) / (2f₁ - f₀ - f₂)] × h',
          'Median = l + [((n/2) - cf) / f] × h',
          'Empirical Formula: 3 Median = Mode + 2 Mean'
        ]
      },
      {
        id: 'math_ch_14_probability',
        num: 14,
        titleEn: 'Probability',
        titleKn: 'ಸಂಭವನೀಯತೆ',
        summary: 'Classical definition of probability, elementary and complementary events, sure and impossible events.',
        formulas: [
          'P(E) = (Favourable outcomes) / (Total outcomes)',
          'Range: 0 ≤ P(E) ≤ 1',
          'Complementary: P(E) + P(not E) = 1',
          'Impossible: P = 0; Sure: P = 1'
        ]
      }
    ];

    let questions = [
{
    "id": "10000000-0000-0000-0005-000000000001",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q1(i)] The taxi fare after each km when the fare is ₹ 15 for the first km and ₹ 8 for each additional km. Does this situation make an arithmetic progression?",
    "options": [
      {
        "id": "A",
        "text": "Yes, it forms an AP because each term is obtained by adding a constant ₹ 8 (series: 15, 23, 31, 39, ...)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, taxi fares follow geometric compounding",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, the initial fare is higher than the per-km rate",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Yes, but only for distances less than 10 km",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Fare for 1 km = ₹ 15.\nStep 2: Fare for 2 km = 15 + 8 = ₹ 23; Fare for 3 km = 23 + 8 = ₹ 31; Fare for 4 km = 31 + 8 = ₹ 39.\nStep 3: The series of terms is 15, 23, 31, 39, ... Here, the difference between consecutive terms is constant (d = 8).\nHence, it forms an Arithmetic Progression (AP)."
  },
  {
    "id": "10000000-0000-0000-0005-000000000002",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "1(ii)",
    "difficulty": "medium",
    "text": "[Exercise 5.1 - Q1(ii)] The amount of air present in a cylinder when a vacuum pump removes 1/4 of the air remaining in the cylinder at a time. Does this situation form an arithmetic progression?",
    "options": [
      {
        "id": "A",
        "text": "No, each stroke leaves 3/4 of the remaining volume, so differences are not constant (V, 3/4 V, 9/16 V, ...)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is an AP with common difference d = -1/4",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, because air is continuously removed at equal intervals",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "No, because volume cannot be measured in an arithmetic progression",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let initial volume = V.\nStep 2: After 1st stroke, volume left = V - (1/4)V = (3/4)V.\nStep 3: After 2nd stroke, volume left = (3/4)V - (1/4)(3/4)V = (9/16)V.\nStep 4: Difference a2 - a1 = -1/4 V, but a3 - a2 = -3/16 V != -1/4 V.\nSince successive differences are not constant, it does NOT form an AP."
  },
  {
    "id": "10000000-0000-0000-0005-000000000003",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "1(iii)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q1(iii)] The cost of digging a well after every metre of digging, when it costs ₹ 150 for the first metre and rises by ₹ 50 for each subsequent metre. Does this situation form an arithmetic progression?",
    "options": [
      {
        "id": "A",
        "text": "Yes, it forms an AP with first term a = 150 and common difference d = 50 (150, 200, 250, 300, ...)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, digging costs increase exponentially with depth",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, because the first metre costs more than subsequent metres",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Yes, but with common difference d = 100",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Cost for 1 m = ₹ 150.\nStep 2: Cost for 2 m = 150 + 50 = ₹ 200; for 3 m = 200 + 50 = ₹ 250; for 4 m = ₹ 300.\nStep 3: List of numbers: 150, 200, 250, 300, ...\nStep 4: Common difference d = 200 - 150 = 250 - 200 = 50 (constant).\nHence, it forms an AP."
  },
  {
    "id": "10000000-0000-0000-0005-000000000004",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "1(iv)",
    "difficulty": "medium",
    "text": "[Exercise 5.1 - Q1(iv)] The amount of money in the account every year, when ₹ 10,000 is deposited at compound interest at 8% per annum. Does this situation form an arithmetic progression?",
    "options": [
      {
        "id": "A",
        "text": "No, compound interest increases the principal geometrically each year, so successive differences are not equal",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is an AP with common difference d = 800",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, it is an AP with common ratio r = 1.08",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "No, money can never form an AP",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Year 1 amount = 10000(1 + 8/100) = ₹ 10,800.\nStep 2: Year 2 amount = 10000(1 + 8/100)^2 = ₹ 11,664.\nStep 3: Year 3 amount = 10000(1 + 8/100)^3 = ₹ 12,597.12.\nStep 4: a2 - a1 = 800, while a3 - a2 = 864 != 800.\nSince successive differences are not constant, compound interest does NOT form an AP."
  },
  {
    "id": "10000000-0000-0000-0005-000000000005",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "2(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q2(i)] Write the first four terms of the AP, when the first term a = 10 and the common difference d = 10.",
    "options": [
      {
        "id": "A",
        "text": "10, 20, 30, 40",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "10, 100, 1000, 10000",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "10, 0, -10, -20",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "0, 10, 20, 30",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a1 = a = 10.\nStep 2: a2 = a + d = 10 + 10 = 20.\nStep 3: a3 = a2 + d = 20 + 10 = 30.\nStep 4: a4 = a3 + d = 30 + 10 = 40.\nFirst four terms are 10, 20, 30, 40."
  },
  {
    "id": "10000000-0000-0000-0005-000000000006",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "2(ii)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q2(ii)] Write the first four terms of the AP, when the first term a = -2 and the common difference d = 0.",
    "options": [
      {
        "id": "A",
        "text": "-2, -2, -2, -2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "-2, 0, 2, 4",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "-2, -4, -6, -8",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "0, -2, -4, -6",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a1 = -2.\nStep 2: a2 = -2 + 0 = -2.\nStep 3: a3 = -2 + 0 = -2.\nStep 4: a4 = -2 + 0 = -2.\nWhen d = 0, every term is equal to a. The terms are -2, -2, -2, -2."
  },
  {
    "id": "10000000-0000-0000-0005-000000000007",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "2(iii)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q2(iii)] Write the first four terms of the AP, when the first term a = 4 and the common difference d = -3.",
    "options": [
      {
        "id": "A",
        "text": "4, 1, -2, -5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "4, 7, 10, 13",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "4, -3, -7, -11",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "4, 1, 0, -3",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a1 = 4.\nStep 2: a2 = 4 + (-3) = 1.\nStep 3: a3 = 1 + (-3) = -2.\nStep 4: a4 = -2 + (-3) = -5.\nFirst four terms are 4, 1, -2, -5."
  },
  {
    "id": "10000000-0000-0000-0005-000000000008",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "2(iv)",
    "difficulty": "medium",
    "text": "[Exercise 5.1 - Q2(iv)] Write the first four terms of the AP, when a = -1 and d = 1/2.",
    "options": [
      {
        "id": "A",
        "text": "-1, -1/2, 0, 1/2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "-1, -3/2, -2, -5/2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "-1, 0, 1, 2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "-1, -1/2, -1/4, 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a1 = -1.\nStep 2: a2 = -1 + 1/2 = -1/2.\nStep 3: a3 = -1/2 + 1/2 = 0.\nStep 4: a4 = 0 + 1/2 = 1/2.\nFirst four terms are -1, -1/2, 0, 1/2."
  },
  {
    "id": "10000000-0000-0000-0005-000000000009",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "2(v)",
    "difficulty": "medium",
    "text": "[Exercise 5.1 - Q2(v)] Write the first four terms of the AP, when a = -1.25 and d = -0.25.",
    "options": [
      {
        "id": "A",
        "text": "-1.25, -1.50, -1.75, -2.00",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "-1.25, -1.00, -0.75, -0.50",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "-1.25, -1.50, -1.70, -1.90",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "-1.25, -2.50, -3.75, -5.00",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a1 = -1.25.\nStep 2: a2 = -1.25 + (-0.25) = -1.50.\nStep 3: a3 = -1.50 + (-0.25) = -1.75.\nStep 4: a4 = -1.75 + (-0.25) = -2.00.\nFirst four terms are -1.25, -1.50, -1.75, -2.00."
  },
  {
    "id": "10000000-0000-0000-0005-000000000010",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "3(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q3(i)] For the AP: 3, 1, -1, -3, ... write the first term and the common difference.",
    "options": [
      {
        "id": "A",
        "text": "First term a = 3, Common difference d = -2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "First term a = 3, Common difference d = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "First term a = 1, Common difference d = -2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "First term a = -3, Common difference d = 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: First term is the first number in the sequence: a = 3.\nStep 2: Common difference d = a2 - a1 = 1 - 3 = -2.\nStep 3: Check: a3 - a2 = -1 - 1 = -2. Verified."
  },
  {
    "id": "10000000-0000-0000-0005-000000000011",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "3(ii)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q3(ii)] For the AP: -5, -1, 3, 7, ... write the first term and the common difference.",
    "options": [
      {
        "id": "A",
        "text": "First term a = -5, Common difference d = 4",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "First term a = -5, Common difference d = -4",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "First term a = -1, Common difference d = 4",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "First term a = 7, Common difference d = 2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: First term a = -5.\nStep 2: Common difference d = a2 - a1 = -1 - (-5) = -1 + 5 = 4.\nStep 3: Check: 3 - (-1) = 4, 7 - 3 = 4. Verified."
  },
  {
    "id": "10000000-0000-0000-0005-000000000012",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "3(iii)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q3(iii)] For the AP: 1/3, 5/3, 9/3, 13/3, ... write the first term and the common difference.",
    "options": [
      {
        "id": "A",
        "text": "First term a = 1/3, Common difference d = 4/3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "First term a = 1/3, Common difference d = 5/3",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "First term a = 5/3, Common difference d = 4/3",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "First term a = 1/3, Common difference d = 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: First term a = 1/3.\nStep 2: Common difference d = 5/3 - 1/3 = 4/3.\nStep 3: Check: 9/3 - 5/3 = 4/3. Verified."
  },
  {
    "id": "10000000-0000-0000-0005-000000000013",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "4",
    "difficulty": "medium",
    "text": "[Exercise 5.1 - Q4] Check whether the following sequences form an AP: (i) 2, 4, 8, 16, ... ; (ii) √2, √8, √18, √32, ... If they form an AP, find the common difference d and write three more terms.",
    "options": [
      {
        "id": "A",
        "text": "(i) is NOT an AP (differences 2, 4, 8); (ii) IS an AP with d = √2 (terms are √2, 2√2, 3√2, 4√2), next terms: √50, √72, √98",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Both are APs with common difference d = 2 and d = √2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "(i) is an AP with d = 2; (ii) is not an AP because radicals cannot form AP",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Neither is an AP",
        "is_correct": false
      }
    ],
    "solution": "Step 1: In (i): a2 - a1 = 4 - 2 = 2, but a3 - a2 = 8 - 4 = 4 != 2. Successive differences not equal, hence NOT an AP.\nStep 2: In (ii): √2, √8 = 2√2, √18 = 3√2, √32 = 4√2.\nStep 3: Common difference d = 2√2 - √2 = √2 (constant). Hence IS an AP.\nStep 4: Next three terms are 5√2 = √50, 6√2 = √72, 7√2 = √98."
  },
  {
    "id": "10000000-0000-0000-0005-000000000014",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.2 - Q1(i)] In the AP table, given first term a = 7, common difference d = 3, number of terms n = 8, find the nth term a_n.",
    "options": [
      {
        "id": "A",
        "text": "a_8 = 28",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "a_8 = 24",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "a_8 = 31",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "a_8 = 21",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Formula: an = a + (n - 1)d.\nStep 2: Substitute a = 7, d = 3, n = 8.\nStep 3: a8 = 7 + (8 - 1) × 3 = 7 + 7 × 3 = 7 + 21 = 28."
  },
  {
    "id": "10000000-0000-0000-0005-000000000015",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "1(ii)",
    "difficulty": "easy",
    "text": "[Exercise 5.2 - Q1(ii)] Given first term a = -18, number of terms n = 10, and nth term a_n = 0, find the common difference d.",
    "options": [
      {
        "id": "A",
        "text": "d = 2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "d = -2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "d = 1.8",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "d = 9",
        "is_correct": false
      }
    ],
    "solution": "Step 1: an = a + (n - 1)d.\nStep 2: 0 = -18 + (10 - 1)d => 0 = -18 + 9d.\nStep 3: 9d = 18 => d = 2."
  },
  {
    "id": "10000000-0000-0000-0005-000000000016",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "1(iv)",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q1(iv)] Given first term a = -18.9, common difference d = 2.5, and nth term a_n = 3.6, find the number of terms n.",
    "options": [
      {
        "id": "A",
        "text": "n = 10",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "n = 9",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "n = 11",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "n = 8",
        "is_correct": false
      }
    ],
    "solution": "Step 1: an = a + (n - 1)d.\nStep 2: 3.6 = -18.9 + (n - 1)(2.5).\nStep 3: 3.6 + 18.9 = 22.5 = 2.5(n - 1).\nStep 4: n - 1 = 22.5 / 2.5 = 9 => n = 10."
  },
  {
    "id": "10000000-0000-0000-0005-000000000017",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "2(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.2 - Q2(i)] Choose the correct choice: The 30th term of the AP: 10, 7, 4, ... is:",
    "options": [
      {
        "id": "A",
        "text": "97",
        "is_correct": false
      },
      {
        "id": "B",
        "text": "77",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "-77",
        "is_correct": true
      },
      {
        "id": "D",
        "text": "-87",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 10, d = 7 - 10 = -3, n = 30.\nStep 2: a30 = a + 29d.\nStep 3: a30 = 10 + 29(-3) = 10 - 87 = -77.\nHence, choice C is correct."
  },
  {
    "id": "10000000-0000-0000-0005-000000000018",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q2(ii)] Choose the correct choice: The 11th term of the AP: -3, -1/2, 2, ... is:",
    "options": [
      {
        "id": "A",
        "text": "28",
        "is_correct": false
      },
      {
        "id": "B",
        "text": "22",
        "is_correct": true
      },
      {
        "id": "C",
        "text": "-38",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "-46.5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = -3, d = -1/2 - (-3) = -1/2 + 3 = 5/2.\nStep 2: a11 = a + 10d = -3 + 10(5/2) = -3 + 25 = 22.\nHence, choice B is correct."
  },
  {
    "id": "10000000-0000-0000-0005-000000000019",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "3(i)&(ii)",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q3] In the following APs, find the missing terms in the boxes: (i) 2, [ ], 26; (ii) [ ], 13, [ ], 3.",
    "options": [
      {
        "id": "A",
        "text": "(i) Box = 14; (ii) First box = 18, Third box = 8",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "(i) Box = 12; (ii) First box = 16, Third box = 10",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "(i) Box = 14; (ii) First box = 15, Third box = 9",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "(i) Box = 13; (ii) First box = 17, Third box = 7",
        "is_correct": false
      }
    ],
    "solution": "Step 1: For (i): Middle term of a, b, c in AP is (a + c)/2 = (2 + 26)/2 = 14.\nStep 2: For (ii): a + d = 13 and a + 3d = 3. Subtracting gives 2d = -10 => d = -5.\nStep 3: a = 13 - (-5) = 18, and third term = 13 + (-5) = 8."
  },
  {
    "id": "10000000-0000-0000-0005-000000000020",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "4",
    "difficulty": "easy",
    "text": "[Exercise 5.2 - Q4] Which term of the AP: 3, 8, 13, 18, ... is 78?",
    "options": [
      {
        "id": "A",
        "text": "16th term",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "15th term",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "17th term",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "14th term",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 3, d = 8 - 3 = 5, an = 78.\nStep 2: 78 = 3 + (n - 1)5 => 75 = 5(n - 1).\nStep 3: n - 1 = 15 => n = 16.\nHence, 78 is the 16th term."
  },
  {
    "id": "10000000-0000-0000-0005-000000000021",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "5(i)",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q5(i)] Find the number of terms in the AP: 7, 13, 19, ..., 205.",
    "options": [
      {
        "id": "A",
        "text": "34 terms",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "33 terms",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "35 terms",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "32 terms",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 7, d = 13 - 7 = 6, an = 205.\nStep 2: 205 = 7 + (n - 1)6 => 198 = 6(n - 1).\nStep 3: n - 1 = 33 => n = 34.\nHence, there are 34 terms."
  },
  {
    "id": "10000000-0000-0000-0005-000000000022",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "6",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q6] Check whether -150 is a term of the AP: 11, 8, 5, 2, ...",
    "options": [
      {
        "id": "A",
        "text": "No, because solving for n gives n = 164/3 = 54 2/3, which is not a positive integer",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is the 54th term",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, it is the 55th term",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "No, because terms of an AP cannot be negative",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 11, d = 8 - 11 = -3. Let an = -150.\nStep 2: -150 = 11 + (n - 1)(-3) => -161 = -3(n - 1).\nStep 3: n - 1 = 161/3 => n = 164/3 = 54 2/3.\nSince n must be a positive integer, -150 is NOT a term of this AP."
  },
  {
    "id": "10000000-0000-0000-0005-000000000023",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "7",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q7] Find the 31st term of an AP whose 11th term is 38 and the 16th term is 73.",
    "options": [
      {
        "id": "A",
        "text": "178",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "185",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "171",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "168",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a11 = a + 10d = 38 ... (1) and a16 = a + 15d = 73 ... (2).\nStep 2: Subtracting (1) from (2): 5d = 35 => d = 7.\nStep 3: a + 10(7) = 38 => a = 38 - 70 = -32.\nStep 4: a31 = a + 30d = -32 + 30(7) = -32 + 210 = 178."
  },
  {
    "id": "10000000-0000-0000-0005-000000000024",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "8",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q8] An AP consists of 50 terms of which 3rd term is 12 and the last term is 106. Find the 29th term.",
    "options": [
      {
        "id": "A",
        "text": "64",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "62",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "68",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "56",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Total terms = 50 => a50 = a + 49d = 106.\nStep 2: a3 = a + 2d = 12.\nStep 3: Subtracting gives 47d = 94 => d = 2.\nStep 4: a = 12 - 2(2) = 8.\nStep 5: a29 = a + 28d = 8 + 28(2) = 8 + 56 = 64."
  },
  {
    "id": "10000000-0000-0000-0005-000000000025",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "10",
    "difficulty": "easy",
    "text": "[Exercise 5.2 - Q10] The 17th term of an AP exceeds its 10th term by 7. Find the common difference.",
    "options": [
      {
        "id": "A",
        "text": "d = 1",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "d = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "d = 7",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "d = 0.5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a17 - a10 = 7.\nStep 2: (a + 16d) - (a + 9d) = 7.\nStep 3: 7d = 7 => d = 1."
  },
  {
    "id": "10000000-0000-0000-0005-000000000026",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "13",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q13] How many three-digit numbers are divisible by 7?",
    "options": [
      {
        "id": "A",
        "text": "128",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "127",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "129",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "130",
        "is_correct": false
      }
    ],
    "solution": "Step 1: First 3-digit number divisible by 7 is 105; last is 994.\nStep 2: AP: 105, 112, ..., 994 with a = 105, d = 7, an = 994.\nStep 3: 994 = 105 + (n - 1)7 => 889 = 7(n - 1).\nStep 4: n - 1 = 127 => n = 128."
  },
  {
    "id": "10000000-0000-0000-0005-000000000027",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "17",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q17] Find the 20th term from the last term of the AP: 3, 8, 13, ..., 253.",
    "options": [
      {
        "id": "A",
        "text": "158",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "163",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "153",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "148",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Reverse AP from the end: 253, 248, 243, ..., 3.\nStep 2: First term a = 253, common difference d = -5.\nStep 3: a20 = a + 19d = 253 + 19(-5) = 253 - 95 = 158."
  },
  {
    "id": "10000000-0000-0000-0005-000000000028",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "19",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q19] Subba Rao started work in 1995 at an annual salary of ₹ 5000 and received an increment of ₹ 200 each year. In which year did his income reach ₹ 7000?",
    "options": [
      {
        "id": "A",
        "text": "11th year (Year 2005)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "10th year (Year 2004)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "12th year (Year 2006)",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "9th year (Year 2003)",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Series forms an AP: 5000, 5200, 5400, ..., 7000 with a = 5000, d = 200, an = 7000.\nStep 2: 7000 = 5000 + (n - 1)200 => 2000 = 200(n - 1) => n - 1 = 10 => n = 11.\nStep 3: 11th year from 1995: 1995 + (11 - 1) = 2005."
  },
  {
    "id": "10000000-0000-0000-0005-000000000029",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.3 - Q1(i)] Find the sum of the AP: 2, 7, 12, ... to 10 terms.",
    "options": [
      {
        "id": "A",
        "text": "245",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "250",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "240",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "255",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 2, d = 5, n = 10.\nStep 2: Sn = (n/2)[2a + (n - 1)d].\nStep 3: S10 = (10/2)[2(2) + 9(5)] = 5[4 + 45] = 5(49) = 245."
  },
  {
    "id": "10000000-0000-0000-0005-000000000030",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "1(ii)",
    "difficulty": "easy",
    "text": "[Exercise 5.3 - Q1(ii)] Find the sum of the AP: -37, -33, -29, ... to 12 terms.",
    "options": [
      {
        "id": "A",
        "text": "-180",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "-192",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "-168",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "-200",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = -37, d = 4, n = 12.\nStep 2: S12 = (12/2)[2(-37) + 11(4)] = 6[-74 + 44] = 6(-30) = -180."
  },
  {
    "id": "10000000-0000-0000-0005-000000000031",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "2(i)",
    "difficulty": "medium",
    "text": "[Exercise 5.3 - Q2(i)] Find the sum: 7 + 10 1/2 + 14 + ... + 84.",
    "options": [
      {
        "id": "A",
        "text": "1046 1/2 (1046.5)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "1040",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "1050 1/2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "1036",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 7, d = 7/2, l = an = 84.\nStep 2: 84 = 7 + (n - 1)(7/2) => 77 = (7/2)(n - 1) => n - 1 = 22 => n = 23.\nStep 3: S23 = (n/2)(a + l) = (23/2)(7 + 84) = (23 × 91)/2 = 2093/2 = 1046 1/2."
  },
  {
    "id": "10000000-0000-0000-0005-000000000032",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "4",
    "difficulty": "hard",
    "text": "[Exercise 5.3 - Q4] How many terms of the AP: 9, 17, 25, ... must be taken to give a sum of 636?",
    "options": [
      {
        "id": "A",
        "text": "12 terms",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "14 terms",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "10 terms",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "16 terms",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 9, d = 8, Sn = 636.\nStep 2: 636 = (n/2)[2(9) + (n - 1)8] = n(4n + 5) => 4n² + 5n - 636 = 0.\nStep 3: Factorise: (n - 12)(4n + 53) = 0 => n = 12 (since n > 0).\nHence, 12 terms must be taken."
  },
  {
    "id": "10000000-0000-0000-0005-000000000033",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "7",
    "difficulty": "medium",
    "text": "[Exercise 5.3 - Q7] Find the sum of first 22 terms of an AP in which d = 7 and 22nd term is 149.",
    "options": [
      {
        "id": "A",
        "text": "1661",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "1650",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "1672",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "1640",
        "is_correct": false
      }
    ],
    "solution": "Step 1: n = 22, d = 7, a22 = 149.\nStep 2: a + 21(7) = 149 => a + 147 = 149 => a = 2.\nStep 3: S22 = (22/2)[a + a22] = 11[2 + 149] = 11 × 151 = 1661."
  },
  {
    "id": "10000000-0000-0000-0005-000000000034",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "12",
    "difficulty": "medium",
    "text": "[Exercise 5.3 - Q12] Find the sum of the first 40 positive integers divisible by 6.",
    "options": [
      {
        "id": "A",
        "text": "4920",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "4860",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "4980",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "4800",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Integers divisible by 6 are: 6, 12, 18, ... to 40 terms.\nStep 2: a = 6, d = 6, n = 40.\nStep 3: S40 = (40/2)[2(6) + 39(6)] = 20[12 + 234] = 20 × 246 = 4920."
  },
  {
    "id": "10000000-0000-0000-0005-000000000035",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "14",
    "difficulty": "medium",
    "text": "[Exercise 5.3 - Q14] Find the sum of the odd numbers between 0 and 50.",
    "options": [
      {
        "id": "A",
        "text": "625",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "600",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "650",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "576",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Odd numbers between 0 and 50: 1, 3, 5, ..., 49.\nStep 2: a = 1, d = 2, an = 49 => 49 = 1 + (n - 1)2 => 2(n - 1) = 48 => n = 25.\nStep 3: S25 = (25/2)(1 + 49) = (25 × 50)/2 = 25 × 25 = 625."
  },
  {
    "id": "10000000-0000-0000-0004-000000000001",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(i)] Check whether the following is a quadratic equation:\n(x + 1)\u00b2 = 2(x \u2013 3)",
    "options": [
      {
        "id": "A",
        "text": "Yes, it is a quadratic equation (x\u00b2 + 7 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, it is a linear equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, it is a cubic equation",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "None of the above",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Expand LHS: (x + 1)\u00b2 = x\u00b2 + 2x + 1.\nStep 2: Expand RHS: 2(x \u2013 3) = 2x \u2013 6.\nStep 3: Equating LHS and RHS:\n  x\u00b2 + 2x + 1 = 2x \u2013 6\n  => x\u00b2 + 7 = 0.\nStep 4: Since it is of the form ax\u00b2 + bx + c = 0 with a = 1 \u2260 0, it is a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000002",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(ii)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(ii)] Check whether the following is a quadratic equation:\nx\u00b2 \u2013 2x = (\u20132)(3 \u2013 x)",
    "options": [
      {
        "id": "A",
        "text": "Yes, it is a quadratic equation (x\u00b2 \u2013 4x + 6 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, it is a linear equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, it is an identity",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Yes, with degree 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = x\u00b2 \u2013 2x.\nStep 2: RHS = (\u20132)(3 \u2013 x) = \u20136 + 2x.\nStep 3: Equating:\n  x\u00b2 \u2013 2x = \u20136 + 2x\n  => x\u00b2 \u2013 4x + 6 = 0.\nStep 4: Degree is 2, hence it is a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000003",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(iii)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(iii)] Check whether the following is a quadratic equation:\n(x \u2013 2)(x + 1) = (x \u2013 1)(x + 3)",
    "options": [
      {
        "id": "A",
        "text": "No, it is a linear equation (3x \u2013 1 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is a quadratic equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, with roots 2 and \u20131",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "It is a cubic equation",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = (x \u2013 2)(x + 1) = x\u00b2 \u2013 x \u2013 2.\nStep 2: RHS = (x \u2013 1)(x + 3) = x\u00b2 + 2x \u2013 3.\nStep 3: Equating:\n  x\u00b2 \u2013 x \u2013 2 = x\u00b2 + 2x \u2013 3\n  => 3x \u2013 1 = 0.\nStep 4: The x\u00b2 term cancels out completely. Degree is 1, so it is NOT a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000004",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(iv)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(iv)] Check whether the following is a quadratic equation:\n(x \u2013 3)(2x + 1) = x(x + 5)",
    "options": [
      {
        "id": "A",
        "text": "Yes, it is a quadratic equation (x\u00b2 \u2013 10x \u2013 3 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, it is a linear equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, it has no real terms",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "None of the above",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = (x \u2013 3)(2x + 1) = 2x\u00b2 + x \u2013 6x \u2013 3 = 2x\u00b2 \u2013 5x \u2013 3.\nStep 2: RHS = x(x + 5) = x\u00b2 + 5x.\nStep 3: 2x\u00b2 \u2013 5x \u2013 3 = x\u00b2 + 5x => x\u00b2 \u2013 10x \u2013 3 = 0.\nStep 4: It is of the form ax\u00b2 + bx + c = 0 (a = 1 \u2260 0), so it is a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000005",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(v)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(v)] Check whether the following is a quadratic equation:\n(2x \u2013 1)(x \u2013 3) = (x + 5)(x \u2013 1)",
    "options": [
      {
        "id": "A",
        "text": "Yes, it is a quadratic equation (x\u00b2 \u2013 11x + 8 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, it is linear (11x \u2013 8 = 0)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, it has degree 3",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Cannot be determined",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = 2x\u00b2 \u2013 6x \u2013 x + 3 = 2x\u00b2 \u2013 7x + 3.\nStep 2: RHS = x\u00b2 \u2013 x + 5x \u2013 5 = x\u00b2 + 4x \u2013 5.\nStep 3: 2x\u00b2 \u2013 7x + 3 = x\u00b2 + 4x \u2013 5 => x\u00b2 \u2013 11x + 8 = 0.\nStep 4: Degree is 2. Hence, it is a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000006",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(vi)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(vi)] Check whether the following is a quadratic equation:\nx\u00b2 + 3x + 1 = (x \u2013 2)\u00b2",
    "options": [
      {
        "id": "A",
        "text": "No, it simplifies to a linear equation (7x \u2013 3 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is a quadratic equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, degree is 2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "It has infinite roots",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = x\u00b2 + 3x + 1.\nStep 2: RHS = (x \u2013 2)\u00b2 = x\u00b2 \u2013 4x + 4.\nStep 3: x\u00b2 + 3x + 1 = x\u00b2 \u2013 4x + 4 => 7x \u2013 3 = 0.\nStep 4: Since x\u00b2 cancels out, degree is 1. It is not a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000007",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(vii)",
    "difficulty": "medium",
    "text": "[Exercise 4.1 - Q1(vii)] Check whether the following is a quadratic equation:\n(x + 2)\u00b3 = 2x(x\u00b2 \u2013 1)",
    "options": [
      {
        "id": "A",
        "text": "No, it is a cubic equation (x\u00b3 \u2013 6x\u00b2 \u2013 14x \u2013 8 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is a quadratic equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, degree is 2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "It is linear",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = (x + 2)\u00b3 = x\u00b3 + 6x\u00b2 + 12x + 8.\nStep 2: RHS = 2x(x\u00b2 \u2013 1) = 2x\u00b3 \u2013 2x.\nStep 3: x\u00b3 + 6x\u00b2 + 12x + 8 = 2x\u00b3 \u2013 2x => x\u00b3 \u2013 6x\u00b2 \u2013 14x \u2013 8 = 0.\nStep 4: Highest power is 3. Hence, it is cubic, NOT quadratic."
  },
  {
    "id": "10000000-0000-0000-0004-000000000008",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(viii)",
    "difficulty": "medium",
    "text": "[Exercise 4.1 - Q1(viii)] Check whether the following is a quadratic equation:\nx\u00b3 \u2013 4x\u00b2 \u2013 x + 1 = (x \u2013 2)\u00b3",
    "options": [
      {
        "id": "A",
        "text": "Yes, it is a quadratic equation (2x\u00b2 \u2013 13x + 9 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, it is a cubic equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, it is linear",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "None of the above",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = x\u00b3 \u2013 4x\u00b2 \u2013 x + 1.\nStep 2: RHS = (x \u2013 2)\u00b3 = x\u00b3 \u2013 6x\u00b2 + 12x \u2013 8.\nStep 3: x\u00b3 \u2013 4x\u00b2 \u2013 x + 1 = x\u00b3 \u2013 6x\u00b2 + 12x \u2013 8 => 2x\u00b2 \u2013 13x + 9 = 0.\nStep 4: The x\u00b3 terms cancel out leaving degree 2. It is a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000009",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "2(i)",
    "difficulty": "medium",
    "text": "[Exercise 4.1 - Q2(i)] Represent the situation as a quadratic equation:\nThe area of a rectangular plot is 528 m\u00b2. The length of the plot (in metres) is one more than twice its breadth. We need to find the length and breadth of the plot.",
    "options": [
      {
        "id": "A",
        "text": "2x\u00b2 + x \u2013 528 = 0, where x is breadth in metres",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x\u00b2 + 2x \u2013 528 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "2x\u00b2 \u2013 x + 528 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "2x\u00b2 + 2x \u2013 528 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let the breadth of the rectangular plot be x metres.\nStep 2: Length is one more than twice its breadth => Length = (2x + 1) metres.\nStep 3: Area = Length \u00d7 Breadth = x(2x + 1) = 2x\u00b2 + x.\nStep 4: Given area = 528 m\u00b2 => 2x\u00b2 + x = 528 => 2x\u00b2 + x \u2013 528 = 0."
  },
  {
    "id": "10000000-0000-0000-0004-000000000010",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 4.1 - Q2(ii)] Represent the situation as a quadratic equation:\nThe product of two consecutive positive integers is 306. We need to find the integers.",
    "options": [
      {
        "id": "A",
        "text": "x\u00b2 + x \u2013 306 = 0, where x is the smaller integer",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x\u00b2 + 2x \u2013 306 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x\u00b2 \u2013 x \u2013 306 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "2x\u00b2 + x \u2013 306 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let two consecutive positive integers be x and (x + 1).\nStep 2: Their product = x(x + 1) = x\u00b2 + x.\nStep 3: Given product = 306 => x\u00b2 + x = 306 => x\u00b2 + x \u2013 306 = 0."
  },
  {
    "id": "10000000-0000-0000-0004-000000000011",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "2(iii)",
    "difficulty": "medium",
    "text": "[Exercise 4.1 - Q2(iii)] Represent the situation as a quadratic equation:\nRohan\u2019s mother is 26 years older than him. The product of their ages (in years) 3 years from now will be 360. We would like to find Rohan\u2019s present age.",
    "options": [
      {
        "id": "A",
        "text": "x\u00b2 + 32x \u2013 273 = 0, where x is Rohan's present age",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x\u00b2 + 26x \u2013 360 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x\u00b2 + 29x \u2013 273 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x\u00b2 + 32x + 273 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let Rohan's present age be x years.\nStep 2: Mother's present age = (x + 26) years.\nStep 3: After 3 years: Rohan's age = (x + 3); Mother's age = (x + 26 + 3) = (x + 29).\nStep 4: Product = (x + 3)(x + 29) = x\u00b2 + 32x + 87.\nStep 5: Given product = 360 => x\u00b2 + 32x + 87 = 360 => x\u00b2 + 32x \u2013 273 = 0."
  },
  {
    "id": "10000000-0000-0000-0004-000000000012",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "2(iv)",
    "difficulty": "hard",
    "text": "[Exercise 4.1 - Q2(iv)] Represent the situation as a quadratic equation:\nA train travels a distance of 480 km at a uniform speed. If the speed had been 8 km/h less, then it would have taken 3 hours more to cover the same distance. We need to find the speed of the train.",
    "options": [
      {
        "id": "A",
        "text": "x\u00b2 \u2013 8x \u2013 1280 = 0, where x is speed in km/h",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x\u00b2 + 8x \u2013 1280 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x\u00b2 \u2013 8x \u2013 480 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "3x\u00b2 \u2013 8x \u2013 1280 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let speed of train be x km/h. Time taken to travel 480 km = 480/x hours.\nStep 2: When speed is reduced by 8 km/h, speed = (x \u2013 8) km/h. Time taken = 480/(x \u2013 8) hours.\nStep 3: Difference in time is 3 hours:\n  480/(x \u2013 8) \u2013 480/x = 3\nStep 4: 480 [ (x \u2013 (x \u2013 8)) / (x(x \u2013 8)) ] = 3\n  => 480 \u00d7 8 / (x\u00b2 \u2013 8x) = 3\n  => 3(x\u00b2 \u2013 8x) = 3840\n  => x\u00b2 \u2013 8x = 1280\n  => x\u00b2 \u2013 8x \u2013 1280 = 0."
  },
  {
    "id": "10000000-0000-0000-0004-000000000013",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "1(i)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q1(i)] Find the roots of the quadratic equation by factorisation:\nx\u00b2 \u2013 3x \u2013 10 = 0",
    "options": [
      {
        "id": "A",
        "text": "x = 5 and x = \u20132",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = \u20135 and x = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 10 and x = \u20131",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 3 and x = \u201310",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Split middle term: \u20133x = \u20135x + 2x and (\u20135)(2) = \u201310.\nStep 2: x\u00b2 \u2013 5x + 2x \u2013 10 = 0\n  => x(x \u2013 5) + 2(x \u2013 5) = 0\n  => (x \u2013 5)(x + 2) = 0.\nStep 3: x \u2013 5 = 0 => x = 5; or x + 2 = 0 => x = \u20132.\nRoots are 5 and \u20132."
  },
  {
    "id": "10000000-0000-0000-0004-000000000014",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "1(ii)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q1(ii)] Find the roots of the quadratic equation by factorisation:\n2x\u00b2 + x \u2013 6 = 0",
    "options": [
      {
        "id": "A",
        "text": "x = 3/2 and x = \u20132",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = \u20133/2 and x = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 2/3 and x = \u20133",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 6 and x = \u20131",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Product = 2 \u00d7 (\u20136) = \u201312. Split +x as +4x \u2013 3x.\nStep 2: 2x\u00b2 + 4x \u2013 3x \u2013 6 = 0\n  => 2x(x + 2) \u2013 3(x + 2) = 0\n  => (2x \u2013 3)(x + 2) = 0.\nStep 3: 2x \u2013 3 = 0 => x = 3/2; x + 2 = 0 => x = \u20132.\nRoots are 3/2 and \u20132."
  },
  {
    "id": "10000000-0000-0000-0004-000000000015",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "1(iii)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q1(iii)] Find the roots of the quadratic equation by factorisation:\n\u221a2 x\u00b2 + 7x + 5\u221a2 = 0",
    "options": [
      {
        "id": "A",
        "text": "x = \u20135/\u221a2 and x = \u2013\u221a2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 5/\u221a2 and x = \u221a2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = \u20135 and x = \u20132",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = \u2013\u221a2 and x = 5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Product = \u221a2 \u00d7 5\u221a2 = 5 \u00d7 2 = 10. Split 7x as 2x + 5x.\nStep 2: \u221a2 x\u00b2 + 2x + 5x + 5\u221a2 = 0\n  => \u221a2 x(x + \u221a2) + 5(x + \u221a2) = 0\n  => (\u221a2 x + 5)(x + \u221a2) = 0.\nStep 3: Either \u221a2 x + 5 = 0 => x = \u20135/\u221a2, or x + \u221a2 = 0 => x = \u2013\u221a2."
  },
  {
    "id": "10000000-0000-0000-0004-000000000016",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "1(iv)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q1(iv)] Find the roots of the quadratic equation by factorisation:\n2x\u00b2 \u2013 x + 1/8 = 0",
    "options": [
      {
        "id": "A",
        "text": "x = 1/4 and x = 1/4",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 1/2 and x = 1/4",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = \u20131/4 and x = \u20131/4",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1/8 and x = 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply entire equation by 8:\n  16x\u00b2 \u2013 8x + 1 = 0.\nStep 2: Recognize identity: (4x \u2013 1)\u00b2 = 16x\u00b2 \u2013 8x + 1 = 0.\nStep 3: (4x \u2013 1)(4x \u2013 1) = 0 => x = 1/4, 1/4.\nBoth equal roots are 1/4."
  },
  {
    "id": "10000000-0000-0000-0004-000000000017",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "1(v)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q1(v)] Find the roots of the quadratic equation by factorisation:\n100x\u00b2 \u2013 20x + 1 = 0",
    "options": [
      {
        "id": "A",
        "text": "x = 1/10 and x = 1/10",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = \u20131/10 and x = \u20131/10",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 1/20 and x = 1/5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1/100 and x = 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Notice (10x \u2013 1)\u00b2 = 100x\u00b2 \u2013 20x + 1 = 0.\nStep 2: (10x \u2013 1)(10x \u2013 1) = 0.\nStep 3: 10x \u2013 1 = 0 => x = 1/10.\nBoth equal roots are 1/10."
  },
  {
    "id": "10000000-0000-0000-0004-000000000018",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "2(i)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q2(i)] Solve the problem given in Example 1(i):\nJohn and Jivanti together have 45 marbles. Both lost 5 marbles each, and the product of marbles they now have is 124. Find how many marbles they had to start with.",
    "options": [
      {
        "id": "A",
        "text": "36 and 9 marbles",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "30 and 15 marbles",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "40 and 5 marbles",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "28 and 17 marbles",
        "is_correct": false
      }
    ],
    "solution": "Step 1: The mathematical formulation from Example 1 is x\u00b2 \u2013 45x + 324 = 0.\nStep 2: Factorise: (x \u2013 36)(x \u2013 9) = 0.\nStep 3: x = 36 or x = 9.\nHence, John and Jivanti had 36 and 9 marbles (or 9 and 36)."
  },
  {
    "id": "10000000-0000-0000-0004-000000000019",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q2(ii)] Solve the problem given in Example 1(ii):\nA cottage industry produces a certain number of toys in a day. Cost of production of each toy was (55 \u2013 x). Total cost of production on that day was \u20b9 750. Find the number of toys produced.",
    "options": [
      {
        "id": "A",
        "text": "30 or 25 toys",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "35 or 20 toys",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "40 or 15 toys",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "50 or 5 toys",
        "is_correct": false
      }
    ],
    "solution": "Step 1: The equation from Example 1 is x\u00b2 \u2013 55x + 750 = 0.\nStep 2: Factorise: (x \u2013 30)(x \u2013 25) = 0.\nStep 3: x = 30 or x = 25.\nThe number of toys produced that day was either 30 or 25."
  },
  {
    "id": "10000000-0000-0000-0004-000000000020",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "3",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q3] Find two numbers whose sum is 27 and product is 182.",
    "options": [
      {
        "id": "A",
        "text": "13 and 14",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "12 and 15",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "11 and 16",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "10 and 17",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let the two numbers be x and (27 \u2013 x).\nStep 2: Product: x(27 \u2013 x) = 182 => 27x \u2013 x\u00b2 = 182 => x\u00b2 \u2013 27x + 182 = 0.\nStep 3: Factorise: 182 = 13 \u00d7 14, and \u201313 \u2013 14 = \u201327.\nStep 4: (x \u2013 13)(x \u2013 14) = 0 => x = 13 or x = 14.\nTherefore, the required numbers are 13 and 14."
  },
  {
    "id": "10000000-0000-0000-0004-000000000021",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "4",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q4] Find two consecutive positive integers, sum of whose squares is 365.",
    "options": [
      {
        "id": "A",
        "text": "13 and 14",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "11 and 12",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "12 and 13",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "14 and 15",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let the two consecutive positive integers be x and (x + 1).\nStep 2: x\u00b2 + (x + 1)\u00b2 = 365 => x\u00b2 + x\u00b2 + 2x + 1 = 365 => 2x\u00b2 + 2x \u2013 364 = 0.\nStep 3: Dividing by 2: x\u00b2 + x \u2013 182 = 0.\nStep 4: (x + 14)(x \u2013 13) = 0 => x = 13 (reject \u201314 since integers are positive).\nStep 5: x + 1 = 14. The two integers are 13 and 14."
  },
  {
    "id": "10000000-0000-0000-0004-000000000022",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "5",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q5] The altitude of a right triangle is 7 cm less than its base. If the hypotenuse is 13 cm, find the other two sides.",
    "options": [
      {
        "id": "A",
        "text": "Base = 12 cm, Altitude = 5 cm",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Base = 10 cm, Altitude = 3 cm",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Base = 15 cm, Altitude = 8 cm",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Base = 9 cm, Altitude = 2 cm",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let base = x cm. Then altitude = (x \u2013 7) cm. Hypotenuse = 13 cm.\nStep 2: By Pythagoras theorem: x\u00b2 + (x \u2013 7)\u00b2 = 13\u00b2 = 169.\nStep 3: x\u00b2 + x\u00b2 \u2013 14x + 49 = 169 => 2x\u00b2 \u2013 14x \u2013 120 = 0 => x\u00b2 \u2013 7x \u2013 60 = 0.\nStep 4: Factorise: (x \u2013 12)(x + 5) = 0 => x = 12 (length cannot be negative).\nStep 5: Base = 12 cm, Altitude = 12 \u2013 7 = 5 cm."
  },
  {
    "id": "10000000-0000-0000-0004-000000000023",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "6",
    "difficulty": "hard",
    "text": "[Exercise 4.2 - Q6] A cottage industry produces a certain number of pottery articles in a day. The cost of production of each article was \u20b9 3 more than twice the number of articles produced. If total cost was \u20b9 90, find the number of articles produced and cost of each article.",
    "options": [
      {
        "id": "A",
        "text": "Number of articles = 6, Cost of each = \u20b9 15",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Number of articles = 5, Cost of each = \u20b9 18",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Number of articles = 10, Cost of each = \u20b9 9",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Number of articles = 8, Cost of each = \u20b9 19",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let number of articles = x. Cost of each article = \u20b9 (2x + 3).\nStep 2: Total cost = x(2x + 3) = 90 => 2x\u00b2 + 3x \u2013 90 = 0.\nStep 3: Factorise: 2x\u00b2 \u2013 12x + 15x \u2013 90 = 0 => 2x(x \u2013 6) + 15(x \u2013 6) = 0 => (2x + 15)(x \u2013 6) = 0.\nStep 4: x = 6 (since articles cannot be negative or fractional).\nStep 5: Cost of each article = 2(6) + 3 = \u20b9 15."
  },
  {
    "id": "10000000-0000-0000-0004-000000000024",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 4.3 - Q1(i)] Find the nature of the roots of the quadratic equation. If real roots exist, find them:\n2x\u00b2 \u2013 3x + 5 = 0",
    "options": [
      {
        "id": "A",
        "text": "No real roots (Discriminant D = \u201331 < 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Two distinct real roots",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Two equal real roots",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Roots are 3/4 and 5/2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Comparing with ax\u00b2 + bx + c = 0: a = 2, b = \u20133, c = 5.\nStep 2: Discriminant D = b\u00b2 \u2013 4ac = (\u20133)\u00b2 \u2013 4(2)(5) = 9 \u2013 40 = \u201331.\nStep 3: Since D < 0, the quadratic equation has NO real roots."
  },
  {
    "id": "10000000-0000-0000-0004-000000000025",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "1(ii)",
    "difficulty": "medium",
    "text": "[Exercise 4.3 - Q1(ii)] Find the nature of the roots of the quadratic equation. If real roots exist, find them:\n3x\u00b2 \u2013 4\u221a3 x + 4 = 0",
    "options": [
      {
        "id": "A",
        "text": "Two equal real roots: 2/\u221a3, 2/\u221a3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No real roots (D < 0)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Two distinct real roots: \u221a3 and \u2013\u221a3",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Two distinct real roots: 4 and 3",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Here a = 3, b = \u20134\u221a3, c = 4.\nStep 2: Discriminant D = b\u00b2 \u2013 4ac = (\u20134\u221a3)\u00b2 \u2013 4(3)(4) = 48 \u2013 48 = 0.\nStep 3: Since D = 0, the equation has two equal real roots.\nStep 4: Roots: x = \u2013b / (2a) = \u2013(\u20134\u221a3) / (2 \u00d7 3) = 4\u221a3 / 6 = 2\u221a3 / 3 = 2/\u221a3.\nHence, roots are 2/\u221a3, 2/\u221a3."
  },
  {
    "id": "10000000-0000-0000-0004-000000000026",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "1(iii)",
    "difficulty": "medium",
    "text": "[Exercise 4.3 - Q1(iii)] Find the nature of the roots of the quadratic equation. If real roots exist, find them:\n2x\u00b2 \u2013 6x + 3 = 0",
    "options": [
      {
        "id": "A",
        "text": "Two distinct real roots: (3 \u00b1 \u221a3) / 2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Two equal real roots: 3/2, 3/2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No real roots (D < 0)",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Two integer roots: 3 and 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 2, b = \u20136, c = 3.\nStep 2: Discriminant D = b\u00b2 \u2013 4ac = (\u20136)\u00b2 \u2013 4(2)(3) = 36 \u2013 24 = 12 > 0.\nStep 3: Since D > 0, there are two distinct real roots.\nStep 4: By quadratic formula:\n  x = [\u2013b \u00b1 \u221aD] / 2a = [\u2013(\u20136) \u00b1 \u221a12] / (2 \u00d7 2) = (6 \u00b1 2\u221a3) / 4 = (3 \u00b1 \u221a3) / 2."
  },
  {
    "id": "10000000-0000-0000-0004-000000000027",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "2(i)",
    "difficulty": "medium",
    "text": "[Exercise 4.3 - Q2(i)] Find the value(s) of k so that the quadratic equation has two equal roots:\n2x\u00b2 + kx + 3 = 0",
    "options": [
      {
        "id": "A",
        "text": "k = \u00b1 2\u221a6",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "k = \u00b1 6",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "k = \u00b1 24",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "k = 12",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 2, b = k, c = 3.\nStep 2: For two equal roots, Discriminant D = b\u00b2 \u2013 4ac = 0.\nStep 3: k\u00b2 \u2013 4(2)(3) = 0 => k\u00b2 \u2013 24 = 0 => k\u00b2 = 24.\nStep 4: k = \u00b1 \u221a24 = \u00b1 \u221a(4 \u00d7 6) = \u00b1 2\u221a6."
  },
  {
    "id": "10000000-0000-0000-0004-000000000028",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 4.3 - Q2(ii)] Find the value(s) of k so that the quadratic equation has two equal roots:\nkx(x \u2013 2) + 6 = 0",
    "options": [
      {
        "id": "A",
        "text": "k = 6",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "k = 0 or 6",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "k = \u20136",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "k = 4",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Expand equation: kx\u00b2 \u2013 2kx + 6 = 0. Here a = k, b = \u20132k, c = 6.\nStep 2: For equal roots, D = b\u00b2 \u2013 4ac = 0.\nStep 3: (\u20132k)\u00b2 \u2013 4(k)(6) = 0 => 4k\u00b2 \u2013 24k = 0 => 4k(k \u2013 6) = 0.\nStep 4: Either k = 0 or k = 6.\nStep 5: If k = 0, equation becomes 6 = 0 (not quadratic). Therefore, k = 6."
  },
  {
    "id": "10000000-0000-0000-0004-000000000029",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "3 to 5",
    "difficulty": "hard",
    "text": "[Exercise 4.3 - Q3 to Q5] Check feasibility of geometric situations:\n(i) Rectangular mango grove length = 2b, area = 800 m\u00b2;\n(ii) Sum of friend ages = 20, product 4 yrs ago was 48;\n(iii) Rectangular park perimeter = 80 m, area = 400 m\u00b2.\nWhich situations are mathematically possible?",
    "options": [
      {
        "id": "A",
        "text": "(i) and (iii) are possible; (ii) is not possible (D < 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "All three situations are possible",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Only (i) is possible",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "None of the situations are possible",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Mango grove: 2x\u00b2 = 800 => x\u00b2 = 400 => x = 20 m (breadth), length = 40 m. Real roots exist. Possible!\nStep 2: Age problem: (x \u2013 4)(16 \u2013 x) = 48 => x\u00b2 \u2013 20x + 112 = 0. D = 400 \u2013 448 = \u201348 < 0. No real roots. Not possible!\nStep 3: Park: l(40 \u2013 l) = 400 => l\u00b2 \u2013 40l + 400 = 0 => (l \u2013 20)\u00b2 = 0 => l = 20 m, b = 20 m. Real equal roots. Possible (square park of side 20 m)!\nHence, (i) and (iii) are possible, (ii) is not possible."
  },
  {
    "id": "10000000-0000-0000-0003-000000000001",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "1(i)",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q1(i)] Form the pair of linear equations and find their solutions graphically:\n10 students of Class X took part in a Mathematics quiz. If the number of girls is 4 more than the number of boys, find the number of boys and girls who took part in the quiz.",
    "options": [
      {
        "id": "A",
        "text": "Boys = 3, Girls = 7",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Boys = 4, Girls = 6",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Boys = 2, Girls = 8",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Boys = 5, Girls = 5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let number of boys = x, girls = y.\nStep 2: Total: x + y = 10 ... (1)\nStep 3: Girls 4 more than boys: y = x + 4 => y - x = 4 ... (2)\nStep 4: Solving gives 2x = 6 => x = 3, y = 7.\nHence, 3 boys and 7 girls took part in the quiz."
  },
  {
    "id": "10000000-0000-0000-0003-000000000002",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "1(ii)",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q1(ii)] Form the pair of linear equations and find their solutions graphically:\n5 pencils and 7 pens together cost \u20b9 50, whereas 7 pencils and 5 pens together cost \u20b9 46. Find the cost of one pencil and that of one pen.",
    "options": [
      {
        "id": "A",
        "text": "Cost of 1 pencil = \u20b9 3, Cost of 1 pen = \u20b9 5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Cost of 1 pencil = \u20b9 5, Cost of 1 pen = \u20b9 3",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Cost of 1 pencil = \u20b9 2, Cost of 1 pen = \u20b9 6",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Cost of 1 pencil = \u20b9 4, Cost of 1 pen = \u20b9 4",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let 1 pencil = \u20b9 x, 1 pen = \u20b9 y.\nStep 2: 5x + 7y = 50 ... (1) and 7x + 5y = 46 ... (2).\nStep 3: Multiplying (1) by 7 and (2) by 5 yields 35x + 49y = 350 and 35x + 25y = 230.\nStep 4: Subtracting gives 24y = 120 => y = 5.\nStep 5: 5x + 35 = 50 => 5x = 15 => x = 3.\nCost of 1 pencil = \u20b9 3, cost of 1 pen = \u20b9 5."
  },
  {
    "id": "10000000-0000-0000-0003-000000000003",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "2(i)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q2(i)] On comparing the ratios a\u2081/a\u2082, b\u2081/b\u2082 and c\u2081/c\u2082, find out whether the lines representing the following pair intersect at a point, are parallel or coincident:\n5x \u2013 4y + 8 = 0\n7x + 6y \u2013 9 = 0",
    "options": [
      {
        "id": "A",
        "text": "Intersect at a point (Unique solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Parallel lines (No solution)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident lines (Infinitely many solutions)",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Inconsistent lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081 = 5, b\u2081 = -4, c\u2081 = 8 and a\u2082 = 7, b\u2082 = 6, c\u2082 = -9.\nStep 2: a\u2081/a\u2082 = 5/7; b\u2081/b\u2082 = -4/6 = -2/3.\nStep 3: Since a\u2081/a\u2082 \u2260 b\u2081/b\u2082 (5/7 \u2260 -2/3), the lines intersect at a point."
  },
  {
    "id": "10000000-0000-0000-0003-000000000004",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "2(ii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q2(ii)] On comparing the ratios a\u2081/a\u2082, b\u2081/b\u2082 and c\u2081/c\u2082, find out whether the lines representing the following pair intersect at a point, are parallel or coincident:\n9x + 3y + 12 = 0\n18x + 6y + 24 = 0",
    "options": [
      {
        "id": "A",
        "text": "Coincident lines (Infinitely many solutions)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Parallel lines",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Intersect at a single point",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Inconsistent lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = 9/18 = 1/2; b\u2081/b\u2082 = 3/6 = 1/2; c\u2081/c\u2082 = 12/24 = 1/2.\nStep 2: Since a\u2081/a\u2082 = b\u2081/b\u2082 = c\u2081/c\u2082 = 1/2, the lines are coincident."
  },
  {
    "id": "10000000-0000-0000-0003-000000000005",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "2(iii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q2(iii)] On comparing the ratios a\u2081/a\u2082, b\u2081/b\u2082 and c\u2081/c\u2082, find out whether the lines representing the following pair intersect at a point, are parallel or coincident:\n6x \u2013 3y + 10 = 0\n2x \u2013 y + 9 = 0",
    "options": [
      {
        "id": "A",
        "text": "Parallel lines (No solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Intersecting lines",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident lines",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Consistent lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = 6/2 = 3; b\u2081/b\u2082 = -3/(-1) = 3; c\u2081/c\u2082 = 10/9.\nStep 2: Since a\u2081/a\u2082 = b\u2081/b\u2082 \u2260 c\u2081/c\u2082 (3 = 3 \u2260 10/9), the lines are parallel."
  },
  {
    "id": "10000000-0000-0000-0003-000000000006",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "3(i)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q3(i)] On comparing the ratios a\u2081/a\u2082, b\u2081/b\u2082 and c\u2081/c\u2082, find out whether the following pair is consistent, or inconsistent:\n3x + 2y = 5\n2x \u2013 3y = 7",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Unique solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent (No solution)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Dependent consistent",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Parallel",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = 3/2; b\u2081/b\u2082 = 2/(-3) = -2/3.\nStep 2: Since a\u2081/a\u2082 \u2260 b\u2081/b\u2082 (3/2 \u2260 -2/3), the pair has a unique solution and is consistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000007",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "3(ii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q3(ii)] On comparing the ratios a\u2081/a\u2082, b\u2081/b\u2082 and c\u2081/c\u2082, find out whether the following pair is consistent, or inconsistent:\n2x \u2013 3y = 8\n4x \u2013 6y = 9",
    "options": [
      {
        "id": "A",
        "text": "Inconsistent (No solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Consistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Infinitely many solutions",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = 2/4 = 1/2; b\u2081/b\u2082 = -3/(-6) = 1/2; c\u2081/c\u2082 = 8/9.\nStep 2: Since a\u2081/a\u2082 = b\u2081/b\u2082 \u2260 c\u2081/c\u2082 (1/2 = 1/2 \u2260 8/9), the lines are parallel and inconsistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000008",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "3(iii)",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q3(iii)] On comparing the ratios a\u2081/a\u2082, b\u2081/b\u2082 and c\u2081/c\u2082, find out whether the pair is consistent or inconsistent:\n(3/2)x + (5/3)y = 7\n9x \u2013 10y = 14",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Unique solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Parallel",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = (3/2)/9 = 1/6; b\u2081/b\u2082 = (5/3)/(-10) = -1/6.\nStep 2: Since a\u2081/a\u2082 \u2260 b\u2081/b\u2082 (1/6 \u2260 -1/6), the pair is consistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000009",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "3(iv)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q3(iv)] On comparing the ratios a\u2081/a\u2082, b\u2081/b\u2082 and c\u2081/c\u2082, find out whether the pair is consistent or inconsistent:\n5x \u2013 3y = 11\n\u201310x + 6y = \u201322",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Coincident lines, infinitely many solutions)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Unique solution",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Parallel lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = 5/(-10) = -1/2; b\u2081/b\u2082 = -3/6 = -1/2; c\u2081/c\u2082 = 11/(-22) = -1/2.\nStep 2: Since a\u2081/a\u2082 = b\u2081/b\u2082 = c\u2081/c\u2082 = -1/2, the pair is consistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000010",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "3(v)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q3(v)] On comparing the ratios a\u2081/a\u2082, b\u2081/b\u2082 and c\u2081/c\u2082, find out whether the pair is consistent or inconsistent:\n(4/3)x + 2y = 8\n2x + 3y = 12",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Coincident lines, dependent)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Parallel lines",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Unique solution",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = (4/3)/2 = 2/3; b\u2081/b\u2082 = 2/3; c\u2081/c\u2082 = 8/12 = 2/3.\nStep 2: Since a\u2081/a\u2082 = b\u2081/b\u2082 = c\u2081/c\u2082 = 2/3, the pair of equations is consistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000011",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "4(i)",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q4(i)] Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:\nx + y = 5\n2x + 2y = 10",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Coincident lines, infinitely many solutions)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent (No solution)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Unique solution: x = 5, y = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Parallel lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = 1/2; b\u2081/b\u2082 = 1/2; c\u2081/c\u2082 = 5/10 = 1/2.\nStep 2: a\u2081/a\u2082 = b\u2081/b\u2082 = c\u2081/c\u2082 = 1/2 => consistent with infinitely many solutions.\nStep 3: Graphically, both lines coincide through (0, 5) and (5, 0)."
  },
  {
    "id": "10000000-0000-0000-0003-000000000012",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "4(ii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q4(ii)] Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:\nx \u2013 y = 8\n3x \u2013 3y = 16",
    "options": [
      {
        "id": "A",
        "text": "Inconsistent (Parallel lines, no solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Consistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Unique solution",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Coincident lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = 1/3; b\u2081/b\u2082 = -1/(-3) = 1/3; c\u2081/c\u2082 = 8/16 = 1/2.\nStep 2: Since a\u2081/a\u2082 = b\u2081/b\u2082 \u2260 c\u2081/c\u2082 (1/3 = 1/3 \u2260 1/2), the lines are parallel and inconsistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000013",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "4(iii)",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q4(iii)] Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:\n2x + y \u2013 6 = 0\n4x \u2013 2y \u2013 4 = 0",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Unique solution: x = 2, y = 2)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident lines",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Parallel lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = 2/4 = 1/2; b\u2081/b\u2082 = 1/(-2) = -1/2.\nStep 2: Since a\u2081/a\u2082 \u2260 b\u2081/b\u2082, the pair is consistent with a unique solution.\nStep 3: Graphing gives intersection at point (2, 2). Hence, x = 2, y = 2."
  },
  {
    "id": "10000000-0000-0000-0003-000000000014",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "4(iv)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q4(iv)] Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:\n2x \u2013 2y \u2013 2 = 0\n4x \u2013 4y \u2013 5 = 0",
    "options": [
      {
        "id": "A",
        "text": "Inconsistent (Parallel lines)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Consistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident lines",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Unique solution",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a\u2081/a\u2082 = 2/4 = 1/2; b\u2081/b\u2082 = -2/(-4) = 1/2; c\u2081/c\u2082 = -2/(-5) = 2/5.\nStep 2: a\u2081/a\u2082 = b\u2081/b\u2082 \u2260 c\u2081/c\u2082 (1/2 = 1/2 \u2260 2/5) => Inconsistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000015",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "5",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q5] Half the perimeter of a rectangular garden, whose length is 4 m more than its width, is 36 m. Find the dimensions of the garden.",
    "options": [
      {
        "id": "A",
        "text": "Length = 20 m, Width = 16 m",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Length = 24 m, Width = 12 m",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Length = 18 m, Width = 14 m",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Length = 22 m, Width = 14 m",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let length = x m, width = y m.\nStep 2: x = y + 4 => x - y = 4 ... (1)\nStep 3: Half perimeter: x + y = 36 ... (2)\nStep 4: Adding gives 2x = 40 => x = 20 m.\nStep 5: y = 36 - 20 = 16 m. Dimensions: Length = 20 m, Width = 16 m."
  },
  {
    "id": "10000000-0000-0000-0003-000000000016",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "6(i)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q6(i)] Given the linear equation 2x + 3y \u2013 8 = 0, write another linear equation in two variables such that the geometrical representation of the pair so formed is intersecting lines.",
    "options": [
      {
        "id": "A",
        "text": "3x + 2y \u2013 7 = 0 (or any equation where a\u2081/a\u2082 \u2260 b\u2081/b\u2082)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "4x + 6y \u2013 16 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "2x + 3y \u2013 12 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "4x + 6y \u2013 9 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Intersecting lines condition: a\u2081/a\u2082 \u2260 b\u2081/b\u2082.\nStep 2: Given 2x + 3y - 8 = 0. Choosing a\u2082 = 3, b\u2082 = 2 gives 2/3 \u2260 3/2.\nStep 3: A valid equation is 3x + 2y - 7 = 0."
  },
  {
    "id": "10000000-0000-0000-0003-000000000017",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "6(ii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q6(ii)] Given the linear equation 2x + 3y \u2013 8 = 0, write another linear equation in two variables such that the geometrical representation of the pair so formed is parallel lines.",
    "options": [
      {
        "id": "A",
        "text": "4x + 6y \u2013 9 = 0 (or any equation where a\u2081/a\u2082 = b\u2081/b\u2082 \u2260 c\u2081/c\u2082)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "4x + 6y \u2013 16 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "3x + 2y \u2013 8 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x + y \u2013 4 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Parallel lines condition: a\u2081/a\u2082 = b\u2081/b\u2082 \u2260 c\u2081/c\u2082.\nStep 2: Multiply coefficients of x and y by 2: 4x + 6y.\nStep 3: Choose c\u2082 \u2260 -16, e.g. -9. Equation: 4x + 6y - 9 = 0."
  },
  {
    "id": "10000000-0000-0000-0003-000000000018",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "6(iii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q6(iii)] Given the linear equation 2x + 3y \u2013 8 = 0, write another linear equation in two variables such that the geometrical representation of the pair so formed is coincident lines.",
    "options": [
      {
        "id": "A",
        "text": "4x + 6y \u2013 16 = 0 (or any scalar multiple k(2x + 3y \u2013 8) = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "4x + 6y \u2013 8 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "2x + 3y + 8 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "3x + 2y \u2013 8 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Coincident lines condition: a\u2081/a\u2082 = b\u2081/b\u2082 = c\u2081/c\u2082.\nStep 2: Multiply equation by 2: 2(2x + 3y - 8) = 4x + 6y - 16 = 0."
  },
  {
    "id": "10000000-0000-0000-0003-000000000019",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "7",
    "difficulty": "hard",
    "text": "[Exercise 3.1 - Q7] Draw the graphs of the equations x \u2013 y + 1 = 0 and 3x + 2y \u2013 12 = 0. Determine the coordinates of the vertices of the triangle formed by these lines and the x-axis, and shade the triangular region.",
    "options": [
      {
        "id": "A",
        "text": "Vertices: (-1, 0), (4, 0), and (2, 3)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Vertices: (1, 0), (4, 0), and (3, 2)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Vertices: (-1, 0), (3, 0), and (2, 4)",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Vertices: (0, 1), (0, 6), and (2, 3)",
        "is_correct": false
      }
    ],
    "solution": "Step 1: For x - y + 1 = 0, x-intercept is (-1, 0).\nStep 2: For 3x + 2y - 12 = 0, x-intercept is (4, 0).\nStep 3: Point of intersection of the lines is (2, 3).\nStep 4: Vertices formed with the x-axis are (-1, 0), (4, 0), and (2, 3)."
  },
  {
    "id": "10000000-0000-0000-0003-000000000020",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 3.2 - Q1(i)] Solve the following pair of linear equations by the substitution method:\nx + y = 14\nx \u2013 y = 4",
    "options": [
      {
        "id": "A",
        "text": "x = 9, y = 5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 5, y = 9",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 10, y = 4",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 8, y = 6",
        "is_correct": false
      }
    ],
    "solution": "Step 1: From (2), x = y + 4.\nStep 2: In (1): (y + 4) + y = 14 => 2y = 10 => y = 5.\nStep 3: x = 5 + 4 = 9. Solution: x = 9, y = 5."
  },
  {
    "id": "10000000-0000-0000-0003-000000000021",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(ii)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q1(ii)] Solve the following pair of linear equations by the substitution method:\ns \u2013 t = 3\n(s/3) + (t/2) = 6",
    "options": [
      {
        "id": "A",
        "text": "s = 9, t = 6",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "s = 6, t = 9",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "s = 8, t = 5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "s = 7, t = 4",
        "is_correct": false
      }
    ],
    "solution": "Step 1: s = t + 3.\nStep 2: Multiply second equation by 6: 2s + 3t = 36.\nStep 3: 2(t + 3) + 3t = 36 => 5t = 30 => t = 6.\nStep 4: s = 6 + 3 = 9. Solution: s = 9, t = 6."
  },
  {
    "id": "10000000-0000-0000-0003-000000000022",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(iii)",
    "difficulty": "easy",
    "text": "[Exercise 3.2 - Q1(iii)] Solve the following pair of linear equations by the substitution method:\n3x \u2013 y = 3\n9x \u2013 3y = 9",
    "options": [
      {
        "id": "A",
        "text": "Infinitely many solutions (y = 3x \u2013 3)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No solution",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Unique solution: x = 1, y = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 3, y = 6",
        "is_correct": false
      }
    ],
    "solution": "Step 1: y = 3x - 3.\nStep 2: In (2): 9x - 3(3x - 3) = 9 => 9 = 9.\nStep 3: True statement for all x. Infinitely many solutions with y = 3x - 3."
  },
  {
    "id": "10000000-0000-0000-0003-000000000023",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(iv)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q1(iv)] Solve the following pair of linear equations by the substitution method:\n0.2x + 0.3y = 1.3\n0.4x + 0.5y = 2.3",
    "options": [
      {
        "id": "A",
        "text": "x = 2, y = 3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 3, y = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 1, y = 4",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 2.5, y = 2.5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply by 10: 2x + 3y = 13 and 4x + 5y = 23.\nStep 2: x = (13 - 3y)/2.\nStep 3: 4((13 - 3y)/2) + 5y = 23 => 26 - 6y + 5y = 23 => y = 3.\nStep 4: x = (13 - 9)/2 = 2. Solution: x = 2, y = 3."
  },
  {
    "id": "10000000-0000-0000-0003-000000000024",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(v)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q1(v)] Solve the following pair of linear equations by the substitution method:\n\u221a2 x + \u221a3 y = 0\n\u221a3 x \u2013 \u221a8 y = 0",
    "options": [
      {
        "id": "A",
        "text": "x = 0, y = 0",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = \u221a2, y = \u221a3",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 1, y = 1",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Infinitely many solutions",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x = (-\u221a3/\u221a2)y.\nStep 2: In (2): \u221a3((-\u221a3/\u221a2)y) - \u221a8 y = 0 => (-7/\u221a2)y = 0 => y = 0.\nStep 3: x = 0. Solution: x = 0, y = 0."
  },
  {
    "id": "10000000-0000-0000-0003-000000000025",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(vi)",
    "difficulty": "hard",
    "text": "[Exercise 3.2 - Q1(vi)] Solve the following pair of linear equations by the substitution method:\n(3/2)x \u2013 (5/3)y = \u20132\n(x/3) + (y/2) = 13/6",
    "options": [
      {
        "id": "A",
        "text": "x = 2, y = 3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 3, y = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = -2, y = -3",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1, y = 2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply by 6: 9x - 10y = -12 and 2x + 3y = 13.\nStep 2: x = (13 - 3y)/2.\nStep 3: 9((13 - 3y)/2) - 10y = -12 => 117 - 47y = -24 => -47y = -141 => y = 3.\nStep 4: x = (13 - 9)/2 = 2. Solution: x = 2, y = 3."
  },
  {
    "id": "10000000-0000-0000-0003-000000000026",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "2",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q2] Solve 2x + 3y = 11 and 2x \u2013 4y = \u201324 and hence find the value of 'm' for which y = mx + 3.",
    "options": [
      {
        "id": "A",
        "text": "x = -2, y = 5; m = -1",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 2, y = 5; m = 1",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = -2, y = 4; m = -2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1, y = 3; m = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: 2x = 11 - 3y.\nStep 2: (11 - 3y) - 4y = -24 => -7y = -35 => y = 5.\nStep 3: 2x = 11 - 15 = -4 => x = -2.\nStep 4: y = mx + 3 => 5 = m(-2) + 3 => 2 = -2m => m = -1."
  },
  {
    "id": "10000000-0000-0000-0003-000000000027",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(i)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q3(i)] The difference between two numbers is 26 and one number is three times the other. Find them.",
    "options": [
      {
        "id": "A",
        "text": "39 and 13",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "36 and 10",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "42 and 16",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "30 and 4",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x - y = 26 and x = 3y.\nStep 2: 3y - y = 26 => 2y = 26 => y = 13.\nStep 3: x = 3(13) = 39. Numbers are 39 and 13."
  },
  {
    "id": "10000000-0000-0000-0003-000000000028",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(ii)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q3(ii)] The larger of two supplementary angles exceeds the smaller by 18 degrees. Find them.",
    "options": [
      {
        "id": "A",
        "text": "99\u00b0 and 81\u00b0",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "100\u00b0 and 80\u00b0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "108\u00b0 and 72\u00b0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "95\u00b0 and 85\u00b0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x + y = 180 and x = y + 18.\nStep 2: (y + 18) + y = 180 => 2y = 162 => y = 81\u00b0.\nStep 3: x = 81 + 18 = 99\u00b0. Angles are 99\u00b0 and 81\u00b0."
  },
  {
    "id": "10000000-0000-0000-0003-000000000029",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(iii)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q3(iii)] The coach of a cricket team buys 7 bats and 6 balls for \u20b9 3800. Later, she buys 3 bats and 5 balls for \u20b9 1750. Find the cost of each bat and each ball.",
    "options": [
      {
        "id": "A",
        "text": "Bat = \u20b9 500, Ball = \u20b9 50",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Bat = \u20b9 450, Ball = \u20b9 70",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Bat = \u20b9 520, Ball = \u20b9 40",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Bat = \u20b9 400, Ball = \u20b9 60",
        "is_correct": false
      }
    ],
    "solution": "Step 1: 7x + 6y = 3800 and 3x + 5y = 1750.\nStep 2: x = (1750 - 5y)/3.\nStep 3: 7((1750 - 5y)/3) + 6y = 3800 => 12250 - 35y + 18y = 11400 => -17y = -850 => y = 50.\nStep 4: x = (1750 - 250)/3 = 500. Bat = \u20b9 500, Ball = \u20b9 50."
  },
  {
    "id": "10000000-0000-0000-0003-000000000030",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(iv)",
    "difficulty": "hard",
    "text": "[Exercise 3.2 - Q3(iv)] The taxi charges in a city consist of a fixed charge together with the charge for distance covered. For 10 km, charge is \u20b9 105; for 15 km, charge is \u20b9 155. What are fixed charges and charge per km? How much for 25 km?",
    "options": [
      {
        "id": "A",
        "text": "Fixed = \u20b9 5, Per km = \u20b9 10; Total for 25 km = \u20b9 255",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Fixed = \u20b9 10, Per km = \u20b9 9; Total for 25 km = \u20b9 235",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Fixed = \u20b9 8, Per km = \u20b9 10; Total for 25 km = \u20b9 258",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Fixed = \u20b9 5, Per km = \u20b9 12; Total for 25 km = \u20b9 305",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x + 10y = 105 and x + 15y = 155.\nStep 2: Subtracting gives 5y = 50 => y = 10 (charge/km).\nStep 3: x = 105 - 100 = 5 (fixed charge).\nStep 4: For 25 km: x + 25y = 5 + 25(10) = \u20b9 255."
  },
  {
    "id": "10000000-0000-0000-0003-000000000031",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(v)",
    "difficulty": "hard",
    "text": "[Exercise 3.2 - Q3(v)] A fraction becomes 9/11, if 2 is added to both numerator and denominator. If 3 is added to both, it becomes 5/6. Find the fraction.",
    "options": [
      {
        "id": "A",
        "text": "7/9",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "5/7",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "3/5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "8/11",
        "is_correct": false
      }
    ],
    "solution": "Step 1: (x + 2)/(y + 2) = 9/11 => 11x - 9y = -4.\nStep 2: (x + 3)/(y + 3) = 5/6 => 6x - 5y = -3.\nStep 3: Solving gives x = 7, y = 9.\nHence, the fraction is 7/9."
  },
  {
    "id": "10000000-0000-0000-0003-000000000032",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(vi)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q3(vi)] Five years hence, the age of Jacob will be three times that of his son. Five years ago, Jacob's age was seven times that of his son. What are their present ages?",
    "options": [
      {
        "id": "A",
        "text": "Jacob = 40 years, Son = 10 years",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Jacob = 45 years, Son = 15 years",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Jacob = 35 years, Son = 5 years",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Jacob = 50 years, Son = 12 years",
        "is_correct": false
      }
    ],
    "solution": "Step 1: (x + 5) = 3(y + 5) => x - 3y = 10.\nStep 2: (x - 5) = 7(y - 5) => x - 7y = -30.\nStep 3: Subtracting gives 4y = 40 => y = 10.\nStep 4: x = 3(10) + 10 = 40. Jacob = 40 years, Son = 10 years."
  },
  {
    "id": "10000000-0000-0000-0003-000000000033",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 3.3 - Q1(i)] Solve the following pair of linear equations by the elimination method and the substitution method:\nx + y = 5\n2x \u2013 3y = 4",
    "options": [
      {
        "id": "A",
        "text": "x = 19/5, y = 6/5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 4, y = 1",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 17/5, y = 8/5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 3, y = 2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply (1) by 2: 2x + 2y = 10.\nStep 2: Subtract (2): 5y = 6 => y = 6/5.\nStep 3: x = 5 - 6/5 = 19/5. Solution: x = 19/5, y = 6/5."
  },
  {
    "id": "10000000-0000-0000-0003-000000000034",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "1(ii)",
    "difficulty": "easy",
    "text": "[Exercise 3.3 - Q1(ii)] Solve the following pair of linear equations by the elimination method:\n3x + 4y = 10\n2x \u2013 2y = 2",
    "options": [
      {
        "id": "A",
        "text": "x = 2, y = 1",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 1, y = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 3, y = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 2, y = 2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply (2) by 2: 4x - 4y = 4.\nStep 2: Add to (1): 7x = 14 => x = 2.\nStep 3: 2(2) - 2y = 2 => 2y = 2 => y = 1. Solution: x = 2, y = 1."
  },
  {
    "id": "10000000-0000-0000-0003-000000000035",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "1(iii)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q1(iii)] Solve the following pair of linear equations by the elimination method:\n3x \u2013 5y \u2013 4 = 0\n9x = 2y + 7",
    "options": [
      {
        "id": "A",
        "text": "x = 9/13, y = -5/13",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = -9/13, y = 5/13",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 7/13, y = -3/13",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1, y = -1/5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: 3x - 5y = 4 and 9x - 2y = 7.\nStep 2: Multiply (1) by 3: 9x - 15y = 12.\nStep 3: Subtract (2): -13y = 5 => y = -5/13.\nStep 4: 3x = 4 + 5(-5/13) = 27/13 => x = 9/13. Solution: x = 9/13, y = -5/13."
  },
  {
    "id": "10000000-0000-0000-0003-000000000036",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "1(iv)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q1(iv)] Solve the following pair of linear equations by the elimination method:\n(x/2) + (2y/3) = \u20131\nx \u2013 (y/3) = 3",
    "options": [
      {
        "id": "A",
        "text": "x = 2, y = -3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = -2, y = 3",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 3, y = -2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1, y = -3",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply (1) by 6: 3x + 4y = -6; Multiply (2) by 3: 3x - y = 9.\nStep 2: Subtract: 5y = -15 => y = -3.\nStep 3: 3x - (-3) = 9 => 3x = 6 => x = 2. Solution: x = 2, y = -3."
  },
  {
    "id": "10000000-0000-0000-0003-000000000037",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "2(i)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q2(i)] If we add 1 to the numerator and subtract 1 from the denominator, a fraction reduces to 1. It becomes 1/2 if we only add 1 to the denominator. What is the fraction?",
    "options": [
      {
        "id": "A",
        "text": "3/5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "2/5",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "4/7",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "5/9",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let fraction be x/y.\nStep 2: (x + 1)/(y - 1) = 1 => x - y = -2.\nStep 3: x/(y + 1) = 1/2 => 2x - y = 1.\nStep 4: Subtracting gives x = 3, y = 5. Fraction is 3/5."
  },
  {
    "id": "10000000-0000-0000-0003-000000000038",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q2(ii)] Five years ago, Nuri was thrice as old as Sonu. Ten years later, Nuri will be twice as old as Sonu. How old are Nuri and Sonu?",
    "options": [
      {
        "id": "A",
        "text": "Nuri = 50 years, Sonu = 20 years",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Nuri = 45 years, Sonu = 15 years",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Nuri = 60 years, Sonu = 25 years",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Nuri = 40 years, Sonu = 15 years",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x - 5 = 3(y - 5) => x - 3y = -10.\nStep 2: x + 10 = 2(y + 10) => x - 2y = 10.\nStep 3: Subtracting gives y = 20, x = 50. Nuri is 50 years old and Sonu is 20 years old."
  },
  {
    "id": "10000000-0000-0000-0003-000000000039",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "2(iii)",
    "difficulty": "hard",
    "text": "[Exercise 3.3 - Q2(iii)] The sum of the digits of a two-digit number is 9. Also, nine times this number is twice the number obtained by reversing the order of the digits. Find the number.",
    "options": [
      {
        "id": "A",
        "text": "18",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "27",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "36",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "45",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Digits x, y. Number = 10x + y. x + y = 9 ... (1)\nStep 2: 9(10x + y) = 2(10y + x) => 88x - 11y = 0 => 8x - y = 0 ... (2)\nStep 3: Adding gives 9x = 9 => x = 1, y = 8. The number is 18."
  },
  {
    "id": "10000000-0000-0000-0003-000000000040",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "2(iv)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q2(iv)] Meena went to a bank to withdraw \u20b9 2000. She asked the cashier to give her \u20b9 50 and \u20b9 100 notes only. Meena got 25 notes in all. Find how many notes of \u20b9 50 and \u20b9 100 she received.",
    "options": [
      {
        "id": "A",
        "text": "10 notes of \u20b9 50, 15 notes of \u20b9 100",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "15 notes of \u20b9 50, 10 notes of \u20b9 100",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "12 notes of \u20b9 50, 13 notes of \u20b9 100",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "8 notes of \u20b9 50, 17 notes of \u20b9 100",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x + y = 25 and 50x + 100y = 2000 => x + 2y = 40.\nStep 2: Subtracting gives y = 15, x = 10.\nMeena received 10 notes of \u20b9 50 and 15 notes of \u20b9 100."
  },
  {
    "id": "10000000-0000-0000-0003-000000000041",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "2(v)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q2(v)] A lending library has a fixed charge for first 3 days and additional charge for each day thereafter. Saritha paid \u20b9 27 for 7 days, Susy paid \u20b9 21 for 5 days. Find fixed charge and charge for each extra day.",
    "options": [
      {
        "id": "A",
        "text": "Fixed charge = \u20b9 15, Extra charge per day = \u20b9 3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Fixed charge = \u20b9 12, Extra charge per day = \u20b9 4",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Fixed charge = \u20b9 14, Extra charge per day = \u20b9 3.5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Fixed charge = \u20b9 10, Extra charge per day = \u20b9 5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x + 4y = 27 and x + 2y = 21.\nStep 2: Subtracting gives 2y = 6 => y = 3 (extra charge/day).\nStep 3: x = 21 - 2(3) = \u20b9 15 (fixed charge)."
  },
  {
    "id": "10000000-0000-0000-0001-000000000001",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 1.1 - Q1(i)] Express the number as a product of its prime factors:\n(i) 140",
    "options": [
      {
        "id": "A",
        "text": "2\u00b2 \u00d7 5 \u00d7 7",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "2 \u00d7 5\u00b2 \u00d7 7",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "2\u00b3 \u00d7 5 \u00d7 7",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "4 \u00d7 35",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Using the prime factorisation method (factor tree):\n  140 \u00f7 2 = 70\n  70 \u00f7 2 = 35\n  35 \u00f7 5 = 7\n  7 \u00f7 7 = 1\nStep 2: Therefore, 140 = 2 \u00d7 2 \u00d7 5 \u00d7 7 = 2\u00b2 \u00d7 5 \u00d7 7."
  },
  {
    "id": "10000000-0000-0000-0001-000000000002",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "1(ii)",
    "difficulty": "easy",
    "text": "[Exercise 1.1 - Q1(ii)] Express the number as a product of its prime factors:\n(ii) 156",
    "options": [
      {
        "id": "A",
        "text": "2\u00b2 \u00d7 3 \u00d7 13",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "2 \u00d7 3\u00b2 \u00d7 13",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "4 \u00d7 39",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "2 \u00d7 78",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Divide 156 by prime factors:\n  156 \u00f7 2 = 78\n  78 \u00f7 2 = 39\n  39 \u00f7 3 = 13\n  13 \u00f7 13 = 1\nStep 2: Therefore, 156 = 2 \u00d7 2 \u00d7 3 \u00d7 13 = 2\u00b2 \u00d7 3 \u00d7 13."
  },
  {
    "id": "10000000-0000-0000-0001-000000000003",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "1(iii)",
    "difficulty": "easy",
    "text": "[Exercise 1.1 - Q1(iii)] Express the number as a product of its prime factors:\n(iii) 3825",
    "options": [
      {
        "id": "A",
        "text": "3\u00b2 \u00d7 5\u00b2 \u00d7 17",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "3 \u00d7 5\u00b2 \u00d7 17",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "3\u00b2 \u00d7 5 \u00d7 17\u00b2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "9 \u00d7 25 \u00d7 17",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Divide 3825 by successive prime numbers:\n  3825 \u00f7 3 = 1275\n  1275 \u00f7 3 = 425\n  425 \u00f7 5 = 85\n  85 \u00f7 5 = 17\n  17 \u00f7 17 = 1\nStep 2: Therefore, 3825 = 3 \u00d7 3 \u00d7 5 \u00d7 5 \u00d7 17 = 3\u00b2 \u00d7 5\u00b2 \u00d7 17."
  },
  {
    "id": "10000000-0000-0000-0001-000000000004",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "1(iv)",
    "difficulty": "easy",
    "text": "[Exercise 1.1 - Q1(iv)] Express the number as a product of its prime factors:\n(iv) 5005",
    "options": [
      {
        "id": "A",
        "text": "5 \u00d7 7 \u00d7 11 \u00d7 13",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "5\u00b2 \u00d7 7 \u00d7 13",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "5 \u00d7 11\u00b2 \u00d7 13",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "35 \u00d7 143",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Divide 5005 by successive prime numbers:\n  5005 \u00f7 5 = 1001\n  1001 \u00f7 7 = 143\n  143 \u00f7 11 = 13\n  13 \u00f7 13 = 1\nStep 2: Therefore, 5005 = 5 \u00d7 7 \u00d7 11 \u00d7 13."
  },
  {
    "id": "10000000-0000-0000-0001-000000000005",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "1(v)",
    "difficulty": "medium",
    "text": "[Exercise 1.1 - Q1(v)] Express the number as a product of its prime factors:\n(v) 7429",
    "options": [
      {
        "id": "A",
        "text": "17 \u00d7 19 \u00d7 23",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "13 \u00d7 19 \u00d7 29",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "17\u00b2 \u00d7 23",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "19 \u00d7 23 \u00d7 29",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Testing initial prime factors shows 2, 3, 5, 7, 11, 13 do not divide 7429.\nStep 2: 7429 \u00f7 17 = 437\nStep 3: 437 \u00f7 19 = 23\nStep 4: 23 \u00f7 23 = 1\nStep 5: Therefore, 7429 = 17 \u00d7 19 \u00d7 23."
  },
  {
    "id": "10000000-0000-0000-0001-000000000006",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "2(i)",
    "difficulty": "easy",
    "text": "[Exercise 1.1 - Q2(i)] Find the LCM and HCF of 26 and 91 and verify that LCM \u00d7 HCF = product of the two numbers.",
    "options": [
      {
        "id": "A",
        "text": "HCF = 13, LCM = 182",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "HCF = 26, LCM = 91",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "HCF = 1, LCM = 2366",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "HCF = 7, LCM = 364",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Prime factorisation:\n  26 = 2 \u00d7 13\n  91 = 7 \u00d7 13\nStep 2: HCF(26, 91) = 13 (common factor with smallest power).\nStep 3: LCM(26, 91) = 2 \u00d7 7 \u00d7 13 = 182.\nStep 4: Verification:\n  LCM \u00d7 HCF = 182 \u00d7 13 = 2366\n  Product of numbers = 26 \u00d7 91 = 2366\n  Hence, LCM \u00d7 HCF = Product of the two numbers verified."
  },
  {
    "id": "10000000-0000-0000-0001-000000000007",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 1.1 - Q2(ii)] Find the LCM and HCF of 510 and 92 and verify that LCM \u00d7 HCF = product of the two numbers.",
    "options": [
      {
        "id": "A",
        "text": "HCF = 2, LCM = 23460",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "HCF = 4, LCM = 11730",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "HCF = 2, LCM = 46920",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "HCF = 6, LCM = 7820",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Prime factorisation:\n  510 = 2 \u00d7 3 \u00d7 5 \u00d7 17\n  92 = 2\u00b2 \u00d7 23\nStep 2: HCF(510, 92) = 2\u00b9 = 2.\nStep 3: LCM(510, 92) = 2\u00b2 \u00d7 3 \u00d7 5 \u00d7 17 \u00d7 23 = 4 \u00d7 15 \u00d7 391 = 23460.\nStep 4: Verification:\n  LCM \u00d7 HCF = 23460 \u00d7 2 = 46920\n  Product of numbers = 510 \u00d7 92 = 46920\n  Hence, LCM \u00d7 HCF = Product of the two numbers verified."
  },
  {
    "id": "10000000-0000-0000-0001-000000000008",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "2(iii)",
    "difficulty": "medium",
    "text": "[Exercise 1.1 - Q2(iii)] Find the LCM and HCF of 336 and 54 and verify that LCM \u00d7 HCF = product of the two numbers.",
    "options": [
      {
        "id": "A",
        "text": "HCF = 6, LCM = 3024",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "HCF = 12, LCM = 1512",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "HCF = 3, LCM = 6048",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "HCF = 18, LCM = 1008",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Prime factorisation:\n  336 = 2\u2074 \u00d7 3 \u00d7 7\n  54 = 2 \u00d7 3\u00b3\nStep 2: HCF(336, 54) = 2\u00b9 \u00d7 3\u00b9 = 6.\nStep 3: LCM(336, 54) = 2\u2074 \u00d7 3\u00b3 \u00d7 7 = 16 \u00d7 27 \u00d7 7 = 3024.\nStep 4: Verification:\n  LCM \u00d7 HCF = 3024 \u00d7 6 = 18144\n  Product of numbers = 336 \u00d7 54 = 18144\n  Hence, LCM \u00d7 HCF = Product of the two numbers verified."
  },
  {
    "id": "10000000-0000-0000-0001-000000000009",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "3(i)",
    "difficulty": "easy",
    "text": "[Exercise 1.1 - Q3(i)] Find the LCM and HCF of 12, 15 and 21 by applying the prime factorisation method.",
    "options": [
      {
        "id": "A",
        "text": "HCF = 3, LCM = 420",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "HCF = 6, LCM = 210",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "HCF = 1, LCM = 1260",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "HCF = 3, LCM = 840",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Prime factorisation:\n  12 = 2\u00b2 \u00d7 3\n  15 = 3 \u00d7 5\n  21 = 3 \u00d7 7\nStep 2: HCF = 3\u00b9 = 3 (common factor in all three).\nStep 3: LCM = 2\u00b2 \u00d7 3 \u00d7 5 \u00d7 7 = 4 \u00d7 3 \u00d7 5 \u00d7 7 = 420."
  },
  {
    "id": "10000000-0000-0000-0001-000000000010",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "3(ii)",
    "difficulty": "easy",
    "text": "[Exercise 1.1 - Q3(ii)] Find the LCM and HCF of 17, 23 and 29 by applying the prime factorisation method.",
    "options": [
      {
        "id": "A",
        "text": "HCF = 1, LCM = 11339",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "HCF = 1, LCM = 22678",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "HCF = 17, LCM = 667",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "HCF = 29, LCM = 391",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Notice that 17, 23, and 29 are all prime numbers:\n  17 = 1 \u00d7 17\n  23 = 1 \u00d7 23\n  29 = 1 \u00d7 29\nStep 2: Since there is no common prime factor, HCF = 1.\nStep 3: LCM = 17 \u00d7 23 \u00d7 29 = 391 \u00d7 29 = 11339."
  },
  {
    "id": "10000000-0000-0000-0001-000000000011",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "3(iii)",
    "difficulty": "easy",
    "text": "[Exercise 1.1 - Q3(iii)] Find the LCM and HCF of 8, 9 and 25 by applying the prime factorisation method.",
    "options": [
      {
        "id": "A",
        "text": "HCF = 1, LCM = 1800",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "HCF = 2, LCM = 900",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "HCF = 3, LCM = 3600",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "HCF = 1, LCM = 72",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Prime factorisation:\n  8 = 2\u00b3\n  9 = 3\u00b2\n  25 = 5\u00b2\nStep 2: No common prime factor exists across all three numbers, so HCF = 1.\nStep 3: LCM = 2\u00b3 \u00d7 3\u00b2 \u00d7 5\u00b2 = 8 \u00d7 9 \u00d7 25 = 72 \u00d7 25 = 1800."
  },
  {
    "id": "10000000-0000-0000-0001-000000000012",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "4",
    "difficulty": "medium",
    "text": "[Exercise 1.1 - Q4] Given that HCF (306, 657) = 9, find LCM (306, 657).",
    "options": [
      {
        "id": "A",
        "text": "22338",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "22383",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "201042",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "22438",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Formula connecting HCF and LCM of two positive integers a and b:\n  HCF(a, b) \u00d7 LCM(a, b) = a \u00d7 b\nStep 2: Here a = 306, b = 657, and HCF = 9.\n  9 \u00d7 LCM(306, 657) = 306 \u00d7 657\nStep 3: LCM(306, 657) = (306 \u00d7 657) / 9\n  306 \u00f7 9 = 34\n  LCM = 34 \u00d7 657 = 22338."
  },
  {
    "id": "10000000-0000-0000-0001-000000000013",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "5",
    "difficulty": "medium",
    "text": "[Exercise 1.1 - Q5] Check whether 6\u207f can end with the digit 0 for any natural number n.",
    "options": [
      {
        "id": "A",
        "text": "No, because the prime factorisation of 6\u207f contains only 2 and 3, not 5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, for any even value of n",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, when n is a multiple of 5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Yes, because 6 ends with an even digit",
        "is_correct": false
      }
    ],
    "solution": "Step 1: If any number ends with the digit 0, it must be divisible by 10 = 2 \u00d7 5.\n  That is, its prime factorisation must contain both 2 and 5 as prime factors.\nStep 2: Prime factorisation of 6\u207f = (2 \u00d7 3)\u207f = 2\u207f \u00d7 3\u207f.\nStep 3: The only primes in the factorisation of 6\u207f are 2 and 3.\nStep 4: By the uniqueness of the Fundamental Theorem of Arithmetic, there are no other primes in the factorisation of 6\u207f.\nStep 5: Since 5 is not a factor, 6\u207f cannot be divisible by 5.\n  Therefore, 6\u207f cannot end with the digit 0 for any natural number n."
  },
  {
    "id": "10000000-0000-0000-0001-000000000014",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "6",
    "difficulty": "easy",
    "text": "[Exercise 1.1 - Q6] Explain why 7 \u00d7 11 \u00d7 13 + 13 and 7 \u00d7 6 \u00d7 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1 + 5 are composite numbers.",
    "options": [
      {
        "id": "A",
        "text": "Both expressions have factors other than 1 and themselves (13 and 5 can be factored out)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Because they are products of consecutive integers",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Because both result in even numbers",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Because their sum is divisible by 2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: A composite number has factors other than 1 and the number itself.\nStep 2: First expression:\n  7 \u00d7 11 \u00d7 13 + 13 = 13 \u00d7 (7 \u00d7 11 + 1)\n  = 13 \u00d7 (77 + 1) = 13 \u00d7 78 = 13 \u00d7 13 \u00d7 6 = 2 \u00d7 3 \u00d7 13\u00b2.\n  Since it has factors 2, 3, 13 besides 1 and itself, it is a composite number.\nStep 3: Second expression:\n  7 \u00d7 6 \u00d7 5 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1 + 5 = 5 \u00d7 (7 \u00d7 6 \u00d7 4 \u00d7 3 \u00d7 2 \u00d7 1 + 1)\n  = 5 \u00d7 (1008 + 1) = 5 \u00d7 1009.\n  Since 1009 is a prime, the number has 5 and 1009 as factors besides 1 and itself.\n  Hence, both are composite numbers."
  },
  {
    "id": "10000000-0000-0000-0001-000000000015",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.1",
    "questionNumber": "7",
    "difficulty": "medium",
    "text": "[Exercise 1.1 - Q7] There is a circular path around a sports field. Sonia takes 18 minutes to drive one round of the field, while Ravi takes 12 minutes for the same. Suppose they both start at the same point and at the same time, and go in the same direction. After how many minutes will they meet again at the starting point?",
    "options": [
      {
        "id": "A",
        "text": "36 minutes",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "6 minutes",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "60 minutes",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "216 minutes",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Sonia and Ravi start simultaneously and travel in the same direction.\nStep 2: They will meet again at the starting point after a time period which is the Lowest Common Multiple (LCM) of the times taken by both:\n  Required time = LCM(18, 12)\nStep 3: Prime factorisation:\n  18 = 2 \u00d7 3\u00b2\n  12 = 2\u00b2 \u00d7 3\nStep 4: LCM(18, 12) = 2\u00b2 \u00d7 3\u00b2 = 4 \u00d7 9 = 36 minutes.\nStep 5: Hence, they will meet again at the starting point after 36 minutes."
  },
  {
    "id": "10000000-0000-0000-0001-000000000016",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.2",
    "questionNumber": "1",
    "difficulty": "hard",
    "text": "[Exercise 1.2 - Q1] Prove that \u221a5 is irrational.",
    "options": [
      {
        "id": "A",
        "text": "Proof by contradiction: 5 divides both a and b, contradicting that gcd(a,b)=1",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Proof by division: \u221a5 cannot be written as a terminating fraction",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Proof by geometry: diagonal of unit square is irrational",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Proof by induction: \u221an is irrational for all primes n",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Assume to the contrary that \u221a5 is rational.\n  Then there exist coprime integers a and b (b \u2260 0, gcd(a,b) = 1) such that:\n  \u221a5 = a / b => a = b\u221a5\nStep 2: Squaring both sides:\n  a\u00b2 = 5b\u00b2  ... (Equation 1)\n  This means 5 divides a\u00b2. By Theorem 1.2, if a prime p divides a\u00b2, then p divides a.\n  Therefore, 5 divides a.\nStep 3: Let a = 5c for some integer c. Substitute a in Equation 1:\n  (5c)\u00b2 = 5b\u00b2 => 25c\u00b2 = 5b\u00b2 => b\u00b2 = 5c\u00b2\n  This means 5 divides b\u00b2, which implies 5 divides b.\nStep 4: From Steps 2 and 3, both a and b share a common factor 5.\n  This contradicts the fact that a and b are coprime (share no common factor other than 1).\nStep 5: This contradiction arises from our incorrect assumption that \u221a5 is rational.\n  Hence, \u221a5 is irrational."
  },
  {
    "id": "10000000-0000-0000-0001-000000000017",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.2",
    "questionNumber": "2",
    "difficulty": "medium",
    "text": "[Exercise 1.2 - Q2] Prove that 3 + 2\u221a5 is irrational.",
    "options": [
      {
        "id": "A",
        "text": "Proof by contradiction: \u221a5 = (a - 3b)/(2b) equates an irrational to a rational",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Proof by approximation: 3 + 2(2.236) is non-terminating",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Proof by squaring: (3 + 2\u221a5)\u00b2 = 29 + 12\u221a5 has no integer root",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Proof by decimal expansion: remainder never repeats",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Assume to the contrary that 3 + 2\u221a5 is rational.\n  Then there exist coprime integers a and b (b \u2260 0) such that:\n  3 + 2\u221a5 = a / b\nStep 2: Rearranging the equation to isolate \u221a5:\n  2\u221a5 = (a / b) - 3\n  2\u221a5 = (a - 3b) / b\n  \u221a5 = (a - 3b) / (2b)\nStep 3: Since a and b are integers, (a - 3b) and 2b are also integers (2b \u2260 0).\n  Therefore, (a - 3b) / (2b) is a rational number.\nStep 4: This implies that \u221a5 is rational. But this contradicts the known fact that \u221a5 is irrational.\nStep 5: This contradiction has arisen because of our incorrect assumption that 3 + 2\u221a5 is rational.\n  Hence, 3 + 2\u221a5 is irrational."
  },
  {
    "id": "10000000-0000-0000-0001-000000000018",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.2",
    "questionNumber": "3(i)",
    "difficulty": "medium",
    "text": "[Exercise 1.2 - Q3(i)] Prove that the following is irrational:\n(i) 1 / \u221a2",
    "options": [
      {
        "id": "A",
        "text": "Proof: 1/\u221a2 = a/b => \u221a2 = b/a, equating irrational \u221a2 to rational b/a",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Proof: Rationalising denominator gives \u221a2 / 2 which cannot be solved",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Proof: 1 divided by any root is non-terminating",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Proof: Reciprocal of an irrational number is always undefined",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let us assume to the contrary that 1/\u221a2 is rational.\n  Then there exist coprime integers a and b (where a \u2260 0, b \u2260 0) such that:\n  1 / \u221a2 = a / b\nStep 2: Taking reciprocals on both sides:\n  \u221a2 = b / a\nStep 3: Since b and a are integers and a \u2260 0, b / a is a rational number.\nStep 4: This implies that \u221a2 is a rational number.\n  But this contradicts the established fact that \u221a2 is irrational.\nStep 5: Hence, our assumption was false. Therefore, 1/\u221a2 is irrational."
  },
  {
    "id": "10000000-0000-0000-0001-000000000019",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.2",
    "questionNumber": "3(ii)",
    "difficulty": "medium",
    "text": "[Exercise 1.2 - Q3(ii)] Prove that the following is irrational:\n(ii) 7\u221a5",
    "options": [
      {
        "id": "A",
        "text": "Proof: 7\u221a5 = a/b => \u221a5 = a/(7b), equating irrational \u221a5 to rational a/(7b)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Proof: Product of any integer and root is an imaginary number",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Proof: Multiplying by 7 preserves prime factorisation",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Proof: 7\u00b2 \u00d7 5 = 245 has no square root",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let us assume to the contrary that 7\u221a5 is rational.\n  Then there exist coprime integers a and b (b \u2260 0) such that:\n  7\u221a5 = a / b\nStep 2: Rearranging for \u221a5:\n  \u221a5 = a / (7b)\nStep 3: Since 7, a, and b are integers and 7b \u2260 0, a / (7b) is a rational number.\nStep 4: This implies that \u221a5 is rational.\n  However, this contradicts the fact that \u221a5 is irrational.\nStep 5: Hence, our assumption is false. Therefore, 7\u221a5 is irrational."
  },
  {
    "id": "10000000-0000-0000-0001-000000000020",
    "subject": "math",
    "chapterId": "math_ch_01_real_numbers",
    "exercise": "Exercise 1.2",
    "questionNumber": "3(iii)",
    "difficulty": "medium",
    "text": "[Exercise 1.2 - Q3(iii)] Prove that the following is irrational:\n(iii) 6 + \u221a2",
    "options": [
      {
        "id": "A",
        "text": "Proof: 6 + \u221a2 = a/b => \u221a2 = (a - 6b)/b, equating irrational \u221a2 to rational",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Proof: 6 is composite so adding \u221a2 makes it transcendental",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Proof: (6 + \u221a2)\u00b2 = 38 + 12\u221a2 is non-repeating",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Proof: Sum of rational and irrational is always undefined",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let us assume to the contrary that 6 + \u221a2 is rational.\n  Then there exist coprime integers a and b (b \u2260 0) such that:\n  6 + \u221a2 = a / b\nStep 2: Rearranging to isolate \u221a2:\n  \u221a2 = (a / b) - 6\n  \u221a2 = (a - 6b) / b\nStep 3: Since a, b, and 6 are integers, (a - 6b) / b is a rational number.\nStep 4: This implies that \u221a2 is rational, which contradicts the theorem that \u221a2 is irrational.\nStep 5: Therefore, our assumption was incorrect. We conclude that 6 + \u221a2 is irrational."
  },
  {
    "id": "m_poly_1",
    "subject": "math",
    "chapterId": "math_ch_02_polynomials",
    "exercise": "Exercise 2.1",
    "questionNumber": "1",
    "difficulty": "easy",
    "text": "If one zero of the quadratic polynomial p(x) = x\u00b2 + 3x + k is 2, then the value of k is:",
    "options": [
      {
        "id": "A",
        "text": "10",
        "correct": false
      },
      {
        "id": "B",
        "text": "-10",
        "correct": true
      },
      {
        "id": "C",
        "text": "-7",
        "correct": false
      },
      {
        "id": "D",
        "text": "-2",
        "correct": false
      }
    ],
    "solution": "Step 1: p(2) = 0 => (2)\u00b2 + 3(2) + k = 0 => 4 + 6 + k = 0 => k = -10."
  },
  {
    "id": "s1",
    "subject": "science",
    "chapterId": "sci_ch_09_light",
    "exercise": "NCERT In-Text",
    "questionNumber": "1",
    "difficulty": "medium",
    "text": "An object is placed at 10 cm in front of a concave mirror of focal length 15 cm. What are the image characteristics?",
    "options": [
      {
        "id": "A",
        "text": "Real and diminished",
        "correct": false
      },
      {
        "id": "B",
        "text": "Virtual, erect, and magnified",
        "correct": true
      },
      {
        "id": "C",
        "text": "Real and inverted",
        "correct": false
      },
      {
        "id": "D",
        "text": "Same size",
        "correct": false
      }
    ],
    "solution": "Step 1: f = -15 cm, u = -10 cm (Object between F and Pole P).\nStep 2: 1/v = -1/15 + 1/10 = +1/30 => v = +30 cm (Behind mirror).\nStep 3: m = +3 => Virtual, erect, magnified."
  },
  {
    "id": "sst1",
    "subject": "sst",
    "chapterId": "sst_ch_02_nationalism",
    "exercise": "NCERT In-Text",
    "questionNumber": "1",
    "difficulty": "easy",
    "text": "Why did Mahatma Gandhi withdraw the Non-Cooperation Movement in February 1922?",
    "options": [
      {
        "id": "A",
        "text": "Rowlatt Act",
        "correct": false
      },
      {
        "id": "B",
        "text": "Chauri Chaura violent clash",
        "correct": true
      },
      {
        "id": "C",
        "text": "Simon Commission",
        "correct": false
      },
      {
        "id": "D",
        "text": "Poona Pact",
        "correct": false
      }
    ],
    "solution": "Step 1: In Feb 1922 at Chauri Chaura, protestors set fire to a police station, killing 22 policemen.\nStep 2: Gandhi called off the movement to train satyagrahis in strict non-violence."
  }
];

    let pending = [
      {
        id: 'p_sci_1',
        subject: 'science',
        chapterId: 'science_ch_1_chemical_reactions',
        chapter: 'Chemical Reactions (Page 6 In-Text)',
        difficulty: 'easy',
        text: 'Why should a magnesium ribbon be cleaned before burning in air?',
        options: [
          { id: 'A', text: 'To remove basic magnesium oxide protective layer', correct: true },
          { id: 'B', text: 'To remove grease and moisture', correct: false }
        ],
        solution: 'Step 1: Magnesium ribbon reacts with moist air forming a protective MgO film.\nStep 2: Sandpaper removes this oxide barrier so it burns with dazzling white flame.'
      }
    ];

    function changeMobileRole(newRole) {
      role = newRole;
      navTo(currentTab);
    }

    function toggleMobileOffline() {
      offline = !offline;
      const btn = document.getElementById('mobile-offline-btn');
      btn.innerHTML = offline ? '⚡ Offline' : '☁️ Live';
      btn.className = offline 
        ? 'px-2 py-1 rounded-full text-[10px] font-bold bg-amber-500/20 text-amber-400 border border-amber-500/30'
        : 'px-2 py-1 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30';
    }


    function selectClassLevel(cls) {
      selectedClassLevel = cls;
      ['Class 8', 'Class 9', 'Class 10'].forEach(c => {
        const num = c.split(' ')[1];
        const btn = document.getElementById('class-btn-' + num);
        if (btn) {
          if (c === cls) {
            btn.className = "flex-1 py-3 px-2 rounded-2xl border text-center transition font-bold border-blue-500 bg-blue-950/70 ring-2 ring-blue-500/40 text-white shadow-md";
          } else {
            btn.className = "flex-1 py-3 px-2 rounded-2xl border text-center transition font-medium border-slate-700 bg-slate-800/80 text-slate-400 hover:border-slate-600";
          }
        }
      });
    }

    function autofillDemoStudent() {
      selectClassLevel('Class 10');
      const nameEl = document.getElementById('input-student-name');
      const emailEl = document.getElementById('input-student-email');
      const schoolEl = document.getElementById('input-student-school');
      if (nameEl) nameEl.value = 'Aarav Sharma';
      if (emailEl) emailEl.value = 'aarav.sharma@cbse10.edu';
      if (schoolEl) schoolEl.value = 'Delhi Public School, Bangalore';
    }

    function submitStudentLogin() {
      const nameEl = document.getElementById('input-student-name');
      const emailEl = document.getElementById('input-student-email');
      const schoolEl = document.getElementById('input-student-school');

      const name = nameEl ? nameEl.value.trim() : '';
      const email = emailEl ? emailEl.value.trim() : '';
      const school = schoolEl ? schoolEl.value.trim() : '';

      if (!name) {
        alert('⚠️ Please enter your Student Name.');
        nameEl?.focus();
        return;
      }
      if (!email || !email.includes('@')) {
        alert('⚠️ Please enter a valid Email-ID.');
        emailEl?.focus();
        return;
      }
      if (!school) {
        alert('⚠️ Please enter your School Name.');
        schoolEl?.focus();
        return;
      }

      studentProfile = {
        name: name,
        email: email,
        school: school,
        classLevel: selectedClassLevel || 'Class 10',
        joinedAt: new Date().toISOString()
      };

      localStorage.setItem('cbse_student_profile', JSON.stringify(studentProfile));
      role = 'student';
      const roleSelect = document.getElementById('role-select');
      if (roleSelect) roleSelect.value = 'student';
      navTo('home');
    }

    function logoutStudent() {
      if (confirm('Do you want to switch or edit your student profile?')) {
        localStorage.removeItem('cbse_student_profile');
        studentProfile = null;
        navTo('login');
      }
    }

    function navTo(screen, param = null) {
      currentTab = screen;
      const header = document.getElementById('mobile-header');
      const bottomNav = document.getElementById('mobile-bottom-nav');
      const title = document.getElementById('mobile-title');
      const content = document.getElementById('mobile-main-content');

      // Enforce student login at the beginning
      if (!studentProfile && role === 'student' && screen !== 'login') {
        screen = 'login';
        currentTab = 'login';
      }

      // Hide or show top header and bottom nav depending on screen
      if (screen === 'login') {
        if (header) header.style.display = 'none';
        if (bottomNav) bottomNav.style.display = 'none';
      } else if (screen === 'chapter_practice' || screen === 'chapter_formulas') {
        if (header) header.style.display = 'none';
        if (bottomNav) bottomNav.style.display = 'flex';
      } else {
        if (header) header.style.display = 'flex';
        if (bottomNav) bottomNav.style.display = 'flex';
      }

      if (screen === 'login') {
        content.innerHTML = `
          <div class="py-2 space-y-4 max-w-md mx-auto">
            <!-- App Branding Header -->
            <div class="text-center space-y-1.5 pt-2">
              <div class="w-16 h-16 mx-auto rounded-3xl bg-gradient-to-tr from-blue-600 to-indigo-600 flex items-center justify-center text-3xl shadow-xl shadow-blue-500/20">
                🎓
              </div>
              <h1 class="text-xl font-black text-white tracking-tight">CBSE Student Masterclass</h1>
              <p class="text-xs text-slate-400 max-w-xs mx-auto">Personalized Board Exam Success Suite, NCERT Exercises & Formula Engine</p>
            </div>

            <!-- Login / Onboarding Card -->
            <div class="bg-slate-800/90 border border-slate-700/80 rounded-3xl p-5 space-y-4 shadow-xl backdrop-blur">
              <div class="flex items-center justify-between border-b border-slate-700/60 pb-3">
                <span class="text-xs font-bold text-blue-400 uppercase tracking-wider">Student Onboarding</span>
                <span class="text-[10px] bg-blue-500/10 text-blue-300 font-semibold px-2 py-0.5 rounded-full border border-blue-500/20">NCERT 2026</span>
              </div>

              <!-- Step 1: Choose Class -->
              <div class="space-y-2">
                <label class="text-xs font-bold text-slate-200 flex items-center gap-1.5">
                  <span>1. Choose Class:</span>
                  <span class="text-[10px] text-blue-400 font-normal">(Select 8, 9 or 10)</span>
                </label>
                <div class="flex gap-2">
                  <button type="button" id="class-btn-8" onclick="selectClassLevel('Class 8')" class="flex-1 py-3 px-2 rounded-2xl border text-center transition font-medium ${selectedClassLevel === 'Class 8' ? 'border-blue-500 bg-blue-950/70 ring-2 ring-blue-500/40 text-white shadow-md' : 'border-slate-700 bg-slate-800/80 text-slate-400 hover:border-slate-600'}">
                    <div class="text-xs font-black">Class 8</div>
                    <div class="text-[9px] opacity-70">Middle School</div>
                  </button>
                  <button type="button" id="class-btn-9" onclick="selectClassLevel('Class 9')" class="flex-1 py-3 px-2 rounded-2xl border text-center transition font-medium ${selectedClassLevel === 'Class 9' ? 'border-blue-500 bg-blue-950/70 ring-2 ring-blue-500/40 text-white shadow-md' : 'border-slate-700 bg-slate-800/80 text-slate-400 hover:border-slate-600'}">
                    <div class="text-xs font-black">Class 9</div>
                    <div class="text-[9px] opacity-70">Foundation</div>
                  </button>
                  <button type="button" id="class-btn-10" onclick="selectClassLevel('Class 10')" class="flex-1 py-3 px-2 rounded-2xl border text-center transition font-bold ${selectedClassLevel === 'Class 10' ? 'border-blue-500 bg-blue-950/70 ring-2 ring-blue-500/40 text-white shadow-md' : 'border-slate-700 bg-slate-800/80 text-slate-400 hover:border-slate-600'}">
                    <div class="text-xs font-black">Class 10</div>
                    <div class="text-[9px] text-blue-300 font-semibold">Board Exam</div>
                  </button>
                </div>
              </div>

              <!-- Step 2: Student Details Form -->
              <div class="space-y-3 pt-1">
                <div class="space-y-1">
                  <label class="text-xs font-bold text-slate-200">2. Student Name:</label>
                  <div class="relative">
                    <span class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 text-xs">👤</span>
                    <input id="input-student-name" type="text" placeholder="Enter your full name" value="${studentProfile?.name || ''}" class="w-full pl-8 pr-3 py-2.5 bg-slate-900/90 border border-slate-700 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 font-medium">
                  </div>
                </div>

                <div class="space-y-1">
                  <label class="text-xs font-bold text-slate-200">3. Email-ID:</label>
                  <div class="relative">
                    <span class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 text-xs">✉️</span>
                    <input id="input-student-email" type="email" placeholder="student@school.edu" value="${studentProfile?.email || ''}" class="w-full pl-8 pr-3 py-2.5 bg-slate-900/90 border border-slate-700 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 font-medium">
                  </div>
                </div>

                <div class="space-y-1">
                  <label class="text-xs font-bold text-slate-200">4. School Name:</label>
                  <div class="relative">
                    <span class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 text-xs">🏫</span>
                    <input id="input-student-school" type="text" placeholder="Enter your school name & city" value="${studentProfile?.school || ''}" class="w-full pl-8 pr-3 py-2.5 bg-slate-900/90 border border-slate-700 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 font-medium">
                  </div>
                </div>
              </div>

              <!-- Submit Buttons -->
              <div class="space-y-2 pt-2">
                <button onclick="submitStudentLogin()" class="w-full py-3 px-4 rounded-2xl bg-gradient-to-r from-blue-600 via-indigo-600 to-blue-700 text-white font-bold text-xs shadow-lg shadow-blue-500/25 hover:from-blue-500 hover:to-indigo-500 active:scale-98 transition flex items-center justify-center gap-2">
                  <span>🚀 Launch Student Dashboard</span>
                  <span>→</span>
                </button>

                <button onclick="autofillDemoStudent()" type="button" class="w-full py-2.5 px-3 rounded-xl bg-slate-700/60 hover:bg-slate-700 text-slate-300 font-semibold text-xs border border-slate-600/60 active:scale-98 transition flex items-center justify-center gap-1.5">
                  <span>⚡ Autofill Demo Student Profile</span>
                </button>
              </div>

              <!-- Switcher link for testing Admin persona directly -->
              <div class="pt-2 text-center border-t border-slate-700/60">
                <button onclick="changeMobileRole('admin'); document.getElementById('role-select').value = 'admin';" class="text-[11px] text-purple-400 hover:text-purple-300 font-medium underline">
                  🛡️ Need Admin / Teacher Ingestion Tools? Switch here
                </button>
              </div>
            </div>
          </div>
        `;
      } else if (screen === 'home') {
        selectedChapterId = null;
        activeHubMode = null;
        title.innerText = 'CBSE Masterclass';

        // Calculate student learning KPIs
        const totalMathQ = questions.filter(q => q.subject === 'math').length;
        const totalSolved = solvedQuestions.size;
        const totalAttempted = Object.keys(userSelectedOptions).length;
        const accuracyPct = totalAttempted > 0 ? Math.round((totalSolved / totalAttempted) * 100) : 100;
        const studentName = studentProfile?.name || 'Aarav Sharma';
        const studentClass = studentProfile?.classLevel || 'Class 10';
        const studentSchool = studentProfile?.school || 'Delhi Public School';

        content.innerHTML = `
          <!-- Student Profile & Welcome Hero Header -->
          <div class="bg-gradient-to-br from-blue-950/80 via-slate-800 to-indigo-950/70 border border-blue-500/30 rounded-3xl p-4 space-y-3 shadow-lg relative overflow-hidden">
            <div class="absolute -right-4 -bottom-4 w-28 h-28 bg-blue-500/10 rounded-full blur-2xl pointer-events-none"></div>

            <div class="flex items-start justify-between gap-3">
              <div class="flex items-center gap-3">
                <div class="w-12 h-12 rounded-2xl bg-gradient-to-tr from-blue-500 to-indigo-600 flex items-center justify-center text-xl font-bold text-white shadow-md shadow-blue-500/20 shrink-0">
                  ${studentName.charAt(0)}
                </div>
                <div>
                  <div class="text-[11px] text-blue-300 font-semibold flex items-center gap-1">
                    <span>👋 Welcome Back,</span>
                  </div>
                  <div class="text-base font-black text-white leading-tight">${studentName}</div>
                </div>
              </div>
              <button onclick="logoutStudent()" title="Edit profile or switch student" class="px-2.5 py-1 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-[11px] text-slate-300 border border-slate-700 transition flex items-center gap-1 shrink-0">
                <span>⚙️</span> <span>Profile</span>
              </button>
            </div>

            <!-- Student Metadata Badges -->
            <div class="flex flex-wrap items-center gap-1.5 pt-1">
              <span class="px-2.5 py-0.5 rounded-lg bg-blue-500/20 border border-blue-500/40 text-blue-300 text-[11px] font-bold">
                🎓 ${studentClass}
              </span>
              <span class="px-2.5 py-0.5 rounded-lg bg-indigo-500/20 border border-indigo-500/30 text-indigo-200 text-[11px] font-medium truncate max-w-[210px]">
                🏫 ${studentSchool}
              </span>
              <span class="px-2.5 py-0.5 rounded-lg bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 text-[11px] font-bold">
                ✓ CBSE Board Ready
              </span>
            </div>
          </div>

          <!-- Academic Performance KPI Metric Cards (2x2 Grid) -->
          <div class="grid grid-cols-2 gap-2.5">
            <div class="bg-slate-800 border border-slate-700/80 rounded-2xl p-3 space-y-1">
              <div class="flex items-center justify-between text-slate-400 text-[11px]">
                <span>🎯 Board Target</span>
                <span class="text-blue-400 font-bold">Max</span>
              </div>
              <div class="text-lg font-black text-white">100 / 100</div>
              <div class="text-[10px] text-slate-400">Aiming for Centum Grade</div>
            </div>

            <div class="bg-slate-800 border border-slate-700/80 rounded-2xl p-3 space-y-1">
              <div class="flex items-center justify-between text-slate-400 text-[11px]">
                <span>📊 Accuracy</span>
                <span class="text-emerald-400 font-bold">${accuracyPct}%</span>
              </div>
              <div class="text-lg font-black text-emerald-400">${accuracyPct}%</div>
              <div class="text-[10px] text-slate-400">${totalSolved} correct of ${totalAttempted} tried</div>
            </div>

            <div class="bg-slate-800 border border-slate-700/80 rounded-2xl p-3 space-y-1">
              <div class="flex items-center justify-between text-slate-400 text-[11px]">
                <span>🏆 Mastered</span>
                <span class="text-purple-400 font-bold">Active</span>
              </div>
              <div class="text-lg font-black text-white">${totalSolved} <span class="text-xs font-normal text-slate-400">Qs</span></div>
              <div class="text-[10px] text-slate-400">${totalMathQ} total in syllabus</div>
            </div>

            <div class="bg-slate-800 border border-slate-700/80 rounded-2xl p-3 space-y-1">
              <div class="flex items-center justify-between text-slate-400 text-[11px]">
                <span>🔥 Learning Streak</span>
                <span class="text-amber-400 font-bold">5 Days</span>
              </div>
              <div class="text-lg font-black text-amber-400">5 Days</div>
              <div class="text-[10px] text-slate-400">Consistent daily study</div>
            </div>
          </div>

          <!-- Admin Quick Access if Admin role is selected in top bar -->
          ${role === 'admin' ? `
            <div onclick="navTo('admin')" class="bg-gradient-to-r from-purple-900/80 to-indigo-900/80 border border-purple-500/40 rounded-2xl p-4 flex items-center justify-between cursor-pointer shadow-lg">
              <div>
                <div class="text-xs font-bold text-purple-200">🛡️ Admin Moderation & Ingestion Hub</div>
                <div class="text-[11px] text-purple-300/80">Bulk Ingest NCERT Q&A or Review Pending Submissions</div>
              </div>
              <span class="text-xs font-bold text-purple-300">Open Hub →</span>
            </div>
          ` : ''}

          <!-- "Resume Practice" Hero Card -->
          <div onclick="openChapterPractice('math_ch_01_real_numbers')" class="bg-gradient-to-r from-blue-900/90 via-indigo-900/80 to-blue-950 border border-blue-500/40 rounded-2xl p-4 flex items-center justify-between cursor-pointer hover:border-blue-400 active:scale-98 transition shadow-lg">
            <div class="space-y-1">
              <div class="flex items-center gap-1.5">
                <span class="text-xs font-bold text-blue-300">⚡ RESUME PRACTICE</span>
                <span class="text-[10px] bg-blue-500/20 px-2 py-0.5 rounded text-blue-200 font-bold">Recommended</span>
              </div>
              <div class="text-sm font-bold text-white">Ch 1: Real Numbers (ವಾಸ್ತವ ಸಂಖ್ಯೆಗಳು)</div>
              <div class="text-[11px] text-slate-300">Interactive step-by-step NCERT exercise solutions</div>
            </div>
            <button class="px-3 py-2 rounded-xl bg-blue-600 text-white font-bold text-xs shadow-md shrink-0">
              Start →
            </button>
          </div>

          <!-- Academic Subjects Section -->
          <div class="space-y-2 pt-1">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Core Subjects</span>
              <span class="text-[10px] text-slate-400">NCERT 2026</span>
            </div>

            <!-- Subject 1: Math -->
            <div onclick="navTo('math')" class="bg-slate-800 border border-slate-700 rounded-2xl p-3.5 flex items-center gap-3 active:scale-98 transition cursor-pointer hover:border-blue-500/50">
              <div class="w-11 h-11 rounded-xl bg-blue-500/20 border border-blue-500/30 flex items-center justify-center text-xl shrink-0">
                📐
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between">
                  <div class="text-sm font-bold text-white truncate">Mathematics • ಗಣಿತ</div>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 border border-blue-500/20">14 Chapters</span>
                </div>
                <div class="text-xs text-slate-400 mt-0.5 truncate">Bilingual Index • Practice Q&A • Formula Cheat-Sheets</div>
                <div class="w-full bg-slate-900 h-1.5 rounded-full mt-2 overflow-hidden">
                  <div class="bg-blue-500 h-full rounded-full" style="width: ${totalMathQ > 0 ? Math.round((totalSolved/totalMathQ)*100) : 0}%"></div>
                </div>
              </div>
              <span class="text-slate-500 text-sm">›</span>
            </div>

            <!-- Subject 2: Science -->
            <div onclick="navTo('science')" class="bg-slate-800 border border-slate-700 rounded-2xl p-3.5 flex items-center gap-3 active:scale-98 transition cursor-pointer hover:border-emerald-500/50">
              <div class="w-11 h-11 rounded-xl bg-emerald-500/20 border border-emerald-500/30 flex items-center justify-center text-xl shrink-0">
                🔬
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between">
                  <div class="text-sm font-bold text-white truncate">Science</div>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">NCERT</span>
                </div>
                <div class="text-xs text-slate-400 mt-0.5 truncate">Ray Diagrams • Equations • Flowcharts</div>
              </div>
              <span class="text-slate-500 text-sm">›</span>
            </div>

            <!-- Subject 3: Social Science -->
            <div onclick="navTo('sst')" class="bg-slate-800 border border-slate-700 rounded-2xl p-3.5 flex items-center gap-3 active:scale-98 transition cursor-pointer hover:border-amber-500/50">
              <div class="w-11 h-11 rounded-xl bg-amber-500/20 border border-amber-500/30 flex items-center justify-center text-xl shrink-0">
                🌍
              </div>
              <div class="flex-1 min-w-0">
                <div class="flex items-center justify-between">
                  <div class="text-sm font-bold text-white truncate">Social Science</div>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-500/10 text-amber-400 border border-amber-500/20">SST</span>
                </div>
                <div class="text-xs text-slate-400 mt-0.5 truncate">Nationalism Timelines • Map Guide • Civics</div>
              </div>
              <span class="text-slate-500 text-sm">›</span>
            </div>
          </div>

          <!-- Formula Quick-Hub Shortcuts -->
          <div class="space-y-2 pt-1">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">Formula Quick-Hub</span>
              <span class="text-[10px] text-emerald-400 font-bold">1-Tap Sheet</span>
            </div>
            <div class="grid grid-cols-2 gap-2">
              <button onclick="openChapterFormulas('math_ch_01_real_numbers')" class="p-2.5 rounded-xl bg-slate-800 border border-slate-700 hover:border-emerald-500/40 text-left active:scale-98 transition">
                <div class="text-[10px] text-emerald-400 font-bold">Ch 1 Formulas</div>
                <div class="text-xs font-bold text-white truncate">Real Numbers</div>
              </button>
              <button onclick="openChapterFormulas('math_ch_02_polynomials')" class="p-2.5 rounded-xl bg-slate-800 border border-slate-700 hover:border-emerald-500/40 text-left active:scale-98 transition">
                <div class="text-[10px] text-emerald-400 font-bold">Ch 2 Formulas</div>
                <div class="text-xs font-bold text-white truncate">Polynomials</div>
              </button>
              <button onclick="openChapterFormulas('math_ch_04_quadratic_equations')" class="p-2.5 rounded-xl bg-slate-800 border border-slate-700 hover:border-emerald-500/40 text-left active:scale-98 transition">
                <div class="text-[10px] text-emerald-400 font-bold">Ch 4 Formulas</div>
                <div class="text-xs font-bold text-white truncate">Quadratic Eq.</div>
              </button>
              <button onclick="openChapterFormulas('math_ch_05_arithmetic_progressions')" class="p-2.5 rounded-xl bg-slate-800 border border-slate-700 hover:border-emerald-500/40 text-left active:scale-98 transition">
                <div class="text-[10px] text-emerald-400 font-bold">Ch 5 Formulas</div>
                <div class="text-xs font-bold text-white truncate">Arithmetic Prog.</div>
              </button>
            </div>
          </div>
        `;
      }
      } else if (screen === 'math') {
        selectedChapterId = null;
        title.innerText = 'Mathematics • ಗಣಿತ';
        
        const totalMathQ = questions.filter(q => q.subject === 'math').length;
        const totalSolved = questions.filter(q => q.subject === 'math' && solvedQuestions.has(q.id)).length;
        const overallPercent = totalMathQ > 0 ? Math.round((totalSolved / totalMathQ) * 100) : 0;

        content.innerHTML = `
          <!-- Header Curriculum Overview -->
          <div class="bg-gradient-to-r from-blue-900 to-indigo-900 border border-blue-500/30 rounded-2xl p-4 space-y-2">
            <div class="flex justify-between items-center">
              <span class="text-xs font-bold text-blue-200">CBSE Class 10 Syllabus</span>
              <span class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-white/10 text-white">14 Chapters</span>
            </div>
            <div class="text-xs text-blue-300">${totalSolved} of ${totalMathQ} Questions Completed (${overallPercent}%)</div>
            <div class="w-full bg-black/30 h-1.5 rounded-full overflow-hidden">
              <div class="bg-emerald-400 h-full rounded-full transition-all" style="width: ${overallPercent}%"></div>
            </div>
          </div>

          <div class="text-xs font-bold text-slate-400 uppercase tracking-wider pt-2">All 14 Syllabus Chapters</div>

          <!-- 14 Chapters List -->
          <div class="space-y-2.5">
            ${mathChapters.map(ch => {
              const chQuestions = questions.filter(q => q.subject === 'math' && q.chapterId === ch.id);
              const qCount = chQuestions.length;
              const chSolved = chQuestions.filter(q => solvedQuestions.has(q.id)).length;
              const hasQ = qCount > 0;
              const pct = hasQ ? Math.round((chSolved / qCount) * 100) : 0;

              return `
                <div onclick="openChapterHub('${ch.id}')" class="bg-slate-800 border border-slate-700/80 rounded-2xl p-3.5 flex items-start gap-3 active:scale-98 transition cursor-pointer hover:border-blue-500/50">
                  <div class="w-9 h-9 rounded-xl bg-blue-500/10 border border-blue-500/30 flex items-center justify-center text-xs font-black text-blue-400 shrink-0">
                    ${ch.num < 10 ? '0' + ch.num : ch.num}
                  </div>
                  <div class="flex-1 min-w-0">
                    <div class="text-sm font-bold text-white truncate">${ch.titleEn}</div>
                    <div class="text-xs font-semibold text-slate-400 kannada-font truncate">${ch.titleKn}</div>
                    <div class="flex items-center gap-2 mt-2">
                      <span class="text-[10px] font-bold px-2 py-0.5 rounded ${hasQ ? 'bg-blue-500/20 text-blue-300' : 'bg-amber-500/20 text-amber-300'}">
                        ${hasQ ? qCount + ' Questions' : 'Seeding Soon'}
                      </span>
                      <span class="text-[10px] text-slate-400">${ch.formulas.length} Formulas</span>
                      ${hasQ && chSolved > 0 ? `
                        <span class="text-[10px] font-bold text-emerald-400 ml-auto">${chSolved}/${qCount} (${pct}%)</span>
                      ` : ''}
                    </div>
                  </div>
                  <span class="text-slate-500 text-sm mt-2">›</span>
                </div>
              `;
            }).join('')}
          </div>
        `;
      } else if (screen === 'chapter_hub') {
        const ch = mathChapters.find(c => c.id === selectedChapterId);
        if (!ch) return navTo('math');

        const chQuestions = questions.filter(q => q.subject === 'math' && q.chapterId === ch.id);
        const qCount = chQuestions.length;

        title.innerText = 'Ch ' + ch.num + ': ' + ch.titleEn;
        content.innerHTML = `
          <button onclick="navTo('math')" class="text-xs text-blue-400 font-bold flex items-center gap-1 mb-2">
            ← All Chapters
          </button>

          <!-- Chapter Header Card -->
          <div class="bg-slate-800 border border-slate-700 rounded-2xl p-4 space-y-2">
            <div class="flex items-center justify-between">
              <span class="text-[11px] font-bold px-2 py-0.5 rounded bg-blue-500/10 text-blue-400">Chapter ${ch.num}</span>
              <span class="text-xs text-slate-400">${qCount} Questions Available</span>
            </div>
            <div class="text-base font-bold text-white">${ch.titleEn}</div>
            <div class="text-xs font-semibold text-slate-300 kannada-font">${ch.titleKn}</div>
            <p class="text-xs text-slate-400 leading-relaxed">${ch.summary}</p>
          </div>

          <div class="text-xs font-bold text-slate-400 uppercase tracking-wider pt-2">Select Study Mode</div>

          <!-- Two Frictionless Options -->
          <div class="space-y-3">
            <!-- Option 1: Practice Questions -->
            <div onclick="openChapterPractice('${ch.id}')" class="bg-gradient-to-r from-blue-950/80 to-blue-900/60 border border-blue-500/40 rounded-2xl p-4 flex items-center gap-3 cursor-pointer hover:border-blue-400 active:scale-98 transition shadow">
              <div class="w-12 h-12 rounded-xl bg-blue-500/20 text-blue-300 flex items-center justify-center text-xl shrink-0">
                📝
              </div>
              <div class="flex-1">
                <div class="flex items-center justify-between">
                  <div class="text-sm font-bold text-white">Practice Questions & Solutions</div>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded ${qCount > 0 ? 'bg-blue-500/20 text-blue-300' : 'bg-amber-500/20 text-amber-300'}">
                    ${qCount > 0 ? qCount + ' Q&A' : 'Pending'}
                  </span>
                </div>
                <div class="text-xs text-blue-300/80 kannada-font">ಪ್ರಶ್ನೋತ್ತರಗಳ ಅಭ್ಯಾಸ</div>
                <div class="text-[11px] text-slate-400 mt-1">Interactive step-by-step solutions with instant feedback.</div>
              </div>
              <span class="text-blue-400 text-sm">›</span>
            </div>

            <!-- Option 2: Formula Cheat-Sheet -->
            <div onclick="openChapterFormulas('${ch.id}')" class="bg-gradient-to-r from-emerald-950/80 to-emerald-900/60 border border-emerald-500/40 rounded-2xl p-4 flex items-center gap-3 cursor-pointer hover:border-emerald-400 active:scale-98 transition shadow">
              <div class="w-12 h-12 rounded-xl bg-emerald-500/20 text-emerald-300 flex items-center justify-center text-xl shrink-0">
                ⚡
              </div>
              <div class="flex-1">
                <div class="flex items-center justify-between">
                  <div class="text-sm font-bold text-white">Chapter Formula Cheat-Sheet</div>
                  <span class="text-[10px] font-bold px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300">
                    ${ch.formulas.length} Formulas
                  </span>
                </div>
                <div class="text-xs text-emerald-300/80 kannada-font">ಸೂತ್ರಗಳ ಸಂಕ್ಷಿಪ್ತ ಪಟ್ಟಿ</div>
                <div class="text-[11px] text-slate-400 mt-1">All identities, definitions, and theorems in one place.</div>
              </div>
              <span class="text-emerald-400 text-sm">›</span>
            </div>
          </div>
        `;
      } else if (screen === 'chapter_practice') {
        const ch = mathChapters.find(c => c.id === selectedChapterId);
        if (!ch) return navTo('math');

        const chQuestions = questions.filter(q => q.subject === 'math' && q.chapterId === ch.id);
        title.innerText = ch.titleEn + ' • Practice';

        if (chQuestions.length === 0) {
          // Graceful Empty State
          content.innerHTML = `
            <div class="sticky -top-4 -mx-4 px-4 py-2 bg-slate-900/95 backdrop-blur border-b border-slate-800 flex items-center justify-between gap-2 z-20 shadow-sm mb-4">
              <button onclick="navTo('chapter_hub')" class="text-xs font-bold text-blue-400 flex items-center gap-1 py-1 px-2.5 rounded-xl bg-slate-800 border border-slate-700 active:scale-95 transition shrink-0">
                <span>←</span> <span>Hub</span>
              </button>
              <div class="text-xs font-bold text-white truncate text-center">
                ${ch.titleEn}
              </div>
              <span class="text-[10px] font-bold text-slate-400">0 Qs</span>
            </div>
            <div class="text-center py-10 px-4 space-y-4">
              <div class="w-16 h-16 mx-auto rounded-full bg-amber-500/10 border border-amber-500/30 flex items-center justify-center text-3xl">
                ⏳
              </div>
              <div class="text-base font-bold text-white">Question Bank Under Preparation</div>
              <p class="text-xs text-slate-400 max-w-sm mx-auto leading-relaxed">
                Faculty members are currently reviewing questions for <b>${ch.titleEn} (${ch.titleKn})</b>. Once approved by the admin, questions will appear here instantly!
              </p>
              <button onclick="openChapterFormulas('${ch.id}')" class="px-4 py-2.5 rounded-xl bg-emerald-600 font-bold text-white text-xs shadow-md">
                ⚡ View Formula Cheat-Sheet
              </button>
            </div>
          `;
        } else {
          // Detect exercises in this chapter
          const exercisesSet = new Set(['All']);
          chQuestions.forEach(q => {
            if (q.exercise) exercisesSet.add(q.exercise);
          });
          const exList = Array.from(exercisesSet);

          const displayed = activeExerciseFilter === 'All'
            ? chQuestions
            : chQuestions.filter(q => q.exercise === activeExerciseFilter);

          content.innerHTML = `
            <!-- Ultra-Clean, Space-Saving Top Bar for Mobile Practice -->
            <div class="sticky -top-4 -mx-4 px-4 py-2 bg-slate-900/95 backdrop-blur border-b border-slate-800 flex items-center justify-between gap-2 z-20 shadow-sm mb-1.5">
              <button onclick="navTo('chapter_hub')" class="text-xs font-bold text-blue-400 flex items-center gap-1 py-1 px-2.5 rounded-xl bg-slate-800 border border-slate-700 active:scale-95 transition shrink-0">
                <span>←</span> <span>Hub</span>
              </button>
              <div class="text-xs font-bold text-white truncate max-w-[170px] text-center">
                ${ch.titleEn}
              </div>
              <div class="text-[10px] font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/20 shrink-0">
                ${displayed.length} Qs
              </div>
            </div>

            ${exList.length > 1 ? `
              <div class="flex gap-1.5 py-1 overflow-x-auto no-scrollbar mb-1">
                ${exList.map(ex => {
                  const count = ex === 'All' ? chQuestions.length : chQuestions.filter(q => q.exercise === ex).length;
                  const isSel = activeExerciseFilter === ex;
                  return `
                    <button onclick="activeExerciseFilter = '${ex}'; navTo('chapter_practice');" class="px-2.5 py-1 rounded-lg text-[11px] font-semibold shrink-0 transition ${isSel ? 'bg-blue-600 text-white shadow-sm' : 'bg-slate-800 text-slate-400 border border-slate-700/60'}">
                      ${ex} (${count})
                    </button>
                  `;
                }).join('')}
              </div>
            ` : ''}

            <div class="space-y-2.5 pt-1">
              ${displayed.map((q, idx) => renderCard(q, idx + 1)).join('')}
            </div>
          `;
        }
      } else if (screen === 'chapter_formulas') {
        const ch = mathChapters.find(c => c.id === selectedChapterId);
        if (!ch) return navTo('math');

        title.innerText = ch.titleEn + ' • Formulas';
        content.innerHTML = `
          <!-- Compact Sticky Top Bar for Formulas -->
          <div class="sticky -top-4 -mx-4 px-4 py-2 bg-slate-900/95 backdrop-blur border-b border-slate-800 flex items-center justify-between gap-2 z-20 shadow-sm mb-3">
            <button onclick="navTo('chapter_hub')" class="text-xs font-bold text-blue-400 flex items-center gap-1 py-1 px-2.5 rounded-xl bg-slate-800 border border-slate-700 active:scale-95 transition shrink-0">
              <span>←</span> <span>Hub</span>
            </button>
            <div class="text-xs font-bold text-white truncate text-center">
              ${ch.titleEn} • Formulas
            </div>
            <span class="text-[10px] font-bold text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded-full border border-emerald-500/20 shrink-0">Ch ${ch.num}</span>
          </div>
          <div class="space-y-3">
            ${ch.formulas.map((f, i) => `
              <div class="bg-slate-800 border border-slate-700 rounded-2xl p-3.5 space-y-2">
                <div class="flex items-center justify-between text-xs">
                  <span class="font-bold text-emerald-400">Formula ${i + 1}</span>
                  <button onclick="navigator.clipboard.writeText('${f.replace(/'/g, "\\'")}'); alert('Formula copied!');" class="text-[10px] text-slate-400 hover:text-white">
                    Copy 📋
                  </button>
                </div>
                <div class="p-2.5 rounded-xl bg-slate-900 font-mono text-xs text-cyan-300 border border-slate-700/60 leading-relaxed">
                  ${f}
                </div>
              </div>
            `).join('')}
          </div>
        `;
      } else if (screen === 'science') {
        title.innerText = 'Science';
        content.innerHTML = `
          <div class="text-xs font-bold text-slate-400 uppercase mb-3">Physics, Chemistry & Biology</div>
          ${questions.filter(q => q.subject === 'science').map((q, idx) => renderCard(q, idx + 1)).join('')}
        `;
      } else if (screen === 'sst') {
        title.innerText = 'Social Science';
        content.innerHTML = `
          <div class="text-xs font-bold text-slate-400 uppercase mb-3">History, Geography & Civics</div>
          ${questions.filter(q => q.subject === 'sst').map((q, idx) => renderCard(q, idx + 1)).join('')}
        `;
      } else if (screen === 'admin') {
        title.innerText = 'Admin Hub';
        if (role !== 'admin') {
          content.innerHTML = `
            <div class="text-center py-12 space-y-3">
              <div class="text-4xl">🛡️</div>
              <div class="text-base font-bold text-white">Admin Privileges Required</div>
              <p class="text-xs text-slate-400 px-6">Supabase Row Level Security restricts content ingestion & approval strictly to <code>role = 'admin'</code>.</p>
              <button onclick="changeMobileRole('admin'); document.getElementById('role-select').value = 'admin';" class="px-4 py-2 rounded-xl bg-purple-600 text-white text-xs font-bold shadow">
                Switch to Admin Persona
              </button>
            </div>
          `;
        } else {
          content.innerHTML = `
            <!-- Admin Navigation Tabs (3 Choices) -->
            <div class="flex gap-1.5 border-b border-slate-700 pb-2 overflow-x-auto no-scrollbar">
              <button onclick="adminHubTab = 'pdf'; navTo('admin');" class="px-3 py-1.5 text-xs font-bold rounded-xl shrink-0 transition ${adminHubTab === 'pdf' ? 'bg-gradient-to-r from-blue-600 to-indigo-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                📄 Upload PDF & AI Extract
              </button>
              <button onclick="adminHubTab = 'pipeline'; navTo('admin');" class="px-3 py-1.5 text-xs font-bold rounded-xl shrink-0 transition ${adminHubTab === 'pipeline' ? 'bg-purple-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                🚀 Raw JSON Ingest
              </button>
              <button onclick="adminHubTab = 'queue'; navTo('admin');" class="px-3 py-1.5 text-xs font-bold rounded-xl shrink-0 transition ${adminHubTab === 'queue' ? 'bg-purple-600 text-white shadow' : 'bg-slate-800 text-slate-400'}">
                🛡️ Queue (${pending.length})
              </button>
            </div>

            ${adminHubTab === 'pdf' ? `
              <!-- PDF Upload & AI Q&A Generation Tab -->
              <div class="space-y-3.5 pt-2">
                <div class="bg-gradient-to-r from-blue-950/70 to-indigo-950/70 border border-blue-500/40 rounded-2xl p-3.5 space-y-1">
                  <div class="text-xs font-bold text-blue-200 flex items-center gap-1.5">
                    <span>✨</span> Automated NCERT PDF Parser & Q&A Generator
                  </div>
                  <div class="text-[11px] text-slate-300 leading-relaxed">
                    Upload an NCERT textbook chapter PDF. The AI engine extracts Exercises (e.g., Ex 2.1, 2.2), formats sub-questions, derives step-by-step proofs, and lets you publish live to students in one click.
                  </div>
                </div>

                <!-- 1. Target Chapter Selector -->
                <div class="space-y-1">
                  <label class="text-xs font-bold text-slate-300">1. Select Target Math Chapter:</label>
                  <select id="admin-pdf-target-ch" onchange="changeAdminTargetChapter(this.value);" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2.5 text-xs font-semibold text-white">
                    ${mathChapters.map(c => `
                      <option value="${c.id}" ${c.id === adminTargetChapterId ? 'selected' : ''}>Ch ${c.num}: ${c.titleEn} (${c.titleKn})</option>
                    `).join('')}
                  </select>
                </div>

                <!-- 2. Interactive PDF Upload Dropzone -->
                <div class="space-y-2">
                  <div class="flex justify-between items-center">
                    <label class="text-xs font-bold text-slate-300">2. Upload Textbook PDF Document:</label>
                    <span class="text-[10px] text-slate-400">PDF up to 50MB</span>
                  </div>

                  <input type="file" id="admin-pdf-file-input" accept=".pdf,application/pdf" style="display:none;" onchange="handleAdminPdfFileSelect(event)">

                  <div onclick="document.getElementById('admin-pdf-file-input').click()" class="border-2 border-dashed ${uploadedPdfFile ? 'border-emerald-500/60 bg-emerald-950/20' : 'border-slate-600 bg-slate-800/60'} rounded-2xl p-5 text-center cursor-pointer hover:border-blue-400 hover:bg-slate-800/80 transition space-y-2">
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
                      <div class="text-[10px] text-slate-400">NCERT Class 10 Textbook Reprint 2026-27 / State Syllabus</div>
                    `}
                  </div>

                  <!-- Quick Select Sample Catalog -->
                  <div class="space-y-1">
                    <div class="text-[10px] font-bold text-slate-400 uppercase tracking-wide">Preload from NCERT Textbook Catalog:</div>
                    <div class="flex gap-1.5 flex-wrap">
                      <button onclick="preloadCatalogPdf('math_ch_04_quadratic_equations')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'math_ch_04_quadratic_equations' && uploadedPdfFile ? 'border-blue-500 text-blue-300' : 'border-slate-700 text-slate-300'}">
                        📘 Ch 4: Quadratic Equations
                      </button>
                      <button onclick="preloadCatalogPdf('math_ch_03_linear_equations')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'math_ch_03_linear_equations' && uploadedPdfFile ? 'border-blue-500 text-blue-300' : 'border-slate-700 text-slate-300'}">
                        📘 Ch 3: Linear Equations
                      </button>
                      <button onclick="preloadCatalogPdf('math_ch_02_polynomials')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'math_ch_02_polynomials' && uploadedPdfFile ? 'border-blue-500 text-blue-300' : 'border-slate-700 text-slate-300'}">
                        📘 Ch 2: Polynomials
                      </button>
                      <button onclick="preloadCatalogPdf('math_ch_01_real_numbers')" class="px-2.5 py-1 rounded-lg text-[10px] font-semibold bg-slate-800 border ${adminTargetChapterId === 'math_ch_01_real_numbers' && uploadedPdfFile ? 'border-blue-500 text-blue-300' : 'border-slate-700 text-slate-300'}">
                        📘 Ch 1: Real Numbers
                      </button>
                    </div>
                  </div>
                </div>

                <!-- 3. Parse & Generate Action Button / Progress -->
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
                  <button onclick="startAdminPdfQaGeneration()" class="w-full py-3 rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-500 hover:to-indigo-500 font-bold text-white text-xs shadow-lg flex items-center justify-center gap-2 active:scale-98 transition">
                    <span>✨</span> Parse PDF & Generate Q&A
                  </button>
                `}

                <!-- 4. Extracted Questions Review & Direct Publish -->
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
                          Verified
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
                      <button onclick="publishPdfQuestionsLive('pending_review')" class="py-2.5 rounded-xl bg-slate-800 border border-amber-500/40 text-amber-300 hover:bg-amber-500/10 text-xs font-bold flex items-center justify-center gap-1 active:scale-98 transition">
                        🛡️ Moderate
                      </button>
                      <button onclick="clearAdminGeneratedMemory()" class="py-2.5 rounded-xl bg-slate-800 border border-rose-500/40 text-rose-300 hover:bg-rose-500/10 text-xs font-bold flex items-center justify-center gap-1 active:scale-98 transition" title="Clear memory for this chapter">
                        🗑️ Clear
                      </button>
                    </div>

                    <!-- Question Preview Cards -->
                    <div class="space-y-2.5 pt-1 max-h-[380px] overflow-y-auto pr-1">
                      ${pdfGeneratedQuestions.map((q, idx) => `
                        <div class="bg-slate-800 border border-slate-700 rounded-xl p-3 space-y-1.5 text-xs">
                          <div class="flex justify-between items-center text-[10px]">
                            <span class="font-bold text-blue-400 uppercase">${q.exercise} • Q${q.questionNumber || idx + 1}</span>
                            <span class="text-slate-400 capitalize">${q.difficulty}</span>
                          </div>
                          <div class="font-semibold text-white whitespace-pre-line">${q.text}</div>
                          <div class="text-[11px] text-slate-300 pl-2 border-l-2 border-emerald-500/50 space-y-0.5">
                            ${q.options.map(o => `
                              <div class="${o.is_correct ? 'text-emerald-400 font-bold' : 'text-slate-400'}">
                                ${o.id}. ${o.text} ${o.is_correct ? '✓' : ''}
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
            ` : adminHubTab === 'pipeline' ? `
              <!-- Direct Bulk Publisher Screen -->
              <div class="space-y-3 pt-2">
                <div class="bg-purple-950/40 border border-purple-500/40 rounded-2xl p-3.5 space-y-1">
                  <div class="text-xs font-bold text-purple-200">🚀 Direct-to-Student Feed Pipeline</div>
                  <div class="text-[11px] text-purple-300/80">Bulk-inserted questions immediately get <code>status = 'approved'</code> and populate student feeds.</div>
                </div>

                <div class="space-y-1">
                  <label class="text-xs font-bold text-slate-300">1. Select Target Math Chapter:</label>
                  <select id="admin-target-ch" class="w-full bg-slate-800 border border-slate-700 rounded-xl p-2.5 text-xs font-semibold text-white">
                    ${mathChapters.map(c => `
                      <option value="${c.id}" ${c.id === 'math_ch_01_real_numbers' ? 'selected' : ''}>Ch ${c.num}: ${c.titleEn} (${c.titleKn})</option>
                    `).join('')}
                  </select>
                </div>

                <div class="space-y-1">
                  <div class="flex justify-between items-center">
                    <label class="text-xs font-bold text-slate-300">2. Parsed Question JSON:</label>
                    <button onclick="loadSampleJsonInAdmin()" class="text-[10px] font-bold text-blue-400 bg-blue-500/10 px-2 py-0.5 rounded border border-blue-500/20">
                      Load Sample NCERT JSON
                    </button>
                  </div>
                  <textarea id="admin-json-input" rows="7" class="w-full bg-slate-900 border border-slate-700 rounded-xl p-2.5 font-mono text-[11px] text-slate-200" placeholder='[ { "text": "...", "options": [...] } ]'></textarea>
                </div>

                <button onclick="executeAdminBulkPublish()" class="w-full py-3 rounded-2xl bg-emerald-600 font-bold text-white text-xs shadow-lg hover:bg-emerald-500 active:scale-98 transition">
                  🚀 Publish Directly to Student Feed
                </button>
              </div>
            ` : `
              <!-- Moderation Queue -->
              <div class="space-y-3 pt-2">
                <div class="text-xs font-bold text-purple-300">Pending Review Queue (${pending.length})</div>
                ${pending.length === 0 ? '<div class="text-xs text-slate-400 py-6 text-center">All queued items have been moderated!</div>' : pending.map((p, idx) => `
                  <div class="bg-slate-800 border border-amber-500/40 rounded-2xl p-4 space-y-2">
                    <div class="text-[10px] font-bold text-amber-400 uppercase">${p.chapter} • ${p.difficulty}</div>
                    <div class="text-xs font-bold text-white">${p.text}</div>
                    <div class="flex gap-2 pt-2">
                      <button onclick="approveQueueItem(${idx});" class="flex-1 py-1.5 rounded-xl bg-emerald-600 text-white text-xs font-bold">Approve</button>
                      <button onclick="rejectQueueItem(${idx});" class="px-3 py-1.5 rounded-xl bg-rose-600 text-white text-xs font-bold">Reject</button>
                    </div>
                  </div>
                `).join('')}
              </div>
            `}`;
        }
      }
    }

    function openChapterHub(chapterId) {
      selectedChapterId = chapterId;
      navTo('chapter_hub');
    }

    function openChapterPractice(chapterId) {
      selectedChapterId = chapterId;
      activeExerciseFilter = 'All';
      navTo('chapter_practice');
    }

    function openChapterFormulas(chapterId) {
      selectedChapterId = chapterId;
      navTo('chapter_formulas');
    }

    function attemptQuestion(qId, optionId) {
      // ANTI-CHEATING UX RULE: If this question was already attempted, choices are locked!
      if (userSelectedOptions[qId] !== undefined) {
        alert("⚠️ Answer already recorded! You cannot change your choice directly. Tap '↺ Reset' at the top right to clear your choice and re-attempt.");
        return;
      }
      userSelectedOptions[qId] = optionId;
      const q = questions.find(item => item.id === qId);
      if (q && q.options) {
        const opt = q.options.find(o => o.id === optionId);
        if (opt && (opt.correct || opt.is_correct)) {
          solvedQuestions.add(qId);
        } else {
          solvedQuestions.delete(qId);
        }
      }
      navTo(currentTab);
    }

    function toggleSolution(qId) {
      const selected = userSelectedOptions[qId];
      if (!selected) {
        alert('⚠️ Please select an option first before revealing the step-by-step solution!');
        return;
      }
      const solEl = document.getElementById('sol-' + qId);
      const btnEl = document.getElementById('sol-btn-' + qId);
      if (solEl) {
        solEl.classList.toggle('hidden');
        const isHidden = solEl.classList.contains('hidden');
        if (btnEl) {
          btnEl.innerHTML = isHidden 
            ? '<span>💡</span> <span>Reveal Step-by-Step Solution</span>' 
            : '<span>🙈</span> <span>Hide Step-by-Step Solution</span>';
        }
        if (!isHidden) {
          setTimeout(() => {
            solEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
          }, 60);
        }
      }
    }

    function resetQuestionAttempt(qId) {
      delete userSelectedOptions[qId];
      solvedQuestions.delete(qId);
      navTo(currentTab);
    }

    function renderCard(q, index) {
      const selectedOptionId = userSelectedOptions[q.id];
      const isAttempted = selectedOptionId !== undefined;
      const isSolved = solvedQuestions.has(q.id);

      return `
        <div class="bg-slate-800 border ${isAttempted ? (isSolved ? 'border-emerald-500/50' : 'border-rose-500/50') : 'border-slate-700'} rounded-2xl p-3.5 space-y-1.5 mb-2.5 transition shadow">
          <div class="flex justify-between items-center text-[10px] font-bold">
            <span class="text-blue-400 uppercase">${q.exercise ? q.exercise + ' • ' : ''}Q${index || 1} • ${q.difficulty || 'standard'}</span>
            <div class="flex items-center gap-1.5">
              ${isAttempted ? `
                ${isSolved 
                  ? '<span class="text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/30">✓ Correct Choice</span>' 
                  : '<span class="text-rose-400 bg-rose-500/10 px-2 py-0.5 rounded border border-rose-500/30">✗ Incorrect Attempt</span>'
                }
                <button onclick="resetQuestionAttempt('${q.id}')" title="Reset and try again" class="text-amber-300 hover:text-white px-2 py-0.5 rounded bg-amber-500/20 border border-amber-500/40 text-[10px] font-bold flex items-center gap-1 active:scale-95 transition">
                  <span>↺ Reset</span>
                </button>
              ` : (isSolved ? '<span class="text-emerald-400 bg-emerald-500/10 px-2 py-0.5 rounded border border-emerald-500/20">✓ Solved</span>' : '')}
            </div>
          </div>
          <div class="text-xs font-semibold text-white whitespace-pre-line leading-snug">${q.text}</div>
          <div class="space-y-1 pt-0.5">
            ${q.options.map(o => {
              const isCorrect = Boolean(o.correct || o.is_correct);
              const isSelected = selectedOptionId === o.id;

              let containerStyle = "p-2 rounded-xl text-xs flex justify-between items-center transition ";
              let feedbackBadge = "";

              if (!isAttempted) {
                // Default unattempted state: Neutral slate, NO green tick, NO red mark, clickable
                containerStyle += "bg-slate-900 border border-slate-700/60 text-slate-200 hover:border-blue-500/50 hover:bg-slate-800/60 cursor-pointer";
              } else {
                // Attempted state: Option choices are strictly locked!
                if (isSelected && isCorrect) {
                  // User chose correctly
                  containerStyle += "bg-emerald-950/40 border-2 border-emerald-500 text-emerald-100 font-medium cursor-default";
                  feedbackBadge = '<span class="text-emerald-400 font-bold flex items-center gap-1"><span>✓</span> <span>Correct!</span></span>';
                } else if (isSelected && !isCorrect) {
                  // User chose incorrectly
                  containerStyle += "bg-rose-950/40 border-2 border-rose-500 text-rose-100 font-medium cursor-default";
                  feedbackBadge = '<span class="text-rose-400 font-bold flex items-center gap-1"><span>✗</span> <span>Your Choice</span></span>';
                } else if (!isSelected && isCorrect) {
                  // Reveal correct answer when user guessed wrong
                  containerStyle += "bg-emerald-950/20 border border-emerald-500/60 text-emerald-200 cursor-not-allowed opacity-90";
                  feedbackBadge = '<span class="text-emerald-400 font-semibold text-[10px] flex items-center gap-1"><span>✓</span> <span>Correct Answer</span></span>';
                } else {
                  // Other unselected wrong options
                  containerStyle += "bg-slate-900/50 border border-slate-800 text-slate-500 opacity-50 cursor-not-allowed";
                }
              }

              return `
                <div onclick="attemptQuestion('${q.id}', '${o.id}')" class="${containerStyle}">
                  <span><b>${o.id}.</b> ${o.text}</span>
                  ${feedbackBadge}
                </div>
              `;
            }).join('')}
          </div>
          ${isAttempted ? `
            <button id="sol-btn-${q.id}" onclick="toggleSolution('${q.id}')" class="w-full mt-1.5 py-2 rounded-xl border border-blue-500/40 bg-blue-500/10 text-blue-300 text-xs font-bold hover:bg-blue-500/20 active:scale-98 transition flex items-center justify-center gap-1.5 shadow-sm">
              <span>💡</span> <span>Reveal Step-by-Step Solution</span>
            </button>
          ` : `
            <button onclick="toggleSolution('${q.id}')" class="w-full mt-1.5 py-2 rounded-xl border border-slate-700 bg-slate-900/60 text-slate-400 text-xs font-medium hover:border-slate-600 transition flex items-center justify-center gap-1.5 opacity-70 cursor-not-allowed">
              <span>🔒</span> <span>Select an option above to unlock solution</span>
            </button>
          `}
          <div id="sol-${q.id}" class="hidden p-3 rounded-xl bg-slate-950/90 border border-slate-700/80 font-mono text-[11px] leading-relaxed text-cyan-300 whitespace-pre-line mt-2">
            ${q.solution || q.step_by_step_solution || ''}
          </div>
        </div>
      `;
    }

    function loadSampleJsonInAdmin() {
      const sample = [
        {
          "text": "An army contingent of 616 members is to march behind an army band of 32 members in a parade. What is the maximum number of columns in which they can march?",
          "difficulty": "medium",
          "options": [
            { "id": "A", "text": "4 columns", "correct": false },
            { "id": "B", "text": "8 columns", "correct": true },
            { "id": "C", "text": "16 columns", "correct": false },
            { "id": "D", "text": "32 columns", "correct": false }
          ],
          "solution": "Step 1: Maximum number of columns is HCF(616, 32).\nStep 2: 32 = 2⁵; 616 = 2³ × 7 × 11.\nStep 3: Common factor with least power = 2³ = 8 columns."
        }
      ];
      document.getElementById('admin-json-input').value = JSON.stringify(sample, null, 2);
    }

    function executeAdminBulkPublish() {
      const chId = document.getElementById('admin-target-ch').value;
      const raw = document.getElementById('admin-json-input').value;
      if (!raw.trim()) {
        alert('Please paste question JSON or click Load Sample.');
        return;
      }

      try {
        const parsed = JSON.parse(raw);
        parsed.forEach((item, i) => {
          questions.unshift({
            id: 'pub-' + Date.now() + '-' + i,
            subject: 'math',
            chapterId: chId,
            difficulty: item.difficulty || 'medium',
            text: item.text,
            options: item.options,
            solution: item.solution
          });
        });

        alert('Published ' + parsed.length + ' approved questions directly to ' + chId + '!');
        navTo('math');
      } catch (e) {
        alert('Invalid JSON: ' + e);
      }
    }

    
    // -------------------------------------------------------------
    // PDF UPLOAD & AUTOMATED Q&A GENERATION HANDLERS
    // -------------------------------------------------------------
    function handleAdminPdfFileSelect(event) {
      const file = event.target.files && event.target.files[0];
      if (!file) return;
      uploadedPdfFile = {
        name: file.name,
        size: (file.size / (1024 * 1024)).toFixed(2) + ' MB',
        preloaded: false
      };
      // CRITICAL: Clear memory on new file upload!
      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      navTo('admin');
    }

    function changeAdminTargetChapter(chId) {
      adminTargetChapterId = chId;
      // Default: Keep PDF attachment clear as requested
      uploadedPdfFile = null;
      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      navTo('admin');
    }

    function preloadCatalogPdf(chId) {
      adminTargetChapterId = chId;
      const ch = mathChapters.find(c => c.id === chId) || mathChapters[0];
      uploadedPdfFile = {
        name: `ncert_class10_${ch.id}.pdf`,
        size: '2.45 MB',
        preloaded: true
      };
      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      navTo('admin');
    }

    function removeAdminAttachedPdf() {
      uploadedPdfFile = null;
      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      navTo('admin');
    }

    function selectPreloadedChapterPdf(chId) {
      preloadCatalogPdf(chId);
    }

    function clearAdminGeneratedMemory() {
      pdfGeneratedQuestions = [];
      pdfGenerationProgress = 0;
      pdfGenerationStatusText = '';
      alert('🧹 Cleared generated Q&A memory for this chapter.');
      navTo('admin');
    }

    function startAdminPdfQaGeneration() {
      if (!uploadedPdfFile) {
        alert('Please select or drop a textbook PDF document first.');
        return;
      }

      pdfGenerating = true;
      pdfGenerationProgress = 15;
      pdfGenerationStatusText = 'Reading textbook PDF document pages...';
      navTo('admin');

      setTimeout(() => {
        pdfGenerationProgress = 55;
        pdfGenerationStatusText = 'Extracting Exercise and In-Text question blocks...';
        navTo('admin');

        setTimeout(() => {
          pdfGenerationProgress = 88;
          pdfGenerationStatusText = 'Deriving step-by-step mathematical proofs & solutions...';
          navTo('admin');

          setTimeout(() => {
            pdfGenerating = false;
            pdfGenerationProgress = 100;
            pdfGeneratedQuestions = generateSampleQuestionsForChapter(adminTargetChapterId);
            navTo('admin');
          }, 400);
        }, 400);
      }, 400);
    }

    
    const ch3SampleQuestions = [
  {
    "id": "10000000-0000-0000-0003-000000000001",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "1(i)",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q1(i)] Form the pair of linear equations and find their solutions graphically:\n10 students of Class X took part in a Mathematics quiz. If the number of girls is 4 more than the number of boys, find the number of boys and girls who took part in the quiz.",
    "options": [
      {
        "id": "A",
        "text": "Boys = 3, Girls = 7",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Boys = 4, Girls = 6",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Boys = 2, Girls = 8",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Boys = 5, Girls = 5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let number of boys = x, girls = y.\nStep 2: Total: x + y = 10 ... (1)\nStep 3: Girls 4 more than boys: y = x + 4 => y - x = 4 ... (2)\nStep 4: Solving gives 2x = 6 => x = 3, y = 7.\nHence, 3 boys and 7 girls took part in the quiz."
  },
  {
    "id": "10000000-0000-0000-0003-000000000002",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "1(ii)",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q1(ii)] Form the pair of linear equations and find their solutions graphically:\n5 pencils and 7 pens together cost ₹ 50, whereas 7 pencils and 5 pens together cost ₹ 46. Find the cost of one pencil and that of one pen.",
    "options": [
      {
        "id": "A",
        "text": "Cost of 1 pencil = ₹ 3, Cost of 1 pen = ₹ 5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Cost of 1 pencil = ₹ 5, Cost of 1 pen = ₹ 3",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Cost of 1 pencil = ₹ 2, Cost of 1 pen = ₹ 6",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Cost of 1 pencil = ₹ 4, Cost of 1 pen = ₹ 4",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let 1 pencil = ₹ x, 1 pen = ₹ y.\nStep 2: 5x + 7y = 50 ... (1) and 7x + 5y = 46 ... (2).\nStep 3: Multiplying (1) by 7 and (2) by 5 yields 35x + 49y = 350 and 35x + 25y = 230.\nStep 4: Subtracting gives 24y = 120 => y = 5.\nStep 5: 5x + 35 = 50 => 5x = 15 => x = 3.\nCost of 1 pencil = ₹ 3, cost of 1 pen = ₹ 5."
  },
  {
    "id": "10000000-0000-0000-0003-000000000003",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "2(i)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q2(i)] On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the lines representing the following pair intersect at a point, are parallel or coincident:\n5x – 4y + 8 = 0\n7x + 6y – 9 = 0",
    "options": [
      {
        "id": "A",
        "text": "Intersect at a point (Unique solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Parallel lines (No solution)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident lines (Infinitely many solutions)",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Inconsistent lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁ = 5, b₁ = -4, c₁ = 8 and a₂ = 7, b₂ = 6, c₂ = -9.\nStep 2: a₁/a₂ = 5/7; b₁/b₂ = -4/6 = -2/3.\nStep 3: Since a₁/a₂ ≠ b₁/b₂ (5/7 ≠ -2/3), the lines intersect at a point."
  },
  {
    "id": "10000000-0000-0000-0003-000000000004",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "2(ii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q2(ii)] On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the lines representing the following pair intersect at a point, are parallel or coincident:\n9x + 3y + 12 = 0\n18x + 6y + 24 = 0",
    "options": [
      {
        "id": "A",
        "text": "Coincident lines (Infinitely many solutions)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Parallel lines",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Intersect at a single point",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Inconsistent lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = 9/18 = 1/2; b₁/b₂ = 3/6 = 1/2; c₁/c₂ = 12/24 = 1/2.\nStep 2: Since a₁/a₂ = b₁/b₂ = c₁/c₂ = 1/2, the lines are coincident."
  },
  {
    "id": "10000000-0000-0000-0003-000000000005",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "2(iii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q2(iii)] On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the lines representing the following pair intersect at a point, are parallel or coincident:\n6x – 3y + 10 = 0\n2x – y + 9 = 0",
    "options": [
      {
        "id": "A",
        "text": "Parallel lines (No solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Intersecting lines",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident lines",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Consistent lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = 6/2 = 3; b₁/b₂ = -3/(-1) = 3; c₁/c₂ = 10/9.\nStep 2: Since a₁/a₂ = b₁/b₂ ≠ c₁/c₂ (3 = 3 ≠ 10/9), the lines are parallel."
  },
  {
    "id": "10000000-0000-0000-0003-000000000006",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "3(i)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q3(i)] On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the following pair is consistent, or inconsistent:\n3x + 2y = 5\n2x – 3y = 7",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Unique solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent (No solution)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Dependent consistent",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Parallel",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = 3/2; b₁/b₂ = 2/(-3) = -2/3.\nStep 2: Since a₁/a₂ ≠ b₁/b₂ (3/2 ≠ -2/3), the pair has a unique solution and is consistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000007",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "3(ii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q3(ii)] On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the following pair is consistent, or inconsistent:\n2x – 3y = 8\n4x – 6y = 9",
    "options": [
      {
        "id": "A",
        "text": "Inconsistent (No solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Consistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Infinitely many solutions",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = 2/4 = 1/2; b₁/b₂ = -3/(-6) = 1/2; c₁/c₂ = 8/9.\nStep 2: Since a₁/a₂ = b₁/b₂ ≠ c₁/c₂ (1/2 = 1/2 ≠ 8/9), the lines are parallel and inconsistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000008",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "3(iii)",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q3(iii)] On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the pair is consistent or inconsistent:\n(3/2)x + (5/3)y = 7\n9x – 10y = 14",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Unique solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Parallel",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = (3/2)/9 = 1/6; b₁/b₂ = (5/3)/(-10) = -1/6.\nStep 2: Since a₁/a₂ ≠ b₁/b₂ (1/6 ≠ -1/6), the pair is consistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000009",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "3(iv)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q3(iv)] On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the pair is consistent or inconsistent:\n5x – 3y = 11\n–10x + 6y = –22",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Coincident lines, infinitely many solutions)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Unique solution",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Parallel lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = 5/(-10) = -1/2; b₁/b₂ = -3/6 = -1/2; c₁/c₂ = 11/(-22) = -1/2.\nStep 2: Since a₁/a₂ = b₁/b₂ = c₁/c₂ = -1/2, the pair is consistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000010",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "3(v)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q3(v)] On comparing the ratios a₁/a₂, b₁/b₂ and c₁/c₂, find out whether the pair is consistent or inconsistent:\n(4/3)x + 2y = 8\n2x + 3y = 12",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Coincident lines, dependent)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Parallel lines",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Unique solution",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = (4/3)/2 = 2/3; b₁/b₂ = 2/3; c₁/c₂ = 8/12 = 2/3.\nStep 2: Since a₁/a₂ = b₁/b₂ = c₁/c₂ = 2/3, the pair of equations is consistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000011",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "4(i)",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q4(i)] Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:\nx + y = 5\n2x + 2y = 10",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Coincident lines, infinitely many solutions)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent (No solution)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Unique solution: x = 5, y = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Parallel lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = 1/2; b₁/b₂ = 1/2; c₁/c₂ = 5/10 = 1/2.\nStep 2: a₁/a₂ = b₁/b₂ = c₁/c₂ = 1/2 => consistent with infinitely many solutions.\nStep 3: Graphically, both lines coincide through (0, 5) and (5, 0)."
  },
  {
    "id": "10000000-0000-0000-0003-000000000012",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "4(ii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q4(ii)] Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:\nx – y = 8\n3x – 3y = 16",
    "options": [
      {
        "id": "A",
        "text": "Inconsistent (Parallel lines, no solution)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Consistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Unique solution",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Coincident lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = 1/3; b₁/b₂ = -1/(-3) = 1/3; c₁/c₂ = 8/16 = 1/2.\nStep 2: Since a₁/a₂ = b₁/b₂ ≠ c₁/c₂ (1/3 = 1/3 ≠ 1/2), the lines are parallel and inconsistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000013",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "4(iii)",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q4(iii)] Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:\n2x + y – 6 = 0\n4x – 2y – 4 = 0",
    "options": [
      {
        "id": "A",
        "text": "Consistent (Unique solution: x = 2, y = 2)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Inconsistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident lines",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Parallel lines",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = 2/4 = 1/2; b₁/b₂ = 1/(-2) = -1/2.\nStep 2: Since a₁/a₂ ≠ b₁/b₂, the pair is consistent with a unique solution.\nStep 3: Graphing gives intersection at point (2, 2). Hence, x = 2, y = 2."
  },
  {
    "id": "10000000-0000-0000-0003-000000000014",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "4(iv)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q4(iv)] Which of the following pairs of linear equations are consistent/inconsistent? If consistent, obtain the solution graphically:\n2x – 2y – 2 = 0\n4x – 4y – 5 = 0",
    "options": [
      {
        "id": "A",
        "text": "Inconsistent (Parallel lines)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Consistent",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Coincident lines",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Unique solution",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a₁/a₂ = 2/4 = 1/2; b₁/b₂ = -2/(-4) = 1/2; c₁/c₂ = -2/(-5) = 2/5.\nStep 2: a₁/a₂ = b₁/b₂ ≠ c₁/c₂ (1/2 = 1/2 ≠ 2/5) => Inconsistent."
  },
  {
    "id": "10000000-0000-0000-0003-000000000015",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "5",
    "difficulty": "medium",
    "text": "[Exercise 3.1 - Q5] Half the perimeter of a rectangular garden, whose length is 4 m more than its width, is 36 m. Find the dimensions of the garden.",
    "options": [
      {
        "id": "A",
        "text": "Length = 20 m, Width = 16 m",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Length = 24 m, Width = 12 m",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Length = 18 m, Width = 14 m",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Length = 22 m, Width = 14 m",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let length = x m, width = y m.\nStep 2: x = y + 4 => x - y = 4 ... (1)\nStep 3: Half perimeter: x + y = 36 ... (2)\nStep 4: Adding gives 2x = 40 => x = 20 m.\nStep 5: y = 36 - 20 = 16 m. Dimensions: Length = 20 m, Width = 16 m."
  },
  {
    "id": "10000000-0000-0000-0003-000000000016",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "6(i)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q6(i)] Given the linear equation 2x + 3y – 8 = 0, write another linear equation in two variables such that the geometrical representation of the pair so formed is intersecting lines.",
    "options": [
      {
        "id": "A",
        "text": "3x + 2y – 7 = 0 (or any equation where a₁/a₂ ≠ b₁/b₂)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "4x + 6y – 16 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "2x + 3y – 12 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "4x + 6y – 9 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Intersecting lines condition: a₁/a₂ ≠ b₁/b₂.\nStep 2: Given 2x + 3y - 8 = 0. Choosing a₂ = 3, b₂ = 2 gives 2/3 ≠ 3/2.\nStep 3: A valid equation is 3x + 2y - 7 = 0."
  },
  {
    "id": "10000000-0000-0000-0003-000000000017",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "6(ii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q6(ii)] Given the linear equation 2x + 3y – 8 = 0, write another linear equation in two variables such that the geometrical representation of the pair so formed is parallel lines.",
    "options": [
      {
        "id": "A",
        "text": "4x + 6y – 9 = 0 (or any equation where a₁/a₂ = b₁/b₂ ≠ c₁/c₂)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "4x + 6y – 16 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "3x + 2y – 8 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x + y – 4 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Parallel lines condition: a₁/a₂ = b₁/b₂ ≠ c₁/c₂.\nStep 2: Multiply coefficients of x and y by 2: 4x + 6y.\nStep 3: Choose c₂ ≠ -16, e.g. -9. Equation: 4x + 6y - 9 = 0."
  },
  {
    "id": "10000000-0000-0000-0003-000000000018",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "6(iii)",
    "difficulty": "easy",
    "text": "[Exercise 3.1 - Q6(iii)] Given the linear equation 2x + 3y – 8 = 0, write another linear equation in two variables such that the geometrical representation of the pair so formed is coincident lines.",
    "options": [
      {
        "id": "A",
        "text": "4x + 6y – 16 = 0 (or any scalar multiple k(2x + 3y – 8) = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "4x + 6y – 8 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "2x + 3y + 8 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "3x + 2y – 8 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Coincident lines condition: a₁/a₂ = b₁/b₂ = c₁/c₂.\nStep 2: Multiply equation by 2: 2(2x + 3y - 8) = 4x + 6y - 16 = 0."
  },
  {
    "id": "10000000-0000-0000-0003-000000000019",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.1",
    "questionNumber": "7",
    "difficulty": "hard",
    "text": "[Exercise 3.1 - Q7] Draw the graphs of the equations x – y + 1 = 0 and 3x + 2y – 12 = 0. Determine the coordinates of the vertices of the triangle formed by these lines and the x-axis, and shade the triangular region.",
    "options": [
      {
        "id": "A",
        "text": "Vertices: (-1, 0), (4, 0), and (2, 3)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Vertices: (1, 0), (4, 0), and (3, 2)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Vertices: (-1, 0), (3, 0), and (2, 4)",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Vertices: (0, 1), (0, 6), and (2, 3)",
        "is_correct": false
      }
    ],
    "solution": "Step 1: For x - y + 1 = 0, x-intercept is (-1, 0).\nStep 2: For 3x + 2y - 12 = 0, x-intercept is (4, 0).\nStep 3: Point of intersection of the lines is (2, 3).\nStep 4: Vertices formed with the x-axis are (-1, 0), (4, 0), and (2, 3)."
  },
  {
    "id": "10000000-0000-0000-0003-000000000020",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 3.2 - Q1(i)] Solve the following pair of linear equations by the substitution method:\nx + y = 14\nx – y = 4",
    "options": [
      {
        "id": "A",
        "text": "x = 9, y = 5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 5, y = 9",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 10, y = 4",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 8, y = 6",
        "is_correct": false
      }
    ],
    "solution": "Step 1: From (2), x = y + 4.\nStep 2: In (1): (y + 4) + y = 14 => 2y = 10 => y = 5.\nStep 3: x = 5 + 4 = 9. Solution: x = 9, y = 5."
  },
  {
    "id": "10000000-0000-0000-0003-000000000021",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(ii)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q1(ii)] Solve the following pair of linear equations by the substitution method:\ns – t = 3\n(s/3) + (t/2) = 6",
    "options": [
      {
        "id": "A",
        "text": "s = 9, t = 6",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "s = 6, t = 9",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "s = 8, t = 5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "s = 7, t = 4",
        "is_correct": false
      }
    ],
    "solution": "Step 1: s = t + 3.\nStep 2: Multiply second equation by 6: 2s + 3t = 36.\nStep 3: 2(t + 3) + 3t = 36 => 5t = 30 => t = 6.\nStep 4: s = 6 + 3 = 9. Solution: s = 9, t = 6."
  },
  {
    "id": "10000000-0000-0000-0003-000000000022",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(iii)",
    "difficulty": "easy",
    "text": "[Exercise 3.2 - Q1(iii)] Solve the following pair of linear equations by the substitution method:\n3x – y = 3\n9x – 3y = 9",
    "options": [
      {
        "id": "A",
        "text": "Infinitely many solutions (y = 3x – 3)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No solution",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Unique solution: x = 1, y = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 3, y = 6",
        "is_correct": false
      }
    ],
    "solution": "Step 1: y = 3x - 3.\nStep 2: In (2): 9x - 3(3x - 3) = 9 => 9 = 9.\nStep 3: True statement for all x. Infinitely many solutions with y = 3x - 3."
  },
  {
    "id": "10000000-0000-0000-0003-000000000023",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(iv)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q1(iv)] Solve the following pair of linear equations by the substitution method:\n0.2x + 0.3y = 1.3\n0.4x + 0.5y = 2.3",
    "options": [
      {
        "id": "A",
        "text": "x = 2, y = 3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 3, y = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 1, y = 4",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 2.5, y = 2.5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply by 10: 2x + 3y = 13 and 4x + 5y = 23.\nStep 2: x = (13 - 3y)/2.\nStep 3: 4((13 - 3y)/2) + 5y = 23 => 26 - 6y + 5y = 23 => y = 3.\nStep 4: x = (13 - 9)/2 = 2. Solution: x = 2, y = 3."
  },
  {
    "id": "10000000-0000-0000-0003-000000000024",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(v)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q1(v)] Solve the following pair of linear equations by the substitution method:\n√2 x + √3 y = 0\n√3 x – √8 y = 0",
    "options": [
      {
        "id": "A",
        "text": "x = 0, y = 0",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = √2, y = √3",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 1, y = 1",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Infinitely many solutions",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x = (-√3/√2)y.\nStep 2: In (2): √3((-√3/√2)y) - √8 y = 0 => (-7/√2)y = 0 => y = 0.\nStep 3: x = 0. Solution: x = 0, y = 0."
  },
  {
    "id": "10000000-0000-0000-0003-000000000025",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "1(vi)",
    "difficulty": "hard",
    "text": "[Exercise 3.2 - Q1(vi)] Solve the following pair of linear equations by the substitution method:\n(3/2)x – (5/3)y = –2\n(x/3) + (y/2) = 13/6",
    "options": [
      {
        "id": "A",
        "text": "x = 2, y = 3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 3, y = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = -2, y = -3",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1, y = 2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply by 6: 9x - 10y = -12 and 2x + 3y = 13.\nStep 2: x = (13 - 3y)/2.\nStep 3: 9((13 - 3y)/2) - 10y = -12 => 117 - 47y = -24 => -47y = -141 => y = 3.\nStep 4: x = (13 - 9)/2 = 2. Solution: x = 2, y = 3."
  },
  {
    "id": "10000000-0000-0000-0003-000000000026",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "2",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q2] Solve 2x + 3y = 11 and 2x – 4y = –24 and hence find the value of 'm' for which y = mx + 3.",
    "options": [
      {
        "id": "A",
        "text": "x = -2, y = 5; m = -1",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 2, y = 5; m = 1",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = -2, y = 4; m = -2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1, y = 3; m = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: 2x = 11 - 3y.\nStep 2: (11 - 3y) - 4y = -24 => -7y = -35 => y = 5.\nStep 3: 2x = 11 - 15 = -4 => x = -2.\nStep 4: y = mx + 3 => 5 = m(-2) + 3 => 2 = -2m => m = -1."
  },
  {
    "id": "10000000-0000-0000-0003-000000000027",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(i)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q3(i)] The difference between two numbers is 26 and one number is three times the other. Find them.",
    "options": [
      {
        "id": "A",
        "text": "39 and 13",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "36 and 10",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "42 and 16",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "30 and 4",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x - y = 26 and x = 3y.\nStep 2: 3y - y = 26 => 2y = 26 => y = 13.\nStep 3: x = 3(13) = 39. Numbers are 39 and 13."
  },
  {
    "id": "10000000-0000-0000-0003-000000000028",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(ii)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q3(ii)] The larger of two supplementary angles exceeds the smaller by 18 degrees. Find them.",
    "options": [
      {
        "id": "A",
        "text": "99° and 81°",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "100° and 80°",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "108° and 72°",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "95° and 85°",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x + y = 180 and x = y + 18.\nStep 2: (y + 18) + y = 180 => 2y = 162 => y = 81°.\nStep 3: x = 81 + 18 = 99°. Angles are 99° and 81°."
  },
  {
    "id": "10000000-0000-0000-0003-000000000029",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(iii)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q3(iii)] The coach of a cricket team buys 7 bats and 6 balls for ₹ 3800. Later, she buys 3 bats and 5 balls for ₹ 1750. Find the cost of each bat and each ball.",
    "options": [
      {
        "id": "A",
        "text": "Bat = ₹ 500, Ball = ₹ 50",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Bat = ₹ 450, Ball = ₹ 70",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Bat = ₹ 520, Ball = ₹ 40",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Bat = ₹ 400, Ball = ₹ 60",
        "is_correct": false
      }
    ],
    "solution": "Step 1: 7x + 6y = 3800 and 3x + 5y = 1750.\nStep 2: x = (1750 - 5y)/3.\nStep 3: 7((1750 - 5y)/3) + 6y = 3800 => 12250 - 35y + 18y = 11400 => -17y = -850 => y = 50.\nStep 4: x = (1750 - 250)/3 = 500. Bat = ₹ 500, Ball = ₹ 50."
  },
  {
    "id": "10000000-0000-0000-0003-000000000030",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(iv)",
    "difficulty": "hard",
    "text": "[Exercise 3.2 - Q3(iv)] The taxi charges in a city consist of a fixed charge together with the charge for distance covered. For 10 km, charge is ₹ 105; for 15 km, charge is ₹ 155. What are fixed charges and charge per km? How much for 25 km?",
    "options": [
      {
        "id": "A",
        "text": "Fixed = ₹ 5, Per km = ₹ 10; Total for 25 km = ₹ 255",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Fixed = ₹ 10, Per km = ₹ 9; Total for 25 km = ₹ 235",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Fixed = ₹ 8, Per km = ₹ 10; Total for 25 km = ₹ 258",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Fixed = ₹ 5, Per km = ₹ 12; Total for 25 km = ₹ 305",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x + 10y = 105 and x + 15y = 155.\nStep 2: Subtracting gives 5y = 50 => y = 10 (charge/km).\nStep 3: x = 105 - 100 = 5 (fixed charge).\nStep 4: For 25 km: x + 25y = 5 + 25(10) = ₹ 255."
  },
  {
    "id": "10000000-0000-0000-0003-000000000031",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(v)",
    "difficulty": "hard",
    "text": "[Exercise 3.2 - Q3(v)] A fraction becomes 9/11, if 2 is added to both numerator and denominator. If 3 is added to both, it becomes 5/6. Find the fraction.",
    "options": [
      {
        "id": "A",
        "text": "7/9",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "5/7",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "3/5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "8/11",
        "is_correct": false
      }
    ],
    "solution": "Step 1: (x + 2)/(y + 2) = 9/11 => 11x - 9y = -4.\nStep 2: (x + 3)/(y + 3) = 5/6 => 6x - 5y = -3.\nStep 3: Solving gives x = 7, y = 9.\nHence, the fraction is 7/9."
  },
  {
    "id": "10000000-0000-0000-0003-000000000032",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.2",
    "questionNumber": "3(vi)",
    "difficulty": "medium",
    "text": "[Exercise 3.2 - Q3(vi)] Five years hence, the age of Jacob will be three times that of his son. Five years ago, Jacob's age was seven times that of his son. What are their present ages?",
    "options": [
      {
        "id": "A",
        "text": "Jacob = 40 years, Son = 10 years",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Jacob = 45 years, Son = 15 years",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Jacob = 35 years, Son = 5 years",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Jacob = 50 years, Son = 12 years",
        "is_correct": false
      }
    ],
    "solution": "Step 1: (x + 5) = 3(y + 5) => x - 3y = 10.\nStep 2: (x - 5) = 7(y - 5) => x - 7y = -30.\nStep 3: Subtracting gives 4y = 40 => y = 10.\nStep 4: x = 3(10) + 10 = 40. Jacob = 40 years, Son = 10 years."
  },
  {
    "id": "10000000-0000-0000-0003-000000000033",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 3.3 - Q1(i)] Solve the following pair of linear equations by the elimination method and the substitution method:\nx + y = 5\n2x – 3y = 4",
    "options": [
      {
        "id": "A",
        "text": "x = 19/5, y = 6/5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 4, y = 1",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 17/5, y = 8/5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 3, y = 2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply (1) by 2: 2x + 2y = 10.\nStep 2: Subtract (2): 5y = 6 => y = 6/5.\nStep 3: x = 5 - 6/5 = 19/5. Solution: x = 19/5, y = 6/5."
  },
  {
    "id": "10000000-0000-0000-0003-000000000034",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "1(ii)",
    "difficulty": "easy",
    "text": "[Exercise 3.3 - Q1(ii)] Solve the following pair of linear equations by the elimination method:\n3x + 4y = 10\n2x – 2y = 2",
    "options": [
      {
        "id": "A",
        "text": "x = 2, y = 1",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 1, y = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 3, y = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 2, y = 2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply (2) by 2: 4x - 4y = 4.\nStep 2: Add to (1): 7x = 14 => x = 2.\nStep 3: 2(2) - 2y = 2 => 2y = 2 => y = 1. Solution: x = 2, y = 1."
  },
  {
    "id": "10000000-0000-0000-0003-000000000035",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "1(iii)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q1(iii)] Solve the following pair of linear equations by the elimination method:\n3x – 5y – 4 = 0\n9x = 2y + 7",
    "options": [
      {
        "id": "A",
        "text": "x = 9/13, y = -5/13",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = -9/13, y = 5/13",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 7/13, y = -3/13",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1, y = -1/5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: 3x - 5y = 4 and 9x - 2y = 7.\nStep 2: Multiply (1) by 3: 9x - 15y = 12.\nStep 3: Subtract (2): -13y = 5 => y = -5/13.\nStep 4: 3x = 4 + 5(-5/13) = 27/13 => x = 9/13. Solution: x = 9/13, y = -5/13."
  },
  {
    "id": "10000000-0000-0000-0003-000000000036",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "1(iv)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q1(iv)] Solve the following pair of linear equations by the elimination method:\n(x/2) + (2y/3) = –1\nx – (y/3) = 3",
    "options": [
      {
        "id": "A",
        "text": "x = 2, y = -3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = -2, y = 3",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 3, y = -2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1, y = -3",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply (1) by 6: 3x + 4y = -6; Multiply (2) by 3: 3x - y = 9.\nStep 2: Subtract: 5y = -15 => y = -3.\nStep 3: 3x - (-3) = 9 => 3x = 6 => x = 2. Solution: x = 2, y = -3."
  },
  {
    "id": "10000000-0000-0000-0003-000000000037",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "2(i)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q2(i)] If we add 1 to the numerator and subtract 1 from the denominator, a fraction reduces to 1. It becomes 1/2 if we only add 1 to the denominator. What is the fraction?",
    "options": [
      {
        "id": "A",
        "text": "3/5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "2/5",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "4/7",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "5/9",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let fraction be x/y.\nStep 2: (x + 1)/(y - 1) = 1 => x - y = -2.\nStep 3: x/(y + 1) = 1/2 => 2x - y = 1.\nStep 4: Subtracting gives x = 3, y = 5. Fraction is 3/5."
  },
  {
    "id": "10000000-0000-0000-0003-000000000038",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q2(ii)] Five years ago, Nuri was thrice as old as Sonu. Ten years later, Nuri will be twice as old as Sonu. How old are Nuri and Sonu?",
    "options": [
      {
        "id": "A",
        "text": "Nuri = 50 years, Sonu = 20 years",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Nuri = 45 years, Sonu = 15 years",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Nuri = 60 years, Sonu = 25 years",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Nuri = 40 years, Sonu = 15 years",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x - 5 = 3(y - 5) => x - 3y = -10.\nStep 2: x + 10 = 2(y + 10) => x - 2y = 10.\nStep 3: Subtracting gives y = 20, x = 50. Nuri is 50 years old and Sonu is 20 years old."
  },
  {
    "id": "10000000-0000-0000-0003-000000000039",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "2(iii)",
    "difficulty": "hard",
    "text": "[Exercise 3.3 - Q2(iii)] The sum of the digits of a two-digit number is 9. Also, nine times this number is twice the number obtained by reversing the order of the digits. Find the number.",
    "options": [
      {
        "id": "A",
        "text": "18",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "27",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "36",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "45",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Digits x, y. Number = 10x + y. x + y = 9 ... (1)\nStep 2: 9(10x + y) = 2(10y + x) => 88x - 11y = 0 => 8x - y = 0 ... (2)\nStep 3: Adding gives 9x = 9 => x = 1, y = 8. The number is 18."
  },
  {
    "id": "10000000-0000-0000-0003-000000000040",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "2(iv)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q2(iv)] Meena went to a bank to withdraw ₹ 2000. She asked the cashier to give her ₹ 50 and ₹ 100 notes only. Meena got 25 notes in all. Find how many notes of ₹ 50 and ₹ 100 she received.",
    "options": [
      {
        "id": "A",
        "text": "10 notes of ₹ 50, 15 notes of ₹ 100",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "15 notes of ₹ 50, 10 notes of ₹ 100",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "12 notes of ₹ 50, 13 notes of ₹ 100",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "8 notes of ₹ 50, 17 notes of ₹ 100",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x + y = 25 and 50x + 100y = 2000 => x + 2y = 40.\nStep 2: Subtracting gives y = 15, x = 10.\nMeena received 10 notes of ₹ 50 and 15 notes of ₹ 100."
  },
  {
    "id": "10000000-0000-0000-0003-000000000041",
    "subject": "math",
    "chapterId": "math_ch_03_linear_equations",
    "exercise": "Exercise 3.3",
    "questionNumber": "2(v)",
    "difficulty": "medium",
    "text": "[Exercise 3.3 - Q2(v)] A lending library has a fixed charge for first 3 days and additional charge for each day thereafter. Saritha paid ₹ 27 for 7 days, Susy paid ₹ 21 for 5 days. Find fixed charge and charge for each extra day.",
    "options": [
      {
        "id": "A",
        "text": "Fixed charge = ₹ 15, Extra charge per day = ₹ 3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Fixed charge = ₹ 12, Extra charge per day = ₹ 4",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Fixed charge = ₹ 14, Extra charge per day = ₹ 3.5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Fixed charge = ₹ 10, Extra charge per day = ₹ 5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: x + 4y = 27 and x + 2y = 21.\nStep 2: Subtracting gives 2y = 6 => y = 3 (extra charge/day).\nStep 3: x = 21 - 2(3) = ₹ 15 (fixed charge)."
  }
];

    const ch4SampleQuestions = [
  {
    "id": "10000000-0000-0000-0004-000000000001",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(i)] Check whether the following is a quadratic equation:\n(x + 1)\u00b2 = 2(x \u2013 3)",
    "options": [
      {
        "id": "A",
        "text": "Yes, it is a quadratic equation (x\u00b2 + 7 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, it is a linear equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, it is a cubic equation",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "None of the above",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Expand LHS: (x + 1)\u00b2 = x\u00b2 + 2x + 1.\nStep 2: Expand RHS: 2(x \u2013 3) = 2x \u2013 6.\nStep 3: Equating LHS and RHS:\n  x\u00b2 + 2x + 1 = 2x \u2013 6\n  => x\u00b2 + 7 = 0.\nStep 4: Since it is of the form ax\u00b2 + bx + c = 0 with a = 1 \u2260 0, it is a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000002",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(ii)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(ii)] Check whether the following is a quadratic equation:\nx\u00b2 \u2013 2x = (\u20132)(3 \u2013 x)",
    "options": [
      {
        "id": "A",
        "text": "Yes, it is a quadratic equation (x\u00b2 \u2013 4x + 6 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, it is a linear equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, it is an identity",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Yes, with degree 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = x\u00b2 \u2013 2x.\nStep 2: RHS = (\u20132)(3 \u2013 x) = \u20136 + 2x.\nStep 3: Equating:\n  x\u00b2 \u2013 2x = \u20136 + 2x\n  => x\u00b2 \u2013 4x + 6 = 0.\nStep 4: Degree is 2, hence it is a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000003",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(iii)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(iii)] Check whether the following is a quadratic equation:\n(x \u2013 2)(x + 1) = (x \u2013 1)(x + 3)",
    "options": [
      {
        "id": "A",
        "text": "No, it is a linear equation (3x \u2013 1 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is a quadratic equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, with roots 2 and \u20131",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "It is a cubic equation",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = (x \u2013 2)(x + 1) = x\u00b2 \u2013 x \u2013 2.\nStep 2: RHS = (x \u2013 1)(x + 3) = x\u00b2 + 2x \u2013 3.\nStep 3: Equating:\n  x\u00b2 \u2013 x \u2013 2 = x\u00b2 + 2x \u2013 3\n  => 3x \u2013 1 = 0.\nStep 4: The x\u00b2 term cancels out completely. Degree is 1, so it is NOT a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000004",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(iv)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(iv)] Check whether the following is a quadratic equation:\n(x \u2013 3)(2x + 1) = x(x + 5)",
    "options": [
      {
        "id": "A",
        "text": "Yes, it is a quadratic equation (x\u00b2 \u2013 10x \u2013 3 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, it is a linear equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, it has no real terms",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "None of the above",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = (x \u2013 3)(2x + 1) = 2x\u00b2 + x \u2013 6x \u2013 3 = 2x\u00b2 \u2013 5x \u2013 3.\nStep 2: RHS = x(x + 5) = x\u00b2 + 5x.\nStep 3: 2x\u00b2 \u2013 5x \u2013 3 = x\u00b2 + 5x => x\u00b2 \u2013 10x \u2013 3 = 0.\nStep 4: It is of the form ax\u00b2 + bx + c = 0 (a = 1 \u2260 0), so it is a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000005",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(v)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(v)] Check whether the following is a quadratic equation:\n(2x \u2013 1)(x \u2013 3) = (x + 5)(x \u2013 1)",
    "options": [
      {
        "id": "A",
        "text": "Yes, it is a quadratic equation (x\u00b2 \u2013 11x + 8 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, it is linear (11x \u2013 8 = 0)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, it has degree 3",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Cannot be determined",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = 2x\u00b2 \u2013 6x \u2013 x + 3 = 2x\u00b2 \u2013 7x + 3.\nStep 2: RHS = x\u00b2 \u2013 x + 5x \u2013 5 = x\u00b2 + 4x \u2013 5.\nStep 3: 2x\u00b2 \u2013 7x + 3 = x\u00b2 + 4x \u2013 5 => x\u00b2 \u2013 11x + 8 = 0.\nStep 4: Degree is 2. Hence, it is a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000006",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(vi)",
    "difficulty": "easy",
    "text": "[Exercise 4.1 - Q1(vi)] Check whether the following is a quadratic equation:\nx\u00b2 + 3x + 1 = (x \u2013 2)\u00b2",
    "options": [
      {
        "id": "A",
        "text": "No, it simplifies to a linear equation (7x \u2013 3 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is a quadratic equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, degree is 2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "It has infinite roots",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = x\u00b2 + 3x + 1.\nStep 2: RHS = (x \u2013 2)\u00b2 = x\u00b2 \u2013 4x + 4.\nStep 3: x\u00b2 + 3x + 1 = x\u00b2 \u2013 4x + 4 => 7x \u2013 3 = 0.\nStep 4: Since x\u00b2 cancels out, degree is 1. It is not a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000007",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(vii)",
    "difficulty": "medium",
    "text": "[Exercise 4.1 - Q1(vii)] Check whether the following is a quadratic equation:\n(x + 2)\u00b3 = 2x(x\u00b2 \u2013 1)",
    "options": [
      {
        "id": "A",
        "text": "No, it is a cubic equation (x\u00b3 \u2013 6x\u00b2 \u2013 14x \u2013 8 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is a quadratic equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, degree is 2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "It is linear",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = (x + 2)\u00b3 = x\u00b3 + 6x\u00b2 + 12x + 8.\nStep 2: RHS = 2x(x\u00b2 \u2013 1) = 2x\u00b3 \u2013 2x.\nStep 3: x\u00b3 + 6x\u00b2 + 12x + 8 = 2x\u00b3 \u2013 2x => x\u00b3 \u2013 6x\u00b2 \u2013 14x \u2013 8 = 0.\nStep 4: Highest power is 3. Hence, it is cubic, NOT quadratic."
  },
  {
    "id": "10000000-0000-0000-0004-000000000008",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "1(viii)",
    "difficulty": "medium",
    "text": "[Exercise 4.1 - Q1(viii)] Check whether the following is a quadratic equation:\nx\u00b3 \u2013 4x\u00b2 \u2013 x + 1 = (x \u2013 2)\u00b3",
    "options": [
      {
        "id": "A",
        "text": "Yes, it is a quadratic equation (2x\u00b2 \u2013 13x + 9 = 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, it is a cubic equation",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, it is linear",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "None of the above",
        "is_correct": false
      }
    ],
    "solution": "Step 1: LHS = x\u00b3 \u2013 4x\u00b2 \u2013 x + 1.\nStep 2: RHS = (x \u2013 2)\u00b3 = x\u00b3 \u2013 6x\u00b2 + 12x \u2013 8.\nStep 3: x\u00b3 \u2013 4x\u00b2 \u2013 x + 1 = x\u00b3 \u2013 6x\u00b2 + 12x \u2013 8 => 2x\u00b2 \u2013 13x + 9 = 0.\nStep 4: The x\u00b3 terms cancel out leaving degree 2. It is a quadratic equation."
  },
  {
    "id": "10000000-0000-0000-0004-000000000009",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "2(i)",
    "difficulty": "medium",
    "text": "[Exercise 4.1 - Q2(i)] Represent the situation as a quadratic equation:\nThe area of a rectangular plot is 528 m\u00b2. The length of the plot (in metres) is one more than twice its breadth. We need to find the length and breadth of the plot.",
    "options": [
      {
        "id": "A",
        "text": "2x\u00b2 + x \u2013 528 = 0, where x is breadth in metres",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x\u00b2 + 2x \u2013 528 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "2x\u00b2 \u2013 x + 528 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "2x\u00b2 + 2x \u2013 528 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let the breadth of the rectangular plot be x metres.\nStep 2: Length is one more than twice its breadth => Length = (2x + 1) metres.\nStep 3: Area = Length \u00d7 Breadth = x(2x + 1) = 2x\u00b2 + x.\nStep 4: Given area = 528 m\u00b2 => 2x\u00b2 + x = 528 => 2x\u00b2 + x \u2013 528 = 0."
  },
  {
    "id": "10000000-0000-0000-0004-000000000010",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 4.1 - Q2(ii)] Represent the situation as a quadratic equation:\nThe product of two consecutive positive integers is 306. We need to find the integers.",
    "options": [
      {
        "id": "A",
        "text": "x\u00b2 + x \u2013 306 = 0, where x is the smaller integer",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x\u00b2 + 2x \u2013 306 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x\u00b2 \u2013 x \u2013 306 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "2x\u00b2 + x \u2013 306 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let two consecutive positive integers be x and (x + 1).\nStep 2: Their product = x(x + 1) = x\u00b2 + x.\nStep 3: Given product = 306 => x\u00b2 + x = 306 => x\u00b2 + x \u2013 306 = 0."
  },
  {
    "id": "10000000-0000-0000-0004-000000000011",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "2(iii)",
    "difficulty": "medium",
    "text": "[Exercise 4.1 - Q2(iii)] Represent the situation as a quadratic equation:\nRohan\u2019s mother is 26 years older than him. The product of their ages (in years) 3 years from now will be 360. We would like to find Rohan\u2019s present age.",
    "options": [
      {
        "id": "A",
        "text": "x\u00b2 + 32x \u2013 273 = 0, where x is Rohan's present age",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x\u00b2 + 26x \u2013 360 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x\u00b2 + 29x \u2013 273 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x\u00b2 + 32x + 273 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let Rohan's present age be x years.\nStep 2: Mother's present age = (x + 26) years.\nStep 3: After 3 years: Rohan's age = (x + 3); Mother's age = (x + 26 + 3) = (x + 29).\nStep 4: Product = (x + 3)(x + 29) = x\u00b2 + 32x + 87.\nStep 5: Given product = 360 => x\u00b2 + 32x + 87 = 360 => x\u00b2 + 32x \u2013 273 = 0."
  },
  {
    "id": "10000000-0000-0000-0004-000000000012",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.1",
    "questionNumber": "2(iv)",
    "difficulty": "hard",
    "text": "[Exercise 4.1 - Q2(iv)] Represent the situation as a quadratic equation:\nA train travels a distance of 480 km at a uniform speed. If the speed had been 8 km/h less, then it would have taken 3 hours more to cover the same distance. We need to find the speed of the train.",
    "options": [
      {
        "id": "A",
        "text": "x\u00b2 \u2013 8x \u2013 1280 = 0, where x is speed in km/h",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x\u00b2 + 8x \u2013 1280 = 0",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x\u00b2 \u2013 8x \u2013 480 = 0",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "3x\u00b2 \u2013 8x \u2013 1280 = 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let speed of train be x km/h. Time taken to travel 480 km = 480/x hours.\nStep 2: When speed is reduced by 8 km/h, speed = (x \u2013 8) km/h. Time taken = 480/(x \u2013 8) hours.\nStep 3: Difference in time is 3 hours:\n  480/(x \u2013 8) \u2013 480/x = 3\nStep 4: 480 [ (x \u2013 (x \u2013 8)) / (x(x \u2013 8)) ] = 3\n  => 480 \u00d7 8 / (x\u00b2 \u2013 8x) = 3\n  => 3(x\u00b2 \u2013 8x) = 3840\n  => x\u00b2 \u2013 8x = 1280\n  => x\u00b2 \u2013 8x \u2013 1280 = 0."
  },
  {
    "id": "10000000-0000-0000-0004-000000000013",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "1(i)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q1(i)] Find the roots of the quadratic equation by factorisation:\nx\u00b2 \u2013 3x \u2013 10 = 0",
    "options": [
      {
        "id": "A",
        "text": "x = 5 and x = \u20132",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = \u20135 and x = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 10 and x = \u20131",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 3 and x = \u201310",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Split middle term: \u20133x = \u20135x + 2x and (\u20135)(2) = \u201310.\nStep 2: x\u00b2 \u2013 5x + 2x \u2013 10 = 0\n  => x(x \u2013 5) + 2(x \u2013 5) = 0\n  => (x \u2013 5)(x + 2) = 0.\nStep 3: x \u2013 5 = 0 => x = 5; or x + 2 = 0 => x = \u20132.\nRoots are 5 and \u20132."
  },
  {
    "id": "10000000-0000-0000-0004-000000000014",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "1(ii)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q1(ii)] Find the roots of the quadratic equation by factorisation:\n2x\u00b2 + x \u2013 6 = 0",
    "options": [
      {
        "id": "A",
        "text": "x = 3/2 and x = \u20132",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = \u20133/2 and x = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 2/3 and x = \u20133",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 6 and x = \u20131",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Product = 2 \u00d7 (\u20136) = \u201312. Split +x as +4x \u2013 3x.\nStep 2: 2x\u00b2 + 4x \u2013 3x \u2013 6 = 0\n  => 2x(x + 2) \u2013 3(x + 2) = 0\n  => (2x \u2013 3)(x + 2) = 0.\nStep 3: 2x \u2013 3 = 0 => x = 3/2; x + 2 = 0 => x = \u20132.\nRoots are 3/2 and \u20132."
  },
  {
    "id": "10000000-0000-0000-0004-000000000015",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "1(iii)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q1(iii)] Find the roots of the quadratic equation by factorisation:\n\u221a2 x\u00b2 + 7x + 5\u221a2 = 0",
    "options": [
      {
        "id": "A",
        "text": "x = \u20135/\u221a2 and x = \u2013\u221a2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 5/\u221a2 and x = \u221a2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = \u20135 and x = \u20132",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = \u2013\u221a2 and x = 5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Product = \u221a2 \u00d7 5\u221a2 = 5 \u00d7 2 = 10. Split 7x as 2x + 5x.\nStep 2: \u221a2 x\u00b2 + 2x + 5x + 5\u221a2 = 0\n  => \u221a2 x(x + \u221a2) + 5(x + \u221a2) = 0\n  => (\u221a2 x + 5)(x + \u221a2) = 0.\nStep 3: Either \u221a2 x + 5 = 0 => x = \u20135/\u221a2, or x + \u221a2 = 0 => x = \u2013\u221a2."
  },
  {
    "id": "10000000-0000-0000-0004-000000000016",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "1(iv)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q1(iv)] Find the roots of the quadratic equation by factorisation:\n2x\u00b2 \u2013 x + 1/8 = 0",
    "options": [
      {
        "id": "A",
        "text": "x = 1/4 and x = 1/4",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = 1/2 and x = 1/4",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = \u20131/4 and x = \u20131/4",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1/8 and x = 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Multiply entire equation by 8:\n  16x\u00b2 \u2013 8x + 1 = 0.\nStep 2: Recognize identity: (4x \u2013 1)\u00b2 = 16x\u00b2 \u2013 8x + 1 = 0.\nStep 3: (4x \u2013 1)(4x \u2013 1) = 0 => x = 1/4, 1/4.\nBoth equal roots are 1/4."
  },
  {
    "id": "10000000-0000-0000-0004-000000000017",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "1(v)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q1(v)] Find the roots of the quadratic equation by factorisation:\n100x\u00b2 \u2013 20x + 1 = 0",
    "options": [
      {
        "id": "A",
        "text": "x = 1/10 and x = 1/10",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "x = \u20131/10 and x = \u20131/10",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "x = 1/20 and x = 1/5",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "x = 1/100 and x = 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Notice (10x \u2013 1)\u00b2 = 100x\u00b2 \u2013 20x + 1 = 0.\nStep 2: (10x \u2013 1)(10x \u2013 1) = 0.\nStep 3: 10x \u2013 1 = 0 => x = 1/10.\nBoth equal roots are 1/10."
  },
  {
    "id": "10000000-0000-0000-0004-000000000018",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "2(i)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q2(i)] Solve the problem given in Example 1(i):\nJohn and Jivanti together have 45 marbles. Both lost 5 marbles each, and the product of marbles they now have is 124. Find how many marbles they had to start with.",
    "options": [
      {
        "id": "A",
        "text": "36 and 9 marbles",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "30 and 15 marbles",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "40 and 5 marbles",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "28 and 17 marbles",
        "is_correct": false
      }
    ],
    "solution": "Step 1: The mathematical formulation from Example 1 is x\u00b2 \u2013 45x + 324 = 0.\nStep 2: Factorise: (x \u2013 36)(x \u2013 9) = 0.\nStep 3: x = 36 or x = 9.\nHence, John and Jivanti had 36 and 9 marbles (or 9 and 36)."
  },
  {
    "id": "10000000-0000-0000-0004-000000000019",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q2(ii)] Solve the problem given in Example 1(ii):\nA cottage industry produces a certain number of toys in a day. Cost of production of each toy was (55 \u2013 x). Total cost of production on that day was \u20b9 750. Find the number of toys produced.",
    "options": [
      {
        "id": "A",
        "text": "30 or 25 toys",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "35 or 20 toys",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "40 or 15 toys",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "50 or 5 toys",
        "is_correct": false
      }
    ],
    "solution": "Step 1: The equation from Example 1 is x\u00b2 \u2013 55x + 750 = 0.\nStep 2: Factorise: (x \u2013 30)(x \u2013 25) = 0.\nStep 3: x = 30 or x = 25.\nThe number of toys produced that day was either 30 or 25."
  },
  {
    "id": "10000000-0000-0000-0004-000000000020",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "3",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q3] Find two numbers whose sum is 27 and product is 182.",
    "options": [
      {
        "id": "A",
        "text": "13 and 14",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "12 and 15",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "11 and 16",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "10 and 17",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let the two numbers be x and (27 \u2013 x).\nStep 2: Product: x(27 \u2013 x) = 182 => 27x \u2013 x\u00b2 = 182 => x\u00b2 \u2013 27x + 182 = 0.\nStep 3: Factorise: 182 = 13 \u00d7 14, and \u201313 \u2013 14 = \u201327.\nStep 4: (x \u2013 13)(x \u2013 14) = 0 => x = 13 or x = 14.\nTherefore, the required numbers are 13 and 14."
  },
  {
    "id": "10000000-0000-0000-0004-000000000021",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "4",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q4] Find two consecutive positive integers, sum of whose squares is 365.",
    "options": [
      {
        "id": "A",
        "text": "13 and 14",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "11 and 12",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "12 and 13",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "14 and 15",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let the two consecutive positive integers be x and (x + 1).\nStep 2: x\u00b2 + (x + 1)\u00b2 = 365 => x\u00b2 + x\u00b2 + 2x + 1 = 365 => 2x\u00b2 + 2x \u2013 364 = 0.\nStep 3: Dividing by 2: x\u00b2 + x \u2013 182 = 0.\nStep 4: (x + 14)(x \u2013 13) = 0 => x = 13 (reject \u201314 since integers are positive).\nStep 5: x + 1 = 14. The two integers are 13 and 14."
  },
  {
    "id": "10000000-0000-0000-0004-000000000022",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "5",
    "difficulty": "medium",
    "text": "[Exercise 4.2 - Q5] The altitude of a right triangle is 7 cm less than its base. If the hypotenuse is 13 cm, find the other two sides.",
    "options": [
      {
        "id": "A",
        "text": "Base = 12 cm, Altitude = 5 cm",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Base = 10 cm, Altitude = 3 cm",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Base = 15 cm, Altitude = 8 cm",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Base = 9 cm, Altitude = 2 cm",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let base = x cm. Then altitude = (x \u2013 7) cm. Hypotenuse = 13 cm.\nStep 2: By Pythagoras theorem: x\u00b2 + (x \u2013 7)\u00b2 = 13\u00b2 = 169.\nStep 3: x\u00b2 + x\u00b2 \u2013 14x + 49 = 169 => 2x\u00b2 \u2013 14x \u2013 120 = 0 => x\u00b2 \u2013 7x \u2013 60 = 0.\nStep 4: Factorise: (x \u2013 12)(x + 5) = 0 => x = 12 (length cannot be negative).\nStep 5: Base = 12 cm, Altitude = 12 \u2013 7 = 5 cm."
  },
  {
    "id": "10000000-0000-0000-0004-000000000023",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.2",
    "questionNumber": "6",
    "difficulty": "hard",
    "text": "[Exercise 4.2 - Q6] A cottage industry produces a certain number of pottery articles in a day. The cost of production of each article was \u20b9 3 more than twice the number of articles produced. If total cost was \u20b9 90, find the number of articles produced and cost of each article.",
    "options": [
      {
        "id": "A",
        "text": "Number of articles = 6, Cost of each = \u20b9 15",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Number of articles = 5, Cost of each = \u20b9 18",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Number of articles = 10, Cost of each = \u20b9 9",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Number of articles = 8, Cost of each = \u20b9 19",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let number of articles = x. Cost of each article = \u20b9 (2x + 3).\nStep 2: Total cost = x(2x + 3) = 90 => 2x\u00b2 + 3x \u2013 90 = 0.\nStep 3: Factorise: 2x\u00b2 \u2013 12x + 15x \u2013 90 = 0 => 2x(x \u2013 6) + 15(x \u2013 6) = 0 => (2x + 15)(x \u2013 6) = 0.\nStep 4: x = 6 (since articles cannot be negative or fractional).\nStep 5: Cost of each article = 2(6) + 3 = \u20b9 15."
  },
  {
    "id": "10000000-0000-0000-0004-000000000024",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 4.3 - Q1(i)] Find the nature of the roots of the quadratic equation. If real roots exist, find them:\n2x\u00b2 \u2013 3x + 5 = 0",
    "options": [
      {
        "id": "A",
        "text": "No real roots (Discriminant D = \u201331 < 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Two distinct real roots",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Two equal real roots",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Roots are 3/4 and 5/2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Comparing with ax\u00b2 + bx + c = 0: a = 2, b = \u20133, c = 5.\nStep 2: Discriminant D = b\u00b2 \u2013 4ac = (\u20133)\u00b2 \u2013 4(2)(5) = 9 \u2013 40 = \u201331.\nStep 3: Since D < 0, the quadratic equation has NO real roots."
  },
  {
    "id": "10000000-0000-0000-0004-000000000025",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "1(ii)",
    "difficulty": "medium",
    "text": "[Exercise 4.3 - Q1(ii)] Find the nature of the roots of the quadratic equation. If real roots exist, find them:\n3x\u00b2 \u2013 4\u221a3 x + 4 = 0",
    "options": [
      {
        "id": "A",
        "text": "Two equal real roots: 2/\u221a3, 2/\u221a3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No real roots (D < 0)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Two distinct real roots: \u221a3 and \u2013\u221a3",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Two distinct real roots: 4 and 3",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Here a = 3, b = \u20134\u221a3, c = 4.\nStep 2: Discriminant D = b\u00b2 \u2013 4ac = (\u20134\u221a3)\u00b2 \u2013 4(3)(4) = 48 \u2013 48 = 0.\nStep 3: Since D = 0, the equation has two equal real roots.\nStep 4: Roots: x = \u2013b / (2a) = \u2013(\u20134\u221a3) / (2 \u00d7 3) = 4\u221a3 / 6 = 2\u221a3 / 3 = 2/\u221a3.\nHence, roots are 2/\u221a3, 2/\u221a3."
  },
  {
    "id": "10000000-0000-0000-0004-000000000026",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "1(iii)",
    "difficulty": "medium",
    "text": "[Exercise 4.3 - Q1(iii)] Find the nature of the roots of the quadratic equation. If real roots exist, find them:\n2x\u00b2 \u2013 6x + 3 = 0",
    "options": [
      {
        "id": "A",
        "text": "Two distinct real roots: (3 \u00b1 \u221a3) / 2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Two equal real roots: 3/2, 3/2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No real roots (D < 0)",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Two integer roots: 3 and 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 2, b = \u20136, c = 3.\nStep 2: Discriminant D = b\u00b2 \u2013 4ac = (\u20136)\u00b2 \u2013 4(2)(3) = 36 \u2013 24 = 12 > 0.\nStep 3: Since D > 0, there are two distinct real roots.\nStep 4: By quadratic formula:\n  x = [\u2013b \u00b1 \u221aD] / 2a = [\u2013(\u20136) \u00b1 \u221a12] / (2 \u00d7 2) = (6 \u00b1 2\u221a3) / 4 = (3 \u00b1 \u221a3) / 2."
  },
  {
    "id": "10000000-0000-0000-0004-000000000027",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "2(i)",
    "difficulty": "medium",
    "text": "[Exercise 4.3 - Q2(i)] Find the value(s) of k so that the quadratic equation has two equal roots:\n2x\u00b2 + kx + 3 = 0",
    "options": [
      {
        "id": "A",
        "text": "k = \u00b1 2\u221a6",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "k = \u00b1 6",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "k = \u00b1 24",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "k = 12",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 2, b = k, c = 3.\nStep 2: For two equal roots, Discriminant D = b\u00b2 \u2013 4ac = 0.\nStep 3: k\u00b2 \u2013 4(2)(3) = 0 => k\u00b2 \u2013 24 = 0 => k\u00b2 = 24.\nStep 4: k = \u00b1 \u221a24 = \u00b1 \u221a(4 \u00d7 6) = \u00b1 2\u221a6."
  },
  {
    "id": "10000000-0000-0000-0004-000000000028",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 4.3 - Q2(ii)] Find the value(s) of k so that the quadratic equation has two equal roots:\nkx(x \u2013 2) + 6 = 0",
    "options": [
      {
        "id": "A",
        "text": "k = 6",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "k = 0 or 6",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "k = \u20136",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "k = 4",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Expand equation: kx\u00b2 \u2013 2kx + 6 = 0. Here a = k, b = \u20132k, c = 6.\nStep 2: For equal roots, D = b\u00b2 \u2013 4ac = 0.\nStep 3: (\u20132k)\u00b2 \u2013 4(k)(6) = 0 => 4k\u00b2 \u2013 24k = 0 => 4k(k \u2013 6) = 0.\nStep 4: Either k = 0 or k = 6.\nStep 5: If k = 0, equation becomes 6 = 0 (not quadratic). Therefore, k = 6."
  },
  {
    "id": "10000000-0000-0000-0004-000000000029",
    "subject": "math",
    "chapterId": "math_ch_04_quadratic_equations",
    "exercise": "Exercise 4.3",
    "questionNumber": "3 to 5",
    "difficulty": "hard",
    "text": "[Exercise 4.3 - Q3 to Q5] Check feasibility of geometric situations:\n(i) Rectangular mango grove length = 2b, area = 800 m\u00b2;\n(ii) Sum of friend ages = 20, product 4 yrs ago was 48;\n(iii) Rectangular park perimeter = 80 m, area = 400 m\u00b2.\nWhich situations are mathematically possible?",
    "options": [
      {
        "id": "A",
        "text": "(i) and (iii) are possible; (ii) is not possible (D < 0)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "All three situations are possible",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Only (i) is possible",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "None of the situations are possible",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Mango grove: 2x\u00b2 = 800 => x\u00b2 = 400 => x = 20 m (breadth), length = 40 m. Real roots exist. Possible!\nStep 2: Age problem: (x \u2013 4)(16 \u2013 x) = 48 => x\u00b2 \u2013 20x + 112 = 0. D = 400 \u2013 448 = \u201348 < 0. No real roots. Not possible!\nStep 3: Park: l(40 \u2013 l) = 400 => l\u00b2 \u2013 40l + 400 = 0 => (l \u2013 20)\u00b2 = 0 => l = 20 m, b = 20 m. Real equal roots. Possible (square park of side 20 m)!\nHence, (i) and (iii) are possible, (ii) is not possible."
  }
];


    const ch5SampleQuestions = [
  {
    "id": "10000000-0000-0000-0005-000000000001",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q1(i)] The taxi fare after each km when the fare is ₹ 15 for the first km and ₹ 8 for each additional km. Does this situation make an arithmetic progression?",
    "options": [
      {
        "id": "A",
        "text": "Yes, it forms an AP because each term is obtained by adding a constant ₹ 8 (series: 15, 23, 31, 39, ...)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, taxi fares follow geometric compounding",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, the initial fare is higher than the per-km rate",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Yes, but only for distances less than 10 km",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Fare for 1 km = ₹ 15.\nStep 2: Fare for 2 km = 15 + 8 = ₹ 23; Fare for 3 km = 23 + 8 = ₹ 31; Fare for 4 km = 31 + 8 = ₹ 39.\nStep 3: The series of terms is 15, 23, 31, 39, ... Here, the difference between consecutive terms is constant (d = 8).\nHence, it forms an Arithmetic Progression (AP)."
  },
  {
    "id": "10000000-0000-0000-0005-000000000002",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "1(ii)",
    "difficulty": "medium",
    "text": "[Exercise 5.1 - Q1(ii)] The amount of air present in a cylinder when a vacuum pump removes 1/4 of the air remaining in the cylinder at a time. Does this situation form an arithmetic progression?",
    "options": [
      {
        "id": "A",
        "text": "No, each stroke leaves 3/4 of the remaining volume, so differences are not constant (V, 3/4 V, 9/16 V, ...)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is an AP with common difference d = -1/4",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, because air is continuously removed at equal intervals",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "No, because volume cannot be measured in an arithmetic progression",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Let initial volume = V.\nStep 2: After 1st stroke, volume left = V - (1/4)V = (3/4)V.\nStep 3: After 2nd stroke, volume left = (3/4)V - (1/4)(3/4)V = (9/16)V.\nStep 4: Difference a2 - a1 = -1/4 V, but a3 - a2 = -3/16 V != -1/4 V.\nSince successive differences are not constant, it does NOT form an AP."
  },
  {
    "id": "10000000-0000-0000-0005-000000000003",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "1(iii)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q1(iii)] The cost of digging a well after every metre of digging, when it costs ₹ 150 for the first metre and rises by ₹ 50 for each subsequent metre. Does this situation form an arithmetic progression?",
    "options": [
      {
        "id": "A",
        "text": "Yes, it forms an AP with first term a = 150 and common difference d = 50 (150, 200, 250, 300, ...)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "No, digging costs increase exponentially with depth",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "No, because the first metre costs more than subsequent metres",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Yes, but with common difference d = 100",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Cost for 1 m = ₹ 150.\nStep 2: Cost for 2 m = 150 + 50 = ₹ 200; for 3 m = 200 + 50 = ₹ 250; for 4 m = ₹ 300.\nStep 3: List of numbers: 150, 200, 250, 300, ...\nStep 4: Common difference d = 200 - 150 = 250 - 200 = 50 (constant).\nHence, it forms an AP."
  },
  {
    "id": "10000000-0000-0000-0005-000000000004",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "1(iv)",
    "difficulty": "medium",
    "text": "[Exercise 5.1 - Q1(iv)] The amount of money in the account every year, when ₹ 10,000 is deposited at compound interest at 8% per annum. Does this situation form an arithmetic progression?",
    "options": [
      {
        "id": "A",
        "text": "No, compound interest increases the principal geometrically each year, so successive differences are not equal",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is an AP with common difference d = 800",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, it is an AP with common ratio r = 1.08",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "No, money can never form an AP",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Year 1 amount = 10000(1 + 8/100) = ₹ 10,800.\nStep 2: Year 2 amount = 10000(1 + 8/100)^2 = ₹ 11,664.\nStep 3: Year 3 amount = 10000(1 + 8/100)^3 = ₹ 12,597.12.\nStep 4: a2 - a1 = 800, while a3 - a2 = 864 != 800.\nSince successive differences are not constant, compound interest does NOT form an AP."
  },
  {
    "id": "10000000-0000-0000-0005-000000000005",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "2(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q2(i)] Write the first four terms of the AP, when the first term a = 10 and the common difference d = 10.",
    "options": [
      {
        "id": "A",
        "text": "10, 20, 30, 40",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "10, 100, 1000, 10000",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "10, 0, -10, -20",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "0, 10, 20, 30",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a1 = a = 10.\nStep 2: a2 = a + d = 10 + 10 = 20.\nStep 3: a3 = a2 + d = 20 + 10 = 30.\nStep 4: a4 = a3 + d = 30 + 10 = 40.\nFirst four terms are 10, 20, 30, 40."
  },
  {
    "id": "10000000-0000-0000-0005-000000000006",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "2(ii)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q2(ii)] Write the first four terms of the AP, when the first term a = -2 and the common difference d = 0.",
    "options": [
      {
        "id": "A",
        "text": "-2, -2, -2, -2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "-2, 0, 2, 4",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "-2, -4, -6, -8",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "0, -2, -4, -6",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a1 = -2.\nStep 2: a2 = -2 + 0 = -2.\nStep 3: a3 = -2 + 0 = -2.\nStep 4: a4 = -2 + 0 = -2.\nWhen d = 0, every term is equal to a. The terms are -2, -2, -2, -2."
  },
  {
    "id": "10000000-0000-0000-0005-000000000007",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "2(iii)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q2(iii)] Write the first four terms of the AP, when the first term a = 4 and the common difference d = -3.",
    "options": [
      {
        "id": "A",
        "text": "4, 1, -2, -5",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "4, 7, 10, 13",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "4, -3, -7, -11",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "4, 1, 0, -3",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a1 = 4.\nStep 2: a2 = 4 + (-3) = 1.\nStep 3: a3 = 1 + (-3) = -2.\nStep 4: a4 = -2 + (-3) = -5.\nFirst four terms are 4, 1, -2, -5."
  },
  {
    "id": "10000000-0000-0000-0005-000000000008",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "2(iv)",
    "difficulty": "medium",
    "text": "[Exercise 5.1 - Q2(iv)] Write the first four terms of the AP, when a = -1 and d = 1/2.",
    "options": [
      {
        "id": "A",
        "text": "-1, -1/2, 0, 1/2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "-1, -3/2, -2, -5/2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "-1, 0, 1, 2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "-1, -1/2, -1/4, 0",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a1 = -1.\nStep 2: a2 = -1 + 1/2 = -1/2.\nStep 3: a3 = -1/2 + 1/2 = 0.\nStep 4: a4 = 0 + 1/2 = 1/2.\nFirst four terms are -1, -1/2, 0, 1/2."
  },
  {
    "id": "10000000-0000-0000-0005-000000000009",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "2(v)",
    "difficulty": "medium",
    "text": "[Exercise 5.1 - Q2(v)] Write the first four terms of the AP, when a = -1.25 and d = -0.25.",
    "options": [
      {
        "id": "A",
        "text": "-1.25, -1.50, -1.75, -2.00",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "-1.25, -1.00, -0.75, -0.50",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "-1.25, -1.50, -1.70, -1.90",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "-1.25, -2.50, -3.75, -5.00",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a1 = -1.25.\nStep 2: a2 = -1.25 + (-0.25) = -1.50.\nStep 3: a3 = -1.50 + (-0.25) = -1.75.\nStep 4: a4 = -1.75 + (-0.25) = -2.00.\nFirst four terms are -1.25, -1.50, -1.75, -2.00."
  },
  {
    "id": "10000000-0000-0000-0005-000000000010",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "3(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q3(i)] For the AP: 3, 1, -1, -3, ... write the first term and the common difference.",
    "options": [
      {
        "id": "A",
        "text": "First term a = 3, Common difference d = -2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "First term a = 3, Common difference d = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "First term a = 1, Common difference d = -2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "First term a = -3, Common difference d = 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: First term is the first number in the sequence: a = 3.\nStep 2: Common difference d = a2 - a1 = 1 - 3 = -2.\nStep 3: Check: a3 - a2 = -1 - 1 = -2. Verified."
  },
  {
    "id": "10000000-0000-0000-0005-000000000011",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "3(ii)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q3(ii)] For the AP: -5, -1, 3, 7, ... write the first term and the common difference.",
    "options": [
      {
        "id": "A",
        "text": "First term a = -5, Common difference d = 4",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "First term a = -5, Common difference d = -4",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "First term a = -1, Common difference d = 4",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "First term a = 7, Common difference d = 2",
        "is_correct": false
      }
    ],
    "solution": "Step 1: First term a = -5.\nStep 2: Common difference d = a2 - a1 = -1 - (-5) = -1 + 5 = 4.\nStep 3: Check: 3 - (-1) = 4, 7 - 3 = 4. Verified."
  },
  {
    "id": "10000000-0000-0000-0005-000000000012",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "3(iii)",
    "difficulty": "easy",
    "text": "[Exercise 5.1 - Q3(iii)] For the AP: 1/3, 5/3, 9/3, 13/3, ... write the first term and the common difference.",
    "options": [
      {
        "id": "A",
        "text": "First term a = 1/3, Common difference d = 4/3",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "First term a = 1/3, Common difference d = 5/3",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "First term a = 5/3, Common difference d = 4/3",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "First term a = 1/3, Common difference d = 1",
        "is_correct": false
      }
    ],
    "solution": "Step 1: First term a = 1/3.\nStep 2: Common difference d = 5/3 - 1/3 = 4/3.\nStep 3: Check: 9/3 - 5/3 = 4/3. Verified."
  },
  {
    "id": "10000000-0000-0000-0005-000000000013",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.1",
    "questionNumber": "4",
    "difficulty": "medium",
    "text": "[Exercise 5.1 - Q4] Check whether the following sequences form an AP: (i) 2, 4, 8, 16, ... ; (ii) √2, √8, √18, √32, ... If they form an AP, find the common difference d and write three more terms.",
    "options": [
      {
        "id": "A",
        "text": "(i) is NOT an AP (differences 2, 4, 8); (ii) IS an AP with d = √2 (terms are √2, 2√2, 3√2, 4√2), next terms: √50, √72, √98",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Both are APs with common difference d = 2 and d = √2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "(i) is an AP with d = 2; (ii) is not an AP because radicals cannot form AP",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "Neither is an AP",
        "is_correct": false
      }
    ],
    "solution": "Step 1: In (i): a2 - a1 = 4 - 2 = 2, but a3 - a2 = 8 - 4 = 4 != 2. Successive differences not equal, hence NOT an AP.\nStep 2: In (ii): √2, √8 = 2√2, √18 = 3√2, √32 = 4√2.\nStep 3: Common difference d = 2√2 - √2 = √2 (constant). Hence IS an AP.\nStep 4: Next three terms are 5√2 = √50, 6√2 = √72, 7√2 = √98."
  },
  {
    "id": "10000000-0000-0000-0005-000000000014",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.2 - Q1(i)] In the AP table, given first term a = 7, common difference d = 3, number of terms n = 8, find the nth term a_n.",
    "options": [
      {
        "id": "A",
        "text": "a_8 = 28",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "a_8 = 24",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "a_8 = 31",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "a_8 = 21",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Formula: an = a + (n - 1)d.\nStep 2: Substitute a = 7, d = 3, n = 8.\nStep 3: a8 = 7 + (8 - 1) × 3 = 7 + 7 × 3 = 7 + 21 = 28."
  },
  {
    "id": "10000000-0000-0000-0005-000000000015",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "1(ii)",
    "difficulty": "easy",
    "text": "[Exercise 5.2 - Q1(ii)] Given first term a = -18, number of terms n = 10, and nth term a_n = 0, find the common difference d.",
    "options": [
      {
        "id": "A",
        "text": "d = 2",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "d = -2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "d = 1.8",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "d = 9",
        "is_correct": false
      }
    ],
    "solution": "Step 1: an = a + (n - 1)d.\nStep 2: 0 = -18 + (10 - 1)d => 0 = -18 + 9d.\nStep 3: 9d = 18 => d = 2."
  },
  {
    "id": "10000000-0000-0000-0005-000000000016",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "1(iv)",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q1(iv)] Given first term a = -18.9, common difference d = 2.5, and nth term a_n = 3.6, find the number of terms n.",
    "options": [
      {
        "id": "A",
        "text": "n = 10",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "n = 9",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "n = 11",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "n = 8",
        "is_correct": false
      }
    ],
    "solution": "Step 1: an = a + (n - 1)d.\nStep 2: 3.6 = -18.9 + (n - 1)(2.5).\nStep 3: 3.6 + 18.9 = 22.5 = 2.5(n - 1).\nStep 4: n - 1 = 22.5 / 2.5 = 9 => n = 10."
  },
  {
    "id": "10000000-0000-0000-0005-000000000017",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "2(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.2 - Q2(i)] Choose the correct choice: The 30th term of the AP: 10, 7, 4, ... is:",
    "options": [
      {
        "id": "A",
        "text": "97",
        "is_correct": false
      },
      {
        "id": "B",
        "text": "77",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "-77",
        "is_correct": true
      },
      {
        "id": "D",
        "text": "-87",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 10, d = 7 - 10 = -3, n = 30.\nStep 2: a30 = a + 29d.\nStep 3: a30 = 10 + 29(-3) = 10 - 87 = -77.\nHence, choice C is correct."
  },
  {
    "id": "10000000-0000-0000-0005-000000000018",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "2(ii)",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q2(ii)] Choose the correct choice: The 11th term of the AP: -3, -1/2, 2, ... is:",
    "options": [
      {
        "id": "A",
        "text": "28",
        "is_correct": false
      },
      {
        "id": "B",
        "text": "22",
        "is_correct": true
      },
      {
        "id": "C",
        "text": "-38",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "-46.5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = -3, d = -1/2 - (-3) = -1/2 + 3 = 5/2.\nStep 2: a11 = a + 10d = -3 + 10(5/2) = -3 + 25 = 22.\nHence, choice B is correct."
  },
  {
    "id": "10000000-0000-0000-0005-000000000019",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "3(i)&(ii)",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q3] In the following APs, find the missing terms in the boxes: (i) 2, [ ], 26; (ii) [ ], 13, [ ], 3.",
    "options": [
      {
        "id": "A",
        "text": "(i) Box = 14; (ii) First box = 18, Third box = 8",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "(i) Box = 12; (ii) First box = 16, Third box = 10",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "(i) Box = 14; (ii) First box = 15, Third box = 9",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "(i) Box = 13; (ii) First box = 17, Third box = 7",
        "is_correct": false
      }
    ],
    "solution": "Step 1: For (i): Middle term of a, b, c in AP is (a + c)/2 = (2 + 26)/2 = 14.\nStep 2: For (ii): a + d = 13 and a + 3d = 3. Subtracting gives 2d = -10 => d = -5.\nStep 3: a = 13 - (-5) = 18, and third term = 13 + (-5) = 8."
  },
  {
    "id": "10000000-0000-0000-0005-000000000020",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "4",
    "difficulty": "easy",
    "text": "[Exercise 5.2 - Q4] Which term of the AP: 3, 8, 13, 18, ... is 78?",
    "options": [
      {
        "id": "A",
        "text": "16th term",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "15th term",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "17th term",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "14th term",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 3, d = 8 - 3 = 5, an = 78.\nStep 2: 78 = 3 + (n - 1)5 => 75 = 5(n - 1).\nStep 3: n - 1 = 15 => n = 16.\nHence, 78 is the 16th term."
  },
  {
    "id": "10000000-0000-0000-0005-000000000021",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "5(i)",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q5(i)] Find the number of terms in the AP: 7, 13, 19, ..., 205.",
    "options": [
      {
        "id": "A",
        "text": "34 terms",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "33 terms",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "35 terms",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "32 terms",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 7, d = 13 - 7 = 6, an = 205.\nStep 2: 205 = 7 + (n - 1)6 => 198 = 6(n - 1).\nStep 3: n - 1 = 33 => n = 34.\nHence, there are 34 terms."
  },
  {
    "id": "10000000-0000-0000-0005-000000000022",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "6",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q6] Check whether -150 is a term of the AP: 11, 8, 5, 2, ...",
    "options": [
      {
        "id": "A",
        "text": "No, because solving for n gives n = 164/3 = 54 2/3, which is not a positive integer",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "Yes, it is the 54th term",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "Yes, it is the 55th term",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "No, because terms of an AP cannot be negative",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 11, d = 8 - 11 = -3. Let an = -150.\nStep 2: -150 = 11 + (n - 1)(-3) => -161 = -3(n - 1).\nStep 3: n - 1 = 161/3 => n = 164/3 = 54 2/3.\nSince n must be a positive integer, -150 is NOT a term of this AP."
  },
  {
    "id": "10000000-0000-0000-0005-000000000023",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "7",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q7] Find the 31st term of an AP whose 11th term is 38 and the 16th term is 73.",
    "options": [
      {
        "id": "A",
        "text": "178",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "185",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "171",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "168",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a11 = a + 10d = 38 ... (1) and a16 = a + 15d = 73 ... (2).\nStep 2: Subtracting (1) from (2): 5d = 35 => d = 7.\nStep 3: a + 10(7) = 38 => a = 38 - 70 = -32.\nStep 4: a31 = a + 30d = -32 + 30(7) = -32 + 210 = 178."
  },
  {
    "id": "10000000-0000-0000-0005-000000000024",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "8",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q8] An AP consists of 50 terms of which 3rd term is 12 and the last term is 106. Find the 29th term.",
    "options": [
      {
        "id": "A",
        "text": "64",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "62",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "68",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "56",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Total terms = 50 => a50 = a + 49d = 106.\nStep 2: a3 = a + 2d = 12.\nStep 3: Subtracting gives 47d = 94 => d = 2.\nStep 4: a = 12 - 2(2) = 8.\nStep 5: a29 = a + 28d = 8 + 28(2) = 8 + 56 = 64."
  },
  {
    "id": "10000000-0000-0000-0005-000000000025",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "10",
    "difficulty": "easy",
    "text": "[Exercise 5.2 - Q10] The 17th term of an AP exceeds its 10th term by 7. Find the common difference.",
    "options": [
      {
        "id": "A",
        "text": "d = 1",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "d = 2",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "d = 7",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "d = 0.5",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a17 - a10 = 7.\nStep 2: (a + 16d) - (a + 9d) = 7.\nStep 3: 7d = 7 => d = 1."
  },
  {
    "id": "10000000-0000-0000-0005-000000000026",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "13",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q13] How many three-digit numbers are divisible by 7?",
    "options": [
      {
        "id": "A",
        "text": "128",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "127",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "129",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "130",
        "is_correct": false
      }
    ],
    "solution": "Step 1: First 3-digit number divisible by 7 is 105; last is 994.\nStep 2: AP: 105, 112, ..., 994 with a = 105, d = 7, an = 994.\nStep 3: 994 = 105 + (n - 1)7 => 889 = 7(n - 1).\nStep 4: n - 1 = 127 => n = 128."
  },
  {
    "id": "10000000-0000-0000-0005-000000000027",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "17",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q17] Find the 20th term from the last term of the AP: 3, 8, 13, ..., 253.",
    "options": [
      {
        "id": "A",
        "text": "158",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "163",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "153",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "148",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Reverse AP from the end: 253, 248, 243, ..., 3.\nStep 2: First term a = 253, common difference d = -5.\nStep 3: a20 = a + 19d = 253 + 19(-5) = 253 - 95 = 158."
  },
  {
    "id": "10000000-0000-0000-0005-000000000028",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.2",
    "questionNumber": "19",
    "difficulty": "medium",
    "text": "[Exercise 5.2 - Q19] Subba Rao started work in 1995 at an annual salary of ₹ 5000 and received an increment of ₹ 200 each year. In which year did his income reach ₹ 7000?",
    "options": [
      {
        "id": "A",
        "text": "11th year (Year 2005)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "10th year (Year 2004)",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "12th year (Year 2006)",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "9th year (Year 2003)",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Series forms an AP: 5000, 5200, 5400, ..., 7000 with a = 5000, d = 200, an = 7000.\nStep 2: 7000 = 5000 + (n - 1)200 => 2000 = 200(n - 1) => n - 1 = 10 => n = 11.\nStep 3: 11th year from 1995: 1995 + (11 - 1) = 2005."
  },
  {
    "id": "10000000-0000-0000-0005-000000000029",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "1(i)",
    "difficulty": "easy",
    "text": "[Exercise 5.3 - Q1(i)] Find the sum of the AP: 2, 7, 12, ... to 10 terms.",
    "options": [
      {
        "id": "A",
        "text": "245",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "250",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "240",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "255",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 2, d = 5, n = 10.\nStep 2: Sn = (n/2)[2a + (n - 1)d].\nStep 3: S10 = (10/2)[2(2) + 9(5)] = 5[4 + 45] = 5(49) = 245."
  },
  {
    "id": "10000000-0000-0000-0005-000000000030",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "1(ii)",
    "difficulty": "easy",
    "text": "[Exercise 5.3 - Q1(ii)] Find the sum of the AP: -37, -33, -29, ... to 12 terms.",
    "options": [
      {
        "id": "A",
        "text": "-180",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "-192",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "-168",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "-200",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = -37, d = 4, n = 12.\nStep 2: S12 = (12/2)[2(-37) + 11(4)] = 6[-74 + 44] = 6(-30) = -180."
  },
  {
    "id": "10000000-0000-0000-0005-000000000031",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "2(i)",
    "difficulty": "medium",
    "text": "[Exercise 5.3 - Q2(i)] Find the sum: 7 + 10 1/2 + 14 + ... + 84.",
    "options": [
      {
        "id": "A",
        "text": "1046 1/2 (1046.5)",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "1040",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "1050 1/2",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "1036",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 7, d = 7/2, l = an = 84.\nStep 2: 84 = 7 + (n - 1)(7/2) => 77 = (7/2)(n - 1) => n - 1 = 22 => n = 23.\nStep 3: S23 = (n/2)(a + l) = (23/2)(7 + 84) = (23 × 91)/2 = 2093/2 = 1046 1/2."
  },
  {
    "id": "10000000-0000-0000-0005-000000000032",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "4",
    "difficulty": "hard",
    "text": "[Exercise 5.3 - Q4] How many terms of the AP: 9, 17, 25, ... must be taken to give a sum of 636?",
    "options": [
      {
        "id": "A",
        "text": "12 terms",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "14 terms",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "10 terms",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "16 terms",
        "is_correct": false
      }
    ],
    "solution": "Step 1: a = 9, d = 8, Sn = 636.\nStep 2: 636 = (n/2)[2(9) + (n - 1)8] = n(4n + 5) => 4n² + 5n - 636 = 0.\nStep 3: Factorise: (n - 12)(4n + 53) = 0 => n = 12 (since n > 0).\nHence, 12 terms must be taken."
  },
  {
    "id": "10000000-0000-0000-0005-000000000033",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "7",
    "difficulty": "medium",
    "text": "[Exercise 5.3 - Q7] Find the sum of first 22 terms of an AP in which d = 7 and 22nd term is 149.",
    "options": [
      {
        "id": "A",
        "text": "1661",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "1650",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "1672",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "1640",
        "is_correct": false
      }
    ],
    "solution": "Step 1: n = 22, d = 7, a22 = 149.\nStep 2: a + 21(7) = 149 => a + 147 = 149 => a = 2.\nStep 3: S22 = (22/2)[a + a22] = 11[2 + 149] = 11 × 151 = 1661."
  },
  {
    "id": "10000000-0000-0000-0005-000000000034",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "12",
    "difficulty": "medium",
    "text": "[Exercise 5.3 - Q12] Find the sum of the first 40 positive integers divisible by 6.",
    "options": [
      {
        "id": "A",
        "text": "4920",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "4860",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "4980",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "4800",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Integers divisible by 6 are: 6, 12, 18, ... to 40 terms.\nStep 2: a = 6, d = 6, n = 40.\nStep 3: S40 = (40/2)[2(6) + 39(6)] = 20[12 + 234] = 20 × 246 = 4920."
  },
  {
    "id": "10000000-0000-0000-0005-000000000035",
    "subject": "math",
    "chapterId": "math_ch_05_arithmetic_progressions",
    "exercise": "Exercise 5.3",
    "questionNumber": "14",
    "difficulty": "medium",
    "text": "[Exercise 5.3 - Q14] Find the sum of the odd numbers between 0 and 50.",
    "options": [
      {
        "id": "A",
        "text": "625",
        "is_correct": true
      },
      {
        "id": "B",
        "text": "600",
        "is_correct": false
      },
      {
        "id": "C",
        "text": "650",
        "is_correct": false
      },
      {
        "id": "D",
        "text": "576",
        "is_correct": false
      }
    ],
    "solution": "Step 1: Odd numbers between 0 and 50: 1, 3, 5, ..., 49.\nStep 2: a = 1, d = 2, an = 49 => 49 = 1 + (n - 1)2 => 2(n - 1) = 48 => n = 25.\nStep 3: S25 = (25/2)(1 + 49) = (25 × 50)/2 = 25 × 25 = 625."
  }
];

function generateSampleQuestionsForChapter(chId) {
      if (chId === 'math_ch_05_arithmetic_progressions') {
        return JSON.parse(JSON.stringify(ch5SampleQuestions));
      }

      if (chId === 'math_ch_04_quadratic_equations') {
        return JSON.parse(JSON.stringify(ch4SampleQuestions));
      }

      if (chId === 'math_ch_03_linear_equations') {
        return JSON.parse(JSON.stringify(ch3SampleQuestions));
      }

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
            solution: 'Step 1: The number of zeroes of polynomial p(x) is the number of points where the graph intersects the x-axis.\nStep 2: The given line is horizontal and never intersects the x-axis.\nStep 3: Hence, the number of zeroes is 0.'
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
            solution: 'Step 1: Count intersections with the x-axis: 1 point.\nStep 2: Intersections with y-axis are not zeroes of p(x).\nStep 3: Therefore, the number of zeroes is 1.'
          },
          {
            id: 'pdf-poly-3',
            subject: 'math',
            chapterId: chId,
            exercise: 'Exercise 2.1',
            questionNumber: '1(iii)',
            difficulty: 'easy',
            text: '[Exercise 2.1 - Q1(iii)] The curve of y = p(x) intersects the x-axis at 3 points. Find the number of zeroes.',
            options: [
              { id: 'A', text: '3 zeroes', is_correct: true },
              { id: 'B', text: '2 zeroes', is_correct: false },
              { id: 'C', text: '1 zero', is_correct: false },
              { id: 'D', text: '4 zeroes', is_correct: false }
            ],
            solution: 'Step 1: Count x-axis intersections: exactly 3 points.\nStep 2: Hence, the polynomial has 3 zeroes.'
          },
          {
            id: 'pdf-poly-4',
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
            solution: 'Step 1: Factorise: x² - 2x - 8 = (x - 4)(x + 2) = 0 => x = 4, x = -2.\nStep 2: Sum of zeroes = 4 + (-2) = 2 = -(-2)/1 = -b/a.\nStep 3: Product of zeroes = 4 × (-2) = -8 = c/a.\nRelationship verified!'
          },
          {
            id: 'pdf-poly-5',
            subject: 'math',
            chapterId: chId,
            exercise: 'Exercise 2.2',
            questionNumber: '1(ii)',
            difficulty: 'medium',
            text: '[Exercise 2.2 - Q1(ii)] Find the zeroes of the quadratic polynomial 4s² - 4s + 1 and verify the relationship.',
            options: [
              { id: 'A', text: 'Zeroes: 1/2 and 1/2; Sum = 1, Product = 1/4', is_correct: true },
              { id: 'B', text: 'Zeroes: -1/2 and -1/2; Sum = -1, Product = 1/4', is_correct: false },
              { id: 'C', text: 'Zeroes: 2 and 2; Sum = 4, Product = 4', is_correct: false },
              { id: 'D', text: 'Zeroes: 1 and 1/4; Sum = 5/4, Product = 1/4', is_correct: false }
            ],
            solution: 'Step 1: 4s² - 4s + 1 = (2s - 1)² = 0 => s = 1/2, 1/2.\nStep 2: Sum of zeroes = 1/2 + 1/2 = 1 = -(-4)/4 = -b/a.\nStep 3: Product of zeroes = 1/2 × 1/2 = 1/4 = c/a. Verified!'
          },
          {
            id: 'pdf-poly-6',
            subject: 'math',
            chapterId: chId,
            exercise: 'Exercise 2.2',
            questionNumber: '2(i)',
            difficulty: 'medium',
            text: '[Exercise 2.2 - Q2(i)] Find a quadratic polynomial with given sum and product of its zeroes: Sum = 1/4, Product = -1.',
            options: [
              { id: 'A', text: '4x² - x - 4', is_correct: true },
              { id: 'B', text: '4x² + x - 4', is_correct: false },
              { id: 'C', text: 'x² - 4x - 1', is_correct: false },
              { id: 'D', text: '4x² - x + 4', is_correct: false }
            ],
            solution: 'Step 1: Quadratic polynomial formula: k[x² - (α + β)x + αβ].\nStep 2: Substitute: k[x² - (1/4)x - 1] = (k/4)[4x² - x - 4].\nStep 3: Taking k = 4, the required polynomial is 4x² - x - 4.'
          }
        ];
      }

      if (chId === 'math_ch_01_real_numbers') {
        const ch1 = questions.filter(q => q.chapterId === 'math_ch_01_real_numbers');
        if (ch1.length > 0) return JSON.parse(JSON.stringify(ch1));
      }

      // Realistic multi-exercise generation for any other chapter
      const ch = mathChapters.find(c => c.id === chId) || mathChapters[0];
      return [
        {
          id: 'pdf-' + ch.id + '-1',
          subject: 'math',
          chapterId: ch.id,
          exercise: 'Exercise 1',
          questionNumber: '1',
          difficulty: 'easy',
          text: `[Exercise 1 - Q1] Based on NCERT syllabus for ${ch.titleEn} (${ch.titleKn}): Apply core definition and state the foundational result.`,
          options: [
            { id: 'A', text: `Primary textbook standard result for ${ch.titleEn}`, is_correct: true },
            { id: 'B', text: 'Alternative interpretation B', is_correct: false },
            { id: 'C', text: 'Alternative interpretation C', is_correct: false },
            { id: 'D', text: 'Alternative interpretation D', is_correct: false }
          ],
          solution: `Step 1: State definition for ${ch.titleEn}.\nStep 2: Deduce result step-by-step.\nStep 3: Verified with NCERT reprint 2026-27.`
        },
        {
          id: 'pdf-' + ch.id + '-2',
          subject: 'math',
          chapterId: ch.id,
          exercise: 'Exercise 1',
          questionNumber: '2',
          difficulty: 'medium',
          text: `[Exercise 1 - Q2] Solve the standard textbook application problem for ${ch.titleEn}.`,
          options: [
            { id: 'A', text: 'Calculated outcome A (Correct Solution)', is_correct: true },
            { id: 'B', text: 'Calculated outcome B', is_correct: false },
            { id: 'C', text: 'Calculated outcome C', is_correct: false },
            { id: 'D', text: 'Calculated outcome D', is_correct: false }
          ],
          solution: `Step 1: Formulate equation according to ${ch.titleEn}.\nStep 2: Simplify algebraic steps.\nStep 3: Result obtained.`
        },
        {
          id: 'pdf-' + ch.id + '-3',
          subject: 'math',
          chapterId: ch.id,
          exercise: 'Exercise 2',
          questionNumber: '1',
          difficulty: 'medium',
          text: `[Exercise 2 - Q1] Formulate the mathematical model and solve the exercise question for ${ch.titleEn}.`,
          options: [
            { id: 'A', text: 'Verified model outcome (Correct)', is_correct: true },
            { id: 'B', text: 'Model outcome B', is_correct: false },
            { id: 'C', text: 'Model outcome C', is_correct: false },
            { id: 'D', text: 'Model outcome D', is_correct: false }
          ],
          solution: `Step 1: Write down given values.\nStep 2: Substitute into formula.\nStep 3: Conclude answer.`
        },
        {
          id: 'pdf-' + ch.id + '-4',
          subject: 'math',
          chapterId: ch.id,
          exercise: 'Exercise 2',
          questionNumber: '2',
          difficulty: 'hard',
          text: `[Exercise 2 - Q2] Prove the theoretical assertion from the review exercise for ${ch.titleEn}.`,
          options: [
            { id: 'A', text: 'Rigorous theorem proof complete', is_correct: true },
            { id: 'B', text: 'Incomplete proof proposition', is_correct: false },
            { id: 'C', text: 'Counterexample contradiction', is_correct: false },
            { id: 'D', text: 'Undefined proposition', is_correct: false }
          ],
          solution: `Step 1: State hypothesis.\nStep 2: Apply properties.\nStep 3: Theorem successfully proved.`
        }
      ];
    }

    function publishPdfQuestionsLive(status) {
      if (!pdfGeneratedQuestions || pdfGeneratedQuestions.length === 0) {
        alert('No questions to publish.');
        return;
      }

      const chId = adminTargetChapterId;
      const count = pdfGeneratedQuestions.length;

      if (status === 'approved') {
        // Clear previous questions for this chapter to prevent duplicate stacking / memory leak
        questions = questions.filter(q => q.chapterId !== chId);

        // Prepend fresh newly approved questions
        pdfGeneratedQuestions.forEach((q, i) => {
          questions.unshift({
            id: 'live-' + Date.now() + '-' + i,
            subject: 'math',
            chapterId: chId,
            exercise: q.exercise,
            questionNumber: q.questionNumber,
            difficulty: q.difficulty,
            text: q.text,
            options: q.options,
            solution: q.solution
          });
        });

        // CRITICAL: Post-publish, clear memory completely!
        pdfGeneratedQuestions = [];
        pdfGenerationProgress = 0;
        pdfGenerationStatusText = '';

        alert(`🚀 Success! Published ${count} approved questions directly to student feed for chapter: ${chId}. Memory cleared.`);
        openChapterPractice(chId);
      } else {
        pdfGeneratedQuestions.forEach((q, i) => {
          pending.unshift({
            id: 'mod-' + Date.now() + '-' + i,
            chapter: chId,
            difficulty: q.difficulty,
            text: q.text
          });
        });

        // CRITICAL: Clear memory completely!
        pdfGeneratedQuestions = [];
        pdfGenerationProgress = 0;
        pdfGenerationStatusText = '';

        alert(`🛡️ Sent ${count} questions to moderation queue. Memory cleared.`);
        adminHubTab = 'queue';
        navTo('admin');
      }
    }

    function approveQueueItem(idx) {
      const item = pending.splice(idx, 1)[0];
      questions.unshift(item);
      navTo('admin');
    }

    function rejectQueueItem(idx) {
      pending.splice(idx, 1);
      navTo('admin');
    }

    // Initialize
    navTo('home');
  