import json
import os

# Complete, strict-source-isolated dataset for NCERT Class 10 Science Chapter 1: Chemical Reactions and Equations
questions = [
    # -------------------------------------------------------------
    # SECTION 1: IN-TEXT "QUESTIONS" (Page 6)
    # -------------------------------------------------------------
    {
        "id": "sci_ch1_p06_q01",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 6)",
        "question_number": "1",
        "text": "Why should a magnesium ribbon be cleaned before burning in air?",
        "options": [
            {
                "id": "A",
                "text": "To remove the protective layer of basic magnesium oxide and carbonate from its surface",
                "is_correct": True,
                "rationale": "Magnesium reacts slowly with moist atmospheric oxygen forming a stable, protective coating of basic magnesium oxide/carbonate which hinders ignition until removed by sandpaper."
            },
            {
                "id": "B",
                "text": "To lower the minimum ignition temperature required for starting the combustion reaction",
                "is_correct": False,
                "rationale": "Cleaning does not change the intrinsic ignition temperature of pure magnesium metal."
            },
            {
                "id": "C",
                "text": "To eliminate surface moisture and grease accumulated during storage in laboratory conditions",
                "is_correct": False,
                "rationale": "While moisture may be present, the chemical impediment to burning is the oxide/carbonate barrier."
            },
            {
                "id": "D",
                "text": "To roughen the metal surface and increase the exposed surface area for rapid oxidation",
                "is_correct": False,
                "rationale": "The goal is removing the chemical passivation layer, not physical surface roughening."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_p06_q02_i",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 6)",
        "question_number": "2(i)",
        "text": "Write the balanced chemical equation for the reaction:\n$$\\text{Hydrogen} + \\text{Chlorine} \\rightarrow \\text{Hydrogen chloride}$$",
        "options": [
            {
                "id": "A",
                "text": "$\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{HCl}(g)$",
                "is_correct": True,
                "rationale": "Hydrogen and chlorine exist as diatomic molecules ($\\text{H}_2$, $\\text{Cl}_2$), yielding two molecules of hydrogen chloride gas ($\\text{HCl}$)."
            },
            {
                "id": "B",
                "text": "$\\text{H}(g) + \\text{Cl}(g) \\rightarrow \\text{HCl}(g)$",
                "is_correct": False,
                "rationale": "Under standard conditions, hydrogen and chlorine are diatomic gases, not monoatomic atoms."
            },
            {
                "id": "C",
                "text": "$\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow \\text{H}_2\\text{Cl}_2(g)$",
                "is_correct": False,
                "rationale": "$\\text{H}_2\\text{Cl}_2$ is a non-existent chemical formula; hydrogen chloride is $\\text{HCl}$."
            },
            {
                "id": "D",
                "text": "$2\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{H}_2\\text{Cl}(g)$",
                "is_correct": False,
                "rationale": "The formula $\\text{H}_2\\text{Cl}$ is incorrect and atoms are not balanced."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_p06_q02_ii",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 6)",
        "question_number": "2(ii)",
        "text": "Write the balanced chemical equation for the reaction:\n$$\\text{Barium chloride} + \\text{Aluminium sulphate} \\rightarrow \\text{Barium sulphate} + \\text{Aluminium chloride}$$",
        "options": [
            {
                "id": "A",
                "text": "$3\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 3\\text{BaSO}_4(s) + 2\\text{AlCl}_3(aq)$",
                "is_correct": True,
                "rationale": "Three $\\text{Ba}^{2+}$ ions combine with three $\\text{SO}_4^{2-}$ ions forming $3\\text{BaSO}_4$, and two $\\text{Al}^{3+}$ ions combine with six $\\text{Cl}^-$ ions forming $2\\text{AlCl}_3$."
            },
            {
                "id": "B",
                "text": "$\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow \\text{BaSO}_4(s) + \\text{AlCl}_3(aq)$",
                "is_correct": False,
                "rationale": "This equation is unbalanced for $\\text{Ba}$, $\\text{Al}$, $\\text{Cl}$, and $\\text{SO}_4$."
            },
            {
                "id": "C",
                "text": "$3\\text{BaCl}_2(aq) + 2\\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 3\\text{BaSO}_4(s) + 4\\text{AlCl}_3(aq)$",
                "is_correct": False,
                "rationale": "Sulphate and chlorine atoms are unbalanced on reactant and product sides."
            },
            {
                "id": "D",
                "text": "$2\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 2\\text{BaSO}_4(s) + 2\\text{AlCl}_3(aq)$",
                "is_correct": False,
                "rationale": "Barium and sulphate atoms are not balanced."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_p06_q02_iii",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 6)",
        "question_number": "2(iii)",
        "text": "Write the balanced chemical equation for the reaction:\n$$\\text{Sodium} + \\text{Water} \\rightarrow \\text{Sodium hydroxide} + \\text{Hydrogen}$$",
        "options": [
            {
                "id": "A",
                "text": "$2\\text{Na}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{NaOH}(aq) + \\text{H}_2(g)$",
                "is_correct": True,
                "rationale": "Two sodium atoms react with two water molecules yielding two sodium hydroxide formula units and one diatomic hydrogen molecule."
            },
            {
                "id": "B",
                "text": "$\\text{Na}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{NaOH}(aq) + \\text{H}(g)$",
                "is_correct": False,
                "rationale": "Hydrogen is liberated as diatomic gas $\\text{H}_2(g)$, not atomic $\\text{H}$."
            },
            {
                "id": "C",
                "text": "$2\\text{Na}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{Na}_2\\text{O}(aq) + \\text{H}_2(g)$",
                "is_correct": False,
                "rationale": "In excess water, sodium forms soluble hydroxide $\\text{NaOH}$, not oxide."
            },
            {
                "id": "D",
                "text": "$\\text{Na}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{Na}(\\text{OH})_2(aq) + \\text{H}_2(g)$",
                "is_correct": False,
                "rationale": "Sodium is monovalent ($+1$); $\\text{Na(OH)}_2$ is an invalid chemical formula."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_p06_q03_i",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 6)",
        "question_number": "3(i)",
        "text": "Which equation with state symbols correctly represents: Solutions of barium chloride and sodium sulphate in water react to give insoluble barium sulphate and sodium chloride solution?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{BaCl}_2(aq) + \\text{Na}_2\\text{SO}_4(aq) \\rightarrow \\text{BaSO}_4(s) + 2\\text{NaCl}(aq)$",
                "is_correct": True,
                "rationale": "Barium chloride and sodium sulphate are aqueous reactants ($aq$), producing insoluble solid white precipitate barium sulphate ($s$) and aqueous sodium chloride ($aq$)."
            },
            {
                "id": "B",
                "text": "$\\text{BaCl}_2(s) + \\text{Na}_2\\text{SO}_4(s) \\rightarrow \\text{BaSO}_4(aq) + 2\\text{NaCl}(aq)$",
                "is_correct": False,
                "rationale": "The reactants are aqueous solutions, and barium sulphate is an insoluble precipitate ($s$), not aqueous ($aq$)."
            },
            {
                "id": "C",
                "text": "$\\text{BaCl}_2(aq) + \\text{Na}_2\\text{SO}_4(aq) \\rightarrow \\text{BaSO}_4(aq) + 2\\text{NaCl}(s)$",
                "is_correct": False,
                "rationale": "Sodium chloride remains dissolved ($aq$); barium sulphate forms the solid precipitate ($s$)."
            },
            {
                "id": "D",
                "text": "$2\\text{BaCl}_2(aq) + \\text{Na}_2\\text{SO}_4(aq) \\rightarrow 2\\text{BaSO}_4(s) + \\text{NaCl}(aq)$",
                "is_correct": False,
                "rationale": "The stoichiometry is unbalanced for both barium and chlorine."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_p06_q03_ii",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 6)",
        "question_number": "3(ii)",
        "text": "Which equation with state symbols correctly represents: Sodium hydroxide solution in water reacts with hydrochloric acid solution in water to produce sodium chloride solution and water?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{NaOH}(aq) + \\text{HCl}(aq) \\rightarrow \\text{NaCl}(aq) + \\text{H}_2\\text{O}(l)$",
                "is_correct": True,
                "rationale": "Aqueous $\\text{NaOH}$ neutralises aqueous $\\text{HCl}$ to produce soluble aqueous $\\text{NaCl}$ and liquid water $\\text{H}_2\\text{O}(l)$."
            },
            {
                "id": "B",
                "text": "$\\text{NaOH}(s) + \\text{HCl}(g) \\rightarrow \\text{NaCl}(s) + \\text{H}_2\\text{O}(g)$",
                "is_correct": False,
                "rationale": "The prompt specifies solutions in water ($aq$), not dry solids or gases."
            },
            {
                "id": "C",
                "text": "$\\text{NaOH}(aq) + \\text{HCl}(aq) \\rightarrow \\text{NaCl}(s) + \\text{H}_2\\text{O}(aq)$",
                "is_correct": False,
                "rationale": "$\\text{NaCl}$ remains dissolved in water as aqueous solution; water is liquid ($l$)."
            },
            {
                "id": "D",
                "text": "$2\\text{NaOH}(aq) + \\text{HCl}(aq) \\rightarrow \\text{NaCl}_2(aq) + \\text{H}_2\\text{O}(l)$",
                "is_correct": False,
                "rationale": "$\\text{NaCl}_2$ is a non-existent formula; sodium chloride is $\\text{NaCl}$."
            }
        ],
        "difficulty": "easy"
    },

    # -------------------------------------------------------------
    # SECTION 2: IN-TEXT "QUESTIONS" (Page 10)
    # -------------------------------------------------------------
    {
        "id": "sci_ch1_p10_q01_i",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 10)",
        "question_number": "1(i)",
        "text": "A solution of a substance 'X' is used for white washing. Identify substance 'X' and state its chemical formula.",
        "options": [
            {
                "id": "A",
                "text": "Calcium oxide (quicklime), $\\text{CaO}$",
                "is_correct": True,
                "rationale": "Quicklime ($\\text{CaO}$) is mixed with water to form slaked lime, which is applied for white washing walls."
            },
            {
                "id": "B",
                "text": "Calcium hydroxide (slaked lime), $\\text{Ca(OH)}_2$",
                "is_correct": False,
                "rationale": "$\\text{Ca(OH)}_2$ is the product formed after substance 'X' reacts with water."
            },
            {
                "id": "C",
                "text": "Calcium carbonate (limestone), $\\text{CaCO}_3$",
                "is_correct": False,
                "rationale": "$\\text{CaCO}_3$ is the shiny film formed on the wall days after white washing."
            },
            {
                "id": "D",
                "text": "Calcium sulphate hemihydrate (Plaster of Paris), $\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Plaster of Paris is used for casts and moulds, not standard white washing."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_p10_q01_ii",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 10)",
        "question_number": "1(ii)",
        "text": "Write the balanced chemical equation for the reaction of substance 'X' (calcium oxide) with water.",
        "options": [
            {
                "id": "A",
                "text": "$\\text{CaO}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{Ca(OH)}_2(aq) + \\text{Heat}$",
                "is_correct": True,
                "rationale": "Calcium oxide reacts vigorously with water in a highly exothermic combination reaction to produce slaked lime $\\text{Ca(OH)}_2$."
            },
            {
                "id": "B",
                "text": "$\\text{CaO}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{Ca(OH)}_2(aq) + \\text{H}_2(g)$",
                "is_correct": False,
                "rationale": "Hydrogen gas is not evolved during the hydration of calcium oxide."
            },
            {
                "id": "C",
                "text": "$2\\text{CaO}(s) + \\text{H}_2\\text{O}(l) \\rightarrow 2\\text{CaOH}(aq) + \\text{O}_2(g)$",
                "is_correct": False,
                "rationale": "$\\text{CaOH}$ is an incorrect formula and oxygen gas is not produced."
            },
            {
                "id": "D",
                "text": "$\\text{CaO}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{CaCO}_3(s) + \\text{Heat}$",
                "is_correct": False,
                "rationale": "Calcium carbonate requires reaction with carbon dioxide, not water alone."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_p10_q02",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 10)",
        "question_number": "2",
        "text": "Why is the volume of gas collected in one test tube during the electrolysis of water (Activity 1.7) double that in the other, and which gas is it?",
        "options": [
            {
                "id": "A",
                "text": "Hydrogen gas, because a water molecule contains two hydrogen atoms for every one oxygen atom",
                "is_correct": True,
                "rationale": "Electrolysis decomposes water according to $2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{H}_2(g) + \\text{O}_2(g)$, yielding hydrogen and oxygen in a $2:1$ ratio by volume."
            },
            {
                "id": "B",
                "text": "Oxygen gas, because oxygen has higher density and displaces twice the volume of aqueous electrolyte",
                "is_correct": False,
                "rationale": "Oxygen gas volume is half that of hydrogen, not double."
            },
            {
                "id": "C",
                "text": "Hydrogen gas, because hydrogen molecules have lower molar mass than diatomic oxygen molecules",
                "is_correct": False,
                "rationale": "Gas volume in Avogadro's law depends on molar quantity, not molecular mass."
            },
            {
                "id": "D",
                "text": "Oxygen gas, because oxygen ions carry twice the electric charge during electrolytic discharge",
                "is_correct": False,
                "rationale": "Oxygen collects at the anode in a $1:2$ ratio compared to hydrogen at the cathode."
            }
        ],
        "difficulty": "medium"
    },

    # -------------------------------------------------------------
    # SECTION 3: IN-TEXT "QUESTIONS" (Page 13)
    # -------------------------------------------------------------
    {
        "id": "sci_ch1_p13_q01",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 13)",
        "question_number": "1",
        "text": "Why does the colour of copper sulphate solution change when an iron nail is dipped in it?",
        "options": [
            {
                "id": "A",
                "text": "Iron displaces copper from $\\text{CuSO}_4$ forming light green $\\text{FeSO}_4$ and depositing brown copper",
                "is_correct": True,
                "rationale": "Iron is more reactive than copper; in $\\text{Fe} + \\text{CuSO}_4 \\rightarrow \\text{FeSO}_4 + \\text{Cu}$, blue $\\text{Cu}^{2+}$ ions are replaced by green $\\text{Fe}^{2+}$ ions."
            },
            {
                "id": "B",
                "text": "Copper metal dissolves from the nail, oxidising the sulphate solution to basic copper carbonate",
                "is_correct": False,
                "rationale": "The nail is iron, not copper; iron enters the solution, copper is deposited."
            },
            {
                "id": "C",
                "text": "Iron acts as an inert catalyst causing photochemical degradation of aqueous copper ions",
                "is_correct": False,
                "rationale": "Iron actively undergoes chemical displacement, not inert catalysis."
            },
            {
                "id": "D",
                "text": "Sulphate ions precipitate out of solution onto the iron surface leaving pure water behind",
                "is_correct": False,
                "rationale": "Sulphate ions remain in solution as soluble ferrous sulphate."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_p13_q02",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 13)",
        "question_number": "2",
        "text": "Which of the following is an example of a double displacement reaction other than the reaction between barium chloride and sodium sulphate?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{Pb(NO}_3)_2(aq) + 2\\text{KI}(aq) \\rightarrow \\text{PbI}_2(s) + 2\\text{KNO}_3(aq)$",
                "is_correct": True,
                "rationale": "Lead nitrate and potassium iodide exchange ions to produce yellow precipitate lead iodide and potassium nitrate solution."
            },
            {
                "id": "B",
                "text": "$\\text{Zn}(s) + \\text{CuSO}_4(aq) \\rightarrow \\text{ZnSO}_4(aq) + \\text{Cu}(s)$",
                "is_correct": False,
                "rationale": "This is a single displacement reaction, not double displacement."
            },
            {
                "id": "C",
                "text": "$2\\text{Mg}(s) + \\text{O}_2(g) \\rightarrow 2\\text{MgO}(s)$",
                "is_correct": False,
                "rationale": "This is a combination reaction."
            },
            {
                "id": "D",
                "text": "$2\\text{FeSO}_4(s) \\xrightarrow{\\Delta} \\text{Fe}_2\\text{O}_3(s) + \\text{SO}_2(g) + \\text{SO}_3(g)$",
                "is_correct": False,
                "rationale": "This is a thermal decomposition reaction."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_p13_q03_i",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 13)",
        "question_number": "3(i)",
        "text": "In the reaction $4\\text{Na}(s) + \\text{O}_2(g) \\rightarrow 2\\text{Na}_2\\text{O}(s)$, identify the substance oxidised and the substance reduced:",
        "options": [
            {
                "id": "A",
                "text": "$\\text{Na}$ is oxidised and $\\text{O}_2$ is reduced",
                "is_correct": True,
                "rationale": "Sodium gains oxygen (oxidised from $0$ to $+1$), while oxygen gains electrons (reduced from $0$ to $-2$)."
            },
            {
                "id": "B",
                "text": "$\\text{O}_2$ is oxidised and $\\text{Na}$ is reduced",
                "is_correct": False,
                "rationale": "Oxygen is the oxidising agent and gets reduced."
            },
            {
                "id": "C",
                "text": "$\\text{Na}_2\\text{O}$ is oxidised and $\\text{Na}$ is reduced",
                "is_correct": False,
                "rationale": "$\\text{Na}_2\\text{O}$ is the reaction product, not the reactant undergoing redox."
            },
            {
                "id": "D",
                "text": "Both $\\text{Na}$ and $\\text{O}_2$ are oxidised simultaneously",
                "is_correct": False,
                "rationale": "Oxidation cannot occur without a complementary reduction reaction."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_p13_q03_ii",
        "chapter": "Chemical Reactions and Equations",
        "section": "QUESTIONS (Page 13)",
        "question_number": "3(ii)",
        "text": "In the reaction $\\text{CuO}(s) + \\text{H}_2(g) \\rightarrow \\text{Cu}(s) + \\text{H}_2\\text{O}(l)$, identify the substance oxidised and the substance reduced:",
        "options": [
            {
                "id": "A",
                "text": "$\\text{H}_2$ is oxidised and $\\text{CuO}$ is reduced",
                "is_correct": True,
                "rationale": "Hydrogen gains oxygen to form $\\text{H}_2\\text{O}$ (oxidised); copper oxide loses oxygen to form $\\text{Cu}$ (reduced)."
            },
            {
                "id": "B",
                "text": "$\\text{CuO}$ is oxidised and $\\text{H}_2$ is reduced",
                "is_correct": False,
                "rationale": "$\\text{CuO}$ loses oxygen, which is reduction, not oxidation."
            },
            {
                "id": "C",
                "text": "$\\text{Cu}$ is oxidised and $\\text{H}_2\\text{O}$ is reduced",
                "is_correct": False,
                "rationale": "$\\text{Cu}$ and $\\text{H}_2\\text{O}$ are products, whereas redox reactants are identified on LHS."
            },
            {
                "id": "D",
                "text": "$\\text{H}_2\\text{O}$ is oxidised and $\\text{CuO}$ is reduced",
                "is_correct": False,
                "rationale": "$\\text{H}_2\\text{O}$ is the oxidation product of elemental hydrogen."
            }
        ],
        "difficulty": "easy"
    },

    # -------------------------------------------------------------
    # SECTION 4: END-OF-CHAPTER "EXERCISES" (Pages 14-16)
    # -------------------------------------------------------------
    {
        "id": "sci_ch1_ex01",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "1",
        "text": "Which of the statements about the reaction below are incorrect?\n$$2\\text{PbO}(s) + \\text{C}(s) \\rightarrow 2\\text{Pb}(s) + \\text{CO}_2(g)$$\n(a) Lead is getting reduced.\n(b) Carbon dioxide is getting oxidised.\n(c) Carbon is getting oxidised.\n(d) Lead oxide is getting reduced.",
        "options": [
            {
                "id": "A",
                "text": "(a) and (b)",
                "is_correct": True,
                "rationale": "Lead oxide ($\\text{PbO}$) is reduced to lead, not lead itself. Carbon ($\\text{C}$) is oxidised to carbon dioxide, not carbon dioxide. Thus, statements (a) and (b) are incorrect."
            },
            {
                "id": "B",
                "text": "(a) and (c)",
                "is_correct": False,
                "rationale": "Statement (c) is correct because carbon is indeed getting oxidised."
            },
            {
                "id": "C",
                "text": "(a), (b) and (c)",
                "is_correct": False,
                "rationale": "Statement (c) is a correct chemical statement, so it cannot be in the incorrect list."
            },
            {
                "id": "D",
                "text": "all of the above",
                "is_correct": False,
                "rationale": "Statements (c) and (d) are both factually correct descriptions of the reaction."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex02",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "2",
        "text": "$$\\text{Fe}_2\\text{O}_3 + 2\\text{Al} \\rightarrow \\text{Al}_2\\text{O}_3 + 2\\text{Fe}$$\nThe above reaction is an example of a:",
        "options": [
            {
                "id": "A",
                "text": "displacement reaction",
                "is_correct": True,
                "rationale": "Aluminium is more reactive than iron and displaces iron from ferric oxide to form aluminium oxide and metallic iron."
            },
            {
                "id": "B",
                "text": "double displacement reaction",
                "is_correct": False,
                "rationale": "There is no mutual exchange of ions between two compounds; elemental aluminium displaces iron."
            },
            {
                "id": "C",
                "text": "combination reaction",
                "is_correct": False,
                "rationale": "Two products are formed; combination reactions yield only a single product."
            },
            {
                "id": "D",
                "text": "decomposition reaction",
                "is_correct": False,
                "rationale": "A single reactant does not break down; two reactants interact."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex03",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "3",
        "text": "What happens when dilute hydrochloric acid is added to iron filings? Tick the correct answer.",
        "options": [
            {
                "id": "A",
                "text": "Hydrogen gas and iron(II) chloride are produced",
                "is_correct": True,
                "rationale": "Iron reacts with dilute acid according to $\\text{Fe}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{FeCl}_2(aq) + \\text{H}_2(g)$."
            },
            {
                "id": "B",
                "text": "Chlorine gas and iron(II) hydroxide are produced",
                "is_correct": False,
                "rationale": "Chlorine gas is not released; iron chloride remains in solution."
            },
            {
                "id": "C",
                "text": "No chemical reaction takes place between them",
                "is_correct": False,
                "rationale": "Iron is placed above hydrogen in the activity series and readily displaces hydrogen from acids."
            },
            {
                "id": "D",
                "text": "Iron salt and liquid water are exclusively produced",
                "is_correct": False,
                "rationale": "Neutralisation produces salt and water; reaction of metal with acid produces salt and hydrogen gas."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex04",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "4",
        "text": "What is a balanced chemical equation, and why should chemical equations be balanced?",
        "options": [
            {
                "id": "A",
                "text": "An equation having equal numbers of each elemental atom on both sides, satisfying the Law of Conservation of Mass",
                "is_correct": True,
                "rationale": "Mass can neither be created nor destroyed in a chemical reaction, meaning total reactant mass must equal total product mass."
            },
            {
                "id": "B",
                "text": "An equation where reactants and products exist in the same physical state, maintaining thermodynamic equilibrium",
                "is_correct": False,
                "rationale": "States of matter can differ among reactants and products in balanced equations."
            },
            {
                "id": "C",
                "text": "An equation having equal numbers of moles of molecules on both sides, ensuring volume conservation during reaction",
                "is_correct": False,
                "rationale": "Total number of molecules often changes during reactions; atom counts must balance, not molecule counts."
            },
            {
                "id": "D",
                "text": "An equation where coefficients match reactant valencies, satisfying the Law of Constant Chemical Proportions",
                "is_correct": False,
                "rationale": "Balancing stems from mass conservation, not valency matching."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex05_a",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "5(a)",
        "text": "Translate the statement into a balanced chemical equation:\n'Hydrogen gas combines with nitrogen to form ammonia.'",
        "options": [
            {
                "id": "A",
                "text": "$3\\text{H}_2(g) + \\text{N}_2(g) \\rightarrow 2\\text{NH}_3(g)$",
                "is_correct": True,
                "rationale": "Three molecules of diatomic hydrogen react with one molecule of diatomic nitrogen to form two molecules of ammonia gas."
            },
            {
                "id": "B",
                "text": "$\\text{H}_2(g) + \\text{N}_2(g) \\rightarrow 2\\text{NH}(g)$",
                "is_correct": False,
                "rationale": "The molecular formula of ammonia is $\\text{NH}_3$, not $\\text{NH}$."
            },
            {
                "id": "C",
                "text": "$2\\text{H}_2(g) + \\text{N}_2(g) \\rightarrow \\text{N}_2\\text{H}_4(g)$",
                "is_correct": False,
                "rationale": "$\\text{N}_2\\text{H}_4$ is hydrazine, not ammonia."
            },
            {
                "id": "D",
                "text": "$3\\text{H}_2(g) + 2\\text{N}_2(g) \\rightarrow 2\\text{NH}_3(g) + \\text{N}_2(g)$",
                "is_correct": False,
                "rationale": "This equation includes unreacted nitrogen on the product side and is not in lowest whole-number terms."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex05_b",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "5(b)",
        "text": "Translate the statement into a balanced chemical equation:\n'Hydrogen sulphide gas burns in air to give water and sulphur dioxide.'",
        "options": [
            {
                "id": "A",
                "text": "$2\\text{H}_2\\text{S}(g) + 3\\text{O}_2(g) \\rightarrow 2\\text{H}_2\\text{O}(l) + 2\\text{SO}_2(g)$",
                "is_correct": True,
                "rationale": "Balancing gives $4\\text{ H}$, $2\\text{ S}$, and $6\\text{ O}$ on both sides of the equation."
            },
            {
                "id": "B",
                "text": "$\\text{H}_2\\text{S}(g) + \\text{O}_2(g) \\rightarrow \\text{H}_2\\text{O}(l) + \\text{SO}_2(g)$",
                "is_correct": False,
                "rationale": "Oxygen atoms are not balanced ($2$ on LHS vs $3$ on RHS)."
            },
            {
                "id": "C",
                "text": "$2\\text{H}_2\\text{S}(g) + 2\\text{O}_2(g) \\rightarrow 2\\text{H}_2\\text{O}(l) + 2\\text{S}(s)$",
                "is_correct": False,
                "rationale": "The problem states sulphur dioxide is formed, not solid sulphur."
            },
            {
                "id": "D",
                "text": "$\\text{H}_2\\text{S}(g) + 2\\text{O}_2(g) \\rightarrow \\text{H}_2\\text{SO}_4(aq)$",
                "is_correct": False,
                "rationale": "Combustion in air yields $\\text{SO}_2$ and $\\text{H}_2\\text{O}$, not sulphuric acid."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex05_c",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "5(c)",
        "text": "Translate the statement into a balanced chemical equation:\n'Barium chloride reacts with aluminium sulphate to give aluminium chloride and a precipitate of barium sulphate.'",
        "options": [
            {
                "id": "A",
                "text": "$3\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 2\\text{AlCl}_3(aq) + 3\\text{BaSO}_4(s)$",
                "is_correct": True,
                "rationale": "Three $\\text{Ba}^{2+}$ ions precipitate with three $\\text{SO}_4^{2-}$ ions, leaving two $\\text{Al}^{3+}$ and six $\\text{Cl}^-$ as $2\\text{AlCl}_3$."
            },
            {
                "id": "B",
                "text": "$\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow \\text{AlCl}_3(aq) + \\text{BaSO}_4(s)$",
                "is_correct": False,
                "rationale": "This formula statement is unbalanced for all elements."
            },
            {
                "id": "C",
                "text": "$2\\text{BaCl}_2(aq) + \\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 2\\text{AlCl}_3(aq) + 2\\text{BaSO}_4(s)$",
                "is_correct": False,
                "rationale": "Sulphate and chlorine atoms are unbalanced."
            },
            {
                "id": "D",
                "text": "$3\\text{BaCl}_2(aq) + 2\\text{Al}_2(\\text{SO}_4)_3(aq) \\rightarrow 4\\text{AlCl}_3(aq) + 3\\text{BaSO}_4(s)$",
                "is_correct": False,
                "rationale": "Aluminium and sulphate counts do not balance."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex05_d",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "5(d)",
        "text": "Translate the statement into a balanced chemical equation:\n'Potassium metal reacts with water to give potassium hydroxide and hydrogen gas.'",
        "options": [
            {
                "id": "A",
                "text": "$2\\text{K}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{KOH}(aq) + \\text{H}_2(g)$",
                "is_correct": True,
                "rationale": "Potassium reacts vigorously with water releasing hydrogen gas and forming aqueous potassium hydroxide."
            },
            {
                "id": "B",
                "text": "$\\text{K}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{KOH}(aq) + \\text{H}(g)$",
                "is_correct": False,
                "rationale": "Hydrogen is evolved as molecular $\\text{H}_2$, not monoatomic $\\text{H}$."
            },
            {
                "id": "C",
                "text": "$2\\text{K}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{K}_2\\text{O}(s) + \\text{H}_2(g)$",
                "is_correct": False,
                "rationale": "The alkali metal hydroxide is formed in water, not oxide."
            },
            {
                "id": "D",
                "text": "$\\text{K}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{K}(\\text{OH})_2(aq) + \\text{H}_2(g)$",
                "is_correct": False,
                "rationale": "Potassium is monovalent ($+1$); $\\text{K(OH)}_2$ is an invalid formula."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex06_a",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "6(a)",
        "text": "Balance the following chemical equation:\n$$\\text{HNO}_3 + \\text{Ca(OH)}_2 \\rightarrow \\text{Ca(NO}_3)_2 + \\text{H}_2\\text{O}$$",
        "options": [
            {
                "id": "A",
                "text": "$2\\text{HNO}_3 + \\text{Ca(OH)}_2 \\rightarrow \\text{Ca(NO}_3)_2 + 2\\text{H}_2\\text{O}$",
                "is_correct": True,
                "rationale": "Two moles of $\\text{HNO}_3$ provide two nitrate ions for $\\text{Ca(NO}_3)_2$ and two hydrogen ions to form $2\\text{H}_2\\text{O}$."
            },
            {
                "id": "B",
                "text": "$\\text{HNO}_3 + \\text{Ca(OH)}_2 \\rightarrow \\text{Ca(NO}_3)_2 + \\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Nitrogen and hydrogen atoms are unbalanced."
            },
            {
                "id": "C",
                "text": "$2\\text{HNO}_3 + 2\\text{Ca(OH)}_2 \\rightarrow 2\\text{Ca(NO}_3)_2 + 3\\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Calcium and oxygen atoms do not balance."
            },
            {
                "id": "D",
                "text": "$\\text{HNO}_3 + 2\\text{Ca(OH)}_2 \\rightarrow \\text{Ca(NO}_3)_2 + 2\\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Nitrate groups are not balanced."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex06_b",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "6(b)",
        "text": "Balance the following chemical equation:\n$$\\text{NaOH} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{Na}_2\\text{SO}_4 + \\text{H}_2\\text{O}$$",
        "options": [
            {
                "id": "A",
                "text": "$2\\text{NaOH} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{Na}_2\\text{SO}_4 + 2\\text{H}_2\\text{O}$",
                "is_correct": True,
                "rationale": "Two sodium atoms on LHS balance $\\text{Na}_2\\text{SO}_4$, and four hydrogen atoms balance $2\\text{H}_2\\text{O}$."
            },
            {
                "id": "B",
                "text": "$\\text{NaOH} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{Na}_2\\text{SO}_4 + \\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Sodium is unbalanced ($1$ on LHS vs $2$ on RHS)."
            },
            {
                "id": "C",
                "text": "$2\\text{NaOH} + 2\\text{H}_2\\text{SO}_4 \\rightarrow 2\\text{Na}_2\\text{SO}_4 + 3\\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Sulphur and oxygen atoms are unbalanced."
            },
            {
                "id": "D",
                "text": "$\\text{NaOH} + 2\\text{H}_2\\text{SO}_4 \\rightarrow \\text{Na}_2\\text{SO}_4 + 2\\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Both sodium and sulphate counts fail to balance."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex06_c",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "6(c)",
        "text": "Balance the following chemical equation:\n$$\\text{NaCl} + \\text{AgNO}_3 \\rightarrow \\text{AgCl} + \\text{NaNO}_3$$",
        "options": [
            {
                "id": "A",
                "text": "$\\text{NaCl} + \\text{AgNO}_3 \\rightarrow \\text{AgCl} + \\text{NaNO}_3$",
                "is_correct": True,
                "rationale": "The equation is already balanced with a $1:1:1:1$ stoichiometric ratio."
            },
            {
                "id": "B",
                "text": "$2\\text{NaCl} + \\text{AgNO}_3 \\rightarrow 2\\text{AgCl} + \\text{NaNO}_3$",
                "is_correct": False,
                "rationale": "Silver and sodium atoms would become unbalanced."
            },
            {
                "id": "C",
                "text": "$\\text{NaCl} + 2\\text{AgNO}_3 \\rightarrow \\text{AgCl} + 2\\text{NaNO}_3$",
                "is_correct": False,
                "rationale": "Chlorine and silver counts do not balance."
            },
            {
                "id": "D",
                "text": "$2\\text{NaCl} + 2\\text{AgNO}_3 \\rightarrow 2\\text{AgCl} + \\text{Na}_2\\text{NO}_3$",
                "is_correct": False,
                "rationale": "$\\text{Na}_2\\text{NO}_3$ is an invalid formula."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex06_d",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "6(d)",
        "text": "Balance the following chemical equation:\n$$\\text{BaCl}_2 + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + \\text{HCl}$$",
        "options": [
            {
                "id": "A",
                "text": "$\\text{BaCl}_2 + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 2\\text{HCl}$",
                "is_correct": True,
                "rationale": "Two chlorine and two hydrogen atoms on the left require coefficient $2$ before $\\text{HCl}$."
            },
            {
                "id": "B",
                "text": "$\\text{BaCl}_2 + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + \\text{HCl}$",
                "is_correct": False,
                "rationale": "Chlorine and hydrogen are unbalanced ($2$ on LHS vs $1$ on RHS)."
            },
            {
                "id": "C",
                "text": "$2\\text{BaCl}_2 + \\text{H}_2\\text{SO}_4 \\rightarrow 2\\text{BaSO}_4 + 2\\text{HCl}$",
                "is_correct": False,
                "rationale": "Sulphate and barium counts do not balance."
            },
            {
                "id": "D",
                "text": "$\\text{BaCl}_2 + 2\\text{H}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 4\\text{HCl}$",
                "is_correct": False,
                "rationale": "Sulphate and chlorine atoms are unbalanced."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex07_a",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "7(a)",
        "text": "Write the balanced chemical equation for the reaction:\n$$\\text{Calcium hydroxide} + \\text{Carbon dioxide} \\rightarrow \\text{Calcium carbonate} + \\text{Water}$$",
        "options": [
            {
                "id": "A",
                "text": "$\\text{Ca(OH)}_2 + \\text{CO}_2 \\rightarrow \\text{CaCO}_3 + \\text{H}_2\\text{O}$",
                "is_correct": True,
                "rationale": "The equation is balanced as written with $1\\text{ Ca}$, $1\\text{ C}$, $2\\text{ H}$, and $4\\text{ O}$ on both sides."
            },
            {
                "id": "B",
                "text": "$2\\text{Ca(OH)}_2 + \\text{CO}_2 \\rightarrow 2\\text{CaCO}_3 + \\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Carbon and oxygen atoms are unbalanced."
            },
            {
                "id": "C",
                "text": "$\\text{Ca(OH)}_2 + 2\\text{CO}_2 \\rightarrow \\text{CaCO}_3 + 2\\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Carbon and oxygen atoms do not balance."
            },
            {
                "id": "D",
                "text": "$\\text{Ca(OH)}_2 + \\text{CO}_2 \\rightarrow \\text{Ca(HCO}_3)_2 + \\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Calcium bicarbonate is formed only when excess $\\text{CO}_2$ is bubbled, and no water is produced."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex07_b",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "7(b)",
        "text": "Write the balanced chemical equation for the reaction:\n$$\\text{Zinc} + \\text{Silver nitrate} \\rightarrow \\text{Zinc nitrate} + \\text{Silver}$$",
        "options": [
            {
                "id": "A",
                "text": "$\\text{Zn} + 2\\text{AgNO}_3 \\rightarrow \\text{Zn(NO}_3)_2 + 2\\text{Ag}$",
                "is_correct": True,
                "rationale": "Zinc is bivalent (forms $\\text{Zn}^{2+}$), requiring two monovalent $\\text{NO}_3^-$ ions and displacing two silver atoms."
            },
            {
                "id": "B",
                "text": "$\\text{Zn} + \\text{AgNO}_3 \\rightarrow \\text{ZnNO}_3 + \\text{Ag}$",
                "is_correct": False,
                "rationale": "$\\text{ZnNO}_3$ is an incorrect formula; zinc nitrate is $\\text{Zn(NO}_3)_2$."
            },
            {
                "id": "C",
                "text": "$2\\text{Zn} + 2\\text{AgNO}_3 \\rightarrow 2\\text{Zn(NO}_3)_2 + \\text{Ag}$",
                "is_correct": False,
                "rationale": "Nitrate and silver atoms are not balanced."
            },
            {
                "id": "D",
                "text": "$\\text{Zn} + 3\\text{AgNO}_3 \\rightarrow \\text{Zn(NO}_3)_3 + 3\\text{Ag}$",
                "is_correct": False,
                "rationale": "Zinc does not exhibit a $+3$ oxidation state."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex07_c",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "7(c)",
        "text": "Write the balanced chemical equation for the reaction:\n$$\\text{Aluminium} + \\text{Copper chloride} \\rightarrow \\text{Aluminium chloride} + \\text{Copper}$$",
        "options": [
            {
                "id": "A",
                "text": "$2\\text{Al} + 3\\text{CuCl}_2 \\rightarrow 2\\text{AlCl}_3 + 3\\text{Cu}$",
                "is_correct": True,
                "rationale": "Two $\\text{Al}$ atoms ($+3$) balance with six chlorine atoms from three $\\text{CuCl}_2$ ($+2$), displacing three $\\text{Cu}$ atoms."
            },
            {
                "id": "B",
                "text": "$\\text{Al} + \\text{CuCl}_2 \\rightarrow \\text{AlCl}_2 + \\text{Cu}$",
                "is_correct": False,
                "rationale": "$\\text{AlCl}_2$ is an incorrect formula; aluminium forms $\\text{AlCl}_3$."
            },
            {
                "id": "C",
                "text": "$2\\text{Al} + \\text{CuCl}_2 \\rightarrow 2\\text{AlCl} + \\text{Cu}$",
                "is_correct": False,
                "rationale": "Aluminium chloride is $\\text{AlCl}_3$ and the equation is unbalanced."
            },
            {
                "id": "D",
                "text": "$3\\text{Al} + 2\\text{CuCl}_2 \\rightarrow 3\\text{AlCl}_2 + 2\\text{Cu}$",
                "is_correct": False,
                "rationale": "Both chemical formula and stoichiometry are incorrect."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex07_d",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "7(d)",
        "text": "Write the balanced chemical equation for the reaction:\n$$\\text{Barium chloride} + \\text{Potassium sulphate} \\rightarrow \\text{Barium sulphate} + \\text{Potassium chloride}$$",
        "options": [
            {
                "id": "A",
                "text": "$\\text{BaCl}_2 + \\text{K}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 2\\text{KCl}$",
                "is_correct": True,
                "rationale": "One $\\text{Ba}^{2+}$ combines with $\\text{SO}_4^{2-}$ forming $\\text{BaSO}_4$, and two $\\text{K}^+$ combine with two $\\text{Cl}^-$ forming $2\\text{KCl}$."
            },
            {
                "id": "B",
                "text": "$\\text{BaCl}_2 + \\text{K}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + \\text{KCl}$",
                "is_correct": False,
                "rationale": "Potassium and chlorine are unbalanced ($2$ on LHS vs $1$ on RHS)."
            },
            {
                "id": "C",
                "text": "$2\\text{BaCl}_2 + \\text{K}_2\\text{SO}_4 \\rightarrow 2\\text{BaSO}_4 + \\text{KCl}_2$",
                "is_correct": False,
                "rationale": "$\\text{KCl}_2$ is an invalid formula and barium is unbalanced."
            },
            {
                "id": "D",
                "text": "$\\text{BaCl}_2 + 2\\text{K}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 4\\text{KCl}$",
                "is_correct": False,
                "rationale": "Sulphate and chlorine atoms do not balance."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex08_a",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "8(a)",
        "text": "Write the balanced chemical equation and identify the reaction type:\n$$\\text{Potassium bromide}(aq) + \\text{Barium iodide}(aq) \\rightarrow \\text{Potassium iodide}(aq) + \\text{Barium bromide}(s)$$",
        "options": [
            {
                "id": "A",
                "text": "$2\\text{KBr}(aq) + \\text{BaI}_2(aq) \\rightarrow 2\\text{KI}(aq) + \\text{BaBr}_2(s)$ (Double displacement)",
                "is_correct": True,
                "rationale": "Potassium and barium exchange their halide counter-ions, representing a double displacement reaction."
            },
            {
                "id": "B",
                "text": "$\\text{KBr}(aq) + \\text{BaI}_2(aq) \\rightarrow \\text{KI}(aq) + \\text{BaBr}_2(s)$ (Single displacement)",
                "is_correct": False,
                "rationale": "This equation is unbalanced and misidentifies ion exchange as single displacement."
            },
            {
                "id": "C",
                "text": "$2\\text{KBr}(aq) + \\text{BaI}_2(aq) \\rightarrow 2\\text{KI}(aq) + \\text{BaBr}_2(s)$ (Decomposition)",
                "is_correct": False,
                "rationale": "The reaction involves two compounds reacting, not a single compound breaking down."
            },
            {
                "id": "D",
                "text": "$\\text{KBr}(aq) + 2\\text{BaI}_2(aq) \\rightarrow \\text{KI}(aq) + 2\\text{BaBr}_2(s)$ (Combination)",
                "is_correct": False,
                "rationale": "The stoichiometry is incorrect and two products are formed, not one."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex08_b",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "8(b)",
        "text": "Write the balanced chemical equation and identify the reaction type:\n$$\\text{Zinc carbonate}(s) \\rightarrow \\text{Zinc oxide}(s) + \\text{Carbon dioxide}(g)$$",
        "options": [
            {
                "id": "A",
                "text": "$\\text{ZnCO}_3(s) \\xrightarrow{\\Delta} \\text{ZnO}(s) + \\text{CO}_2(g)$ (Decomposition)",
                "is_correct": True,
                "rationale": "A single reactant (zinc carbonate) breaks down upon heating into two simpler products (zinc oxide and carbon dioxide)."
            },
            {
                "id": "B",
                "text": "$2\\text{ZnCO}_3(s) \\rightarrow 2\\text{ZnO}(s) + \\text{CO}_2(g)$ (Combination)",
                "is_correct": False,
                "rationale": "Equation is unbalanced for oxygen and misclassifies decomposition as combination."
            },
            {
                "id": "C",
                "text": "$\\text{ZnCO}_3(s) \\rightarrow \\text{ZnO}(s) + \\text{CO}_2(g)$ (Displacement)",
                "is_correct": False,
                "rationale": "There is no elemental displacing agent; it is a thermal breakdown."
            },
            {
                "id": "D",
                "text": "$\\text{ZnCO}_3(s) \\rightarrow \\text{Zn}(s) + \\text{CO}_3(g)$ (Neutralisation)",
                "is_correct": False,
                "rationale": "$\\text{CO}_3$ is not a stable neutral gas and this is not acid-base neutralisation."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex08_c",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "8(c)",
        "text": "Write the balanced chemical equation and identify the reaction type:\n$$\\text{Hydrogen}(g) + \\text{Chlorine}(g) \\rightarrow \\text{Hydrogen chloride}(g)$$",
        "options": [
            {
                "id": "A",
                "text": "$\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{HCl}(g)$ (Combination)",
                "is_correct": True,
                "rationale": "Two elemental reactants combine to form a single product ($\\text{HCl}$), which is a combination reaction."
            },
            {
                "id": "B",
                "text": "$\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{HCl}(g)$ (Displacement)",
                "is_correct": False,
                "rationale": "Neither element is displaced from a compound; two elements synthesize one compound."
            },
            {
                "id": "C",
                "text": "$\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow \\text{H}_2\\text{Cl}_2(g)$ (Decomposition)",
                "is_correct": False,
                "rationale": "$\\text{H}_2\\text{Cl}_2$ is an invalid formula and this is synthesis, not decomposition."
            },
            {
                "id": "D",
                "text": "$2\\text{H}_2(g) + \\text{Cl}_2(g) \\rightarrow 2\\text{H}_2\\text{Cl}(g)$ (Double displacement)",
                "is_correct": False,
                "rationale": "The equation is stoichiometry incorrect and not double displacement."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex08_d",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "8(d)",
        "text": "Write the balanced chemical equation and identify the reaction type:\n$$\\text{Magnesium}(s) + \\text{Hydrochloric acid}(aq) \\rightarrow \\text{Magnesium chloride}(aq) + \\text{Hydrogen}(g)$$",
        "options": [
            {
                "id": "A",
                "text": "$\\text{Mg}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{MgCl}_2(aq) + \\text{H}_2(g)$ (Displacement)",
                "is_correct": True,
                "rationale": "Magnesium is more reactive than hydrogen and displaces it from $\\text{HCl}$, forming $\\text{MgCl}_2$ and $\\text{H}_2$."
            },
            {
                "id": "B",
                "text": "$\\text{Mg}(s) + \\text{HCl}(aq) \\rightarrow \\text{MgCl}_2(aq) + \\text{H}_2(g)$ (Combination)",
                "is_correct": False,
                "rationale": "Equation is unbalanced for $\\text{Cl}$ and $\\text{H}$, and two products are formed."
            },
            {
                "id": "C",
                "text": "$2\\text{Mg}(s) + 2\\text{HCl}(aq) \\rightarrow 2\\text{MgCl}(aq) + \\text{H}_2(g)$ (Decomposition)",
                "is_correct": False,
                "rationale": "$\\text{MgCl}$ is incorrect (magnesium is bivalent) and it is not decomposition."
            },
            {
                "id": "D",
                "text": "$\\text{Mg}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{MgCl}_2(aq) + \\text{H}_2(g)$ (Double displacement)",
                "is_correct": False,
                "rationale": "Magnesium is an element reacting with a compound, which is single displacement."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex09",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "9",
        "text": "What is the primary difference between exothermic and endothermic reactions?",
        "options": [
            {
                "id": "A",
                "text": "Exothermic reactions release heat energy into surroundings; endothermic reactions absorb heat energy",
                "is_correct": True,
                "rationale": "Exothermic reactions produce heat along with products ($\\Delta H < 0$); endothermic reactions require continuous heat input ($\\Delta H > 0$)."
            },
            {
                "id": "B",
                "text": "Exothermic reactions absorb electrical energy from surroundings; endothermic reactions release photons",
                "is_correct": False,
                "rationale": "The defining thermodynamic distinction is release versus absorption of heat energy."
            },
            {
                "id": "C",
                "text": "Exothermic reactions occur only at high temperatures; endothermic reactions occur only below freezing point",
                "is_correct": False,
                "rationale": "Reaction temperature range does not define exothermic or endothermic nature."
            },
            {
                "id": "D",
                "text": "Exothermic reactions require catalyst addition; endothermic reactions proceed spontaneously without input",
                "is_correct": False,
                "rationale": "Catalysis affects reaction rate, not the net exothermic or endothermic enthalpy change."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex10",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "10",
        "text": "Why is respiration considered an exothermic reaction?",
        "options": [
            {
                "id": "A",
                "text": "Glucose combines with oxygen in cells to form carbon dioxide, water, and releases energy",
                "is_correct": True,
                "rationale": "In $\\text{C}_6\\text{H}_{12}\\text{O}_6 + 6\\text{O}_2 \\rightarrow 6\\text{CO}_2 + 6\\text{H}_2\\text{O} + \\text{Energy}$, the oxidation of glucose yields metabolic energy sustaining cellular life."
            },
            {
                "id": "B",
                "text": "Digestion breaks complex starch molecules down into simpler sugars by absorbing atmospheric heat",
                "is_correct": False,
                "rationale": "Digestion is preliminary breakdown; respiration is the cellular oxidation yielding energy."
            },
            {
                "id": "C",
                "text": "Inhaled oxygen expands within lung alveoli producing thermal heat during mechanical gas exchange",
                "is_correct": False,
                "rationale": "Physical lung expansion is mechanical breathing, not biochemical cellular respiration."
            },
            {
                "id": "D",
                "text": "Body temperature is maintained solely by cooling perspiration produced during physical activity",
                "is_correct": False,
                "rationale": "Perspiration is an evaporative cooling mechanism, not the heat-producing process."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex11",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "11",
        "text": "Why are decomposition reactions called the opposite of combination reactions?",
        "options": [
            {
                "id": "A",
                "text": "In combination two or more reactants form one product; in decomposition one reactant breaks into multiple products",
                "is_correct": True,
                "rationale": "Combination follows $A + B \\rightarrow AB$, whereas decomposition follows the reverse $AB \\rightarrow A + B$."
            },
            {
                "id": "B",
                "text": "Combination reactions require constant energy input; decomposition reactions always release large amounts of heat",
                "is_correct": False,
                "rationale": "Decomposition typically absorbs energy (endothermic), while combination often releases heat."
            },
            {
                "id": "C",
                "text": "Combination reactions involve only gaseous elements; decomposition reactions involve only solid ionic compounds",
                "is_correct": False,
                "rationale": "Both reaction classes encompass solids, liquids, aqueous solutions, and gases."
            },
            {
                "id": "D",
                "text": "In combination oxidation numbers decrease; in decomposition all reacting elements retain zero oxidation state",
                "is_correct": False,
                "rationale": "Oxidation states change depending on the specific redox nature of the reaction."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex12",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "12",
        "text": "Which set correctly provides one decomposition equation each using heat, light, and electricity?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{CaCO}_3 \\xrightarrow{\\Delta} \\text{CaO} + \\text{CO}_2$, $2\\text{AgCl} \\xrightarrow{\\text{light}} 2\\text{Ag} + \\text{Cl}_2$, $2\\text{H}_2\\text{O} \\xrightarrow{\\text{elec.}} 2\\text{H}_2 + \\text{O}_2$",
                "is_correct": True,
                "rationale": "Thermal decomposition of limestone (heat), photolytic decomposition of silver chloride (light), and electrolytic decomposition of water (electricity)."
            },
            {
                "id": "B",
                "text": "$\\text{C} + \\text{O}_2 \\rightarrow \\text{CO}_2$, $\\text{H}_2 + \\text{Cl}_2 \\rightarrow 2\\text{HCl}$, $\\text{Zn} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{ZnSO}_4 + \\text{H}_2$",
                "is_correct": False,
                "rationale": "These are combination and single displacement reactions, not decomposition reactions."
            },
            {
                "id": "C",
                "text": "$2\\text{Mg} + \\text{O}_2 \\rightarrow 2\\text{MgO}$, $\\text{CH}_4 + 2\\text{O}_2 \\rightarrow \\text{CO}_2 + 2\\text{H}_2\\text{O}$, $\\text{Fe} + \\text{CuSO}_4 \\rightarrow \\text{FeSO}_4 + \\text{Cu}$",
                "is_correct": False,
                "rationale": "These represent synthesis, combustion, and displacement reactions."
            },
            {
                "id": "D",
                "text": "$\\text{CaO} + \\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2$, $2\\text{H}_2 + \\text{O}_2 \\rightarrow 2\\text{H}_2\\text{O}$, $\\text{Pb} + \\text{CuCl}_2 \\rightarrow \\text{PbCl}_2 + \\text{Cu}$",
                "is_correct": False,
                "rationale": "These are combination and displacement reactions."
            }
        ],
        "difficulty": "hard"
    },
    {
        "id": "sci_ch1_ex13",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "13",
        "text": "What is the primary difference between displacement and double displacement reactions?",
        "options": [
            {
                "id": "A",
                "text": "Displacement involves a more reactive element replacing another; double displacement involves mutual exchange of ions",
                "is_correct": True,
                "rationale": "In single displacement, a free element displaces a less reactive element from a compound; in double displacement, two compounds exchange ions."
            },
            {
                "id": "B",
                "text": "Displacement occurs only in molten salts; double displacement occurs exclusively between neutral non-polar gases",
                "is_correct": False,
                "rationale": "Both reactions predominantly occur in aqueous solutions."
            },
            {
                "id": "C",
                "text": "Displacement always yields a white precipitate; double displacement always produces an inflammable gas",
                "is_correct": False,
                "rationale": "Double displacement often forms precipitates, whereas displacement often liberates metals or hydrogen gas."
            },
            {
                "id": "D",
                "text": "Displacement involves two compounds exchanging cations; double displacement involves a single element reaction",
                "is_correct": False,
                "rationale": "This reverses the fundamental definitions of the two reaction types."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex14",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "14",
        "text": "In silver refining, recovery of silver from silver nitrate solution involves displacement by copper metal. What is the reaction equation?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{Cu}(s) + 2\\text{AgNO}_3(aq) \\rightarrow \\text{Cu(NO}_3)_2(aq) + 2\\text{Ag}(s)$",
                "is_correct": True,
                "rationale": "Copper is more reactive than silver and displaces silver ions from silver nitrate, forming blue cupric nitrate solution and metallic silver."
            },
            {
                "id": "B",
                "text": "$\\text{Cu}(s) + \\text{AgNO}_3(aq) \\rightarrow \\text{CuNO}_3(aq) + \\text{Ag}(s)$",
                "is_correct": False,
                "rationale": "Copper(II) nitrate is $\\text{Cu(NO}_3)_2$, not $\\text{CuNO}_3$."
            },
            {
                "id": "C",
                "text": "$2\\text{Cu}(s) + 2\\text{AgNO}_3(aq) \\rightarrow 2\\text{CuNO}_3(aq) + \\text{Ag}_2(s)$",
                "is_correct": False,
                "rationale": "Silver metal precipitates as individual atoms ($2\\text{Ag}$), not $\\text{Ag}_2$ molecules."
            },
            {
                "id": "D",
                "text": "$\\text{Cu}(s) + 3\\text{AgNO}_3(aq) \\rightarrow \\text{Cu(NO}_3)_3(aq) + 3\\text{Ag}(s)$",
                "is_correct": False,
                "rationale": "Copper exhibits $+1$ and $+2$ oxidation states, not $+3$."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex15",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "15",
        "text": "What defines a precipitation reaction in aqueous solutions?",
        "options": [
            {
                "id": "A",
                "text": "A reaction between aqueous solutions that produces an insoluble solid substance separating from the liquid",
                "is_correct": True,
                "rationale": "Any chemical reaction that produces an insoluble salt (precipitate) is defined as a precipitation reaction."
            },
            {
                "id": "B",
                "text": "A reaction in which liquid water evaporates completely leaving behind dry crystalline solute residue",
                "is_correct": False,
                "rationale": "Evaporation is a physical separation process, not a chemical precipitation reaction."
            },
            {
                "id": "C",
                "text": "A reaction in which strong acid neutralises base forming only soluble salt and liquid water",
                "is_correct": False,
                "rationale": "Neutralisation forming soluble salt does not produce a precipitate."
            },
            {
                "id": "D",
                "text": "A reaction where thermal heating decomposes a hydrated metal sulphate into gaseous oxides",
                "is_correct": False,
                "rationale": "This describes thermal decomposition, not aqueous precipitation."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex16_a",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "16(a)",
        "text": "How is oxidation defined in terms of gain or loss of oxygen, and which is an example?",
        "options": [
            {
                "id": "A",
                "text": "Oxidation is the gain of oxygen; e.g., $2\\text{Cu} + \\text{O}_2 \\rightarrow 2\\text{CuO}$",
                "is_correct": True,
                "rationale": "Oxidation is chemically defined as the addition/gain of oxygen to a substance; here copper gains oxygen."
            },
            {
                "id": "B",
                "text": "Oxidation is the loss of oxygen; e.g., $\\text{CuO} + \\text{H}_2 \\rightarrow \\text{Cu} + \\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Loss of oxygen is reduction, not oxidation."
            },
            {
                "id": "C",
                "text": "Oxidation is the gain of hydrogen; e.g., $\\text{N}_2 + 3\\text{H}_2 \\rightarrow 2\\text{NH}_3$",
                "is_correct": False,
                "rationale": "Gain of hydrogen corresponds to reduction, and the prompt requires oxygen terms."
            },
            {
                "id": "D",
                "text": "Oxidation is the displacement of metal ions; e.g., $\\text{Fe} + \\text{CuSO}_4 \\rightarrow \\text{FeSO}_4 + \\text{Cu}$",
                "is_correct": False,
                "rationale": "This is single displacement, not the classical oxygen gain definition."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex16_b",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "16(b)",
        "text": "How is reduction defined in terms of gain or loss of oxygen, and which is an example?",
        "options": [
            {
                "id": "A",
                "text": "Reduction is the loss of oxygen; e.g., $\\text{CuO} + \\text{H}_2 \\rightarrow \\text{Cu} + \\text{H}_2\\text{O}$",
                "is_correct": True,
                "rationale": "Reduction is chemically defined as the loss/removal of oxygen from a substance; here copper oxide loses oxygen to become copper."
            },
            {
                "id": "B",
                "text": "Reduction is the gain of oxygen; e.g., $2\\text{Mg} + \\text{O}_2 \\rightarrow 2\\text{MgO}$",
                "is_correct": False,
                "rationale": "Gain of oxygen is oxidation, not reduction."
            },
            {
                "id": "C",
                "text": "Reduction is the loss of hydrogen; e.g., $2\\text{H}_2\\text{S} + \\text{O}_2 \\rightarrow 2\\text{S} + 2\\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "Loss of hydrogen represents oxidation, not reduction."
            },
            {
                "id": "D",
                "text": "Reduction is the formation of a precipitate; e.g., $\\text{BaCl}_2 + \\text{Na}_2\\text{SO}_4 \\rightarrow \\text{BaSO}_4 + 2\\text{NaCl}$",
                "is_correct": False,
                "rationale": "Precipitation is double displacement, not reduction."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex17",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "17",
        "text": "A shiny brown coloured element 'X' on heating in air becomes black in colour. Identify element 'X' and the black compound formed.",
        "options": [
            {
                "id": "A",
                "text": "Element 'X' is copper ($\\text{Cu}$), and the black compound is copper(II) oxide ($\\text{CuO}$)",
                "is_correct": True,
                "rationale": "Copper metal is shiny reddish-brown; when heated in air, it oxidises to black cupric oxide according to $2\\text{Cu} + \\text{O}_2 \\rightarrow 2\\text{CuO}$."
            },
            {
                "id": "B",
                "text": "Element 'X' is iron ($\\text{Fe}$), and the black compound is ferrous sulphate ($\\text{FeSO}_4$)",
                "is_correct": False,
                "rationale": "Iron forms reddish-brown rust on moist oxidation, not black $\\text{CuO}$."
            },
            {
                "id": "C",
                "text": "Element 'X' is lead ($\\text{Pb}$), and the black compound is lead(II) oxide ($\\text{PbO}$)",
                "is_correct": False,
                "rationale": "Lead metal is silvery-grey, and lead oxide is yellow/reddish, not black."
            },
            {
                "id": "D",
                "text": "Element 'X' is silver ($\\text{Ag}$), and the black compound is silver sulphide ($\\text{Ag}_2\\text{S}$)",
                "is_correct": False,
                "rationale": "Silver is lustrous white, and tarnishing requires atmospheric sulphur, not heating in pure air."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch1_ex18",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "18",
        "text": "Why do we apply paint on iron articles?",
        "options": [
            {
                "id": "A",
                "text": "To prevent air and moisture from coming in direct contact with the iron surface, preventing corrosion",
                "is_correct": True,
                "rationale": "Rusting requires both oxygen and water vapor; paint creates an impermeable barrier blocking both."
            },
            {
                "id": "B",
                "text": "To chemically convert surface iron atoms into an inert layer of hard iron carbide alloy",
                "is_correct": False,
                "rationale": "Paint is a protective physical coating, not a metallurgical alloy conversion."
            },
            {
                "id": "C",
                "text": "To neutralize acidic sulfur dioxide pollutants present in ambient rain water on the metal",
                "is_correct": False,
                "rationale": "Paint acts as a barrier, not an acid-neutralising chemical buffer."
            },
            {
                "id": "D",
                "text": "To increase surface thermal conductivity so heat dissipates rapidly preventing oxidation",
                "is_correct": False,
                "rationale": "Thermal conductivity does not prevent electrochemical corrosion."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex19",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "19",
        "text": "Why are oil and fat containing food items flushed with nitrogen gas during packaging?",
        "options": [
            {
                "id": "A",
                "text": "To provide an unreactive inert atmosphere that prevents oxidation of oils and fats, avoiding rancidity",
                "is_correct": True,
                "rationale": "Nitrogen is chemically inert under packaging conditions; displacing oxygen prevents fat oxidation, unpleasant odor, and bad taste."
            },
            {
                "id": "B",
                "text": "To destroy anaerobic bacteria and mold spores by dehydrating packaged food materials",
                "is_correct": False,
                "rationale": "Flushing prevents oxidation, not dehydration sterilisation."
            },
            {
                "id": "C",
                "text": "To preserve crispy food texture by absorbing moisture released from packaged chips",
                "is_correct": False,
                "rationale": "Nitrogen gas is not a chemical desiccant."
            },
            {
                "id": "D",
                "text": "To chemically bind with unsaturated fatty acids and extend their calorific nutritional value",
                "is_correct": False,
                "rationale": "Nitrogen gas does not chemically react with food fats."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex20_a",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "20(a)",
        "text": "Which statement correctly explains the term 'corrosion' along with an example?",
        "options": [
            {
                "id": "A",
                "text": "The deterioration of metals by action of air, moisture, or acids; e.g., reddish-brown coating on iron",
                "is_correct": True,
                "rationale": "Corrosion is the slow eating away of metals by environmental agents; rusting of iron, black coating on silver, and green coating on copper are textbook examples."
            },
            {
                "id": "B",
                "text": "The rapid thermal decomposition of metals in flame; e.g., dazzling white light from magnesium",
                "is_correct": False,
                "rationale": "Combustion in flame is rapid oxidation, not corrosion."
            },
            {
                "id": "C",
                "text": "The violent dissolution of alkali metals in water; e.g., effervescence of sodium in water",
                "is_correct": False,
                "rationale": "Violent single displacement is not corrosion."
            },
            {
                "id": "D",
                "text": "The coating of non-reactive metals over plastics; e.g., chrome electroplating on polymer trim",
                "is_correct": False,
                "rationale": "Electroplating is an industrial manufacturing technique, not metal corrosion."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch1_ex20_b",
        "chapter": "Chemical Reactions and Equations",
        "section": "EXERCISES",
        "question_number": "20(b)",
        "text": "Which statement correctly explains the term 'rancidity' along with an example?",
        "options": [
            {
                "id": "A",
                "text": "The oxidation of fats and oils leading to foul smell and altered taste; e.g., butter left exposed in warm air",
                "is_correct": True,
                "rationale": "When fats and oils undergo atmospheric oxidation, they produce volatile, foul-smelling carboxylic acids and aldehydes (rancidity)."
            },
            {
                "id": "B",
                "text": "The bacterial fermentation of dairy milk sugars into lactic acid; e.g., formation of sour curd",
                "is_correct": False,
                "rationale": "Lactic fermentation is enzymatic bacterial fermentation, not lipid rancidity."
            },
            {
                "id": "C",
                "text": "The loss of hydration water from stored bakery items; e.g., hardening of bread in ambient air",
                "is_correct": False,
                "rationale": "Staling/drying is physical water loss, not fat oxidation."
            },
            {
                "id": "D",
                "text": "The thermal caramelisation of carbohydrates; e.g., browning of table sugar upon gentle heating",
                "is_correct": False,
                "rationale": "Caramelisation is thermal sugar degradation, not oil rancidity."
            }
        ],
        "difficulty": "easy"
    }
]

# Validation assertions
assert len(questions) == 47, f"Expected 47 questions, got {len(questions)}"
for idx, q in enumerate(questions, 1):
    assert len(q["options"]) == 4, f"Question {q['id']} must have exactly 4 options"
    correct_count = sum(1 for o in q["options"] if o["is_correct"])
    assert correct_count == 1, f"Question {q['id']} must have exactly 1 correct option, got {correct_count}"
    assert all("rationale" in o and len(o["rationale"]) > 5 for o in q["options"]), f"Missing rationale in {q['id']}"
    # Verify no rationale is leaked into text
    for o in q["options"]:
        assert "because" not in o["text"].lower() or len(o["text"]) < 130, f"Possible explanation leaked into option text in {q['id']}"

os.makedirs("assets/data", exist_ok=True)
with open("assets/data/ncert_science_ch1.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"SUCCESS: Validated and saved all {len(questions)} textbook questions to assets/data/ncert_science_ch1.json")
