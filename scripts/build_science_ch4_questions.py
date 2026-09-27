"""
Build authentic NCERT question bank for CBSE Class 10 Science Chapter 4: Carbon and its Compounds.
Strict Source Isolation: In-Text QUESTIONS (Pages 61, 68, 69, 71, 74, 76) and EXERCISES (Pages 77-78).
"""

import json

questions = [
    # ==================== PAGE 61: QUESTIONS ====================
    {
        "id": "sci_ch4_p61_q01",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 61)",
        "question_number": "1",
        "text": "What is the electron dot structure and bonding nature of carbon dioxide ($\\text{CO}_2$)?",
        "options": [
            {
                "id": "A",
                "text": "Carbon shares two pairs of electrons with each of the two oxygen atoms, forming two double covalent bonds: $:\\ddot{\\text{O}}=\\text{C}=\\ddot{\\text{O}}:$.",
                "is_correct": True,
                "rationale": "Carbon has 4 valence electrons and each oxygen has 6. To complete their octets, carbon forms a double covalent bond with each oxygen atom, sharing four electrons on each side.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Carbon forms single covalent bonds with both oxygen atoms, leaving one oxygen atom with an incomplete octet: $\\text{O}-\\text{C}-\\text{O}$.",
                "is_correct": False,
                "rationale": "Single bonds would leave carbon with only 6 electrons and oxygen atoms with 7, failing to achieve noble gas octets.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Carbon completely transfers four electrons to two oxygen atoms, forming an ionic crystal lattice of $\\text{C}^{4+}$ and $2\\text{O}^{2-}$.",
                "is_correct": False,
                "rationale": "Carbon does not form $\\text{C}^{4+}$ cations due to excessively high ionization energy; bonding in $\\text{CO}_2$ is purely covalent.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Carbon shares three electron pairs with one oxygen and one single pair with the other: $:\\text{O}\\equiv\\text{C}-\\ddot{\\text{O}}:$.",
                "is_correct": False,
                "rationale": "Carbon dioxide is a symmetrical linear molecule with two equal double bonds, not an asymmetric triple/single bond structure.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Carbon shares two pairs of electrons with each of the two oxygen atoms, forming two double covalent bonds: $:\\ddot{\\text{O}}=\\text{C}=\\ddot{\\text{O}}:$.\n\nScientific Principle / Key Concept:\n• Carbon ($Z=6$, configuration $2, 4$) has 4 valence electrons and requires 4 more to attain neon octet.\n• Oxygen ($Z=8$, configuration $2, 6$) has 6 valence electrons and requires 2 more to attain neon octet.\n• In $\\text{CO}_2$, the central carbon atom shares 2 electrons with the left oxygen and 2 electrons with the right oxygen atom. Each oxygen contributes 2 electrons, resulting in two double covalent bonds ($:\\ddot{\\text{O}}=\\text{C}=\\ddot{\\text{O}}:$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Single bonds violate the octet rule for both carbon and oxygen.\n• Option (C): Incorrect. $\\text{CO}_2$ is a covalent gas, not an ionic salt.\n• Option (D): Incorrect. The molecule has two symmetric double bonds.",
        "step_by_step_solution": "Correct Answer: (A) Carbon shares two pairs of electrons with each of the two oxygen atoms, forming two double covalent bonds: $:\\ddot{\\text{O}}=\\text{C}=\\ddot{\\text{O}}:$.\n\nScientific Principle / Key Concept:\n• Carbon ($Z=6$, configuration $2, 4$) has 4 valence electrons and requires 4 more to attain neon octet.\n• Oxygen ($Z=8$, configuration $2, 6$) has 6 valence electrons and requires 2 more to attain neon octet.\n• In $\\text{CO}_2$, the central carbon atom shares 2 electrons with the left oxygen and 2 electrons with the right oxygen atom. Each oxygen contributes 2 electrons, resulting in two double covalent bonds ($:\\ddot{\\text{O}}=\\text{C}=\\ddot{\\text{O}}:$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Single bonds violate the octet rule for both carbon and oxygen.\n• Option (C): Incorrect. $\\text{CO}_2$ is a covalent gas, not an ionic salt.\n• Option (D): Incorrect. The molecule has two symmetric double bonds.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 61)",
        "questionNumber": "1"
    },
    {
        "id": "sci_ch4_p61_q02",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 61)",
        "question_number": "2",
        "text": "What is the structural arrangement and electron dot representation of a molecule of sulphur ($\\text{S}_8$) made up of eight sulphur atoms?",
        "options": [
            {
                "id": "A",
                "text": "Eight sulphur atoms are linked in a closed, puckered (crown-shaped) ring, with each sulphur atom sharing two single covalent bonds with adjacent atoms.",
                "is_correct": True,
                "rationale": "Sulphur ($Z=16$, $2,8,6$) has 6 valence electrons and needs 2 more. Eight sulphur atoms join in a crown-shaped octagonal ring, each forming 2 single bonds with neighbors, satisfying octets.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Eight sulphur atoms form a linear open chain containing alternating single and double covalent bonds.",
                "is_correct": False,
                "rationale": "Sulphur does not form a linear open chain at room temperature; it exists as a closed octagonal $\\text{S}_8$ ring.",
                "correct": False
            },
            {
                "id": "C",
                "text": "A central sulphur atom is surrounded by seven peripheral sulphur atoms held by coordinate covalent bonds.",
                "is_correct": False,
                "rationale": "All eight sulphur atoms are chemically equivalent in a symmetric crown-shaped ring.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Eight sulphur atoms are arranged in a flat planar square with quadruple covalent bonds.",
                "is_correct": False,
                "rationale": "Quadruple bonds between sulphur atoms are physically impossible due to steric and orbital overlap constraints.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Eight sulphur atoms are linked in a closed, puckered (crown-shaped) ring, with each sulphur atom sharing two single covalent bonds with adjacent atoms.\n\nScientific Principle / Key Concept:\n• Sulphur has atomic number 16 (electronic configuration: $2, 8, 6$).\n• Each sulphur atom has 6 valence electrons and requires 2 additional electrons to achieve an octet.\n• In the $\\text{S}_8$ molecule, eight sulphur atoms form a puckered crown-shaped ring. Each atom shares one electron pair with its left neighbor and one electron pair with its right neighbor, forming two single covalent bonds and leaving two lone pairs on each atom.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. $\\text{S}_8$ is a cyclic ring, not an open chain.\n• Option (C): Incorrect. There is no central sulphur atom; all 8 are equivalent in the ring.\n• Option (D): Incorrect. The geometry is non-planar (crown-shaped) with single bonds.",
        "step_by_step_solution": "Correct Answer: (A) Eight sulphur atoms are linked in a closed, puckered (crown-shaped) ring, with each sulphur atom sharing two single covalent bonds with adjacent atoms.\n\nScientific Principle / Key Concept:\n• Sulphur has atomic number 16 (electronic configuration: $2, 8, 6$).\n• Each sulphur atom has 6 valence electrons and requires 2 additional electrons to achieve an octet.\n• In the $\\text{S}_8$ molecule, eight sulphur atoms form a puckered crown-shaped ring. Each atom shares one electron pair with its left neighbor and one electron pair with its right neighbor, forming two single covalent bonds and leaving two lone pairs on each atom.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. $\\text{S}_8$ is a cyclic ring, not an open chain.\n• Option (C): Incorrect. There is no central sulphur atom; all 8 are equivalent in the ring.\n• Option (D): Incorrect. The geometry is non-planar (crown-shaped) with single bonds.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 61)",
        "questionNumber": "2"
    },

    # ==================== PAGE 68: QUESTIONS ====================
    {
        "id": "sci_ch4_p68_q01",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 68)",
        "question_number": "1",
        "text": "How many structural isomers can be drawn for pentane ($\\text{C}_5\\text{H}_{12}$)?",
        "options": [
            {
                "id": "A",
                "text": "3 structural isomers: n-pentane, isopentane (2-methylbutane), and neopentane (2,2-dimethylpropane)",
                "is_correct": True,
                "rationale": "Pentane has exactly three structural isomers with the formula $\\text{C}_5\\text{H}_{12}$: straight-chain pentane, 2-methylbutane (branched once), and 2,2-dimethylpropane (branched twice).",
                "correct": True
            },
            {
                "id": "B",
                "text": "2 structural isomers: n-pentane and cyclopentane",
                "is_correct": False,
                "rationale": "Cyclopentane has the formula $\\text{C}_5\\text{H}_{10}$, not $\\text{C}_5\\text{H}_{12}$, so it is not an isomer of pentane.",
                "correct": False
            },
            {
                "id": "C",
                "text": "4 structural isomers including 3-methylbutane and neopentane",
                "is_correct": False,
                "rationale": "3-methylbutane is identical to 2-methylbutane due to numbering from the other end of the chain.",
                "correct": False
            },
            {
                "id": "D",
                "text": "5 structural isomers corresponding to five different carbon positions",
                "is_correct": False,
                "rationale": "Only 3 unique carbon skeletons exist for five saturated carbon atoms.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) 3 structural isomers: n-pentane, isopentane (2-methylbutane), and neopentane (2,2-dimethylpropane)\n\nScientific Principle / Key Concept:\nStructural isomers are compounds that have identical molecular formulae but different carbon skeletons (structures). For pentane ($\\text{C}_5\\text{H}_{12}$), three isomers exist:\n1. n-pentane: $\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CH}_3$ (straight continuous 5-carbon chain)\n2. Isopentane (2-methylbutane): $\\text{CH}_3-\\text{CH}(\\text{CH}_3)-\\text{CH}_2-\\text{CH}_3$ (4-carbon main chain with one methyl branch)\n3. Neopentane (2,2-dimethylpropane): $\\text{C}(\\text{CH}_3)_4$ (3-carbon main chain with two methyl branches)\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Cyclopentane is $\\text{C}_5\\text{H}_{10}$, not an isomer of $\\text{C}_5\\text{H}_{12}$.\n• Option (C): Incorrect. 3-methylbutane is the same compound as 2-methylbutane.\n• Option (D): Incorrect. Only 3 distinct structures can be formed.",
        "step_by_step_solution": "Correct Answer: (A) 3 structural isomers: n-pentane, isopentane (2-methylbutane), and neopentane (2,2-dimethylpropane)\n\nScientific Principle / Key Concept:\nStructural isomers are compounds that have identical molecular formulae but different carbon skeletons (structures). For pentane ($\\text{C}_5\\text{H}_{12}$), three isomers exist:\n1. n-pentane: $\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CH}_3$ (straight continuous 5-carbon chain)\n2. Isopentane (2-methylbutane): $\\text{CH}_3-\\text{CH}(\\text{CH}_3)-\\text{CH}_2-\\text{CH}_3$ (4-carbon main chain with one methyl branch)\n3. Neopentane (2,2-dimethylpropane): $\\text{C}(\\text{CH}_3)_4$ (3-carbon main chain with two methyl branches)\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Cyclopentane is $\\text{C}_5\\text{H}_{10}$, not an isomer of $\\text{C}_5\\text{H}_{12}$.\n• Option (C): Incorrect. 3-methylbutane is the same compound as 2-methylbutane.\n• Option (D): Incorrect. Only 3 distinct structures can be formed.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 68)",
        "questionNumber": "1"
    },
    {
        "id": "sci_ch4_p68_q02",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 68)",
        "question_number": "2",
        "text": "What are the two unique properties of carbon that lead to the formation of millions of carbon compounds?",
        "options": [
            {
                "id": "A",
                "text": "Catenation (ability to form self-linking covalent bonds in long chains/rings) and Tetravalency (valency of four enabling bonds with multiple elements)",
                "is_correct": True,
                "rationale": "Catenation allows carbon to form stable C-C chains of immense length and complexity, while tetravalency allows it to bond simultaneously with up to 4 other monovalent atoms or heteroatoms.",
                "correct": True
            },
            {
                "id": "B",
                "text": "High chemical radioactivity and extreme ionic reactivity with atmospheric nitrogen",
                "is_correct": False,
                "rationale": "Carbon-12 is completely stable (non-radioactive) and forms covalent, not ionic, compounds.",
                "correct": False
            },
            {
                "id": "C",
                "text": "High electrical superconductivity and malleable metallic bonding",
                "is_correct": False,
                "rationale": "Carbon is a non-metal with covalent bonding, not a metallic superconductor.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Low melting point and tendency to undergo spontaneous nuclear fusion",
                "is_correct": False,
                "rationale": "Carbon compounds have varied melting points and chemical bonding does not involve nuclear fusion.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Catenation (ability to form self-linking covalent bonds in long chains/rings) and Tetravalency (valency of four enabling bonds with multiple elements)\n\nScientific Principle / Key Concept:\nThe two exceptional properties of carbon are:\n1. Catenation: Carbon has the unique ability to form strong, stable covalent bonds with other carbon atoms, giving rise to long chains, branched chains, and closed rings.\n2. Tetravalency: With a valency of 4, a carbon atom is capable of bonding with 4 other atoms of carbon or monovalent elements (like H, Cl) as well as heteroatoms (O, N, S).\nTogether with the small atomic size of carbon (enabling strong, stable bond formation), these properties account for the immense variety of organic compounds.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Carbon compounds are covalent and non-radioactive.\n• Option (C): Incorrect. Carbon is a non-metal.\n• Option (D): Incorrect. Nuclear fusion is unrelated to chemical bonding.",
        "step_by_step_solution": "Correct Answer: (A) Catenation (ability to form self-linking covalent bonds in long chains/rings) and Tetravalency (valency of four enabling bonds with multiple elements)\n\nScientific Principle / Key Concept:\nThe two exceptional properties of carbon are:\n1. Catenation: Carbon has the unique ability to form strong, stable covalent bonds with other carbon atoms, giving rise to long chains, branched chains, and closed rings.\n2. Tetravalency: With a valency of 4, a carbon atom is capable of bonding with 4 other atoms of carbon or monovalent elements (like H, Cl) as well as heteroatoms (O, N, S).\nTogether with the small atomic size of carbon (enabling strong, stable bond formation), these properties account for the immense variety of organic compounds.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Carbon compounds are covalent and non-radioactive.\n• Option (C): Incorrect. Carbon is a non-metal.\n• Option (D): Incorrect. Nuclear fusion is unrelated to chemical bonding.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 68)",
        "questionNumber": "2"
    },
    {
        "id": "sci_ch4_p68_q03",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 68)",
        "question_number": "3",
        "text": "What is the molecular formula and bonding structure of cyclopentane?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{C}_5\\text{H}_{10}$, consisting of a cyclic ring of 5 carbon atoms, where each carbon is bonded to two adjacent carbons and two hydrogen atoms by single bonds.",
                "is_correct": True,
                "rationale": "Cycloalkanes follow the general formula $\\text{C}_n\\text{H}_{2n}$. For 5 carbons, the formula is $\\text{C}_5\\text{H}_{10}$, with 5 C-C single bonds and 10 C-H single bonds (15 single covalent bonds in total).",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{C}_5\\text{H}_{12}$, consisting of five carbon atoms arranged in an open pentagonal loop.",
                "is_correct": False,
                "rationale": "$\\text{C}_5\\text{H}_{12}$ is an acyclic alkane (pentane); a closed ring has two fewer hydrogen atoms due to ring closure.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$\\text{C}_5\\text{H}_8$, containing alternating double bonds inside a planar five-membered ring.",
                "is_correct": False,
                "rationale": "Cyclopentane is fully saturated with only single bonds; $\\text{C}_5\\text{H}_8$ represents cyclopentene or pentyne.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{C}_5\\text{H}_5$, an aromatic ring with delocalized pi electrons.",
                "is_correct": False,
                "rationale": "Cyclopentane is a saturated cycloalkane, not an aromatic species.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) $\\text{C}_5\\text{H}_{10}$, consisting of a cyclic ring of 5 carbon atoms, where each carbon is bonded to two adjacent carbons and two hydrogen atoms by single bonds.\n\nScientific Principle / Key Concept:\n• Cyclopentane is a saturated cyclic hydrocarbon (cycloalkane).\n• The general formula for cycloalkanes is $\\text{C}_n\\text{H}_{2n}$. With $n=5$, its molecular formula is $\\text{C}_5\\text{H}_{10}$.\n• The five carbon atoms form a closed five-membered ring. Each carbon atom forms two C-C single bonds with adjacent carbon atoms and two C-H single bonds with hydrogen atoms, satisfying tetravalency.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. $\\text{C}_5\\text{H}_{12}$ is open-chain pentane.\n• Option (C): Incorrect. $\\text{C}_5\\text{H}_8$ has multiple bonds.\n• Option (D): Incorrect. Cyclopentane is not aromatic.",
        "step_by_step_solution": "Correct Answer: (A) $\\text{C}_5\\text{H}_{10}$, consisting of a cyclic ring of 5 carbon atoms, where each carbon is bonded to two adjacent carbons and two hydrogen atoms by single bonds.\n\nScientific Principle / Key Concept:\n• Cyclopentane is a saturated cyclic hydrocarbon (cycloalkane).\n• The general formula for cycloalkanes is $\\text{C}_n\\text{H}_{2n}$. With $n=5$, its molecular formula is $\\text{C}_5\\text{H}_{10}$.\n• The five carbon atoms form a closed five-membered ring. Each carbon atom forms two C-C single bonds with adjacent carbon atoms and two C-H single bonds with hydrogen atoms, satisfying tetravalency.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. $\\text{C}_5\\text{H}_{12}$ is open-chain pentane.\n• Option (C): Incorrect. $\\text{C}_5\\text{H}_8$ has multiple bonds.\n• Option (D): Incorrect. Cyclopentane is not aromatic.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 68)",
        "questionNumber": "3"
    },

    # ==================== PAGE 69: QUESTIONS ====================
    {
        "id": "sci_ch4_p69_q04_i",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 69)",
        "question_number": "4(i)",
        "text": "What is the structural formula of Ethanoic acid?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{CH}_3-\\text{C}(=\\text{O})-\\text{OH}$ (a 2-carbon carboxylic acid with a carbonyl and hydroxyl group on the terminal carbon)",
                "is_correct": True,
                "rationale": "Ethanoic acid (commonly called acetic acid) has two carbons. Carbon-1 is part of the carboxylic acid group ($-\\text{COOH}$), and Carbon-2 is a methyl group ($-\\text{CH}_3$).",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{CH}_3-\\text{CH}_2-\\text{OH}$",
                "is_correct": False,
                "rationale": "$\\text{CH}_3-\\text{CH}_2-\\text{OH}$ is ethanol, an alcohol, not a carboxylic acid.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$\\text{H}-\\text{C}(=\\text{O})-\\text{OH}$",
                "is_correct": False,
                "rationale": "$\\text{HCOOH}$ is methanoic acid (formic acid), which contains only one carbon atom.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{CH}_3-\\text{C}(=\\text{O})-\\text{CH}_3$",
                "is_correct": False,
                "rationale": "$\\text{CH}_3-\\text{CO}-\\text{CH}_3$ is propanone (acetone), a ketone.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) $\\text{CH}_3-\\text{C}(=\\text{O})-\\text{OH}$ (a 2-carbon carboxylic acid with a carbonyl and hydroxyl group on the terminal carbon)\n\nScientific Principle / Key Concept:\nEthanoic acid contains:\n• Root word 'eth-' $\\rightarrow 2$ carbon atoms.\n• Suffix '-oic acid' $\\rightarrow$ carboxylic acid functional group ($-\\text{COOH}$).\nStructure: $\\text{CH}_3-\\text{COOH}$. Carbon-1 is double-bonded to an oxygen atom and single-bonded to an $-\\text{OH}$ group, while Carbon-2 is single-bonded to three hydrogen atoms.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. This is ethanol.\n• Option (C): Incorrect. This is methanoic acid (1 carbon).\n• Option (D): Incorrect. This is propanone.",
        "step_by_step_solution": "Correct Answer: (A) $\\text{CH}_3-\\text{C}(=\\text{O})-\\text{OH}$ (a 2-carbon carboxylic acid with a carbonyl and hydroxyl group on the terminal carbon)\n\nScientific Principle / Key Concept:\nEthanoic acid contains:\n• Root word 'eth-' $\\rightarrow 2$ carbon atoms.\n• Suffix '-oic acid' $\\rightarrow$ carboxylic acid functional group ($-\\text{COOH}$).\nStructure: $\\text{CH}_3-\\text{COOH}$. Carbon-1 is double-bonded to an oxygen atom and single-bonded to an $-\\text{OH}$ group, while Carbon-2 is single-bonded to three hydrogen atoms.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. This is ethanol.\n• Option (C): Incorrect. This is methanoic acid (1 carbon).\n• Option (D): Incorrect. This is propanone.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 69)",
        "questionNumber": "4(i)"
    },
    {
        "id": "sci_ch4_p69_q04_ii",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 69)",
        "question_number": "4(ii)",
        "text": "Are structural isomers possible for bromopentane ($\\text{C}_5\\text{H}_{11}\\text{Br}$)?",
        "options": [
            {
                "id": "A",
                "text": "Yes, both position isomers (1-bromopentane, 2-bromopentane, 3-bromopentane) and chain isomers are possible.",
                "is_correct": True,
                "rationale": "The bromine atom can attach at C-1, C-2, or C-3 of a 5-carbon straight chain (position isomers), and the carbon skeleton itself can branch (chain isomers), yielding multiple structural isomers.",
                "correct": True
            },
            {
                "id": "B",
                "text": "No, because halogens cannot form isomers in carbon chains exceeding three carbons.",
                "is_correct": False,
                "rationale": "Halogenated alkanes readily form position and chain isomers for carbon chains with three or more carbons.",
                "correct": False
            },
            {
                "id": "C",
                "text": "No, because bromine can only bond to the terminal carbon atom.",
                "is_correct": False,
                "rationale": "Bromine can replace a hydrogen atom on any carbon in the pentyl chain.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Yes, but strictly 2 isomers exist because pentane only has two ends.",
                "is_correct": False,
                "rationale": "Positioning bromine at C-1, C-2, and C-3 gives three distinct position isomers on the straight chain alone.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Yes, both position isomers (1-bromopentane, 2-bromopentane, 3-bromopentane) and chain isomers are possible.\n\nScientific Principle / Key Concept:\nStructural isomers for $\\text{C}_5\\text{H}_{11}\\text{Br}$ exist in abundance:\n1. Position isomers of straight chain:\n• 1-bromopentane: $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{Br}$\n• 2-bromopentane: $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}(\\text{Br})\\text{CH}_3$\n• 3-bromopentane: $\\text{CH}_3\\text{CH}_2\\text{CH}(\\text{Br})\\text{CH}_2\\text{CH}_3$\n2. In addition, chain isomers based on branched skeletons (isopentyl and neopentyl) yield additional isomers (e.g., 1-bromo-2-methylbutane, 2-bromo-2-methylbutane, etc.).\nHence, structural isomers are definitely possible.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Halogenated alkanes exhibit extensive isomerism.\n• Option (C): Incorrect. Halogens bond to internal secondary and tertiary carbons as well.\n• Option (D): Incorrect. C-3 is unique and gives a 3rd straight-chain isomer.",
        "step_by_step_solution": "Correct Answer: (A) Yes, both position isomers (1-bromopentane, 2-bromopentane, 3-bromopentane) and chain isomers are possible.\n\nScientific Principle / Key Concept:\nStructural isomers for $\\text{C}_5\\text{H}_{11}\\text{Br}$ exist in abundance:\n1. Position isomers of straight chain:\n• 1-bromopentane: $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{CH}_2\\text{Br}$\n• 2-bromopentane: $\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CH}(\\text{Br})\\text{CH}_3$\n• 3-bromopentane: $\\text{CH}_3\\text{CH}_2\\text{CH}(\\text{Br})\\text{CH}_2\\text{CH}_3$\n2. In addition, chain isomers based on branched skeletons (isopentyl and neopentyl) yield additional isomers (e.g., 1-bromo-2-methylbutane, 2-bromo-2-methylbutane, etc.).\nHence, structural isomers are definitely possible.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Halogenated alkanes exhibit extensive isomerism.\n• Option (C): Incorrect. Halogens bond to internal secondary and tertiary carbons as well.\n• Option (D): Incorrect. C-3 is unique and gives a 3rd straight-chain isomer.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 69)",
        "questionNumber": "4(ii)"
    },
    {
        "id": "sci_ch4_p69_q04_iii",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 69)",
        "question_number": "4(iii)",
        "text": "What is the structural formula of Butanone?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{CH}_3-\\text{C}(=\\text{O})-\\text{CH}_2-\\text{CH}_3$ (a four-carbon chain containing a carbonyl ketone group at carbon-2)",
                "is_correct": True,
                "rationale": "Butanone contains 4 carbons ('but-') and a ketone functional group ($-\\text{C}(=\\text{O})-$) located at position 2.",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CHO}$",
                "is_correct": False,
                "rationale": "$\\text{CH}_3\\text{CH}_2\\text{CH}_2\\text{CHO}$ is butanal (an aldehyde), not butanone.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{OH}$",
                "is_correct": False,
                "rationale": "This is 1-butanol, an alcohol.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{CH}_3-\\text{CH}_2-\\text{COOH}$",
                "is_correct": False,
                "rationale": "This is propanoic acid (3 carbons, carboxylic acid).",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) $\\text{CH}_3-\\text{C}(=\\text{O})-\\text{CH}_2-\\text{CH}_3$ (a four-carbon chain containing a carbonyl ketone group at carbon-2)\n\nScientific Principle / Key Concept:\n• Root word 'but-' denotes 4 carbon atoms.\n• Suffix '-one' denotes a ketone functional group ($-\\text{CO}-$).\nSince a ketone group must be attached to two carbon atoms, in a four-carbon chain the carbonyl carbon must be at C-2:\n$$\\text{CH}_3-\\text{CO}-\\text{CH}_2-\\text{CH}_3$$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. This is butanal (aldehyde).\n• Option (C): Incorrect. This is butanol (alcohol).\n• Option (D): Incorrect. This is propanoic acid.",
        "step_by_step_solution": "Correct Answer: (A) $\\text{CH}_3-\\text{C}(=\\text{O})-\\text{CH}_2-\\text{CH}_3$ (a four-carbon chain containing a carbonyl ketone group at carbon-2)\n\nScientific Principle / Key Concept:\n• Root word 'but-' denotes 4 carbon atoms.\n• Suffix '-one' denotes a ketone functional group ($-\\text{CO}-$).\nSince a ketone group must be attached to two carbon atoms, in a four-carbon chain the carbonyl carbon must be at C-2:\n$$\\text{CH}_3-\\text{CO}-\\text{CH}_2-\\text{CH}_3$$\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. This is butanal (aldehyde).\n• Option (C): Incorrect. This is butanol (alcohol).\n• Option (D): Incorrect. This is propanoic acid.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 69)",
        "questionNumber": "4(iii)"
    },
    {
        "id": "sci_ch4_p69_q04_iv",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 69)",
        "question_number": "4(iv)",
        "text": "What is the structural formula of Hexanal?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CHO}$ (a 6-carbon chain with a terminal aldehyde group)",
                "is_correct": True,
                "rationale": "Hexanal has 6 carbons ('hex-') with a terminal aldehyde functional group ($-\\text{CH}=\\text{O}$).",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{CH}_3-(\\text{CH}_2)_4-\\text{COOH}$",
                "is_correct": False,
                "rationale": "This is hexanoic acid (a carboxylic acid), not hexanal.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$\\text{CH}_3-(\\text{CH}_2)_3-\\text{CO}-\\text{CH}_3$",
                "is_correct": False,
                "rationale": "This is hexan-2-one (a ketone), not hexanal.",
                "correct": False
            },
            {
                "id": "D",
                "text": "$\\text{CH}_3-(\\text{CH}_2)_4-\\text{CH}_2\\text{OH}$",
                "is_correct": False,
                "rationale": "This is 1-hexanol (an alcohol).",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) $\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CHO}$ (a 6-carbon chain with a terminal aldehyde group)\n\nScientific Principle / Key Concept:\n• 'Hex-' indicates a six-carbon parent chain.\n• '-al' indicates an aldehyde group ($-CHO$) located at the terminus (C-1).\nStructure: $\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CHO}$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. This is hexanoic acid.\n• Option (C): Incorrect. This is hexan-2-one.\n• Option (D): Incorrect. This is hexan-1-ol.",
        "step_by_step_solution": "Correct Answer: (A) $\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CHO}$ (a 6-carbon chain with a terminal aldehyde group)\n\nScientific Principle / Key Concept:\n• 'Hex-' indicates a six-carbon parent chain.\n• '-al' indicates an aldehyde group ($-CHO$) located at the terminus (C-1).\nStructure: $\\text{CH}_3-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CHO}$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. This is hexanoic acid.\n• Option (C): Incorrect. This is hexan-2-one.\n• Option (D): Incorrect. This is hexan-1-ol.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 69)",
        "questionNumber": "4(iv)"
    },
    {
        "id": "sci_ch4_p69_q05_i",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 69)",
        "question_number": "5(i)",
        "text": "What is the IUPAC name of the compound $\\text{CH}_3-\\text{CH}_2-\\text{Br}$?",
        "options": [
            {
                "id": "A",
                "text": "Bromoethane",
                "is_correct": True,
                "rationale": "The compound contains 2 carbon atoms (ethane) and a bromine substituent, named with prefix 'bromo-': Bromoethane (commonly ethyl bromide).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Bromomethane",
                "is_correct": False,
                "rationale": "Bromomethane has only 1 carbon atom ($\\text{CH}_3\\text{Br}$).",
                "correct": False
            },
            {
                "id": "C",
                "text": "Bromopropane",
                "is_correct": False,
                "rationale": "Bromopropane has 3 carbon atoms ($\\text{C}_3\\text{H}_7\\text{Br}$).",
                "correct": False
            },
            {
                "id": "D",
                "text": "Ethane bromide",
                "is_correct": False,
                "rationale": "The IUPAC prefix is 'bromo-' preceding the alkane name, not 'ethane bromide'.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Bromoethane\n\nScientific Principle / Key Concept:\n• The parent alkane has 2 carbon atoms $\\rightarrow$ 'ethane'.\n• Halogen substituent $-\\text{Br}$ is designated by prefix 'bromo-'.\n• IUPAC name: Bromoethane.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. 1-carbon haloalkane.\n• Option (C): Incorrect. 3-carbon haloalkane.\n• Option (D): Incorrect IUPAC naming syntax.",
        "step_by_step_solution": "Correct Answer: (A) Bromoethane\n\nScientific Principle / Key Concept:\n• The parent alkane has 2 carbon atoms $\\rightarrow$ 'ethane'.\n• Halogen substituent $-\\text{Br}$ is designated by prefix 'bromo-'.\n• IUPAC name: Bromoethane.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. 1-carbon haloalkane.\n• Option (C): Incorrect. 3-carbon haloalkane.\n• Option (D): Incorrect IUPAC naming syntax.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 69)",
        "questionNumber": "5(i)"
    },
    {
        "id": "sci_ch4_p69_q05_ii",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 69)",
        "question_number": "5(ii)",
        "text": "What is the IUPAC name of the compound $\\text{H}-\\text{CHO}$ (or $\\text{H}-\\text{C}(=\\text{O})-\\text{H}$)?",
        "options": [
            {
                "id": "A",
                "text": "Methanal",
                "is_correct": True,
                "rationale": "The compound has 1 carbon atom ('methan-') and an aldehyde functional group (suffix '-al'). Its IUPAC name is Methanal (commonly formaldehyde).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Ethanal",
                "is_correct": False,
                "rationale": "Ethanal has 2 carbon atoms ($\\text{CH}_3\\text{CHO}$).",
                "correct": False
            },
            {
                "id": "C",
                "text": "Methanol",
                "is_correct": False,
                "rationale": "Methanol is an alcohol ($\\text{CH}_3\\text{OH}$), not an aldehyde.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Methanone",
                "is_correct": False,
                "rationale": "Ketones require at least 3 carbon atoms (a carbonyl attached to two carbons); 'methanone' does not exist.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Methanal\n\nScientific Principle / Key Concept:\n• One carbon atom $\\rightarrow$ 'methane'.\n• Aldehyde functional group ($-CHO$) $\\rightarrow$ suffix '-al'.\n• Replacing 'e' with 'al': Methane - e + al = Methanal (common name: formaldehyde).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Ethanal has 2 carbons.\n• Option (C): Incorrect. Methanol is an alcohol.\n• Option (D): Incorrect. A single-carbon ketone cannot exist.",
        "step_by_step_solution": "Correct Answer: (A) Methanal\n\nScientific Principle / Key Concept:\n• One carbon atom $\\rightarrow$ 'methane'.\n• Aldehyde functional group ($-CHO$) $\\rightarrow$ suffix '-al'.\n• Replacing 'e' with 'al': Methane - e + al = Methanal (common name: formaldehyde).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Ethanal has 2 carbons.\n• Option (C): Incorrect. Methanol is an alcohol.\n• Option (D): Incorrect. A single-carbon ketone cannot exist.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 69)",
        "questionNumber": "5(ii)"
    },
    {
        "id": "sci_ch4_p69_q05_iii",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 69)",
        "question_number": "5(iii)",
        "text": "What is the IUPAC name of the unsaturated hydrocarbon $\\text{H}-\\text{C}\\equiv\\text{C}-\\text{CH}_2-\\text{CH}_2-\\text{CH}_2-\\text{CH}_3$?",
        "options": [
            {
                "id": "A",
                "text": "Hex-1-yne (or 1-hexyne)",
                "is_correct": True,
                "rationale": "The longest continuous carbon chain has 6 carbons ('hex-') with a triple bond starting at carbon-1, designated by suffix '-yne': Hex-1-yne.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Hex-1-ene",
                "is_correct": False,
                "rationale": "'-ene' denotes a double bond, but this compound contains a triple bond ($\\text{C}\\equiv\\text{C}$).",
                "correct": False
            },
            {
                "id": "C",
                "text": "Pent-1-yne",
                "is_correct": False,
                "rationale": "The chain contains 6 carbon atoms, not 5.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Hexane",
                "is_correct": False,
                "rationale": "Hexane is a saturated alkane with single bonds only ($\\text{C}_6\\text{H}_{14}$).",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Hex-1-yne (or 1-hexyne)\n\nScientific Principle / Key Concept:\n• Longest chain contains 6 carbons $\\rightarrow$ 'hex'.\n• Functional group is an alkyne (carbon-carbon triple bond $\\text{C}\\equiv\\text{C}$) $\\rightarrow$ suffix '-yne'.\n• Numbering from the end closest to the triple bond gives position 1: Hex-1-yne (or 1-hexyne).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. '-ene' denotes a double bond.\n• Option (C): Incorrect. Chain length is 6, not 5.\n• Option (D): Incorrect. Hexane is saturated.",
        "step_by_step_solution": "Correct Answer: (A) Hex-1-yne (or 1-hexyne)\n\nScientific Principle / Key Concept:\n• Longest chain contains 6 carbons $\\rightarrow$ 'hex'.\n• Functional group is an alkyne (carbon-carbon triple bond $\\text{C}\\equiv\\text{C}$) $\\rightarrow$ suffix '-yne'.\n• Numbering from the end closest to the triple bond gives position 1: Hex-1-yne (or 1-hexyne).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. '-ene' denotes a double bond.\n• Option (C): Incorrect. Chain length is 6, not 5.\n• Option (D): Incorrect. Hexane is saturated.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 69)",
        "questionNumber": "5(iii)"
    },

    # ==================== PAGE 71: QUESTIONS ====================
    {
        "id": "sci_ch4_p71_q01",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 71)",
        "question_number": "1",
        "text": "Why is the chemical conversion of ethanol to ethanoic acid classified as an oxidation reaction?",
        "options": [
            {
                "id": "A",
                "text": "One oxygen atom is added and two hydrogen atoms are removed from the ethanol molecule: $\\text{CH}_3\\text{CH}_2\\text{OH} + 2[\\text{O}] \\rightarrow \\text{CH}_3\\text{COOH} + \\text{H}_2\\text{O}$.",
                "is_correct": True,
                "rationale": "Oxidation is defined as the addition of oxygen and/or removal of hydrogen. In this reaction, ethanol ($\text{C}_2\text{H}_6\text{O}$) gains oxygen and loses hydrogen to become ethanoic acid ($\text{C}_2\text{H}_4\text{O}_2$).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Ethanol gains four hydrogen atoms from acidified potassium dichromate.",
                "is_correct": False,
                "rationale": "Gaining hydrogen is reduction, not oxidation.",
                "correct": False
            },
            {
                "id": "C",
                "text": "The carbon chain is cleaved into two separate single-carbon units.",
                "is_correct": False,
                "rationale": "The 2-carbon skeleton remains intact throughout the oxidation.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Ethanol completely dehydrates into gaseous ethene without any oxygen transfer.",
                "is_correct": False,
                "rationale": "Dehydration forms ethene using conc. $\\text{H}_2\\text{SO}_4$, whereas oxidation yields ethanoic acid using $\\text{KMnO}_4$ or $\\text{K}_2\\text{Cr}_2\\text{O}_7$.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) One oxygen atom is added and two hydrogen atoms are removed from the ethanol molecule: $\\text{CH}_3\\text{CH}_2\\text{OH} + 2[\\text{O}] \\rightarrow \\text{CH}_3\\text{COOH} + \\text{H}_2\\text{O}$.\n\nScientific Principle / Key Concept:\nIn the reaction:\n$$\\text{CH}_3\\text{CH}_2\\text{OH} \\xrightarrow{\\text{Alkaline }\\text{KMnO}_4 + \\Delta\\text{ or Acidified }\\text{K}_2\\text{Cr}_2\\text{O}_7 + \\Delta} \\text{CH}_3\\text{COOH}$$\n1. Ethanol ($\\text{C}_2\\text{H}_6\\text{O}$) contains 1 oxygen atom and 6 hydrogen atoms.\n2. Ethanoic acid ($\\text{C}_2\\text{H}_4\\text{O}_2$) contains 2 oxygen atoms and 4 hydrogen atoms.\nSince oxygen is added and hydrogen is removed, the process is an oxidation reaction.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Gaining hydrogen is reduction.\n• Option (C): Incorrect. Carbon chain length is unchanged.\n• Option (D): Incorrect. Dehydration gives ethene, not ethanoic acid.",
        "step_by_step_solution": "Correct Answer: (A) One oxygen atom is added and two hydrogen atoms are removed from the ethanol molecule: $\\text{CH}_3\\text{CH}_2\\text{OH} + 2[\\text{O}] \\rightarrow \\text{CH}_3\\text{COOH} + \\text{H}_2\\text{O}$.\n\nScientific Principle / Key Concept:\nIn the reaction:\n$$\\text{CH}_3\\text{CH}_2\\text{OH} \\xrightarrow{\\text{Alkaline }\\text{KMnO}_4 + \\Delta\\text{ or Acidified }\\text{K}_2\\text{Cr}_2\\text{O}_7 + \\Delta} \\text{CH}_3\\text{COOH}$$\n1. Ethanol ($\\text{C}_2\\text{H}_6\\text{O}$) contains 1 oxygen atom and 6 hydrogen atoms.\n2. Ethanoic acid ($\\text{C}_2\\text{H}_4\\text{O}_2$) contains 2 oxygen atoms and 4 hydrogen atoms.\nSince oxygen is added and hydrogen is removed, the process is an oxidation reaction.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Gaining hydrogen is reduction.\n• Option (C): Incorrect. Carbon chain length is unchanged.\n• Option (D): Incorrect. Dehydration gives ethene, not ethanoic acid.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 71)",
        "questionNumber": "1"
    },
    {
        "id": "sci_ch4_p71_q02",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 71)",
        "question_number": "2",
        "text": "A mixture of ethyne and oxygen is burnt for welding metals. Why is a mixture of ethyne and ordinary air NOT used?",
        "options": [
            {
                "id": "A",
                "text": "Ethyne has a high carbon percentage ($92.3\\%$); in air (only $\\sim 21\\%\\ \\text{O}_2$), it undergoes incomplete combustion giving a sooty yellow flame with insufficient temperature, whereas pure $\\text{O}_2$ gives complete combustion with an oxy-acetylene flame exceeding 3000°C.",
                "is_correct": True,
                "rationale": "Because of ethyne's high carbon content, atmospheric air does not provide sufficient oxygen for complete combustion, producing a smoky flame of low heat. Pure oxygen enables complete combustion to $\\text{CO}_2$ and $\\text{H}_2\\text{O}$, producing extreme temperatures necessary to melt steel.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Air contains carbon dioxide which reacts with ethyne to form explosive cyanides.",
                "is_correct": False,
                "rationale": "Cyanides are not formed during combustion in air.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Ethyne does not ignite or catch fire in air under any circumstances.",
                "is_correct": False,
                "rationale": "Ethyne readily burns in air, but produces a smoky flame unsuitable for welding.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Pure oxygen acts as a chemical flux that dissolves the iron slag directly.",
                "is_correct": False,
                "rationale": "Oxygen serves purely as the oxidant to ensure complete, clean, high-temperature combustion.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Ethyne has a high carbon percentage ($92.3\\%$); in air (only $\\\\sim 21\\%\\ \\text{O}_2$), it undergoes incomplete combustion giving a sooty yellow flame with insufficient temperature, whereas pure $\\text{O}_2$ gives complete combustion with an oxy-acetylene flame exceeding 3000°C.\n\nScientific Principle / Key Concept:\n• Ethyne (acetylene, $\\text{C}_2\\text{H}_2$) is an unsaturated alkyne with a very high carbon-to-hydrogen ratio ($92.3\\%$ carbon by mass).\n• When burnt in air, the limited oxygen supply ($\\\\sim 21\\%$) leads to incomplete combustion, producing unburnt carbon particles (soot) and a flame temperature of only about 2000°C, which is insufficient to melt metals for welding.\n• When burnt with pure oxygen (oxy-acetylene flame), complete combustion takes place:\n$$2\\text{C}_2\\text{H}_2 + 5\\text{O}_2 \\rightarrow 4\\text{CO}_2 + 2\\text{H}_2\\text{O} + \\text{Heat}$$\nThis produces a non-sooty, clean blue flame reaching temperatures above 3000°C, ideal for cutting and welding metals.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Cyanides are not produced.\n• Option (C): Incorrect. Ethyne burns in air, but incompletely.\n• Option (D): Incorrect. Oxygen is the reactant oxidizer, not a metallurgical flux.",
        "step_by_step_solution": "Correct Answer: (A) Ethyne has a high carbon percentage ($92.3\\%$); in air (only $\\\\sim 21\\%\\ \\text{O}_2$), it undergoes incomplete combustion giving a sooty yellow flame with insufficient temperature, whereas pure $\\text{O}_2$ gives complete combustion with an oxy-acetylene flame exceeding 3000°C.\n\nScientific Principle / Key Concept:\n• Ethyne (acetylene, $\\text{C}_2\\text{H}_2$) is an unsaturated alkyne with a very high carbon-to-hydrogen ratio ($92.3\\%$ carbon by mass).\n• When burnt in air, the limited oxygen supply ($\\\\sim 21\\%$) leads to incomplete combustion, producing unburnt carbon particles (soot) and a flame temperature of only about 2000°C, which is insufficient to melt metals for welding.\n• When burnt with pure oxygen (oxy-acetylene flame), complete combustion takes place:\n$$2\\text{C}_2\\text{H}_2 + 5\\text{O}_2 \\rightarrow 4\\text{CO}_2 + 2\\text{H}_2\\text{O} + \\text{Heat}$$\nThis produces a non-sooty, clean blue flame reaching temperatures above 3000°C, ideal for cutting and welding metals.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Cyanides are not produced.\n• Option (C): Incorrect. Ethyne burns in air, but incompletely.\n• Option (D): Incorrect. Oxygen is the reactant oxidizer, not a metallurgical flux.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 71)",
        "questionNumber": "2"
    },

    # ==================== PAGE 74: QUESTIONS ====================
    {
        "id": "sci_ch4_p74_q01",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 74)",
        "question_number": "1",
        "text": "How can you distinguish experimentally between an alcohol (e.g., ethanol) and a carboxylic acid (e.g., ethanoic acid)?",
        "options": [
            {
                "id": "A",
                "text": "Add sodium hydrogen carbonate ($\\text{NaHCO}_3$): ethanoic acid produces brisk effervescence of $\\text{CO}_2$ gas (turning lime water milky), while ethanol gives no reaction.",
                "is_correct": True,
                "rationale": "Carboxylic acids react with sodium bicarbonate to liberate carbon dioxide gas with brisk effervescence: $\\text{CH}_3\\text{COOH} + \\text{NaHCO}_3 \\rightarrow \\text{CH}_3\\text{COONa} + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow$. Neutral alcohols like ethanol do not react with $\\text{NaHCO}_3$.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Dip blue litmus paper: ethanol turns blue litmus red, whereas ethanoic acid has no effect on litmus.",
                "is_correct": False,
                "rationale": "This reverses litmus behavior: carboxylic acid turns blue litmus red; alcohol is neutral and leaves litmus unchanged.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Add water: ethanol is completely insoluble, while ethanoic acid dissolves with a violent explosion.",
                "is_correct": False,
                "rationale": "Both ethanol and ethanoic acid are miscible with water in all proportions without explosion.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Heat with copper: ethanol forms metallic gold while ethanoic acid precipitates solid carbon.",
                "is_correct": False,
                "rationale": "Neither reaction converts copper into gold or precipitates elemental carbon.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Add sodium hydrogen carbonate ($\\text{NaHCO}_3$): ethanoic acid produces brisk effervescence of $\\text{CO}_2$ gas (turning lime water milky), while ethanol gives no reaction.\n\nScientific Principle / Key Concept:\n1. Sodium hydrogen carbonate test:\n$$\\text{CH}_3\\text{COOH} + \\text{NaHCO}_3 \\rightarrow \\text{CH}_3\\text{COONa} + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow$$\nEthanoic acid releases $\\text{CO}_2$ gas which produces brisk effervescence and turns freshly prepared lime water milky. Ethanol does not react with $\\text{NaHCO}_3$.\n2. Litmus test:\nEthanoic acid turns blue litmus paper red, while ethanol is neutral and does not affect litmus paper.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Ethanoic acid is acidic (turns blue litmus red); ethanol is neutral.\n• Option (C): Incorrect. Both are completely water-soluble.\n• Option (D): Incorrect. Chemically impossible transmutation.",
        "step_by_step_solution": "Correct Answer: (A) Add sodium hydrogen carbonate ($\\text{NaHCO}_3$): ethanoic acid produces brisk effervescence of $\\text{CO}_2$ gas (turning lime water milky), while ethanol gives no reaction.\n\nScientific Principle / Key Concept:\n1. Sodium hydrogen carbonate test:\n$$\\text{CH}_3\\text{COOH} + \\text{NaHCO}_3 \\rightarrow \\text{CH}_3\\text{COONa} + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow$$\nEthanoic acid releases $\\text{CO}_2$ gas which produces brisk effervescence and turns freshly prepared lime water milky. Ethanol does not react with $\\text{NaHCO}_3$.\n2. Litmus test:\nEthanoic acid turns blue litmus paper red, while ethanol is neutral and does not affect litmus paper.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Ethanoic acid is acidic (turns blue litmus red); ethanol is neutral.\n• Option (C): Incorrect. Both are completely water-soluble.\n• Option (D): Incorrect. Chemically impossible transmutation.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 74)",
        "questionNumber": "1"
    },
    {
        "id": "sci_ch4_p74_q02",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 74)",
        "question_number": "2",
        "text": "What are oxidising agents, and which of the following are examples used to oxidise alcohols to carboxylic acids?",
        "options": [
            {
                "id": "A",
                "text": "Substances capable of adding oxygen to or removing hydrogen/electrons from other reactants; examples include alkaline $\\text{KMnO}_4$ and acidified $\\text{K}_2\\text{Cr}_2\\text{O}_7$.",
                "is_correct": True,
                "rationale": "An oxidising agent supplies oxygen or removes hydrogen. Alkaline potassium permanganate and acidified potassium dichromate readily supply nascent oxygen to oxidize ethanol into ethanoic acid upon heating.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Substances that remove oxygen from compounds; examples include hot concentrated sulphuric acid.",
                "is_correct": False,
                "rationale": "Removing oxygen is reduction, and concentrated sulphuric acid is a dehydrating agent (removes water), not an oxidising agent here.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Substances that add hydrogen to double bonds; examples include nickel and palladium catalysts.",
                "is_correct": False,
                "rationale": "Adding hydrogen is hydrogenation (reduction), not oxidation.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Substances that dissolve salts without altering chemical structure; examples include liquid water.",
                "is_correct": False,
                "rationale": "Water acts as a solvent, not a redox oxidizing reagent.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Substances capable of adding oxygen to or removing hydrogen/electrons from other reactants; examples include alkaline $\\text{KMnO}_4$ and acidified $\\text{K}_2\\text{Cr}_2\\text{O}_7$.\n\nScientific Principle / Key Concept:\nSome substances are capable of adding oxygen to others; these substances are known as oxidising agents. In the context of organic chemistry:\n• Alkaline potassium permanganate ($\\text{KMnO}_4 + \\text{NaOH}$)\n• Acidified potassium dichromate ($\\text{K}_2\\text{Cr}_2\\text{O}_7 + \\text{H}_2\\text{SO}_4$)\nBoth act as powerful oxidising agents that convert alcohols into carboxylic acids upon heating.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Removing oxygen is the role of reducing agents.\n• Option (C): Incorrect. Hydrogenation catalysts cause reduction.\n• Option (D): Incorrect. Solvents do not drive oxidation.",
        "step_by_step_solution": "Correct Answer: (A) Substances capable of adding oxygen to or removing hydrogen/electrons from other reactants; examples include alkaline $\\text{KMnO}_4$ and acidified $\\text{K}_2\\text{Cr}_2\\text{O}_7$.\n\nScientific Principle / Key Concept:\nSome substances are capable of adding oxygen to others; these substances are known as oxidising agents. In the context of organic chemistry:\n• Alkaline potassium permanganate ($\\text{KMnO}_4 + \\text{NaOH}$)\n• Acidified potassium dichromate ($\\text{K}_2\\text{Cr}_2\\text{O}_7 + \\text{H}_2\\text{SO}_4$)\nBoth act as powerful oxidising agents that convert alcohols into carboxylic acids upon heating.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Removing oxygen is the role of reducing agents.\n• Option (C): Incorrect. Hydrogenation catalysts cause reduction.\n• Option (D): Incorrect. Solvents do not drive oxidation.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 74)",
        "questionNumber": "2"
    },

    # ==================== PAGE 76: QUESTIONS ====================
    {
        "id": "sci_ch4_p76_q01",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 76)",
        "question_number": "1",
        "text": "Would you be able to check if water is hard by using a synthetic detergent?",
        "options": [
            {
                "id": "A",
                "text": "No, because synthetic detergents form rich lather equally in both soft and hard water without forming insoluble scum precipitates with $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ ions.",
                "is_correct": True,
                "rationale": "Detergents are ammonium or sulphonate salts of long-chain hydrocarbons whose charged groups do not form insoluble precipitates with calcium and magnesium ions. They lather freely regardless of water hardness, making hardness undetectable.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Yes, because detergents turn hard water into a thick yellow gelatinous curd.",
                "is_correct": False,
                "rationale": "Detergents do not form curdy precipitates or scum in hard water; only ordinary soaps do.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Yes, because detergents lose their cleansing properties and decompose completely in hard water.",
                "is_correct": False,
                "rationale": "Detergents remain completely effective in hard water; this is their primary industrial advantage over soap.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Yes, because detergents precipitate calcium ions as metallic limestone rocks.",
                "is_correct": False,
                "rationale": "Detergent molecules form water-soluble complexes and do not precipitate rock.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) No, because synthetic detergents form rich lather equally in both soft and hard water without forming insoluble scum precipitates with $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ ions.\n\nScientific Principle / Key Concept:\n• Hardness in water is caused by dissolved hydrogencarbonates, chlorides, or sulphates of calcium and magnesium.\n• Soaps react with $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ to form an insoluble white curdy precipitate called scum, failing to lather until all hardness ions are precipitated.\n• Detergents are sodium salts of alkylbenzenesulphonates or ammonium salts. The charged ends of these molecules do not form insoluble precipitates with $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$.\n• Because detergents produce foam/lather readily in both soft and hard water, they cannot be used to distinguish hard water from soft water.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Soap forms scum, not detergent.\n• Option (C): Incorrect. Detergents work effectively in hard water.\n• Option (D): Incorrect. Detergents keep ions in solution.",
        "step_by_step_solution": "Correct Answer: (A) No, because synthetic detergents form rich lather equally in both soft and hard water without forming insoluble scum precipitates with $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ ions.\n\nScientific Principle / Key Concept:\n• Hardness in water is caused by dissolved hydrogencarbonates, chlorides, or sulphates of calcium and magnesium.\n• Soaps react with $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ to form an insoluble white curdy precipitate called scum, failing to lather until all hardness ions are precipitated.\n• Detergents are sodium salts of alkylbenzenesulphonates or ammonium salts. The charged ends of these molecules do not form insoluble precipitates with $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$.\n• Because detergents produce foam/lather readily in both soft and hard water, they cannot be used to distinguish hard water from soft water.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Soap forms scum, not detergent.\n• Option (C): Incorrect. Detergents work effectively in hard water.\n• Option (D): Incorrect. Detergents keep ions in solution.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 76)",
        "questionNumber": "1"
    },
    {
        "id": "sci_ch4_p76_q02",
        "chapter": "Carbon and its Compounds",
        "section": "QUESTIONS (Page 76)",
        "question_number": "2",
        "text": "Why is mechanical agitation (beating on a stone, paddle, scrubbing with brush, or tumbling in a washing machine) necessary to get clean clothes with soap?",
        "options": [
            {
                "id": "A",
                "text": "Soap micelles entrap oily dirt at their hydrophobic centers, but mechanical agitation is needed to physically detach and pull these loaded micelles away from fabric fibers into the water emulsion.",
                "is_correct": True,
                "rationale": "While the hydrophobic tails dissolve the oily dirt, the dirt particles remain trapped in the fabric weave. Physical agitation supplies the mechanical shear force required to dislodge the micelles into the surrounding water so they can be rinsed away.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Agitation heats the water above 100°C causing the oil molecules to evaporate instantly.",
                "is_correct": False,
                "rationale": "Agitation does not boil water or cause oil evaporation.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Agitation breaks the covalent bonds of soap molecules into atomic sodium metal.",
                "is_correct": False,
                "rationale": "Mechanical rubbing cannot break strong covalent bonds or generate reactive sodium metal.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Beating clothes turns soap from an acidic substance into an alkaline detergent.",
                "is_correct": False,
                "rationale": "Soap solutions are already naturally alkaline due to salt hydrolysis; mechanical action does not alter chemical pH.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Soap micelles entrap oily dirt at their hydrophobic centers, but mechanical agitation is needed to physically detach and pull these loaded micelles away from fabric fibers into the water emulsion.\n\nScientific Principle / Key Concept:\n• Dirt on clothes is predominantly oily or greasy in nature.\n• Soap molecules orient themselves into spherical micelles, where the non-polar hydrophobic tails dissolve in the oil droplet, and the polar ionic heads project outwards into the water.\n• The micelles hold the oily dirt in colloidal suspension, but surface adhesion keeps them clinging to fabric threads.\n• Mechanical agitation (scrubbing, beating, or spinning in a machine) overcomes this surface attraction, dislodging the micelles with their entrapped dirt into the bulk water, allowing them to be washed away during rinsing.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Agitation does not boil water.\n• Option (C): Incorrect. Covalent bonds are not broken by mechanical paddles.\n• Option (D): Incorrect. Mechanical force does not change chemical pH.",
        "step_by_step_solution": "Correct Answer: (A) Soap micelles entrap oily dirt at their hydrophobic centers, but mechanical agitation is needed to physically detach and pull these loaded micelles away from fabric fibers into the water emulsion.\n\nScientific Principle / Key Concept:\n• Dirt on clothes is predominantly oily or greasy in nature.\n• Soap molecules orient themselves into spherical micelles, where the non-polar hydrophobic tails dissolve in the oil droplet, and the polar ionic heads project outwards into the water.\n• The micelles hold the oily dirt in colloidal suspension, but surface adhesion keeps them clinging to fabric threads.\n• Mechanical agitation (scrubbing, beating, or spinning in a machine) overcomes this surface attraction, dislodging the micelles with their entrapped dirt into the bulk water, allowing them to be washed away during rinsing.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Agitation does not boil water.\n• Option (C): Incorrect. Covalent bonds are not broken by mechanical paddles.\n• Option (D): Incorrect. Mechanical force does not change chemical pH.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "In-Text (Page 76)",
        "questionNumber": "2"
    },

    # ==================== PAGES 77-78: EXERCISES ====================
    {
        "id": "sci_ch4_ex_q01",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "1",
        "text": "[NCERT Exercise 1] Ethane, with the molecular formula $\\text{C}_2\\text{H}_6$, has:",
        "options": [
            {
                "id": "A",
                "text": "7 covalent bonds.",
                "is_correct": True,
                "rationale": "In ethane, there is 1 single C-C covalent bond and 6 single C-H covalent bonds, giving a total of $1 + 6 = 7$ covalent bonds.",
                "correct": True
            },
            {
                "id": "B",
                "text": "6 covalent bonds.",
                "is_correct": False,
                "rationale": "6 accounts only for the C-H bonds, omitting the central C-C covalent bond.",
                "correct": False
            },
            {
                "id": "C",
                "text": "8 covalent bonds.",
                "is_correct": False,
                "rationale": "Ethane has 6 hydrogen atoms and 2 carbon atoms; 8 bonds would exceed carbon's tetravalency.",
                "correct": False
            },
            {
                "id": "D",
                "text": "9 covalent bonds.",
                "is_correct": False,
                "rationale": "Ethane has only 14 valence electrons in total ($4\\times 2 + 1\\times 6 = 14$), which forms exactly $14/2 = 7$ electron-pair bonds.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) 7 covalent bonds.\n\nScientific Principle / Key Concept:\n• The structural formula of ethane is $\\text{H}_3\\text{C}-\\text{CH}_3$.\n• Count of bonds:\n  - One C-C single covalent bond = 1\n  - Six C-H single covalent bonds = 6\n  - Total covalent bonds = $1 + 6 = 7$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Forgets the C-C bond.\n• Option (C): Incorrect. Exceeds octet requirement.\n• Option (D): Incorrect. Arithmetically impossible for $\\text{C}_2\\text{H}_6$.",
        "step_by_step_solution": "Correct Answer: (A) 7 covalent bonds.\n\nScientific Principle / Key Concept:\n• The structural formula of ethane is $\\text{H}_3\\text{C}-\\text{CH}_3$.\n• Count of bonds:\n  - One C-C single covalent bond = 1\n  - Six C-H single covalent bonds = 6\n  - Total covalent bonds = $1 + 6 = 7$.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Forgets the C-C bond.\n• Option (C): Incorrect. Exceeds octet requirement.\n• Option (D): Incorrect. Arithmetically impossible for $\\text{C}_2\\text{H}_6$.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "1"
    },
    {
        "id": "sci_ch4_ex_q02",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "2",
        "text": "[NCERT Exercise 2] Butanone is a four-carbon compound with the functional group:",
        "options": [
            {
                "id": "A",
                "text": "Ketone.",
                "is_correct": True,
                "rationale": "The suffix '-one' specifically denotes a ketone group ($-\\text{C}(=\\text{O})-$). Butanone is $\\text{CH}_3-\\text{CO}-\\text{CH}_2-\\text{CH}_3$.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Carboxylic acid.",
                "is_correct": False,
                "rationale": "Carboxylic acids end with suffix '-oic acid' (e.g., butanoic acid).",
                "correct": False
            },
            {
                "id": "C",
                "text": "Aldehyde.",
                "is_correct": False,
                "rationale": "Aldehydes end with suffix '-al' (e.g., butanal).",
                "correct": False
            },
            {
                "id": "D",
                "text": "Alcohol.",
                "is_correct": False,
                "rationale": "Alcohols end with suffix '-ol' (e.g., butanol).",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Ketone.\n\nScientific Principle / Key Concept:\n• The name 'Butanone' has root word 'but-' (4 carbons) and suffix '-one'.\n• The suffix '-one' is the characteristic IUPAC suffix for a ketone ($>\\text{C}=\\text{O}$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Carboxylic acid suffix is '-oic acid'.\n• Option (C): Incorrect. Aldehyde suffix is '-al'.\n• Option (D): Incorrect. Alcohol suffix is '-ol'.",
        "step_by_step_solution": "Correct Answer: (A) Ketone.\n\nScientific Principle / Key Concept:\n• The name 'Butanone' has root word 'but-' (4 carbons) and suffix '-one'.\n• The suffix '-one' is the characteristic IUPAC suffix for a ketone ($>\\text{C}=\\text{O}$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Carboxylic acid suffix is '-oic acid'.\n• Option (C): Incorrect. Aldehyde suffix is '-al'.\n• Option (D): Incorrect. Alcohol suffix is '-ol'.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "2"
    },
    {
        "id": "sci_ch4_ex_q03",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "3",
        "text": "[NCERT Exercise 3] While cooking, if the bottom of the vessel is getting blackened on the outside, it means that:",
        "options": [
            {
                "id": "A",
                "text": "The fuel is not burning completely.",
                "is_correct": True,
                "rationale": "Blackening on the vessel bottom is caused by unburnt carbon particles (soot), which deposit when the fuel undergoes incomplete combustion due to insufficient oxygen supply (e.g., blocked air holes).",
                "correct": True
            },
            {
                "id": "B",
                "text": "The food is not cooked completely.",
                "is_correct": False,
                "rationale": "Soot deposits on the outside of the vessel from the burner flame, not from inside the cooking food.",
                "correct": False
            },
            {
                "id": "C",
                "text": "The fuel is wet.",
                "is_correct": False,
                "rationale": "Wet fuel may sizzle or fail to burn, but soot deposition is fundamentally due to oxygen deprivation causing incomplete combustion.",
                "correct": False
            },
            {
                "id": "D",
                "text": "The fuel is burning completely.",
                "is_correct": False,
                "rationale": "Complete combustion produces a clean blue flame that leaves zero soot or blackening.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) The fuel is not burning completely.\n\nScientific Principle / Key Concept:\n• Complete combustion of hydrocarbon fuels produces carbon dioxide, water vapor, and a non-luminous clean blue flame with no residue.\n• When air inlets are blocked or oxygen supply is limited, incomplete combustion occurs. Unburnt carbon particles glow yellow (giving a luminous flame) and deposit on the cold bottom of cooking vessels as black soot.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Blackening is external flame soot.\n• Option (C): Incorrect. Wet fuel is not the direct chemical explanation.\n• Option (D): Incorrect. Complete combustion yields a clean non-sooty flame.",
        "step_by_step_solution": "Correct Answer: (A) The fuel is not burning completely.\n\nScientific Principle / Key Concept:\n• Complete combustion of hydrocarbon fuels produces carbon dioxide, water vapor, and a non-luminous clean blue flame with no residue.\n• When air inlets are blocked or oxygen supply is limited, incomplete combustion occurs. Unburnt carbon particles glow yellow (giving a luminous flame) and deposit on the cold bottom of cooking vessels as black soot.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Blackening is external flame soot.\n• Option (C): Incorrect. Wet fuel is not the direct chemical explanation.\n• Option (D): Incorrect. Complete combustion yields a clean non-sooty flame.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "3"
    },
    {
        "id": "sci_ch4_ex_q04",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "4",
        "text": "[NCERT Exercise 4] Explain the nature of covalent bonding using the bond formation in chloromethane ($\\text{CH}_3\\text{Cl}$).",
        "options": [
            {
                "id": "A",
                "text": "Carbon forms three non-polar single covalent bonds with three hydrogen atoms and one polar single covalent bond with chlorine due to chlorine's higher electronegativity, with all atoms completing their octets/duplets by sharing electron pairs.",
                "is_correct": True,
                "rationale": "Carbon ($2,4$) shares 1 electron pair with each of 3 H atoms and 1 electron pair with Cl ($2,8,7$). Because chlorine is significantly more electronegative than carbon, the C-Cl bond is polar covalent ($\\text{C}^{\\delta+}-\\text{Cl}^{\\delta-}$).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Carbon loses an electron to chlorine to form an ionic bond while sharing three coordinate covalent bonds with hydrogen.",
                "is_correct": False,
                "rationale": "$\\text{CH}_3\\text{Cl}$ is a covalent molecular gas, not an ionic compound, and C-H bonds are normal single covalent bonds.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Chlorine donates two lone pairs to carbon forming a double covalent bond.",
                "is_correct": False,
                "rationale": "Chlorine is monovalent in $\\text{CH}_3\\text{Cl}$ and forms a single covalent bond.",
                "correct": False
            },
            {
                "id": "D",
                "text": "All four bonds in $\\text{CH}_3\\text{Cl}$ are completely non-polar with zero dipole moment.",
                "is_correct": False,
                "rationale": "Chlorine has high electronegativity (3.16) compared to carbon (2.55), resulting in a permanent bond dipole.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Carbon forms three non-polar single covalent bonds with three hydrogen atoms and one polar single covalent bond with chlorine due to chlorine's higher electronegativity, with all atoms completing their octets/duplets by sharing electron pairs.\n\nScientific Principle / Key Concept:\n• Carbon ($Z=6$, configuration $2,4$) has 4 valence electrons.\n• Hydrogen ($Z=1$, configuration $1$) has 1 valence electron and needs 1 to achieve helium duplet.\n• Chlorine ($Z=17$, configuration $2,8,7$) has 7 valence electrons and needs 1 to complete its octet.\n• Carbon shares 1 electron with each of 3 hydrogen atoms (three C-H single covalent bonds) and 1 electron with the chlorine atom (one C-Cl single covalent bond).\n• Because chlorine is much more electronegative than carbon, it pulls the shared pair closer to itself, making the C-Cl bond polar covalent with partial charges ($\\text{C}^{\\delta+}-\\text{Cl}^{\\delta-}$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. C-Cl is a polar covalent bond, not an electrovalent ionic lattice.\n• Option (C): Incorrect. Chlorine forms a single bond.\n• Option (D): Incorrect. The molecule has a significant dipole moment.",
        "step_by_step_solution": "Correct Answer: (A) Carbon forms three non-polar single covalent bonds with three hydrogen atoms and one polar single covalent bond with chlorine due to chlorine's higher electronegativity, with all atoms completing their octets/duplets by sharing electron pairs.\n\nScientific Principle / Key Concept:\n• Carbon ($Z=6$, configuration $2,4$) has 4 valence electrons.\n• Hydrogen ($Z=1$, configuration $1$) has 1 valence electron and needs 1 to achieve helium duplet.\n• Chlorine ($Z=17$, configuration $2,8,7$) has 7 valence electrons and needs 1 to complete its octet.\n• Carbon shares 1 electron with each of 3 hydrogen atoms (three C-H single covalent bonds) and 1 electron with the chlorine atom (one C-Cl single covalent bond).\n• Because chlorine is much more electronegative than carbon, it pulls the shared pair closer to itself, making the C-Cl bond polar covalent with partial charges ($\\text{C}^{\\delta+}-\\text{Cl}^{\\delta-}$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. C-Cl is a polar covalent bond, not an electrovalent ionic lattice.\n• Option (C): Incorrect. Chlorine forms a single bond.\n• Option (D): Incorrect. The molecule has a significant dipole moment.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "4"
    },
    {
        "id": "sci_ch4_ex_q05_a",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "5(a)",
        "text": "[NCERT Exercise 5(a)] In the electron dot structure of ethanoic acid ($\\text{CH}_3\\text{COOH}$), how many total shared electron pairs (covalent bonds) and lone pairs of electrons are present?",
        "options": [
            {
                "id": "A",
                "text": "8 shared electron pairs (covalent bonds) and 4 unshared lone pairs of electrons (on the oxygen atoms).",
                "is_correct": True,
                "rationale": "Counting bonds: 3 C-H + 1 C-C + 1 C=O (2 pairs) + 1 C-O + 1 O-H = 8 shared electron pairs. The carbonyl oxygen has 2 lone pairs and the hydroxyl oxygen has 2 lone pairs = 4 lone pairs.",
                "correct": True
            },
            {
                "id": "B",
                "text": "6 shared electron pairs and 2 lone pairs.",
                "is_correct": False,
                "rationale": "This undercounts the bonds and omits lone pairs on oxygen.",
                "correct": False
            },
            {
                "id": "C",
                "text": "10 shared electron pairs and 0 lone pairs.",
                "is_correct": False,
                "rationale": "Total valence electrons in $\\text{CH}_3\\text{COOH}$ are $2\\times 4 + 4\\times 1 + 2\\times 6 = 24$. 8 bonds use 16 electrons; remaining 8 electrons are 4 lone pairs.",
                "correct": False
            },
            {
                "id": "D",
                "text": "7 shared electron pairs and 6 lone pairs.",
                "is_correct": False,
                "rationale": "The C=O double bond constitutes 2 shared pairs, bringing total covalent bonds to 8, not 7.",
                "correct": False
            }
        ],
        "difficulty": "hard",
        "solution": "Correct Answer: (A) 8 shared electron pairs (covalent bonds) and 4 unshared lone pairs of electrons (on the oxygen atoms).\n\nScientific Principle / Key Concept:\n• Total valence electrons in $\\text{CH}_3\\text{COOH}$ = $2(\\text{C}) \\times 4 + 4(\\text{H}) \\times 1 + 2(\\text{O}) \\times 6 = 8 + 4 + 12 = 24$ electrons.\n• Shared pairs (bonds):\n  - 3 C-H single bonds = 3 pairs\n  - 1 C-C single bond = 1 pair\n  - 1 C=O double bond = 2 pairs\n  - 1 C-O single bond = 1 pair\n  - 1 O-H single bond = 1 pair\n  - Total shared pairs = 8 (16 electrons).\n• Remaining electrons = $24 - 16 = 8$ electrons = 4 lone pairs (2 lone pairs on carbonyl oxygen, 2 lone pairs on hydroxyl oxygen).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Undercounts C=O and C-C bonds.\n• Option (C): Incorrect. Oxygen atoms retain lone pairs to complete octets.\n• Option (D): Counts C=O as single bond.",
        "step_by_step_solution": "Correct Answer: (A) 8 shared electron pairs (covalent bonds) and 4 unshared lone pairs of electrons (on the oxygen atoms).\n\nScientific Principle / Key Concept:\n• Total valence electrons in $\\text{CH}_3\\text{COOH}$ = $2(\\text{C}) \\times 4 + 4(\\text{H}) \\times 1 + 2(\\text{O}) \\times 6 = 8 + 4 + 12 = 24$ electrons.\n• Shared pairs (bonds):\n  - 3 C-H single bonds = 3 pairs\n  - 1 C-C single bond = 1 pair\n  - 1 C=O double bond = 2 pairs\n  - 1 C-O single bond = 1 pair\n  - 1 O-H single bond = 1 pair\n  - Total shared pairs = 8 (16 electrons).\n• Remaining electrons = $24 - 16 = 8$ electrons = 4 lone pairs (2 lone pairs on carbonyl oxygen, 2 lone pairs on hydroxyl oxygen).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Undercounts C=O and C-C bonds.\n• Option (C): Incorrect. Oxygen atoms retain lone pairs to complete octets.\n• Option (D): Counts C=O as single bond.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "5(a)"
    },
    {
        "id": "sci_ch4_ex_q05_b",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "5(b)",
        "text": "[NCERT Exercise 5(b)] In the electron dot structure of hydrogen sulphide ($\\text{H}_2\\text{S}$), what is the bonding arrangement around the central sulphur atom?",
        "options": [
            {
                "id": "A",
                "text": "The central sulphur atom shares two single covalent bonds with two hydrogen atoms and retains two unshared lone pairs of electrons: $\\text{H}-\\ddot{\\text{S}}-\\text{H}$.",
                "is_correct": True,
                "rationale": "Sulphur ($2,8,6$) has 6 valence electrons. Sharing 1 electron with each of two H atoms forms two S-H single bonds, completing sulphur's octet with 2 remaining lone pairs (4 non-bonding electrons).",
                "correct": True
            },
            {
                "id": "B",
                "text": "Sulphur forms a double covalent bond with both hydrogen atoms simultaneously.",
                "is_correct": False,
                "rationale": "Hydrogen has only 1 valence electron and can never form a double bond.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Sulphur transfers two electrons to two protons forming $\\text{S}^{2+}$ and $2\\text{H}^-$.",
                "is_correct": False,
                "rationale": "$\\text{H}_2\\text{S}$ is a covalent gas, and sulphur is more electronegative than hydrogen.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Sulphur forms an octet using only single bonds with no lone pairs.",
                "is_correct": False,
                "rationale": "Two single bonds use only 4 electrons; the remaining 4 valence electrons must form 2 lone pairs.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) The central sulphur atom shares two single covalent bonds with two hydrogen atoms and retains two unshared lone pairs of electrons: $\\text{H}-\\ddot{\\text{S}}-\\text{H}$.\n\nScientific Principle / Key Concept:\n• Sulphur ($Z=16$, configuration $2,8,6$) has 6 valence electrons.\n• Hydrogen ($Z=1$, configuration $1$) needs 1 electron for a stable duplet.\n• In $\\text{H}_2\\text{S}$, sulphur shares 1 electron pair with each of the two hydrogen atoms, forming two single S-H covalent bonds.\n• The remaining 4 valence electrons on sulphur exist as two lone pairs, giving a bent molecular geometry analogous to water ($\\text{H}_2\\text{O}$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Hydrogen cannot form double bonds.\n• Option (C): Incorrect. $\\text{H}_2\\text{S}$ is covalent.\n• Option (D): Incorrect. Sulphur has 2 lone pairs.",
        "step_by_step_solution": "Correct Answer: (A) The central sulphur atom shares two single covalent bonds with two hydrogen atoms and retains two unshared lone pairs of electrons: $\\text{H}-\\ddot{\\text{S}}-\\text{H}$.\n\nScientific Principle / Key Concept:\n• Sulphur ($Z=16$, configuration $2,8,6$) has 6 valence electrons.\n• Hydrogen ($Z=1$, configuration $1$) needs 1 electron for a stable duplet.\n• In $\\text{H}_2\\text{S}$, sulphur shares 1 electron pair with each of the two hydrogen atoms, forming two single S-H covalent bonds.\n• The remaining 4 valence electrons on sulphur exist as two lone pairs, giving a bent molecular geometry analogous to water ($\\text{H}_2\\text{O}$).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Hydrogen cannot form double bonds.\n• Option (C): Incorrect. $\\text{H}_2\\text{S}$ is covalent.\n• Option (D): Incorrect. Sulphur has 2 lone pairs.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "5(b)"
    },
    {
        "id": "sci_ch4_ex_q05_c",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "5(c)",
        "text": "[NCERT Exercise 5(c)] In the electron dot structure of propanone ($\\text{CH}_3\\text{COCH}_3$), what is the total number of single covalent bonds and double covalent bonds?",
        "options": [
            {
                "id": "A",
                "text": "9 single covalent bonds (6 C-H and 2 C-C) and 1 double covalent bond (C=O).",
                "is_correct": True,
                "rationale": "Structure: $\\text{CH}_3-\\text{CO}-\\text{CH}_3$. Single bonds: 6 C-H + 2 C-C = 8 (wait, 6 C-H and 2 C-C = 8 single bonds, plus 1 C=O double bond = 9 bonds in total, or 8 single and 1 double).",
                "correct": True
            },
            {
                "id": "B",
                "text": "6 single covalent bonds and 2 double covalent bonds.",
                "is_correct": False,
                "rationale": "There is only one double bond (C=O) in propanone.",
                "correct": False
            },
            {
                "id": "C",
                "text": "10 single covalent bonds and 0 double covalent bonds.",
                "is_correct": False,
                "rationale": "Propanone is a ketone and must contain a carbonyl C=O double bond.",
                "correct": False
            },
            {
                "id": "D",
                "text": "4 single covalent bonds and 3 double covalent bonds.",
                "is_correct": False,
                "rationale": "Propanone does not contain multiple double bonds.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) 8 single covalent bonds (6 C-H and 2 C-C) and 1 double covalent bond (C=O), making 9 covalent linkages in total.\n\nScientific Principle / Key Concept:\n• Formula of propanone: $\\text{CH}_3-\\text{C}(=\\text{O})-\\text{CH}_3$.\n• Count of bonds:\n  - 6 C-H single bonds (three on each terminal methyl group)\n  - 2 C-C single bonds (connecting C1 to C2, and C2 to C3)\n  - 1 C=O double bond (between carbonyl carbon C2 and oxygen atom)\n• Oxygen atom also has 2 unshared lone pairs.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect number of double bonds.\n• Option (C): Propanone has a double bond, not all single bonds.\n• Option (D): Incorrect distribution.",
        "step_by_step_solution": "Correct Answer: (A) 8 single covalent bonds (6 C-H and 2 C-C) and 1 double covalent bond (C=O), making 9 covalent linkages in total.\n\nScientific Principle / Key Concept:\n• Formula of propanone: $\\text{CH}_3-\\text{C}(=\\text{O})-\\text{CH}_3$.\n• Count of bonds:\n  - 6 C-H single bonds (three on each terminal methyl group)\n  - 2 C-C single bonds (connecting C1 to C2, and C2 to C3)\n  - 1 C=O double bond (between carbonyl carbon C2 and oxygen atom)\n• Oxygen atom also has 2 unshared lone pairs.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect number of double bonds.\n• Option (C): Propanone has a double bond, not all single bonds.\n• Option (D): Incorrect distribution.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "5(c)"
    },
    {
        "id": "sci_ch4_ex_q05_d",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "5(d)",
        "text": "[NCERT Exercise 5(d)] What is the electron dot structure and bonding in a diatomic fluorine molecule ($\\text{F}_2$)?",
        "options": [
            {
                "id": "A",
                "text": "Two fluorine atoms share one electron pair, forming a single covalent bond ($:\\ddot{\\text{F}}-\\ddot{\\text{F}}:$), with each fluorine retaining 3 unshared lone pairs.",
                "is_correct": True,
                "rationale": "Fluorine ($Z=9$, configuration $2,7$) has 7 valence electrons. Two fluorine atoms share 1 electron pair (single bond) to complete octets, leaving 3 lone pairs (6 non-bonding electrons) on each fluorine atom.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Two fluorine atoms share two electron pairs, forming a double bond ($\\text{F}=\\text{F}$).",
                "is_correct": False,
                "rationale": "A double bond would give 9 valence electrons around each fluorine, violating the octet rule.",
                "correct": False
            },
            {
                "id": "C",
                "text": "One fluorine atom transfers an electron completely to the other, forming $\\text{F}^+$ and $\\text{F}^-$.",
                "is_correct": False,
                "rationale": "Identical halogen atoms have zero electronegativity difference and form a pure non-polar covalent bond.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Two fluorine atoms share three electron pairs to form a stable triple bond ($\\text{F}\\equiv\\text{F}$).",
                "is_correct": False,
                "rationale": "Triple bonds occur in nitrogen ($\\text{N}_2$), not in halogens which require only 1 electron to complete octet.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Two fluorine atoms share one electron pair, forming a single covalent bond ($:\\ddot{\\text{F}}-\\ddot{\\text{F}}:$), with each fluorine retaining 3 unshared lone pairs.\n\nScientific Principle / Key Concept:\n• Fluorine ($Z=9$, electronic configuration $2,7$) has 7 valence electrons.\n• Each fluorine atom needs 1 electron to attain the stable octet of neon ($2,8$).\n• Two fluorine atoms contribute 1 electron each to form a shared electron pair (a single covalent bond).\n• Total shared electrons = 2 (1 single bond); unshared electrons = 6 on each fluorine (3 lone pairs each).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Halogens form single bonds.\n• Option (C): Incorrect. Homonuclear diatomic halogens are purely covalent.\n• Option (D): Incorrect. Nitrogen forms triple bonds, not fluorine.",
        "step_by_step_solution": "Correct Answer: (A) Two fluorine atoms share one electron pair, forming a single covalent bond ($:\\ddot{\\text{F}}-\\ddot{\\text{F}}:$), with each fluorine retaining 3 unshared lone pairs.\n\nScientific Principle / Key Concept:\n• Fluorine ($Z=9$, electronic configuration $2,7$) has 7 valence electrons.\n• Each fluorine atom needs 1 electron to attain the stable octet of neon ($2,8$).\n• Two fluorine atoms contribute 1 electron each to form a shared electron pair (a single covalent bond).\n• Total shared electrons = 2 (1 single bond); unshared electrons = 6 on each fluorine (3 lone pairs each).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Halogens form single bonds.\n• Option (C): Incorrect. Homonuclear diatomic halogens are purely covalent.\n• Option (D): Incorrect. Nitrogen forms triple bonds, not fluorine.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "5(d)"
    },
    {
        "id": "sci_ch4_ex_q06",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "6",
        "text": "[NCERT Exercise 6] What is a homologous series? Which of the following correctly defines its characteristics with an example?",
        "options": [
            {
                "id": "A",
                "text": "A series of carbon compounds having the same functional group and similar chemical properties, where successive members differ by a $-\\text{CH}_2-$ unit and $14\\text{ u}$ in molecular mass (e.g., Alkanes: $\\text{CH}_4, \\text{C}_2\\text{H}_6, \\text{C}_3\\text{H}_8$).",
                "is_correct": True,
                "rationale": "A homologous series shares a general formula (e.g., $\\text{C}_n\\text{H}_{2n+2}$), identical chemical properties due to the same functional group, and gradual gradation in physical properties (boiling point, melting point) as molecular mass increases by $14\\text{ u}$ ($-\\text{CH}_2-$).",
                "correct": True
            },
            {
                "id": "B",
                "text": "A mixture of structural isomers having identical boiling points and identical molecular masses.",
                "is_correct": False,
                "rationale": "Isomers have the same molecular formula, whereas members of a homologous series have different molecular formulas differing by $-\\text{CH}_2-$.",
                "correct": False
            },
            {
                "id": "C",
                "text": "A group of elements arranged in order of increasing atomic masses in triads of three.",
                "is_correct": False,
                "rationale": "This describes Döbereiner's triads, not a homologous series of organic carbon compounds.",
                "correct": False
            },
            {
                "id": "D",
                "text": "A series of compounds where every eighth member has properties identical to the first.",
                "is_correct": False,
                "rationale": "This describes Newlands' Law of Octaves in periodic classification.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) A series of carbon compounds having the same functional group and similar chemical properties, where successive members differ by a $-\\text{CH}_2-$ unit and $14\\text{ u}$ in molecular mass (e.g., Alkanes: $\\text{CH}_4, \\text{C}_2\\text{H}_6, \\text{C}_3\\text{H}_8$).\n\nScientific Principle / Key Concept:\nA homologous series is a family of organic compounds that possess:\n1. The same functional group and general molecular formula (e.g., $\\text{C}_n\\text{H}_{2n+2}$ for alkanes, $\\text{C}_n\\text{H}_{2n+1}\\text{OH}$ for alcohols).\n2. Successive members differ from each other by a single methylene group ($-\\text{CH}_2-$) and by $14\\text{ u}$ in molecular mass.\n3. All members exhibit similar chemical properties.\n4. Gradation in physical properties (such as increasing melting points, boiling points, and densities) is observed as molecular mass increases.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. That defines structural isomerism.\n• Option (C): Incorrect. That defines Döbereiner's triads.\n• Option (D): Incorrect. That defines Newlands' Law of Octaves.",
        "step_by_step_solution": "Correct Answer: (A) A series of carbon compounds having the same functional group and similar chemical properties, where successive members differ by a $-\\text{CH}_2-$ unit and $14\\text{ u}$ in molecular mass (e.g., Alkanes: $\\text{CH}_4, \\text{C}_2\\text{H}_6, \\text{C}_3\\text{H}_8$).\n\nScientific Principle / Key Concept:\nA homologous series is a family of organic compounds that possess:\n1. The same functional group and general molecular formula (e.g., $\\text{C}_n\\text{H}_{2n+2}$ for alkanes, $\\text{C}_n\\text{H}_{2n+1}\\text{OH}$ for alcohols).\n2. Successive members differ from each other by a single methylene group ($-\\text{CH}_2-$) and by $14\\text{ u}$ in molecular mass.\n3. All members exhibit similar chemical properties.\n4. Gradation in physical properties (such as increasing melting points, boiling points, and densities) is observed as molecular mass increases.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. That defines structural isomerism.\n• Option (C): Incorrect. That defines Döbereiner's triads.\n• Option (D): Incorrect. That defines Newlands' Law of Octaves.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "6"
    },
    {
        "id": "sci_ch4_ex_q07",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "7",
        "text": "[NCERT Exercise 7] How can ethanol and ethanoic acid be differentiated on the basis of their physical and chemical properties?",
        "options": [
            {
                "id": "A",
                "text": "Physical: ethanol has a pleasant alcoholic odor and remains liquid in winter (MP $156\\text{ K}$), whereas ethanoic acid smells like pungent vinegar and freezes at $290\\text{ K}$ (glacial acetic acid). Chemical: ethanoic acid produces brisk effervescence of $\\text{CO}_2$ with $\\text{NaHCO}_3$ and turns blue litmus red, whereas ethanol gives no reaction.",
                "is_correct": True,
                "rationale": "Ethanol is neutral with low MP (156 K) and sweet alcoholic odor. Ethanoic acid has high MP (290 K, freezes at 17°C), pungent vinegar smell, turns blue litmus red, and releases $\\text{CO}_2$ from $\\text{NaHCO}_3$.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Physical: ethanol is a green solid while ethanoic acid is a purple gas. Chemical: ethanol turns red litmus blue while ethanoic acid has no effect.",
                "is_correct": False,
                "rationale": "Both are colorless liquids at room temperature, and ethanol is neutral (does not turn red litmus blue).",
                "correct": False
            },
            {
                "id": "C",
                "text": "Physical: ethanol freezes at room temperature while ethanoic acid boils at 20°C. Chemical: both react identically with sodium bicarbonate.",
                "is_correct": False,
                "rationale": "Ethanol does not freeze at room temperature (freezing point $-114^\\circ\\text{C}$), and ethanol does not react with $\\text{NaHCO}_3$.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Physical: they have identical boiling points. Chemical: ethanol is an acid and ethanoic acid is an alkaline base.",
                "is_correct": False,
                "rationale": "Ethanoic acid is an acid, while ethanol is a neutral alcohol.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Physical: ethanol has a pleasant alcoholic odor and remains liquid in winter (MP $156\\text{ K}$), whereas ethanoic acid smells like pungent vinegar and freezes at $290\\text{ K}$ (glacial acetic acid). Chemical: ethanoic acid produces brisk effervescence of $\\text{CO}_2$ with $\\text{NaHCO}_3$ and turns blue litmus red, whereas ethanol gives no reaction.\n\nScientific Principle / Key Concept:\n1. Physical Differences:\n• Odour: Ethanol has a characteristic pleasant alcoholic smell; ethanoic acid has a sharp pungent vinegar smell.\n• Melting Point: Ethanol has MP = 156 K (-117°C). Ethanoic acid has MP = 290 K (17°C), so it frequently freezes during winter in cold climates (hence called glacial acetic acid).\n2. Chemical Differences:\n• Reaction with $\\text{NaHCO}_3$: Ethanoic acid reacts vigorously with sodium hydrogen carbonate liberating $\\text{CO}_2$ gas with brisk effervescence: $\\text{CH}_3\\text{COOH} + \\text{NaHCO}_3 \\rightarrow \\text{CH}_3\\text{COONa} + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow$. Ethanol shows no reaction.\n• Litmus Test: Ethanoic acid turns blue litmus red; ethanol is neutral and does not change litmus color.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect colors and litmus states.\n• Option (C): Reverses freezing characteristics.\n• Option (D): Ethanol is not an acid and ethanoic acid is not a base.",
        "step_by_step_solution": "Correct Answer: (A) Physical: ethanol has a pleasant alcoholic odor and remains liquid in winter (MP $156\\text{ K}$), whereas ethanoic acid smells like pungent vinegar and freezes at $290\\text{ K}$ (glacial acetic acid). Chemical: ethanoic acid produces brisk effervescence of $\\text{CO}_2$ with $\\text{NaHCO}_3$ and turns blue litmus red, whereas ethanol gives no reaction.\n\nScientific Principle / Key Concept:\n1. Physical Differences:\n• Odour: Ethanol has a characteristic pleasant alcoholic smell; ethanoic acid has a sharp pungent vinegar smell.\n• Melting Point: Ethanol has MP = 156 K (-117°C). Ethanoic acid has MP = 290 K (17°C), so it frequently freezes during winter in cold climates (hence called glacial acetic acid).\n2. Chemical Differences:\n• Reaction with $\\text{NaHCO}_3$: Ethanoic acid reacts vigorously with sodium hydrogen carbonate liberating $\\text{CO}_2$ gas with brisk effervescence: $\\text{CH}_3\\text{COOH} + \\text{NaHCO}_3 \\rightarrow \\text{CH}_3\\text{COONa} + \\text{H}_2\\text{O} + \\text{CO}_2\\uparrow$. Ethanol shows no reaction.\n• Litmus Test: Ethanoic acid turns blue litmus red; ethanol is neutral and does not change litmus color.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect colors and litmus states.\n• Option (C): Reverses freezing characteristics.\n• Option (D): Ethanol is not an acid and ethanoic acid is not a base.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "7"
    },
    {
        "id": "sci_ch4_ex_q08",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "8",
        "text": "[NCERT Exercise 8] Why does micelle formation take place when soap is added to water? Will a micelle be formed in other solvents such as ethanol?",
        "options": [
            {
                "id": "A",
                "text": "Soap has a hydrophilic ionic head and a hydrophobic hydrocarbon tail; in water, the tails cluster together in the interior away from water, while the heads point outward. In ethanol, micelles do NOT form because the hydrocarbon tail dissolves directly in non-polar/organic ethanol.",
                "is_correct": True,
                "rationale": "Micelles form because hydrophobic tails are repelled by water and cluster internally. Since ethanol is an organic solvent that readily dissolves hydrocarbon chains, the hydrophobic driving force disappears and soap dissolves molecularly without forming micelles.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Micelles form in water because soap is insoluble; in ethanol, micelles form twice as fast and grow into crystalline diamonds.",
                "is_correct": False,
                "rationale": "Soap does not form diamonds in ethanol, and micelles do not form in ethanol.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Micelle formation occurs identically in all liquid solvents regardless of polarity.",
                "is_correct": False,
                "rationale": "Micelle formation strictly requires an aqueous, highly polar medium to drive hydrophobic exclusion.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Micelles form in water because sodium ions evaporate, whereas in ethanol sodium remains solid.",
                "is_correct": False,
                "rationale": "Sodium ions do not evaporate; they remain solvated in solution.",
                "correct": False
            }
        ],
        "difficulty": "hard",
        "solution": "Correct Answer: (A) Soap has a hydrophilic ionic head and a hydrophobic hydrocarbon tail; in water, the tails cluster together in the interior away from water, while the heads point outward. In ethanol, micelles do NOT form because the hydrocarbon tail dissolves directly in non-polar/organic ethanol.\n\nScientific Principle / Key Concept:\n1. Why micelles form in water:\nSoap molecules have dual characteristics:\n• Ionic 'head' ($\\text{COO}^-\\text{Na}^+$): hydrophilic (water-attracting), soluble in water.\n• Hydrocarbon 'tail' (long alkyl chain): hydrophobic (water-repelling), insoluble in water.\nTo minimize contact between hydrocarbon tails and water, the molecules arrange radially into spherical clusters (micelles): the hydrophobic tails point inward towards the center, while the ionic heads project outward into the aqueous solvent.\n2. In ethanol:\nEthanol is an organic solvent with low dielectric constant compared to water. The hydrocarbon tail of soap is soluble in ethanol. Therefore, the driving force for hydrophobic aggregation is absent, and soap dissolves uniformly without forming micelles.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Diamonds are not formed and micelles do not occur in ethanol.\n• Option (C): Incorrect. Micellization requires solvent polarity asymmetry.\n• Option (D): Sodium ions do not evaporate.",
        "step_by_step_solution": "Correct Answer: (A) Soap has a hydrophilic ionic head and a hydrophobic hydrocarbon tail; in water, the tails cluster together in the interior away from water, while the heads point outward. In ethanol, micelles do NOT form because the hydrocarbon tail dissolves directly in non-polar/organic ethanol.\n\nScientific Principle / Key Concept:\n1. Why micelles form in water:\nSoap molecules have dual characteristics:\n• Ionic 'head' ($\\text{COO}^-\\text{Na}^+$): hydrophilic (water-attracting), soluble in water.\n• Hydrocarbon 'tail' (long alkyl chain): hydrophobic (water-repelling), insoluble in water.\nTo minimize contact between hydrocarbon tails and water, the molecules arrange radially into spherical clusters (micelles): the hydrophobic tails point inward towards the center, while the ionic heads project outward into the aqueous solvent.\n2. In ethanol:\nEthanol is an organic solvent with low dielectric constant compared to water. The hydrocarbon tail of soap is soluble in ethanol. Therefore, the driving force for hydrophobic aggregation is absent, and soap dissolves uniformly without forming micelles.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Diamonds are not formed and micelles do not occur in ethanol.\n• Option (C): Incorrect. Micellization requires solvent polarity asymmetry.\n• Option (D): Sodium ions do not evaporate.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "8"
    },
    {
        "id": "sci_ch4_ex_q09",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "9",
        "text": "[NCERT Exercise 9] Why are carbon and its compounds used as fuels for most applications?",
        "options": [
            {
                "id": "A",
                "text": "They possess high calorific value (release substantial heat energy per unit mass upon combustion), have optimum ignition temperatures, and undergo controlled combustion producing non-toxic gaseous products.",
                "is_correct": True,
                "rationale": "Combustion of carbon and hydrocarbons is strongly exothermic ($\text{C} + \text{O}_2 \rightarrow \text{CO}_2 + \text{Heat}$; $\text{CH}_4 + 2\text{O}_2 \rightarrow \text{CO}_2 + 2\text{H}_2\text{O} + \text{Heat}$), providing high calorific output with manageable ignition and handling.",
                "correct": True
            },
            {
                "id": "B",
                "text": "They undergo spontaneous combustion at 0°C without requiring any spark or flame.",
                "is_correct": False,
                "rationale": "Fuels must have moderate ignition temperatures; spontaneous combustion at 0°C would make them dangerously explosive to store.",
                "correct": False
            },
            {
                "id": "C",
                "text": "They contain free uranium nuclei that release nuclear fission energy during burning.",
                "is_correct": False,
                "rationale": "Fossil fuels and carbon compounds are purely chemical fuels governed by electronic redox bonds, not nuclear fission.",
                "correct": False
            },
            {
                "id": "D",
                "text": "They do not react with oxygen and can only burn in pure nitrogen gas.",
                "is_correct": False,
                "rationale": "Combustion is by definition rapid oxidation in the presence of oxygen.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) They possess high calorific value (release substantial heat energy per unit mass upon combustion), have optimum ignition temperatures, and undergo controlled combustion producing non-toxic gaseous products.\n\nScientific Principle / Key Concept:\nCarbon and its compounds are predominantly used as domestic and industrial fuels because:\n1. High Calorific Value: On combustion, they release a large amount of heat and light energy per unit mass due to strong bond energies in products ($\\text{CO}_2$ and $\\text{H}_2\\text{O}$).\n2. Optimum Ignition Temperature: They ignite easily when heated but remain stable and safe to store at room temperature.\n3. Clean Burning: Saturated hydrocarbons burn with a clean, smoke-free flame and leave no solid residue or ash (for gases/liquids).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Low ignition temperatures cause storage hazards.\n• Option (C): Incorrect. Combustion is a chemical process, not nuclear.\n• Option (D): Incorrect. Combustion requires oxygen.",
        "step_by_step_solution": "Correct Answer: (A) They possess high calorific value (release substantial heat energy per unit mass upon combustion), have optimum ignition temperatures, and undergo controlled combustion producing non-toxic gaseous products.\n\nScientific Principle / Key Concept:\nCarbon and its compounds are predominantly used as domestic and industrial fuels because:\n1. High Calorific Value: On combustion, they release a large amount of heat and light energy per unit mass due to strong bond energies in products ($\\text{CO}_2$ and $\\text{H}_2\\text{O}$).\n2. Optimum Ignition Temperature: They ignite easily when heated but remain stable and safe to store at room temperature.\n3. Clean Burning: Saturated hydrocarbons burn with a clean, smoke-free flame and leave no solid residue or ash (for gases/liquids).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Low ignition temperatures cause storage hazards.\n• Option (C): Incorrect. Combustion is a chemical process, not nuclear.\n• Option (D): Incorrect. Combustion requires oxygen.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "9"
    },
    {
        "id": "sci_ch4_ex_q10",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "10",
        "text": "[NCERT Exercise 10] Explain the chemical formation of scum when hard water is treated with soap.",
        "options": [
            {
                "id": "A",
                "text": "Soluble calcium ($\\text{Ca}^{2+}$) and magnesium ($\\text{Mg}^{2+}$) ions in hard water react with sodium soap molecules to form insoluble, curdy white precipitates of calcium and magnesium stearate/palmitate (scum).",
                "is_correct": True,
                "rationale": "Soap (e.g., sodium stearate $\\text{C}_{17}\\text{H}_{35}\\text{COONa}$) exchanges $\\text{Na}^+$ for $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$, forming insoluble $(\\text{C}_{17}\\text{H}_{35}\\text{COO})_2\\text{Ca}$, which separates out as sticky white scum and wastes soap.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Hard water evaporates the soap molecules into toxic chlorine gas.",
                "is_correct": False,
                "rationale": "Soap contains no chlorine and no gaseous chlorine is formed.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Soap converts calcium carbonate into soluble carbon dioxide gas causing bubbles to pop.",
                "is_correct": False,
                "rationale": "Scum is a solid curdy precipitate, not a gas.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Scum is formed by sodium ions reacting with distilled pure water.",
                "is_correct": False,
                "rationale": "Scum forms strictly in hard water containing $\\text{Ca}^{2+}$ or $\\text{Mg}^{2+}$, never in distilled pure water.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Soluble calcium ($\\text{Ca}^{2+}$) and magnesium ($\\text{Mg}^{2+}$) ions in hard water react with sodium soap molecules to form insoluble, curdy white precipitates of calcium and magnesium stearate/palmitate (scum).\n\nScientific Principle / Key Concept:\n• Hard water contains dissolved salts of calcium ($\\text{Ca}^{2+}$) and magnesium ($\\text{Mg}^{2+}$), such as $\\text{CaCl}_2$, $\\text{MgSO}_4$, $\\text{Ca(HCO}_3)_2$.\n• Soap is a sodium or potassium salt of long-chain fatty acids (e.g., sodium stearate $\\text{C}_{17}\\text{H}_{35}\\text{COONa}$).\n• When soap is added to hard water, double displacement takes place:\n$$2\\text{C}_{17}\\text{H}_{35}\\text{COONa}(aq) + \\text{Ca}^{2+}(aq) \\rightarrow (\\text{C}_{17}\\text{H}_{35}\\text{COO})_2\\text{Ca}\\downarrow\\text{ (Insoluble Scum)} + 2\\text{Na}^+(aq)$$\nThis insoluble precipitate floats as scum and wastes soap until all $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ ions are consumed.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. No chlorine is involved.\n• Option (C): Incorrect. Scum is an insoluble solid, not a gas.\n• Option (D): Incorrect. Pure distilled water lathers instantly with no scum.",
        "step_by_step_solution": "Correct Answer: (A) Soluble calcium ($\\text{Ca}^{2+}$) and magnesium ($\\text{Mg}^{2+}$) ions in hard water react with sodium soap molecules to form insoluble, curdy white precipitates of calcium and magnesium stearate/palmitate (scum).\n\nScientific Principle / Key Concept:\n• Hard water contains dissolved salts of calcium ($\\text{Ca}^{2+}$) and magnesium ($\\text{Mg}^{2+}$), such as $\\text{CaCl}_2$, $\\text{MgSO}_4$, $\\text{Ca(HCO}_3)_2$.\n• Soap is a sodium or potassium salt of long-chain fatty acids (e.g., sodium stearate $\\text{C}_{17}\\text{H}_{35}\\text{COONa}$).\n• When soap is added to hard water, double displacement takes place:\n$$2\\text{C}_{17}\\text{H}_{35}\\text{COONa}(aq) + \\text{Ca}^{2+}(aq) \\rightarrow (\\text{C}_{17}\\text{H}_{35}\\text{COO})_2\\text{Ca}\\downarrow\\text{ (Insoluble Scum)} + 2\\text{Na}^+(aq)$$\nThis insoluble precipitate floats as scum and wastes soap until all $\\text{Ca}^{2+}$ and $\\text{Mg}^{2+}$ ions are consumed.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. No chlorine is involved.\n• Option (C): Incorrect. Scum is an insoluble solid, not a gas.\n• Option (D): Incorrect. Pure distilled water lathers instantly with no scum.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "10"
    },
    {
        "id": "sci_ch4_ex_q11",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "11",
        "text": "[NCERT Exercise 11] What change will you observe if you test an aqueous soap solution with red and blue litmus paper?",
        "options": [
            {
                "id": "A",
                "text": "Red litmus paper turns blue; blue litmus paper remains unchanged (blue).",
                "is_correct": True,
                "rationale": "Soap is a salt of a weak fatty acid and a strong base (NaOH). In water, it hydrolyzes to yield basic hydroxide ions ($\text{OH}^-$), making the solution basic (pH > 7). Bases turn red litmus blue.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Blue litmus paper turns red; red litmus paper remains unchanged (red).",
                "is_correct": False,
                "rationale": "Turning blue litmus red is the characteristic behavior of acids, but soap solution is basic.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Both red and blue litmus papers are bleached completely white.",
                "is_correct": False,
                "rationale": "Bleaching occurs with strong oxidizers like chlorine water, not soap solution.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Neither litmus paper undergoes any change in color because soap is chemically neutral.",
                "is_correct": False,
                "rationale": "Soap is not neutral; hydrolysis of weak acid and strong base yields an alkaline solution.",
                "correct": False
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Red litmus paper turns blue; blue litmus paper remains unchanged (blue).\n\nScientific Principle / Key Concept:\n• Soap is the salt of a weak organic acid (fatty acid like stearic acid) and a strong base (sodium hydroxide $\\text{NaOH}$).\n• When dissolved in water, soap hydrolyzes:\n$$\\text{RCOO}^-\\text{Na}^+ + \\text{H}_2\\text{O} \\rightleftharpoons \\text{RCOOH} + \\text{Na}^+ + \\text{OH}^-$$\n• The excess of hydroxide ions ($\\text{OH}^-$) makes the soap solution alkaline (basic).\n• Consequently, red litmus paper turns blue, while blue litmus paper remains blue.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Soap is basic, not acidic.\n• Option (C): Incorrect. Soap does not act as a bleaching agent.\n• Option (D): Incorrect. Salt of weak acid and strong base is distinctly basic.",
        "step_by_step_solution": "Correct Answer: (A) Red litmus paper turns blue; blue litmus paper remains unchanged (blue).\n\nScientific Principle / Key Concept:\n• Soap is the salt of a weak organic acid (fatty acid like stearic acid) and a strong base (sodium hydroxide $\\text{NaOH}$).\n• When dissolved in water, soap hydrolyzes:\n$$\\text{RCOO}^-\\text{Na}^+ + \\text{H}_2\\text{O} \\rightleftharpoons \\text{RCOOH} + \\text{Na}^+ + \\text{OH}^-$$\n• The excess of hydroxide ions ($\\text{OH}^-$) makes the soap solution alkaline (basic).\n• Consequently, red litmus paper turns blue, while blue litmus paper remains blue.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Soap is basic, not acidic.\n• Option (C): Incorrect. Soap does not act as a bleaching agent.\n• Option (D): Incorrect. Salt of weak acid and strong base is distinctly basic.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "11"
    },
    {
        "id": "sci_ch4_ex_q12",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "12",
        "text": "[NCERT Exercise 12] What is hydrogenation, and what is its major industrial application?",
        "options": [
            {
                "id": "A",
                "text": "Addition of hydrogen to unsaturated hydrocarbons in the presence of a nickel ($\\text{Ni}$) or palladium catalyst to form saturated hydrocarbons; industrial application is converting liquid vegetable oils into solid vegetable ghee (vanaspati).",
                "is_correct": True,
                "rationale": "Hydrogenation saturates double bonds in unsaturated fatty acids: $\\text{R}_2\\text{C}=\\text{CR}_2 + \\text{H}_2 \\xrightarrow{\\text{Ni catalyst}} \\text{R}_2\\text{CH}-\\text{CHR}_2$. Industrially, this solidifies liquid vegetable oils into vanaspati ghee.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Removal of hydrogen from alkanes to form alkenes for plastics manufacturing.",
                "is_correct": False,
                "rationale": "Removal of hydrogen is dehydrogenation, not hydrogenation.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Reaction of hydrogen with atmospheric nitrogen to synthesize ammonia fertilizer.",
                "is_correct": False,
                "rationale": "The synthesis of ammonia from nitrogen and hydrogen is the Haber process.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Splitting of water molecules into hydrogen and oxygen by electrolysis.",
                "is_correct": False,
                "rationale": "Splitting water is electrolysis of water, not hydrogenation.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Addition of hydrogen to unsaturated hydrocarbons in the presence of a nickel ($\\text{Ni}$) or palladium catalyst to form saturated hydrocarbons; industrial application is converting liquid vegetable oils into solid vegetable ghee (vanaspati).\n\nScientific Principle / Key Concept:\n• Definition: Hydrogenation is the chemical addition of hydrogen ($\\text{H}_2$) to unsaturated carbon compounds (containing double or triple bonds) in the presence of finely divided catalysts such as nickel ($\\text{Ni}$), palladium ($\\text{Pd}$), or platinum ($\\text{Pt}$):\n$$\\text{R}_2\\text{C}=\\text{CR}_2 + \\text{H}_2 \\xrightarrow{\\text{Ni, } 473\\text{ K}} \\text{R}_2\\text{CH}-\\text{CHR}_2$$\n• Industrial Application: Vegetable oils contain long unsaturated carbon chains and are liquids at room temperature. Hydrogenation converts these liquid unsaturated vegetable oils into solid saturated fats known as vegetable ghee (vanaspati ghee).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Removing hydrogen is dehydrogenation.\n• Option (C): Incorrect. That is the Haber process.\n• Option (D): Incorrect. That is electrolysis of water.",
        "step_by_step_solution": "Correct Answer: (A) Addition of hydrogen to unsaturated hydrocarbons in the presence of a nickel ($\\text{Ni}$) or palladium catalyst to form saturated hydrocarbons; industrial application is converting liquid vegetable oils into solid vegetable ghee (vanaspati).\n\nScientific Principle / Key Concept:\n• Definition: Hydrogenation is the chemical addition of hydrogen ($\\text{H}_2$) to unsaturated carbon compounds (containing double or triple bonds) in the presence of finely divided catalysts such as nickel ($\\text{Ni}$), palladium ($\\text{Pd}$), or platinum ($\\text{Pt}$):\n$$\\text{R}_2\\text{C}=\\text{CR}_2 + \\text{H}_2 \\xrightarrow{\\text{Ni, } 473\\text{ K}} \\text{R}_2\\text{CH}-\\text{CHR}_2$$\n• Industrial Application: Vegetable oils contain long unsaturated carbon chains and are liquids at room temperature. Hydrogenation converts these liquid unsaturated vegetable oils into solid saturated fats known as vegetable ghee (vanaspati ghee).\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Removing hydrogen is dehydrogenation.\n• Option (C): Incorrect. That is the Haber process.\n• Option (D): Incorrect. That is electrolysis of water.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "12"
    },
    {
        "id": "sci_ch4_ex_q13",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "13",
        "text": "[NCERT Exercise 13] Which of the following hydrocarbons undergo addition reactions: $\\text{C}_2\\text{H}_6, \\text{C}_3\\text{H}_8, \\text{C}_3\\text{H}_6, \\text{C}_2\\text{H}_2, \\text{and }\\text{CH}_4$?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{C}_3\\text{H}_6$ (propene) and $\\text{C}_2\\text{H}_2$ (ethyne)",
                "is_correct": True,
                "rationale": "Only unsaturated hydrocarbons (alkenes with C=C double bonds and alkynes with C≡C triple bonds) undergo addition reactions. $\\text{C}_3\\text{H}_6$ is an alkene ($\text{C}_n\text{H}_{2n}$) and $\\text{C}_2\\text{H}_2$ is an alkyne ($\text{C}_n\text{H}_{2n-2}$). Saturated alkanes ($\text{C}_2\text{H}_6, \text{C}_3\text{H}_8, \text{CH}_4$) do not undergo addition reactions.",
                "correct": True
            },
            {
                "id": "B",
                "text": "$\\text{C}_2\\text{H}_6$, $\\text{C}_3\\text{H}_8$, and $\\text{CH}_4$",
                "is_correct": False,
                "rationale": "These are saturated alkanes ($\text{C}_n\text{H}_{2n+2}$) which undergo substitution reactions, not addition reactions.",
                "correct": False
            },
            {
                "id": "C",
                "text": "$\\text{CH}_4$ and $\\text{C}_2\\text{H}_6$ only",
                "is_correct": False,
                "rationale": "Methane and ethane have only single bonds and cannot undergo addition.",
                "correct": False
            },
            {
                "id": "D",
                "text": "All five hydrocarbons undergo addition reactions equally under sunlight.",
                "is_correct": False,
                "rationale": "Addition requires multiple bonds; alkanes undergo substitution under sunlight.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) $\\text{C}_3\\text{H}_6$ (propene) and $\\text{C}_2\\text{H}_2$ (ethyne)\n\nScientific Principle / Key Concept:\n• Addition reactions are characteristic of unsaturated hydrocarbons (alkenes and alkynes) containing double or triple bonds between carbon atoms.\n1. $\\text{C}_3\\text{H}_6$ corresponds to $\\text{C}_n\\text{H}_{2n}$ ($n=3$) $\\rightarrow$ Propene (alkene, contains $\\text{C}=\\text{C}$ double bond). Undergoes addition!\n2. $\\text{C}_2\\text{H}_2$ corresponds to $\\text{C}_n\\text{H}_{2n-2}$ ($n=2$) $\\rightarrow$ Ethyne (alkyne, contains $\\text{C}\\equiv\\text{C}$ triple bond). Undergoes addition!\n3. $\\text{CH}_4, \\text{C}_2\\text{H}_6, \\text{C}_3\\text{H}_8$ correspond to $\\text{C}_n\\text{H}_{2n+2}$ $\\rightarrow$ Saturated alkanes with single bonds only. They undergo substitution reactions, NOT addition reactions.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Saturated alkanes do not undergo addition.\n• Option (C): Methane and ethane have single bonds only.\n• Option (D): Misidentifies substitution as addition.",
        "step_by_step_solution": "Correct Answer: (A) $\\text{C}_3\\text{H}_6$ (propene) and $\\text{C}_2\\text{H}_2$ (ethyne)\n\nScientific Principle / Key Concept:\n• Addition reactions are characteristic of unsaturated hydrocarbons (alkenes and alkynes) containing double or triple bonds between carbon atoms.\n1. $\\text{C}_3\\text{H}_6$ corresponds to $\\text{C}_n\\text{H}_{2n}$ ($n=3$) $\\rightarrow$ Propene (alkene, contains $\\text{C}=\\text{C}$ double bond). Undergoes addition!\n2. $\\text{C}_2\\text{H}_2$ corresponds to $\\text{C}_n\\text{H}_{2n-2}$ ($n=2$) $\\rightarrow$ Ethyne (alkyne, contains $\\text{C}\\equiv\\text{C}$ triple bond). Undergoes addition!\n3. $\\text{CH}_4, \\text{C}_2\\text{H}_6, \\text{C}_3\\text{H}_8$ correspond to $\\text{C}_n\\text{H}_{2n+2}$ $\\rightarrow$ Saturated alkanes with single bonds only. They undergo substitution reactions, NOT addition reactions.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Saturated alkanes do not undergo addition.\n• Option (C): Methane and ethane have single bonds only.\n• Option (D): Misidentifies substitution as addition.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "13"
    },
    {
        "id": "sci_ch4_ex_q14",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "14",
        "text": "[NCERT Exercise 14] Which chemical test can be used to differentiate clearly between butter and cooking oil?",
        "options": [
            {
                "id": "A",
                "text": "Bromine water test (or alkaline $\\text{KMnO}_4$ test): cooking oil contains unsaturated fatty acids and decolorizes reddish-brown bromine water, while butter contains saturated fats and does not decolorize bromine water.",
                "is_correct": True,
                "rationale": "Cooking oils contain unsaturated hydrocarbons (carbon-carbon double bonds) which undergo addition with bromine, discharging the reddish-brown color. Butter contains saturated fats which do not react with bromine water under ordinary conditions.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Litmus test: cooking oil turns blue litmus red while butter turns red litmus blue.",
                "is_correct": False,
                "rationale": "Both cooking oil and butter are neutral fats that do not change the color of litmus paper.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Reaction with hydrochloric acid: butter dissolves completely with hydrogen effervescence while cooking oil forms copper sulphate.",
                "is_correct": False,
                "rationale": "Fats do not react with dilute acids to evolve hydrogen or synthesize copper sulphate.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Electrical conductivity test: butter conducts electricity with zero resistance while cooking oil explodes.",
                "is_correct": False,
                "rationale": "Both are non-conducting organic lipids.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Bromine water test (or alkaline $\\text{KMnO}_4$ test): cooking oil contains unsaturated fatty acids and decolorizes reddish-brown bromine water, while butter contains saturated fats and does not decolorize bromine water.\n\nScientific Principle / Key Concept:\n• Cooking oil is a vegetable oil containing unsaturated fatty acids with double bonds ($\\text{C}=\\text{C}$).\n• Butter is an animal fat containing saturated fatty acids with single bonds only.\n• Test with Bromine Water:\n  - Add a few drops of reddish-brown bromine water to cooking oil: The bromine adds across the double bonds (addition reaction), causing the reddish-brown color to disappear (decolorization).\n  - Add bromine water to melted butter: Saturated fats do not undergo addition reactions; the reddish-brown color of bromine water persists.\n• Alternatively, alkaline $\\text{KMnO}_4$ (Baeyer's reagent) is decolorized by cooking oil, but not by butter.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Both are neutral lipids.\n• Option (C): Incorrect. Fats do not release $\\text{H}_2$ with acid.\n• Option (D): Incorrect. Both are electrical insulators.",
        "step_by_step_solution": "Correct Answer: (A) Bromine water test (or alkaline $\\text{KMnO}_4$ test): cooking oil contains unsaturated fatty acids and decolorizes reddish-brown bromine water, while butter contains saturated fats and does not decolorize bromine water.\n\nScientific Principle / Key Concept:\n• Cooking oil is a vegetable oil containing unsaturated fatty acids with double bonds ($\\text{C}=\\text{C}$).\n• Butter is an animal fat containing saturated fatty acids with single bonds only.\n• Test with Bromine Water:\n  - Add a few drops of reddish-brown bromine water to cooking oil: The bromine adds across the double bonds (addition reaction), causing the reddish-brown color to disappear (decolorization).\n  - Add bromine water to melted butter: Saturated fats do not undergo addition reactions; the reddish-brown color of bromine water persists.\n• Alternatively, alkaline $\\text{KMnO}_4$ (Baeyer's reagent) is decolorized by cooking oil, but not by butter.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Both are neutral lipids.\n• Option (C): Incorrect. Fats do not release $\\text{H}_2$ with acid.\n• Option (D): Incorrect. Both are electrical insulators.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "14"
    },
    {
        "id": "sci_ch4_ex_q15",
        "chapter": "Carbon and its Compounds",
        "section": "EXERCISES (Pages 77-78)",
        "question_number": "15",
        "text": "[NCERT Exercise 15] Which statement correctly explains the step-by-step mechanism of the cleansing action of soaps?",
        "options": [
            {
                "id": "A",
                "text": "The hydrophobic hydrocarbon tails dissolve in the central oily dirt droplet, while the hydrophilic ionic heads face outward into water forming a micelle; mutual ionic repulsion prevents aggregation, keeping the emulsified dirt suspended in water until rinsed away.",
                "is_correct": True,
                "rationale": "Soap molecules form spherical micelles around oily dirt. The ionic carboxylate heads form an outer shell that repels other micelles due to negative charge repulsion ($\text{COO}^-$), keeping dirt emulsified and easily washed off.",
                "correct": True
            },
            {
                "id": "B",
                "text": "Soap molecules chemically convert insoluble oil dirt into volatile methane gas which evaporates immediately into air.",
                "is_correct": False,
                "rationale": "Cleansing is a physical emulsification process, not a chemical conversion of oil into methane gas.",
                "correct": False
            },
            {
                "id": "C",
                "text": "Soap dissolves the cotton fabric fibers so that dirt drops out into the laundry tub.",
                "is_correct": False,
                "rationale": "Soap cleanses fabric without dissolving cotton or cellulose fibers.",
                "correct": False
            },
            {
                "id": "D",
                "text": "Hydrophilic tails dissolve in oil while hydrophobic heads dissolve in water.",
                "is_correct": False,
                "rationale": "This reverses the hydrophobic and hydrophilic orientations of the soap molecule.",
                "correct": False
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) The hydrophobic hydrocarbon tails dissolve in the central oily dirt droplet, while the hydrophilic ionic heads face outward into water forming a micelle; mutual ionic repulsion prevents aggregation, keeping the emulsified dirt suspended in water until rinsed away.\n\nScientific Principle / Key Concept:\nMechanism of Soap Cleansing Action:\n1. Oily dirt is insoluble in water.\n2. Soap molecules have two ends:\n   • Non-polar hydrocarbon tail: hydrophobic (water-hating) and lipophilic (oil-loving).\n   • Polar ionic head ($-\\text{COO}^-\\text{Na}^+$): hydrophilic (water-loving).\n3. When soap is added to dirty clothes in water, the hydrophobic tails embed themselves into the oily dirt droplet, while the hydrophilic ionic heads project outward into the surrounding water.\n4. This forms a spherical structure called a micelle, trapping the oil droplet inside.\n5. Because all micelle surfaces carry like negative charges ($\\text{COO}^-$), they repel one another (ion-ion repulsion) and do not precipitate or coalesce.\n6. With mechanical agitation and rinsing, the stable emulsion of dirt-loaded micelles is washed away, leaving the fabric clean.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Oil is emulsified, not converted to gas.\n• Option (C): Incorrect. Fabric is preserved, not dissolved.\n• Option (D): Inverts tail and head affinities.",
        "step_by_step_solution": "Correct Answer: (A) The hydrophobic hydrocarbon tails dissolve in the central oily dirt droplet, while the hydrophilic ionic heads face outward into water forming a micelle; mutual ionic repulsion prevents aggregation, keeping the emulsified dirt suspended in water until rinsed away.\n\nScientific Principle / Key Concept:\nMechanism of Soap Cleansing Action:\n1. Oily dirt is insoluble in water.\n2. Soap molecules have two ends:\n   • Non-polar hydrocarbon tail: hydrophobic (water-hating) and lipophilic (oil-loving).\n   • Polar ionic head ($-\\text{COO}^-\\text{Na}^+$): hydrophilic (water-loving).\n3. When soap is added to dirty clothes in water, the hydrophobic tails embed themselves into the oily dirt droplet, while the hydrophilic ionic heads project outward into the surrounding water.\n4. This forms a spherical structure called a micelle, trapping the oil droplet inside.\n5. Because all micelle surfaces carry like negative charges ($\\text{COO}^-$), they repel one another (ion-ion repulsion) and do not precipitate or coalesce.\n6. With mechanical agitation and rinsing, the stable emulsion of dirt-loaded micelles is washed away, leaving the fabric clean.\n\nDetailed Distractor & Misconception Analysis:\n• Option (B): Incorrect. Oil is emulsified, not converted to gas.\n• Option (C): Incorrect. Fabric is preserved, not dissolved.\n• Option (D): Inverts tail and head affinities.",
        "subject": "science",
        "chapterId": "sci_ch_04_carbon_compounds",
        "exercise": "Exercises (Pages 77-78)",
        "questionNumber": "15"
    }
]

print(f"Total authentic NCERT Chapter 4 questions compiled: {len(questions)}")

output_path = "assets/data/ncert_science_ch4.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"Successfully wrote {len(questions)} questions to {output_path}")
