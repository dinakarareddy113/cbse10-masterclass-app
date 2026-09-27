-- ==============================================================================
-- Migration: Seed NCERT Class 10 Science Chapter 1 ('Chemical Reactions and Equations')
-- Enforces: status = 'pending_review', subject = 'science', chapter_id = 'science_ch_1_chemical_reactions'
-- ==============================================================================

DO $$
BEGIN

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000001',
        'science',
        'science_ch_1_chemical_reactions',
        'Why should a magnesium ribbon be cleaned before burning in air?',
        '[{"id": "A", "text": "To remove the protective layer of basic magnesium oxide formed by reaction with moist air", "is_correct": true}, {"id": "B", "text": "To remove moisture and grease from human fingers", "is_correct": false}, {"id": "C", "text": "To decrease its ignition temperature", "is_correct": false}, {"id": "D", "text": "To make it burn with a colored flame instead of white", "is_correct": false}]'::jsonb,
        'Step 1: Magnesium is a chemically active metal.
Step 2: When exposed to air, it reacts with atmospheric oxygen to form a thin, stable protective layer of basic magnesium oxide (MgO) on its surface.
Step 3: This coating acts as a barrier that hinders further reaction with oxygen during combustion.
Step 4: Cleaning the ribbon with sandpaper removes this oxide layer, allowing the metal to burn smoothly with a dazzling white flame.',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '10 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000002',
        'science',
        'science_ch_1_chemical_reactions',
        'Write the balanced chemical equation for: Hydrogen + Chlorine → Hydrogen chloride',
        '[{"id": "A", "text": "H2 + Cl2 \u2192 2HCl", "is_correct": true}, {"id": "B", "text": "H + Cl \u2192 HCl", "is_correct": false}, {"id": "C", "text": "2H2 + 2Cl2 \u2192 4HCl", "is_correct": false}, {"id": "D", "text": "H2 + Cl2 \u2192 HCl2", "is_correct": false}]'::jsonb,
        'Step 1: Write skeletal equation: H2(g) + Cl2(g) → HCl(g)
Step 2: Count atoms on LHS: H = 2, Cl = 2; on RHS: H = 1, Cl = 1.
Step 3: Multiply HCl on RHS by coefficient 2.
Step 4: Balanced Equation: H2(g) + Cl2(g) → 2HCl(g).',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '20 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000003',
        'science',
        'science_ch_1_chemical_reactions',
        'Write the balanced equation for: Barium chloride + Aluminium sulphate → Barium sulphate + Aluminium chloride',
        '[{"id": "A", "text": "3BaCl2 + Al2(SO4)3 \u2192 3BaSO4 + 2AlCl3", "is_correct": true}, {"id": "B", "text": "BaCl2 + Al2(SO4)3 \u2192 BaSO4 + AlCl3", "is_correct": false}, {"id": "C", "text": "3BaCl2 + Al2(SO4)3 \u2192 Ba3(SO4)2 + 2AlCl3", "is_correct": false}, {"id": "D", "text": "BaCl2 + AlSO4 \u2192 BaSO4 + AlCl2", "is_correct": false}]'::jsonb,
        'Step 1: Write skeletal equation: BaCl2 + Al2(SO4)3 → BaSO4 + AlCl3
Step 2: Balance SO4^(2-) polyatomic ions: 3 sulphate ions on LHS require 3BaSO4 on RHS.
Step 3: 3BaSO4 requires 3BaCl2 on LHS.
Step 4: 3BaCl2 provides 6 chlorine atoms; 2Al on LHS gives 2AlCl3 on RHS (2 x 3 = 6 Cl atoms).
Step 5: Balanced equation: 3BaCl2(aq) + Al2(SO4)3(aq) → 3BaSO4(s)↓ + 2AlCl3(aq).',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '30 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000004',
        'science',
        'science_ch_1_chemical_reactions',
        'Write the balanced chemical equation for: Sodium + Water → Sodium hydroxide + Hydrogen',
        '[{"id": "A", "text": "2Na + 2H2O \u2192 2NaOH + H2", "is_correct": true}, {"id": "B", "text": "Na + H2O \u2192 NaOH + H", "is_correct": false}, {"id": "C", "text": "Na + 2H2O \u2192 Na(OH)2 + H2", "is_correct": false}, {"id": "D", "text": "2Na + H2O \u2192 Na2O + H2", "is_correct": false}]'::jsonb,
        'Step 1: Skeletal equation: Na + H2O → NaOH + H2
Step 2: LHS: Na = 1, H = 2, O = 1. RHS: Na = 1, H = 3 (1 in NaOH + 2 in H2), O = 1.
Step 3: Multiply H2O by 2 to make hydrogen even on LHS: 2H2O => 4 H atoms, 2 O atoms.
Step 4: Multiply NaOH by 2: 2NaOH provides 2 Na, 2 O, and 2 H (plus 2 H from H2 = 4 H).
Step 5: Multiply Na by 2 on LHS: 2Na(s) + 2H2O(l) → 2NaOH(aq) + H2(g).',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '40 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000005',
        'science',
        'science_ch_1_chemical_reactions',
        'Write a balanced equation with state symbols: Solutions of barium chloride and sodium sulphate in water react to give insoluble barium sulphate precipitate and sodium chloride solution.',
        '[{"id": "A", "text": "BaCl2(aq) + Na2SO4(aq) \u2192 BaSO4(s) + 2NaCl(aq)", "is_correct": true}, {"id": "B", "text": "BaCl2(s) + Na2SO4(aq) \u2192 BaSO4(aq) + NaCl(aq)", "is_correct": false}, {"id": "C", "text": "BaCl(aq) + NaSO4(aq) \u2192 BaSO4(s) + NaCl(aq)", "is_correct": false}, {"id": "D", "text": "BaCl2(aq) + 2Na2SO4(aq) \u2192 Ba(SO4)2(s) + 4NaCl(aq)", "is_correct": false}]'::jsonb,
        'Step 1: Reactants: BaCl2(aq) and Na2SO4(aq).
Step 2: Products: White precipitate of BaSO4(s) and dissolved NaCl(aq).
Step 3: Balance Na and Cl: BaCl2(aq) + Na2SO4(aq) → BaSO4(s)↓ + 2NaCl(aq).',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '50 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000006',
        'science',
        'science_ch_1_chemical_reactions',
        'Write a balanced equation with state symbols: Sodium hydroxide solution in water reacts with hydrochloric acid solution in water to produce sodium chloride solution and water.',
        '[{"id": "A", "text": "NaOH(aq) + HCl(aq) \u2192 NaCl(aq) + H2O(l)", "is_correct": true}, {"id": "B", "text": "2NaOH(aq) + 2HCl(aq) \u2192 2NaCl(s) + H2O(l)", "is_correct": false}, {"id": "C", "text": "NaOH(s) + HCl(g) \u2192 NaCl(aq) + H2O(g)", "is_correct": false}, {"id": "D", "text": "Na(OH)2 + 2HCl \u2192 NaCl2 + 2H2O", "is_correct": false}]'::jsonb,
        'Step 1: Identification: Acid-base neutralization reaction.
Step 2: Equation: NaOH(aq) + HCl(aq) → NaCl(aq) + H2O(l).
Step 3: Atom inventory: Na=1, O=1, H=2, Cl=1 on both sides. Already balanced.',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '60 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000007',
        'science',
        'science_ch_1_chemical_reactions',
        'A solution of substance ''X'' is used for whitewashing. (i) Name substance ''X'' and write its formula. (ii) Write the reaction of ''X'' with water.',
        '[{"id": "A", "text": "X is Quicklime (Calcium oxide, CaO); Reaction: CaO(s) + H2O(l) \u2192 Ca(OH)2(aq)", "is_correct": true}, {"id": "B", "text": "X is Limestone (Calcium carbonate, CaCO3); Reaction: CaCO3 + H2O \u2192 Ca(OH)2 + CO2", "is_correct": false}, {"id": "C", "text": "X is Slaked lime (Calcium hydroxide, Ca(OH)2); Reaction: Ca(OH)2 + H2O \u2192 CaO + 2H2O", "is_correct": false}, {"id": "D", "text": "X is Plaster of Paris (CaSO4\u00b71/2H2O); Reaction: CaSO4 + H2O \u2192 CaSO4\u00b72H2O", "is_correct": false}]'::jsonb,
        'Step 1: The substance ''X'' used for whitewashing is Quicklime (chemical name: Calcium oxide).
Step 2: Chemical formula: CaO.
Step 3: When water is added to quicklime, it reacts vigorously in an exothermic combination reaction to produce slaked lime:
CaO(s) + H2O(l) → Ca(OH)2(aq) + Heat.',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '70 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000008',
        'science',
        'science_ch_1_chemical_reactions',
        'Why is the volume of gas collected in one test tube during the electrolysis of water double the volume collected in the other? Name this gas.',
        '[{"id": "A", "text": "Water (H2O) contains 2 parts of hydrogen to 1 part of oxygen by volume; the double-volume gas is Hydrogen (collected at cathode)", "is_correct": true}, {"id": "B", "text": "Oxygen is denser than hydrogen; the double-volume gas is Oxygen (collected at anode)", "is_correct": false}, {"id": "C", "text": "Electrons carry more charge at the anode; the gas is Hydrogen", "is_correct": false}, {"id": "D", "text": "Hydrogen dissolves in water; the gas is Oxygen", "is_correct": false}]'::jsonb,
        'Step 1: Chemical formula of water is H2O, meaning two atoms of hydrogen combine with one atom of oxygen.
Step 2: Reaction: 2H2O(l) --[Electricity]--> 2H2(g) [Cathode] + O2(g) [Anode].
Step 3: Two moles of H2 gas are produced for every one mole of O2 gas.
Step 4: According to Avogadro''s Law, molar ratio equals volume ratio. Therefore, the volume of Hydrogen gas collected at the cathode is double that of Oxygen at the anode.',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '80 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000009',
        'science',
        'science_ch_1_chemical_reactions',
        'Why does the blue colour of copper sulphate solution change when an iron nail is dipped into it?',
        '[{"id": "A", "text": "Iron is more reactive than copper; it displaces copper forming pale green ferrous sulphate (FeSO4)", "is_correct": true}, {"id": "B", "text": "Copper displaces iron from solution, evaporating the blue pigment", "is_correct": false}, {"id": "C", "text": "Iron reacts with water to form basic iron hydroxide precipitate", "is_correct": false}, {"id": "D", "text": "Sulphate ions decompose into sulphur dioxide gas", "is_correct": false}]'::jsonb,
        'Step 1: According to the reactivity series, iron (Fe) is more reactive than copper (Cu).
Step 2: Single displacement reaction: Fe(s) + CuSO4(aq) [Blue] → FeSO4(aq) [Light Green] + Cu(s) [Reddish-brown].
Step 3: Cu2+ ions responsible for the blue color are displaced and deposited as copper metal on the iron nail, while Fe2+ ions dissolve into solution giving it a light green color.',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '90 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000010',
        'science',
        'science_ch_1_chemical_reactions',
        'Give an example of a double displacement reaction other than the reaction between sodium sulphate and barium chloride.',
        '[{"id": "A", "text": "Lead nitrate reacts with potassium iodide: Pb(NO3)2(aq) + 2KI(aq) \u2192 PbI2(s)\u2193 + 2KNO3(aq)", "is_correct": true}, {"id": "B", "text": "Zinc reacts with sulphuric acid: Zn + H2SO4 \u2192 ZnSO4 + H2", "is_correct": false}, {"id": "C", "text": "Calcium oxide reacts with water: CaO + H2O \u2192 Ca(OH)2", "is_correct": false}, {"id": "D", "text": "Methane burns in oxygen: CH4 + 2O2 \u2192 CO2 + 2H2O", "is_correct": false}]'::jsonb,
        'Step 1: In a double displacement reaction, there is an exchange of ions between the two reactants.
Step 2: Example: Reaction between Lead(II) nitrate and Potassium iodide.
Step 3: Pb(NO3)2(aq) + 2KI(aq) → PbI2(s)↓ [Bright yellow precipitate] + 2KNO3(aq).
Step 4: Pb2+ exchanges with K+ to form insoluble lead iodide.',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '100 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000011',
        'science',
        'science_ch_1_chemical_reactions',
        'Identify the substances that are oxidised and reduced in: (i) 4Na(s) + O2(g) → 2Na2O(s) and (ii) CuO(s) + H2(g) → Cu(s) + H2O(l).',
        '[{"id": "A", "text": "(i) Na is oxidised, O2 is reduced; (ii) H2 is oxidised, CuO is reduced", "is_correct": true}, {"id": "B", "text": "(i) O2 is oxidised, Na is reduced; (ii) Cu is oxidised, H2O is reduced", "is_correct": false}, {"id": "C", "text": "(i) Na is oxidised, Na2O is reduced; (ii) CuO is oxidised, H2 is reduced", "is_correct": false}, {"id": "D", "text": "Both reactions are displacement reactions without redox", "is_correct": false}]'::jsonb,
        'Reaction (i): 4Na + O2 → 2Na2O
- Sodium (Na) gains oxygen to become Na2O, so Na is oxidised.
- Oxygen (O2) gains electrons from sodium, so O2 is reduced.

Reaction (ii): CuO + H2 → Cu + H2O
- Copper(II) oxide (CuO) loses oxygen to become elemental Cu, so CuO is reduced.
- Hydrogen (H2) gains oxygen to form H2O, so H2 is oxidised.',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '110 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000012',
        'science',
        'science_ch_1_chemical_reactions',
        'Which of the statements about the reaction: 2PbO(s) + C(s) → 2Pb(s) + CO2(g) are incorrect?
(a) Lead is getting reduced.
(b) Carbon dioxide is getting oxidised.
(c) Carbon is getting oxidised.
(d) Lead oxide is getting reduced.',
        '[{"id": "A", "text": "(a) and (b)", "is_correct": true}, {"id": "B", "text": "(a) and (c)", "is_correct": false}, {"id": "C", "text": "(a), (b) and (c)", "is_correct": false}, {"id": "D", "text": "All are incorrect", "is_correct": false}]'::jsonb,
        'Step 1: Observe reactants: PbO and C.
Step 2: PbO loses oxygen to form Pb => Lead oxide (PbO) is reduced, NOT lead.
Step 3: Carbon (C) gains oxygen to form CO2 => Carbon is oxidised, NOT carbon dioxide.
Step 4: Therefore, statements (a) and (b) are incorrect. Correct answer is (A).',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '120 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000013',
        'science',
        'science_ch_1_chemical_reactions',
        'Fe2O3 + 2Al → Al2O3 + 2Fe. The above reaction is an example of a:',
        '[{"id": "A", "text": "combination reaction", "is_correct": false}, {"id": "B", "text": "double displacement reaction", "is_correct": false}, {"id": "C", "text": "decomposition reaction", "is_correct": false}, {"id": "D", "text": "displacement reaction", "is_correct": true}]'::jsonb,
        'Step 1: Aluminium (Al) is more reactive than iron (Fe).
Step 2: Al displaces iron from ferric oxide (Fe2O3) to form aluminium oxide (Al2O3) and molten iron.
Step 3: Since a more reactive element displaces a less reactive element from its compound, this is a displacement reaction (specifically the thermite reaction).',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '130 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000014',
        'science',
        'science_ch_1_chemical_reactions',
        'What happens when dilute hydrochloric acid is added to iron filings?',
        '[{"id": "A", "text": "Hydrogen gas and iron(II) chloride are produced", "is_correct": true}, {"id": "B", "text": "Chlorine gas and iron hydroxide are produced", "is_correct": false}, {"id": "C", "text": "No reaction takes place", "is_correct": false}, {"id": "D", "text": "Iron salt and water are produced", "is_correct": false}]'::jsonb,
        'Step 1: Iron (Fe) is more reactive than hydrogen and displaces it from dilute acids.
Step 2: Reaction: Fe(s) + 2HCl(aq) → FeCl2(aq) + H2(g)↑.
Step 3: Hence, hydrogen gas and iron(II) chloride are produced.',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '140 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000015',
        'science',
        'science_ch_1_chemical_reactions',
        'What is a balanced chemical equation? Why should chemical equations be balanced?',
        '[{"id": "A", "text": "An equation where the number of atoms of each element is equal on both reactant and product sides; required by the Law of Conservation of Mass", "is_correct": true}, {"id": "B", "text": "An equation with equal number of compounds on both sides", "is_correct": false}, {"id": "C", "text": "An equation where reactants are in gaseous state", "is_correct": false}, {"id": "D", "text": "An equation showing only exothermic heat release", "is_correct": false}]'::jsonb,
        'Step 1: Definition: A chemical equation in which the total number of atoms of each element on the reactant side is equal to the total number of atoms on the product side is called a balanced chemical equation.
Step 2: Reason: According to the Law of Conservation of Mass, mass can neither be created nor destroyed in a chemical reaction.
Step 3: Therefore, the total mass of the elements present in the products must equal the total mass of elements present in the reactants.',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '150 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000016',
        'science',
        'science_ch_1_chemical_reactions',
        'Translate and balance: Hydrogen gas combines with nitrogen to form ammonia.',
        '[{"id": "A", "text": "3H2(g) + N2(g) \u2192 2NH3(g)", "is_correct": true}, {"id": "B", "text": "H2 + N2 \u2192 NH3", "is_correct": false}, {"id": "C", "text": "H3 + N \u2192 NH3", "is_correct": false}, {"id": "D", "text": "2H2 + N2 \u2192 2NH2", "is_correct": false}]'::jsonb,
        'Step 1: Skeletal equation: N2 + H2 → NH3
Step 2: Balance N: 2 nitrogen atoms on LHS require 2NH3 on RHS: N2 + H2 → 2NH3
Step 3: Balance H: 2NH3 contains 2 x 3 = 6 hydrogen atoms. Place coefficient 3 before H2: 3H2
Step 4: Final balanced equation: N2(g) + 3H2(g) → 2NH3(g).',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '160 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000017',
        'science',
        'science_ch_1_chemical_reactions',
        'Translate and balance: Hydrogen sulphide gas burns in air to give water and sulphur dioxide.',
        '[{"id": "A", "text": "2H2S(g) + 3O2(g) \u2192 2H2O(l) + 2SO2(g)", "is_correct": true}, {"id": "B", "text": "H2S + O2 \u2192 H2O + SO2", "is_correct": false}, {"id": "C", "text": "H2S + 2O2 \u2192 H2O + SO3", "is_correct": false}, {"id": "D", "text": "2H2S + 2O2 \u2192 2H2O + S2O", "is_correct": false}]'::jsonb,
        'Step 1: Skeletal equation: H2S + O2 → H2O + SO2
Step 2: Total O on RHS: 1 (in H2O) + 2 (in SO2) = 3 (odd number).
Step 3: Multiply H2O by 2: 2H2S + O2 → 2H2O + SO2 => now 4 H on RHS, so place 2 before H2S on LHS: 2H2S.
Step 4: Balance S: 2H2S gives 2S, so place 2 before SO2: 2SO2.
Step 5: Count oxygen atoms on RHS: 2 (in 2H2O) + 4 (in 2SO2) = 6 O atoms. Place 3 before O2: 3O2.
Step 6: Balanced: 2H2S(g) + 3O2(g) → 2H2O(l) + 2SO2(g).',
        'hard',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '170 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000018',
        'science',
        'science_ch_1_chemical_reactions',
        'Balance the chemical equation: HNO3 + Ca(OH)2 → Ca(NO3)2 + H2O',
        '[{"id": "A", "text": "2HNO3 + Ca(OH)2 \u2192 Ca(NO3)2 + 2H2O", "is_correct": true}, {"id": "B", "text": "HNO3 + Ca(OH)2 \u2192 Ca(NO3)2 + H2O", "is_correct": false}, {"id": "C", "text": "2HNO3 + 2Ca(OH)2 \u2192 2Ca(NO3)2 + 3H2O", "is_correct": false}, {"id": "D", "text": "HNO3 + 2Ca(OH)2 \u2192 Ca(NO3)2 + 2H2O", "is_correct": false}]'::jsonb,
        'Step 1: Observe polyatomic nitrate ion (NO3-): 2 on RHS in Ca(NO3)2, so multiply HNO3 by 2.
Step 2: Now on LHS: 2 H (from 2HNO3) + 2 H (from Ca(OH)2) = 4 H atoms.
Step 3: Place coefficient 2 before H2O on RHS to get 4 H atoms.
Step 4: Check Ca and O: Ca=1 on both sides; O=2x3 + 2 = 8 on LHS, 6 + 2 = 8 on RHS.
Step 5: Balanced equation: 2HNO3 + Ca(OH)2 → Ca(NO3)2 + 2H2O.',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '180 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000019',
        'science',
        'science_ch_1_chemical_reactions',
        'Write the balanced chemical equation for: Calcium hydroxide + Carbon dioxide → Calcium carbonate + Water',
        '[{"id": "A", "text": "Ca(OH)2 + CO2 \u2192 CaCO3 + H2O", "is_correct": true}, {"id": "B", "text": "Ca(OH)2 + 2CO2 \u2192 Ca(HCO3)2", "is_correct": false}, {"id": "C", "text": "2Ca(OH)2 + CO2 \u2192 2CaCO3 + H2O", "is_correct": false}, {"id": "D", "text": "CaO + CO2 \u2192 CaCO3", "is_correct": false}]'::jsonb,
        'Step 1: Formula of reactants: Ca(OH)2 and CO2.
Step 2: Formula of products: CaCO3 and H2O.
Step 3: Count atoms on LHS: Ca=1, O=2+2=4, H=2, C=1.
Step 4: Count atoms on RHS: Ca=1, C=1, O=3+1=4, H=2.
Step 5: All atoms match: Ca(OH)2(aq) + CO2(g) → CaCO3(s)↓ + H2O(l).',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '190 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000020',
        'science',
        'science_ch_1_chemical_reactions',
        'Write the balanced chemical equation and identify the reaction type: Potassium bromide(aq) + Barium iodide(aq) → Potassium iodide(aq) + Barium bromide(s)',
        '[{"id": "A", "text": "2KBr(aq) + BaI2(aq) \u2192 2KI(aq) + BaBr2(s); Double displacement and precipitation", "is_correct": true}, {"id": "B", "text": "KBr + BaI2 \u2192 KI + BaBr2; Single displacement", "is_correct": false}, {"id": "C", "text": "2KBr + BaI2 \u2192 2KI + BaBr2; Decomposition reaction", "is_correct": false}, {"id": "D", "text": "KBr + BaI \u2192 KI + BaBr; Neutralization reaction", "is_correct": false}]'::jsonb,
        'Step 1: Unbalanced: KBr(aq) + BaI2(aq) → KI(aq) + BaBr2(s)
Step 2: 2 iodide ions on LHS require 2KI on RHS; 2 bromide ions on RHS require 2KBr on LHS.
Step 3: Balanced equation: 2KBr(aq) + BaI2(aq) → 2KI(aq) + BaBr2(s)↓.
Step 4: Reaction type: Double displacement reaction accompanied by precipitation of BaBr2.',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '200 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000021',
        'science',
        'science_ch_1_chemical_reactions',
        'What does one mean by exothermic and endothermic reactions? Give examples.',
        '[{"id": "A", "text": "Exothermic reactions release heat (e.g. burning of natural gas); Endothermic reactions absorb heat (e.g. decomposition of CaCO3)", "is_correct": true}, {"id": "B", "text": "Exothermic absorbs electricity; Endothermic releases light", "is_correct": false}, {"id": "C", "text": "Exothermic reactions occur without catalysts; Endothermic require oxygen", "is_correct": false}, {"id": "D", "text": "Exothermic produces precipitates; Endothermic produces gases", "is_correct": false}]'::jsonb,
        'Step 1: Exothermic Reactions: Reactions in which heat energy is released along with the formation of products.
Example: CH4(g) + 2O2(g) → CO2(g) + 2H2O(g) + Heat energy.
Step 2: Endothermic Reactions: Reactions in which energy is absorbed from the surroundings in the form of heat, light, or electricity.
Example: CaCO3(s) --[Heat]--> CaO(s) + CO2(g).',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '210 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000022',
        'science',
        'science_ch_1_chemical_reactions',
        'Why is respiration considered an exothermic reaction? Explain.',
        '[{"id": "A", "text": "Glucose is oxidised by oxygen inside cells to form CO2 and H2O, releasing large amounts of metabolic energy (ATP)", "is_correct": true}, {"id": "B", "text": "Lungs absorb external thermal heat during inhalation", "is_correct": false}, {"id": "C", "text": "Blood circulation produces friction heat", "is_correct": false}, {"id": "D", "text": "Carbon dioxide dissolves in water endothermically", "is_correct": false}]'::jsonb,
        'Step 1: During digestion, food containing carbohydrates is broken down into simple glucose.
Step 2: Glucose (C6H12O6) combines with oxygen in the cells of our body and breaks down:
C6H12O6(aq) + 6O2(aq) → 6CO2(aq) + 6H2O(l) + Energy.
Step 3: Since energy is released in this process to fuel life processes, respiration is classified as an exothermic reaction.',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '220 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000023',
        'science',
        'science_ch_1_chemical_reactions',
        'Why are decomposition reactions called the opposite of combination reactions? Write equations.',
        '[{"id": "A", "text": "Combination joins two or more reactants into one product; decomposition splits a single reactant into two or more products", "is_correct": true}, {"id": "B", "text": "Combination reactions require heat while decomposition always releases heat", "is_correct": false}, {"id": "C", "text": "Combination only involves gases while decomposition involves solids", "is_correct": false}, {"id": "D", "text": "Decomposition reactions are not chemical changes", "is_correct": false}]'::jsonb,
        'Step 1: In a combination reaction, two or more substances combine to form a single new substance:
2H2(g) + O2(g) → 2H2O(l).
Step 2: In a decomposition reaction, a single compound breaks down under external energy into two or more simpler substances:
2H2O(l) --[Electricity]--> 2H2(g) + O2(g).
Step 3: Because the process mechanisms are exact reversals of each other, decomposition reactions are called the opposite of combination reactions.',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '230 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000024',
        'science',
        'science_ch_1_chemical_reactions',
        'Write equations for decomposition reactions where energy is supplied as heat, light, and electricity respectively.',
        '[{"id": "A", "text": "Heat: CaCO3 \u2192 CaO + CO2; Light: 2AgCl \u2192 2Ag + Cl2; Electricity: 2H2O \u2192 2H2 + O2", "is_correct": true}, {"id": "B", "text": "Heat: 2H2 + O2 \u2192 2H2O; Light: CH4 + 2O2 \u2192 CO2 + 2H2O; Electricity: Zn + HCl \u2192 ZnCl2 + H2", "is_correct": false}, {"id": "C", "text": "Heat: 2Fe + 3Cl2 \u2192 2FeCl3; Light: Cu + O2 \u2192 2CuO; Electricity: Na + Cl \u2192 NaCl", "is_correct": false}, {"id": "D", "text": "All decomposition reactions only use thermal heat", "is_correct": false}]'::jsonb,
        '1. Thermal Decomposition (Heat):
CaCO3(s) --[Heat]--> CaO(s) + CO2(g)

2. Photolytic Decomposition (Light):
2AgCl(s) --[Sunlight]--> 2Ag(s) [Grey] + Cl2(g)

3. Electrolytic Decomposition (Electricity):
2H2O(l) --[Electric Current]--> 2H2(g) + O2(g).',
        'hots',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '240 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000025',
        'science',
        'science_ch_1_chemical_reactions',
        'What is the difference between displacement and double displacement reactions? Write equations.',
        '[{"id": "A", "text": "Displacement involves a more reactive element displacing a less reactive one; Double displacement involves mutual exchange of ions between two salts", "is_correct": true}, {"id": "B", "text": "Displacement forms two precipitates; double displacement forms none", "is_correct": false}, {"id": "C", "text": "Displacement requires acid; double displacement requires alkali", "is_correct": false}, {"id": "D", "text": "There is no difference in ion exchange", "is_correct": false}]'::jsonb,
        'Step 1: Displacement: A more reactive element takes the place of a less reactive element in a compound.
Example: Zn(s) + CuSO4(aq) → ZnSO4(aq) + Cu(s).

Step 2: Double Displacement: Two compounds react by mutual exchange of their positive and negative ions to form two new compounds.
Example: Na2SO4(aq) + BaCl2(aq) → BaSO4(s)↓ + 2NaCl(aq).',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '250 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000026',
        'science',
        'science_ch_1_chemical_reactions',
        'In the refining of silver, recovery of silver from silver nitrate solution involved displacement by copper metal. Write the reaction.',
        '[{"id": "A", "text": "Cu(s) + 2AgNO3(aq) \u2192 Cu(NO3)2(aq) + 2Ag(s)", "is_correct": true}, {"id": "B", "text": "Cu + AgNO3 \u2192 CuNO3 + Ag", "is_correct": false}, {"id": "C", "text": "2Cu + AgNO3 \u2192 Cu2NO3 + Ag", "is_correct": false}, {"id": "D", "text": "Cu + Ag2NO3 \u2192 Cu(NO3)2 + 2Ag", "is_correct": false}]'::jsonb,
        'Step 1: Copper (Cu) is higher than silver (Ag) in the metal activity series.
Step 2: When copper is added to colorless silver nitrate solution, it displaces silver ions.
Step 3: Balanced equation: Cu(s) + 2AgNO3(aq) → Cu(NO3)2(aq) [Blue solution] + 2Ag(s) [White shining silver deposit].',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '260 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000027',
        'science',
        'science_ch_1_chemical_reactions',
        'What do you mean by a precipitation reaction? Explain with an example.',
        '[{"id": "A", "text": "Any chemical reaction that produces an insoluble solid precipitate that separates out of the solution", "is_correct": true}, {"id": "B", "text": "A reaction where gas condenses into liquid raindrops", "is_correct": false}, {"id": "C", "text": "A reaction where all reactants completely evaporate", "is_correct": false}, {"id": "D", "text": "A combination reaction releasing heat only", "is_correct": false}]'::jsonb,
        'Step 1: Definition: A reaction in which two aqueous solutions react to form an insoluble solid substance (called a precipitate) which settles down is known as a precipitation reaction.
Step 2: Example: Na2SO4(aq) + BaCl2(aq) → BaSO4(s)↓ + 2NaCl(aq).
Step 3: White insoluble barium sulphate (BaSO4) precipitates immediately upon mixing.',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '270 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000028',
        'science',
        'science_ch_1_chemical_reactions',
        'Explain Oxidation and Reduction in terms of gain or loss of oxygen with examples.',
        '[{"id": "A", "text": "Oxidation: Gain of oxygen (2Cu + O2 \u2192 2CuO); Reduction: Loss of oxygen (CuO + H2 \u2192 Cu + H2O)", "is_correct": true}, {"id": "B", "text": "Oxidation: Loss of oxygen; Reduction: Gain of oxygen", "is_correct": false}, {"id": "C", "text": "Both involve gain of oxygen only", "is_correct": false}, {"id": "D", "text": "Oxidation and reduction do not involve oxygen", "is_correct": false}]'::jsonb,
        '1. Oxidation (Gain of Oxygen):
Example 1: 2Cu + O2 --[Heat]--> 2CuO (Copper gains oxygen to form black copper oxide).
Example 2: C + O2 → CO2 (Carbon gains oxygen).

2. Reduction (Loss of Oxygen):
Example 1: CuO + H2 --[Heat]--> Cu + H2O (CuO loses oxygen to form Cu).
Example 2: ZnO + C → Zn + CO (ZnO loses oxygen to form Zn).',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '280 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000029',
        'science',
        'science_ch_1_chemical_reactions',
        'A shiny brown coloured element ''X'' on heating in air becomes black in colour. Name element ''X'' and the black compound formed.',
        '[{"id": "A", "text": "Element ''X'' is Copper (Cu); Black compound is Copper(II) oxide (CuO)", "is_correct": true}, {"id": "B", "text": "Element ''X'' is Iron (Fe); Black compound is Fe3O4", "is_correct": false}, {"id": "C", "text": "Element ''X'' is Carbon (C); Black compound is Coal", "is_correct": false}, {"id": "D", "text": "Element ''X'' is Lead (Pb); Black compound is PbO2", "is_correct": false}]'::jsonb,
        'Step 1: The shiny brown-coloured element is Copper (Cu).
Step 2: When copper powder is heated in a china dish in the presence of oxygen, it undergoes oxidation.
Step 3: 2Cu(s) [Brown] + O2(g) --[Heat]--> 2CuO(s) [Black coating].
Step 4: The black compound formed is Copper(II) oxide.',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '290 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000030',
        'science',
        'science_ch_1_chemical_reactions',
        'Why do we apply paint on iron articles?',
        '[{"id": "A", "text": "Paint creates a protective barrier preventing iron from coming in contact with moisture and oxygen, preventing corrosion (rusting)", "is_correct": true}, {"id": "B", "text": "To increase the tensile strength and hardness of iron", "is_correct": false}, {"id": "C", "text": "To prevent iron from conducting electrical currents", "is_correct": false}, {"id": "D", "text": "To dissolve surface iron atoms into pigment", "is_correct": false}]'::jsonb,
        'Step 1: Rusting of iron requires simultaneous exposure to both moist air (water vapor) and oxygen: 4Fe + 3O2 + 2xH2O → 2Fe2O3·xH2O.
Step 2: Applying a coat of paint creates an impermeable protective barrier on the metal surface.
Step 3: This isolates the underlying iron from contact with air and moisture, thereby completely preventing rust formation.',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '300 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000031',
        'science',
        'science_ch_1_chemical_reactions',
        'Oil and fat containing food items are flushed with nitrogen. Why?',
        '[{"id": "A", "text": "Nitrogen is an unreactive inert gas that displaces oxygen, preventing oxidation of oils and fats (rancidity)", "is_correct": true}, {"id": "B", "text": "Nitrogen adds nutritional protein value to packaged food", "is_correct": false}, {"id": "C", "text": "Nitrogen cools the food down to freezing temperatures", "is_correct": false}, {"id": "D", "text": "Nitrogen keeps the packaging pouch inflated for appearance only", "is_correct": false}]'::jsonb,
        'Step 1: Oils and fats in food react with atmospheric oxygen over time in a process called oxidation.
Step 2: Oxidation causes oils and fats to become rancid, resulting in an unpleasant taste and foul odor.
Step 3: Nitrogen gas is an inert, non-reactive gas. Flushing snack packets (like potato chips) with nitrogen removes oxygen, preventing aerial oxidation and extending shelf life.',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '310 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000032',
        'science',
        'science_ch_1_chemical_reactions',
        'Explain Corrosion and Rancidity with one example of each.',
        '[{"id": "A", "text": "Corrosion is slow deterioration of metals by moist air/acids (e.g. rusting of iron); Rancidity is oxidation of fats/oils causing foul odor/taste (e.g. stale butter)", "is_correct": true}, {"id": "B", "text": "Corrosion is burning of metals; Rancidity is melting of cheese", "is_correct": false}, {"id": "C", "text": "Both processes only happen in cold storage", "is_correct": false}, {"id": "D", "text": "Corrosion occurs on food items; Rancidity occurs on copper", "is_correct": false}]'::jsonb,
        '1. Corrosion: The process in which a metal is slowly attacked and degraded by substances around it such as moisture, air, and acids.
- Example: Rusting of iron (formation of reddish-brown Fe2O3·xH2O) or black tarnish on silver (Ag2S).

2. Rancidity: The condition produced by aerial oxidation of fats and oils in food marked by unpleasant odor and rancid taste.
- Example: Butter or fried potato chips left exposed to air for several days developing an acidic bad smell.',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '320 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000033',
        'science',
        'science_ch_1_chemical_reactions',
        'In Activity 1.1, what observation is recorded when a cleaned magnesium ribbon is held with tongs and burnt over a spirit lamp?',
        '[{"id": "A", "text": "Burns with a dazzling white flame and changes into a white powder of magnesium oxide (MgO)", "is_correct": true}, {"id": "B", "text": "Burns with a pop sound leaving a grey residue", "is_correct": false}, {"id": "C", "text": "Melts into a liquid with blue flame", "is_correct": false}, {"id": "D", "text": "No reaction occurs without catalyst", "is_correct": false}]'::jsonb,
        'Step 1: Magnesium reacts energetically with atmospheric oxygen.
Step 2: Observation 1: Burns vigorously with a dazzling white brilliant flame.
Step 3: Observation 2: Leaves behind a white powdery residue of Magnesium Oxide (MgO).
Step 4: Equation: 2Mg(s) + O2(g) → 2MgO(s).',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '330 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000034',
        'science',
        'science_ch_1_chemical_reactions',
        'In Activity 1.2, lead nitrate solution is mixed with potassium iodide solution in a test tube. What precipitate forms and what is its color?',
        '[{"id": "A", "text": "Bright yellow precipitate of Lead iodide (PbI2)", "is_correct": true}, {"id": "B", "text": "White precipitate of Potassium nitrate (KNO3)", "is_correct": false}, {"id": "C", "text": "Dark brown precipitate of Lead oxide (PbO)", "is_correct": false}, {"id": "D", "text": "Blue precipitate of Copper iodide", "is_correct": false}]'::jsonb,
        'Step 1: Reactants: Colorless Pb(NO3)2(aq) and colorless KI(aq).
Step 2: Double displacement takes place.
Step 3: Pb(NO3)2(aq) + 2KI(aq) → PbI2(s)↓ + 2KNO3(aq).
Step 4: An immediate bright yellow precipitate of Lead(II) iodide (PbI2) is formed.',
        'easy',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '340 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '11000000-0000-0000-0000-000000000035',
        'science',
        'science_ch_1_chemical_reactions',
        'In Activity 1.3, dilute sulphuric acid is added to zinc granules in a conical flask. Which observations confirm a chemical reaction has occurred?',
        '[{"id": "A", "text": "Brisk effervescence with evolution of hydrogen gas and the flask becomes hot to touch (exothermic)", "is_correct": true}, {"id": "B", "text": "Flask cools down drastically with precipitate formation", "is_correct": false}, {"id": "C", "text": "Brown fumes of nitrogen dioxide evolve", "is_correct": false}, {"id": "D", "text": "Zinc granules dissolve with no gas evolution", "is_correct": false}]'::jsonb,
        'Step 1: Reaction: Zn(s) + H2SO4(aq) → ZnSO4(aq) + H2(g)↑ + Heat.
Step 2: Observation 1: Bubbles of hydrogen gas evolve rapidly around the zinc granules.
Step 3: Observation 2: Touching the bottom of the flask reveals an increase in temperature, confirming an exothermic reaction.',
        'medium',
        'pending_review',
        '00000000-0000-0000-0000-000000000002',
        NULL,
        NOW() - INTERVAL '350 minutes'
    ) ON CONFLICT (id) DO UPDATE SET 
        question_text = EXCLUDED.question_text,
        options = EXCLUDED.options,
        step_by_step_solution = EXCLUDED.step_by_step_solution,
        status = EXCLUDED.status;

END $$;