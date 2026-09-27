-- ==============================================================================
-- Migration: 20260925020000_seed_math_chapters.sql
-- Project: CBSE Class 10 Masterclass
-- Description: Master Chapters Table, Row Level Security, and 14 Bilingual Math Seeds
-- ==============================================================================

-- 1. Create Chapters Table
CREATE TABLE IF NOT EXISTS public.chapters (
    id TEXT PRIMARY KEY,
    chapter_number INTEGER NOT NULL,
    subject TEXT NOT NULL CHECK (subject IN ('math', 'science', 'social_science')),
    title_en TEXT NOT NULL,
    title_kn TEXT NOT NULL,
    summary TEXT,
    formulas JSONB DEFAULT '[]'::jsonb,
    total_questions INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ NOT NULL DEFAULT TIMEZONE('utc'::text, NOW())
);

-- Indexes for fast querying
CREATE INDEX IF NOT EXISTS idx_chapters_subject ON public.chapters(subject);
CREATE INDEX IF NOT EXISTS idx_chapters_number ON public.chapters(chapter_number);

-- 2. Row Level Security (RLS)
ALTER TABLE public.chapters ENABLE ROW LEVEL SECURITY;

-- Read policy: Anyone (students, teachers, admins) can view chapters
DROP POLICY IF EXISTS "Public read chapters" ON public.chapters;
CREATE POLICY "Public read chapters" 
ON public.chapters FOR SELECT 
USING (true);

-- Admin manage policy: Only admin users can insert, update, or delete chapters
DROP POLICY IF EXISTS "Admin manage chapters" ON public.chapters;
CREATE POLICY "Admin manage chapters" 
ON public.chapters FOR ALL 
USING (
    EXISTS (
        SELECT 1 FROM public.profiles 
        WHERE id = auth.uid() AND role = 'admin'
    )
);

-- 3. Seed All 14 CBSE Class 10 Mathematics Chapters (Bilingual English + Kannada)
INSERT INTO public.chapters (id, chapter_number, subject, title_en, title_kn, summary, formulas)
VALUES
(
    'math_ch_01_real_numbers',
    1,
    'math',
    'Real Numbers',
    'ವಾಸ್ತವ ಸಂಖ್ಯೆಗಳು',
    'Fundamental Theorem of Arithmetic, irrationality proofs, prime factorization, and HCF-LCM relationships.',
    '[
        "Fundamental Theorem of Arithmetic: Every composite number can be uniquely expressed as a product of primes, apart from the order in which prime factors occur.",
        "Relationship: HCF(a, b) × LCM(a, b) = a × b",
        "Irrationality Proof: Assume √p = a/b (where a and b are co-prime integers, b ≠ 0). Prove a and b share a common factor to reach contradiction.",
        "Decimal Expansions: Let x = p/q be rational. If prime factorization of q is of the form 2^n · 5^m, x has a terminating decimal expansion."
    ]'::jsonb
),
(
    'math_ch_02_polynomials',
    2,
    'math',
    'Polynomials',
    'ಬಹುಪದೋಕ್ತಿಗಳು',
    'Zeroes of polynomials, relationship between zeroes and coefficients of quadratic polynomials.',
    '[
        "Standard Quadratic Form: p(x) = ax² + bx + c (a ≠ 0)",
        "Sum of zeroes: α + β = -b / a = -(Coefficient of x) / (Coefficient of x²)",
        "Product of zeroes: α · β = c / a = (Constant term) / (Coefficient of x²)",
        "Forming a polynomial: p(x) = k[x² - (α + β)x + αβ]"
    ]'::jsonb
),
(
    'math_ch_03_linear_equations',
    3,
    'math',
    'Pair of Linear Equations in Two Variables',
    'ಎರಡು ಚರಾಕ್ಷರಗಳಿರುವ ರೇಖಾತ್ಮಕ ಸಮೀಕರಣಗಳ ಜೋಡಿಗಳು',
    'Graphical and algebraic methods: substitution, elimination, and consistency condition ratios.',
    '[
        "Standard Pair: a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0",
        "Intersecting lines (Unique solution): a₁/a₂ ≠ b₁/b₂ (Consistent)",
        "Coincident lines (Infinitely many solutions): a₁/a₂ = b₁/b₂ = c₁/c₂ (Dependent & Consistent)",
        "Parallel lines (No solution): a₁/a₂ = b₁/b₂ ≠ c₁/c₂ (Inconsistent)"
    ]'::jsonb
),
(
    'math_ch_04_quadratic_equations',
    4,
    'math',
    'Quadratic Equations',
    'ವರ್ಗ ಸಮೀಕರಣಗಳು',
    'Standard form, factorization, quadratic formula, and discriminant nature of roots.',
    '[
        "Standard Form: ax² + bx + c = 0 (where a ≠ 0)",
        "Discriminant: D = b² - 4ac",
        "Quadratic Formula (Sridharacharya): x = (-b ± √D) / (2a)",
        "Nature of Roots: If D > 0 (two distinct real roots); If D = 0 (two equal real roots: -b/2a); If D < 0 (no real roots)"
    ]'::jsonb
),
(
    'math_ch_05_arithmetic_progressions',
    5,
    'math',
    'Arithmetic Progressions',
    'ಸಮಾಂತರ ಶ್ರೇಢಿಗಳು',
    'nth term of an AP, common difference, and sum of first n terms with practical applications.',
    '[
        "nth Term: a_n = a + (n - 1)d",
        "Common Difference: d = a_(k+1) - a_k",
        "Sum of first n terms: S_n = (n / 2) [2a + (n - 1)d]",
        "Alternative Sum formula: S_n = (n / 2) [a + l], where l = last term = a_n",
        "nth term from sum: a_n = S_n - S_(n-1)"
    ]'::jsonb
),
(
    'math_ch_06_triangles',
    6,
    'math',
    'Triangles',
    'ತ್ರಿಭುಜಗಳು',
    'Basic Proportionality Theorem (Thales), criteria for similarity of triangles (AAA, SSS, SAS).',
    '[
        "Basic Proportionality Theorem (BPT): If a line is drawn parallel to one side of a triangle intersecting other two sides, then AD/DB = AE/EC",
        "Converse of BPT: If a line divides any two sides of a triangle in the same ratio, then the line is parallel to the third side.",
        "Similarity Criteria: AAA (or AA), SSS, and SAS similarity rules"
    ]'::jsonb
),
(
    'math_ch_07_coordinate_geometry',
    7,
    'math',
    'Coordinate Geometry',
    'ನಿರ್ದೇಶಾಂಕ ರೇಖಾಗಣಿತ',
    'Distance formula, section formula (internal division), and midpoint coordinates.',
    '[
        "Distance Formula: d = √[(x₂ - x₁)² + (y₂ - y₁)²]",
        "Distance from Origin: d = √(x² + y²)",
        "Section Formula: P(x, y) = ((m₁x₂ + m₂x₁) / (m₁ + m₂), (m₁y₂ + m₂y₁) / (m₁ + m₂))",
        "Midpoint Formula: M = ((x₁ + x₂) / 2, (y₁ + y₂) / 2)"
    ]'::jsonb
),
(
    'math_ch_08_intro_trigonometry',
    8,
    'math',
    'Introduction to Trigonometry',
    'ತ್ರಿಕೋನಮಿತಿಯ ಪ್ರಸ್ತಾವನೆ',
    'Trigonometric ratios, values of standard angles (0°, 30°, 45°, 60°, 90°), and Pythagorean identities.',
    '[
        "Definitions: sin θ = Opp/Hyp, cos θ = Adj/Hyp, tan θ = Opp/Adj = sin θ / cos θ",
        "Reciprocal Ratios: cosec θ = 1/sin θ, sec θ = 1/cos θ, cot θ = 1/tan θ",
        "Pythagorean Identity 1: sin² θ + cos² θ = 1",
        "Pythagorean Identity 2: 1 + tan² θ = sec² θ (for 0° ≤ θ < 90°)",
        "Pythagorean Identity 3: 1 + cot² θ = cosec² θ (for 0° < θ ≤ 90°)",
        "Standard Values: sin 30° = 1/2, sin 45° = 1/√2, sin 60° = √3/2, cos 60° = 1/2, tan 45° = 1"
    ]'::jsonb
),
(
    'math_ch_09_applications_trigonometry',
    9,
    'math',
    'Some Applications of Trigonometry',
    'ತ್ರಿಕೋನಮಿತಿಯ ಕೆಲವು ಅನ್ವಯಗಳು',
    'Heights and distances, angles of elevation and depression, line of sight calculations.',
    '[
        "Angle of Elevation: Angle formed by the line of sight with the horizontal when the point observed is above the horizontal level.",
        "Angle of Depression: Angle formed by the line of sight with the horizontal when the point is below the horizontal level.",
        "Calculation: Height = Distance × tan θ (when right-angled triangle base is known)"
    ]'::jsonb
),
(
    'math_ch_10_circles',
    10,
    'math',
    'Circles',
    'ವೃತ್ತಗಳು',
    'Tangent to a circle, number of tangents from a point, and equality of lengths of tangents from external point.',
    '[
        "Theorem 1: The tangent at any point of a circle is perpendicular to the radius through the point of contact (OP ⊥ AB).",
        "Theorem 2: The lengths of tangents drawn from an external point to a circle are equal (PQ = PR).",
        "Angle Relation: The angle between the two tangents drawn from an external point to a circle is supplementary to the angle subtended by the line segment joining the points of contact at the centre."
    ]'::jsonb
),
(
    'math_ch_11_areas_related_to_circles',
    11,
    'math',
    'Areas Related to Circles',
    'ವೃತ್ತಗಳಿಗೆ ಸಂಬಂಧಿಸಿದ ವಿಸ್ತೀರ್ಣಗಳು',
    'Perimeter and area of a circle, area of sector, and area of segment of a circle.',
    '[
        "Circumference = 2πr; Area = πr²",
        "Area of Sector of angle θ: Area = (θ / 360°) × πr²",
        "Length of Arc of sector of angle θ: l = (θ / 360°) × 2πr",
        "Area of Segment = Area of corresponding Sector - Area of corresponding Triangle"
    ]'::jsonb
),
(
    'math_ch_12_surface_areas_volumes',
    12,
    'math',
    'Surface Areas and Volumes',
    'ಮೇಲ್ಮೈ ವಿಸ್ತೀರ್ಣಗಳು ಮತ್ತು ಘನಫಲಗಳು',
    'Surface areas and volumes of combinations of solids: cuboid, cube, cylinder, cone, and sphere.',
    '[
        "Cylinder: CSA = 2πrh, TSA = 2πr(r + h), Volume = πr²h",
        "Cone: Slant height l = √(r² + h²), CSA = πrl, TSA = πr(l + r), Volume = (1/3)πr²h",
        "Sphere: Surface Area = 4πr², Volume = (4/3)πr³",
        "Hemisphere: CSA = 2πr², TSA = 3πr², Volume = (2/3)πr³",
        "Combination of solids: Total Surface Area is calculated strictly along the exposed outer boundaries."
    ]'::jsonb
),
(
    'math_ch_13_statistics',
    13,
    'math',
    'Statistics',
    'ಸಂಖ್ಯಾಶಾಸ್ತ್ರ',
    'Mean, Median, and Mode of grouped data, modal class, median class, and empirical formula.',
    '[
        "Direct Mean: x̄ = Σ(fᵢxᵢ) / Σfᵢ",
        "Assumed Mean: x̄ = a + [Σ(fᵢdᵢ) / Σfᵢ], where dᵢ = xᵢ - a",
        "Step Deviation: x̄ = a + [Σ(fᵢuᵢ) / Σfᵢ] × h, where uᵢ = (xᵢ - a)/h",
        "Mode = l + [(f₁ - f₀) / (2f₁ - f₀ - f₂)] × h",
        "Median = l + [((n / 2) - cf) / f] × h",
        "Empirical Relationship: 3 Median = Mode + 2 Mean"
    ]'::jsonb
),
(
    'math_ch_14_probability',
    14,
    'math',
    'Probability',
    'ಸಂಭವನೀಯತೆ',
    'Classical definition of probability, elementary events, complementary events, and impossible/sure events.',
    '[
        "Theoretical Probability: P(E) = (Number of outcomes favourable to E) / (Number of all possible outcomes of the experiment)",
        "Probability Range: 0 ≤ P(E) ≤ 1",
        "Complementary Event: P(E) + P(not E) = 1 => P(Ē) = 1 - P(E)",
        "Impossible Event: P(impossible) = 0",
        "Sure / Certain Event: P(sure) = 1"
    ]'::jsonb
)
ON CONFLICT (id) DO UPDATE SET
    title_en = EXCLUDED.title_en,
    title_kn = EXCLUDED.title_kn,
    summary = EXCLUDED.summary,
    formulas = EXCLUDED.formulas;
