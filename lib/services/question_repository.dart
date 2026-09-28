import 'package:flutter/foundation.dart';
import '../core/constants/cbse_curriculum.dart';
import '../core/constants/supabase_constants.dart';
import '../models/chapter.dart';
import '../models/question.dart';
import 'local_cache_service.dart';
import 'ncert_math_ch1_data.dart';
import 'ncert_math_ch3_data.dart';
import 'ncert_math_ch4_data.dart';
import 'ncert_math_ch5_data.dart';
import 'ncert_science_ch1_data.dart';
import 'ncert_science_ch2_data.dart';
import 'ncert_science_ch3_data.dart';
import 'ncert_science_ch4_data.dart';
import 'ncert_science_ch5_data.dart';
import 'supabase_service.dart';

/// Question Repository orchestrating remote Supabase queries and Hive local caching
class QuestionRepository {
  final SupabaseService _supabaseService;
  final LocalCacheService _cacheService;

  // In-memory store for seamless offline/dev emulation
  final List<Question> _inMemoryQuestions = [];

  QuestionRepository({
    SupabaseService? supabaseService,
    LocalCacheService? cacheService,
  })  : _supabaseService = supabaseService ?? SupabaseService.instance,
        _cacheService = cacheService ?? LocalCacheService.instance {
    _initDefaultSeedData();
    _inMemoryQuestions.addAll(NcertMathCh1Data.questions);
    _inMemoryQuestions.addAll(ncertMathCh3Questions);
    _inMemoryQuestions.addAll(ncertMathCh4Questions);
    _inMemoryQuestions.addAll(ncertMathCh5Questions);
    _inMemoryQuestions.addAll(NcertScienceCh1Data.questions);
    _inMemoryQuestions.addAll(NcertScienceCh2Data.questions);
    _inMemoryQuestions.addAll(NcertScienceCh3Data.questions);
    _inMemoryQuestions.addAll(NcertScienceCh4Data.questions);
    _inMemoryQuestions.addAll(NcertScienceCh5Data.questions);
    _loadNcertChapter1PendingQuestions();
  }

  /// Initialize default high-yield questions for offline & instant readiness
  void _initDefaultSeedData() {
    _inMemoryQuestions.addAll([
      // Approved Math - Chapter 2: Polynomials
      Question(
        id: '10000000-0000-0000-0000-000000000021',
        subject: Subject.math,
        chapterId: 'math_ch_02_polynomials',
        questionText:
            'If one zero of the quadratic polynomial p(x) = x² + 3x + k is 2, then the value of k is:',
        options: const [
          QuestionOption(id: 'A', text: '10', isCorrect: false),
          QuestionOption(id: 'B', text: '-10', isCorrect: true),
          QuestionOption(id: 'C', text: '-7', isCorrect: false),
          QuestionOption(id: 'D', text: '-2', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: If 2 is a zero of p(x), then p(2) = 0.\nStep 2: Substitute x = 2: (2)² + 3(2) + k = 0.\nStep 3: 4 + 6 + k = 0 => 10 + k = 0.\nStep 4: k = -10.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.approved,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: '00000000-0000-0000-0000-000000000001',
        createdAt: DateTime.fromMillisecondsSinceEpoch(1726930000000),
      ),
      // Approved Math Q1
      Question(
        id: '10000000-0000-0000-0000-000000000001',
        subject: Subject.math,
        chapterId: 'ch_04_quadratic_equations',
        questionText:
            'Find the value of k for which the quadratic equation (k - 12)x² + 2(k - 12)x + 2 = 0 has two equal real roots, given k ≠ 12.',
        options: const [
          QuestionOption(id: 'A', text: 'k = 12', isCorrect: false),
          QuestionOption(id: 'B', text: 'k = 14', isCorrect: true),
          QuestionOption(id: 'C', text: 'k = 10', isCorrect: false),
          QuestionOption(id: 'D', text: 'k = 16', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Standard form ax² + bx + c = 0 has equal roots when discriminant D = b² - 4ac = 0.\nStep 2: Here a = (k - 12), b = 2(k - 12), c = 2.\nStep 3: D = [2(k - 12)]² - 4(k - 12)(2) = 0\nStep 4: 4(k - 12)² - 8(k - 12) = 0\nStep 5: Factor out 4(k - 12): 4(k - 12)[(k - 12) - 2] = 0\nStep 6: Either k - 12 = 0 => k = 12 (rejected as k ≠ 12) or k - 14 = 0 => k = 14.\nTherefore, k = 14.',
        difficultyLevel: DifficultyLevel.hots,
        status: QuestionStatus.approved,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: '00000000-0000-0000-0000-000000000001',
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727000000000),
      ),
      // Approved Math Q2
      Question(
        id: '10000000-0000-0000-0000-000000000002',
        subject: Subject.math,
        chapterId: 'ch_08_introduction_to_trigonometry',
        questionText:
            'If sin(θ) + cos(θ) = √3, find the value of sin(θ) · cos(θ).',
        options: const [
          QuestionOption(id: 'A', text: '1/2', isCorrect: false),
          QuestionOption(id: 'B', text: '1', isCorrect: true),
          QuestionOption(id: 'C', text: '√3/2', isCorrect: false),
          QuestionOption(id: 'D', text: '1/4', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Given sin(θ) + cos(θ) = √3\nStep 2: Square both sides: [sin(θ) + cos(θ)]² = 3\nStep 3: sin²(θ) + cos²(θ) + 2sin(θ)cos(θ) = 3\nStep 4: Since sin²(θ) + cos²(θ) = 1, we get: 1 + 2sin(θ)cos(θ) = 3\nStep 5: 2sin(θ)cos(θ) = 2 => sin(θ)cos(θ) = 1.',
        difficultyLevel: DifficultyLevel.medium,
        status: QuestionStatus.approved,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: '00000000-0000-0000-0000-000000000001',
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727050000000),
      ),
      // Pending Math Q3 (For Admin Moderation)
      Question(
        id: '10000000-0000-0000-0000-000000000003',
        subject: Subject.math,
        chapterId: 'ch_05_arithmetic_progressions',
        questionText:
            'In an AP, if the sum of the first n terms is given by Sn = 3n² + 5n, find the 20th term of this progression.',
        options: const [
          QuestionOption(id: 'A', text: '118', isCorrect: false),
          QuestionOption(id: 'B', text: '122', isCorrect: true),
          QuestionOption(id: 'C', text: '120', isCorrect: false),
          QuestionOption(id: 'D', text: '126', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: nth term a_n = S_n - S_(n-1)\nStep 2: a₂₀ = S₂₀ - S₁₉\nStep 3: S₂₀ = 3(400) + 100 = 1300\nStep 4: S₁₉ = 3(361) + 95 = 1178\nStep 5: a₂₀ = 1300 - 1178 = 122.',
        difficultyLevel: DifficultyLevel.hard,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727100000000),
      ),

      // Approved Science Q1: Physics Ray Diagram
      Question(
        id: '20000000-0000-0000-0000-000000000001',
        subject: Subject.science,
        chapterId: 'sci_ch_09_light_reflection_refraction',
        questionText:
            'An object is placed at a distance of 10 cm in front of a concave mirror of focal length 15 cm. What are the characteristics of the image formed?',
        options: const [
          QuestionOption(id: 'A', text: 'Real, inverted, and diminished', isCorrect: false),
          QuestionOption(id: 'B', text: 'Virtual, erect, and magnified', isCorrect: true),
          QuestionOption(id: 'C', text: 'Real, inverted, and magnified', isCorrect: false),
          QuestionOption(id: 'D', text: 'Virtual, erect, and same size', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Sign convention: f = -15 cm, u = -10 cm (between F and P).\nStep 2: 1/v = 1/f - 1/u = -1/15 - (-1/10) = -1/15 + 1/10 = +1/30.\nStep 3: v = +30 cm (formed behind the mirror).\nStep 4: Magnification m = -v/u = -30 / -10 = +3.\nStep 5: Since m is positive and > 1, the image is virtual, erect, and magnified.',
        difficultyLevel: DifficultyLevel.medium,
        status: QuestionStatus.approved,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: '00000000-0000-0000-0000-000000000001',
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727010000000),
      ),
      // Approved Science Q2: Chemistry Redox
      Question(
        id: '20000000-0000-0000-0000-000000000002',
        subject: Subject.science,
        chapterId: 'sci_ch_01_chemical_reactions_equations',
        questionText:
            'In the redox reaction: MnO₂ + 4HCl → MnCl₂ + 2H₂O + Cl₂, identify the substance oxidized and the oxidizing agent respectively.',
        options: const [
          QuestionOption(id: 'A', text: 'Oxidized: MnO₂, Oxidizing Agent: HCl', isCorrect: false),
          QuestionOption(id: 'B', text: 'Oxidized: HCl, Oxidizing Agent: MnO₂', isCorrect: true),
          QuestionOption(id: 'C', text: 'Oxidized: Cl₂, Oxidizing Agent: MnCl₂', isCorrect: false),
          QuestionOption(id: 'D', text: 'Oxidized: MnO₂, Oxidizing Agent: H₂O', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Oxidation involves removal of hydrogen or addition of oxygen.\nStep 2: In HCl, hydrogen is removed to yield Cl₂; thus HCl is oxidized.\nStep 3: MnO₂ loses oxygen to form MnCl₂; thus MnO₂ is reduced.\nStep 4: The reduced substance is the oxidizing agent. Hence, MnO₂ is oxidizing agent and HCl is oxidized.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.approved,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: '00000000-0000-0000-0000-000000000001',
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727060000000),
      ),
      // Pending Science Q3 (For Admin Moderation)
      Question(
        id: '20000000-0000-0000-0000-000000000003',
        subject: Subject.science,
        chapterId: 'sci_ch_06_life_processes',
        questionText:
            'Which component of the human nephron is primarily responsible for selective reabsorption of glucose, amino acids, and major amounts of water?',
        options: const [
          QuestionOption(id: 'A', text: "Bowman's capsule", isCorrect: false),
          QuestionOption(id: 'B', text: 'Glomerulus', isCorrect: false),
          QuestionOption(id: 'C', text: 'Tubular part of nephron (PCT / Henle loop)', isCorrect: true),
          QuestionOption(id: 'D', text: 'Collecting duct only', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Ultrafiltration occurs at the glomerulus into Bowman’s capsule.\nStep 2: Initial filtrate passes through the tubular part (PCT and Henle loop).\nStep 3: Glucose, amino acids, salts, and water are selectively reabsorbed by surrounding capillary networks.\nStep 4: Remaining liquid forms concentrated urine.',
        difficultyLevel: DifficultyLevel.medium,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727120000000),
      ),

      // Approved Social Science Q1: History
      Question(
        id: '30000000-0000-0000-0000-000000000001',
        subject: Subject.socialScience,
        chapterId: 'sst_hist_ch_02_nationalism_in_india',
        questionText:
            'Why did Mahatma Gandhi decide to withdraw the Non-Cooperation Movement in February 1922?',
        options: const [
          QuestionOption(id: 'A', text: 'Passing of the Rowlatt Act', isCorrect: false),
          QuestionOption(id: 'B', text: 'The violent clash at Chauri Chaura', isCorrect: true),
          QuestionOption(id: 'C', text: 'Execution of Bhagat Singh', isCorrect: false),
          QuestionOption(id: 'D', text: 'Arrival of the Simon Commission', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: In February 1922 at Chauri Chaura (Gorakhpur, UP), a peaceful protest turned into a violent clash.\nStep 2: Protesters set fire to a police station, killing 22 policemen.\nStep 3: Gandhi observed that the movement was turning violent and satyagrahis needed further non-violence training.\nStep 4: He immediately halted the nationwide movement.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.approved,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: '00000000-0000-0000-0000-000000000001',
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727020000000),
      ),
      // Approved Social Science Q2: Geography Map
      Question(
        id: '30000000-0000-0000-0000-000000000002',
        subject: Subject.socialScience,
        chapterId: 'sst_geo_ch_07_lifelines_of_national_economy',
        questionText:
            'Which tidal port in Gujarat was developed soon after Independence to ease the volume of trade on Mumbai port following the loss of Karachi to Pakistan?',
        options: const [
          QuestionOption(id: 'A', text: 'Marmagao Port', isCorrect: false),
          QuestionOption(id: 'B', text: 'Kandla (Deendayal Port)', isCorrect: true),
          QuestionOption(id: 'C', text: 'Paradip Port', isCorrect: false),
          QuestionOption(id: 'D', text: 'Tuticorin Port', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Post-Partition, Karachi port went to Pakistan, overwhelming Mumbai port.\nStep 2: Kandla in Kachchh was developed as the first major port after Independence.\nStep 3: It is a tidal port catering to northern and north-western states.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.approved,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: '00000000-0000-0000-0000-000000000001',
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727070000000),
      ),
      // Pending Social Science Q3 (For Admin Moderation)
      Question(
        id: '30000000-0000-0000-0000-000000000003',
        subject: Subject.socialScience,
        chapterId: 'sst_civ_ch_02_federalism',
        questionText:
            'Under the 73rd Constitutional Amendment Act (1992), which provision was made mandatory for local self-government in India?',
        options: const [
          QuestionOption(id: 'A', text: 'Holding regular elections every 5 years & 1/3rd seats reserved for women', isCorrect: true),
          QuestionOption(id: 'B', text: 'Abolishing the State Election Commission', isCorrect: false),
          QuestionOption(id: 'C', text: 'Direct control of village panchayats by the Governor', isCorrect: false),
          QuestionOption(id: 'D', text: 'Exempting municipalities from state revenue sharing', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: The 73rd Amendment institutionalized Panchayati Raj.\nStep 2: Mandatory rules include: holding elections every 5 years, reserving at least 33% seats for women, establishing a State Election Commission, and statutory devolution of powers and revenue.',
        difficultyLevel: DifficultyLevel.medium,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727130000000),
      ),
    ]);
  }

  /// Ingested NCERT Class 10 Science Chapter 1 ("Chemical Reactions and Equations")
  /// Enforces status: QuestionStatus.pendingReview and chapterId: 'science_ch_1_chemical_reactions'
  void _loadNcertChapter1PendingQuestions() {
    _inMemoryQuestions.addAll([
      // 1. In-Text Page 6 Q1
      Question(
        id: '11000000-0000-0000-0000-000000000001',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'Why should a magnesium ribbon be cleaned before burning in air?',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'To remove the protective layer of basic magnesium oxide formed by reaction with moist air',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'To remove moisture and grease from human fingers',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'To decrease its ignition temperature',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'To make it burn with a colored flame instead of white',
              isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Magnesium is a chemically active metal.\nStep 2: When exposed to air, it reacts with atmospheric oxygen to form a thin, stable protective layer of basic magnesium oxide (MgO) on its surface.\nStep 3: This coating acts as a barrier that hinders further reaction with oxygen during combustion.\nStep 4: Cleaning the ribbon with sandpaper removes this oxide layer, allowing the metal to burn smoothly with a dazzling white flame.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727140000000),
      ),

      // 2. In-Text Page 6 Q2
      Question(
        id: '11000000-0000-0000-0000-000000000002',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'Write the balanced chemical equation for: Hydrogen + Chlorine → Hydrogen chloride',
        options: const [
          QuestionOption(id: 'A', text: 'H2 + Cl2 → 2HCl', isCorrect: true),
          QuestionOption(id: 'B', text: 'H + Cl → HCl', isCorrect: false),
          QuestionOption(id: 'C', text: '2H2 + 2Cl2 → 4HCl', isCorrect: false),
          QuestionOption(id: 'D', text: 'H2 + Cl2 → HCl2', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Skeletal equation: H2(g) + Cl2(g) → HCl(g)\nStep 2: Count atoms on LHS: H = 2, Cl = 2; on RHS: H = 1, Cl = 1.\nStep 3: Multiply HCl on RHS by coefficient 2.\nStep 4: Balanced Equation: H2(g) + Cl2(g) → 2HCl(g).',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727141000000),
      ),

      // 3. In-Text Page 6 Q3
      Question(
        id: '11000000-0000-0000-0000-000000000003',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'Write a balanced chemical equation with state symbols: Solutions of barium chloride and sodium sulphate in water react to give insoluble barium sulphate precipitate and sodium chloride solution.',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'BaCl2(aq) + Na2SO4(aq) → BaSO4(s)↓ + 2NaCl(aq)',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'BaCl2(s) + Na2SO4(aq) → BaSO4(aq) + NaCl(aq)',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'BaCl(aq) + NaSO4(aq) → BaSO4(s) + NaCl(aq)',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'BaCl2(aq) + 2Na2SO4(aq) → Ba(SO4)2(s) + 4NaCl(aq)',
              isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Reactants: BaCl2(aq) and Na2SO4(aq).\nStep 2: Products: White precipitate of BaSO4(s) and dissolved NaCl(aq).\nStep 3: Balance Na and Cl: BaCl2(aq) + Na2SO4(aq) → BaSO4(s)↓ + 2NaCl(aq).',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727142000000),
      ),

      // 4. In-Text Page 10 Q1
      Question(
        id: '11000000-0000-0000-0000-000000000004',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'A solution of substance \'X\' is used for whitewashing. (i) Name substance \'X\' and write its formula. (ii) Write the reaction of \'X\' with water.',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'X is Quicklime (Calcium oxide, CaO); Reaction: CaO(s) + H2O(l) → Ca(OH)2(aq)',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'X is Limestone (Calcium carbonate, CaCO3); Reaction: CaCO3 + H2O → Ca(OH)2 + CO2',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'X is Slaked lime (Calcium hydroxide, Ca(OH)2); Reaction: Ca(OH)2 + H2O → CaO + 2H2O',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'X is Plaster of Paris (CaSO4·1/2H2O)',
              isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Substance \'X\' used for whitewashing is Quicklime (Calcium oxide).\nStep 2: Formula: CaO.\nStep 3: Reaction with water: CaO(s) + H2O(l) → Ca(OH)2(aq) + Heat (exothermic combination).',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727143000000),
      ),

      // 5. In-Text Page 10 Q2
      Question(
        id: '11000000-0000-0000-0000-000000000005',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'Why is the volume of gas collected in one test tube during the electrolysis of water double the volume collected in the other? Name this gas.',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'Water (H2O) has 2 parts hydrogen to 1 part oxygen by volume; the gas is Hydrogen (collected at cathode)',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'Oxygen is denser than hydrogen; the double-volume gas is Oxygen',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'Hydrogen dissolves in water; the double gas is Oxygen',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'Electrons carry extra charge at the anode; the gas is Hydrogen',
              isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Chemical formula of water is H2O.\nStep 2: Decomposition equation: 2H2O(l) --[Electricity]--> 2H2(g) [Cathode] + O2(g) [Anode].\nStep 3: Two moles of H2 gas are produced for every one mole of O2 gas.\nStep 4: Molar ratio equals volume ratio. Therefore, the volume of Hydrogen gas collected at the cathode is double that of Oxygen at the anode.',
        difficultyLevel: DifficultyLevel.medium,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727144000000),
      ),

      // 6. In-Text Page 13 Q1
      Question(
        id: '11000000-0000-0000-0000-000000000006',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'Why does the blue colour of copper sulphate solution change when an iron nail is dipped into it?',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'Iron is more reactive than copper; it displaces copper forming pale green ferrous sulphate (FeSO4)',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'Copper displaces iron from solution, evaporating the blue pigment',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'Iron reacts with water to form basic iron hydroxide precipitate',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'Sulphate ions decompose into sulphur dioxide gas',
              isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: According to the reactivity series, iron (Fe) is more reactive than copper (Cu).\nStep 2: Single displacement reaction: Fe(s) + CuSO4(aq) [Blue] → FeSO4(aq) [Light Green] + Cu(s) [Reddish-brown].\nStep 3: Cu2+ ions responsible for the blue color are displaced and deposited on the nail, while Fe2+ ions dissolve, giving a pale green solution.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727145000000),
      ),

      // 7. NCERT Exercise Q1
      Question(
        id: '11000000-0000-0000-0000-000000000007',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'Which of the statements about the reaction: 2PbO(s) + C(s) → 2Pb(s) + CO2(g) are incorrect?\n(a) Lead is getting reduced.\n(b) Carbon dioxide is getting oxidised.\n(c) Carbon is getting oxidised.\n(d) Lead oxide is getting reduced.',
        options: const [
          QuestionOption(id: 'A', text: '(a) and (b)', isCorrect: true),
          QuestionOption(id: 'B', text: '(a) and (c)', isCorrect: false),
          QuestionOption(id: 'C', text: '(a), (b) and (c)', isCorrect: false),
          QuestionOption(id: 'D', text: 'All are incorrect', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: In the reaction 2PbO + C → 2Pb + CO2:\nStep 2: PbO loses oxygen to become Pb, so Lead oxide (PbO) is reduced (statement d is correct, statement a is incorrect).\nStep 3: Carbon (C) gains oxygen to become CO2, so Carbon is oxidised (statement c is correct, statement b is incorrect).\nStep 4: Therefore, statements (a) and (b) are incorrect. Option (A) is correct.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727146000000),
      ),

      // 8. NCERT Exercise Q2
      Question(
        id: '11000000-0000-0000-0000-000000000008',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'Fe2O3 + 2Al → Al2O3 + 2Fe. The above reaction is an example of a:',
        options: const [
          QuestionOption(id: 'A', text: 'combination reaction', isCorrect: false),
          QuestionOption(id: 'B', text: 'double displacement reaction', isCorrect: false),
          QuestionOption(id: 'C', text: 'decomposition reaction', isCorrect: false),
          QuestionOption(id: 'D', text: 'displacement reaction', isCorrect: true),
        ],
        stepByStepSolution:
            'Step 1: Aluminium (Al) is more reactive than iron (Fe).\nStep 2: Al displaces iron from ferric oxide (Fe2O3) to form aluminium oxide (Al2O3) and iron.\nStep 3: A more reactive element displaces a less reactive element from its compound. Thus, it is a displacement reaction.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727147000000),
      ),

      // 9. NCERT Exercise Q3
      Question(
        id: '11000000-0000-0000-0000-000000000009',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'What happens when dilute hydrochloric acid is added to iron filings?',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'Hydrogen gas and iron(II) chloride are produced',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'Chlorine gas and iron hydroxide are produced',
              isCorrect: false),
          QuestionOption(id: 'C', text: 'No reaction takes place', isCorrect: false),
          QuestionOption(
              id: 'D', text: 'Iron salt and water are produced', isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Iron (Fe) is more reactive than hydrogen.\nStep 2: Reaction: Fe(s) + 2HCl(aq) → FeCl2(aq) + H2(g)↑.\nStep 3: Hydrogen gas and iron(II) chloride are produced.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727148000000),
      ),

      // 10. NCERT Exercise Q10
      Question(
        id: '11000000-0000-0000-0000-000000000010',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'Why is respiration considered an exothermic reaction? Explain.',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'Glucose combines with oxygen in cells and releases carbon dioxide, water, and metabolic energy (ATP)',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'Lungs absorb external heat during inhalation',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'Blood friction generates heat energy',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'Respiration consumes ATP without releasing energy',
              isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Food carbohydrates are digested into glucose (C6H12O6).\nStep 2: In body cells, glucose combines with oxygen: C6H12O6(aq) + 6O2(aq) → 6CO2(aq) + 6H2O(l) + Energy.\nStep 3: Because energy is released to power vital biological functions, respiration is an exothermic reaction.',
        difficultyLevel: DifficultyLevel.medium,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727149000000),
      ),

      // 11. NCERT Exercise Q12
      Question(
        id: '11000000-0000-0000-0000-000000000011',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'Write equations for decomposition reactions where energy is supplied as heat, light, and electricity respectively.',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'Heat: CaCO3 → CaO + CO2; Light: 2AgCl → 2Ag + Cl2; Electricity: 2H2O → 2H2 + O2',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'Heat: 2H2 + O2 → 2H2O; Light: CH4 + 2O2 → CO2 + 2H2O; Electricity: Zn + HCl → ZnCl2 + H2',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'Heat: Fe + S → FeS; Light: H2 + Cl2 → 2HCl; Electricity: 2Na + Cl2 → 2NaCl',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'All decomposition reactions only require thermal heat',
              isCorrect: false),
        ],
        stepByStepSolution:
            '1. Thermal Decomposition (Heat):\nCaCO3(s) --[Heat]--> CaO(s) + CO2(g)\n\n2. Photolytic Decomposition (Light):\n2AgCl(s) --[Sunlight]--> 2Ag(s) + Cl2(g)\n\n3. Electrolytic Decomposition (Electricity):\n2H2O(l) --[Electricity]--> 2H2(g) + O2(g).',
        difficultyLevel: DifficultyLevel.hots,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727150000000),
      ),

      // 12. NCERT Exercise Q17
      Question(
        id: '11000000-0000-0000-0000-000000000012',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'A shiny brown coloured element \'X\' on heating in air becomes black in colour. Name element \'X\' and the black compound formed.',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'Element \'X\' is Copper (Cu); Black compound is Copper(II) oxide (CuO)',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'Element \'X\' is Iron (Fe); Black compound is Fe3O4',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'Element \'X\' is Carbon (C); Black compound is Coal',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'Element \'X\' is Lead (Pb); Black compound is PbO2',
              isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: The shiny brown-coloured element is Copper (Cu).\nStep 2: When heated in air, copper reacts with atmospheric oxygen to undergo oxidation.\nStep 3: Reaction: 2Cu(s) [Brown] + O2(g) --[Heat]--> 2CuO(s) [Black].\nStep 4: The black compound formed is Copper(II) oxide.',
        difficultyLevel: DifficultyLevel.medium,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727151000000),
      ),

      // 13. NCERT Exercise Q19
      Question(
        id: '11000000-0000-0000-0000-000000000013',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'Oil and fat containing food items are flushed with nitrogen. Why?',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'Nitrogen is an unreactive inert gas that displaces oxygen, preventing aerial oxidation of oils and fats (rancidity)',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'Nitrogen adds nutritional protein to packaged chips',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'Nitrogen lowers temperature to freezing point',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'Nitrogen is used only to inflate the packaging bag for look',
              isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Oils and fats in food react with atmospheric oxygen over time in a process called oxidation.\nStep 2: Oxidation causes oils and fats to become rancid, resulting in an unpleasant taste and foul odor.\nStep 3: Nitrogen is an inert, non-reactive gas. Flushing snack packets with nitrogen removes oxygen, preventing aerial oxidation and extending shelf life.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727152000000),
      ),

      // 14. NCERT Activity 1.2
      Question(
        id: '11000000-0000-0000-0000-000000000014',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'In Activity 1.2, lead nitrate solution is mixed with potassium iodide solution in a test tube. What precipitate forms and what is its color?',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'Bright yellow precipitate of Lead iodide (PbI2)',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'White precipitate of Potassium nitrate (KNO3)',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'Dark brown precipitate of Lead oxide (PbO)',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'Blue precipitate of Copper iodide',
              isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Reactants: Colorless Pb(NO3)2(aq) and colorless KI(aq).\nStep 2: Double displacement takes place.\nStep 3: Pb(NO3)2(aq) + 2KI(aq) → PbI2(s)↓ + 2KNO3(aq).\nStep 4: An immediate bright yellow precipitate of Lead(II) iodide (PbI2) is formed.',
        difficultyLevel: DifficultyLevel.easy,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727153000000),
      ),

      // 15. NCERT Activity 1.3
      Question(
        id: '11000000-0000-0000-0000-000000000015',
        subject: Subject.science,
        chapterId: 'science_ch_1_chemical_reactions',
        questionText:
            'In Activity 1.3, dilute sulphuric acid is added to zinc granules in a conical flask. Which observations confirm a chemical reaction has occurred?',
        options: const [
          QuestionOption(
              id: 'A',
              text: 'Brisk effervescence with evolution of hydrogen gas and the flask becomes hot (exothermic)',
              isCorrect: true),
          QuestionOption(
              id: 'B',
              text: 'Flask cools down drastically with precipitate formation',
              isCorrect: false),
          QuestionOption(
              id: 'C',
              text: 'Brown fumes of nitrogen dioxide evolve',
              isCorrect: false),
          QuestionOption(
              id: 'D',
              text: 'Zinc granules dissolve without gas evolution',
              isCorrect: false),
        ],
        stepByStepSolution:
            'Step 1: Reaction: Zn(s) + H2SO4(aq) → ZnSO4(aq) + H2(g)↑ + Heat.\nStep 2: Observation 1: Bubbles of hydrogen gas evolve rapidly around the zinc granules.\nStep 3: Observation 2: Touching the bottom of the flask reveals an increase in temperature, confirming an exothermic reaction.',
        difficultyLevel: DifficultyLevel.medium,
        status: QuestionStatus.pendingReview,
        submittedBy: '00000000-0000-0000-0000-000000000002',
        reviewedBy: null,
        createdAt: DateTime.fromMillisecondsSinceEpoch(1727154000000),
      ),
    ]);
  }

  /// Student Facing: Fetch approved questions
  /// Follows Cache-First / Stale-While-Revalidate network strategy
  Future<List<Question>> fetchApprovedQuestions({Subject? subject, String? chapterId}) async {
    // 1. Try fetching from Supabase if connected
    if (_supabaseService.client != null) {
      try {
        var query = _supabaseService.client!
            .from(SupabaseConstants.questionsTable)
            .select()
            .eq('status', QuestionStatus.approved.value);

        if (subject != null) {
          query = query.eq('subject', subject.value);
        }
        if (chapterId != null) {
          query = query.eq('chapter_id', chapterId);
        }

        final List<dynamic> response = await query.order('created_at', ascending: false);
        final questions = response
            .map((item) => Question.fromJson(Map<String, dynamic>.from(item as Map)))
            .toList();

        // Update local cache
        await _cacheService.cacheQuestions(questions);
        return questions;
      } catch (e) {
        debugPrint('Supabase fetch failed, falling back to local cache: $e');
      }
    }

    // 2. Fall back to local Hive cache
    final cached = _cacheService.getCachedQuestions(subject: subject);
    if (cached.isNotEmpty) {
      if (chapterId != null) {
        return cached.where((q) {
          final matchChapter = q.chapterId == chapterId ||
              q.chapterId == chapterId.replaceFirst('math_', '') ||
              chapterId == 'math_${q.chapterId}' ||
              q.chapterId == chapterId.replaceFirst('sci_', '') ||
              chapterId == 'sci_${q.chapterId}' ||
              q.chapterId == chapterId.replaceFirst('sst_', '') ||
              chapterId == 'sst_${q.chapterId}';
          return matchChapter && q.status == QuestionStatus.approved;
        }).toList();
      }
      return cached.where((q) => q.status == QuestionStatus.approved).toList();
    }

    // 3. Fall back to in-memory initial store
    return _inMemoryQuestions.where((q) {
      final matchStatus = q.status == QuestionStatus.approved;
      final matchSubject = subject == null || q.subject == subject;
      final matchChapter = chapterId == null ||
          q.chapterId == chapterId ||
          q.chapterId == chapterId.replaceFirst('math_', '') ||
          chapterId == 'math_${q.chapterId}' ||
          q.chapterId == chapterId.replaceFirst('sci_', '') ||
          chapterId == 'sci_${q.chapterId}' ||
          q.chapterId == chapterId.replaceFirst('sst_', '') ||
          chapterId == 'sst_${q.chapterId}';
      return matchStatus && matchSubject && matchChapter;
    }).toList();
  }

  /// Admin Moderation: Fetch pending questions awaiting review
  Future<List<Question>> fetchPendingQuestions({Subject? subject}) async {
    if (_supabaseService.client != null) {
      try {
        var query = _supabaseService.client!
            .from(SupabaseConstants.questionsTable)
            .select()
            .eq('status', QuestionStatus.pendingReview.value);

        if (subject != null) {
          query = query.eq('subject', subject.value);
        }

        final List<dynamic> response = await query.order('created_at', ascending: false);
        return response
            .map((item) => Question.fromJson(Map<String, dynamic>.from(item as Map)))
            .toList();
      } catch (e) {
        debugPrint('Supabase fetch pending questions failed: $e');
      }
    }

    // Fall back to in-memory pending questions
    return _inMemoryQuestions.where((q) {
      final matchStatus = q.status == QuestionStatus.pendingReview;
      final matchSubject = subject == null || q.subject == subject;
      return matchStatus && matchSubject;
    }).toList();
  }

  /// Ingestion Pipeline: Submit a new question (status: 'pending_review')
  Future<Question> submitQuestion({
    required Subject subject,
    required String chapterId,
    required String questionText,
    required List<QuestionOption>? options,
    required String stepByStepSolution,
    required DifficultyLevel difficultyLevel,
    required String submittedBy,
  }) async {
    final newQuestion = Question(
      id: 'gen-${DateTime.now().millisecondsSinceEpoch}',
      subject: subject,
      chapterId: chapterId,
      questionText: questionText,
      options: options,
      stepByStepSolution: stepByStepSolution,
      difficultyLevel: difficultyLevel,
      status: QuestionStatus.pendingReview,
      submittedBy: submittedBy,
      reviewedBy: null,
      createdAt: DateTime.now(),
    );

    if (_supabaseService.client != null) {
      try {
        final res = await _supabaseService.client!
            .from(SupabaseConstants.questionsTable)
            .insert(newQuestion.toJson())
            .select()
            .single();
        return Question.fromJson(res);
      } catch (e) {
        debugPrint('Error inserting question to Supabase: $e');
      }
    }

    _inMemoryQuestions.insert(0, newQuestion);
    return newQuestion;
  }

  /// Admin Action: Approve Question
  Future<bool> approveQuestion({required String questionId, required String adminId}) async {
    if (_supabaseService.client != null) {
      try {
        await _supabaseService.client!
            .from(SupabaseConstants.questionsTable)
            .update({
              'status': QuestionStatus.approved.value,
              'reviewed_by': adminId,
            })
            .eq('id', questionId);
      } catch (e) {
        debugPrint('Supabase approve error: $e');
      }
    }

    final index = _inMemoryQuestions.indexWhere((q) => q.id == questionId);
    if (index != -1) {
      final updated = _inMemoryQuestions[index].copyWith(
        status: QuestionStatus.approved,
        reviewedBy: adminId,
      );
      _inMemoryQuestions[index] = updated;
      await _cacheService.cacheQuestions([updated]);
      return true;
    }
    return true;
  }

  /// Admin Action: Reject Question with feedback
  Future<bool> rejectQuestion({
    required String questionId,
    required String adminId,
    String? feedback,
  }) async {
    if (_supabaseService.client != null) {
      try {
        await _supabaseService.client!
            .from(SupabaseConstants.questionsTable)
            .update({
              'status': QuestionStatus.rejected.value,
              'reviewed_by': adminId,
              'rejection_feedback': feedback,
            })
            .eq('id', questionId);
      } catch (e) {
        debugPrint('Supabase reject error: $e');
      }
    }

    final index = _inMemoryQuestions.indexWhere((q) => q.id == questionId);
    if (index != -1) {
      _inMemoryQuestions[index] = _inMemoryQuestions[index].copyWith(
        status: QuestionStatus.rejected,
        reviewedBy: adminId,
        rejectionFeedback: feedback,
      );
      return true;
    }
    return true;
  }

  /// Admin Action: Edit & Approve Question
  Future<bool> editAndApproveQuestion({
    required String questionId,
    required String adminId,
    required String updatedQuestionText,
    required List<QuestionOption>? updatedOptions,
    required String updatedSolution,
    required DifficultyLevel updatedDifficulty,
  }) async {
    final updateData = {
      'question_text': updatedQuestionText,
      'options': updatedOptions?.map((o) => o.toJson()).toList(),
      'step_by_step_solution': updatedSolution,
      'difficulty_level': updatedDifficulty.value,
      'status': QuestionStatus.approved.value,
      'reviewed_by': adminId,
    };

    if (_supabaseService.client != null) {
      try {
        await _supabaseService.client!
            .from(SupabaseConstants.questionsTable)
            .update(updateData)
            .eq('id', questionId);
      } catch (e) {
        debugPrint('Supabase editAndApprove error: $e');
      }
    }

    final index = _inMemoryQuestions.indexWhere((q) => q.id == questionId);
    if (index != -1) {
      final updated = _inMemoryQuestions[index].copyWith(
        questionText: updatedQuestionText,
        options: updatedOptions,
        stepByStepSolution: updatedSolution,
        difficultyLevel: updatedDifficulty,
        status: QuestionStatus.approved,
        reviewedBy: adminId,
      );
      _inMemoryQuestions[index] = updated;
      await _cacheService.cacheQuestions([updated]);
      return true;
    }
    return true;
  }

  /// Master Chapters: Fetch syllabus chapters with dynamic question counts and student progress
  Future<List<Chapter>> fetchChapters({required Subject subject}) async {
    List<Chapter> chapters = [];

    // 1. Try Supabase remote
    if (_supabaseService.client != null) {
      try {
        final List<dynamic> response = await _supabaseService.client!
            .from('chapters')
            .select()
            .eq('subject', subject.value)
            .order('chapter_number', ascending: true);

        if (response.isNotEmpty) {
          chapters = response
              .map((item) => Chapter.fromJson(Map<String, dynamic>.from(item as Map)))
              .toList();
        }
      } catch (e) {
        debugPrint('Supabase fetchChapters error, falling back to static curriculum: $e');
      }
    }

    // 2. Fall back to static curriculum definitions
    if (chapters.isEmpty) {
      if (subject == Subject.math) {
        chapters = CbseCurriculum.mathChapters.map((m) {
          return Chapter(
            id: m['id'] as String,
            chapterNumber: (m['chapter_number'] as num?)?.toInt() ?? 1,
            subject: Subject.math,
            titleEn: (m['title_en'] ?? m['title']) as String,
            titleKn: (m['title_kn'] ?? '') as String,
            summary: (m['summary'] ?? '') as String,
            formulas: List<String>.from((m['formulas'] as List?) ?? []),
          );
        }).toList();
      } else if (subject == Subject.science) {
        chapters = CbseCurriculum.scienceChapters.map((m) {
          return Chapter(
            id: m['id'] as String,
            chapterNumber: (m['chapter_number'] as num?)?.toInt() ?? 1,
            subject: Subject.science,
            titleEn: (m['title_en'] ?? m['title']) as String,
            titleKn: (m['title_kn'] ?? '') as String,
            summary: (m['summary'] ?? '') as String,
            formulas: List<String>.from((m['formulas'] as List?) ?? []),
          );
        }).toList();
      } else if (subject == Subject.socialScience) {
        chapters = CbseCurriculum.sstChapters.map((m) {
          return Chapter(
            id: m['id'] as String,
            chapterNumber: (m['chapter_number'] as num?)?.toInt() ?? 1,
            subject: Subject.socialScience,
            titleEn: (m['title_en'] ?? m['title']) as String,
            titleKn: (m['title_kn'] ?? '') as String,
            summary: (m['summary'] ?? '') as String,
            formulas: List<String>.from((m['formulas'] as List?) ?? []),
          );
        }).toList();
      }
    }

    // 3. Attach dynamic total_questions and solved_questions counts
    final approvedQuestions = await fetchApprovedQuestions(subject: subject);

    final List<Chapter> enriched = chapters.map((ch) {
      final total = approvedQuestions.where((q) {
        return q.chapterId == ch.id ||
            q.chapterId == ch.id.replaceFirst('math_', '') ||
            ch.id == 'math_${q.chapterId}' ||
            q.chapterId == ch.id.replaceFirst('sci_', '') ||
            ch.id == 'sci_${q.chapterId}' ||
            q.chapterId == ch.id.replaceFirst('sst_', '') ||
            ch.id == 'sst_${q.chapterId}';
      }).length;

      final solvedIds = _cacheService.getSolvedQuestionIdsForChapter(ch.id);
      final solved = solvedIds.length;

      return ch.copyWith(
        totalQuestions: total,
        solvedQuestions: solved > total ? total : solved,
      );
    }).toList();

    return enriched;
  }

  /// Admin Bulk Ingestion Action: Publish parsed questions directly to student feed (status: 'approved')
  Future<List<Question>> bulkPublishQuestions({
    required String chapterId,
    required List<Question> questions,
    required String adminId,
  }) async {
    final List<Question> approvedList = questions.map((q) {
      return q.copyWith(
        chapterId: chapterId,
        status: QuestionStatus.approved,
        submittedBy: adminId,
        reviewedBy: adminId,
      );
    }).toList();

    if (_supabaseService.client != null) {
      try {
        final payload = approvedList.map((q) => q.toJson()).toList();
        await _supabaseService.client!
            .from(SupabaseConstants.questionsTable)
            .insert(payload);
      } catch (e) {
        debugPrint('Supabase bulkPublish error: $e');
      }
    }

    // Update in-memory & local Hive cache
    for (final q in approvedList) {
      _inMemoryQuestions.removeWhere((item) => item.id == q.id);
      _inMemoryQuestions.insert(0, q);
    }
    await _cacheService.cacheQuestions(approvedList);

    return approvedList;
  }
}
