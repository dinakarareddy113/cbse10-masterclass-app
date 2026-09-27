import '../models/question.dart';

/// Pre-seeded 100% NCERT-verified questions for CBSE Class 10 Science Chapter 1 (Chemical Reactions and Equations)
/// In-Text Questions (Pages 6, 10, 13) and End-of-Chapter Exercises (Pages 14-16)
class NcertScienceCh1Data {
  static List<Question> get questions => [
    Question(
      id: 'sci_ch1_p06_q01',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Why should a magnesium ribbon be cleaned before burning in air?''',
      options: const [
        QuestionOption(id: 'A', text: 'To remove the protective layer of basic magnesium oxide and carbonate from its surface', isCorrect: true),
        QuestionOption(id: 'B', text: 'To lower the minimum ignition temperature required for starting the combustion reaction', isCorrect: false),
        QuestionOption(id: 'C', text: 'To eliminate surface moisture and grease accumulated during storage in laboratory conditions', isCorrect: false),
        QuestionOption(id: 'D', text: 'To roughen the metal surface and increase the exposed surface area for rapid oxidation', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) To remove the protective layer of basic magnesium oxide and carbonate from its surface

Scientific Principle / Key Concept:
Magnesium reacts slowly with moist atmospheric oxygen forming a stable, protective coating of basic magnesium oxide/carbonate which hinders ignition until removed by sandpaper.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Cleaning does not change the intrinsic ignition temperature of pure magnesium metal.
• Option (C): Incorrect. While moisture may be present, the chemical impediment to burning is the oxide/carbonate barrier.
• Option (D): Incorrect. The goal is removing the chemical passivation layer, not physical surface roughening.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 0),
    ),
    Question(
      id: 'sci_ch1_p06_q02_i',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation for the reaction:
$$\text{Hydrogen} + \text{Chlorine} \rightarrow \text{Hydrogen chloride}$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{HCl}(g)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{H}(g) + \\text{Cl}(g) \\rightarrow \\text{HCl}(g)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow \\text{H}_2\\text{Cl}_2(g)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$2\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{H}_2\\text{Cl}(g)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{H}_2(g) + \text{Cl}_2(g) \rightarrow 2\text{HCl}(g)$

Scientific Principle / Key Concept:
Hydrogen and chlorine exist as diatomic molecules ($\text{H}_2$, $\text{Cl}_2$), yielding two molecules of hydrogen chloride gas ($\text{HCl}$).

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Under standard conditions, hydrogen and chlorine are diatomic gases, not monoatomic atoms.
• Option (C): Incorrect. $\text{H}_2\text{Cl}_2$ is a non-existent chemical formula; hydrogen chloride is $\text{HCl}$.
• Option (D): Incorrect. The formula $\text{H}_2\text{Cl}$ is incorrect and atoms are not balanced.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 1000),
    ),
    Question(
      id: 'sci_ch1_p06_q02_ii',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation for the reaction:
$$\text{Barium chloride} + \text{Aluminium sulphate} \rightarrow \text{Barium sulphate} + \text{Aluminium chloride}$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$3\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 3\\text{BaSO}_4(s) + 2\\text{AlCl}_3(aq)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow \\text{BaSO}_4(s) + \\text{AlCl}_3(aq)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$3\\text{BaCl}_2(aq) + 2\\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 3\\text{BaSO}_4(s) + 4\\text{AlCl}_3(aq)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$2\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 2\\text{BaSO}_4(s) + 2\\text{AlCl}_3(aq)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $3\text{BaCl}_2(aq) + \text{Al}_2(\text{SO}_4)_3(aq) \rightarrow 3\text{BaSO}_4(s) + 2\text{AlCl}_3(aq)$

Scientific Principle / Key Concept:
Three $\text{Ba}^{2+}$ ions combine with three $\text{SO}_4^{2-}$ ions forming $3\text{BaSO}_4$, and two $\text{Al}^{3+}$ ions combine with six $\text{Cl}^-$ ions forming $2\text{AlCl}_3$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. This equation is unbalanced for $\text{Ba}$, $\text{Al}$, $\text{Cl}$, and $\text{SO}_4$.
• Option (C): Incorrect. Sulphate and chlorine atoms are unbalanced on reactant and product sides.
• Option (D): Incorrect. Barium and sulphate atoms are not balanced.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 2000),
    ),
    Question(
      id: 'sci_ch1_p06_q02_iii',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation for the reaction:
$$\text{Sodium} + \text{Water} \rightarrow \text{Sodium hydroxide} + \text{Hydrogen}$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$2\\text{Na}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{NaOH}(aq) + \\text{H}_2(g)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{Na}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{NaOH}(aq) + \\text{H}(g)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{Na}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{Na}_2\\text{O}(aq) + \\text{H}_2(g)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{Na}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{Na}(\\text{OH})_2(aq) + \\text{H}_2(g)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $2\text{Na}(s) + 2\text{H}_2\text{O}(l) \rightarrow 2\text{NaOH}(aq) + \text{H}_2(g)$

Scientific Principle / Key Concept:
Two sodium atoms react with two water molecules yielding two sodium hydroxide formula units and one diatomic hydrogen molecule.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Hydrogen is liberated as diatomic gas $\text{H}_2(g)$, not atomic $\text{H}$.
• Option (C): Incorrect. In excess water, sodium forms soluble hydroxide $\text{NaOH}$, not oxide.
• Option (D): Incorrect. Sodium is monovalent ($+1$); $\text{Na(OH)}_2$ is an invalid chemical formula.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 3000),
    ),
    Question(
      id: 'sci_ch1_p06_q03_i',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Which equation with state symbols correctly represents: Solutions of barium chloride and sodium sulphate in water react to give insoluble barium sulphate and sodium chloride solution?''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{BaCl}_2(aq) + \\text{Na}_2\\text{SO}_4(aq) \\rightarrow \\text{BaSO}_4(s) + 2\\text{NaCl}(aq)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{BaCl}_2(s) + \\text{Na}_2\\text{SO}_4(s) \\rightarrow \\text{BaSO}_4(aq) + 2\\text{NaCl}(aq)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$\\text{BaCl}_2(aq) + \\text{Na}_2\\text{SO}_4(aq) \\rightarrow \\text{BaSO}_4(aq) + 2\\text{NaCl}(s)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$2\\text{BaCl}_2(aq) + \\text{Na}_2\\text{SO}_4(aq) \\rightarrow 2\\text{BaSO}_4(s) + \\text{NaCl}(aq)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{BaCl}_2(aq) + \text{Na}_2\text{SO}_4(aq) \rightarrow \text{BaSO}_4(s) + 2\text{NaCl}(aq)$

Scientific Principle / Key Concept:
Barium chloride and sodium sulphate are aqueous reactants ($aq$), producing insoluble solid white precipitate barium sulphate ($s$) and aqueous sodium chloride ($aq$).

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. The reactants are aqueous solutions, and barium sulphate is an insoluble precipitate ($s$), not aqueous ($aq$).
• Option (C): Incorrect. Sodium chloride remains dissolved ($aq$); barium sulphate forms the solid precipitate ($s$).
• Option (D): Incorrect. The stoichiometry is unbalanced for both barium and chlorine.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 4000),
    ),
    Question(
      id: 'sci_ch1_p06_q03_ii',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Which equation with state symbols correctly represents: Sodium hydroxide solution in water reacts with hydrochloric acid solution in water to produce sodium chloride solution and water?''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{NaOH}(aq) + \\text{HCl}(aq) \\rightarrow \\text{NaCl}(aq) + \\text{H}_2\\text{O}(l)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{NaOH}(s) + \\text{HCl}(g) \\rightarrow \\text{NaCl}(s) + \\text{H}_2\\text{O}(g)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$\\text{NaOH}(aq) + \\text{HCl}(aq) \\rightarrow \\text{NaCl}(s) + \\text{H}_2\\text{O}(aq)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$2\\text{NaOH}(aq) + \\text{HCl}(aq) \\rightarrow \\text{NaCl}_2(aq) + \\text{H}_2\\text{O}(l)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{NaOH}(aq) + \text{HCl}(aq) \rightarrow \text{NaCl}(aq) + \text{H}_2\text{O}(l)$

Scientific Principle / Key Concept:
Aqueous $\text{NaOH}$ neutralises aqueous $\text{HCl}$ to produce soluble aqueous $\text{NaCl}$ and liquid water $\text{H}_2\text{O}(l)$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. The prompt specifies solutions in water ($aq$), not dry solids or gases.
• Option (C): Incorrect. $\text{NaCl}$ remains dissolved in water as aqueous solution; water is liquid ($l$).
• Option (D): Incorrect. $\text{NaCl}_2$ is a non-existent formula; sodium chloride is $\text{NaCl}$.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 5000),
    ),
    Question(
      id: 'sci_ch1_p10_q01_i',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''A solution of a substance 'X' is used for white washing. Identify substance 'X' and state its chemical formula.''',
      options: const [
        QuestionOption(id: 'A', text: 'Calcium oxide (quicklime), \$\\text{CaO}\$', isCorrect: true),
        QuestionOption(id: 'B', text: 'Calcium hydroxide (slaked lime), \$\\text{Ca(OH)}_2\$', isCorrect: false),
        QuestionOption(id: 'C', text: 'Calcium carbonate (limestone), \$\\text{CaCO}_3\$', isCorrect: false),
        QuestionOption(id: 'D', text: 'Calcium sulphate hemihydrate (Plaster of Paris), \$\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) Calcium oxide (quicklime), $\text{CaO}$

Scientific Principle / Key Concept:
Quicklime ($\text{CaO}$) is mixed with water to form slaked lime, which is applied for white washing walls.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. $\text{Ca(OH)}_2$ is the product formed after substance 'X' reacts with water.
• Option (C): Incorrect. $\text{CaCO}_3$ is the shiny film formed on the wall days after white washing.
• Option (D): Incorrect. Plaster of Paris is used for casts and moulds, not standard white washing.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 6000),
    ),
    Question(
      id: 'sci_ch1_p10_q01_ii',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation for the reaction of substance 'X' (calcium oxide) with water.''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{CaO}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{Ca(OH)}_2(aq) + \\text{Heat}\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{CaO}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{Ca(OH)}_2(aq) + \\text{H}_2(g)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{CaO}(s) + \\text{H}_2\\text{O}(l) \\rightarrow 2\\text{CaOH}(aq) + \\text{O}_2(g)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{CaO}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{CaCO}_3(s) + \\text{Heat}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{CaO}(s) + \text{H}_2\text{O}(l) \rightarrow \text{Ca(OH)}_2(aq) + \text{Heat}$

Scientific Principle / Key Concept:
Calcium oxide reacts vigorously with water in a highly exothermic combination reaction to produce slaked lime $\text{Ca(OH)}_2$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Hydrogen gas is not evolved during the hydration of calcium oxide.
• Option (C): Incorrect. $\text{CaOH}$ is an incorrect formula and oxygen gas is not produced.
• Option (D): Incorrect. Calcium carbonate requires reaction with carbon dioxide, not water alone.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 7000),
    ),
    Question(
      id: 'sci_ch1_p10_q02',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Why is the volume of gas collected in one test tube during the electrolysis of water (Activity 1.7) double that in the other, and which gas is it?''',
      options: const [
        QuestionOption(id: 'A', text: 'Hydrogen gas, because a water molecule contains two hydrogen atoms for every one oxygen atom', isCorrect: true),
        QuestionOption(id: 'B', text: 'Oxygen gas, because oxygen has higher density and displaces twice the volume of aqueous electrolyte', isCorrect: false),
        QuestionOption(id: 'C', text: 'Hydrogen gas, because hydrogen molecules have lower molar mass than diatomic oxygen molecules', isCorrect: false),
        QuestionOption(id: 'D', text: 'Oxygen gas, because oxygen ions carry twice the electric charge during electrolytic discharge', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) Hydrogen gas, because a water molecule contains two hydrogen atoms for every one oxygen atom

Scientific Principle / Key Concept:
Electrolysis decomposes water according to $2\text{H}_2\text{O}(l) \rightarrow 2\text{H}_2(g) + \text{O}_2(g)$, yielding hydrogen and oxygen in a $2:1$ ratio by volume.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Oxygen gas volume is half that of hydrogen, not double.
• Option (C): Incorrect. Gas volume in Avogadro's law depends on molar quantity, not molecular mass.
• Option (D): Incorrect. Oxygen collects at the anode in a $1:2$ ratio compared to hydrogen at the cathode.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 8000),
    ),
    Question(
      id: 'sci_ch1_p13_q01',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Why does the colour of copper sulphate solution change when an iron nail is dipped in it?''',
      options: const [
        QuestionOption(id: 'A', text: 'Iron displaces copper from \$\\text{CuSO}_4\$ forming light green \$\\text{FeSO}_4\$ and depositing brown copper', isCorrect: true),
        QuestionOption(id: 'B', text: 'Copper metal dissolves from the nail, oxidising the sulphate solution to basic copper carbonate', isCorrect: false),
        QuestionOption(id: 'C', text: 'Iron acts as an inert catalyst causing photochemical degradation of aqueous copper ions', isCorrect: false),
        QuestionOption(id: 'D', text: 'Sulphate ions precipitate out of solution onto the iron surface leaving pure water behind', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) Iron displaces copper from $\text{CuSO}_4$ forming light green $\text{FeSO}_4$ and depositing brown copper

Scientific Principle / Key Concept:
Iron is more reactive than copper; in $\text{Fe} + \text{CuSO}_4 \rightarrow \text{FeSO}_4 + \text{Cu}$, blue $\text{Cu}^{2+}$ ions are replaced by green $\text{Fe}^{2+}$ ions.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. The nail is iron, not copper; iron enters the solution, copper is deposited.
• Option (C): Incorrect. Iron actively undergoes chemical displacement, not inert catalysis.
• Option (D): Incorrect. Sulphate ions remain in solution as soluble ferrous sulphate.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 9000),
    ),
    Question(
      id: 'sci_ch1_p13_q02',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Which of the following is an example of a double displacement reaction other than the reaction between barium chloride and sodium sulphate?''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{Pb(NO}_3)_2(aq) + 2\\text{KI}(aq) \\rightarrow \\text{PbI}_2(s) + 2\\text{KNO}_3(aq)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{Zn}(s) + \\text{CuSO}_4(aq) \\rightarrow \\text{ZnSO}_4(aq) + \\text{Cu}(s)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{Mg}(s) + \\text{O}_2(g) \\rightarrow 2\\text{MgO}(s)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$2\\text{FeSO}_4(s) \\xrightarrow{\\Delta} \\text{Fe}_2\\text{O}_3(s) + \\text{SO}_2(g) + \\text{SO}_3(g)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{Pb(NO}_3)_2(aq) + 2\text{KI}(aq) \rightarrow \text{PbI}_2(s) + 2\text{KNO}_3(aq)$

Scientific Principle / Key Concept:
Lead nitrate and potassium iodide exchange ions to produce yellow precipitate lead iodide and potassium nitrate solution.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. This is a single displacement reaction, not double displacement.
• Option (C): Incorrect. This is a combination reaction.
• Option (D): Incorrect. This is a thermal decomposition reaction.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 10000),
    ),
    Question(
      id: 'sci_ch1_p13_q03_i',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''In the reaction $4\text{Na}(s) + \text{O}_2(g) \rightarrow 2\text{Na}_2\text{O}(s)$, identify the substance oxidised and the substance reduced:''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{Na}\$ is oxidised and \$\\text{O}_2\$ is reduced', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{O}_2\$ is oxidised and \$\\text{Na}\$ is reduced', isCorrect: false),
        QuestionOption(id: 'C', text: '\$\\text{Na}_2\\text{O}\$ is oxidised and \$\\text{Na}\$ is reduced', isCorrect: false),
        QuestionOption(id: 'D', text: 'Both \$\\text{Na}\$ and \$\\text{O}_2\$ are oxidised simultaneously', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{Na}$ is oxidised and $\text{O}_2$ is reduced

Scientific Principle / Key Concept:
Sodium gains oxygen (oxidised from $0$ to $+1$), while oxygen gains electrons (reduced from $0$ to $-2$).

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Oxygen is the oxidising agent and gets reduced.
• Option (C): Incorrect. $\text{Na}_2\text{O}$ is the reaction product, not the reactant undergoing redox.
• Option (D): Incorrect. Oxidation cannot occur without a complementary reduction reaction.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 11000),
    ),
    Question(
      id: 'sci_ch1_p13_q03_ii',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''In the reaction $\text{CuO}(s) + \text{H}_2(g) \rightarrow \text{Cu}(s) + \text{H}_2\text{O}(l)$, identify the substance oxidised and the substance reduced:''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{H}_2\$ is oxidised and \$\\text{CuO}\$ is reduced', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{CuO}\$ is oxidised and \$\\text{H}_2\$ is reduced', isCorrect: false),
        QuestionOption(id: 'C', text: '\$\\text{Cu}\$ is oxidised and \$\\text{H}_2\\text{O}\$ is reduced', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{H}_2\\text{O}\$ is oxidised and \$\\text{CuO}\$ is reduced', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{H}_2$ is oxidised and $\text{CuO}$ is reduced

Scientific Principle / Key Concept:
Hydrogen gains oxygen to form $\text{H}_2\text{O}$ (oxidised); copper oxide loses oxygen to form $\text{Cu}$ (reduced).

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. $\text{CuO}$ loses oxygen, which is reduction, not oxidation.
• Option (C): Incorrect. $\text{Cu}$ and $\text{H}_2\text{O}$ are products, whereas redox reactants are identified on LHS.
• Option (D): Incorrect. $\text{H}_2\text{O}$ is the oxidation product of elemental hydrogen.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 12000),
    ),
    Question(
      id: 'sci_ch1_ex01',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Which of the statements about the reaction below are incorrect?
$$2\text{PbO}(s) + \text{C}(s) \rightarrow 2\text{Pb}(s) + \text{CO}_2(g)$$
(a) Lead is getting reduced.
(b) Carbon dioxide is getting oxidised.
(c) Carbon is getting oxidised.
(d) Lead oxide is getting reduced.''',
      options: const [
        QuestionOption(id: 'A', text: '(a) and (b)', isCorrect: true),
        QuestionOption(id: 'B', text: '(a) and (c)', isCorrect: false),
        QuestionOption(id: 'C', text: '(a), (b) and (c)', isCorrect: false),
        QuestionOption(id: 'D', text: 'all of the above', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) (a) and (b)

Scientific Principle / Key Concept:
Lead oxide ($\text{PbO}$) is reduced to lead, not lead itself. Carbon ($\text{C}$) is oxidised to carbon dioxide, not carbon dioxide. Thus, statements (a) and (b) are incorrect.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Statement (c) is correct because carbon is indeed getting oxidised.
• Option (C): Incorrect. Statement (c) is a correct chemical statement, so it cannot be in the incorrect list.
• Option (D): Incorrect. Statements (c) and (d) are both factually correct descriptions of the reaction.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 13000),
    ),
    Question(
      id: 'sci_ch1_ex02',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''$$\text{Fe}_2\text{O}_3 + 2\text{Al} \rightarrow \text{Al}_2\text{O}_3 + 2\text{Fe}$$
The above reaction is an example of a:''',
      options: const [
        QuestionOption(id: 'A', text: 'displacement reaction', isCorrect: true),
        QuestionOption(id: 'B', text: 'double displacement reaction', isCorrect: false),
        QuestionOption(id: 'C', text: 'combination reaction', isCorrect: false),
        QuestionOption(id: 'D', text: 'decomposition reaction', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) displacement reaction

Scientific Principle / Key Concept:
Aluminium is more reactive than iron and displaces iron from ferric oxide to form aluminium oxide and metallic iron.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. There is no mutual exchange of ions between two compounds; elemental aluminium displaces iron.
• Option (C): Incorrect. Two products are formed; combination reactions yield only a single product.
• Option (D): Incorrect. A single reactant does not break down; two reactants interact.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 14000),
    ),
    Question(
      id: 'sci_ch1_ex03',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''What happens when dilute hydrochloric acid is added to iron filings? Tick the correct answer.''',
      options: const [
        QuestionOption(id: 'A', text: 'Hydrogen gas and iron(II) chloride are produced', isCorrect: true),
        QuestionOption(id: 'B', text: 'Chlorine gas and iron(II) hydroxide are produced', isCorrect: false),
        QuestionOption(id: 'C', text: 'No chemical reaction takes place between them', isCorrect: false),
        QuestionOption(id: 'D', text: 'Iron salt and liquid water are exclusively produced', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) Hydrogen gas and iron(II) chloride are produced

Scientific Principle / Key Concept:
Iron reacts with dilute acid according to $\text{Fe}(s) + 2\text{HCl}(aq) \rightarrow \text{FeCl}_2(aq) + \text{H}_2(g)$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Chlorine gas is not released; iron chloride remains in solution.
• Option (C): Incorrect. Iron is placed above hydrogen in the activity series and readily displaces hydrogen from acids.
• Option (D): Incorrect. Neutralisation produces salt and water; reaction of metal with acid produces salt and hydrogen gas.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 15000),
    ),
    Question(
      id: 'sci_ch1_ex04',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''What is a balanced chemical equation, and why should chemical equations be balanced?''',
      options: const [
        QuestionOption(id: 'A', text: 'An equation having equal numbers of each elemental atom on both sides, satisfying the Law of Conservation of Mass', isCorrect: true),
        QuestionOption(id: 'B', text: 'An equation where reactants and products exist in the same physical state, maintaining thermodynamic equilibrium', isCorrect: false),
        QuestionOption(id: 'C', text: 'An equation having equal numbers of moles of molecules on both sides, ensuring volume conservation during reaction', isCorrect: false),
        QuestionOption(id: 'D', text: 'An equation where coefficients match reactant valencies, satisfying the Law of Constant Chemical Proportions', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) An equation having equal numbers of each elemental atom on both sides, satisfying the Law of Conservation of Mass

Scientific Principle / Key Concept:
Mass can neither be created nor destroyed in a chemical reaction, meaning total reactant mass must equal total product mass.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. States of matter can differ among reactants and products in balanced equations.
• Option (C): Incorrect. Total number of molecules often changes during reactions; atom counts must balance, not molecule counts.
• Option (D): Incorrect. Balancing stems from mass conservation, not valency matching.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 16000),
    ),
    Question(
      id: 'sci_ch1_ex05_a',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Translate the statement into a balanced chemical equation:
'Hydrogen gas combines with nitrogen to form ammonia.' ''',
      options: const [
        QuestionOption(id: 'A', text: '\$3\\text{H}_2(g) + \\text{N}_2(g) \\rightarrow 2\\text{NH}_3(g)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{H}_2(g) + \\text{N}_2(g) \\rightarrow 2\\text{NH}(g)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{H}_2(g) + \\text{N}_2(g) \\rightarrow \\text{N}_2\\text{H}_4(g)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$3\\text{H}_2(g) + 2\\text{N}_2(g) \\rightarrow 2\\text{NH}_3(g) + \\text{N}_2(g)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $3\text{H}_2(g) + \text{N}_2(g) \rightarrow 2\text{NH}_3(g)$

Scientific Principle / Key Concept:
Three molecules of diatomic hydrogen react with one molecule of diatomic nitrogen to form two molecules of ammonia gas.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. The molecular formula of ammonia is $\text{NH}_3$, not $\text{NH}$.
• Option (C): Incorrect. $\text{N}_2\text{H}_4$ is hydrazine, not ammonia.
• Option (D): Incorrect. This equation includes unreacted nitrogen on the product side and is not in lowest whole-number terms.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 17000),
    ),
    Question(
      id: 'sci_ch1_ex05_b',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Translate the statement into a balanced chemical equation:
'Hydrogen sulphide gas burns in air to give water and sulphur dioxide.' ''',
      options: const [
        QuestionOption(id: 'A', text: '\$2\\text{H}_2\\text{S}(g) + 3\\text{O}_2(g) \\rightarrow 2\\text{H}_2\\text{O}(l) + 2\\text{SO}_2(g)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{H}_2\\text{S}(g) + \\text{O}_2(g) \\rightarrow \\text{H}_2\\text{O}(l) + \\text{SO}_2(g)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{H}_2\\text{S}(g) + 2\\text{O}_2(g) \\rightarrow 2\\text{H}_2\\text{O}(l) + 2\\text{S}(s)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{H}_2\\text{S}(g) + 2\\text{O}_2(g) \\rightarrow \\text{H}_2\\text{SO}_4(aq)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $2\text{H}_2\text{S}(g) + 3\text{O}_2(g) \rightarrow 2\text{H}_2\text{O}(l) + 2\text{SO}_2(g)$

Scientific Principle / Key Concept:
Balancing gives $4\text{ H}$, $2\text{ S}$, and $6\text{ O}$ on both sides of the equation.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Oxygen atoms are not balanced ($2$ on LHS vs $3$ on RHS).
• Option (C): Incorrect. The problem states sulphur dioxide is formed, not solid sulphur.
• Option (D): Incorrect. Combustion in air yields $\text{SO}_2$ and $\text{H}_2\text{O}$, not sulphuric acid.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 18000),
    ),
    Question(
      id: 'sci_ch1_ex05_c',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Translate the statement into a balanced chemical equation:
'Barium chloride reacts with aluminium sulphate to give aluminium chloride and a precipitate of barium sulphate.' ''',
      options: const [
        QuestionOption(id: 'A', text: '\$3\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 2\\text{AlCl}_3(aq) + 3\\text{BaSO}_4(s)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow \\text{AlCl}_3(aq) + \\text{BaSO}_4(s)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 2\\text{AlCl}_3(aq) + 2\\text{BaSO}_4(s)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$3\\text{BaCl}_2(aq) + 2\\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 4\\text{AlCl}_3(aq) + 3\\text{BaSO}_4(s)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $3\text{BaCl}_2(aq) + \text{Al}_2(\text{SO}_4)_3(aq) \rightarrow 2\text{AlCl}_3(aq) + 3\text{BaSO}_4(s)$

Scientific Principle / Key Concept:
Three $\text{Ba}^{2+}$ ions precipitate with three $\text{SO}_4^{2-}$ ions, leaving two $\text{Al}^{3+}$ and six $\text{Cl}^-$ as $2\text{AlCl}_3$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. This formula statement is unbalanced for all elements.
• Option (C): Incorrect. Sulphate and chlorine atoms are unbalanced.
• Option (D): Incorrect. Aluminium and sulphate counts do not balance.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 19000),
    ),
    Question(
      id: 'sci_ch1_ex05_d',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Translate the statement into a balanced chemical equation:
'Potassium metal reacts with water to give potassium hydroxide and hydrogen gas.' ''',
      options: const [
        QuestionOption(id: 'A', text: '\$2\\text{K}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{KOH}(aq) + \\text{H}_2(g)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{K}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{KOH}(aq) + \\text{H}(g)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{K}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{K}_2\\text{O}(s) + \\text{H}_2(g)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{K}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{K}(\\text{OH})_2(aq) + \\text{H}_2(g)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $2\text{K}(s) + 2\text{H}_2\text{O}(l) \rightarrow 2\text{KOH}(aq) + \text{H}_2(g)$

Scientific Principle / Key Concept:
Potassium reacts vigorously with water releasing hydrogen gas and forming aqueous potassium hydroxide.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Hydrogen is evolved as molecular $\text{H}_2$, not monoatomic $\text{H}$.
• Option (C): Incorrect. The alkali metal hydroxide is formed in water, not oxide.
• Option (D): Incorrect. Potassium is monovalent ($+1$); $\text{K(OH)}_2$ is an invalid formula.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 20000),
    ),
    Question(
      id: 'sci_ch1_ex06_a',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Balance the following chemical equation:
$$\text{HNO}_3 + \text{Ca(OH)}_2 \rightarrow \text{Ca(NO}_3)_2 + \text{H}_2\text{O}$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$2\\text{HNO}_3 + \\text{Ca(OH)}_2 \\rightarrow \\text{Ca(NO}_3)_2 + 2\\text{H}_2\\text{O}\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{HNO}_3 + \\text{Ca(OH)}_2 \\rightarrow \\text{Ca(NO}_3)_2 + \\text{H}_2\\text{O}\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{HNO}_3 + 2\\text{Ca(OH)}_2 \\rightarrow 2\\text{Ca(NO}_3)_2 + 3\\text{H}_2\\text{O}\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{HNO}_3 + 2\\text{Ca(OH)}_2 \\rightarrow \\text{Ca(NO}_3)_2 + 2\\text{H}_2\\text{O}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $2\text{HNO}_3 + \text{Ca(OH)}_2 \rightarrow \text{Ca(NO}_3)_2 + 2\text{H}_2\text{O}$

Scientific Principle / Key Concept:
Two moles of $\text{HNO}_3$ provide two nitrate ions for $\text{Ca(NO}_3)_2$ and two hydrogen ions to form $2\text{H}_2\text{O}$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Nitrogen and hydrogen atoms are unbalanced.
• Option (C): Incorrect. Calcium and oxygen atoms do not balance.
• Option (D): Incorrect. Nitrate groups are not balanced.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 21000),
    ),
    Question(
      id: 'sci_ch1_ex06_b',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Balance the following chemical equation:
$$\text{NaOH} + \text{H}_2\text{SO}_4 \rightarrow \text{Na}_2\text{SO}_4 + \text{H}_2\text{O}$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$2\\text{NaOH} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{Na}_2\\text{SO}_4 + 2\\text{H}_2\\text{O}\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{NaOH} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{Na}_2\\text{SO}_4 + \\text{H}_2\\text{O}\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{NaOH} + 2\\text{H}_2\\text{SO}_4 \\rightarrow 2\\text{Na}_2\\text{SO}_4 + 3\\text{H}_2\\text{O}\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{NaOH} + 2\\text{H}_2\\text{SO}_4 \\rightarrow \\text{Na}_2\\text{SO}_4 + 2\\text{H}_2\\text{O}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $2\text{NaOH} + \text{H}_2\text{SO}_4 \rightarrow \text{Na}_2\text{SO}_4 + 2\text{H}_2\text{O}$

Scientific Principle / Key Concept:
Two sodium atoms on LHS balance $\text{Na}_2\text{SO}_4$, and four hydrogen atoms balance $2\text{H}_2\text{O}$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Sodium is unbalanced ($1$ on LHS vs $2$ on RHS).
• Option (C): Incorrect. Sulphur and oxygen atoms are unbalanced.
• Option (D): Incorrect. Both sodium and sulphate counts fail to balance.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 22000),
    ),
    Question(
      id: 'sci_ch1_ex06_c',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Balance the following chemical equation:
$$\text{NaCl} + \text{AgNO}_3 \rightarrow \text{AgCl} + \text{NaNO}_3$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{NaCl} + \\text{AgNO}_3 \\rightarrow \\text{AgCl} + \\text{NaNO}_3\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$2\\text{NaCl} + \\text{AgNO}_3 \\rightarrow 2\\text{AgCl} + \\text{NaNO}_3\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$\\text{NaCl} + 2\\text{AgNO}_3 \\rightarrow \\text{AgCl} + 2\\text{NaNO}_3\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$2\\text{NaCl} + 2\\text{AgNO}_3 \\rightarrow 2\\text{AgCl} + \\text{Na}_2\\text{NO}_3\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{NaCl} + \text{AgNO}_3 \rightarrow \text{AgCl} + \text{NaNO}_3$

Scientific Principle / Key Concept:
The equation is already balanced with a $1:1:1:1$ stoichiometric ratio.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Silver and sodium atoms would become unbalanced.
• Option (C): Incorrect. Chlorine and silver counts do not balance.
• Option (D): Incorrect. $\text{Na}_2\text{NO}_3$ is an invalid formula.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 23000),
    ),
    Question(
      id: 'sci_ch1_ex06_d',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Balance the following chemical equation:
$$\text{BaCl}_2 + \text{H}_2\text{SO}_4 \rightarrow \text{BaSO}_4 + \text{HCl}$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{BaCl}_2 + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 2\\text{HCl}\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{BaCl}_2 + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + \\text{HCl}\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{BaCl}_2 + \\text{H}_2\\text{SO}_4 \\rightarrow 2\\text{BaSO}_4 + 2\\text{HCl}\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{BaCl}_2 + 2\\text{H}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 4\\text{HCl}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{BaCl}_2 + \text{H}_2\text{SO}_4 \rightarrow \text{BaSO}_4 + 2\text{HCl}$

Scientific Principle / Key Concept:
Two chlorine and two hydrogen atoms on the left require coefficient $2$ before $\text{HCl}$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Chlorine and hydrogen are unbalanced ($2$ on LHS vs $1$ on RHS).
• Option (C): Incorrect. Sulphate and barium counts do not balance.
• Option (D): Incorrect. Sulphate and chlorine atoms are unbalanced.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 24000),
    ),
    Question(
      id: 'sci_ch1_ex07_a',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation for the reaction:
$$\text{Calcium hydroxide} + \text{Carbon dioxide} \rightarrow \text{Calcium carbonate} + \text{Water}$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{Ca(OH)}_2 + \\text{CO}_2 \\rightarrow \\text{CaCO}_3 + \\text{H}_2\\text{O}\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$2\\text{Ca(OH)}_2 + \\text{CO}_2 \\rightarrow 2\\text{CaCO}_3 + \\text{H}_2\\text{O}\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$\\text{Ca(OH)}_2 + 2\\text{CO}_2 \\rightarrow \\text{CaCO}_3 + 2\\text{H}_2\\text{O}\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{Ca(OH)}_2 + \\text{CO}_2 \\rightarrow \\text{Ca(HCO}_3)_2 + \\text{H}_2\\text{O}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{Ca(OH)}_2 + \text{CO}_2 \rightarrow \text{CaCO}_3 + \text{H}_2\text{O}$

Scientific Principle / Key Concept:
The equation is balanced as written with $1\text{ Ca}$, $1\text{ C}$, $2\text{ H}$, and $4\text{ O}$ on both sides.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Carbon and oxygen atoms are unbalanced.
• Option (C): Incorrect. Carbon and oxygen atoms do not balance.
• Option (D): Incorrect. Calcium bicarbonate is formed only when excess $\text{CO}_2$ is bubbled, and no water is produced.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 25000),
    ),
    Question(
      id: 'sci_ch1_ex07_b',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation for the reaction:
$$\text{Zinc} + \text{Silver nitrate} \rightarrow \text{Zinc nitrate} + \text{Silver}$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{Zn} + 2\\text{AgNO}_3 \\rightarrow \\text{Zn(NO}_3)_2 + 2\\text{Ag}\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{Zn} + \\text{AgNO}_3 \\rightarrow \\text{ZnNO}_3 + \\text{Ag}\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{Zn} + 2\\text{AgNO}_3 \\rightarrow 2\\text{Zn(NO}_3)_2 + \\text{Ag}\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{Zn} + 3\\text{AgNO}_3 \\rightarrow \\text{Zn(NO}_3)_3 + 3\\text{Ag}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{Zn} + 2\text{AgNO}_3 \rightarrow \text{Zn(NO}_3)_2 + 2\text{Ag}$

Scientific Principle / Key Concept:
Zinc is bivalent (forms $\text{Zn}^{2+}$), requiring two monovalent $\text{NO}_3^-$ ions and displacing two silver atoms.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. $\text{ZnNO}_3$ is an incorrect formula; zinc nitrate is $\text{Zn(NO}_3)_2$.
• Option (C): Incorrect. Nitrate and silver atoms are not balanced.
• Option (D): Incorrect. Zinc does not exhibit a $+3$ oxidation state.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 26000),
    ),
    Question(
      id: 'sci_ch1_ex07_c',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation for the reaction:
$$\text{Aluminium} + \text{Copper chloride} \rightarrow \text{Aluminium chloride} + \text{Copper}$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$2\\text{Al} + 3\\text{CuCl}_2 \\rightarrow 2\\text{AlCl}_3 + 3\\text{Cu}\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{Al} + \\text{CuCl}_2 \\rightarrow \\text{AlCl}_2 + \\text{Cu}\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{Al} + \\text{CuCl}_2 \\rightarrow 2\\text{AlCl} + \\text{Cu}\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$3\\text{Al} + 2\\text{CuCl}_2 \\rightarrow 3\\text{AlCl}_2 + 2\\text{Cu}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $2\text{Al} + 3\text{CuCl}_2 \rightarrow 2\text{AlCl}_3 + 3\text{Cu}$

Scientific Principle / Key Concept:
Two $\text{Al}$ atoms ($+3$) balance with six chlorine atoms from three $\text{CuCl}_2$ ($+2$), displacing three $\text{Cu}$ atoms.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. $\text{AlCl}_2$ is an incorrect formula; aluminium forms $\text{AlCl}_3$.
• Option (C): Incorrect. Aluminium chloride is $\text{AlCl}_3$ and the equation is unbalanced.
• Option (D): Incorrect. Both chemical formula and stoichiometry are incorrect.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 27000),
    ),
    Question(
      id: 'sci_ch1_ex07_d',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation for the reaction:
$$\text{Barium chloride} + \text{Potassium sulphate} \rightarrow \text{Barium sulphate} + \text{Potassium chloride}$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{BaCl}_2 + \\text{K}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 2\\text{KCl}\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{BaCl}_2 + \\text{K}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + \\text{KCl}\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{BaCl}_2 + \\text{K}_2\\text{SO}_4 \\rightarrow 2\\text{BaSO}_4 + \\text{KCl}_2\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{BaCl}_2 + 2\\text{K}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 4\\text{KCl}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{BaCl}_2 + \text{K}_2\text{SO}_4 \rightarrow \text{BaSO}_4 + 2\text{KCl}$

Scientific Principle / Key Concept:
One $\text{Ba}^{2+}$ combines with $\text{SO}_4^{2-}$ forming $\text{BaSO}_4$, and two $\text{K}^+$ combine with two $\text{Cl}^-$ forming $2\text{KCl}$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Potassium and chlorine are unbalanced ($2$ on LHS vs $1$ on RHS).
• Option (C): Incorrect. $\text{KCl}_2$ is an invalid formula and barium is unbalanced.
• Option (D): Incorrect. Sulphate and chlorine atoms do not balance.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 28000),
    ),
    Question(
      id: 'sci_ch1_ex08_a',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation and identify the reaction type:
$$\text{Potassium bromide}(aq) + \text{Barium iodide}(aq) \rightarrow \text{Potassium iodide}(aq) + \text{Barium bromide}(s)$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$2\\text{KBr}(aq) + \\text{BaI}_2(aq) \\rightarrow 2\\text{KI}(aq) + \\text{BaBr}_2(s)\$ (Double displacement)', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{KBr}(aq) + \\text{BaI}_2(aq) \\rightarrow \\text{KI}(aq) + \\text{BaBr}_2(s)\$ (Single displacement)', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{KBr}(aq) + \\text{BaI}_2(aq) \\rightarrow 2\\text{KI}(aq) + \\text{BaBr}_2(s)\$ (Decomposition)', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{KBr}(aq) + 2\\text{BaI}_2(aq) \\rightarrow \\text{KI}(aq) + 2\\text{BaBr}_2(s)\$ (Combination)', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $2\text{KBr}(aq) + \text{BaI}_2(aq) \rightarrow 2\text{KI}(aq) + \text{BaBr}_2(s)$ (Double displacement)

Scientific Principle / Key Concept:
Potassium and barium exchange their halide counter-ions, representing a double displacement reaction.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. This equation is unbalanced and misidentifies ion exchange as single displacement.
• Option (C): Incorrect. The reaction involves two compounds reacting, not a single compound breaking down.
• Option (D): Incorrect. The stoichiometry is incorrect and two products are formed, not one.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 29000),
    ),
    Question(
      id: 'sci_ch1_ex08_b',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation and identify the reaction type:
$$\text{Zinc carbonate}(s) \rightarrow \text{Zinc oxide}(s) + \text{Carbon dioxide}(g)$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{ZnCO}_3(s) \\xrightarrow{\\Delta} \\text{ZnO}(s) + \\text{CO}_2(g)\$ (Decomposition)', isCorrect: true),
        QuestionOption(id: 'B', text: '\$2\\text{ZnCO}_3(s) \\rightarrow 2\\text{ZnO}(s) + \\text{CO}_2(g)\$ (Combination)', isCorrect: false),
        QuestionOption(id: 'C', text: '\$\\text{ZnCO}_3(s) \\rightarrow \\text{ZnO}(s) + \\text{CO}_2(g)\$ (Displacement)', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{ZnCO}_3(s) \\rightarrow \\text{Zn}(s) + \\text{CO}_3(g)\$ (Neutralisation)', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{ZnCO}_3(s) \xrightarrow{\Delta} \text{ZnO}(s) + \text{CO}_2(g)$ (Decomposition)

Scientific Principle / Key Concept:
A single reactant (zinc carbonate) breaks down upon heating into two simpler products (zinc oxide and carbon dioxide).

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Equation is unbalanced for oxygen and misclassifies decomposition as combination.
• Option (C): Incorrect. There is no elemental displacing agent; it is a thermal breakdown.
• Option (D): Incorrect. $\text{CO}_3$ is not a stable neutral gas and this is not acid-base neutralisation.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 30000),
    ),
    Question(
      id: 'sci_ch1_ex08_c',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation and identify the reaction type:
$$\text{Hydrogen}(g) + \text{Chlorine}(g) \rightarrow \text{Hydrogen chloride}(g)$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{HCl}(g)\$ (Combination)', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{HCl}(g)\$ (Displacement)', isCorrect: false),
        QuestionOption(id: 'C', text: '\$\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow \\text{H}_2\\text{Cl}_2(g)\$ (Decomposition)', isCorrect: false),
        QuestionOption(id: 'D', text: '\$2\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{H}_2\\text{Cl}(g)\$ (Double displacement)', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{H}_2(g) + \text{Cl}_2(g) \rightarrow 2\text{HCl}(g)$ (Combination)

Scientific Principle / Key Concept:
Two elemental reactants combine to form a single product ($\text{HCl}$), which is a combination reaction.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Neither element is displaced from a compound; two elements synthesize one compound.
• Option (C): Incorrect. $\text{H}_2\text{Cl}_2$ is an invalid formula and this is synthesis, not decomposition.
• Option (D): Incorrect. The equation is stoichiometry incorrect and not double displacement.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 31000),
    ),
    Question(
      id: 'sci_ch1_ex08_d',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Write the balanced chemical equation and identify the reaction type:
$$\text{Magnesium}(s) + \text{Hydrochloric acid}(aq) \rightarrow \text{Magnesium chloride}(aq) + \text{Hydrogen}(g)$$''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{Mg}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{MgCl}_2(aq) + \\text{H}_2(g)\$ (Displacement)', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{Mg}(s) + \\text{HCl}(aq) \\rightarrow \\text{MgCl}_2(aq) + \\text{H}_2(g)\$ (Combination)', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{Mg}(s) + 2\\text{HCl}(aq) \\rightarrow 2\\text{MgCl}(aq) + \\text{H}_2(g)\$ (Decomposition)', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{Mg}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{MgCl}_2(aq) + \\text{H}_2(g)\$ (Double displacement)', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{Mg}(s) + 2\text{HCl}(aq) \rightarrow \text{MgCl}_2(aq) + \text{H}_2(g)$ (Displacement)

Scientific Principle / Key Concept:
Magnesium is more reactive than hydrogen and displaces it from $\text{HCl}$, forming $\text{MgCl}_2$ and $\text{H}_2$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Equation is unbalanced for $\text{Cl}$ and $\text{H}$, and two products are formed.
• Option (C): Incorrect. $\text{MgCl}$ is incorrect (magnesium is bivalent) and it is not decomposition.
• Option (D): Incorrect. Magnesium is an element reacting with a compound, which is single displacement.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 32000),
    ),
    Question(
      id: 'sci_ch1_ex09',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''What is the primary difference between exothermic and endothermic reactions?''',
      options: const [
        QuestionOption(id: 'A', text: 'Exothermic reactions release heat energy into surroundings; endothermic reactions absorb heat energy', isCorrect: true),
        QuestionOption(id: 'B', text: 'Exothermic reactions absorb electrical energy from surroundings; endothermic reactions release photons', isCorrect: false),
        QuestionOption(id: 'C', text: 'Exothermic reactions occur only at high temperatures; endothermic reactions occur only below freezing point', isCorrect: false),
        QuestionOption(id: 'D', text: 'Exothermic reactions require catalyst addition; endothermic reactions proceed spontaneously without input', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) Exothermic reactions release heat energy into surroundings; endothermic reactions absorb heat energy

Scientific Principle / Key Concept:
Exothermic reactions produce heat along with products ($\Delta H < 0$); endothermic reactions require continuous heat input ($\Delta H > 0$).

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. The defining thermodynamic distinction is release versus absorption of heat energy.
• Option (C): Incorrect. Reaction temperature range does not define exothermic or endothermic nature.
• Option (D): Incorrect. Catalysis affects reaction rate, not the net exothermic or endothermic enthalpy change.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 33000),
    ),
    Question(
      id: 'sci_ch1_ex10',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Why is respiration considered an exothermic reaction?''',
      options: const [
        QuestionOption(id: 'A', text: 'Glucose combines with oxygen in cells to form carbon dioxide, water, and releases energy', isCorrect: true),
        QuestionOption(id: 'B', text: 'Digestion breaks complex starch molecules down into simpler sugars by absorbing atmospheric heat', isCorrect: false),
        QuestionOption(id: 'C', text: 'Inhaled oxygen expands within lung alveoli producing thermal heat during mechanical gas exchange', isCorrect: false),
        QuestionOption(id: 'D', text: 'Body temperature is maintained solely by cooling perspiration produced during physical activity', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) Glucose combines with oxygen in cells to form carbon dioxide, water, and releases energy

Scientific Principle / Key Concept:
In $\text{C}_6\text{H}_{12}\text{O}_6 + 6\text{O}_2 \rightarrow 6\text{CO}_2 + 6\text{H}_2\text{O} + \text{Energy}$, the oxidation of glucose yields metabolic energy sustaining cellular life.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Digestion is preliminary breakdown; respiration is the cellular oxidation yielding energy.
• Option (C): Incorrect. Physical lung expansion is mechanical breathing, not biochemical cellular respiration.
• Option (D): Incorrect. Perspiration is an evaporative cooling mechanism, not the heat-producing process.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 34000),
    ),
    Question(
      id: 'sci_ch1_ex11',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Why are decomposition reactions called the opposite of combination reactions?''',
      options: const [
        QuestionOption(id: 'A', text: 'In combination two or more reactants form one product; in decomposition one reactant breaks into multiple products', isCorrect: true),
        QuestionOption(id: 'B', text: 'Combination reactions require constant energy input; decomposition reactions always release large amounts of heat', isCorrect: false),
        QuestionOption(id: 'C', text: 'Combination reactions involve only gaseous elements; decomposition reactions involve only solid ionic compounds', isCorrect: false),
        QuestionOption(id: 'D', text: 'In combination oxidation numbers decrease; in decomposition all reacting elements retain zero oxidation state', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) In combination two or more reactants form one product; in decomposition one reactant breaks into multiple products

Scientific Principle / Key Concept:
Combination follows $A + B \rightarrow AB$, whereas decomposition follows the reverse $AB \rightarrow A + B$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Decomposition typically absorbs energy (endothermic), while combination often releases heat.
• Option (C): Incorrect. Both reaction classes encompass solids, liquids, aqueous solutions, and gases.
• Option (D): Incorrect. Oxidation states change depending on the specific redox nature of the reaction.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 35000),
    ),
    Question(
      id: 'sci_ch1_ex12',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Which set correctly provides one decomposition equation each using heat, light, and electricity?''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{CaCO}_3 \\xrightarrow{\\Delta} \\text{CaO} + \\text{CO}_2\$, \$2\\text{AgCl} \\xrightarrow{\\text{light}} 2\\text{Ag} + \\text{Cl}_2\$, \$2\\text{H}_2\\text{O} \\xrightarrow{\\text{elec.}} 2\\text{H}_2 + \\text{O}_2\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{C} + \\text{O}_2 \\rightarrow \\text{CO}_2\$, \$\\text{H}_2 + \\text{Cl}_2 \\rightarrow 2\\text{HCl}\$, \$\\text{Zn} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{ZnSO}_4 + \\text{H}_2\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{Mg} + \\text{O}_2 \\rightarrow 2\\text{MgO}\$, \$\\text{CH}_4 + 2\\text{O}_2 \\rightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O}\$, \$\\text{Fe} + \\text{CuSO}_4 \\rightarrow \\text{FeSO}_4 + \\text{Cu}\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{CaO} + \\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2\$, \$2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}\$, \$\\text{Pb} + \\text{CuCl}_2 \\rightarrow \\text{PbCl}_2 + \\text{Cu}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{CaCO}_3 \xrightarrow{\Delta} \text{CaO} + \text{CO}_2$, $2\text{AgCl} \xrightarrow{\text{light}} 2\text{Ag} + \text{Cl}_2$, $2\text{H}_2\text{O} \xrightarrow{\text{elec.}} 2\text{H}_2 + \text{O}_2$

Scientific Principle / Key Concept:
Thermal decomposition of limestone (heat), photolytic decomposition of silver chloride (light), and electrolytic decomposition of water (electricity).

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. These are combination and single displacement reactions, not decomposition reactions.
• Option (C): Incorrect. These represent synthesis, combustion, and displacement reactions.
• Option (D): Incorrect. These are combination and displacement reactions.''',
      difficultyLevel: DifficultyLevel.hard,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 36000),
    ),
    Question(
      id: 'sci_ch1_ex13',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''What is the primary difference between displacement and double displacement reactions?''',
      options: const [
        QuestionOption(id: 'A', text: 'Displacement involves a more reactive element replacing another; double displacement involves mutual exchange of ions', isCorrect: true),
        QuestionOption(id: 'B', text: 'Displacement occurs only in molten salts; double displacement occurs exclusively between neutral non-polar gases', isCorrect: false),
        QuestionOption(id: 'C', text: 'Displacement always yields a white precipitate; double displacement always produces an inflammable gas', isCorrect: false),
        QuestionOption(id: 'D', text: 'Displacement involves two compounds exchanging cations; double displacement involves a single element reaction', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) Displacement involves a more reactive element replacing another; double displacement involves mutual exchange of ions

Scientific Principle / Key Concept:
In single displacement, a free element displaces a less reactive element from a compound; in double displacement, two compounds exchange ions.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Both reactions predominantly occur in aqueous solutions.
• Option (C): Incorrect. Double displacement often forms precipitates, whereas displacement often liberates metals or hydrogen gas.
• Option (D): Incorrect. This reverses the fundamental definitions of the two reaction types.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 37000),
    ),
    Question(
      id: 'sci_ch1_ex14',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''In silver refining, recovery of silver from silver nitrate solution involves displacement by copper metal. What is the reaction equation?''',
      options: const [
        QuestionOption(id: 'A', text: '\$\\text{Cu}(s) + 2\\text{AgNO}_3(aq) \\rightarrow \\text{Cu(NO}_3)_2(aq) + 2\\text{Ag}(s)\$', isCorrect: true),
        QuestionOption(id: 'B', text: '\$\\text{Cu}(s) + \\text{AgNO}_3(aq) \\rightarrow \\text{CuNO}_3(aq) + \\text{Ag}(s)\$', isCorrect: false),
        QuestionOption(id: 'C', text: '\$2\\text{Cu}(s) + 2\\text{AgNO}_3(aq) \\rightarrow 2\\text{CuNO}_3(aq) + \\text{Ag}_2(s)\$', isCorrect: false),
        QuestionOption(id: 'D', text: '\$\\text{Cu}(s) + 3\\text{AgNO}_3(aq) \\rightarrow \\text{Cu(NO}_3)_3(aq) + 3\\text{Ag}(s)\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) $\text{Cu}(s) + 2\text{AgNO}_3(aq) \rightarrow \text{Cu(NO}_3)_2(aq) + 2\text{Ag}(s)$

Scientific Principle / Key Concept:
Copper is more reactive than silver and displaces silver ions from silver nitrate, forming blue cupric nitrate solution and metallic silver.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Copper(II) nitrate is $\text{Cu(NO}_3)_2$, not $\text{CuNO}_3$.
• Option (C): Incorrect. Silver metal precipitates as individual atoms ($2\text{Ag}$), not $\text{Ag}_2$ molecules.
• Option (D): Incorrect. Copper exhibits $+1$ and $+2$ oxidation states, not $+3$.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 38000),
    ),
    Question(
      id: 'sci_ch1_ex15',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''What defines a precipitation reaction in aqueous solutions?''',
      options: const [
        QuestionOption(id: 'A', text: 'A reaction between aqueous solutions that produces an insoluble solid substance separating from the liquid', isCorrect: true),
        QuestionOption(id: 'B', text: 'A reaction in which liquid water evaporates completely leaving behind dry crystalline solute residue', isCorrect: false),
        QuestionOption(id: 'C', text: 'A reaction in which strong acid neutralises base forming only soluble salt and liquid water', isCorrect: false),
        QuestionOption(id: 'D', text: 'A reaction where thermal heating decomposes a hydrated metal sulphate into gaseous oxides', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) A reaction between aqueous solutions that produces an insoluble solid substance separating from the liquid

Scientific Principle / Key Concept:
Any chemical reaction that produces an insoluble salt (precipitate) is defined as a precipitation reaction.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Evaporation is a physical separation process, not a chemical precipitation reaction.
• Option (C): Incorrect. Neutralisation forming soluble salt does not produce a precipitate.
• Option (D): Incorrect. This describes thermal decomposition, not aqueous precipitation.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 39000),
    ),
    Question(
      id: 'sci_ch1_ex16_a',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''How is oxidation defined in terms of gain or loss of oxygen, and which is an example?''',
      options: const [
        QuestionOption(id: 'A', text: 'Oxidation is the gain of oxygen; e.g., \$2\\text{Cu} + \\text{O}_2 \\rightarrow 2\\text{CuO}\$', isCorrect: true),
        QuestionOption(id: 'B', text: 'Oxidation is the loss of oxygen; e.g., \$\\text{CuO} + \\text{H}_2 \\rightarrow \\text{Cu} + \\text{H}_2\\text{O}\$', isCorrect: false),
        QuestionOption(id: 'C', text: 'Oxidation is the gain of hydrogen; e.g., \$\\text{N}_2 + 3\\text{H}_2 \\rightarrow 2\\text{NH}_3\$', isCorrect: false),
        QuestionOption(id: 'D', text: 'Oxidation is the displacement of metal ions; e.g., \$\\text{Fe} + \\text{CuSO}_4 \\rightarrow \\text{FeSO}_4 + \\text{Cu}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) Oxidation is the gain of oxygen; e.g., $2\text{Cu} + \text{O}_2 \rightarrow 2\text{CuO}$

Scientific Principle / Key Concept:
Oxidation is chemically defined as the addition/gain of oxygen to a substance; here copper gains oxygen.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Loss of oxygen is reduction, not oxidation.
• Option (C): Incorrect. Gain of hydrogen corresponds to reduction, and the prompt requires oxygen terms.
• Option (D): Incorrect. This is single displacement, not the classical oxygen gain definition.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 40000),
    ),
    Question(
      id: 'sci_ch1_ex16_b',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''How is reduction defined in terms of gain or loss of oxygen, and which is an example?''',
      options: const [
        QuestionOption(id: 'A', text: 'Reduction is the loss of oxygen; e.g., \$\\text{CuO} + \\text{H}_2 \\rightarrow \\text{Cu} + \\text{H}_2\\text{O}\$', isCorrect: true),
        QuestionOption(id: 'B', text: 'Reduction is the gain of oxygen; e.g., \$2\\text{Mg} + \\text{O}_2 \\rightarrow 2\\text{MgO}\$', isCorrect: false),
        QuestionOption(id: 'C', text: 'Reduction is the loss of hydrogen; e.g., \$2\\text{H}_2\\text{S} + \\text{O}_2 \\rightarrow 2\\text{S} + 2\\text{H}_2\\text{O}\$', isCorrect: false),
        QuestionOption(id: 'D', text: 'Reduction is the formation of a precipitate; e.g., \$\\text{BaCl}_2 + \\text{Na}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 2\\text{NaCl}\$', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) Reduction is the loss of oxygen; e.g., $\text{CuO} + \text{H}_2 \rightarrow \text{Cu} + \text{H}_2\text{O}$

Scientific Principle / Key Concept:
Reduction is chemically defined as the loss/removal of oxygen from a substance; here copper oxide loses oxygen to become copper.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Gain of oxygen is oxidation, not reduction.
• Option (C): Incorrect. Loss of hydrogen represents oxidation, not reduction.
• Option (D): Incorrect. Precipitation is double displacement, not reduction.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 41000),
    ),
    Question(
      id: 'sci_ch1_ex17',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''A shiny brown coloured element 'X' on heating in air becomes black in colour. Identify element 'X' and the black compound formed.''',
      options: const [
        QuestionOption(id: 'A', text: 'Element \'X\' is copper (\$\\text{Cu}\$), and the black compound is copper(II) oxide (\$\\text{CuO}\$)', isCorrect: true),
        QuestionOption(id: 'B', text: 'Element \'X\' is iron (\$\\text{Fe}\$), and the black compound is ferrous sulphate (\$\\text{FeSO}_4\$)', isCorrect: false),
        QuestionOption(id: 'C', text: 'Element \'X\' is lead (\$\\text{Pb}\$), and the black compound is lead(II) oxide (\$\\text{PbO}\$)', isCorrect: false),
        QuestionOption(id: 'D', text: 'Element \'X\' is silver (\$\\text{Ag}\$), and the black compound is silver sulphide (\$\\text{Ag}_2\\text{S}\$)', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) Element 'X' is copper ($\text{Cu}$), and the black compound is copper(II) oxide ($\text{CuO}$)

Scientific Principle / Key Concept:
Copper metal is shiny reddish-brown; when heated in air, it oxidises to black cupric oxide according to $2\text{Cu} + \text{O}_2 \rightarrow 2\text{CuO}$.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Iron forms reddish-brown rust on moist oxidation, not black $\text{CuO}$.
• Option (C): Incorrect. Lead metal is silvery-grey, and lead oxide is yellow/reddish, not black.
• Option (D): Incorrect. Silver is lustrous white, and tarnishing requires atmospheric sulphur, not heating in pure air.''',
      difficultyLevel: DifficultyLevel.medium,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 42000),
    ),
    Question(
      id: 'sci_ch1_ex18',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Why do we apply paint on iron articles?''',
      options: const [
        QuestionOption(id: 'A', text: 'To prevent air and moisture from coming in direct contact with the iron surface, preventing corrosion', isCorrect: true),
        QuestionOption(id: 'B', text: 'To chemically convert surface iron atoms into an inert layer of hard iron carbide alloy', isCorrect: false),
        QuestionOption(id: 'C', text: 'To neutralize acidic sulfur dioxide pollutants present in ambient rain water on the metal', isCorrect: false),
        QuestionOption(id: 'D', text: 'To increase surface thermal conductivity so heat dissipates rapidly preventing oxidation', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) To prevent air and moisture from coming in direct contact with the iron surface, preventing corrosion

Scientific Principle / Key Concept:
Rusting requires both oxygen and water vapor; paint creates an impermeable barrier blocking both.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Paint is a protective physical coating, not a metallurgical alloy conversion.
• Option (C): Incorrect. Paint acts as a barrier, not an acid-neutralising chemical buffer.
• Option (D): Incorrect. Thermal conductivity does not prevent electrochemical corrosion.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 43000),
    ),
    Question(
      id: 'sci_ch1_ex19',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Why are oil and fat containing food items flushed with nitrogen gas during packaging?''',
      options: const [
        QuestionOption(id: 'A', text: 'To provide an unreactive inert atmosphere that prevents oxidation of oils and fats, avoiding rancidity', isCorrect: true),
        QuestionOption(id: 'B', text: 'To destroy anaerobic bacteria and mold spores by dehydrating packaged food materials', isCorrect: false),
        QuestionOption(id: 'C', text: 'To preserve crispy food texture by absorbing moisture released from packaged chips', isCorrect: false),
        QuestionOption(id: 'D', text: 'To chemically bind with unsaturated fatty acids and extend their calorific nutritional value', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) To provide an unreactive inert atmosphere that prevents oxidation of oils and fats, avoiding rancidity

Scientific Principle / Key Concept:
Nitrogen is chemically inert under packaging conditions; displacing oxygen prevents fat oxidation, unpleasant odor, and bad taste.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Flushing prevents oxidation, not dehydration sterilisation.
• Option (C): Incorrect. Nitrogen gas is not a chemical desiccant.
• Option (D): Incorrect. Nitrogen gas does not chemically react with food fats.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 44000),
    ),
    Question(
      id: 'sci_ch1_ex20_a',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Which statement correctly explains the term 'corrosion' along with an example?''',
      options: const [
        QuestionOption(id: 'A', text: 'The deterioration of metals by action of air, moisture, or acids; e.g., reddish-brown coating on iron', isCorrect: true),
        QuestionOption(id: 'B', text: 'The rapid thermal decomposition of metals in flame; e.g., dazzling white light from magnesium', isCorrect: false),
        QuestionOption(id: 'C', text: 'The violent dissolution of alkali metals in water; e.g., effervescence of sodium in water', isCorrect: false),
        QuestionOption(id: 'D', text: 'The coating of non-reactive metals over plastics; e.g., chrome electroplating on polymer trim', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) The deterioration of metals by action of air, moisture, or acids; e.g., reddish-brown coating on iron

Scientific Principle / Key Concept:
Corrosion is the slow eating away of metals by environmental agents; rusting of iron, black coating on silver, and green coating on copper are textbook examples.

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Combustion in flame is rapid oxidation, not corrosion.
• Option (C): Incorrect. Violent single displacement is not corrosion.
• Option (D): Incorrect. Electroplating is an industrial manufacturing technique, not metal corrosion.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 45000),
    ),
    Question(
      id: 'sci_ch1_ex20_b',
      subject: Subject.science,
      chapterId: 'sci_ch_01_chemical_reactions_equations',
      questionText: r'''Which statement correctly explains the term 'rancidity' along with an example?''',
      options: const [
        QuestionOption(id: 'A', text: 'The oxidation of fats and oils leading to foul smell and altered taste; e.g., butter left exposed in warm air', isCorrect: true),
        QuestionOption(id: 'B', text: 'The bacterial fermentation of dairy milk sugars into lactic acid; e.g., formation of sour curd', isCorrect: false),
        QuestionOption(id: 'C', text: 'The loss of hydration water from stored bakery items; e.g., hardening of bread in ambient air', isCorrect: false),
        QuestionOption(id: 'D', text: 'The thermal caramelisation of carbohydrates; e.g., browning of table sugar upon gentle heating', isCorrect: false),
      ],
      stepByStepSolution: r'''Correct Answer: (A) The oxidation of fats and oils leading to foul smell and altered taste; e.g., butter left exposed in warm air

Scientific Principle / Key Concept:
When fats and oils undergo atmospheric oxidation, they produce volatile, foul-smelling carboxylic acids and aldehydes (rancidity).

Detailed Distractor & Misconception Analysis:
• Option (B): Incorrect. Lactic fermentation is enzymatic bacterial fermentation, not lipid rancidity.
• Option (C): Incorrect. Staling/drying is physical water loss, not fat oxidation.
• Option (D): Incorrect. Caramelisation is thermal sugar degradation, not oil rancidity.''',
      difficultyLevel: DifficultyLevel.easy,
      status: QuestionStatus.approved,
      submittedBy: '00000000-0000-0000-0000-000000000001',
      reviewedBy: '00000000-0000-0000-0000-000000000001',
      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000 + 46000),
    ),
  ];
}
