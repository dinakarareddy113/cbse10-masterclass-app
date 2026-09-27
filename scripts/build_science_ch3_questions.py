"""
Script to generate ncert_science_ch3.json for CBSE Class 10 Science Chapter 3: Metals and Non-metals.
Source Isolation: NCERT Class 10 Science Chapter 3 in-text QUESTIONS (Pages 40, 46, 49, 53, 55)
and end-of-chapter EXERCISES (Pages 56-57).
"""

import json

questions = [
    # ==================== PAGE 40: QUESTIONS ====================
    {
        "id": "sci_ch3_p40_q01_i",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 40)",
        "question_number": "1(i)",
        "text": "Which of the following is an example of a metal that exists as a liquid at room temperature?",
        "options": [
            {
                "id": "A",
                "text": "Mercury ($\\text{Hg}$)",
                "is_correct": True,
                "rationale": "Mercury is the only elemental metal that remains liquid at standard room temperature (25°C / 298 K).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Bromine ($\\text{Br}$)",
                "is_correct": False,
                "rationale": "Bromine is indeed a liquid at room temperature, but it is a non-metal, not a metal.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Gallium ($\\text{Ga}$)",
                "is_correct": False,
                "rationale": "Gallium has a very low melting point (30°C / 303 K) and melts on palm heat, but is solid at standard room temperature (25°C).",
                "correct": False
            },
            {
                "id": "D",
                "text": "Lead ($\\text{Pb}$)",
                "is_correct": False,
                "rationale": "Lead is a solid, malleable, heavy metal at room temperature with a high melting point (327.5°C).",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Mercury ($\\text{Hg}$)\n\nScientific Principle / Key Concept:\nAlmost all metals are crystalline solids at room temperature. Mercury ($\\text{Hg}$) is the notable exception among metals that exists in liquid state at standard room temperature (25°C).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Bromine is a liquid at room temperature, but it belongs to the halogen group of non-metals.\n• Option (C): Incorrect. Gallium melts at body temperature (30°C), but remains a solid under ordinary room temperature.\n• Option (D): Incorrect. Lead is a solid metal with a melting point of 327.5°C.",
        "step_by_step_solution": "Correct Answer: (A) Mercury ($\\text{Hg}$)\n\nScientific Principle / Key Concept:\nAlmost all metals are crystalline solids at room temperature. Mercury ($\\text{Hg}$) is the notable exception among metals that exists in liquid state at standard room temperature (25°C).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Bromine is a liquid at room temperature, but it belongs to the halogen group of non-metals.\n• Option (C): Incorrect. Gallium melts at body temperature (30°C), but remains a solid under ordinary room temperature.\n• Option (D): Incorrect. Lead is a solid metal with a melting point of 327.5°C.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 40)",
        "questionNumber": "1(i)"
    },
    {
        "id": "sci_ch3_p40_q01_ii",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 40)",
        "question_number": "1(ii)",
        "text": "Which of the following metals is so soft that it can be easily cut with an ordinary knife?",
        "options": [
            {
                "id": "A",
                "text": "Sodium ($\\text{Na}$) and Potassium ($\\text{K}$)",
                "is_correct": True,
                "rationale": "Alkali metals like sodium and potassium have low densities, large atomic radii, and weak metallic bonding, making them soft enough to be sliced with a knife.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Iron ($\\text{Fe}$) and Copper ($\\text{Cu}$)",
                "is_correct": False,
                "rationale": "Iron and copper have dense crystal lattices with strong metallic bonds and high tensile strength, requiring heavy tools to cut.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Aluminium ($\\text{Al}$) and Zinc ($\\text{Zn}$)",
                "is_correct": False,
                "rationale": "Aluminium and zinc are moderately hard, ductile metals that cannot be cut with a common kitchen knife.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Gold ($\\text{Au}$) and Platinum ($\\text{Pt}$)",
                "is_correct": False,
                "rationale": "Gold is malleable and soft compared to steel, but cannot be sliced effortlessly like alkali metals.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Sodium ($\\text{Na}$) and Potassium ($\\text{K}$)\n\nScientific Principle / Key Concept:\nAlkali metals (Group 1 elements: Lithium, Sodium, Potassium) have only one valence electron per atom, resulting in relatively weak metallic bonding and low densities. Consequently, they are soft enough to be cut cleanly with a standard knife.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Transition metals like iron and copper have high hardness and strong metallic bonds.\n• Option (C): Incorrect. Aluminium and zinc are solid rigid metals.\n• Option (D): Incorrect. Gold and platinum are dense noble metals.",
        "step_by_step_solution": "Correct Answer: (A) Sodium ($\\text{Na}$) and Potassium ($\\text{K}$)\n\nScientific Principle / Key Concept:\nAlkali metals (Group 1 elements: Lithium, Sodium, Potassium) have only one valence electron per atom, resulting in relatively weak metallic bonding and low densities. Consequently, they are soft enough to be cut cleanly with a standard knife.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Transition metals like iron and copper have high hardness and strong metallic bonds.\n• Option (C): Incorrect. Aluminium and zinc are solid rigid metals.\n• Option (D): Incorrect. Gold and platinum are dense noble metals.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 40)",
        "questionNumber": "1(ii)"
    },
    {
        "id": "sci_ch3_p40_q01_iii",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 40)",
        "question_number": "1(iii)",
        "text": "Which metal is recognized as the best conductor of heat?",
        "options": [
            {
                "id": "A",
                "text": "Silver ($\\text{Ag}$)",
                "is_correct": True,
                "rationale": "Silver possesses the highest thermal conductivity and electrical conductivity of all metals, followed closely by copper.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Iron ($\\text{Fe}$)",
                "is_correct": False,
                "rationale": "Iron is a moderate conductor of heat, but its conductivity is significantly lower than that of silver and copper.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Lead ($\\text{Pb}$)",
                "is_correct": False,
                "rationale": "Lead is among the poorest thermal conductors among all metals.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Mercury ($\\text{Hg}$)",
                "is_correct": False,
                "rationale": "Mercury is a relatively poor conductor of heat compared to solid structural metals.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Silver ($\\text{Ag}$)\n\nScientific Principle / Key Concept:\nSilver ($\\text{Ag}$) and Copper ($\\text{Cu}$) are the best conductors of heat due to the high density and mobility of free electrons in their crystal lattices.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Iron conducts heat moderately well, but far less efficiently than silver.\n• Option (C): Incorrect. Lead is actually a poor conductor of heat.\n• Option (D): Incorrect. Mercury has low thermal conductivity relative to silver and copper.",
        "step_by_step_solution": "Correct Answer: (A) Silver ($\\text{Ag}$)\n\nScientific Principle / Key Concept:\nSilver ($\\text{Ag}$) and Copper ($\\text{Cu}$) are the best conductors of heat due to the high density and mobility of free electrons in their crystal lattices.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Iron conducts heat moderately well, but far less efficiently than silver.\n• Option (C): Incorrect. Lead is actually a poor conductor of heat.\n• Option (D): Incorrect. Mercury has low thermal conductivity relative to silver and copper.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 40)",
        "questionNumber": "1(iii)"
    },
    {
        "id": "sci_ch3_p40_q01_iv",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 40)",
        "question_number": "1(iv)",
        "text": "Which pair of metals are comparatively poor conductors of heat?",
        "options": [
            {
                "id": "A",
                "text": "Lead ($\\text{Pb}$) and Mercury ($\\text{Hg}$)",
                "is_correct": True,
                "rationale": "Lead and mercury have high electrical resistivity and poor thermal conductivity compared to typical metals like silver, copper, and aluminium.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Silver ($\\text{Ag}$) and Copper ($\\text{Cu}$)",
                "is_correct": False,
                "rationale": "Silver and copper are the best conductors of heat, not poor conductors.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Aluminium ($\\text{Al}$) and Gold ($\\text{Au}$)",
                "is_correct": False,
                "rationale": "Both aluminium and gold are excellent thermal conductors.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Zinc ($\\text{Zn}$) and Magnesium ($\\text{Mg}$)",
                "is_correct": False,
                "rationale": "Zinc and magnesium have good thermal conductivity, substantially higher than lead and mercury.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Lead ($\\text{Pb}$) and Mercury ($\\text{Hg}$)\n\nScientific Principle / Key Concept:\nWhile metals in general are good thermal conductors, Lead ($\\text{Pb}$) and Mercury ($\\text{Hg}$) stand out as notably poor conductors of heat.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Silver and copper are the top two thermal conductors.\n• Option (C): Incorrect. Aluminium and gold conduct heat very well.\n• Option (D): Incorrect. Zinc and magnesium are decent metallic conductors.",
        "step_by_step_solution": "Correct Answer: (A) Lead ($\\text{Pb}$) and Mercury ($\\text{Hg}$)\n\nScientific Principle / Key Concept:\nWhile metals in general are good thermal conductors, Lead ($\\text{Pb}$) and Mercury ($\\text{Hg}$) stand out as notably poor conductors of heat.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Silver and copper are the top two thermal conductors.\n• Option (C): Incorrect. Aluminium and gold conduct heat very well.\n• Option (D): Incorrect. Zinc and magnesium are decent metallic conductors.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 40)",
        "questionNumber": "1(iv)"
    },
    {
        "id": "sci_ch3_p40_q02_i",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 40)",
        "question_number": "2(i)",
        "text": "What is meant by the physical property of 'malleability' in metals?",
        "options": [
            {
                "id": "A",
                "text": "The property that allows metals to be beaten into thin sheets without fracturing",
                "is_correct": True,
                "rationale": "Malleability is the physical property of metals allowing them to deform under compressive stress (hammering or rolling) into thin sheets (e.g., gold and silver foils).",
                "correct": True
            },
            {
                "id": "B",
                "text": "The ability of metals to be drawn into very thin, flexible wires",
                "is_correct": False,
                "rationale": "Drawing into thin wires is ductility, not malleability.",
                "correct": False
            },
            {
                "id": "C",
                "text": "The property of metals to produce a ringing sound when struck",
                "is_correct": False,
                "rationale": "Producing a ringing sound is sonorousness.",
                "correct": False
            },
            {
                "id": "D",
                "text": "The tendency of metals to reflect light brightly from a clean surface",
                "is_correct": False,
                "rationale": "Reflecting light from a clean surface is metallic lustre.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) The property that allows metals to be beaten into thin sheets without fracturing\n\nScientific Principle / Key Concept:\nMalleability is the ability of a material to deform under compressive strain, allowing it to be hammered or rolled into thin sheets. Gold and silver are the most malleable metals.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. The ability to be stretched into thin wires is termed ductility.\n• Option (C): Incorrect. Ringing upon impact is sonorousness.\n• Option (D): Incorrect. Shiny appearance is metallic lustre.",
        "step_by_step_solution": "Correct Answer: (A) The property that allows metals to be beaten into thin sheets without fracturing\n\nScientific Principle / Key Concept:\nMalleability is the ability of a material to deform under compressive strain, allowing it to be hammered or rolled into thin sheets. Gold and silver are the most malleable metals.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. The ability to be stretched into thin wires is termed ductility.\n• Option (C): Incorrect. Ringing upon impact is sonorousness.\n• Option (D): Incorrect. Shiny appearance is metallic lustre.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 40)",
        "questionNumber": "2(i)"
    },
    {
        "id": "sci_ch3_p40_q02_ii",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 40)",
        "question_number": "2(ii)",
        "text": "What is meant by the physical property of 'ductility' in metals?",
        "options": [
            {
                "id": "A",
                "text": "The ability of metals to be drawn into long, thin wires without snapping",
                "is_correct": True,
                "rationale": "Ductility is the property of being drawn or stretched into thin wires under tensile force. Gold is the most ductile metal (1 g of gold can yield a 2 km wire).",
                "correct": True
            },
            {
                "id": "B",
                "text": "The capacity of metals to be flattened into foils by hammering",
                "is_correct": False,
                "rationale": "Flattening into foils is malleability.",
                "correct": False
            },
            {
                "id": "C",
                "text": "The resistance of metals to scratch marks and surface wear",
                "is_correct": False,
                "rationale": "Resistance to scratches is hardness.",
                "correct": False
            },
            {
                "id": "D",
                "text": "The property of metals conducting electric current with zero resistance",
                "is_correct": False,
                "rationale": "Zero electrical resistance is superconductivity.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) The ability of metals to be drawn into long, thin wires without snapping\n\nScientific Principle / Key Concept:\nDuctility is the capacity of a solid material to undergo tensile plastic deformation, enabling it to be drawn into thin wires. Gold is remarkably ductile; a wire of about 2 km length can be drawn from just 1 gram of gold.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Being flattened into foils is malleability.\n• Option (C): Incorrect. Resistance to wear is hardness.\n• Option (D): Incorrect. Conduction with zero resistance describes superconductivity.",
        "step_by_step_solution": "Correct Answer: (A) The ability of metals to be drawn into long, thin wires without snapping\n\nScientific Principle / Key Concept:\nDuctility is the capacity of a solid material to undergo tensile plastic deformation, enabling it to be drawn into thin wires. Gold is remarkably ductile; a wire of about 2 km length can be drawn from just 1 gram of gold.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Being flattened into foils is malleability.\n• Option (C): Incorrect. Resistance to wear is hardness.\n• Option (D): Incorrect. Conduction with zero resistance describes superconductivity.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 40)",
        "questionNumber": "2(ii)"
    },

    # ==================== PAGE 46: QUESTIONS ====================
    {
        "id": "sci_ch3_p46_q01",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 46)",
        "question_number": "1",
        "text": "Why is sodium metal always kept immersed in kerosene oil?",
        "options": [
            {
                "id": "A",
                "text": "It reacts vigorously with atmospheric oxygen and moisture, releasing heat that ignites the liberated hydrogen gas.",
                "is_correct": True,
                "rationale": "Sodium is an extremely reactive alkali metal. In open air, it reacts violently with oxygen and water vapor, spontaneously catching fire. Kerosene shields it from air and moisture.",
                "correct": True
            },
            {
                "id": "B",
                "text": "It is volatile and readily evaporates into toxic vapors if exposed to open air.",
                "is_correct": False,
                "rationale": "Sodium is a solid metal with a boiling point of 883°C; it does not evaporate at room temperature.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Kerosene dissolves the outer oxide layer to keep the sodium metal pure and shiny.",
                "is_correct": False,
                "rationale": "Kerosene is a non-polar hydrocarbon that neither reacts with nor dissolves sodium or sodium oxide.",
                "correct": False
            },
            {
                "id": "D",
                "text": "To prevent it from absorbing carbon dioxide which causes it to turn into a toxic gas.",
                "is_correct": False,
                "rationale": "Reaction with CO₂ forms solid sodium carbonate, not a toxic gas.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) It reacts vigorously with atmospheric oxygen and moisture, releasing heat that ignites the liberated hydrogen gas.\n\nScientific Principle / Key Concept:\nSodium ($\\text{Na}$) and Potassium ($\\text{K}$) have very low ionization energies and react vigorously with both oxygen and moisture present in the atmosphere. The reaction is so exothermic that the liberated $\\text{H}_2$ gas instantly catches fire ($2\\text{Na} + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{NaOH} + \\text{H}_2 + \\text{Heat}$). To prevent accidental fires, it is stored under kerosene.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Sodium is a solid metal with boiling point 883°C; it does not evaporate.\n• Option (C): Incorrect. Kerosene does not dissolve metal oxides.\n• Option (D): Incorrect. Reaction with air causes fire, not poisonous gas emission.",
        "step_by_step_solution": "Correct Answer: (A) It reacts vigorously with atmospheric oxygen and moisture, releasing heat that ignites the liberated hydrogen gas.\n\nScientific Principle / Key Concept:\nSodium ($\\text{Na}$) and Potassium ($\\text{K}$) have very low ionization energies and react vigorously with both oxygen and moisture present in the atmosphere. The reaction is so exothermic that the liberated $\\text{H}_2$ gas instantly catches fire ($2\\text{Na} + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{NaOH} + \\text{H}_2 + \\text{Heat}$). To prevent accidental fires, it is stored under kerosene.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Sodium is a solid metal with boiling point 883°C; it does not evaporate.\n• Option (C): Incorrect. Kerosene does not dissolve metal oxides.\n• Option (D): Incorrect. Reaction with air causes fire, not poisonous gas emission.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 46)",
        "questionNumber": "1"
    },
    {
        "id": "sci_ch3_p46_q02_i",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 46)",
        "question_number": "2(i)",
        "text": "Which balanced chemical equation correctly represents the reaction of red-hot iron with steam?",
        "options": [
            {
                "id": "A",
                "text": "$3\\text{Fe}(s) + 4\\text{H}_2\\text{O}(g) \\rightarrow \\text{Fe}_3\\text{O}_4(s) + 4\\text{H}_2(g)$",
                "is_correct": True,
                "rationale": "Iron does not react with cold or hot liquid water, but reacts with steam to form iron(II,III) oxide (magnetic iron oxide $\\text{Fe}_3\\text{O}_4$) and hydrogen gas.",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{Fe}(s) + \\text{H}_2\\text{O}(g) \\rightarrow \\text{FeO}(s) + \\text{H}_2(g)$",
                "is_correct": False,
                "rationale": "The oxide formed under steam is mixed ferroso-ferric oxide $\\text{Fe}_3\\text{O}_4$, not ferrous oxide $\\text{FeO}$.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$2\\text{Fe}(s) + 3\\text{H}_2\\text{O}(l) \\rightarrow \\text{Fe}_2\\text{O}_3(s) + 3\\text{H}_2(g)$",
                "is_correct": False,
                "rationale": "Iron does not react with liquid water $\\text{H}_2\\text{O}(l)$ to liberate hydrogen; steam $\\text{H}_2\\text{O}(g)$ is required, producing $\\text{Fe}_3\\text{O}_4$.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{Fe}(s) + 2\\text{H}_2\\text{O}(g) \\rightarrow \\text{Fe(OH)}_2(s) + \\text{H}_2(g)$",
                "is_correct": False,
                "rationale": "At the high temperatures of steam, metal hydroxides decompose into oxides; iron forms $\\text{Fe}_3\\text{O}_4$, not $\\text{Fe(OH)}_2$.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) $3\\text{Fe}(s) + 4\\text{H}_2\\text{O}(g) \\rightarrow \\text{Fe}_3\\text{O}_4(s) + 4\\text{H}_2(g)$\n\nScientific Principle / Key Concept:\nMetals like $\\text{Al}$, $\\text{Zn}$, and $\\text{Fe}$ do not react with cold or hot water. They react only with steam to produce metal oxide and hydrogen gas. In the case of iron, it forms mixed iron(II,III) oxide:\n$$3\\text{Fe}(s) + 4\\text{H}_2\\text{O}(g) \\rightarrow \\text{Fe}_3\\text{O}_4(s) + 4\\text{H}_2(g)$$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. The product is magnetic iron oxide $\\text{Fe}_3\\text{O}_4$, not $\\text{FeO}$.\n• Option (C): Incorrect. Iron does not react with liquid water to give $\\text{H}_2$, and the stoichiometry does not yield $\\text{Fe}_2\\text{O}_3$.\n• Option (D): Incorrect. Metal hydroxides are unstable at steam temperatures.",
        "step_by_step_solution": "Correct Answer: (A) $3\\text{Fe}(s) + 4\\text{H}_2\\text{O}(g) \\rightarrow \\text{Fe}_3\\text{O}_4(s) + 4\\text{H}_2(g)$\n\nScientific Principle / Key Concept:\nMetals like $\\text{Al}$, $\\text{Zn}$, and $\\text{Fe}$ do not react with cold or hot water. They react only with steam to produce metal oxide and hydrogen gas. In the case of iron, it forms mixed iron(II,III) oxide:\n$$3\\text{Fe}(s) + 4\\text{H}_2\\text{O}(g) \\rightarrow \\text{Fe}_3\\text{O}_4(s) + 4\\text{H}_2(g)$$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. The product is magnetic iron oxide $\\text{Fe}_3\\text{O}_4$, not $\\text{FeO}$.\n• Option (C): Incorrect. Iron does not react with liquid water to give $\\text{H}_2$, and the stoichiometry does not yield $\\text{Fe}_2\\text{O}_3$.\n• Option (D): Incorrect. Metal hydroxides are unstable at steam temperatures.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 46)",
        "questionNumber": "2(i)"
    },
    {
        "id": "sci_ch3_p46_q02_ii_a",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 46)",
        "question_number": "2(ii)(a)",
        "text": "When calcium metal is dropped into cold water, what is the chemical equation and why does calcium start floating?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{Ca}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{Ca(OH)}_2(aq) + \\text{H}_2(g)$; bubbles of $\\text{H}_2$ gas stick to the surface of the metal.",
                "is_correct": True,
                "rationale": "Calcium reacts less violently with water. The heat is insufficient for $\\text{H}_2$ to catch fire, and the bubbles of $\\text{H}_2$ gas adhere to the calcium metal, making it buoyant so it floats.",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{Ca}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{CaO}(s) + \\text{H}_2(g)$; calcium has lower density than water.",
                "is_correct": False,
                "rationale": "Calcium forms hydroxide $\\text{Ca(OH)}_2$, not oxide, and solid calcium is denser than water ($1.55\\text{ g/cm}^3$ vs $1.0\\text{ g/cm}^3$).",
                "correct": False
            },
            {
                "id": "C",
                "text": "$2\\text{Ca}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{CaOH}(aq) + \\text{H}_2(g)$; convection currents keep it on top.",
                "is_correct": False,
                "rationale": "Calcium has a valency of 2, forming $\\text{Ca(OH)}_2$, not $\\text{CaOH}$.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{Ca}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{CaH}_2(s) + \\text{O}_2(g)$; oxygen gas pushes it upward.",
                "is_correct": False,
                "rationale": "Reaction of metal with water liberates hydrogen gas, never oxygen gas.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) $\\text{Ca}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{Ca(OH)}_2(aq) + \\text{H}_2(g)$; bubbles of $\\text{H}_2$ gas stick to the surface of the metal.\n\nScientific Principle / Key Concept:\nThe reaction of calcium with water is less violent than sodium or potassium:\n$$\\text{Ca}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{Ca(OH)}_2(aq) + \\text{H}_2(g)$$\nThe heat evolved is insufficient for hydrogen to ignite. Calcium sinks initially, but soon starts floating because bubbles of hydrogen gas stick to its surface.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Calcium is denser than water (1.55 g/cm³); it floats only because of attached hydrogen gas bubbles.\n• Option (C): Incorrect. Calcium forms divalent $\\text{Ca(OH)}_2$.\n• Option (D): Incorrect. The reaction liberates $\\text{H}_2$, not $\\text{O}_2$.",
        "step_by_step_solution": "Correct Answer: (A) $\\text{Ca}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{Ca(OH)}_2(aq) + \\text{H}_2(g)$; bubbles of $\\text{H}_2$ gas stick to the surface of the metal.\n\nScientific Principle / Key Concept:\nThe reaction of calcium with water is less violent than sodium or potassium:\n$$\\text{Ca}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{Ca(OH)}_2(aq) + \\text{H}_2(g)$$\nThe heat evolved is insufficient for hydrogen to ignite. Calcium sinks initially, but soon starts floating because bubbles of hydrogen gas stick to its surface.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Calcium is denser than water (1.55 g/cm³); it floats only because of attached hydrogen gas bubbles.\n• Option (C): Incorrect. Calcium forms divalent $\\text{Ca(OH)}_2$.\n• Option (D): Incorrect. The reaction liberates $\\text{H}_2$, not $\\text{O}_2$.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 46)",
        "questionNumber": "2(ii)(a)"
    },
    {
        "id": "sci_ch3_p46_q02_ii_b",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 46)",
        "question_number": "2(ii)(b)",
        "text": "What is the balanced equation and observation when potassium reacts with cold water?",
        "options": [
            {
                "id": "A",
                "text": "$2\\text{K}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{KOH}(aq) + \\text{H}_2(g) + \\text{Heat}$; hydrogen instantly catches fire with a lilac flame.",
                "is_correct": True,
                "rationale": "Potassium reacts violently and exothermically with cold water. The immense heat ignites the evolved hydrogen gas with a characteristic violet/lilac flame.",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{K}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{K}_2\\text{O}(s) + \\text{H}_2(g)$; it forms an insoluble white precipitate without flame.",
                "is_correct": False,
                "rationale": "In excess water, potassium forms soluble hydroxide $\\text{KOH}$, not $\\text{K}_2\\text{O}$, and the reaction is violent with flame.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$2\\text{K}(s) + 4\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{KOH}(aq) + 2\\text{H}_2\\text{O}_2(aq)$; water is oxidized to hydrogen peroxide.",
                "is_correct": False,
                "rationale": "Water is reduced to $\\text{H}_2$ gas, not peroxide.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{K}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow \\text{K(OH)}_2(aq) + \\text{H}_2(g)$; potassium is divalent in solution.",
                "is_correct": False,
                "rationale": "Potassium is a monovalent alkali metal ($+1$), forming $\\text{KOH}$, not $\\text{K(OH)}_2$.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) $2\\text{K}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{KOH}(aq) + \\text{H}_2(g) + \\text{Heat}$; hydrogen instantly catches fire with a lilac flame.\n\nScientific Principle / Key Concept:\nPotassium reacts violently with cold water. The reaction is so violently exothermic that the evolved hydrogen gas instantly catches fire, burning with a distinctive lilac (violet) flame due to excitation of potassium atoms:\n$$2\\text{K}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{KOH}(aq) + \\text{H}_2(g) + \\text{Heat}$$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. In water, it forms soluble $\\text{KOH}$, not oxide, and burns vigorously.\n• Option (C): Incorrect. Hydrogen peroxide is not produced.\n• Option (D): Incorrect. Potassium is monovalent ($+1$).",
        "step_by_step_solution": "Correct Answer: (A) $2\\text{K}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{KOH}(aq) + \\text{H}_2(g) + \\text{Heat}$; hydrogen instantly catches fire with a lilac flame.\n\nScientific Principle / Key Concept:\nPotassium reacts violently with cold water. The reaction is so violently exothermic that the evolved hydrogen gas instantly catches fire, burning with a distinctive lilac (violet) flame due to excitation of potassium atoms:\n$$2\\text{K}(s) + 2\\text{H}_2\\text{O}(l) \\rightarrow 2\\text{KOH}(aq) + \\text{H}_2(g) + \\text{Heat}$$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. In water, it forms soluble $\\text{KOH}$, not oxide, and burns vigorously.\n• Option (C): Incorrect. Hydrogen peroxide is not produced.\n• Option (D): Incorrect. Potassium is monovalent ($+1$).",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 46)",
        "questionNumber": "2(ii)(b)"
    },
    {
        "id": "sci_ch3_p46_q03_i",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 46)",
        "question_number": "3(i)",
        "text": "Samples of four metals A, B, C, and D were added to salt solutions:\n• Metal A: No reaction with $\\text{FeSO}_4$, Displacement with $\\text{CuSO}_4$\n• Metal B: Displacement with $\\text{FeSO}_4$, No reaction with $\\text{ZnSO}_4$\n• Metal C: No reaction with $\\text{FeSO}_4$, $\\text{CuSO}_4$, or $\\text{ZnSO}_4$; Displacement with $\\text{AgNO}_3$\n• Metal D: No reaction with any of the four solutions.\n\nWhich of the metals is the most reactive?",
        "options": [
            {
                "id": "A",
                "text": "Metal B",
                "is_correct": True,
                "rationale": "Metal B is able to displace iron from $\\text{FeSO}_4$ solution, meaning B is more reactive than Fe. All other metals (A, C, D) failed to displace Fe.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Metal A",
                "is_correct": False,
                "rationale": "Metal A cannot displace Fe from $\\text{FeSO}_4$; it only displaces Cu, making it less reactive than B.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Metal C",
                "is_correct": False,
                "rationale": "Metal C cannot displace Fe, Cu, or Zn; it only displaces Ag, which has very low reactivity.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Metal D",
                "is_correct": False,
                "rationale": "Metal D does not displace any metal from solution, making it the least reactive of all.",
                "correct": False
            }
        ],
        "difficulty": "hard",
        "solution": "Correct Answer: (A) Metal B\n\nScientific Principle / Key Concept:\nA more reactive metal displaces a less reactive metal from its aqueous salt solution. In the reactivity series, $\\text{Zn} > \\text{Fe} > \\text{Cu} > \\text{Ag}$.\n• Metal B displaces $\\text{Fe}$, so $\\text{Reactivity of B} > \\text{Fe}$.\n• Metal A does not displace $\\text{Fe}$, but displaces $\\text{Cu}$, so $\\text{Fe} > \\text{A} > \\text{Cu}$.\n• Metal C only displaces $\\text{Ag}$, so $\\text{Cu} > \\text{C} > \\text{Ag}$.\n• Metal D displaces none, so it is the least reactive.\nHence, Metal B is the most reactive metal.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. A is below Fe since it cannot displace Fe.\n• Option (C): Incorrect. C is below Cu since it cannot displace Cu.\n• Option (D): Incorrect. D is the least reactive metal of all.",
        "step_by_step_solution": "Correct Answer: (A) Metal B\n\nScientific Principle / Key Concept:\nA more reactive metal displaces a less reactive metal from its aqueous salt solution. In the reactivity series, $\\text{Zn} > \\text{Fe} > \\text{Cu} > \\text{Ag}$.\n• Metal B displaces $\\text{Fe}$, so $\\text{Reactivity of B} > \\text{Fe}$.\n• Metal A does not displace $\\text{Fe}$, but displaces $\\text{Cu}$, so $\\text{Fe} > \\text{A} > \\text{Cu}$.\n• Metal C only displaces $\\text{Ag}$, so $\\text{Cu} > \\text{C} > \\text{Ag}$.\n• Metal D displaces none, so it is the least reactive.\nHence, Metal B is the most reactive metal.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. A is below Fe since it cannot displace Fe.\n• Option (C): Incorrect. C is below Cu since it cannot displace Cu.\n• Option (D): Incorrect. D is the least reactive metal of all.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 46)",
        "questionNumber": "3(i)"
    },
    {
        "id": "sci_ch3_p46_q03_ii",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 46)",
        "question_number": "3(ii)",
        "text": "Referring to the metals table (where Metal B displaces $\\text{Fe}$ from $\\text{FeSO}_4$), what would you observe if metal B is added to a solution of Copper(II) sulphate ($\\text{CuSO}_4$)?",
        "options": [
            {
                "id": "A",
                "text": "A displacement reaction occurs: the blue color of $\\text{CuSO}_4$ fades/discharges, and a reddish-brown deposit of copper forms on metal B.",
                "is_correct": True,
                "rationale": "Since B is more reactive than Fe, and Fe is more reactive than Cu, B is much more reactive than Cu. Therefore, B displaces Cu, decolorizing the blue $\\text{CuSO}_4$ and precipitating reddish-brown copper.",
                "correct": True
            },
            {
                "id": "B",
                "text": "No reaction takes place because Copper(II) sulphate is more stable than Iron(II) sulphate.",
                "is_correct": False,
                "rationale": "Copper is lower than iron in the reactivity series; if B displaces iron, it must also displace copper.",
                "correct": False
            },
            {
                "id": "C",
                "text": "A vigorous effervescence occurs releasing pungent smelling sulfur dioxide gas.",
                "is_correct": False,
                "rationale": "Displacement between a reactive metal and neutral $\\text{CuSO}_4$ does not liberate sulfur dioxide gas.",
                "correct": False
            },
            {
                "id": "D",
                "text": "The solution turns intensely dark green with no solid deposit.",
                "is_correct": False,
                "rationale": "Copper is displaced as a reddish-brown precipitate; the solution decolorizes or takes the color of metal B's ion.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) A displacement reaction occurs: the blue color of $\\text{CuSO}_4$ fades/discharges, and a reddish-brown deposit of copper forms on metal B.\n\nScientific Principle / Key Concept:\nMetal B displaces $\\text{Fe}$ from $\\text{FeSO}_4$, proving $\\text{Reactivity of B} > \\text{Fe}$. In the reactivity series, $\\text{Fe} > \\text{Cu}$. Thus, $\\text{B} > \\text{Cu}$. Therefore, when B is added to $\\text{CuSO}_4$, it displaces copper:\n• The characteristic blue color of $\\text{Cu}^{2+}(aq)$ fades.\n• Reddish-brown metallic copper is deposited on metal B.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Copper is below iron; B readily displaces it.\n• Option (C): Incorrect. $\\text{SO}_2$ is not evolved in aqueous displacement.\n• Option (D): Incorrect. Metallic copper is visibly precipitated.",
        "step_by_step_solution": "Correct Answer: (A) A displacement reaction occurs: the blue color of $\\text{CuSO}_4$ fades/discharges, and a reddish-brown deposit of copper forms on metal B.\n\nScientific Principle / Key Concept:\nMetal B displaces $\\text{Fe}$ from $\\text{FeSO}_4$, proving $\\text{Reactivity of B} > \\text{Fe}$. In the reactivity series, $\\text{Fe} > \\text{Cu}$. Thus, $\\text{B} > \\text{Cu}$. Therefore, when B is added to $\\text{CuSO}_4$, it displaces copper:\n• The characteristic blue color of $\\text{Cu}^{2+}(aq)$ fades.\n• Reddish-brown metallic copper is deposited on metal B.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Copper is below iron; B readily displaces it.\n• Option (C): Incorrect. $\\text{SO}_2$ is not evolved in aqueous displacement.\n• Option (D): Incorrect. Metallic copper is visibly precipitated.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 46)",
        "questionNumber": "3(ii)"
    },
    {
        "id": "sci_ch3_p46_q03_iii",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 46)",
        "question_number": "3(iii)",
        "text": "Based on the displacement data (B displaces Fe; A displaces Cu; C displaces Ag; D displaces none), what is the correct arrangement of metals A, B, C, and D in the order of decreasing reactivity?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{B} > \\text{A} > \\text{C} > \\text{D}$",
                "is_correct": True,
                "rationale": "B displaces Fe (above Cu); A displaces Cu (above Ag); C displaces Ag (low reactivity); D displaces nothing (least reactive). Thus: B > A > C > D.",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{A} > \\text{B} > \\text{C} > \\text{D}$",
                "is_correct": False,
                "rationale": "A cannot displace Fe, whereas B displaces Fe, so B > A.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$\\text{B} > \\text{D} > \\text{C} > \\text{A}$",
                "is_correct": False,
                "rationale": "D displaces no metal at all, so D is at the very bottom, not second.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{D} > \\text{C} > \\text{A} > \\text{B}$",
                "is_correct": False,
                "rationale": "This reverses the entire reactivity series.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) $\\text{B} > \\text{A} > \\text{C} > \\text{D}$\n\nScientific Principle / Key Concept:\nWe establish the relative reactivity of metals based on their displacement power:\n1. B displaces Fe, so $\\text{B} > \\text{Fe}$.\n2. A displaces Cu but not Fe, so $\\text{Fe} > \\text{A} > \\text{Cu}$.\n3. C displaces Ag but not Cu, so $\\text{Cu} > \\text{C} > \\text{Ag}$.\n4. D displaces none, so $\\text{Ag} > \\text{D}$.\nCombining these yields: $\\text{B} > \\text{A} > \\text{C} > \\text{D}$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. B is more reactive than A because B displaces Fe while A cannot.\n• Option (C): Incorrect. D is unreactive with all four solutions and is at the bottom.\n• Option (D): Incorrect. This is the inverted order (increasing reactivity).",
        "step_by_step_solution": "Correct Answer: (A) $\\text{B} > \\text{A} > \\text{C} > \\text{D}$\n\nScientific Principle / Key Concept:\nWe establish the relative reactivity of metals based on their displacement power:\n1. B displaces Fe, so $\\text{B} > \\text{Fe}$.\n2. A displaces Cu but not Fe, so $\\text{Fe} > \\text{A} > \\text{Cu}$.\n3. C displaces Ag but not Cu, so $\\text{Cu} > \\text{C} > \\text{Ag}$.\n4. D displaces none, so $\\text{Ag} > \\text{D}$.\nCombining these yields: $\\text{B} > \\text{A} > \\text{C} > \\text{D}$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. B is more reactive than A because B displaces Fe while A cannot.\n• Option (C): Incorrect. D is unreactive with all four solutions and is at the bottom.\n• Option (D): Incorrect. This is the inverted order (increasing reactivity).",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 46)",
        "questionNumber": "3(iii)"
    },
    {
        "id": "sci_ch3_p46_q04_a",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 46)",
        "question_number": "4(a)",
        "text": "Which gas is produced when dilute hydrochloric acid is added to a reactive metal?",
        "options": [
            {
                "id": "A",
                "text": "Hydrogen gas ($\\text{H}_2$)",
                "is_correct": True,
                "rationale": "Metals above hydrogen in the activity series displace $\\text{H}^+$ ions from dilute acids, producing hydrogen gas ($\\text{Metal} + \\text{Acid} \\rightarrow \\text{Salt} + \\text{H}_2\\uparrow$).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Chlorine gas ($\\text{Cl}_2$)",
                "is_correct": False,
                "rationale": "Chlorine is an oxidized species ($\text{Cl}^-$ to $\text{Cl}_2$); metals are reducing agents and reduce $\text{H}^+$, not oxidize chloride ions.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Oxygen gas ($\\text{O}_2$)",
                "is_correct": False,
                "rationale": "Hydrochloric acid does not contain oxygen; oxygen gas cannot be formed.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Hydrogen chloride gas ($\\text{HCl}$)",
                "is_correct": False,
                "rationale": "HCl is the reactant acid, not the evolved gas product.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Hydrogen gas ($\\text{H}_2$)\n\nScientific Principle / Key Concept:\nReactive metals (e.g., $\\text{Zn}, \\text{Fe}, \\text{Mg}$) displace hydrogen from dilute non-oxidizing acids like $\\text{HCl}$ and $\\text{H}_2\\text{SO}_4$, producing metal chloride/sulphate salts and evolving hydrogen gas ($\\text{H}_2$), which burns with a 'pop' sound.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Chlorine gas is not released when dilute $\\text{HCl}$ reacts with metals.\n• Option (C): Incorrect. $\\text{HCl}$ contains no oxygen atoms.\n• Option (D): Incorrect. Hydrogen chloride is the dissolved acid solute.",
        "step_by_step_solution": "Correct Answer: (A) Hydrogen gas ($\\text{H}_2$)\n\nScientific Principle / Key Concept:\nReactive metals (e.g., $\\text{Zn}, \\text{Fe}, \\text{Mg}$) displace hydrogen from dilute non-oxidizing acids like $\\text{HCl}$ and $\\text{H}_2\\text{SO}_4$, producing metal chloride/sulphate salts and evolving hydrogen gas ($\\text{H}_2$), which burns with a 'pop' sound.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Chlorine gas is not released when dilute $\\text{HCl}$ reacts with metals.\n• Option (C): Incorrect. $\\text{HCl}$ contains no oxygen atoms.\n• Option (D): Incorrect. Hydrogen chloride is the dissolved acid solute.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 46)",
        "questionNumber": "4(a)"
    },
    {
        "id": "sci_ch3_p46_q04_b",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 46)",
        "question_number": "4(b)",
        "text": "Write the chemical equation when iron reacts with dilute sulphuric acid ($\\text{H}_2\\text{SO}_4$).",
        "options": [
            {
                "id": "A",
                "text": "$\\text{Fe}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{FeSO}_4(aq) + \\text{H}_2(g)$",
                "is_correct": True,
                "rationale": "Iron reacts with dilute sulphuric acid forming ferrous sulphate (iron(II) sulphate, light green solution) and releasing hydrogen gas.",
                "correct": True
            },
            {
                "id": "B",
                "text": "$2\\text{Fe}(s) + 3\\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{Fe}_2(\\text{SO}_4)_3(aq) + 3\\text{H}_2(g)$",
                "is_correct": False,
                "rationale": "With dilute acid, iron oxidizes only to the $+2$ ferrous state ($\\text{FeSO}_4$), not the $+3$ ferric state.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$\\text{Fe}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{FeO}(s) + \\text{SO}_2(g) + \\text{H}_2\\text{O}(l)$",
                "is_correct": False,
                "rationale": "This represents the reaction with concentrated, hot oxidising sulphuric acid, not dilute acid.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{Fe}(s) + 2\\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{FeS}(s) + 2\\text{H}_2\\text{O}(l) + 2\\text{O}_2(g)$",
                "is_correct": False,
                "rationale": "Dilute acids do not undergo reduction to iron sulphide or liberate oxygen.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) $\\text{Fe}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{FeSO}_4(aq) + \\text{H}_2(g)$\n\nScientific Principle / Key Concept:\nIron lies above hydrogen in the activity series. It displaces $\\text{H}^+$ from dilute $\\text{H}_2\\text{SO}_4$ to form Iron(II) sulphate ($\\text{FeSO}_4$) and hydrogen gas:\n$$\\text{Fe}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{FeSO}_4(aq) + \\text{H}_2(g)$$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Dilute acid oxidizes Fe to $\\text{Fe}^{2+}$, not $\\text{Fe}^{3+}$.\n• Option (C): Incorrect. Hot concentrated sulphuric acid yields $\\text{SO}_2$, but dilute acid releases pure $\\text{H}_2$.\n• Option (D): Incorrect. Sulphide salts are not formed.",
        "step_by_step_solution": "Correct Answer: (A) $\\text{Fe}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{FeSO}_4(aq) + \\text{H}_2(g)$\n\nScientific Principle / Key Concept:\nIron lies above hydrogen in the activity series. It displaces $\\text{H}^+$ from dilute $\\text{H}_2\\text{SO}_4$ to form Iron(II) sulphate ($\\text{FeSO}_4$) and hydrogen gas:\n$$\\text{Fe}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{FeSO}_4(aq) + \\text{H}_2(g)$$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Dilute acid oxidizes Fe to $\\text{Fe}^{2+}$, not $\\text{Fe}^{3+}$.\n• Option (C): Incorrect. Hot concentrated sulphuric acid yields $\\text{SO}_2$, but dilute acid releases pure $\\text{H}_2$.\n• Option (D): Incorrect. Sulphide salts are not formed.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 46)",
        "questionNumber": "4(b)"
    },
    {
        "id": "sci_ch3_p46_q05",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 46)",
        "question_number": "5",
        "text": "What would you observe when zinc is added to a solution of iron(II) sulphate? Write the chemical reaction that takes place.",
        "options": [
            {
                "id": "A",
                "text": "The pale green color of $\\text{FeSO}_4$ solution gradually fades to colorless, and a greyish-black coating of iron metal is deposited on the zinc: $\\text{Zn}(s) + \\text{FeSO}_4(aq) \\rightarrow \\text{ZnSO}_4(aq) + \\text{Fe}(s)$.",
                "is_correct": True,
                "rationale": "Zinc is more reactive than iron (Zn > Fe). Zinc displaces iron, converting green $\\text{Fe}^{2+}$ into colorless $\\text{ZnSO}_4$ and precipitating grey metallic iron.",
                "correct": True
            },
            {
                "id": "B",
                "text": "No reaction takes place because iron sulphate is more reactive than zinc sulphate.",
                "is_correct": False,
                "rationale": "Zinc is above iron in the reactivity series, so a displacement reaction definitely occurs.",
                "correct": False
            },
            {
                "id": "C",
                "text": "The solution turns deep blue and reddish copper is deposited.",
                "is_correct": False,
                "rationale": "There is no copper present in the reactants.",
                "correct": False
            },
            {
                "id": "D",
                "text": "A vigorous reaction occurs releasing pungent $\\text{SO}_2$ gas and forming yellow zinc oxide.",
                "is_correct": False,
                "rationale": "Displacement in aqueous solution forms soluble $\\text{ZnSO}_4$ and solid iron, not $\\text{SO}_2$ gas.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) The pale green color of $\\text{FeSO}_4$ solution gradually fades to colorless, and a greyish-black coating of iron metal is deposited on the zinc: $\\text{Zn}(s) + \\text{FeSO}_4(aq) \\rightarrow \\text{ZnSO}_4(aq) + \\text{Fe}(s)$.\n\nScientific Principle / Key Concept:\nZinc is higher than iron in the reactivity series ($\\text{Zn} > \\text{Fe}$). When zinc strips are placed into pale green iron(II) sulphate solution, zinc displaces iron:\n$$\\text{Zn}(s) + \\text{FeSO}_4(aq) \\rightarrow \\text{ZnSO}_4(aq) + \\text{Fe}(s)$$\nObservations:\n1. The pale green solution of $\\text{FeSO}_4$ turns colorless due to formation of $\\text{ZnSO}_4$.\n2. Greyish-black iron metal precipitates onto the surface of the zinc strip.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Zn is more reactive than Fe, so displacement occurs.\n• Option (C): Incorrect. Copper is not involved.\n• Option (D): Incorrect. $\\text{SO}_2$ is not formed.",
        "step_by_step_solution": "Correct Answer: (A) The pale green color of $\\text{FeSO}_4$ solution gradually fades to colorless, and a greyish-black coating of iron metal is deposited on the zinc: $\\text{Zn}(s) + \\text{FeSO}_4(aq) \\rightarrow \\text{ZnSO}_4(aq) + \\text{Fe}(s)$.\n\nScientific Principle / Key Concept:\nZinc is higher than iron in the reactivity series ($\\text{Zn} > \\text{Fe}$). When zinc strips are placed into pale green iron(II) sulphate solution, zinc displaces iron:\n$$\\text{Zn}(s) + \\text{FeSO}_4(aq) \\rightarrow \\text{ZnSO}_4(aq) + \\text{Fe}(s)$$\nObservations:\n1. The pale green solution of $\\text{FeSO}_4$ turns colorless due to formation of $\\text{ZnSO}_4$.\n2. Greyish-black iron metal precipitates onto the surface of the zinc strip.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Zn is more reactive than Fe, so displacement occurs.\n• Option (C): Incorrect. Copper is not involved.\n• Option (D): Incorrect. $\\text{SO}_2$ is not formed.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 46)",
        "questionNumber": "5"
    },

    # ==================== PAGE 49: QUESTIONS ====================
    {
        "id": "sci_ch3_p49_q01_i",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 49)",
        "question_number": "1(i)",
        "text": "What are the numbers of valence electrons represented in the electron-dot structures for Sodium ($\\text{Na}$, $Z=11$), Oxygen ($\\text{O}$, $Z=8$), and Magnesium ($\\text{Mg}$, $Z=12$)?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{Na}$: 1 dot, $\\text{O}$: 6 dots, $\\text{Mg}$: 2 dots",
                "is_correct": True,
                "rationale": "Electronic configurations: Na = 2, 8, 1 (1 valence electron); O = 2, 6 (6 valence electrons); Mg = 2, 8, 2 (2 valence electrons). Electron-dot symbols show only valence electrons.",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{Na}$: 11 dots, $\\text{O}$: 8 dots, $\\text{Mg}$: 12 dots",
                "is_correct": False,
                "rationale": "Electron-dot (Lewis) structures show only outermost valence shell electrons, not the total atomic number of electrons.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$\\text{Na}$: 8 dots, $\\text{O}$: 2 dots, $\\text{Mg}$: 8 dots",
                "is_correct": False,
                "rationale": "This confuses the inner noble core or valency with valence shell electrons.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{Na}$: 1 dot, $\\text{O}$: 2 dots, $\\text{Mg}$: 2 dots",
                "is_correct": False,
                "rationale": "Oxygen has 6 valence electrons, although its valency is 2.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) $\\text{Na}$: 1 dot, $\\text{O}$: 6 dots, $\\text{Mg}$: 2 dots\n\nScientific Principle / Key Concept:\nElectron-dot structures represent only the valence electrons (electrons in the outermost shell):\n1. Sodium ($\\text{Na}, Z=11$): Electronic configuration is $2, 8, 1 \\rightarrow 1$ valence electron ($\\text{Na}\\cdot$).\n2. Oxygen ($\\text{O}, Z=8$): Electronic configuration is $2, 6 \\rightarrow 6$ valence electrons ($\\cdot\\ddot{\\text{O}}\\cdot$).\n3. Magnesium ($\\text{Mg}, Z=12$): Electronic configuration is $2, 8, 2 \\rightarrow 2$ valence electrons ($\\cdot\\text{Mg}\\cdot$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Total electrons are never drawn in Lewis dot diagrams.\n• Option (C): Incorrect. Innermost octets are omitted.\n• Option (D): Incorrect. 2 is oxygen's valency, but its Lewis structure has 6 valence electrons.",
        "step_by_step_solution": "Correct Answer: (A) $\\text{Na}$: 1 dot, $\\text{O}$: 6 dots, $\\text{Mg}$: 2 dots\n\nScientific Principle / Key Concept:\nElectron-dot structures represent only the valence electrons (electrons in the outermost shell):\n1. Sodium ($\\text{Na}, Z=11$): Electronic configuration is $2, 8, 1 \\rightarrow 1$ valence electron ($\\text{Na}\\cdot$).\n2. Oxygen ($\\text{O}, Z=8$): Electronic configuration is $2, 6 \\rightarrow 6$ valence electrons ($\\cdot\\ddot{\\text{O}}\\cdot$).\n3. Magnesium ($\\text{Mg}, Z=12$): Electronic configuration is $2, 8, 2 \\rightarrow 2$ valence electrons ($\\cdot\\text{Mg}\\cdot$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Total electrons are never drawn in Lewis dot diagrams.\n• Option (C): Incorrect. Innermost octets are omitted.\n• Option (D): Incorrect. 2 is oxygen's valency, but its Lewis structure has 6 valence electrons.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 49)",
        "questionNumber": "1(i)"
    },
    {
        "id": "sci_ch3_p49_q01_ii_a",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 49)",
        "question_number": "1(ii)(a)",
        "text": "How is sodium oxide ($\\text{Na}_2\\text{O}$) formed by the transfer of electrons?",
        "options": [
            {
                "id": "A",
                "text": "Two sodium atoms lose one electron each to a single oxygen atom, forming two $\\text{Na}^+$ cations and one oxide anion $[\\text{O}]^{2-}$.",
                "is_correct": True,
                "rationale": "Each Na atom ($2,8,1$) donates 1 electron to attain neon octet ($2,8$). Oxygen ($2,6$) requires 2 electrons to complete its octet ($2,8$). Hence, 2 Na atoms transfer 2 electrons in total to 1 O atom, yielding $(\\text{Na}^+)_2[\\text{O}]^{2-}$.",
                "correct": True
            },
            {
                "id": "B",
                "text": "One sodium atom loses two electrons to an oxygen atom, forming $\\text{Na}^{2+}$ and $\\text{O}^{2-}$.",
                "is_correct": False,
                "rationale": "Sodium has only 1 valence electron and cannot form a stable $\\text{Na}^{2+}$ ion under standard chemical conditions.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Two sodium atoms share two pairs of electrons with one oxygen atom to form covalent bonds.",
                "is_correct": False,
                "rationale": "$\\text{Na}_2\\text{O}$ is an electrovalent (ionic) compound formed by complete electron transfer, not by electron sharing.",
                "correct": False
            },
            {
                "id": "D",
                "text": "An oxygen atom donates two electrons to two sodium atoms, creating $\\text{O}^{2+}$ and two $\\text{Na}^-$ ions.",
                "is_correct": False,
                "rationale": "Oxygen is highly electronegative and accepts electrons, while electropositive sodium donates electrons.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Two sodium atoms lose one electron each to a single oxygen atom, forming two $\\text{Na}^+$ cations and one oxide anion $[\\text{O}]^{2-}$.\n\nScientific Principle / Key Concept:\nFormation of $\\text{Na}_2\\text{O}$:\n1. Sodium ($\\text{Na}, 2,8,1 \\rightarrow \\text{Na}^+ + e^-$). Two sodium atoms lose $2 \\times 1 = 2$ electrons.\n2. Oxygen ($\\text{O}, 2,6 + 2e^- \\rightarrow [\\text{O}]^{2-}, 2,8$).\n3. Oppositely charged ions attract via strong electrostatic forces to form $(\\text{Na}^+)_2[\\text{O}]^{2-}$ or $\\text{Na}_2\\text{O}$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Sodium has only 1 valence electron and does not form $\\text{Na}^{2+}$.\n• Option (C): Incorrect. It is an ionic compound, not covalent.\n• Option (D): Incorrect. Metals donate electrons; oxygen gains them.",
        "step_by_step_solution": "Correct Answer: (A) Two sodium atoms lose one electron each to a single oxygen atom, forming two $\\text{Na}^+$ cations and one oxide anion $[\\text{O}]^{2-}$.\n\nScientific Principle / Key Concept:\nFormation of $\\text{Na}_2\\text{O}$:\n1. Sodium ($\\text{Na}, 2,8,1 \\rightarrow \\text{Na}^+ + e^-$). Two sodium atoms lose $2 \\times 1 = 2$ electrons.\n2. Oxygen ($\\text{O}, 2,6 + 2e^- \\rightarrow [\\text{O}]^{2-}, 2,8$).\n3. Oppositely charged ions attract via strong electrostatic forces to form $(\\text{Na}^+)_2[\\text{O}]^{2-}$ or $\\text{Na}_2\\text{O}$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Sodium has only 1 valence electron and does not form $\\text{Na}^{2+}$.\n• Option (C): Incorrect. It is an ionic compound, not covalent.\n• Option (D): Incorrect. Metals donate electrons; oxygen gains them.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 49)",
        "questionNumber": "1(ii)(a)"
    },
    {
        "id": "sci_ch3_p49_q01_ii_b",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 49)",
        "question_number": "1(ii)(b)",
        "text": "How is magnesium oxide ($\\text{MgO}$) formed by electron transfer?",
        "options": [
            {
                "id": "A",
                "text": "One magnesium atom transfers two valence electrons to an oxygen atom, forming $\\text{Mg}^{2+}$ and $[\\text{O}]^{2-}$.",
                "is_correct": True,
                "rationale": "Magnesium ($2,8,2$) loses 2 electrons to form $\\text{Mg}^{2+}$ ($2,8$), and oxygen ($2,6$) gains these 2 electrons to form $\\text{O}^{2-}$ ($2,8$). The electrostatic attraction between $\\text{Mg}^{2+}$ and $\\text{O}^{2-}$ yields $\\text{MgO}$.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Two magnesium atoms transfer one electron each to one oxygen atom, forming $\\text{Mg}_2\\text{O}$.",
                "is_correct": False,
                "rationale": "Magnesium has 2 valence electrons; one atom suffices to supply both electrons required by an oxygen atom.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Magnesium and oxygen share a double covalent bond to complete their octets.",
                "is_correct": False,
                "rationale": "$\\text{MgO}$ has a massive electronegativity difference between alkaline earth metal and oxygen, resulting in an ionic crystal lattice, not a molecular covalent bond.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Magnesium loses one electron to form $\\text{Mg}^+$ and oxygen gains one to form $\\text{O}^-$.",
                "is_correct": False,
                "rationale": "Stable octet configurations require $\\text{Mg}^{2+}$ and $\\text{O}^{2-}$.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) One magnesium atom transfers two valence electrons to an oxygen atom, forming $\\text{Mg}^{2+}$ and $[\\text{O}]^{2-}$.\n\nScientific Principle / Key Concept:\nFormation of $\\text{MgO}$:\n1. $\\text{Mg} (2,8,2) \\rightarrow \\text{Mg}^{2+} (2,8) + 2e^-$\n2. $\\text{O} (2,6) + 2e^- \\rightarrow [\\text{O}]^{2-} (2,8)$\n3. The strong electrostatic attraction between $\\text{Mg}^{2+}$ and $[\\text{O}]^{2-}$ forms the ionic solid $\\text{MgO}$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. The formula of magnesium oxide is $\\text{MgO}$, not $\\text{Mg}_2\\text{O}$.\n• Option (C): Incorrect. Bonding is ionic (electrovalent), not covalent.\n• Option (D): Incorrect. The stable ionic charges are $+2$ and $-2$.",
        "step_by_step_solution": "Correct Answer: (A) One magnesium atom transfers two valence electrons to an oxygen atom, forming $\\text{Mg}^{2+}$ and $[\\text{O}]^{2-}$.\n\nScientific Principle / Key Concept:\nFormation of $\\text{MgO}$:\n1. $\\text{Mg} (2,8,2) \\rightarrow \\text{Mg}^{2+} (2,8) + 2e^-$\n2. $\\text{O} (2,6) + 2e^- \\rightarrow [\\text{O}]^{2-} (2,8)$\n3. The strong electrostatic attraction between $\\text{Mg}^{2+}$ and $[\\text{O}]^{2-}$ forms the ionic solid $\\text{MgO}$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. The formula of magnesium oxide is $\\text{MgO}$, not $\\text{Mg}_2\\text{O}$.\n• Option (C): Incorrect. Bonding is ionic (electrovalent), not covalent.\n• Option (D): Incorrect. The stable ionic charges are $+2$ and $-2$.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 49)",
        "questionNumber": "1(ii)(b)"
    },
    {
        "id": "sci_ch3_p49_q01_iii",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 49)",
        "question_number": "1(iii)",
        "text": "What are the exact ions present in the compounds sodium oxide ($\\text{Na}_2\\text{O}$) and magnesium oxide ($\\text{MgO}$)?",
        "options": [
            {
                "id": "A",
                "text": "In $\\text{Na}_2\\text{O}$: $\\text{Na}^+$ and $\\text{O}^{2-}$; in $\\text{MgO}$: $\\text{Mg}^{2+}$ and $\\text{O}^{2-}$",
                "is_correct": True,
                "rationale": "Sodium forms univalent sodium cations ($\\text{Na}^+$), magnesium forms divalent magnesium cations ($\\text{Mg}^{2+}$), and oxygen forms divalent oxide anions ($\\text{O}^{2-}$).",
                "correct": True
            },
            {
                "id": "B",
                "text": "In $\\text{Na}_2\\text{O}$: $\\text{Na}^{2+}$ and $\\text{O}^-$; in $\\text{MgO}$: $\\text{Mg}^+$ and $\\text{O}^-$",
                "is_correct": False,
                "rationale": "These incorrect valency states violate the octet rule.",
                "correct": False
            },
            {
                "id": "C",
                "text": "In $\\text{Na}_2\\text{O}$: $\\text{Na}^+$ and $\\text{O}_2^{2-}$; in $\\text{MgO}$: $\\text{Mg}^{2+}$ and $\\text{O}_2^{2-}$",
                "is_correct": False,
                "rationale": "$\\text{O}_2^{2-}$ is the peroxide ion; the given compounds are normal oxides containing the $\\text{O}^{2-}$ ion.",
                "correct": False
            },
            {
                "id": "D",
                "text": "In $\\text{Na}_2\\text{O}$: $\\text{Na}_2^+$ and $\\text{O}^{2-}$; in $\\text{MgO}$: $\\text{Mg}^{2+}$ and $\\text{O}^-$",
                "is_correct": False,
                "rationale": "Sodium exists as discrete individual $\\text{Na}^+$ ions, not diatomic polyatomic ions.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) In $\\text{Na}_2\\text{O}$: $\\text{Na}^+$ and $\\text{O}^{2-}$; in $\\text{MgO}$: $\\text{Mg}^{2+}$ and $\\text{O}^{2-}$\n\nScientific Principle / Key Concept:\n• In $\\text{Na}_2\\text{O}$: The ions are Sodium cations ($\\text{Na}^+$) and Oxide anions ($\\text{O}^{2-}$), present in a $2:1$ ratio.\n• In $\\text{MgO}$: The ions are Magnesium cations ($\\text{Mg}^{2+}$) and Oxide anions ($\\text{O}^{2-}$), present in a $1:1$ ratio.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect charges.\n• Option (C): Incorrect. These are oxides, not peroxides.\n• Option (D): Incorrect formula representations.",
        "step_by_step_solution": "Correct Answer: (A) In $\\text{Na}_2\\text{O}$: $\\text{Na}^+$ and $\\text{O}^{2-}$; in $\\text{MgO}$: $\\text{Mg}^{2+}$ and $\\text{O}^{2-}$\n\nScientific Principle / Key Concept:\n• In $\\text{Na}_2\\text{O}$: The ions are Sodium cations ($\\text{Na}^+$) and Oxide anions ($\\text{O}^{2-}$), present in a $2:1$ ratio.\n• In $\\text{MgO}$: The ions are Magnesium cations ($\\text{Mg}^{2+}$) and Oxide anions ($\\text{O}^{2-}$), present in a $1:1$ ratio.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect charges.\n• Option (C): Incorrect. These are oxides, not peroxides.\n• Option (D): Incorrect formula representations.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 49)",
        "questionNumber": "1(iii)"
    },
    {
        "id": "sci_ch3_p49_q02",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 49)",
        "question_number": "2",
        "text": "Why do ionic compounds have remarkably high melting points?",
        "options": [
            {
                "id": "A",
                "text": "A tremendous amount of thermal energy is required to overcome the strong electrostatic inter-ionic attractions holding the crystal lattice together.",
                "is_correct": True,
                "rationale": "Ionic compounds form 3D crystalline giant lattices held by intense omnidirectional electrostatic attractions between oppositely charged cations and anions, requiring substantial thermal energy to disrupt.",
                "correct": True
            },
            {
                "id": "B",
                "text": "They consist of heavy metallic molecules held by strong covalent double bonds.",
                "is_correct": False,
                "rationale": "Ionic compounds do not contain discrete molecules or covalent bonds; they consist of ions in an electrostatic lattice.",
                "correct": False
            },
            {
                "id": "C",
                "text": "They have strong intermolecular hydrogen bonds between molecules.",
                "is_correct": False,
                "rationale": "Hydrogen bonds exist between polar covalent molecules (e.g., $\\text{H}_2\\text{O}$), not ionic salts like $\\text{NaCl}$ or $\\text{MgO}$.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Their free mobile electrons absorb heat without allowing the solid to expand.",
                "is_correct": False,
                "rationale": "Solid ionic compounds have no mobile free electrons; all electrons are localized in complete valence octets.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) A tremendous amount of thermal energy is required to overcome the strong electrostatic inter-ionic attractions holding the crystal lattice together.\n\nScientific Principle / Key Concept:\nIonic compounds are composed of oppositely charged ions arranged in a regular, three-dimensional crystal lattice. The electrostatic forces of attraction between positive cations and negative anions are exceptionally strong. Consequently, a considerable amount of thermal energy (high temperature) is required to break these ionic bonds and melt the compound.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. They do not consist of discrete molecules or covalent bonds.\n• Option (C): Incorrect. Hydrogen bonding applies to specific molecular substances, not ionic salts.\n• Option (D): Incorrect. Solid ionic compounds do not have free electrons.",
        "step_by_step_solution": "Correct Answer: (A) A tremendous amount of thermal energy is required to overcome the strong electrostatic inter-ionic attractions holding the crystal lattice together.\n\nScientific Principle / Key Concept:\nIonic compounds are composed of oppositely charged ions arranged in a regular, three-dimensional crystal lattice. The electrostatic forces of attraction between positive cations and negative anions are exceptionally strong. Consequently, a considerable amount of thermal energy (high temperature) is required to break these ionic bonds and melt the compound.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. They do not consist of discrete molecules or covalent bonds.\n• Option (C): Incorrect. Hydrogen bonding applies to specific molecular substances, not ionic salts.\n• Option (D): Incorrect. Solid ionic compounds do not have free electrons.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 49)",
        "questionNumber": "2"
    },

    # ==================== PAGE 53: QUESTIONS ====================
    {
        "id": "sci_ch3_p53_q01_i",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 53)",
        "question_number": "1(i)",
        "text": "What is the precise scientific definition of a 'Mineral' in geology and metallurgy?",
        "options": [
            {
                "id": "A",
                "text": "Naturally occurring inorganic elements or compounds found naturally in the Earth's crust",
                "is_correct": True,
                "rationale": "Minerals are natural inorganic chemical substances having definite or characteristic chemical compositions and crystalline structures found in the Earth's crust.",
                "correct": True
            },
            {
                "id": "B",
                "text": "A synthetic metal alloy prepared in blast furnaces for commercial fabrication",
                "is_correct": False,
                "rationale": "Alloys are man-made homogeneous mixtures, not naturally occurring geological minerals.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Only those specific rocks from which a metal can be extracted with high economic profit",
                "is_correct": False,
                "rationale": "Minerals from which metals can be extracted profitably are specifically called ores.",
                "correct": False
            },
            {
                "id": "D",
                "text": "The unwanted sandy, clayey waste material separated from crushed rocks",
                "is_correct": False,
                "rationale": "Unwanted waste material associated with ore is called gangue or matrix.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Naturally occurring inorganic elements or compounds found naturally in the Earth's crust\n\nScientific Principle / Key Concept:\nThe elements or compounds which occur naturally in the earth’s crust are known as minerals. All ores are minerals, but not all minerals are ores.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Synthetic alloys are artificial, not geological minerals.\n• Option (C): Incorrect. This describes an ore.\n• Option (D): Incorrect. This describes gangue.",
        "step_by_step_solution": "Correct Answer: (A) Naturally occurring inorganic elements or compounds found naturally in the Earth's crust\n\nScientific Principle / Key Concept:\nThe elements or compounds which occur naturally in the earth’s crust are known as minerals. All ores are minerals, but not all minerals are ores.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Synthetic alloys are artificial, not geological minerals.\n• Option (C): Incorrect. This describes an ore.\n• Option (D): Incorrect. This describes gangue.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 53)",
        "questionNumber": "1(i)"
    },
    {
        "id": "sci_ch3_p53_q01_ii",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 53)",
        "question_number": "1(ii)",
        "text": "What is the defining criterion that distinguishes an 'Ore' from an ordinary mineral?",
        "options": [
            {
                "id": "A",
                "text": "It contains a particularly high percentage of a metal that can be extracted conveniently and profitably on a commercial scale.",
                "is_correct": True,
                "rationale": "An ore is a mineral having sufficiently high metal concentration such that extracting the metal is technologically viable and commercially profitable.",
                "correct": True
            },
            {
                "id": "B",
                "text": "It is completely free of any sand, rock, or silica contamination.",
                "is_correct": False,
                "rationale": "All natural ores are contaminated with gangue (sand, clay, rock) that must be removed during concentration.",
                "correct": False
            },
            {
                "id": "C",
                "text": "It must contain at least three different precious metals in equal proportions.",
                "is_correct": False,
                "rationale": "Ores are typically mined for one primary target metal (e.g., bauxite for aluminium, haematite for iron).",
                "correct": False
            },
            {
                "id": "D",
                "text": "It can only be processed using electrolysis without requiring heating or roasting.",
                "is_correct": False,
                "rationale": "Many ores are extracted by smelting, roasting, calcination, or carbon reduction, not just electrolysis.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) It contains a particularly high percentage of a metal that can be extracted conveniently and profitably on a commercial scale.\n\nScientific Principle / Key Concept:\nAt some places, minerals contain a very high percentage of a particular metal and the metal can be profitably extracted from it. These minerals are called ores. Thus, all ores are minerals, but not all minerals are ores.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Natural ores invariably contain gangue.\n• Option (C): Incorrect. Ores are mined for a specific target metal.\n• Option (D): Incorrect. Smelting and chemical reduction are widely used for ores of moderate reactivity.",
        "step_by_step_solution": "Correct Answer: (A) It contains a particularly high percentage of a metal that can be extracted conveniently and profitably on a commercial scale.\n\nScientific Principle / Key Concept:\nAt some places, minerals contain a very high percentage of a particular metal and the metal can be profitably extracted from it. These minerals are called ores. Thus, all ores are minerals, but not all minerals are ores.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Natural ores invariably contain gangue.\n• Option (C): Incorrect. Ores are mined for a specific target metal.\n• Option (D): Incorrect. Smelting and chemical reduction are widely used for ores of moderate reactivity.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 53)",
        "questionNumber": "1(ii)"
    },
    {
        "id": "sci_ch3_p53_q01_iii",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 53)",
        "question_number": "1(iii)",
        "text": "What is meant by the term 'Gangue' in metallurgical processes?",
        "options": [
            {
                "id": "A",
                "text": "Undesirable earthly and siliceous impurities like sand, clay, and rocky matter associated with mined ores",
                "is_correct": True,
                "rationale": "Ores mined from the earth are contaminated with large amounts of impurities such as soil, sand, limestone, and rocky debris, collectively termed gangue.",
                "correct": True
            },
            {
                "id": "B",
                "text": "The chemical flux added to dissolve high melting impurities in a blast furnace",
                "is_correct": False,
                "rationale": "Chemical substances added to remove gangue are called fluxes (e.g., $\\text{CaO}, \\text{SiO}_2$), producing slag.",
                "correct": False
            },
            {
                "id": "C",
                "text": "The molten pure metal collected at the base of an electrolytic reduction cell",
                "is_correct": False,
                "rationale": "The pure metal is the final product, not gangue.",
                "correct": False
            },
            {
                "id": "D",
                "text": "The gaseous exhaust released during roasting and calcination",
                "is_correct": False,
                "rationale": "Gaseous exhaust (like $\\text{SO}_2, \\text{CO}_2$) is flue gas, not gangue.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Undesirable earthly and siliceous impurities like sand, clay, and rocky matter associated with mined ores\n\nScientific Principle / Key Concept:\nOres mined from the earth are usually contaminated with large amounts of impurities such as soil, sand, clay, etc., called gangue. The gangue must be removed from the ore prior to the extraction of the metal based on differences between physical or chemical properties of gangue and ore.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Flux is the substance added to react with gangue.\n• Option (C): Incorrect. Pure metal is the extracted commodity.\n• Option (D): Incorrect. Gaseous byproducts are flue gases.",
        "step_by_step_solution": "Correct Answer: (A) Undesirable earthly and siliceous impurities like sand, clay, and rocky matter associated with mined ores\n\nScientific Principle / Key Concept:\nOres mined from the earth are usually contaminated with large amounts of impurities such as soil, sand, clay, etc., called gangue. The gangue must be removed from the ore prior to the extraction of the metal based on differences between physical or chemical properties of gangue and ore.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Flux is the substance added to react with gangue.\n• Option (C): Incorrect. Pure metal is the extracted commodity.\n• Option (D): Incorrect. Gaseous byproducts are flue gases.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 53)",
        "questionNumber": "1(iii)"
    },
    {
        "id": "sci_ch3_p53_q02",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 53)",
        "question_number": "2",
        "text": "Which pair of metals are found in nature predominantly in the native (free uncombined) state?",
        "options": [
            {
                "id": "A",
                "text": "Gold ($\\text{Au}$) and Platinum ($\\text{Pt}$)",
                "is_correct": True,
                "rationale": "Gold and platinum lie at the very bottom of the reactivity series. They are the least reactive noble metals and do not easily combine with oxygen, moisture, or carbon dioxide, occurring naturally in native metallic form.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Sodium ($\\text{Na}$) and Potassium ($\\text{K}$)",
                "is_correct": False,
                "rationale": "Sodium and potassium are top of the reactivity series and are never found in native free state; they occur as chlorides, carbonates, or nitrates.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Iron ($\\text{Fe}$) and Zinc ($\\text{Zn}$)",
                "is_correct": False,
                "rationale": "Iron and zinc have moderate reactivity and are found as oxides, carbonates, or sulphides (e.g., haematite, zinc blende).",
                "correct": False
            },
            {
                "id": "D",
                "text": "Aluminium ($\\text{Al}$) and Magnesium ($\\text{Mg}$)",
                "is_correct": False,
                "rationale": "Highly electropositive metals that occur strictly as combined oxides, carbonates, or silicates (e.g., bauxite).",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Gold ($\\text{Au}$) and Platinum ($\\text{Pt}$)\n\nScientific Principle / Key Concept:\nThe metals that are at the bottom of the activity series are the least reactive. They are often found in a free state. For example, gold ($\\text{Au}$), platinum ($\\text{Pt}$), and silver ($\\text{Ag}$) are found in the free state (silver and copper are also found in the combined state as sulphide or oxide ores).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Alkali metals are extremely reactive and occur only in combined forms.\n• Option (C): Incorrect. Iron and zinc occur as oxides/sulphides.\n• Option (D): Incorrect. Aluminium and magnesium have strong affinity for oxygen.",
        "step_by_step_solution": "Correct Answer: (A) Gold ($\\text{Au}$) and Platinum ($\\text{Pt}$)\n\nScientific Principle / Key Concept:\nThe metals that are at the bottom of the activity series are the least reactive. They are often found in a free state. For example, gold ($\\text{Au}$), platinum ($\\text{Pt}$), and silver ($\\text{Ag}$) are found in the free state (silver and copper are also found in the combined state as sulphide or oxide ores).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Alkali metals are extremely reactive and occur only in combined forms.\n• Option (C): Incorrect. Iron and zinc occur as oxides/sulphides.\n• Option (D): Incorrect. Aluminium and magnesium have strong affinity for oxygen.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 53)",
        "questionNumber": "2"
    },
    {
        "id": "sci_ch3_p53_q03",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 53)",
        "question_number": "3",
        "text": "What chemical process is generally used for obtaining a moderately reactive metal from its oxide?",
        "options": [
            {
                "id": "A",
                "text": "Reduction using carbon (coke) or a more reactive displacement metal like aluminium powder",
                "is_correct": True,
                "rationale": "Metal oxides of moderate reactivity (e.g., $\\text{ZnO}, \\text{Fe}_2\\text{O}_3, \\text{PbO}$) are reduced to free metals by heating with carbon/coke ($\\text{ZnO} + \\text{C} \\rightarrow \\text{Zn} + \\text{CO}$) or by displacement reduction using highly reactive metals like aluminium (thermite reaction).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Oxidation by passing a steady stream of hot air or oxygen through the oxide",
                "is_correct": False,
                "rationale": "The metal in the metal oxide is already in an oxidized state; extracting the elemental metal requires removal of oxygen (reduction), not oxidation.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Hydration by dissolving the oxide in excess distilled water at room temperature",
                "is_correct": False,
                "rationale": "Hydration forms basic metal hydroxides, not elemental zero-valent metals.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Roasting by heating in excess oxygen gas",
                "is_correct": False,
                "rationale": "Roasting is used to convert sulphide ores into oxides, not to extract elemental metal from an oxide.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Reduction using carbon (coke) or a more reactive displacement metal like aluminium powder\n\nScientific Principle / Key Concept:\nObtaining a metal from its oxide involves the chemical removal of oxygen, which is a reduction reaction:\n1. Reduction with Carbon: $\\text{ZnO}(s) + \\text{C}(s) \\rightarrow \\text{Zn}(s) + \\text{CO}(g)$.\n2. Reduction with reactive metals (displacement): Highly reactive metals like $\\text{Na}, \\text{Ca}, \\text{Al}$ act as reducing agents because they displace metals of lower reactivity from their oxides (e.g., Thermite process: $3\\text{MnO}_2 + 4\\text{Al} \\rightarrow 3\\text{Mn} + 2\\text{Al}_2\\text{O}_3 + \\text{Heat}$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Oxidation adds oxygen, whereas extraction requires removing oxygen.\n• Option (C): Incorrect. Hydration produces metal hydroxides.\n• Option (D): Incorrect. Roasting converts sulphides into oxides.",
        "step_by_step_solution": "Correct Answer: (A) Reduction using carbon (coke) or a more reactive displacement metal like aluminium powder\n\nScientific Principle / Key Concept:\nObtaining a metal from its oxide involves the chemical removal of oxygen, which is a reduction reaction:\n1. Reduction with Carbon: $\\text{ZnO}(s) + \\text{C}(s) \\rightarrow \\text{Zn}(s) + \\text{CO}(g)$.\n2. Reduction with reactive metals (displacement): Highly reactive metals like $\\text{Na}, \\text{Ca}, \\text{Al}$ act as reducing agents because they displace metals of lower reactivity from their oxides (e.g., Thermite process: $3\\text{MnO}_2 + 4\\text{Al} \\rightarrow 3\\text{Mn} + 2\\text{Al}_2\\text{O}_3 + \\text{Heat}$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Oxidation adds oxygen, whereas extraction requires removing oxygen.\n• Option (C): Incorrect. Hydration produces metal hydroxides.\n• Option (D): Incorrect. Roasting converts sulphides into oxides.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 53)",
        "questionNumber": "3"
    },

    # ==================== PAGE 55: QUESTIONS ====================
    {
        "id": "sci_ch3_p55_q01",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 55)",
        "question_number": "1",
        "text": "Metallic oxides of Zinc oxide ($\\text{ZnO}$), Magnesium oxide ($\\text{MgO}$), and Copper oxide ($\\text{CuO}$) were heated separately with Zinc, Magnesium, and Copper. In which cases will displacement reactions take place?",
        "options": [
            {
                "id": "A",
                "text": "Magnesium displaces both $\\text{ZnO}$ and $\\text{CuO}$; Zinc displaces only $\\text{CuO}$; Copper displaces none.",
                "is_correct": True,
                "rationale": "Reactivity order is $\\text{Mg} > \\text{Zn} > \\text{Cu}$. Mg is more reactive than Zn and Cu, so it reduces $\\text{ZnO}$ and $\\text{CuO}$. Zn is more reactive than Cu, reducing $\\text{CuO}$. Cu cannot reduce $\\text{ZnO}$ or $\\text{MgO}$.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Copper displaces both $\\text{ZnO}$ and $\\text{MgO}$; Zinc displaces $\\text{MgO}$; Magnesium displaces none.",
                "is_correct": False,
                "rationale": "Copper is the least reactive of the three and cannot reduce oxides of zinc or magnesium.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Displacement occurs in all nine combinations because metal oxides readily decompose on heating with any metal.",
                "is_correct": False,
                "rationale": "Displacement strictly requires the free metal to be more reactive than the metal in the oxide.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Zinc displaces $\\text{MgO}$ and $\\text{CuO}$; Magnesium displaces only $\\text{ZnO}$; Copper displaces $\\text{ZnO}$.",
                "is_correct": False,
                "rationale": "Zinc is less reactive than magnesium and cannot reduce magnesium oxide.",
                "correct": False
            }
        ],
        "difficulty": "hard",
        "solution": "Correct Answer: (A) Magnesium displaces both $\\text{ZnO}$ and $\\text{CuO}$; Zinc displaces only $\\text{CuO}$; Copper displaces none.\n\nScientific Principle / Key Concept:\nA displacement reaction occurs if the heating metal is more electropositive (more reactive) than the metal cation in the oxide. Reactivity series: $\\text{Mg} > \\text{Zn} > \\text{Cu}$.\n1. With $\\text{ZnO}$: Only $\\text{Mg}$ will displace $\\text{Zn}$ ($\\text{Mg} + \\text{ZnO} \\rightarrow \\text{MgO} + \\text{Zn}$).\n2. With $\\text{MgO}$: No displacement (neither $\\text{Zn}$ nor $\\text{Cu}$ is more reactive than $\\text{Mg}$).\n3. With $\\text{CuO}$: Both $\\text{Mg}$ and $\\text{Zn}$ will displace $\\text{Cu}$ ($\\text{Mg} + \\text{CuO} \\rightarrow \\text{MgO} + \\text{Cu}$; $\\text{Zn} + \\text{CuO} \\rightarrow \\text{ZnO} + \\text{Cu}$).\n4. Copper is less reactive than both $\\text{Mg}$ and $\\text{Zn}$, so it shows no reaction.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Inverts the reactivity series.\n• Option (C): Incorrect. A less reactive metal cannot displace a more reactive metal.\n• Option (D): Zn cannot displace Mg from MgO.",
        "step_by_step_solution": "Correct Answer: (A) Magnesium displaces both $\\text{ZnO}$ and $\\text{CuO}$; Zinc displaces only $\\text{CuO}$; Copper displaces none.\n\nScientific Principle / Key Concept:\nA displacement reaction occurs if the heating metal is more electropositive (more reactive) than the metal cation in the oxide. Reactivity series: $\\text{Mg} > \\text{Zn} > \\text{Cu}$.\n1. With $\\text{ZnO}$: Only $\\text{Mg}$ will displace $\\text{Zn}$ ($\\text{Mg} + \\text{ZnO} \\rightarrow \\text{MgO} + \\text{Zn}$).\n2. With $\\text{MgO}$: No displacement (neither $\\text{Zn}$ nor $\\text{Cu}$ is more reactive than $\\text{Mg}$).\n3. With $\\text{CuO}$: Both $\\text{Mg}$ and $\\text{Zn}$ will displace $\\text{Cu}$ ($\\text{Mg} + \\text{CuO} \\rightarrow \\text{MgO} + \\text{Cu}$; $\\text{Zn} + \\text{CuO} \\rightarrow \\text{ZnO} + \\text{Cu}$).\n4. Copper is less reactive than both $\\text{Mg}$ and $\\text{Zn}$, so it shows no reaction.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Inverts the reactivity series.\n• Option (C): Incorrect. A less reactive metal cannot displace a more reactive metal.\n• Option (D): Zn cannot displace Mg from MgO.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 55)",
        "questionNumber": "1"
    },
    {
        "id": "sci_ch3_p55_q02",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 55)",
        "question_number": "2",
        "text": "Which metals do not corrode easily even after prolonged exposure to air and moisture?",
        "options": [
            {
                "id": "A",
                "text": "Gold ($\\text{Au}$) and Platinum ($\\text{Pt}$)",
                "is_correct": True,
                "rationale": "Gold and platinum are noble metals located at the bottom of the reactivity series. They possess extremely low electrode potentials and chemical inertness toward oxygen, moisture, and carbon dioxide.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Iron ($\\text{Fe}$) and Copper ($\\text{Cu}$)",
                "is_correct": False,
                "rationale": "Iron rusts readily forming flaky hydrated iron(III) oxide, and copper corrodes forming a green basic carbonate layer.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Sodium ($\\text{Na}$) and Potassium ($\\text{K}$)",
                "is_correct": False,
                "rationale": "Alkali metals tarnish within seconds of exposure to moist air.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Magnesium ($\\text{Mg}$) and Calcium ($\\text{Ca}$)",
                "is_correct": False,
                "rationale": "Alkaline earth metals readily react with atmospheric air forming oxide/carbonate films.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Gold ($\\text{Au}$) and Platinum ($\\text{Pt}$)\n\nScientific Principle / Key Concept:\nMetals that do not corrode easily are the noble metals such as Gold ($\\text{Au}$) and Platinum ($\\text{Pt}$). They are at the bottom of the activity series and do not react with atmospheric gases (oxygen, water vapor, carbon dioxide, sulfur compounds) under ordinary conditions.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Fe rusts and Cu forms green patina.\n• Option (C): Incorrect. Na and K react violently with air and water.\n• Option (D): Incorrect. Mg and Ca tarnish by oxidation.",
        "step_by_step_solution": "Correct Answer: (A) Gold ($\\text{Au}$) and Platinum ($\\text{Pt}$)\n\nScientific Principle / Key Concept:\nMetals that do not corrode easily are the noble metals such as Gold ($\\text{Au}$) and Platinum ($\\text{Pt}$). They are at the bottom of the activity series and do not react with atmospheric gases (oxygen, water vapor, carbon dioxide, sulfur compounds) under ordinary conditions.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Fe rusts and Cu forms green patina.\n• Option (C): Incorrect. Na and K react violently with air and water.\n• Option (D): Incorrect. Mg and Ca tarnish by oxidation.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 55)",
        "questionNumber": "2"
    },
    {
        "id": "sci_ch3_p55_q03",
        "chapter": "Metals and Non-metals",
        "section": "QUESTIONS (Page 55)",
        "question_number": "3",
        "text": "What is an alloy, and how is it typically prepared?",
        "options": [
            {
                "id": "A",
                "text": "A homogeneous mixture of two or more metals, or a metal and a non-metal, prepared by melting the primary metal and dissolving the other elements in definite proportions.",
                "is_correct": True,
                "rationale": "An alloy is a solid homogeneous solution of metals or metals and non-metals (e.g., Brass = Cu + Zn, Stainless steel = Fe + C + Ni + Cr) prepared by melting the primary metal and dissolving solutes uniformly.",
                "correct": True
            },
            {
                "id": "B",
                "text": "A heterogeneous mixture of crushed metal powders compressed together at high pressure without melting.",
                "is_correct": False,
                "rationale": "Alloys are homogeneous solutions prepared through melting, not heterogeneous compressed mechanical powders.",
                "correct": False
            },
            {
                "id": "C",
                "text": "A chemical compound with fixed stoichiometric covalent bonding between two metals.",
                "is_correct": False,
                "rationale": "Alloys are mixtures with variable compositions, not stoichiometric chemical compounds.",
                "correct": False
            },
            {
                "id": "D",
                "text": "A pure refined metal coated with a non-corrosive layer of zinc or tin.",
                "is_correct": False,
                "rationale": "Coating a metal surface is galvanization or electroplating, not alloying.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) A homogeneous mixture of two or more metals, or a metal and a non-metal, prepared by melting the primary metal and dissolving the other elements in definite proportions.\n\nScientific Principle / Key Concept:\nAn alloy is a homogeneous mixture of two or more metals, or a metal and a non-metal. It is prepared by first melting the primary metal, and then dissolving the other elements in it in definite proportions. It is then cooled to room temperature.\nExamples: Brass (Copper + Zinc), Bronze (Copper + Tin), Solder (Lead + Tin), Stainless Steel (Iron + Nickel + Chromium + Carbon).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. An alloy is homogeneous, formed by melting.\n• Option (C): Incorrect. Alloys are solid solutions/mixtures, not stoichiometric covalent compounds.\n• Option (D): Incorrect. Surface plating is galvanizing, not alloying.",
        "step_by_step_solution": "Correct Answer: (A) A homogeneous mixture of two or more metals, or a metal and a non-metal, prepared by melting the primary metal and dissolving the other elements in definite proportions.\n\nScientific Principle / Key Concept:\nAn alloy is a homogeneous mixture of two or more metals, or a metal and a non-metal. It is prepared by first melting the primary metal, and then dissolving the other elements in it in definite proportions. It is then cooled to room temperature.\nExamples: Brass (Copper + Zinc), Bronze (Copper + Tin), Solder (Lead + Tin), Stainless Steel (Iron + Nickel + Chromium + Carbon).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. An alloy is homogeneous, formed by melting.\n• Option (C): Incorrect. Alloys are solid solutions/mixtures, not stoichiometric covalent compounds.\n• Option (D): Incorrect. Surface plating is galvanizing, not alloying.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "In-Text (Page 55)",
        "questionNumber": "3"
    },

    # ==================== PAGES 56-57: EXERCISES ====================
    {
        "id": "sci_ch3_ex_q01",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "1",
        "text": "[NCERT Exercise 1] Which of the following pairs will give displacement reactions?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{AgNO}_3$ solution and Copper metal",
                "is_correct": True,
                "rationale": "Copper is higher than silver in the reactivity series (Cu > Ag). Copper displaces silver from silver nitrate solution: $\\text{Cu} + 2\\text{AgNO}_3 \\rightarrow \\text{Cu(NO}_3)_2 + 2\\text{Ag}$.",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{NaCl}$ solution and Copper metal",
                "is_correct": False,
                "rationale": "Copper is far less reactive than sodium and cannot displace sodium from $\\text{NaCl}$.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$\\text{MgCl}_2$ solution and Aluminium metal",
                "is_correct": False,
                "rationale": "Aluminium is less reactive than magnesium (Mg > Al) and cannot displace magnesium.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{FeSO}_4$ solution and Silver metal",
                "is_correct": False,
                "rationale": "Silver is less reactive than iron (Fe > Ag) and cannot displace iron.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) $\\text{AgNO}_3$ solution and Copper metal\n\nScientific Principle / Key Concept:\nA displacement reaction occurs only when a free metal is higher in the reactivity series than the metal cation present in the salt solution.\n• (A): Copper lies above silver in the reactivity series ($\\text{Cu} > \\text{Ag}$). Thus, $\\text{Cu}(s) + 2\\text{AgNO}_3(aq) \\rightarrow \\text{Cu(NO}_3)_2(aq) + 2\\text{Ag}(s)$. Displacement occurs!\n• (B): $\\text{Na} > \\text{Cu}$ (No reaction)\n• (C): $\\text{Mg} > \\text{Al}$ (No reaction)\n• (D): $\\text{Fe} > \\text{Ag}$ (No reaction)\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Cu cannot displace Na.\n• Option (C): Incorrect. Al cannot displace Mg.\n• Option (D): Incorrect. Ag cannot displace Fe.",
        "step_by_step_solution": "Correct Answer: (A) $\\text{AgNO}_3$ solution and Copper metal\n\nScientific Principle / Key Concept:\nA displacement reaction occurs only when a free metal is higher in the reactivity series than the metal cation present in the salt solution.\n• (A): Copper lies above silver in the reactivity series ($\\text{Cu} > \\text{Ag}$). Thus, $\\text{Cu}(s) + 2\\text{AgNO}_3(aq) \\rightarrow \\text{Cu(NO}_3)_2(aq) + 2\\text{Ag}(s)$. Displacement occurs!\n• (B): $\\text{Na} > \\text{Cu}$ (No reaction)\n• (C): $\\text{Mg} > \\text{Al}$ (No reaction)\n• (D): $\\text{Fe} > \\text{Ag}$ (No reaction)\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Cu cannot displace Na.\n• Option (C): Incorrect. Al cannot displace Mg.\n• Option (D): Incorrect. Ag cannot displace Fe.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "1"
    },
    {
        "id": "sci_ch3_ex_q02",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "2",
        "text": "[NCERT Exercise 2] Which of the following methods is suitable for preventing an iron frying pan from rusting?",
        "options": [
            {
                "id": "A",
                "text": "Applying a coating of zinc (or using Teflon/seasoned oil)",
                "is_correct": True,
                "rationale": "Applying grease or paint is completely unsuitable for a cooking frying pan because grease spoils food and paint burns/decomposes emitting toxic fumes on heating. Applying a zinc layer (or seasoning) withstands heat.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Applying grease",
                "is_correct": False,
                "rationale": "Grease is toxic when ingested with cooked food and washes away immediately during washing.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Applying paint",
                "is_correct": False,
                "rationale": "Paint chars, burns off on flame, and releases harmful chemical vapors into food.",
                "correct": False
            },
            {
                "id": "D",
                "text": "All of the above",
                "is_correct": False,
                "rationale": "Applying paint and grease are strictly unsuitable for cooking utensils.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Applying a coating of zinc (or using Teflon/seasoned oil)\n\nScientific Principle / Key Concept:\nAlthough applying grease and paint are standard rust prevention methods for iron tools and gates, they cannot be used on an iron frying pan because:\n1. Grease will contaminate cooking food.\n2. Paint will scorch, melt, and peel off when heated on a stove, emitting noxious fumes.\nHence, a protective metallic zinc coating (or seasoning/Teflon coating) is the appropriate choice among standard metallurgical options presented in the NCERT exercise.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Grease ruins cooking.\n• Option (C): Incorrect. Paint burns at stove temperatures.\n• Option (D): Incorrect. 'All of the above' ignores the cooking context.",
        "step_by_step_solution": "Correct Answer: (A) Applying a coating of zinc (or using Teflon/seasoned oil)\n\nScientific Principle / Key Concept:\nAlthough applying grease and paint are standard rust prevention methods for iron tools and gates, they cannot be used on an iron frying pan because:\n1. Grease will contaminate cooking food.\n2. Paint will scorch, melt, and peel off when heated on a stove, emitting noxious fumes.\nHence, a protective metallic zinc coating (or seasoning/Teflon coating) is the appropriate choice among standard metallurgical options presented in the NCERT exercise.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Grease ruins cooking.\n• Option (C): Incorrect. Paint burns at stove temperatures.\n• Option (D): Incorrect. 'All of the above' ignores the cooking context.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "2"
    },
    {
        "id": "sci_ch3_ex_q03",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "3",
        "text": "[NCERT Exercise 3] An element reacts with oxygen to give a compound with a high melting point. This compound is also soluble in water. The element is likely to be:",
        "options": [
            {
                "id": "A",
                "text": "Calcium ($\\text{Ca}$)",
                "is_correct": True,
                "rationale": "Calcium reacts with oxygen to form calcium oxide ($\\text{CaO}$, quicklime), which is an ionic solid with a high melting point (2845 K / 2572°C) and dissolves in water to form calcium hydroxide $\\text{Ca(OH)}_2$ (slaked lime).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Carbon ($\\text{C}$)",
                "is_correct": False,
                "rationale": "Carbon reacts with oxygen to form $\\text{CO}_2$, which is a gas at room temperature (very low melting point).",
                "correct": False
            },
            {
                "id": "C",
                "text": "Silicon ($\\text{Si}$)",
                "is_correct": False,
                "rationale": "Silicon forms silica ($\\text{SiO}_2$), which has a high melting point but is completely insoluble in water.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Iron ($\\text{Fe}$)",
                "is_correct": False,
                "rationale": "Iron forms iron oxide ($\\text{Fe}_2\\text{O}_3$), which has a high melting point but is insoluble in water.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Calcium ($\\text{Ca}$)\n\nScientific Principle / Key Concept:\n• Calcium reacts with oxygen: $2\\text{Ca} + \\text{O}_2 \\rightarrow 2\\text{CaO}$.\n• $\\text{CaO}$ (quicklime) is an ionic solid with a very high melting point (~2572°C) due to strong electrostatic attraction between $\\text{Ca}^{2+}$ and $\\text{O}^{2-}$.\n• Furthermore, $\\text{CaO}$ reacts vigorously with water and dissolves to form slaked lime: $\\text{CaO} + \\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2(aq)$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. $\\text{CO}_2$ is a gas at room temperature.\n• Option (C): Incorrect. $\\text{SiO}_2$ (quartz/sand) is completely insoluble in water.\n• Option (D): Incorrect. Iron oxides are completely insoluble in water.",
        "step_by_step_solution": "Correct Answer: (A) Calcium ($\\text{Ca}$)\n\nScientific Principle / Key Concept:\n• Calcium reacts with oxygen: $2\\text{Ca} + \\text{O}_2 \\rightarrow 2\\text{CaO}$.\n• $\\text{CaO}$ (quicklime) is an ionic solid with a very high melting point (~2572°C) due to strong electrostatic attraction between $\\text{Ca}^{2+}$ and $\\text{O}^{2-}$.\n• Furthermore, $\\text{CaO}$ reacts vigorously with water and dissolves to form slaked lime: $\\text{CaO} + \\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2(aq)$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. $\\text{CO}_2$ is a gas at room temperature.\n• Option (C): Incorrect. $\\text{SiO}_2$ (quartz/sand) is completely insoluble in water.\n• Option (D): Incorrect. Iron oxides are completely insoluble in water.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "3"
    },
    {
        "id": "sci_ch3_ex_q04",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "4",
        "text": "[NCERT Exercise 4] Food cans are coated with tin ($\\text{Sn}$) and not with zinc ($\\text{Zn}$) because:",
        "options": [
            {
                "id": "A",
                "text": "Zinc is more reactive than tin.",
                "is_correct": True,
                "rationale": "Zinc is higher than tin in the reactivity series (Zn > Sn). Food contains organic acids which would react with reactive zinc forming toxic compounds, whereas tin is unreactive with food acids.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Zinc is costlier than tin.",
                "is_correct": False,
                "rationale": "Tin is actually much more expensive than zinc; cost is not the reason.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Zinc has a higher melting point than tin.",
                "is_correct": False,
                "rationale": "Melting points are irrelevant to food can storage temperatures.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Zinc is less reactive than tin.",
                "is_correct": False,
                "rationale": "Zinc is more electropositive and more reactive than tin, not less.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Zinc is more reactive than tin.\n\nScientific Principle / Key Concept:\nIn the reactivity series, Zinc is more reactive than Tin ($\\text{Zn} > \\text{Sn}$). Food items (such as fruit juices, curd, pickles, and canned vegetables) contain organic acids. If food cans were coated with zinc, the acids would react with the zinc to produce toxic zinc salts causing food poisoning. Tin is much less reactive, resists organic acids, and safely preserves food.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Tin is rarer and more expensive than zinc.\n• Option (C): Incorrect. Melting points do not affect room temperature food storage.\n• Option (D): Incorrect. Zinc is higher in reactivity series than tin.",
        "step_by_step_solution": "Correct Answer: (A) Zinc is more reactive than tin.\n\nScientific Principle / Key Concept:\nIn the reactivity series, Zinc is more reactive than Tin ($\\text{Zn} > \\text{Sn}$). Food items (such as fruit juices, curd, pickles, and canned vegetables) contain organic acids. If food cans were coated with zinc, the acids would react with the zinc to produce toxic zinc salts causing food poisoning. Tin is much less reactive, resists organic acids, and safely preserves food.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Tin is rarer and more expensive than zinc.\n• Option (C): Incorrect. Melting points do not affect room temperature food storage.\n• Option (D): Incorrect. Zinc is higher in reactivity series than tin.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "4"
    },
    {
        "id": "sci_ch3_ex_q05_a",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "5(a)",
        "text": "[NCERT Exercise 5(a)] You are given a hammer, a battery, a bulb, wires, and a switch. How can you use them to distinguish between samples of metals and non-metals?",
        "options": [
            {
                "id": "A",
                "text": "Hammer test: metals flatten into thin sheets (malleable), while non-metals shatter into powder (brittle). Circuit test: inserting a metal completes the circuit and the bulb glows (conductors), whereas non-metals do not conduct (bulb does not glow).",
                "is_correct": True,
                "rationale": "Metals are malleable (flatten when struck with a hammer) and electrical conductors (complete circuit causing bulb to glow). Non-metals are brittle (shatter under hammer) and non-conductors/insulators (circuit remains open).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Hammering non-metals produces sparks that light the bulb directly without requiring a battery.",
                "is_correct": False,
                "rationale": "Hammering non-metals shatters them; it does not produce electrical current.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Connecting non-metals causes the battery to short-circuit while metals discharge zero voltage.",
                "is_correct": False,
                "rationale": "Non-metals are electrical insulators; they do not cause a short circuit.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Hammering metals causes them to crack and crumble while non-metals stretch into thin foils.",
                "is_correct": False,
                "rationale": "This completely reverses the malleability and brittleness properties.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Hammer test: metals flatten into thin sheets (malleable), while non-metals shatter into powder (brittle). Circuit test: inserting a metal completes the circuit and the bulb glows (conductors), whereas non-metals do not conduct (bulb does not glow).\n\nScientific Principle / Key Concept:\n1. Malleability test (Hammer): Striking a sample with a hammer. If it flattens into a thin sheet without breaking, it is a metal (malleable). If it shatters into pieces or powder, it is a non-metal (brittle).\n2. Electrical conductivity test (Circuit): Connect the battery, bulb, wires, and switch. Insert the sample between test terminals. If the bulb glows, the sample conducts electricity (metal). If the bulb does not glow, it is an insulator (non-metal).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Striking does not power the bulb.\n• Option (C): Incorrect. Non-metals are insulators.\n• Option (D): Incorrect. Reverses metal and non-metal mechanical behaviors.",
        "step_by_step_solution": "Correct Answer: (A) Hammer test: metals flatten into thin sheets (malleable), while non-metals shatter into powder (brittle). Circuit test: inserting a metal completes the circuit and the bulb glows (conductors), whereas non-metals do not conduct (bulb does not glow).\n\nScientific Principle / Key Concept:\n1. Malleability test (Hammer): Striking a sample with a hammer. If it flattens into a thin sheet without breaking, it is a metal (malleable). If it shatters into pieces or powder, it is a non-metal (brittle).\n2. Electrical conductivity test (Circuit): Connect the battery, bulb, wires, and switch. Insert the sample between test terminals. If the bulb glows, the sample conducts electricity (metal). If the bulb does not glow, it is an insulator (non-metal).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Striking does not power the bulb.\n• Option (C): Incorrect. Non-metals are insulators.\n• Option (D): Incorrect. Reverses metal and non-metal mechanical behaviors.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "5(a)"
    },
    {
        "id": "sci_ch3_ex_q05_b",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "5(b)",
        "text": "[NCERT Exercise 5(b)] Assess the usefulness and reliability of the hammer test and electrical circuit test in distinguishing between metals and non-metals.",
        "options": [
            {
                "id": "A",
                "text": "The electrical conductivity test is more non-destructive and reliable, though graphite (carbon non-metal) is an exception that conducts; the hammer test reliably demonstrates malleability vs brittleness without exception.",
                "is_correct": True,
                "rationale": "Both physical tests are useful, but graphite is an allotrope of carbon that conducts electricity despite being a non-metal. The hammer test unequivocally distinguishes graphite (which crumbles) from metals.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Neither test has any practical validity because all non-metals conduct electricity and flatten like metals.",
                "is_correct": False,
                "rationale": "Non-metals are generally non-conductors and brittle.",
                "correct": False
            },
            {
                "id": "C",
                "text": "The hammer test cannot be used because metals are too brittle to strike with a hammer.",
                "is_correct": False,
                "rationale": "Metals possess high ductility and malleability, not brittleness.",
                "correct": False
            },
            {
                "id": "D",
                "text": "The circuit test is 100% foolproof with zero exceptions across all elements in the periodic table.",
                "is_correct": False,
                "rationale": "Graphite conducts electricity despite being a non-metal, so exceptions exist.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) The electrical conductivity test is more non-destructive and reliable, though graphite (carbon non-metal) is an exception that conducts; the hammer test reliably demonstrates malleability vs brittleness without exception.\n\nScientific Principle / Key Concept:\nAssessment of usefulness:\n1. The hammer test is highly effective: all solid metals are malleable, whereas solid non-metals are brittle and break under impact.\n2. The electrical test is convenient and non-destructive, but has exceptions: graphite (an allotrope of carbon, a non-metal) conducts electricity.\nTherefore, using both tests together provides definitive identification.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. The tests are standard textbook procedures with strong validity.\n• Option (C): Incorrect. Metals are malleable.\n• Option (D): Incorrect. Graphite is a notable exception that conducts electricity.",
        "step_by_step_solution": "Correct Answer: (A) The electrical conductivity test is more non-destructive and reliable, though graphite (carbon non-metal) is an exception that conducts; the hammer test reliably demonstrates malleability vs brittleness without exception.\n\nScientific Principle / Key Concept:\nAssessment of usefulness:\n1. The hammer test is highly effective: all solid metals are malleable, whereas solid non-metals are brittle and break under impact.\n2. The electrical test is convenient and non-destructive, but has exceptions: graphite (an allotrope of carbon, a non-metal) conducts electricity.\nTherefore, using both tests together provides definitive identification.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. The tests are standard textbook procedures with strong validity.\n• Option (C): Incorrect. Metals are malleable.\n• Option (D): Incorrect. Graphite is a notable exception that conducts electricity.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "5(b)"
    },
    {
        "id": "sci_ch3_ex_q06",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "6",
        "text": "[NCERT Exercise 6] What are amphoteric oxides? Give two examples of amphoteric oxides with their chemical behavior.",
        "options": [
            {
                "id": "A",
                "text": "Metal oxides that react with both acids and bases to produce salt and water; examples are Aluminium oxide ($\\text{Al}_2\\text{O}_3$) and Zinc oxide ($\\text{ZnO}$).",
                "is_correct": True,
                "rationale": "Amphoteric oxides exhibit dual chemical behavior, reacting as basic oxides with acids and as acidic oxides with strong bases to yield salt and water (e.g., $\\text{Al}_2\\text{O}_3 + 6\\text{HCl} \\rightarrow 2\\text{AlCl}_3 + 3\\text{H}_2\\text{O}$ and $\\text{Al}_2\\text{O}_3 + 2\\text{NaOH} \\rightarrow 2\\text{NaAlO}_2 + \\text{H}_2\\text{O}$).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Oxides that dissolve in water to form neutral solutions with pH 7; examples are $\\text{H}_2\\text{O}$ and $\\text{CO}$.",
                "is_correct": False,
                "rationale": "$\\text{H}_2\\text{O}$ and $\\text{CO}$ are neutral non-metal oxides, not amphoteric oxides.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Oxides that react only with strong mineral acids and are completely unreactive with alkalis; examples are $\\text{Na}_2\\text{O}$ and $\\text{K}_2\\text{O}$.",
                "is_correct": False,
                "rationale": "$\\text{Na}_2\\text{O}$ and $\\text{K}_2\\text{O}$ are strictly basic oxides, not amphoteric.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Non-metal oxides that turn red litmus blue; examples are $\\text{SO}_2$ and $\\text{CO}_2$.",
                "is_correct": False,
                "rationale": "$\\text{SO}_2$ and $\\text{CO}_2$ are acidic oxides, not amphoteric.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Metal oxides that react with both acids and bases to produce salt and water; examples are Aluminium oxide ($\\text{Al}_2\\text{O}_3$) and Zinc oxide ($\\text{ZnO}$).\n\nScientific Principle / Key Concept:\nSuch metal oxides which react with both acids as well as bases to produce salts and water are known as amphoteric oxides.\nExamples:\n1. Aluminium oxide ($\\text{Al}_2\\text{O}_3$):\n• Reaction with acid: $\\text{Al}_2\\text{O}_3 + 6\\text{HCl} \\rightarrow 2\\text{AlCl}_3 + 3\\text{H}_2\\text{O}$\n• Reaction with base: $\\text{Al}_2\\text{O}_3 + 2\\text{NaOH} \\rightarrow 2\\text{NaAlO}_2\\text{ (Sodium aluminate)} + \\text{H}_2\\text{O}$\n2. Zinc oxide ($\\text{ZnO}$):\n• Reaction with acid: $\\text{ZnO} + 2\\text{HCl} \\rightarrow \\text{ZnCl}_2 + \\text{H}_2\\text{O}$\n• Reaction with base: $\\text{ZnO} + 2\\text{NaOH} \\rightarrow \\text{Na}_2\\text{ZnO}_2\\text{ (Sodium zincate)} + \\text{H}_2\\text{O}$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Neutral oxides do not react with acids or bases.\n• Option (C): Incorrect. Basic oxides react only with acids.\n• Option (D): Incorrect. Non-metal oxides are acidic.",
        "step_by_step_solution": "Correct Answer: (A) Metal oxides that react with both acids and bases to produce salt and water; examples are Aluminium oxide ($\\text{Al}_2\\text{O}_3$) and Zinc oxide ($\\text{ZnO}$).\n\nScientific Principle / Key Concept:\nSuch metal oxides which react with both acids as well as bases to produce salts and water are known as amphoteric oxides.\nExamples:\n1. Aluminium oxide ($\\text{Al}_2\\text{O}_3$):\n• Reaction with acid: $\\text{Al}_2\\text{O}_3 + 6\\text{HCl} \\rightarrow 2\\text{AlCl}_3 + 3\\text{H}_2\\text{O}$\n• Reaction with base: $\\text{Al}_2\\text{O}_3 + 2\\text{NaOH} \\rightarrow 2\\text{NaAlO}_2\\text{ (Sodium aluminate)} + \\text{H}_2\\text{O}$\n2. Zinc oxide ($\\text{ZnO}$):\n• Reaction with acid: $\\text{ZnO} + 2\\text{HCl} \\rightarrow \\text{ZnCl}_2 + \\text{H}_2\\text{O}$\n• Reaction with base: $\\text{ZnO} + 2\\text{NaOH} \\rightarrow \\text{Na}_2\\text{ZnO}_2\\text{ (Sodium zincate)} + \\text{H}_2\\text{O}$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Neutral oxides do not react with acids or bases.\n• Option (C): Incorrect. Basic oxides react only with acids.\n• Option (D): Incorrect. Non-metal oxides are acidic.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "6"
    },
    {
        "id": "sci_ch3_ex_q07",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "7",
        "text": "[NCERT Exercise 7] Name two metals which will displace hydrogen from dilute acids, and two metals which will not.",
        "options": [
            {
                "id": "A",
                "text": "Displace hydrogen: Zinc ($\\text{Zn}$) and Iron ($\\text{Fe}$); Will not displace: Copper ($\\text{Cu}$) and Silver ($\\text{Ag}$)",
                "is_correct": True,
                "rationale": "Metals situated above hydrogen in the reactivity series (e.g., Zn, Fe, Mg) displace $\\text{H}_2$ from dilute acids. Metals below hydrogen (Cu, Ag, Au) cannot displace hydrogen.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Displace hydrogen: Copper ($\\text{Cu}$) and Gold ($\\text{Au}$); Will not displace: Magnesium ($\\text{Mg}$) and Calcium ($\\text{Ca}$)",
                "is_correct": False,
                "rationale": "This reverses the activity series relative to hydrogen.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Displace hydrogen: Silver ($\\text{Ag}$) and Platinum ($\\text{Pt}$); Will not displace: Sodium ($\\text{Na}$) and Potassium ($\\text{K}$)",
                "is_correct": False,
                "rationale": "Noble metals cannot displace hydrogen from dilute acids.",
                "correct": False
            },
            {
                "id": "D",
                "text": "All metals displace hydrogen from dilute acids without exception.",
                "is_correct": False,
                "rationale": "Metals below hydrogen in the reactivity series (Cu, Hg, Ag, Au, Pt) never displace hydrogen.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Displace hydrogen: Zinc ($\\text{Zn}$) and Iron ($\\text{Fe}$); Will not displace: Copper ($\\text{Cu}$) and Silver ($\\text{Ag}$)\n\nScientific Principle / Key Concept:\nMetals placed above hydrogen in the reactivity series have higher standard oxidation tendencies and reduce $\\text{H}^+$ ions to $\\text{H}_2(g)$:\n• Two metals that displace hydrogen: Zinc ($\\text{Zn}$) and Iron ($\\text{Fe}$) (or $\\text{Mg}, \\text{Al}$).\n• Two metals that do not displace hydrogen: Copper ($\\text{Cu}$) and Silver ($\\text{Ag}$) (or $\\text{Au}$), as they lie below hydrogen.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Inverts the activity series relative to hydrogen.\n• Option (C): Noble metals do not displace hydrogen.\n• Option (D): Incorrect generalization.",
        "step_by_step_solution": "Correct Answer: (A) Displace hydrogen: Zinc ($\\text{Zn}$) and Iron ($\\text{Fe}$); Will not displace: Copper ($\\text{Cu}$) and Silver ($\\text{Ag}$)\n\nScientific Principle / Key Concept:\nMetals placed above hydrogen in the reactivity series have higher standard oxidation tendencies and reduce $\\text{H}^+$ ions to $\\text{H}_2(g)$:\n• Two metals that displace hydrogen: Zinc ($\\text{Zn}$) and Iron ($\\text{Fe}$) (or $\\text{Mg}, \\text{Al}$).\n• Two metals that do not displace hydrogen: Copper ($\\text{Cu}$) and Silver ($\\text{Ag}$) (or $\\text{Au}$), as they lie below hydrogen.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Inverts the activity series relative to hydrogen.\n• Option (C): Noble metals do not displace hydrogen.\n• Option (D): Incorrect generalization.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "7"
    },
    {
        "id": "sci_ch3_ex_q08",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "8",
        "text": "[NCERT Exercise 8] In the electrolytic refining of an impure metal M, what are used as the anode, the cathode, and the electrolyte?",
        "options": [
            {
                "id": "A",
                "text": "Anode: Thick block of impure metal M; Cathode: Thin strip of pure metal M; Electrolyte: Acidified aqueous solution of a soluble salt of metal M.",
                "is_correct": True,
                "rationale": "At the positive anode, impure metal M dissolves ($\text{M} \rightarrow \text{M}^{n+} + n e^-$). At the negative cathode, metal ions deposit as pure metal ($\text{M}^{n+} + n e^- \rightarrow \text{M}$). The electrolyte is a soluble metal salt solution.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Anode: Thin strip of pure metal M; Cathode: Thick block of impure metal M; Electrolyte: Distilled water.",
                "is_correct": False,
                "rationale": "This reverses the electrodes and distilled water is non-conducting.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Anode: Carbon graphite rod; Cathode: Platinum wire; Electrolyte: Molten metal oxide.",
                "is_correct": False,
                "rationale": "In electrolytic refining of metals like copper, the anode must be the impure metal itself.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Anode: Pure metal M; Cathode: Impure metal M; Electrolyte: Concentrated sulphuric acid.",
                "is_correct": False,
                "rationale": "Impure metal dissolves at the anode, not at the cathode.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Anode: Thick block of impure metal M; Cathode: Thin strip of pure metal M; Electrolyte: Acidified aqueous solution of a soluble salt of metal M.\n\nScientific Principle / Key Concept:\nIn electrolytic refining (such as refining of crude copper):\n1. Anode (positive electrode): A thick plate of impure metal M.\n   Reaction: $\\text{M} \\rightarrow \\text{M}^{n+} + ne^-$ (metal dissolves into electrolyte)\n2. Cathode (negative electrode): A thin strip of pure metal M.\n   Reaction: $\\text{M}^{n+} + ne^- \\rightarrow \\text{M}$ (pure metal deposits on cathode)\n3. Electrolyte: An acidified aqueous solution of a salt of metal M (e.g., acidified $\\text{CuSO}_4$ for copper refining).\nInsoluble impurities settle down below the anode as anode mud.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Inverts the anode and cathode.\n• Option (C): Graphite anodes are used in smelting extraction (Hall-Héroult), not electrolytic refining.\n• Option (D): Impure metal must be the dissolving anode.",
        "step_by_step_solution": "Correct Answer: (A) Anode: Thick block of impure metal M; Cathode: Thin strip of pure metal M; Electrolyte: Acidified aqueous solution of a soluble salt of metal M.\n\nScientific Principle / Key Concept:\nIn electrolytic refining (such as refining of crude copper):\n1. Anode (positive electrode): A thick plate of impure metal M.\n   Reaction: $\\text{M} \\rightarrow \\text{M}^{n+} + ne^-$ (metal dissolves into electrolyte)\n2. Cathode (negative electrode): A thin strip of pure metal M.\n   Reaction: $\\text{M}^{n+} + ne^- \\rightarrow \\text{M}$ (pure metal deposits on cathode)\n3. Electrolyte: An acidified aqueous solution of a salt of metal M (e.g., acidified $\\text{CuSO}_4$ for copper refining).\nInsoluble impurities settle down below the anode as anode mud.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Inverts the anode and cathode.\n• Option (C): Graphite anodes are used in smelting extraction (Hall-Héroult), not electrolytic refining.\n• Option (D): Impure metal must be the dissolving anode.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "8"
    },
    {
        "id": "sci_ch3_ex_q09_a",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "9(a)",
        "text": "[NCERT Exercise 9(a)] Pratyush heated sulphur powder in a spatula and collected the evolved gas ($\\text{SO}_2$). What will be the action of this gas on (i) dry litmus paper, and (ii) moist litmus paper?",
        "options": [
            {
                "id": "A",
                "text": "No effect on dry litmus paper; turns moist blue litmus paper red.",
                "is_correct": True,
                "rationale": "Dry $\\text{SO}_2$ gas has no $\\text{H}^+$ ions and cannot affect dry litmus. With moisture, $\\text{SO}_2$ dissolves to form sulphurous acid ($\\text{H}_2\\text{SO}_3$), dissociating $\\text{H}^+$ ions that turn moist blue litmus red.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Turns dry litmus paper blue; turns moist litmus paper completely white/bleached.",
                "is_correct": False,
                "rationale": "Non-metal oxides are acidic, never turning litmus blue.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Turns both dry and moist litmus paper instantly to dark blue.",
                "is_correct": False,
                "rationale": "Blue color indicates basicity; $\\text{SO}_2$ produces an acidic solution.",
                "correct": False
            },
            {
                "id": "D",
                "text": "No effect on either dry or moist litmus paper because $\\text{SO}_2$ is a neutral gas.",
                "is_correct": False,
                "rationale": "$\\text{SO}_2$ is strongly acidic in water, not neutral.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) No effect on dry litmus paper; turns moist blue litmus paper red.\n\nScientific Principle / Key Concept:\nWhen sulphur is burned, it forms sulphur dioxide gas: $\\text{S} + \\text{O}_2 \\rightarrow \\text{SO}_2$.\n1. On dry litmus paper: No change in color occurs because acid behavior requires ionization into hydrogen ions ($\\text{H}^+$), which can only occur in the presence of water.\n2. On moist blue litmus paper: The gas dissolves in water to produce sulphurous acid:\n$$\\text{SO}_2(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{SO}_3(aq)$$\nSulphurous acid releases $\\text{H}^+$ ions, turning moist blue litmus paper red.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. $\\text{SO}_2$ is acidic, not basic.\n• Option (C): Incorrect. Basic color is blue; acid turns blue litmus red.\n• Option (D): Incorrect. $\\text{SO}_2$ is an acidic oxide.",
        "step_by_step_solution": "Correct Answer: (A) No effect on dry litmus paper; turns moist blue litmus paper red.\n\nScientific Principle / Key Concept:\nWhen sulphur is burned, it forms sulphur dioxide gas: $\\text{S} + \\text{O}_2 \\rightarrow \\text{SO}_2$.\n1. On dry litmus paper: No change in color occurs because acid behavior requires ionization into hydrogen ions ($\\text{H}^+$), which can only occur in the presence of water.\n2. On moist blue litmus paper: The gas dissolves in water to produce sulphurous acid:\n$$\\text{SO}_2(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{SO}_3(aq)$$\nSulphurous acid releases $\\text{H}^+$ ions, turning moist blue litmus paper red.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. $\\text{SO}_2$ is acidic, not basic.\n• Option (C): Incorrect. Basic color is blue; acid turns blue litmus red.\n• Option (D): Incorrect. $\\text{SO}_2$ is an acidic oxide.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "9(a)"
    },
    {
        "id": "sci_ch3_ex_q09_b",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "9(b)",
        "text": "[NCERT Exercise 9(b)] What are the balanced chemical equations for the combustion of sulphur and the reaction of the evolved gas with moisture?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{S}(s) + \\text{O}_2(g) \\rightarrow \\text{SO}_2(g)$ and $\\text{SO}_2(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{SO}_3(aq)$",
                "is_correct": True,
                "rationale": "Sulphur burns in air to give sulphur dioxide gas ($\\text{SO}_2$), which dissolves in water to form sulphurous acid ($\\text{H}_2\\text{SO}_3$).",
                "correct": True
            },
            {
                "id": "B",
                "text": "$2\\text{S}(s) + 3\\text{O}_2(g) \\rightarrow 2\\text{SO}_3(g)$ and $\\text{SO}_3(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{SO}_4(aq)$",
                "is_correct": False,
                "rationale": "Combustion of sulphur directly in air produces $\\text{SO}_2$, not $\\text{SO}_3$ (which requires a catalyst like $\\text{V}_2\\text{O}_5$).",
                "correct": False
            },
            {
                "id": "C",
                "text": "$\\text{S}(s) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{S}(g) + \\text{O}_2(g)$",
                "is_correct": False,
                "rationale": "Sulphur does not react with water to form hydrogen sulphide gas.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{S}(s) + 2\\text{O}_2(g) \\rightarrow \\text{SO}_4(g)$",
                "is_correct": False,
                "rationale": "$\\text{SO}_4$ does not exist as a neutral gas molecule.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) $\\text{S}(s) + \\text{O}_2(g) \\rightarrow \\text{SO}_2(g)$ and $\\text{SO}_2(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{SO}_3(aq)$\n\nScientific Principle / Key Concept:\n1. Heating sulphur in air:\n$$\\text{S}(s) + \\text{O}_2(g) \\rightarrow \\text{SO}_2(g)$$\n2. Reaction of sulphur dioxide with water:\n$$\\text{SO}_2(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{SO}_3(aq)\\text{ (Sulphurous acid)}$$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Direct combustion gives $\\text{SO}_2$, not $\\text{SO}_3$.\n• Option (C): Incorrect. Solid sulphur does not react with cold water.\n• Option (D): Incorrect chemical formula.",
        "step_by_step_solution": "Correct Answer: (A) $\\text{S}(s) + \\text{O}_2(g) \\rightarrow \\text{SO}_2(g)$ and $\\text{SO}_2(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{SO}_3(aq)$\n\nScientific Principle / Key Concept:\n1. Heating sulphur in air:\n$$\\text{S}(s) + \\text{O}_2(g) \\rightarrow \\text{SO}_2(g)$$\n2. Reaction of sulphur dioxide with water:\n$$\\text{SO}_2(g) + \\text{H}_2\\text{O}(l) \\rightarrow \\text{H}_2\\text{SO}_3(aq)\\text{ (Sulphurous acid)}$$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Direct combustion gives $\\text{SO}_2$, not $\\text{SO}_3$.\n• Option (C): Incorrect. Solid sulphur does not react with cold water.\n• Option (D): Incorrect chemical formula.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "9(b)"
    },
    {
        "id": "sci_ch3_ex_q10",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "10",
        "text": "[NCERT Exercise 10] Which of the following pairs represents two effective methods to prevent the rusting of iron?",
        "options": [
            {
                "id": "A",
                "text": "Galvanisation (coating with zinc) and Alloying (e.g., making stainless steel with Cr and Ni)",
                "is_correct": True,
                "rationale": "Galvanisation applies a sacrificial zinc barrier, and alloying iron with chromium and nickel forms stainless steel which does not rust.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Washing with hot water and polishing with sandpaper",
                "is_correct": False,
                "rationale": "Hot water accelerates rusting by providing moisture and heat, and polishing exposes fresh iron to atmospheric oxidation.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Exposing to humid air and dipping in salt solution",
                "is_correct": False,
                "rationale": "Both humid air and salt water dramatically accelerate rusting.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Heating iron to red hot in a furnace and quenching in cold water",
                "is_correct": False,
                "rationale": "This hardens steel (heat treatment), but does not prevent subsequent rusting when exposed to moisture.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Galvanisation (coating with zinc) and Alloying (e.g., making stainless steel with Cr and Ni)\n\nScientific Principle / Key Concept:\nRusting requires both oxygen ($\\text{O}_2$) and moisture ($\\text{H}_2\\text{O}$). Prevention methods include:\n1. Barrier protection & Galvanisation: Coating iron with a thin layer of zinc. Zinc protects sacrificially because it is more reactive and forms a protective oxide layer.\n2. Alloying: Mixing iron with Nickel and Chromium produces Stainless Steel, which resists rust completely.\nOther methods: Painting, greasing, and electroplating.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Accelerates rusting.\n• Option (C): Saline water speeds up rusting electrochemically.\n• Option (D): Heat treatment alters hardness, not corrosion immunity.",
        "step_by_step_solution": "Correct Answer: (A) Galvanisation (coating with zinc) and Alloying (e.g., making stainless steel with Cr and Ni)\n\nScientific Principle / Key Concept:\nRusting requires both oxygen ($\\text{O}_2$) and moisture ($\\text{H}_2\\text{O}$). Prevention methods include:\n1. Barrier protection & Galvanisation: Coating iron with a thin layer of zinc. Zinc protects sacrificially because it is more reactive and forms a protective oxide layer.\n2. Alloying: Mixing iron with Nickel and Chromium produces Stainless Steel, which resists rust completely.\nOther methods: Painting, greasing, and electroplating.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Accelerates rusting.\n• Option (C): Saline water speeds up rusting electrochemically.\n• Option (D): Heat treatment alters hardness, not corrosion immunity.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "10"
    },
    {
        "id": "sci_ch3_ex_q11",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "11",
        "text": "[NCERT Exercise 11] What type of oxides are formed when non-metals combine with oxygen?",
        "options": [
            {
                "id": "A",
                "text": "Acidic oxides (like $\\text{SO}_2, \\text{CO}_2$) or Neutral oxides (like $\\text{CO}, \\text{H}_2\\text{O}, \\text{N}_2\\text{O}$)",
                "is_correct": True,
                "rationale": "Non-metals react with oxygen to form covalent oxides. Most are acidic (dissolve in water to form acids), while some are neutral (no reaction with litmus). They never form basic oxides.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Basic oxides that dissolve in water to give alkaline solutions of pH > 12",
                "is_correct": False,
                "rationale": "Basic oxides are characteristic of electropositive metals (e.g., $\\text{Na}_2\\text{O}, \\text{CaO}$), never non-metals.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Exclusively amphoteric oxides that react equally with strong acids and bases",
                "is_correct": False,
                "rationale": "Amphoteric oxides are metal oxides like $\\text{Al}_2\\text{O}_3$ and $\\text{ZnO}$.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Ionic lattice oxides held by electrovalent bonds",
                "is_correct": False,
                "rationale": "Non-metal oxides are molecular covalent compounds, not ionic lattices.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Acidic oxides (like $\\text{SO}_2, \\text{CO}_2$) or Neutral oxides (like $\\text{CO}, \\text{H}_2\\text{O}, \\text{N}_2\\text{O}$)\n\nScientific Principle / Key Concept:\nWhen non-metals combine with oxygen, they form covalent oxides which are either:\n1. Acidic oxides: When dissolved in water, they produce acids (e.g., $\\text{CO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{H}_2\\text{CO}_3$; $\\text{SO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{H}_2\\text{SO}_3$).\n2. Neutral oxides: They show neither acidic nor basic properties and do not change the color of litmus (e.g., Carbon monoxide $\\text{CO}$, Water $\\text{H}_2\\text{O}$, Nitrous oxide $\\text{N}_2\\text{O}$).\nNon-metals never form basic oxides.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Metals form basic oxides.\n• Option (C): Incorrect. Non-metal oxides are not amphoteric.\n• Option (D): Incorrect. Non-metal oxides are covalent.",
        "step_by_step_solution": "Correct Answer: (A) Acidic oxides (like $\\text{SO}_2, \\text{CO}_2$) or Neutral oxides (like $\\text{CO}, \\text{H}_2\\text{O}, \\text{N}_2\\text{O}$)\n\nScientific Principle / Key Concept:\nWhen non-metals combine with oxygen, they form covalent oxides which are either:\n1. Acidic oxides: When dissolved in water, they produce acids (e.g., $\\text{CO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{H}_2\\text{CO}_3$; $\\text{SO}_2 + \\text{H}_2\\text{O} \\rightarrow \\text{H}_2\\text{SO}_3$).\n2. Neutral oxides: They show neither acidic nor basic properties and do not change the color of litmus (e.g., Carbon monoxide $\\text{CO}$, Water $\\text{H}_2\\text{O}$, Nitrous oxide $\\text{N}_2\\text{O}$).\nNon-metals never form basic oxides.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Metals form basic oxides.\n• Option (C): Incorrect. Non-metal oxides are not amphoteric.\n• Option (D): Incorrect. Non-metal oxides are covalent.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "11"
    },
    {
        "id": "sci_ch3_ex_q12_a",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "12(a)",
        "text": "[NCERT Exercise 12(a)] Why are Platinum, Gold, and Silver used to make jewellery?",
        "options": [
            {
                "id": "A",
                "text": "They have high metallic lustre, extraordinary malleability and ductility, and are highly unreactive noble metals that do not tarnish or corrode.",
                "is_correct": True,
                "rationale": "Gold, platinum, and silver are shiny, can be crafted into delicate patterns due to high malleability and ductility, and resist corrosion by air, moisture, and common chemicals.",
                "correct": True
            },
            {
                "id": "B",
                "text": "They are the hardest substances known and have magnetic properties that attract precious gems.",
                "is_correct": False,
                "rationale": "Diamond is the hardest substance, not gold/silver, and none of these noble metals are ferromagnetic.",
                "correct": False
            },
            {
                "id": "C",
                "text": "They react with skin sweat to form a protective natural green glaze.",
                "is_correct": False,
                "rationale": "Jewellery metals must NOT react with sweat; green glaze is copper corrosion, which is undesirable.",
                "correct": False
            },
            {
                "id": "D",
                "text": "They have very low melting points and can be remolded by hot water.",
                "is_correct": False,
                "rationale": "They have high melting points (e.g., Gold melts at 1064°C).",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) They have high metallic lustre, extraordinary malleability and ductility, and are highly unreactive noble metals that do not tarnish or corrode.\n\nScientific Principle / Key Concept:\nPlatinum, Gold, and Silver are used for making jewellery because:\n1. They possess a brilliant metallic shine and luster.\n2. They are the most malleable and ductile metals, enabling artisans to shape them into intricate designs.\n3. They are noble metals at the bottom of the activity series; they do not react with air, water, or acids, retaining their shine for decades without corroding.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. They are relatively soft metals, and non-magnetic.\n• Option (C): Incorrect. Tarnishing on skin is undesirable.\n• Option (D): Incorrect. They have high melting points.",
        "step_by_step_solution": "Correct Answer: (A) They have high metallic lustre, extraordinary malleability and ductility, and are highly unreactive noble metals that do not tarnish or corrode.\n\nScientific Principle / Key Concept:\nPlatinum, Gold, and Silver are used for making jewellery because:\n1. They possess a brilliant metallic shine and luster.\n2. They are the most malleable and ductile metals, enabling artisans to shape them into intricate designs.\n3. They are noble metals at the bottom of the activity series; they do not react with air, water, or acids, retaining their shine for decades without corroding.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. They are relatively soft metals, and non-magnetic.\n• Option (C): Incorrect. Tarnishing on skin is undesirable.\n• Option (D): Incorrect. They have high melting points.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "12(a)"
    },
    {
        "id": "sci_ch3_ex_q12_b",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "12(b)",
        "text": "[NCERT Exercise 12(b)] Why are Sodium, Potassium, and Lithium stored under oil (such as kerosene)?",
        "options": [
            {
                "id": "A",
                "text": "They are extremely reactive metals that catch fire spontaneously when exposed to atmospheric oxygen and water vapor.",
                "is_correct": True,
                "rationale": "Alkali metals react violently with air and moisture. The reaction is highly exothermic and ignites the evolved hydrogen gas, posing a severe fire hazard. Oil acts as an inert protective barrier.",
                "correct": True
            },
            {
                "id": "B",
                "text": "They are hygroscopic liquids that dissolve if stored in glass containers.",
                "is_correct": False,
                "rationale": "Sodium, potassium, and lithium are soft solids, not liquids.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Kerosene cools them down to prevent nuclear radioactive decay.",
                "is_correct": False,
                "rationale": "These common isotopes are stable chemical elements, not radioactive materials.",
                "correct": False
            },
            {
                "id": "D",
                "text": "To prevent them from subliming into gas at room temperature.",
                "is_correct": False,
                "rationale": "Metals do not sublime at room temperature.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) They are extremely reactive metals that catch fire spontaneously when exposed to atmospheric oxygen and water vapor.\n\nScientific Principle / Key Concept:\nSodium, potassium, and lithium are placed at the top of the reactivity series. They react vigorously with atmospheric oxygen and water vapor:\n$$4\\text{Na} + \\text{O}_2 \\rightarrow 2\\text{Na}_2\\text{O}$$\n$$2\\text{Na} + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{NaOH} + \\text{H}_2 + \\text{Heat}$$\nThe reaction is violently exothermic, igniting the hydrogen gas. Storing them under kerosene oil cuts off contact with air and moisture, preventing accidental combustion.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. They are solid metals.\n• Option (C): Incorrect. There is no nuclear radioactivity involved.\n• Option (D): Incorrect. They have high boiling points and do not sublime.",
        "step_by_step_solution": "Correct Answer: (A) They are extremely reactive metals that catch fire spontaneously when exposed to atmospheric oxygen and water vapor.\n\nScientific Principle / Key Concept:\nSodium, potassium, and lithium are placed at the top of the reactivity series. They react vigorously with atmospheric oxygen and water vapor:\n$$4\\text{Na} + \\text{O}_2 \\rightarrow 2\\text{Na}_2\\text{O}$$\n$$2\\text{Na} + 2\\text{H}_2\\text{O} \\rightarrow 2\\text{NaOH} + \\text{H}_2 + \\text{Heat}$$\nThe reaction is violently exothermic, igniting the hydrogen gas. Storing them under kerosene oil cuts off contact with air and moisture, preventing accidental combustion.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. They are solid metals.\n• Option (C): Incorrect. There is no nuclear radioactivity involved.\n• Option (D): Incorrect. They have high boiling points and do not sublime.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "12(b)"
    },
    {
        "id": "sci_ch3_ex_q12_c",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "12(c)",
        "text": "[NCERT Exercise 12(c)] Aluminium is a highly reactive metal, yet it is extensively used to manufacture cooking utensils. What is the reason?",
        "options": [
            {
                "id": "A",
                "text": "It rapidly forms a thin, tough, non-porous protective surface layer of Aluminium oxide ($\\text{Al}_2\\text{O}_3$) that prevents further corrosion, combined with high thermal conductivity and light weight.",
                "is_correct": True,
                "rationale": "Aluminium reacts with atmospheric oxygen to form a passive, impenetrable $\\text{Al}_2\\text{O}_3$ coating. This passivation layer prevents further oxidation and reaction with food, while its good thermal conductivity distributes cooking heat efficiently.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Aluminium becomes completely unreactive when heated above 50°C.",
                "is_correct": False,
                "rationale": "Aluminium does not change its fundamental chemical identity with temperature; it is protected by the oxide barrier.",
                "correct": False
            },
            {
                "id": "C",
                "text": "It is cheaper than clay and dissolves completely in water after cooking.",
                "is_correct": False,
                "rationale": "Aluminium is insoluble in water; utensils do not dissolve.",
                "correct": False
            },
            {
                "id": "D",
                "text": "It absorbs food toxins and converts all organic acids into neutral sugars.",
                "is_correct": False,
                "rationale": "Utensils are inert cookware; they do not perform biochemical conversion of food acids into sugars.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) It rapidly forms a thin, tough, non-porous protective surface layer of Aluminium oxide ($\\text{Al}_2\\text{O}_3$) that prevents further corrosion, combined with high thermal conductivity and light weight.\n\nScientific Principle / Key Concept:\nThough aluminium is a reactive metal, on exposure to air it quickly develops a thin, adherent, non-porous protective oxide film:\n$$4\\text{Al} + 3\\text{O}_2 \\rightarrow 2\\text{Al}_2\\text{O}_3$$\nThis oxide layer passivates the metal and protects the underlying aluminium from corrosion and attack by moisture or food ingredients. Coupled with its excellent thermal conductivity, light weight, and high malleability, it is ideal for cooking utensils.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Passivation is due to the oxide layer, not heat neutralization.\n• Option (C): Incorrect. Aluminium is insoluble.\n• Option (D): Incorrect. Utensils do not convert food acids into sugars.",
        "step_by_step_solution": "Correct Answer: (A) It rapidly forms a thin, tough, non-porous protective surface layer of Aluminium oxide ($\\text{Al}_2\\text{O}_3$) that prevents further corrosion, combined with high thermal conductivity and light weight.\n\nScientific Principle / Key Concept:\nThough aluminium is a reactive metal, on exposure to air it quickly develops a thin, adherent, non-porous protective oxide film:\n$$4\\text{Al} + 3\\text{O}_2 \\rightarrow 2\\text{Al}_2\\text{O}_3$$\nThis oxide layer passivates the metal and protects the underlying aluminium from corrosion and attack by moisture or food ingredients. Coupled with its excellent thermal conductivity, light weight, and high malleability, it is ideal for cooking utensils.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Passivation is due to the oxide layer, not heat neutralization.\n• Option (C): Incorrect. Aluminium is insoluble.\n• Option (D): Incorrect. Utensils do not convert food acids into sugars.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "12(c)"
    },
    {
        "id": "sci_ch3_ex_q12_d",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "12(d)",
        "text": "[NCERT Exercise 12(d)] Why are carbonate and sulphide ores usually converted into oxides during the process of metal extraction?",
        "options": [
            {
                "id": "A",
                "text": "It is chemically much easier and more economical to reduce a metal oxide to free metal using carbon or other reducing agents than to reduce carbonates or sulphides directly.",
                "is_correct": True,
                "rationale": "Direct reduction of sulphides and carbonates by common reducing agents like coke is thermodynamically unfavorable. Converting them to oxides (via roasting or calcination) allows simple, efficient reduction by carbon: $\\text{MO} + \\text{C} \\rightarrow \\text{M} + \\text{CO}$.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Carbonate and sulphide ores are radioactive and must be deactivated by conversion to oxides.",
                "is_correct": False,
                "rationale": "Common industrial ores of zinc, iron, lead, and copper are non-radioactive.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Metal oxides are liquids at room temperature and separate naturally by gravity.",
                "is_correct": False,
                "rationale": "Metal oxides are high-melting crystalline solids, not liquids.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Sulphur and carbon cannot be separated except by dissolving the ores in aqua regia.",
                "is_correct": False,
                "rationale": "Calcination and roasting drive off carbon dioxide and sulphur dioxide as gases without requiring expensive aqua regia.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) It is chemically much easier and more economical to reduce a metal oxide to free metal using carbon or other reducing agents than to reduce carbonates or sulphides directly.\n\nScientific Principle / Key Concept:\nIt is much easier to obtain a metal from its oxide, as compared from its sulphides and carbonates. Therefore, prior to reduction, the metal sulphides and carbonates must be converted into metal oxides:\n1. Calcination (for carbonate ores): Heating strongly in limited air:\n$$\\text{ZnCO}_3 \\xrightarrow{\\Delta} \\text{ZnO} + \\text{CO}_2\\uparrow$$\n2. Roasting (for sulphide ores): Heating strongly in excess air:\n$$2\\text{ZnS} + 3\\text{O}_2 \\xrightarrow{\\Delta} 2\\text{ZnO} + 2\\text{SO}_2\\uparrow$$\nOnce converted into oxide, reduction with carbon is straightforward: $\\text{ZnO} + \\text{C} \\rightarrow \\text{Zn} + \\text{CO}$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Standard ores are non-radioactive.\n• Option (C): Incorrect. Metal oxides are solids with very high melting points.\n• Option (D): Incorrect. Roasting/calcination cleanly evolves gases.",
        "step_by_step_solution": "Correct Answer: (A) It is chemically much easier and more economical to reduce a metal oxide to free metal using carbon or other reducing agents than to reduce carbonates or sulphides directly.\n\nScientific Principle / Key Concept:\nIt is much easier to obtain a metal from its oxide, as compared from its sulphides and carbonates. Therefore, prior to reduction, the metal sulphides and carbonates must be converted into metal oxides:\n1. Calcination (for carbonate ores): Heating strongly in limited air:\n$$\\text{ZnCO}_3 \\xrightarrow{\\Delta} \\text{ZnO} + \\text{CO}_2\\uparrow$$\n2. Roasting (for sulphide ores): Heating strongly in excess air:\n$$2\\text{ZnS} + 3\\text{O}_2 \\xrightarrow{\\Delta} 2\\text{ZnO} + 2\\text{SO}_2\\uparrow$$\nOnce converted into oxide, reduction with carbon is straightforward: $\\text{ZnO} + \\text{C} \\rightarrow \\text{Zn} + \\text{CO}$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Standard ores are non-radioactive.\n• Option (C): Incorrect. Metal oxides are solids with very high melting points.\n• Option (D): Incorrect. Roasting/calcination cleanly evolves gases.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "12(d)"
    },
    {
        "id": "sci_ch3_ex_q13",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "13",
        "text": "[NCERT Exercise 13] Why are tarnished copper vessels cleaned effectively with lemon or tamarind juice?",
        "options": [
            {
                "id": "A",
                "text": "Copper tarnishes by forming a green layer of basic copper carbonate, which is neutralized and dissolved by the citric or tartaric acid present in sour juices, forming soluble copper salts.",
                "is_correct": True,
                "rationale": "Copper reacts with moist atmospheric $\\text{CO}_2$ to form basic copper carbonate ($\\text{CuCO}_3 \\cdot \\text{Cu(OH)}_2$, green layer). Sour juices contain weak organic acids (citric acid in lemon, tartaric acid in tamarind) that react with this basic layer to form soluble copper citrate/tartrate, washing it away to restore shiny reddish-brown copper.",
                "correct": True
            },
            {
                "id": "B",
                "text": "The juices deposit a fresh thin layer of metallic copper from their seeds.",
                "is_correct": False,
                "rationale": "Fruit juices contain no elemental copper metal.",
                "correct": False
            },
            {
                "id": "C",
                "text": "The high pH of alkaline juices bleaches the dark tarnish to transparent copper.",
                "is_correct": False,
                "rationale": "Lemon and tamarind juices are acidic (low pH < 3), not alkaline.",
                "correct": False
            },
            {
                "id": "D",
                "text": "The juices act as mechanical abrasives with hard silicate crystals that scrape the metal.",
                "is_correct": False,
                "rationale": "The cleaning mechanism is chemical acid-base neutralization, not physical abrasive scratching.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Copper tarnishes by forming a green layer of basic copper carbonate, which is neutralized and dissolved by the citric or tartaric acid present in sour juices, forming soluble copper salts.\n\nScientific Principle / Key Concept:\nCopper reacts slowly with moist carbon dioxide in the air and loses its shiny brown coat, gaining a green coat of basic copper carbonate:\n$$2\\text{Cu} + \\text{H}_2\\text{O} + \\text{CO}_2 + \\text{O}_2 \\rightarrow \\text{CuCO}_3 \\cdot \\text{Cu(OH)}_2\\text{ (Green)}$$\nLemon contains citric acid and tamarind contains tartaric acid. When rubbed on tarnished copper, these acids neutralize the basic copper carbonate, converting it into soluble copper salts that are washed away with water, leaving the shiny reddish-brown metal surface clean.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Juices do not contain metallic copper.\n• Option (C): Incorrect. Sour juices are acidic, not alkaline.\n• Option (D): Incorrect. The cleaning is chemical neutralization, not abrasive wear.",
        "step_by_step_solution": "Correct Answer: (A) Copper tarnishes by forming a green layer of basic copper carbonate, which is neutralized and dissolved by the citric or tartaric acid present in sour juices, forming soluble copper salts.\n\nScientific Principle / Key Concept:\nCopper reacts slowly with moist carbon dioxide in the air and loses its shiny brown coat, gaining a green coat of basic copper carbonate:\n$$2\\text{Cu} + \\text{H}_2\\text{O} + \\text{CO}_2 + \\text{O}_2 \\rightarrow \\text{CuCO}_3 \\cdot \\text{Cu(OH)}_2\\text{ (Green)}$$\nLemon contains citric acid and tamarind contains tartaric acid. When rubbed on tarnished copper, these acids neutralize the basic copper carbonate, converting it into soluble copper salts that are washed away with water, leaving the shiny reddish-brown metal surface clean.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Juices do not contain metallic copper.\n• Option (C): Incorrect. Sour juices are acidic, not alkaline.\n• Option (D): Incorrect. The cleaning is chemical neutralization, not abrasive wear.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "13"
    },
    {
        "id": "sci_ch3_ex_q14",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "14",
        "text": "[NCERT Exercise 14] Which statement correctly differentiates metals from non-metals based strictly on their chemical properties?",
        "options": [
            {
                "id": "A",
                "text": "Metals form basic oxides, act as reducing agents by losing electrons, and displace hydrogen from dilute acids; non-metals form acidic or neutral oxides, act as oxidizing agents by gaining electrons, and do not displace hydrogen from acids.",
                "is_correct": True,
                "rationale": "Metals are electropositive (form cations), their oxides are basic/amphoteric, and they reduce $\\text{H}^+$ from acids. Non-metals are electronegative (form anions), their oxides are acidic/neutral, and they cannot donate electrons to $\\text{H}^+$ in acids.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Metals form acidic oxides and gain electrons; non-metals form basic oxides and lose electrons.",
                "is_correct": False,
                "rationale": "This completely reverses the chemical redox and oxide behaviors of metals and non-metals.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Metals are malleable and sonorous, while non-metals are brittle and dull.",
                "is_correct": False,
                "rationale": "Malleability, sonorousness, and lustre are physical properties, not chemical properties.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Both metals and non-metals displace hydrogen from water and form identical ionic chlorides.",
                "is_correct": False,
                "rationale": "Non-metals do not displace hydrogen from water and form covalent chlorides (e.g., $\\text{CCl}_4, \\text{PCl}_3$), unlike ionic metallic chlorides (e.g., $\\text{NaCl}, \\text{MgCl}_2$).",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Metals form basic oxides, act as reducing agents by losing electrons, and displace hydrogen from dilute acids; non-metals form acidic or neutral oxides, act as oxidizing agents by gaining electrons, and do not displace hydrogen from acids.\n\nScientific Principle / Key Concept:\nChemical Differences:\n1. Nature of Oxides: Metals form basic oxides (e.g., $\\text{Na}_2\\text{O}, \\text{CaO}$) or amphoteric oxides. Non-metals form acidic oxides ($\\text{SO}_2, \\text{CO}_2$) or neutral oxides ($\\text{CO}, \\text{H}_2\\text{O}$).\n2. Reaction with Acids: Metals above hydrogen displace $\\text{H}_2$ gas from dilute acids. Non-metals do not displace hydrogen.\n3. Electron behavior: Metals are electropositive and act as reducing agents (lose electrons). Non-metals are electronegative and act as oxidizing agents (gain electrons).\n4. Chlorides: Metals form ionic chlorides with high melting points; non-metals form covalent chlorides.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Inverts fundamental properties.\n• Option (C): Lists physical properties, not chemical properties.\n• Option (D): Non-metals do not displace hydrogen from water.",
        "step_by_step_solution": "Correct Answer: (A) Metals form basic oxides, act as reducing agents by losing electrons, and displace hydrogen from dilute acids; non-metals form acidic or neutral oxides, act as oxidizing agents by gaining electrons, and do not displace hydrogen from acids.\n\nScientific Principle / Key Concept:\nChemical Differences:\n1. Nature of Oxides: Metals form basic oxides (e.g., $\\text{Na}_2\\text{O}, \\text{CaO}$) or amphoteric oxides. Non-metals form acidic oxides ($\\text{SO}_2, \\text{CO}_2$) or neutral oxides ($\\text{CO}, \\text{H}_2\\text{O}$).\n2. Reaction with Acids: Metals above hydrogen displace $\\text{H}_2$ gas from dilute acids. Non-metals do not displace hydrogen.\n3. Electron behavior: Metals are electropositive and act as reducing agents (lose electrons). Non-metals are electronegative and act as oxidizing agents (gain electrons).\n4. Chlorides: Metals form ionic chlorides with high melting points; non-metals form covalent chlorides.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Inverts fundamental properties.\n• Option (C): Lists physical properties, not chemical properties.\n• Option (D): Non-metals do not displace hydrogen from water.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "14"
    },
    {
        "id": "sci_ch3_ex_q15",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "15",
        "text": "[NCERT Exercise 15] An imposter posing as a goldsmith dipped a lady's dull gold bangles into a solution. The bangles sparkled like new, but their weight was drastically reduced. What was the solution used by the fraudulent goldsmith?",
        "options": [
            {
                "id": "A",
                "text": "Aqua Regia (a freshly prepared mixture of concentrated $\\text{HCl}$ and concentrated $\\text{HNO}_3$ in a $3:1$ ratio by volume)",
                "is_correct": True,
                "rationale": "Aqua regia ('royal water') is capable of dissolving noble metals like gold and platinum. The outer tarnished layers of gold dissolved into the acid forming soluble chlorauric acid ($\text{HAuCl}_4$), revealing shining gold underneath while drastically reducing the bangles' weight.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Concentrated Sulphuric acid ($\\text{H}_2\\text{SO}_4$)",
                "is_correct": False,
                "rationale": "Gold does not react with or dissolve in concentrated sulphuric acid.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Dilute Sodium hydroxide ($\\text{NaOH}$) solution",
                "is_correct": False,
                "rationale": "Gold is completely unaffected by sodium hydroxide solutions.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Copper sulphate ($\\text{CuSO}_4$) solution",
                "is_correct": False,
                "rationale": "Gold lies far below copper and shows zero displacement or dissolution in copper sulphate.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Aqua Regia (a freshly prepared mixture of concentrated $\\text{HCl}$ and concentrated $\\text{HNO}_3$ in a $3:1$ ratio by volume)\n\nScientific Principle / Key Concept:\nGold is a noble metal that does not react with single mineral acids like $\\text{HCl}$, $\\text{HNO}_3$, or $\\text{H}_2\\text{SO}_4$. However, it dissolves in Aqua Regia (Latin for 'royal water'), which is a freshly prepared mixture of concentrated Hydrochloric acid and concentrated Nitric acid in the ratio $3:1$:\n$$\\text{Au} + 3\\text{HCl} + \\text{HNO}_3 \\rightarrow \\text{HAuCl}_4 + \\text{NO} + 2\\text{H}_2\\text{O}$$\nThe outer layer of gold dissolved into the liquid, leaving the fresh inner gold sparkling clean but causing a substantial loss in the weight of the gold bangles.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Pure gold does not dissolve in concentrated sulphuric acid.\n• Option (C): Incorrect. Gold does not react with alkalis.\n• Option (D): Incorrect. Copper sulphate has no reaction with gold.",
        "step_by_step_solution": "Correct Answer: (A) Aqua Regia (a freshly prepared mixture of concentrated $\\text{HCl}$ and concentrated $\\text{HNO}_3$ in a $3:1$ ratio by volume)\n\nScientific Principle / Key Concept:\nGold is a noble metal that does not react with single mineral acids like $\\text{HCl}$, $\\text{HNO}_3$, or $\\text{H}_2\\text{SO}_4$. However, it dissolves in Aqua Regia (Latin for 'royal water'), which is a freshly prepared mixture of concentrated Hydrochloric acid and concentrated Nitric acid in the ratio $3:1$:\n$$\\text{Au} + 3\\text{HCl} + \\text{HNO}_3 \\rightarrow \\text{HAuCl}_4 + \\text{NO} + 2\\text{H}_2\\text{O}$$\nThe outer layer of gold dissolved into the liquid, leaving the fresh inner gold sparkling clean but causing a substantial loss in the weight of the gold bangles.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Pure gold does not dissolve in concentrated sulphuric acid.\n• Option (C): Incorrect. Gold does not react with alkalis.\n• Option (D): Incorrect. Copper sulphate has no reaction with gold.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "15"
    },
    {
        "id": "sci_ch3_ex_q16",
        "chapter": "Metals and Non-metals",
        "section": "EXERCISES (Pages 56-57)",
        "question_number": "16",
        "text": "[NCERT Exercise 16] Why is copper used to make hot water tanks, while steel (an alloy of iron) is not used?",
        "options": [
            {
                "id": "A",
                "text": "Copper does not react with cold water, hot water, or steam, whereas iron in steel reacts with steam at boiling temperatures forming $\\text{Fe}_3\\text{O}_4$ and rusts over time.",
                "is_correct": True,
                "rationale": "Copper lies below hydrogen in the reactivity series and does not react with water at any temperature. Iron in steel reacts with steam ($3\\text{Fe} + 4\\text{H}_2\\text{O} \\rightarrow \\text{Fe}_3\\text{O}_4 + 4\\text{H}_2$) and rusts in the presence of dissolved oxygen, degrading the tank.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Steel melts below 100°C when water boils, while copper has a high melting point.",
                "is_correct": False,
                "rationale": "Steel melts above 1370°C, far higher than the boiling point of water.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Copper is a poor conductor of heat, keeping the water hot by insulation.",
                "is_correct": False,
                "rationale": "Copper is an excellent conductor of heat, not an insulator.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Steel dissolves in water to form poisonous iron cyanide compounds.",
                "is_correct": False,
                "rationale": "Steel contains iron and carbon; cyanides are not formed.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Copper does not react with cold water, hot water, or steam, whereas iron in steel reacts with steam at boiling temperatures forming $\\text{Fe}_3\\text{O}_4$ and rusts over time.\n\nScientific Principle / Key Concept:\n1. Copper is below hydrogen in the reactivity series and does not react with water, hot water, or steam under any conditions:\n$$\\text{Cu} + \\text{H}_2\\text{O} \\rightarrow \\text{No Reaction}$$\n2. Steel contains iron, which is above hydrogen in the reactivity series. Iron reacts readily with hot water and steam to produce magnetic iron oxide and hydrogen gas:\n$$3\\text{Fe}(s) + 4\\text{H}_2\\text{O}(g) \\rightarrow \\text{Fe}_3\\text{O}_4(s) + 4\\text{H}_2(g)$$\nFurthermore, dissolved oxygen in hot water causes severe rusting and perforation of steel tanks. Hence, copper is preferred.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Steel's melting point is ~1400°C.\n• Option (C): Incorrect. Copper has very high thermal conductivity.\n• Option (D): Incorrect. Toxic cyanides are never produced.",
        "step_by_step_solution": "Correct Answer: (A) Copper does not react with cold water, hot water, or steam, whereas iron in steel reacts with steam at boiling temperatures forming $\\text{Fe}_3\\text{O}_4$ and rusts over time.\n\nScientific Principle / Key Concept:\n1. Copper is below hydrogen in the reactivity series and does not react with water, hot water, or steam under any conditions:\n$$\\text{Cu} + \\text{H}_2\\text{O} \\rightarrow \\text{No Reaction}$$\n2. Steel contains iron, which is above hydrogen in the reactivity series. Iron reacts readily with hot water and steam to produce magnetic iron oxide and hydrogen gas:\n$$3\\text{Fe}(s) + 4\\text{H}_2\\text{O}(g) \\rightarrow \\text{Fe}_3\\text{O}_4(s) + 4\\text{H}_2(g)$$\nFurthermore, dissolved oxygen in hot water causes severe rusting and perforation of steel tanks. Hence, copper is preferred.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Steel's melting point is ~1400°C.\n• Option (C): Incorrect. Copper has very high thermal conductivity.\n• Option (D): Incorrect. Toxic cyanides are never produced.",
        "subject": "science",
        "chapterId": "sci_ch_03_metals_non_metals",
        "exercise": "Exercises (Pages 56-57)",
        "questionNumber": "16"
    }
]

print(f"Total authentic NCERT questions compiled: {len(questions)}")

# Write to assets/data/ncert_science_ch3.json
output_path = "assets/data/ncert_science_ch3.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(questions)} questions to {output_path}")
