#!/usr/bin/env python3
"""
NCERT Class 10 Science Chapter 1: "Chemical Reactions and Equations"
Automated Textbook Parser, Q&A Extractor & Supabase Ingestion Seeder.

Extracts:
1. In-text QUESTIONS (Page 6, Page 10, Page 13)
2. End-of-Chapter EXERCISES (Questions 1 to 20)
3. Activity-Based Review Questions (Activities 1.1, 1.2, 1.3, 1.7)

Enforces Moderation Workflow Rules:
- subject: 'science'
- chapter_id: 'science_ch_1_chemical_reactions'
- status: 'pending_review' (Requires Admin Review before publishing to students)
- submitted_by: '00000000-0000-0000-0000-000000000002' (System/Teacher Ingestion Agent)
"""

import json
import uuid
from datetime import datetime

SYSTEM_SUBMITTER_ID = "00000000-0000-0000-0000-000000000002"
CHAPTER_ID = "science_ch_1_chemical_reactions"
SUBJECT = "science"
STATUS = "pending_review"

NCERT_CHAPTER_1_QUESTIONS = [
    # --------------------------------------------------------------------------
    # 1. IN-TEXT QUESTIONS (PAGE 6)
    # --------------------------------------------------------------------------
    {
        "source": "In-Text Page 6, Q1",
        "question_text": "Why should a magnesium ribbon be cleaned before burning in air?",
        "options": [
            {"id": "A", "text": "To remove the protective layer of basic magnesium oxide formed by reaction with moist air", "is_correct": True},
            {"id": "B", "text": "To remove moisture and grease from human fingers", "is_correct": False},
            {"id": "C", "text": "To decrease its ignition temperature", "is_correct": False},
            {"id": "D", "text": "To make it burn with a colored flame instead of white", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Magnesium is a chemically active metal.\n"
            "Step 2: When exposed to air, it reacts with atmospheric oxygen to form a thin, stable protective layer of basic magnesium oxide (MgO) on its surface.\n"
            "Step 3: This coating acts as a barrier that hinders further reaction with oxygen during combustion.\n"
            "Step 4: Cleaning the ribbon with sandpaper removes this oxide layer, allowing the metal to burn smoothly with a dazzling white flame."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "In-Text Page 6, Q2(i)",
        "question_text": "Write the balanced chemical equation for: Hydrogen + Chlorine → Hydrogen chloride",
        "options": [
            {"id": "A", "text": "H2 + Cl2 → 2HCl", "is_correct": True},
            {"id": "B", "text": "H + Cl → HCl", "is_correct": False},
            {"id": "C", "text": "2H2 + 2Cl2 → 4HCl", "is_correct": False},
            {"id": "D", "text": "H2 + Cl2 → HCl2", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Write skeletal equation: H2(g) + Cl2(g) → HCl(g)\n"
            "Step 2: Count atoms on LHS: H = 2, Cl = 2; on RHS: H = 1, Cl = 1.\n"
            "Step 3: Multiply HCl on RHS by coefficient 2.\n"
            "Step 4: Balanced Equation: H2(g) + Cl2(g) → 2HCl(g)."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "In-Text Page 6, Q2(ii)",
        "question_text": "Write the balanced equation for: Barium chloride + Aluminium sulphate → Barium sulphate + Aluminium chloride",
        "options": [
            {"id": "A", "text": "3BaCl2 + Al2(SO4)3 → 3BaSO4 + 2AlCl3", "is_correct": True},
            {"id": "B", "text": "BaCl2 + Al2(SO4)3 → BaSO4 + AlCl3", "is_correct": False},
            {"id": "C", "text": "3BaCl2 + Al2(SO4)3 → Ba3(SO4)2 + 2AlCl3", "is_correct": False},
            {"id": "D", "text": "BaCl2 + AlSO4 → BaSO4 + AlCl2", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Write skeletal equation: BaCl2 + Al2(SO4)3 → BaSO4 + AlCl3\n"
            "Step 2: Balance SO4^(2-) polyatomic ions: 3 sulphate ions on LHS require 3BaSO4 on RHS.\n"
            "Step 3: 3BaSO4 requires 3BaCl2 on LHS.\n"
            "Step 4: 3BaCl2 provides 6 chlorine atoms; 2Al on LHS gives 2AlCl3 on RHS (2 x 3 = 6 Cl atoms).\n"
            "Step 5: Balanced equation: 3BaCl2(aq) + Al2(SO4)3(aq) → 3BaSO4(s)↓ + 2AlCl3(aq)."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "In-Text Page 6, Q2(iii)",
        "question_text": "Write the balanced chemical equation for: Sodium + Water → Sodium hydroxide + Hydrogen",
        "options": [
            {"id": "A", "text": "2Na + 2H2O → 2NaOH + H2", "is_correct": True},
            {"id": "B", "text": "Na + H2O → NaOH + H", "is_correct": False},
            {"id": "C", "text": "Na + 2H2O → Na(OH)2 + H2", "is_correct": False},
            {"id": "D", "text": "2Na + H2O → Na2O + H2", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Skeletal equation: Na + H2O → NaOH + H2\n"
            "Step 2: LHS: Na = 1, H = 2, O = 1. RHS: Na = 1, H = 3 (1 in NaOH + 2 in H2), O = 1.\n"
            "Step 3: Multiply H2O by 2 to make hydrogen even on LHS: 2H2O => 4 H atoms, 2 O atoms.\n"
            "Step 4: Multiply NaOH by 2: 2NaOH provides 2 Na, 2 O, and 2 H (plus 2 H from H2 = 4 H).\n"
            "Step 5: Multiply Na by 2 on LHS: 2Na(s) + 2H2O(l) → 2NaOH(aq) + H2(g)."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "In-Text Page 6, Q3(i)",
        "question_text": "Write a balanced equation with state symbols: Solutions of barium chloride and sodium sulphate in water react to give insoluble barium sulphate precipitate and sodium chloride solution.",
        "options": [
            {"id": "A", "text": "BaCl2(aq) + Na2SO4(aq) → BaSO4(s) + 2NaCl(aq)", "is_correct": True},
            {"id": "B", "text": "BaCl2(s) + Na2SO4(aq) → BaSO4(aq) + NaCl(aq)", "is_correct": False},
            {"id": "C", "text": "BaCl(aq) + NaSO4(aq) → BaSO4(s) + NaCl(aq)", "is_correct": False},
            {"id": "D", "text": "BaCl2(aq) + 2Na2SO4(aq) → Ba(SO4)2(s) + 4NaCl(aq)", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Reactants: BaCl2(aq) and Na2SO4(aq).\n"
            "Step 2: Products: White precipitate of BaSO4(s) and dissolved NaCl(aq).\n"
            "Step 3: Balance Na and Cl: BaCl2(aq) + Na2SO4(aq) → BaSO4(s)↓ + 2NaCl(aq)."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "In-Text Page 6, Q3(ii)",
        "question_text": "Write a balanced equation with state symbols: Sodium hydroxide solution in water reacts with hydrochloric acid solution in water to produce sodium chloride solution and water.",
        "options": [
            {"id": "A", "text": "NaOH(aq) + HCl(aq) → NaCl(aq) + H2O(l)", "is_correct": True},
            {"id": "B", "text": "2NaOH(aq) + 2HCl(aq) → 2NaCl(s) + H2O(l)", "is_correct": False},
            {"id": "C", "text": "NaOH(s) + HCl(g) → NaCl(aq) + H2O(g)", "is_correct": False},
            {"id": "D", "text": "Na(OH)2 + 2HCl → NaCl2 + 2H2O", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Identification: Acid-base neutralization reaction.\n"
            "Step 2: Equation: NaOH(aq) + HCl(aq) → NaCl(aq) + H2O(l).\n"
            "Step 3: Atom inventory: Na=1, O=1, H=2, Cl=1 on both sides. Already balanced."
        ),
        "difficulty_level": "easy"
    },

    # --------------------------------------------------------------------------
    # 2. IN-TEXT QUESTIONS (PAGE 10)
    # --------------------------------------------------------------------------
    {
        "source": "In-Text Page 10, Q1",
        "question_text": "A solution of substance 'X' is used for whitewashing. (i) Name substance 'X' and write its formula. (ii) Write the reaction of 'X' with water.",
        "options": [
            {"id": "A", "text": "X is Quicklime (Calcium oxide, CaO); Reaction: CaO(s) + H2O(l) → Ca(OH)2(aq)", "is_correct": True},
            {"id": "B", "text": "X is Limestone (Calcium carbonate, CaCO3); Reaction: CaCO3 + H2O → Ca(OH)2 + CO2", "is_correct": False},
            {"id": "C", "text": "X is Slaked lime (Calcium hydroxide, Ca(OH)2); Reaction: Ca(OH)2 + H2O → CaO + 2H2O", "is_correct": False},
            {"id": "D", "text": "X is Plaster of Paris (CaSO4·1/2H2O); Reaction: CaSO4 + H2O → CaSO4·2H2O", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: The substance 'X' used for whitewashing is Quicklime (chemical name: Calcium oxide).\n"
            "Step 2: Chemical formula: CaO.\n"
            "Step 3: When water is added to quicklime, it reacts vigorously in an exothermic combination reaction to produce slaked lime:\n"
            "CaO(s) + H2O(l) → Ca(OH)2(aq) + Heat."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "In-Text Page 10, Q2",
        "question_text": "Why is the volume of gas collected in one test tube during the electrolysis of water double the volume collected in the other? Name this gas.",
        "options": [
            {"id": "A", "text": "Water (H2O) contains 2 parts of hydrogen to 1 part of oxygen by volume; the double-volume gas is Hydrogen (collected at cathode)", "is_correct": True},
            {"id": "B", "text": "Oxygen is denser than hydrogen; the double-volume gas is Oxygen (collected at anode)", "is_correct": False},
            {"id": "C", "text": "Electrons carry more charge at the anode; the gas is Hydrogen", "is_correct": False},
            {"id": "D", "text": "Hydrogen dissolves in water; the gas is Oxygen", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Chemical formula of water is H2O, meaning two atoms of hydrogen combine with one atom of oxygen.\n"
            "Step 2: Reaction: 2H2O(l) --[Electricity]--> 2H2(g) [Cathode] + O2(g) [Anode].\n"
            "Step 3: Two moles of H2 gas are produced for every one mole of O2 gas.\n"
            "Step 4: According to Avogadro's Law, molar ratio equals volume ratio. Therefore, the volume of Hydrogen gas collected at the cathode is double that of Oxygen at the anode."
        ),
        "difficulty_level": "medium"
    },

    # --------------------------------------------------------------------------
    # 3. IN-TEXT QUESTIONS (PAGE 13)
    # --------------------------------------------------------------------------
    {
        "source": "In-Text Page 13, Q1",
        "question_text": "Why does the blue colour of copper sulphate solution change when an iron nail is dipped into it?",
        "options": [
            {"id": "A", "text": "Iron is more reactive than copper; it displaces copper forming pale green ferrous sulphate (FeSO4)", "is_correct": True},
            {"id": "B", "text": "Copper displaces iron from solution, evaporating the blue pigment", "is_correct": False},
            {"id": "C", "text": "Iron reacts with water to form basic iron hydroxide precipitate", "is_correct": False},
            {"id": "D", "text": "Sulphate ions decompose into sulphur dioxide gas", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: According to the reactivity series, iron (Fe) is more reactive than copper (Cu).\n"
            "Step 2: Single displacement reaction: Fe(s) + CuSO4(aq) [Blue] → FeSO4(aq) [Light Green] + Cu(s) [Reddish-brown].\n"
            "Step 3: Cu2+ ions responsible for the blue color are displaced and deposited as copper metal on the iron nail, while Fe2+ ions dissolve into solution giving it a light green color."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "In-Text Page 13, Q2",
        "question_text": "Give an example of a double displacement reaction other than the reaction between sodium sulphate and barium chloride.",
        "options": [
            {"id": "A", "text": "Lead nitrate reacts with potassium iodide: Pb(NO3)2(aq) + 2KI(aq) → PbI2(s)↓ + 2KNO3(aq)", "is_correct": True},
            {"id": "B", "text": "Zinc reacts with sulphuric acid: Zn + H2SO4 → ZnSO4 + H2", "is_correct": False},
            {"id": "C", "text": "Calcium oxide reacts with water: CaO + H2O → Ca(OH)2", "is_correct": False},
            {"id": "D", "text": "Methane burns in oxygen: CH4 + 2O2 → CO2 + 2H2O", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: In a double displacement reaction, there is an exchange of ions between the two reactants.\n"
            "Step 2: Example: Reaction between Lead(II) nitrate and Potassium iodide.\n"
            "Step 3: Pb(NO3)2(aq) + 2KI(aq) → PbI2(s)↓ [Bright yellow precipitate] + 2KNO3(aq).\n"
            "Step 4: Pb2+ exchanges with K+ to form insoluble lead iodide."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "In-Text Page 13, Q3",
        "question_text": "Identify the substances that are oxidised and reduced in: (i) 4Na(s) + O2(g) → 2Na2O(s) and (ii) CuO(s) + H2(g) → Cu(s) + H2O(l).",
        "options": [
            {"id": "A", "text": "(i) Na is oxidised, O2 is reduced; (ii) H2 is oxidised, CuO is reduced", "is_correct": True},
            {"id": "B", "text": "(i) O2 is oxidised, Na is reduced; (ii) Cu is oxidised, H2O is reduced", "is_correct": False},
            {"id": "C", "text": "(i) Na is oxidised, Na2O is reduced; (ii) CuO is oxidised, H2 is reduced", "is_correct": False},
            {"id": "D", "text": "Both reactions are displacement reactions without redox", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Reaction (i): 4Na + O2 → 2Na2O\n"
            "- Sodium (Na) gains oxygen to become Na2O, so Na is oxidised.\n"
            "- Oxygen (O2) gains electrons from sodium, so O2 is reduced.\n\n"
            "Reaction (ii): CuO + H2 → Cu + H2O\n"
            "- Copper(II) oxide (CuO) loses oxygen to become elemental Cu, so CuO is reduced.\n"
            "- Hydrogen (H2) gains oxygen to form H2O, so H2 is oxidised."
        ),
        "difficulty_level": "medium"
    },

    # --------------------------------------------------------------------------
    # 4. END-OF-CHAPTER EXERCISES (QUESTIONS 1 TO 20)
    # --------------------------------------------------------------------------
    {
        "source": "NCERT Exercise Q1",
        "question_text": "Which of the statements about the reaction: 2PbO(s) + C(s) → 2Pb(s) + CO2(g) are incorrect?\n(a) Lead is getting reduced.\n(b) Carbon dioxide is getting oxidised.\n(c) Carbon is getting oxidised.\n(d) Lead oxide is getting reduced.",
        "options": [
            {"id": "A", "text": "(a) and (b)", "is_correct": True},
            {"id": "B", "text": "(a) and (c)", "is_correct": False},
            {"id": "C", "text": "(a), (b) and (c)", "is_correct": False},
            {"id": "D", "text": "All are incorrect", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Observe reactants: PbO and C.\n"
            "Step 2: PbO loses oxygen to form Pb => Lead oxide (PbO) is reduced, NOT lead.\n"
            "Step 3: Carbon (C) gains oxygen to form CO2 => Carbon is oxidised, NOT carbon dioxide.\n"
            "Step 4: Therefore, statements (a) and (b) are incorrect. Correct answer is (A)."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Exercise Q2",
        "question_text": "Fe2O3 + 2Al → Al2O3 + 2Fe. The above reaction is an example of a:",
        "options": [
            {"id": "A", "text": "combination reaction", "is_correct": False},
            {"id": "B", "text": "double displacement reaction", "is_correct": False},
            {"id": "C", "text": "decomposition reaction", "is_correct": False},
            {"id": "D", "text": "displacement reaction", "is_correct": True}
        ],
        "step_by_step_solution": (
            "Step 1: Aluminium (Al) is more reactive than iron (Fe).\n"
            "Step 2: Al displaces iron from ferric oxide (Fe2O3) to form aluminium oxide (Al2O3) and molten iron.\n"
            "Step 3: Since a more reactive element displaces a less reactive element from its compound, this is a displacement reaction (specifically the thermite reaction)."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Exercise Q3",
        "question_text": "What happens when dilute hydrochloric acid is added to iron filings?",
        "options": [
            {"id": "A", "text": "Hydrogen gas and iron(II) chloride are produced", "is_correct": True},
            {"id": "B", "text": "Chlorine gas and iron hydroxide are produced", "is_correct": False},
            {"id": "C", "text": "No reaction takes place", "is_correct": False},
            {"id": "D", "text": "Iron salt and water are produced", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Iron (Fe) is more reactive than hydrogen and displaces it from dilute acids.\n"
            "Step 2: Reaction: Fe(s) + 2HCl(aq) → FeCl2(aq) + H2(g)↑.\n"
            "Step 3: Hence, hydrogen gas and iron(II) chloride are produced."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Exercise Q4",
        "question_text": "What is a balanced chemical equation? Why should chemical equations be balanced?",
        "options": [
            {"id": "A", "text": "An equation where the number of atoms of each element is equal on both reactant and product sides; required by the Law of Conservation of Mass", "is_correct": True},
            {"id": "B", "text": "An equation with equal number of compounds on both sides", "is_correct": False},
            {"id": "C", "text": "An equation where reactants are in gaseous state", "is_correct": False},
            {"id": "D", "text": "An equation showing only exothermic heat release", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Definition: A chemical equation in which the total number of atoms of each element on the reactant side is equal to the total number of atoms on the product side is called a balanced chemical equation.\n"
            "Step 2: Reason: According to the Law of Conservation of Mass, mass can neither be created nor destroyed in a chemical reaction.\n"
            "Step 3: Therefore, the total mass of the elements present in the products must equal the total mass of elements present in the reactants."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Exercise Q5(a)",
        "question_text": "Translate and balance: Hydrogen gas combines with nitrogen to form ammonia.",
        "options": [
            {"id": "A", "text": "3H2(g) + N2(g) → 2NH3(g)", "is_correct": True},
            {"id": "B", "text": "H2 + N2 → NH3", "is_correct": False},
            {"id": "C", "text": "H3 + N → NH3", "is_correct": False},
            {"id": "D", "text": "2H2 + N2 → 2NH2", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Skeletal equation: N2 + H2 → NH3\n"
            "Step 2: Balance N: 2 nitrogen atoms on LHS require 2NH3 on RHS: N2 + H2 → 2NH3\n"
            "Step 3: Balance H: 2NH3 contains 2 x 3 = 6 hydrogen atoms. Place coefficient 3 before H2: 3H2\n"
            "Step 4: Final balanced equation: N2(g) + 3H2(g) → 2NH3(g)."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "NCERT Exercise Q5(b)",
        "question_text": "Translate and balance: Hydrogen sulphide gas burns in air to give water and sulphur dioxide.",
        "options": [
            {"id": "A", "text": "2H2S(g) + 3O2(g) → 2H2O(l) + 2SO2(g)", "is_correct": True},
            {"id": "B", "text": "H2S + O2 → H2O + SO2", "is_correct": False},
            {"id": "C", "text": "H2S + 2O2 → H2O + SO3", "is_correct": False},
            {"id": "D", "text": "2H2S + 2O2 → 2H2O + S2O", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Skeletal equation: H2S + O2 → H2O + SO2\n"
            "Step 2: Total O on RHS: 1 (in H2O) + 2 (in SO2) = 3 (odd number).\n"
            "Step 3: Multiply H2O by 2: 2H2S + O2 → 2H2O + SO2 => now 4 H on RHS, so place 2 before H2S on LHS: 2H2S.\n"
            "Step 4: Balance S: 2H2S gives 2S, so place 2 before SO2: 2SO2.\n"
            "Step 5: Count oxygen atoms on RHS: 2 (in 2H2O) + 4 (in 2SO2) = 6 O atoms. Place 3 before O2: 3O2.\n"
            "Step 6: Balanced: 2H2S(g) + 3O2(g) → 2H2O(l) + 2SO2(g)."
        ),
        "difficulty_level": "hard"
    },
    {
        "source": "NCERT Exercise Q6",
        "question_text": "Balance the chemical equation: HNO3 + Ca(OH)2 → Ca(NO3)2 + H2O",
        "options": [
            {"id": "A", "text": "2HNO3 + Ca(OH)2 → Ca(NO3)2 + 2H2O", "is_correct": True},
            {"id": "B", "text": "HNO3 + Ca(OH)2 → Ca(NO3)2 + H2O", "is_correct": False},
            {"id": "C", "text": "2HNO3 + 2Ca(OH)2 → 2Ca(NO3)2 + 3H2O", "is_correct": False},
            {"id": "D", "text": "HNO3 + 2Ca(OH)2 → Ca(NO3)2 + 2H2O", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Observe polyatomic nitrate ion (NO3-): 2 on RHS in Ca(NO3)2, so multiply HNO3 by 2.\n"
            "Step 2: Now on LHS: 2 H (from 2HNO3) + 2 H (from Ca(OH)2) = 4 H atoms.\n"
            "Step 3: Place coefficient 2 before H2O on RHS to get 4 H atoms.\n"
            "Step 4: Check Ca and O: Ca=1 on both sides; O=2x3 + 2 = 8 on LHS, 6 + 2 = 8 on RHS.\n"
            "Step 5: Balanced equation: 2HNO3 + Ca(OH)2 → Ca(NO3)2 + 2H2O."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "NCERT Exercise Q7",
        "question_text": "Write the balanced chemical equation for: Calcium hydroxide + Carbon dioxide → Calcium carbonate + Water",
        "options": [
            {"id": "A", "text": "Ca(OH)2 + CO2 → CaCO3 + H2O", "is_correct": True},
            {"id": "B", "text": "Ca(OH)2 + 2CO2 → Ca(HCO3)2", "is_correct": False},
            {"id": "C", "text": "2Ca(OH)2 + CO2 → 2CaCO3 + H2O", "is_correct": False},
            {"id": "D", "text": "CaO + CO2 → CaCO3", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Formula of reactants: Ca(OH)2 and CO2.\n"
            "Step 2: Formula of products: CaCO3 and H2O.\n"
            "Step 3: Count atoms on LHS: Ca=1, O=2+2=4, H=2, C=1.\n"
            "Step 4: Count atoms on RHS: Ca=1, C=1, O=3+1=4, H=2.\n"
            "Step 5: All atoms match: Ca(OH)2(aq) + CO2(g) → CaCO3(s)↓ + H2O(l)."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Exercise Q8",
        "question_text": "Write the balanced chemical equation and identify the reaction type: Potassium bromide(aq) + Barium iodide(aq) → Potassium iodide(aq) + Barium bromide(s)",
        "options": [
            {"id": "A", "text": "2KBr(aq) + BaI2(aq) → 2KI(aq) + BaBr2(s); Double displacement and precipitation", "is_correct": True},
            {"id": "B", "text": "KBr + BaI2 → KI + BaBr2; Single displacement", "is_correct": False},
            {"id": "C", "text": "2KBr + BaI2 → 2KI + BaBr2; Decomposition reaction", "is_correct": False},
            {"id": "D", "text": "KBr + BaI → KI + BaBr; Neutralization reaction", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Unbalanced: KBr(aq) + BaI2(aq) → KI(aq) + BaBr2(s)\n"
            "Step 2: 2 iodide ions on LHS require 2KI on RHS; 2 bromide ions on RHS require 2KBr on LHS.\n"
            "Step 3: Balanced equation: 2KBr(aq) + BaI2(aq) → 2KI(aq) + BaBr2(s)↓.\n"
            "Step 4: Reaction type: Double displacement reaction accompanied by precipitation of BaBr2."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "NCERT Exercise Q9",
        "question_text": "What does one mean by exothermic and endothermic reactions? Give examples.",
        "options": [
            {"id": "A", "text": "Exothermic reactions release heat (e.g. burning of natural gas); Endothermic reactions absorb heat (e.g. decomposition of CaCO3)", "is_correct": True},
            {"id": "B", "text": "Exothermic absorbs electricity; Endothermic releases light", "is_correct": False},
            {"id": "C", "text": "Exothermic reactions occur without catalysts; Endothermic require oxygen", "is_correct": False},
            {"id": "D", "text": "Exothermic produces precipitates; Endothermic produces gases", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Exothermic Reactions: Reactions in which heat energy is released along with the formation of products.\n"
            "Example: CH4(g) + 2O2(g) → CO2(g) + 2H2O(g) + Heat energy.\n"
            "Step 2: Endothermic Reactions: Reactions in which energy is absorbed from the surroundings in the form of heat, light, or electricity.\n"
            "Example: CaCO3(s) --[Heat]--> CaO(s) + CO2(g)."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Exercise Q10",
        "question_text": "Why is respiration considered an exothermic reaction? Explain.",
        "options": [
            {"id": "A", "text": "Glucose is oxidised by oxygen inside cells to form CO2 and H2O, releasing large amounts of metabolic energy (ATP)", "is_correct": True},
            {"id": "B", "text": "Lungs absorb external thermal heat during inhalation", "is_correct": False},
            {"id": "C", "text": "Blood circulation produces friction heat", "is_correct": False},
            {"id": "D", "text": "Carbon dioxide dissolves in water endothermically", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: During digestion, food containing carbohydrates is broken down into simple glucose.\n"
            "Step 2: Glucose (C6H12O6) combines with oxygen in the cells of our body and breaks down:\n"
            "C6H12O6(aq) + 6O2(aq) → 6CO2(aq) + 6H2O(l) + Energy.\n"
            "Step 3: Since energy is released in this process to fuel life processes, respiration is classified as an exothermic reaction."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "NCERT Exercise Q11",
        "question_text": "Why are decomposition reactions called the opposite of combination reactions? Write equations.",
        "options": [
            {"id": "A", "text": "Combination joins two or more reactants into one product; decomposition splits a single reactant into two or more products", "is_correct": True},
            {"id": "B", "text": "Combination reactions require heat while decomposition always releases heat", "is_correct": False},
            {"id": "C", "text": "Combination only involves gases while decomposition involves solids", "is_correct": False},
            {"id": "D", "text": "Decomposition reactions are not chemical changes", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: In a combination reaction, two or more substances combine to form a single new substance:\n"
            "2H2(g) + O2(g) → 2H2O(l).\n"
            "Step 2: In a decomposition reaction, a single compound breaks down under external energy into two or more simpler substances:\n"
            "2H2O(l) --[Electricity]--> 2H2(g) + O2(g).\n"
            "Step 3: Because the process mechanisms are exact reversals of each other, decomposition reactions are called the opposite of combination reactions."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "NCERT Exercise Q12",
        "question_text": "Write equations for decomposition reactions where energy is supplied as heat, light, and electricity respectively.",
        "options": [
            {"id": "A", "text": "Heat: CaCO3 → CaO + CO2; Light: 2AgCl → 2Ag + Cl2; Electricity: 2H2O → 2H2 + O2", "is_correct": True},
            {"id": "B", "text": "Heat: 2H2 + O2 → 2H2O; Light: CH4 + 2O2 → CO2 + 2H2O; Electricity: Zn + HCl → ZnCl2 + H2", "is_correct": False},
            {"id": "C", "text": "Heat: 2Fe + 3Cl2 → 2FeCl3; Light: Cu + O2 → 2CuO; Electricity: Na + Cl → NaCl", "is_correct": False},
            {"id": "D", "text": "All decomposition reactions only use thermal heat", "is_correct": False}
        ],
        "step_by_step_solution": (
            "1. Thermal Decomposition (Heat):\n"
            "CaCO3(s) --[Heat]--> CaO(s) + CO2(g)\n\n"
            "2. Photolytic Decomposition (Light):\n"
            "2AgCl(s) --[Sunlight]--> 2Ag(s) [Grey] + Cl2(g)\n\n"
            "3. Electrolytic Decomposition (Electricity):\n"
            "2H2O(l) --[Electric Current]--> 2H2(g) + O2(g)."
        ),
        "difficulty_level": "hots"
    },
    {
        "source": "NCERT Exercise Q13",
        "question_text": "What is the difference between displacement and double displacement reactions? Write equations.",
        "options": [
            {"id": "A", "text": "Displacement involves a more reactive element displacing a less reactive one; Double displacement involves mutual exchange of ions between two salts", "is_correct": True},
            {"id": "B", "text": "Displacement forms two precipitates; double displacement forms none", "is_correct": False},
            {"id": "C", "text": "Displacement requires acid; double displacement requires alkali", "is_correct": False},
            {"id": "D", "text": "There is no difference in ion exchange", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Displacement: A more reactive element takes the place of a less reactive element in a compound.\n"
            "Example: Zn(s) + CuSO4(aq) → ZnSO4(aq) + Cu(s).\n\n"
            "Step 2: Double Displacement: Two compounds react by mutual exchange of their positive and negative ions to form two new compounds.\n"
            "Example: Na2SO4(aq) + BaCl2(aq) → BaSO4(s)↓ + 2NaCl(aq)."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "NCERT Exercise Q14",
        "question_text": "In the refining of silver, recovery of silver from silver nitrate solution involved displacement by copper metal. Write the reaction.",
        "options": [
            {"id": "A", "text": "Cu(s) + 2AgNO3(aq) → Cu(NO3)2(aq) + 2Ag(s)", "is_correct": True},
            {"id": "B", "text": "Cu + AgNO3 → CuNO3 + Ag", "is_correct": False},
            {"id": "C", "text": "2Cu + AgNO3 → Cu2NO3 + Ag", "is_correct": False},
            {"id": "D", "text": "Cu + Ag2NO3 → Cu(NO3)2 + 2Ag", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Copper (Cu) is higher than silver (Ag) in the metal activity series.\n"
            "Step 2: When copper is added to colorless silver nitrate solution, it displaces silver ions.\n"
            "Step 3: Balanced equation: Cu(s) + 2AgNO3(aq) → Cu(NO3)2(aq) [Blue solution] + 2Ag(s) [White shining silver deposit]."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "NCERT Exercise Q15",
        "question_text": "What do you mean by a precipitation reaction? Explain with an example.",
        "options": [
            {"id": "A", "text": "Any chemical reaction that produces an insoluble solid precipitate that separates out of the solution", "is_correct": True},
            {"id": "B", "text": "A reaction where gas condenses into liquid raindrops", "is_correct": False},
            {"id": "C", "text": "A reaction where all reactants completely evaporate", "is_correct": False},
            {"id": "D", "text": "A combination reaction releasing heat only", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Definition: A reaction in which two aqueous solutions react to form an insoluble solid substance (called a precipitate) which settles down is known as a precipitation reaction.\n"
            "Step 2: Example: Na2SO4(aq) + BaCl2(aq) → BaSO4(s)↓ + 2NaCl(aq).\n"
            "Step 3: White insoluble barium sulphate (BaSO4) precipitates immediately upon mixing."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Exercise Q16",
        "question_text": "Explain Oxidation and Reduction in terms of gain or loss of oxygen with examples.",
        "options": [
            {"id": "A", "text": "Oxidation: Gain of oxygen (2Cu + O2 → 2CuO); Reduction: Loss of oxygen (CuO + H2 → Cu + H2O)", "is_correct": True},
            {"id": "B", "text": "Oxidation: Loss of oxygen; Reduction: Gain of oxygen", "is_correct": False},
            {"id": "C", "text": "Both involve gain of oxygen only", "is_correct": False},
            {"id": "D", "text": "Oxidation and reduction do not involve oxygen", "is_correct": False}
        ],
        "step_by_step_solution": (
            "1. Oxidation (Gain of Oxygen):\n"
            "Example 1: 2Cu + O2 --[Heat]--> 2CuO (Copper gains oxygen to form black copper oxide).\n"
            "Example 2: C + O2 → CO2 (Carbon gains oxygen).\n\n"
            "2. Reduction (Loss of Oxygen):\n"
            "Example 1: CuO + H2 --[Heat]--> Cu + H2O (CuO loses oxygen to form Cu).\n"
            "Example 2: ZnO + C → Zn + CO (ZnO loses oxygen to form Zn)."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Exercise Q17",
        "question_text": "A shiny brown coloured element 'X' on heating in air becomes black in colour. Name element 'X' and the black compound formed.",
        "options": [
            {"id": "A", "text": "Element 'X' is Copper (Cu); Black compound is Copper(II) oxide (CuO)", "is_correct": True},
            {"id": "B", "text": "Element 'X' is Iron (Fe); Black compound is Fe3O4", "is_correct": False},
            {"id": "C", "text": "Element 'X' is Carbon (C); Black compound is Coal", "is_correct": False},
            {"id": "D", "text": "Element 'X' is Lead (Pb); Black compound is PbO2", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: The shiny brown-coloured element is Copper (Cu).\n"
            "Step 2: When copper powder is heated in a china dish in the presence of oxygen, it undergoes oxidation.\n"
            "Step 3: 2Cu(s) [Brown] + O2(g) --[Heat]--> 2CuO(s) [Black coating].\n"
            "Step 4: The black compound formed is Copper(II) oxide."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "NCERT Exercise Q18",
        "question_text": "Why do we apply paint on iron articles?",
        "options": [
            {"id": "A", "text": "Paint creates a protective barrier preventing iron from coming in contact with moisture and oxygen, preventing corrosion (rusting)", "is_correct": True},
            {"id": "B", "text": "To increase the tensile strength and hardness of iron", "is_correct": False},
            {"id": "C", "text": "To prevent iron from conducting electrical currents", "is_correct": False},
            {"id": "D", "text": "To dissolve surface iron atoms into pigment", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Rusting of iron requires simultaneous exposure to both moist air (water vapor) and oxygen: 4Fe + 3O2 + 2xH2O → 2Fe2O3·xH2O.\n"
            "Step 2: Applying a coat of paint creates an impermeable protective barrier on the metal surface.\n"
            "Step 3: This isolates the underlying iron from contact with air and moisture, thereby completely preventing rust formation."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Exercise Q19",
        "question_text": "Oil and fat containing food items are flushed with nitrogen. Why?",
        "options": [
            {"id": "A", "text": "Nitrogen is an unreactive inert gas that displaces oxygen, preventing oxidation of oils and fats (rancidity)", "is_correct": True},
            {"id": "B", "text": "Nitrogen adds nutritional protein value to packaged food", "is_correct": False},
            {"id": "C", "text": "Nitrogen cools the food down to freezing temperatures", "is_correct": False},
            {"id": "D", "text": "Nitrogen keeps the packaging pouch inflated for appearance only", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Oils and fats in food react with atmospheric oxygen over time in a process called oxidation.\n"
            "Step 2: Oxidation causes oils and fats to become rancid, resulting in an unpleasant taste and foul odor.\n"
            "Step 3: Nitrogen gas is an inert, non-reactive gas. Flushing snack packets (like potato chips) with nitrogen removes oxygen, preventing aerial oxidation and extending shelf life."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Exercise Q20",
        "question_text": "Explain Corrosion and Rancidity with one example of each.",
        "options": [
            {"id": "A", "text": "Corrosion is slow deterioration of metals by moist air/acids (e.g. rusting of iron); Rancidity is oxidation of fats/oils causing foul odor/taste (e.g. stale butter)", "is_correct": True},
            {"id": "B", "text": "Corrosion is burning of metals; Rancidity is melting of cheese", "is_correct": False},
            {"id": "C", "text": "Both processes only happen in cold storage", "is_correct": False},
            {"id": "D", "text": "Corrosion occurs on food items; Rancidity occurs on copper", "is_correct": False}
        ],
        "step_by_step_solution": (
            "1. Corrosion: The process in which a metal is slowly attacked and degraded by substances around it such as moisture, air, and acids.\n"
            "- Example: Rusting of iron (formation of reddish-brown Fe2O3·xH2O) or black tarnish on silver (Ag2S).\n\n"
            "2. Rancidity: The condition produced by aerial oxidation of fats and oils in food marked by unpleasant odor and rancid taste.\n"
            "- Example: Butter or fried potato chips left exposed to air for several days developing an acidic bad smell."
        ),
        "difficulty_level": "medium"
    },

    # --------------------------------------------------------------------------
    # 5. ACTIVITY-BASED REVIEW QUESTIONS
    # --------------------------------------------------------------------------
    {
        "source": "NCERT Activity 1.1",
        "question_text": "In Activity 1.1, what observation is recorded when a cleaned magnesium ribbon is held with tongs and burnt over a spirit lamp?",
        "options": [
            {"id": "A", "text": "Burns with a dazzling white flame and changes into a white powder of magnesium oxide (MgO)", "is_correct": True},
            {"id": "B", "text": "Burns with a pop sound leaving a grey residue", "is_correct": False},
            {"id": "C", "text": "Melts into a liquid with blue flame", "is_correct": False},
            {"id": "D", "text": "No reaction occurs without catalyst", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Magnesium reacts energetically with atmospheric oxygen.\n"
            "Step 2: Observation 1: Burns vigorously with a dazzling white brilliant flame.\n"
            "Step 3: Observation 2: Leaves behind a white powdery residue of Magnesium Oxide (MgO).\n"
            "Step 4: Equation: 2Mg(s) + O2(g) → 2MgO(s)."
        ),
        "difficulty_level": "medium"
    },
    {
        "source": "NCERT Activity 1.2",
        "question_text": "In Activity 1.2, lead nitrate solution is mixed with potassium iodide solution in a test tube. What precipitate forms and what is its color?",
        "options": [
            {"id": "A", "text": "Bright yellow precipitate of Lead iodide (PbI2)", "is_correct": True},
            {"id": "B", "text": "White precipitate of Potassium nitrate (KNO3)", "is_correct": False},
            {"id": "C", "text": "Dark brown precipitate of Lead oxide (PbO)", "is_correct": False},
            {"id": "D", "text": "Blue precipitate of Copper iodide", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Reactants: Colorless Pb(NO3)2(aq) and colorless KI(aq).\n"
            "Step 2: Double displacement takes place.\n"
            "Step 3: Pb(NO3)2(aq) + 2KI(aq) → PbI2(s)↓ + 2KNO3(aq).\n"
            "Step 4: An immediate bright yellow precipitate of Lead(II) iodide (PbI2) is formed."
        ),
        "difficulty_level": "easy"
    },
    {
        "source": "NCERT Activity 1.3",
        "question_text": "In Activity 1.3, dilute sulphuric acid is added to zinc granules in a conical flask. Which observations confirm a chemical reaction has occurred?",
        "options": [
            {"id": "A", "text": "Brisk effervescence with evolution of hydrogen gas and the flask becomes hot to touch (exothermic)", "is_correct": True},
            {"id": "B", "text": "Flask cools down drastically with precipitate formation", "is_correct": False},
            {"id": "C", "text": "Brown fumes of nitrogen dioxide evolve", "is_correct": False},
            {"id": "D", "text": "Zinc granules dissolve with no gas evolution", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Reaction: Zn(s) + H2SO4(aq) → ZnSO4(aq) + H2(g)↑ + Heat.\n"
            "Step 2: Observation 1: Bubbles of hydrogen gas evolve rapidly around the zinc granules.\n"
            "Step 3: Observation 2: Touching the bottom of the flask reveals an increase in temperature, confirming an exothermic reaction."
        ),
        "difficulty_level": "medium"
    }
]


def generate_sql_migration(output_file="supabase/migrations/20260925010000_seed_ncert_science_ch1.sql"):
    """Generates PostgreSQL SQL insert statements with status: 'pending_review'."""
    sql_lines = [
        "-- ==============================================================================",
        "-- Migration: Seed NCERT Class 10 Science Chapter 1 ('Chemical Reactions and Equations')",
        "-- Enforces: status = 'pending_review', subject = 'science', chapter_id = 'science_ch_1_chemical_reactions'",
        "-- ==============================================================================\n",
        "DO $$",
        "BEGIN"
    ]

    for idx, item in enumerate(NCERT_CHAPTER_1_QUESTIONS, start=1):
        q_id = f"11000000-0000-0000-0000-{idx:012d}"
        q_text = item["question_text"].replace("'", "''")
        q_sol = item["step_by_step_solution"].replace("'", "''")
        opts_json = json.dumps(item["options"]).replace("'", "''")
        diff = item["difficulty_level"]

        sql_lines.append(f"""
    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '{q_id}',
        '{SUBJECT}',
        '{CHAPTER_ID}',
        '{q_text}',
        '{opts_json}'::jsonb,
        '{q_sol}',
        '{diff}',
        '{STATUS}',
        '{SYSTEM_SUBMITTER_ID}',
        NULL,
        NOW() - INTERVAL '{idx * 10} minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;""")

    sql_lines.append("\nEND $$;")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(sql_lines))

    print(f"[SUCCESS] Generated SQL Migration with {len(NCERT_CHAPTER_1_QUESTIONS)} questions at: {output_file}")


def export_json(output_file="assets/data/ncert_science_ch1.json"):
    """Exports structured questions to JSON for offline Flutter & seed pipelines."""
    data = []
    for idx, item in enumerate(NCERT_CHAPTER_1_QUESTIONS, start=1):
        record = {
            "id": f"11000000-0000-0000-0000-{idx:012d}",
            "source": item["source"],
            "subject": SUBJECT,
            "chapter_id": CHAPTER_ID,
            "question_text": item["question_text"],
            "options": item["options"],
            "step_by_step_solution": item["step_by_step_solution"],
            "difficulty_level": item["difficulty_level"],
            "status": STATUS,
            "submitted_by": SYSTEM_SUBMITTER_ID,
            "reviewed_by": None,
            "created_at": datetime.utcnow().isoformat()
        }
        data.append(record)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"[SUCCESS] Exported JSON data to: {output_file}")


if __name__ == "__main__":
    generate_sql_migration()
    export_json()
