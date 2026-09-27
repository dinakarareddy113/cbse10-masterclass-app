# -*- coding: utf-8 -*-
"""
Build 36 authentic Class 10 Geography Chapter 1 (Resources and Development)
questions strictly isolated from:
1. End-of-Chapter EXERCISES (Pages 11-12):
   - Q1(i), Q1(ii), Q1(iii) Multiple Choice
   - Q2(i), Q2(ii), Q2(iii) Short Answers (30 words)
   - Q3(i), Q3(ii) Long Answers (120 words)
   - Puzzle Clues 4(i) to 4(vi) (Crossword)
2. In-Text Questions, Activity & Find-Out Inquiry Prompts (Pages 1-10)
"""

import json
import os

questions = [
    # =========================================================================
    # EXERCISES (Page 11) - 1. Multiple Choice Questions
    # =========================================================================
    {
        "id": "sst_geo_ch1_ex1_i",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "1(i)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "1(i)",
        "text": "Which one of the following is the main cause of land degradation in Punjab?",
        "options": [
            {
                "id": "A",
                "text": "Over irrigation",
                "is_correct": True,
                "rationale": "In Punjab, Haryana, and western Uttar Pradesh, excessive canal irrigation causes waterlogging, which significantly increases salinity and alkalinity in the soil, leading to land degradation."
            },
            {
                "id": "B",
                "text": "Intensive cultivation",
                "is_correct": False,
                "rationale": "While intensive farming depletes soil nutrients, over-irrigation and subsequent waterlogging are specifically identified as the primary driver of soil salinity/alkalinity in Punjab."
            },
            {
                "id": "C",
                "text": "Deforestation",
                "is_correct": False,
                "rationale": "Deforestation due to mining is the primary cause of land degradation in states like Jharkhand, Chhattisgarh, and Odisha, not in agrarian Punjab."
            },
            {
                "id": "D",
                "text": "Overgrazing",
                "is_correct": False,
                "rationale": "Overgrazing is the main cause of land degradation in western states like Gujarat, Rajasthan, and Madhya Pradesh, not in Punjab."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Over irrigation\n\nGeographical Principle:\nAccording to NCERT Class 10 Geography Chapter 1, in agricultural states like Punjab, Haryana, and western Uttar Pradesh, over-irrigation is responsible for land degradation due to waterlogging, which raises the subsoil water table and brings dissolved salts to the surface, making the soil saline and alkaline.\n\nDistractor Analysis:\n• (B) Intensive cultivation: Causes nutrient depletion, but waterlogging from over-irrigation is the designated main cause.\n• (C) Deforestation: Main cause in mining states (Jharkhand, MP, Odisha).\n• (D) Overgrazing: Main cause in arid/semi-arid pastoral states (Gujarat, Rajasthan).",
        "step_by_step_solution": "Correct Answer: (A) Over irrigation\n\nGeographical Principle:\nAccording to NCERT Class 10 Geography Chapter 1, in agricultural states like Punjab, Haryana, and western Uttar Pradesh, over-irrigation is responsible for land degradation due to waterlogging, which raises the subsoil water table and brings dissolved salts to the surface, making the soil saline and alkaline.\n\nDistractor Analysis:\n• (B) Intensive cultivation: Causes nutrient depletion, but waterlogging from over-irrigation is the designated main cause.\n• (C) Deforestation: Main cause in mining states (Jharkhand, MP, Odisha).\n• (D) Overgrazing: Main cause in arid/semi-arid pastoral states (Gujarat, Rajasthan).",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex1_ii",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "1(ii)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "1(ii)",
        "text": "In which one of the following states is terrace cultivation widely practised?",
        "options": [
            {
                "id": "A",
                "text": "Uttarakhand",
                "is_correct": True,
                "rationale": "Terrace farming is widely developed in the mountainous slopes of the Western and Central Himalayas, such as Uttarakhand and Himachal Pradesh, to restrict soil erosion."
            },
            {
                "id": "B",
                "text": "Punjab",
                "is_correct": False,
                "rationale": "Punjab is predominantly a flat alluvial plain where mechanized intensive agriculture and tube-well irrigation are practiced, not terrace cultivation."
            },
            {
                "id": "C",
                "text": "Plains of Uttar Pradesh",
                "is_correct": False,
                "rationale": "The plains of Uttar Pradesh feature flat topography where contour or terrace cutting is neither applicable nor needed."
            },
            {
                "id": "D",
                "text": "Haryana",
                "is_correct": False,
                "rationale": "Haryana consists of flat plain topography with extensive canal and tubewell farming rather than slope terrace cultivation."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Uttarakhand\n\nGeographical Principle:\nTerrace cultivation involves cutting steps or wide flat benches into mountain slopes to slow down water runoff and retain soil. The Western and Central Himalayas, particularly the state of Uttarakhand, have well-developed terrace farming.\n\nDistractor Analysis:\n• (B), (C), and (D) are all northern alluvial plains with flat terrain where terrace cultivation is inapplicable.",
        "step_by_step_solution": "Correct Answer: (A) Uttarakhand\n\nGeographical Principle:\nTerrace cultivation involves cutting steps or wide flat benches into mountain slopes to slow down water runoff and retain soil. The Western and Central Himalayas, particularly the state of Uttarakhand, have well-developed terrace farming.\n\nDistractor Analysis:\n• (B), (C), and (D) are all northern alluvial plains with flat terrain where terrace cultivation is inapplicable.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex1_iii",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "1(iii)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "1(iii)",
        "text": "In which of the following states is black soil predominantly found?",
        "options": [
            {
                "id": "A",
                "text": "Maharashtra",
                "is_correct": True,
                "rationale": "Black soil (regur soil) covers the Deccan trap basalt region spread across the northwestern Deccan plateau, covering Maharashtra, Saurashtra, and Malwa."
            },
            {
                "id": "B",
                "text": "Uttar Pradesh",
                "is_correct": False,
                "rationale": "Uttar Pradesh is dominated by deep alluvial soils deposited by the Ganga-Yamuna river systems."
            },
            {
                "id": "C",
                "text": "Rajasthan",
                "is_correct": False,
                "rationale": "Western Rajasthan is predominantly covered by arid and desert soils, while eastern parts have red and yellow or alluvial soils."
            },
            {
                "id": "D",
                "text": "Jharkhand",
                "is_correct": False,
                "rationale": "Jharkhand is largely covered by red and yellow soils over crystalline igneous rocks of the Chotanagpur plateau."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Maharashtra\n\nGeographical Principle:\nBlack soils (Regur soils) are typical of the Deccan trap region made of weathered basaltic lava flows. They cover the plateaus of Maharashtra, Saurashtra, Malwa, and parts of Madhya Pradesh and Chhattisgarh.\n\nDistractor Analysis:\n• (B) UP: Alluvial soil.\n• (C) Rajasthan: Arid and sandy soils.\n• (D) Jharkhand: Red and yellow soils.",
        "step_by_step_solution": "Correct Answer: (A) Maharashtra\n\nGeographical Principle:\nBlack soils (Regur soils) are typical of the Deccan trap region made of weathered basaltic lava flows. They cover the plateaus of Maharashtra, Saurashtra, Malwa, and parts of Madhya Pradesh and Chhattisgarh.\n\nDistractor Analysis:\n• (B) UP: Alluvial soil.\n• (C) Rajasthan: Arid and sandy soils.\n• (D) Jharkhand: Red and yellow soils.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },

    # =========================================================================
    # EXERCISES (Page 11) - 2. Answer in about 30 words
    # =========================================================================
    {
        "id": "sst_geo_ch1_ex2_i_states",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "2(i)(a)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "2(i)(a)",
        "text": "[NCERT Exercise 2(i)] Which of the following groups of Indian states predominantly possess extensive deposits of black soil?",
        "options": [
            {
                "id": "A",
                "text": "Maharashtra, Madhya Pradesh, and Gujarat",
                "is_correct": True,
                "rationale": "Black soil is typical of the Deccan trap (basalt) region covering the plateaus of Maharashtra, Saurashtra (Gujarat), and Malwa (Madhya Pradesh)."
            },
            {
                "id": "B",
                "text": "Punjab, Haryana, and Uttar Pradesh",
                "is_correct": False,
                "rationale": "These states are located in the Indo-Gangetic plains and are covered by alluvial soils."
            },
            {
                "id": "C",
                "text": "Assam, Nagaland, and Meghalaya",
                "is_correct": False,
                "rationale": "Northeastern states are dominated by forest, mountain, and red lateritic soils."
            },
            {
                "id": "D",
                "text": "Rajasthan, Jammu and Kashmir, and Himachal Pradesh",
                "is_correct": False,
                "rationale": "These states feature arid, mountain, and alluvial soils."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Maharashtra, Madhya Pradesh, and Gujarat\n\nKey Concept:\nBlack soil is found over the Deccan Trap covering Maharashtra, Saurashtra, Malwa, Madhya Pradesh, and Chhattisgarh.",
        "step_by_step_solution": "Correct Answer: (A) Maharashtra, Madhya Pradesh, and Gujarat\n\nKey Concept:\nBlack soil is found over the Deccan Trap covering Maharashtra, Saurashtra, Malwa, Madhya Pradesh, and Chhattisgarh.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex2_i_crop",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "2(i)(b)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "2(i)(b)",
        "text": "[NCERT Exercise 2(i)] Which major commercial fiber crop is best suited for cultivation in black soil, giving it its traditional alternative name?",
        "options": [
            {
                "id": "A",
                "text": "Cotton (Black Cotton Soil)",
                "is_correct": True,
                "rationale": "Black soil is exceptionally ideal for growing cotton due to its high moisture-retentive clayey texture and nutrient richness, earning it the name 'black cotton soil'."
            },
            {
                "id": "B",
                "text": "Jute (Golden Fiber)",
                "is_correct": False,
                "rationale": "Jute grows best on well-drained fertile soils in flood plains renewed every year, particularly alluvial soils in West Bengal and Bihar."
            },
            {
                "id": "C",
                "text": "Tea and Coffee",
                "is_correct": False,
                "rationale": "Tea and coffee require well-drained, acidic laterite or mountain soils with high organic humus."
            },
            {
                "id": "D",
                "text": "Rubber",
                "is_correct": False,
                "rationale": "Rubber is an equatorial crop requiring moist humid climate and well-drained loamy soils, predominantly in Kerala."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Cotton (Black Cotton Soil)\n\nKey Concept:\nBlack soil is also called 'black cotton soil' because it provides ideal moisture and mineral conditions for cotton cultivation.",
        "step_by_step_solution": "Correct Answer: (A) Cotton (Black Cotton Soil)\n\nKey Concept:\nBlack soil is also called 'black cotton soil' because it provides ideal moisture and mineral conditions for cotton cultivation.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex2_ii_deltas",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "2(ii)(a)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "2(ii)(a)",
        "text": "[NCERT Exercise 2(ii)] What type of soil is predominantly deposited in the river deltas of the eastern coast of India (Mahanadi, Godavari, Krishna, and Kaveri)?",
        "options": [
            {
                "id": "A",
                "text": "Alluvial Soil",
                "is_correct": True,
                "rationale": "The deltas of the eastern coastal rivers (Mahanadi, Godavari, Krishna, and Kaveri) are composed of rich alluvial sediments deposited by flowing river waters."
            },
            {
                "id": "B",
                "text": "Laterite Soil",
                "is_correct": False,
                "rationale": "Laterite soils form in highland tropical areas under heavy rainfall and intense leaching, not in low-lying river deltas."
            },
            {
                "id": "C",
                "text": "Black Soil",
                "is_correct": False,
                "rationale": "Black soil is formed in situ from weathering of Deccan basaltic lava, whereas delta soils are transported river sediments."
            },
            {
                "id": "D",
                "text": "Arid Soil",
                "is_correct": False,
                "rationale": "Arid soils develop in hot, dry climatic zones like western Rajasthan."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Alluvial Soil\n\nKey Concept:\nAlluvial soil is found in the northern plains and eastern coastal plains, especially in the fertile deltas of the Mahanadi, Godavari, Krishna, and Kaveri rivers.",
        "step_by_step_solution": "Correct Answer: (A) Alluvial Soil\n\nKey Concept:\nAlluvial soil is found in the northern plains and eastern coastal plains, especially in the fertile deltas of the Mahanadi, Godavari, Krishna, and Kaveri rivers.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex2_ii_features",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "2(ii)(b)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "2(ii)(b)",
        "text": "[NCERT Exercise 2(ii)] Which combination correctly identifies three defining chemical and agricultural features of Alluvial soils?",
        "options": [
            {
                "id": "A",
                "text": "Adequate potash, phosphoric acid, and lime; high fertility; ideal for sugarcane, paddy, and wheat",
                "is_correct": True,
                "rationale": "NCERT explicitly lists that alluvial soils contain adequate proportions of potash, phosphoric acid, and lime, supporting dense cultivation of cereal crops."
            },
            {
                "id": "B",
                "text": "High acidity (pH < 6.0), poor potash, and high iron content; ideal only for tea and coffee",
                "is_correct": False,
                "rationale": "Acidic soils with pH < 6.0 and suitability for tea describe laterite soils, not alluvial soils."
            },
            {
                "id": "C",
                "text": "High salt concentration, lack of moisture and humus, and impermeable Kankar bottom layer",
                "is_correct": False,
                "rationale": "High salt and Kankar horizons characterize arid desert soils."
            },
            {
                "id": "D",
                "text": "Extremely low fertility, rocky texture, and rapid water percolation through coarse gravel",
                "is_correct": False,
                "rationale": "Alluvial soils are among the most fertile and intensively cultivated soils in the world."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Adequate potash, phosphoric acid, and lime; high fertility; ideal for sugarcane, paddy, and wheat\n\nKey Concept:\nAlluvial soils are chemically enriched with potash, phosphoric acid, and lime, making them intensively cultivated and densely populated.",
        "step_by_step_solution": "Correct Answer: (A) Adequate potash, phosphoric acid, and lime; high fertility; ideal for sugarcane, paddy, and wheat\n\nKey Concept:\nAlluvial soils are chemically enriched with potash, phosphoric acid, and lime, making them intensively cultivated and densely populated.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex2_iii_erosion",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "2(iii)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "2(iii)",
        "text": "[NCERT Exercise 2(iii)] Which effective soil conservation measures are specifically recommended to control soil erosion in hilly and mountainous terrains?",
        "options": [
            {
                "id": "A",
                "text": "Contour ploughing and terrace farming",
                "is_correct": True,
                "rationale": "Contour ploughing decelerates water runoff down slopes, while cutting steps for terrace cultivation restricts sheet wash and gully formation in hilly regions."
            },
            {
                "id": "B",
                "text": "Stabilisation of sand dunes by thorny bushes",
                "is_correct": False,
                "rationale": "Stabilising sand dunes with thorny scrub is a technique for arid desert plains (like Rajasthan), not mountain slopes."
            },
            {
                "id": "C",
                "text": "Deep ploughing up and down the natural slope line",
                "is_correct": False,
                "rationale": "Ploughing up and down slope creates channels that accelerate water flow and worsen erosion."
            },
            {
                "id": "D",
                "text": "Extensive flood irrigation and open pasture overgrazing",
                "is_correct": False,
                "rationale": "Over-irrigation and overgrazing severely aggravate land degradation."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Contour ploughing and terrace farming\n\nKey Concept:\nContour ploughing along elevation lines and terrace farming on slopes are the two primary soil conservation techniques for mountainous areas.",
        "step_by_step_solution": "Correct Answer: (A) Contour ploughing and terrace farming\n\nKey Concept:\nContour ploughing along elevation lines and terrace farming on slopes are the two primary soil conservation techniques for mountainous areas.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },

    # =========================================================================
    # EXERCISES (Page 11) - 3. Answer in about 120 words
    # =========================================================================
    {
        "id": "sst_geo_ch1_ex3_i_forest_policy",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "3(i)(a)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "3(i)(a)",
        "text": "[NCERT Exercise 3(i)] According to the National Forest Policy (1952), what is the desired percentage of geographical area that should be under forest cover to maintain ecological balance in India?",
        "options": [
            {
                "id": "A",
                "text": "33 per cent",
                "is_correct": True,
                "rationale": "The National Forest Policy of 1952 explicitly mandated that a minimum of 33% of the total geographical area must be under forest cover to ensure environmental stability and ecological balance."
            },
            {
                "id": "B",
                "text": "23 per cent",
                "is_correct": False,
                "rationale": "Approximately 23-24% is the actual existing forest cover in India, which is far below the policy's target."
            },
            {
                "id": "C",
                "text": "43 per cent",
                "is_correct": False,
                "rationale": "43% is the proportion of total land area in India that consists of flat agricultural and industrial plains."
            },
            {
                "id": "D",
                "text": "54 per cent",
                "is_correct": False,
                "rationale": "54% is the total potential net sown area including fallow lands, not the forest target."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) 33 per cent\n\nKey Concept:\nThe National Forest Policy of 1952 fixed the target forest cover at 33% of the national geographical area.",
        "step_by_step_solution": "Correct Answer: (A) 33 per cent\n\nKey Concept:\nThe National Forest Policy of 1952 fixed the target forest cover at 33% of the national geographical area.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex3_i_forest_growth",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "3(i)(b)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "3(i)(b)",
        "text": "[NCERT Exercise 3(i)] Why has the area under forest not increased significantly in India since 1960-61 despite national policy mandates?",
        "options": [
            {
                "id": "A",
                "text": "Rapid population expansion, agricultural encroachment, urbanisation, and multi-purpose river valley projects",
                "is_correct": True,
                "rationale": "Post-independence developmental pressures—feeding a rising population, clearing land for agriculture, urban development, mining, and large dam reservoirs—have continuously encroached upon forest land."
            },
            {
                "id": "B",
                "text": "Universal adoption of terrace farming across all plains of northern India",
                "is_correct": False,
                "rationale": "Terrace farming is practiced in hills to prevent erosion, not a factor limiting forest growth in plains."
            },
            {
                "id": "C",
                "text": "A total prohibition of afforestation and social forestry by local panchayats",
                "is_correct": False,
                "rationale": "Panchayats and community bodies actively participate in tree plantation and social forestry."
            },
            {
                "id": "D",
                "text": "Climatic cooling converting the Deccan plateau into permanent snowfields",
                "is_correct": False,
                "rationale": "Factually incorrect and geographically impossible."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Rapid population expansion, agricultural encroachment, urbanisation, and multi-purpose river valley projects\n\nKey Concept:\nDeforestation due to agricultural expansion, industrialization, and river valley projects has balanced out afforestation efforts, keeping forest growth marginal (18.11% in 1960-61 to ~24% in 2019-20).",
        "step_by_step_solution": "Correct Answer: (A) Rapid population expansion, agricultural encroachment, urbanisation, and multi-purpose river valley projects\n\nKey Concept:\nDeforestation due to agricultural expansion, industrialization, and river valley projects has balanced out afforestation efforts, keeping forest growth marginal (18.11% in 1960-61 to ~24% in 2019-20).",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex3_ii_consumption",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 11)",
        "question_number": "3(ii)",
        "exercise": "Exercises (Page 11)",
        "questionNumber": "3(ii)",
        "text": "[NCERT Exercise 3(ii)] In what primary manner have technological and economic development directly led to higher consumption and depletion of natural resources?",
        "options": [
            {
                "id": "A",
                "text": "Advanced technology enables large-scale mechanised extraction, while economic prosperity raises per-capita demand and living standards",
                "is_correct": True,
                "rationale": "Technological advancement equips human societies with powerful machinery to locate and extract previously inaccessible resources, while rising incomes increase demand for consumer goods, energy, and raw materials."
            },
            {
                "id": "B",
                "text": "Technology automatically eliminates all human need for water, minerals, and fossil fuels",
                "is_correct": False,
                "rationale": "Technological advancement increases resource exploitation rather than eliminating reliance on nature."
            },
            {
                "id": "C",
                "text": "Economic development restricts all industrial production to primitive village handicrafts",
                "is_correct": False,
                "rationale": "Economic growth transitions societies towards high-volume factory production and urbanisation."
            },
            {
                "id": "D",
                "text": "Technological progression permanently doubles the biological renewal speed of non-renewable fossil fuels",
                "is_correct": False,
                "rationale": "Fossil fuels take millions of years to form and cannot have their geologic formation cycle accelerated by technology."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Advanced technology enables large-scale mechanised extraction, while economic prosperity raises per-capita demand and living standards\n\nKey Concept:\nAs noted by Gandhiji, modern technology facilitates mass production and predatory exploitation of nature to satisfy human greed rather than basic needs.",
        "step_by_step_solution": "Correct Answer: (A) Advanced technology enables large-scale mechanised extraction, while economic prosperity raises per-capita demand and living standards\n\nKey Concept:\nAs noted by Gandhiji, modern technology facilitates mass production and predatory exploitation of nature to satisfy human greed rather than basic needs.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },

    # =========================================================================
    # EXERCISES (Pages 11-12) - 4. Crossword Puzzle Clues
    # =========================================================================
    {
        "id": "sst_geo_ch1_ex4_i_puzzle",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Pages 11-12)",
        "question_number": "4(i)",
        "exercise": "Exercises (Pages 11-12)",
        "questionNumber": "4(i)",
        "text": "[NCERT Puzzle Clue (i)] What single comprehensive term describes 'Natural endowments in the form of land, water, vegetation, and minerals'?",
        "options": [
            {
                "id": "A",
                "text": "RESOURCES",
                "is_correct": True,
                "rationale": "The word hidden horizontally in the NCERT puzzle grid is RESOURCES, defined as natural endowments used to satisfy human needs."
            },
            {
                "id": "B",
                "text": "RESERVES",
                "is_correct": False,
                "rationale": "Reserves are a subset of stock that can be put into use with existing technical know-how but are conserved for future requirements."
            },
            {
                "id": "C",
                "text": "STOCKS",
                "is_correct": False,
                "rationale": "Stock refers to materials that have the potential to satisfy needs but humans lack the technology to access."
            },
            {
                "id": "D",
                "text": "HABITAT",
                "is_correct": False,
                "rationale": "Habitat refers to the biological living environment of organisms."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) RESOURCES\n\nCrossword Solution:\nRow 3 & clue (i) corresponds to RESOURCES.",
        "step_by_step_solution": "Correct Answer: (A) RESOURCES\n\nCrossword Solution:\nRow 3 & clue (i) corresponds to RESOURCES.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex4_ii_puzzle",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Pages 11-12)",
        "question_number": "4(ii)",
        "exercise": "Exercises (Pages 11-12)",
        "questionNumber": "4(ii)",
        "text": "[NCERT Puzzle Clue (ii)] Which term in the puzzle grid identifies 'A vital type of non-renewable resource' formed over geological epochs?",
        "options": [
            {
                "id": "A",
                "text": "MINERALS",
                "is_correct": True,
                "rationale": "MINERALS appears horizontally across Row 6 of the puzzle grid as the canonical non-renewable resource."
            },
            {
                "id": "B",
                "text": "SOLAR",
                "is_correct": False,
                "rationale": "Solar energy is an inexhaustible, continuous renewable flow resource."
            },
            {
                "id": "C",
                "text": "TIMBER",
                "is_correct": False,
                "rationale": "Timber is a biological renewable resource."
            },
            {
                "id": "D",
                "text": "WIND",
                "is_correct": False,
                "rationale": "Wind is a flow renewable resource."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) MINERALS\n\nCrossword Solution:\nRow 6 spells MINERALS.",
        "step_by_step_solution": "Correct Answer: (A) MINERALS\n\nCrossword Solution:\nRow 6 spells MINERALS.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex4_iii_puzzle",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Pages 11-12)",
        "question_number": "4(iii)",
        "exercise": "Exercises (Pages 11-12)",
        "questionNumber": "4(iii)",
        "text": "[NCERT Puzzle Clue (iii)] Which type of soil described in the puzzle is renowned for its 'high water-retaining capacity' and self-ploughing property when drying?",
        "options": [
            {
                "id": "A",
                "text": "BLACK",
                "is_correct": True,
                "rationale": "BLACK appears vertically in Column 1 of the puzzle grid. Black soils are composed of fine clayey particles with immense moisture-holding capability."
            },
            {
                "id": "B",
                "text": "ARID",
                "is_correct": False,
                "rationale": "Arid soils are sandy, highly porous, and have extremely poor moisture-holding capacity."
            },
            {
                "id": "C",
                "text": "LATERITE",
                "is_correct": False,
                "rationale": "Laterite soil is heavily leached with coarse structure and low water-retention."
            },
            {
                "id": "D",
                "text": "MOUNTAIN",
                "is_correct": False,
                "rationale": "Mountain soils on steep slopes are coarse-grained with rapid drainage."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) BLACK\n\nCrossword Solution:\nColumn 1 (downwards) spells B-L-A-C-K.",
        "step_by_step_solution": "Correct Answer: (A) BLACK\n\nCrossword Solution:\nColumn 1 (downwards) spells B-L-A-C-K.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex4_iv_puzzle",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Pages 11-12)",
        "question_number": "4(iv)",
        "exercise": "Exercises (Pages 11-12)",
        "questionNumber": "4(iv)",
        "text": "[NCERT Puzzle Clue (iv)] Which soil type fits the clue: 'Intensively leached soils of the tropical monsoon climate with alternate wet and dry seasons'?",
        "options": [
            {
                "id": "A",
                "text": "LATERITE",
                "is_correct": True,
                "rationale": "LATERITE appears horizontally across Row 8 of the puzzle grid. It is formed by heavy monsoon rains leaching out soluble minerals and silica."
            },
            {
                "id": "B",
                "text": "ALLUVIAL",
                "is_correct": False,
                "rationale": "Alluvial soil is formed by river sedimentation, not by intense in situ leaching."
            },
            {
                "id": "C",
                "text": "PEATY",
                "is_correct": False,
                "rationale": "Peaty soils form in heavy rainfall areas with high humidity and accumulation of organic matter."
            },
            {
                "id": "D",
                "text": "SALINE",
                "is_correct": False,
                "rationale": "Saline soils occur in dry arid climates or waterlogged canals with high capillary salt deposits."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) LATERITE\n\nCrossword Solution:\nRow 8 spells L-A-T-E-R-I-T-E.",
        "step_by_step_solution": "Correct Answer: (A) LATERITE\n\nCrossword Solution:\nRow 8 spells L-A-T-E-R-I-T-E.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex4_v_puzzle",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 12)",
        "question_number": "4(v)",
        "exercise": "Exercises (Page 12)",
        "questionNumber": "4(v)",
        "text": "[NCERT Puzzle Clue (v)] What key conservation term solves the clue: 'Plantation of trees on a large scale to check soil erosion and restore forest cover'?",
        "options": [
            {
                "id": "A",
                "text": "AFFORESTATION",
                "is_correct": True,
                "rationale": "AFFORESTATION appears horizontally across Row 2 of the puzzle grid."
            },
            {
                "id": "B",
                "text": "DEFORESTATION",
                "is_correct": False,
                "rationale": "Deforestation is the clearance of forests, which accelerates soil erosion."
            },
            {
                "id": "C",
                "text": "DESERTIFICATION",
                "is_correct": False,
                "rationale": "Desertification is the degradation of arid and semi-arid land into barren desert."
            },
            {
                "id": "D",
                "text": "STRIP CROPPING",
                "is_correct": False,
                "rationale": "Strip cropping involves alternating grass strips with crops, not large-scale tree planting."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) AFFORESTATION\n\nCrossword Solution:\nRow 2 spells A-F-F-O-R-E-S-T-A-T-I-O-N.",
        "step_by_step_solution": "Correct Answer: (A) AFFORESTATION\n\nCrossword Solution:\nRow 2 spells A-F-F-O-R-E-S-T-A-T-I-O-N.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_ex4_vi_puzzle",
        "chapter": "Resources and Development",
        "section": "EXERCISES (Page 12)",
        "question_number": "4(vi)",
        "exercise": "Exercises (Page 12)",
        "questionNumber": "4(vi)",
        "text": "[NCERT Puzzle Clue (vi)] Which soil answers the puzzle clue: 'The vast Great Northern Plains of India are made up of these fertile transported soils'?",
        "options": [
            {
                "id": "A",
                "text": "ALLUVIAL",
                "is_correct": True,
                "rationale": "ALLUVIAL appears vertically in Column 12 of the puzzle grid. The northern plains are formed by Indus, Ganga, and Brahmaputra alluvial deposits."
            },
            {
                "id": "B",
                "text": "RED AND YELLOW",
                "is_correct": False,
                "rationale": "Red and yellow soils dominate the southern and eastern Deccan plateau."
            },
            {
                "id": "C",
                "text": "ARID",
                "is_correct": False,
                "rationale": "Arid soils form the Thar desert in Rajasthan."
            },
            {
                "id": "D",
                "text": "LATERITE",
                "is_correct": False,
                "rationale": "Laterite soil occurs in Western Ghats and parts of Odisha/Assam."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) ALLUVIAL\n\nCrossword Solution:\nColumn 12 spells A-L-L-U-V-I-A-L.",
        "step_by_step_solution": "Correct Answer: (A) ALLUVIAL\n\nCrossword Solution:\nColumn 12 spells A-L-L-U-V-I-A-L.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },

    # =========================================================================
    # IN-TEXT QUESTIONS & ACTIVITY PROMPTS (Pages 1-10)
    # =========================================================================
    {
        "id": "sst_geo_ch1_p01_def_resource",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 1)",
        "question_number": "Page 1 - Concept",
        "exercise": "In-Text (Page 1)",
        "questionNumber": "1",
        "text": "According to the formal definition of a 'Resource' on Page 1, which three essential criteria must an environmental object satisfy to be termed a resource?",
        "options": [
            {
                "id": "A",
                "text": "Technologically accessible, economically feasible, and culturally acceptable",
                "is_correct": True,
                "rationale": "NCERT Page 1 defines a resource as: 'Everything available in our environment which can be used to satisfy our needs, provided, it is technologically accessible, economically feasible and culturally acceptable'."
            },
            {
                "id": "B",
                "text": "Naturally abundant, commercially exportable, and non-taxable",
                "is_correct": False,
                "rationale": "Abundance and exportability are not part of the standard three criteria."
            },
            {
                "id": "C",
                "text": "Infinitely replenishable, completely cost-free, and legally deregulated",
                "is_correct": False,
                "rationale": "Resources are not free gifts of nature and many are non-renewable."
            },
            {
                "id": "D",
                "text": "Exclusively owned by private corporations, easily transported, and combustible",
                "is_correct": False,
                "rationale": "Ownership can be individual, community, national, or international."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Technologically accessible, economically feasible, and culturally acceptable\n\nKey Concept:\nAn environmental object is only a resource if technology exists to extract it, economic value exceeds extraction cost, and society accepts its usage.",
        "step_by_step_solution": "Correct Answer: (A) Technologically accessible, economically feasible, and culturally acceptable\n\nKey Concept:\nAn environmental object is only a resource if technology exists to extract it, economic value exceeds extraction cost, and society accepts its usage.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p01_classification",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 1)",
        "question_number": "Page 1 - Classification",
        "exercise": "In-Text (Page 1)",
        "questionNumber": "2",
        "text": "On the basis of 'Exhaustibility', how are environmental resources classified?",
        "options": [
            {
                "id": "A",
                "text": "Renewable and Non-renewable resources",
                "is_correct": True,
                "rationale": "Resources are categorized by exhaustibility into renewable (replenishable by physical/chemical/mechanical processes) and non-renewable (take millions of years to form)."
            },
            {
                "id": "B",
                "text": "Biotic and Abiotic resources",
                "is_correct": False,
                "rationale": "Biotic and abiotic is the classification based on origin."
            },
            {
                "id": "C",
                "text": "Individual, Community, National, and International resources",
                "is_correct": False,
                "rationale": "This is the classification based on ownership."
            },
            {
                "id": "D",
                "text": "Potential, Developed, Stock, and Reserves",
                "is_correct": False,
                "rationale": "This is the classification based on status of development."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Renewable and Non-renewable resources\n\nKey Concept:\nExhaustibility divides resources into Renewable (solar, wind, water, forests) and Non-Renewable (minerals, fossil fuels).",
        "step_by_step_solution": "Correct Answer: (A) Renewable and Non-renewable resources\n\nKey Concept:\nExhaustibility divides resources into Renewable (solar, wind, water, forests) and Non-Renewable (minerals, fossil fuels).",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p02_sustainable_dev",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 2)",
        "question_number": "Page 2 - In-Text",
        "exercise": "In-Text (Page 2)",
        "questionNumber": "1",
        "text": "What is the core principle of 'Sustainable Development' as formulated on Page 2 of the textbook?",
        "options": [
            {
                "id": "A",
                "text": "Development should take place without damaging the environment, and present development should not compromise the needs of future generations",
                "is_correct": True,
                "rationale": "NCERT defines: 'Sustainable economic development means development should take place without damaging the environment, and development in the present should not compromise with the needs of the future generations'."
            },
            {
                "id": "B",
                "text": "Complete cessation of all industrial mining and fossil fuel consumption immediately",
                "is_correct": False,
                "rationale": "Sustainable development seeks balanced, judicious growth, not complete economic halt."
            },
            {
                "id": "C",
                "text": "Maximising resource extraction today to generate financial wealth for future investments",
                "is_correct": False,
                "rationale": "This leads to immediate environmental degradation and resource depletion."
            },
            {
                "id": "D",
                "text": "Restricting resource usage strictly to developed nations with advanced green technology",
                "is_correct": False,
                "rationale": "Agenda 21 and sustainable development emphasize global cooperation and equity."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Development should take place without damaging the environment, and present development should not compromise the needs of future generations\n\nKey Concept:\nSustainable development balances present socio-economic progress with intergenerational environmental preservation.",
        "step_by_step_solution": "Correct Answer: (A) Development should take place without damaging the environment, and present development should not compromise the needs of future generations\n\nKey Concept:\nSustainable development balances present socio-economic progress with intergenerational environmental preservation.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p02_agenda21",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 2)",
        "question_number": "Page 2 - Agenda 21",
        "exercise": "In-Text (Page 2)",
        "questionNumber": "2",
        "text": "Where and when was 'Agenda 21' endorsed by world leaders, and what is its prime objective?",
        "options": [
            {
                "id": "A",
                "text": "Rio de Janeiro (Brazil) in 1992 at UNCED; to achieve global sustainable development and encourage every local government to draw its own Agenda 21",
                "is_correct": True,
                "rationale": "In June 1992, over 100 heads of states met at Rio de Janeiro for the first International Earth Summit (UNCED) and adopted Agenda 21."
            },
            {
                "id": "B",
                "text": "Kyoto (Japan) in 1997; to eliminate all nuclear weapons worldwide",
                "is_correct": False,
                "rationale": "The Kyoto Protocol dealt with greenhouse gas emission caps, not Agenda 21."
            },
            {
                "id": "C",
                "text": "Paris (France) in 2015; to privatize municipal water reservoirs globally",
                "is_correct": False,
                "rationale": "The 2015 Paris Agreement dealt with global warming limits (1.5°C/2°C)."
            },
            {
                "id": "D",
                "text": "Geneva (Switzerland) in 1948; to regulate international currency exchange rates",
                "is_correct": False,
                "rationale": "Geneva conventions deal with humanitarian treatment in warfare, not Agenda 21."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Rio de Janeiro (Brazil) in 1992 at UNCED; to achieve global sustainable development and encourage every local government to draw its own Agenda 21\n\nKey Concept:\nAgenda 21 is a comprehensive blueprint for sustainable development combating environmental damage, poverty, and disease through shared responsibilities.",
        "step_by_step_solution": "Correct Answer: (A) Rio de Janeiro (Brazil) in 1992 at UNCED; to achieve global sustainable development and encourage every local government to draw its own Agenda 21\n\nKey Concept:\nAgenda 21 is a comprehensive blueprint for sustainable development combating environmental damage, poverty, and disease through shared responsibilities.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p03_resource_planning",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 3)",
        "question_number": "Page 3 - Planning",
        "exercise": "In-Text (Page 3)",
        "questionNumber": "1",
        "text": "Which of the following outlines the correct sequence of the three complex stages involved in 'Resource Planning in India'?",
        "options": [
            {
                "id": "A",
                "text": "(i) Identification and inventory through surveying and mapping; (ii) Evolving a planning structure with appropriate technology; (iii) Matching resource plans with national development goals",
                "is_correct": True,
                "rationale": "NCERT Page 3 outlines these exact three stages: surveying/mapping inventory, building tech/institutional capacity, and aligning with five-year national plans."
            },
            {
                "id": "B",
                "text": "(i) Privatisation of all public lands; (ii) Immediate excavation; (iii) Exporting all reserves to foreign markets",
                "is_correct": False,
                "rationale": "Resource planning focuses on sustainable, balanced domestic development, not unchecked export or indiscriminate privatization."
            },
            {
                "id": "C",
                "text": "(i) Banning all technology; (ii) Manual digging; (iii) Equal distribution per household without survey",
                "is_correct": False,
                "rationale": "Technology and institutions are essential pillars of systematic planning."
            },
            {
                "id": "D",
                "text": "(i) Converting forests into housing colonies; (ii) Subsidizing chemical fertilizers; (iii) Draining wetlands",
                "is_correct": False,
                "rationale": "These lead to land degradation rather than sustainable planning."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) (i) Identification and inventory through surveying and mapping; (ii) Evolving a planning structure with appropriate technology; (iii) Matching resource plans with national development goals\n\nKey Concept:\nResource planning is an integrated 3-stage process starting from surveying to institutional implementation and national alignment.",
        "step_by_step_solution": "Correct Answer: (A) (i) Identification and inventory through surveying and mapping; (ii) Evolving a planning structure with appropriate technology; (iii) Matching resource plans with national development goals\n\nKey Concept:\nResource planning is an integrated 3-stage process starting from surveying to institutional implementation and national alignment.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p03_paradox",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 3)",
        "question_number": "Page 3 - Find Out",
        "exercise": "In-Text (Page 3)",
        "questionNumber": "2",
        "text": "[Page 3 Find Out] Which group of Indian states illustrates the phenomenon of being 'rich in mineral and coal deposits, yet included among economically backward regions' due to lack of corresponding technological and institutional development?",
        "options": [
            {
                "id": "A",
                "text": "Jharkhand, Chhattisgarh, and Madhya Pradesh",
                "is_correct": True,
                "rationale": "NCERT specifically highlights Jharkhand, Chhattisgarh, and Madhya Pradesh as richly endowed with minerals and coal, but facing economic backwardness due to historical underdevelopment of processing industries and infrastructure."
            },
            {
                "id": "B",
                "text": "Punjab, Haryana, and Delhi",
                "is_correct": False,
                "rationale": "These regions have poor mineral deposits but are economically very prosperous."
            },
            {
                "id": "C",
                "text": "Kerala and Goa",
                "is_correct": False,
                "rationale": "These states have high Human Development Index (HDI) and are economically advanced."
            },
            {
                "id": "D",
                "text": "Arunachal Pradesh, Sikkim, and Ladakh",
                "is_correct": False,
                "rationale": "These are mountainous regions with rich water or solar resources, but not the primary coal/mineral belt."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Jharkhand, Chhattisgarh, and Madhya Pradesh\n\nKey Concept:\nMere availability of resources does not guarantee development unless accompanied by appropriate technology, skilled human resources, and institutional changes.",
        "step_by_step_solution": "Correct Answer: (A) Jharkhand, Chhattisgarh, and Madhya Pradesh\n\nKey Concept:\nMere availability of resources does not guarantee development unless accompanied by appropriate technology, skilled human resources, and institutional changes.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p04_gandhi",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 4)",
        "question_number": "Page 4 - Philosophy",
        "exercise": "In-Text (Page 4)",
        "questionNumber": "1",
        "text": "Mahatma Gandhi voiced his concern against modern technological exploitation in which famous words quoted on Page 4?",
        "options": [
            {
                "id": "A",
                "text": "\"There is enough for everybody's need and not for any body's greed.\"",
                "is_correct": True,
                "rationale": "Gandhiji held greedy individuals and the exploitative nature of modern technology as the root cause of global resource depletion, advocating 'production by the masses' rather than 'mass production'."
            },
            {
                "id": "B",
                "text": "\"Industrialisation is the sole yardstick of a nation's true greatness.\"",
                "is_correct": False,
                "rationale": "Gandhiji was critical of aggressive, unbridled industrialism."
            },
            {
                "id": "C",
                "text": "\"Nature exists only to be subjugated by technological machines.\"",
                "is_correct": False,
                "rationale": "Opposite of Gandhian conservationist philosophy."
            },
            {
                "id": "D",
                "text": "\"Fossil fuels should be exploited at maximum speed before they deplete.\"",
                "is_correct": False,
                "rationale": "Directly contradicts sustainable conservation."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) \"There is enough for everybody's need and not for any body's greed.\"\n\nKey Concept:\nGandhian resource philosophy prioritizes ethical stewardship, self-reliance, and conservation over predatory greed.",
        "step_by_step_solution": "Correct Answer: (A) \"There is enough for everybody's need and not for any body's greed.\"\n\nKey Concept:\nGandhian resource philosophy prioritizes ethical stewardship, self-reliance, and conservation over predatory greed.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p04_relief_features",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 4)",
        "question_number": "Page 4 - Relief Features",
        "exercise": "In-Text (Page 4)",
        "questionNumber": "2",
        "text": "What is the proportion of Plains, Mountains, and Plateaus respectively in the total land surface area of India?",
        "options": [
            {
                "id": "A",
                "text": "Plains: 43%, Mountains: 30%, Plateaus: 27%",
                "is_correct": True,
                "rationale": "NCERT Page 4 (Fig 1.3) clearly breaks down India's relief into 43% Plains (agriculture/industry), 30% Mountains (perennial rivers/tourism), and 27% Plateaus (minerals/fuels/forests)."
            },
            {
                "id": "B",
                "text": "Plains: 50%, Mountains: 25%, Plateaus: 25%",
                "is_correct": False,
                "rationale": "Incorrect proportions."
            },
            {
                "id": "C",
                "text": "Plains: 33%, Mountains: 33%, Plateaus: 34%",
                "is_correct": False,
                "rationale": "Incorrect equal distribution."
            },
            {
                "id": "D",
                "text": "Plains: 27%, Mountains: 43%, Plateaus: 30%",
                "is_correct": False,
                "rationale": "Inverted figures."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Plains: 43%, Mountains: 30%, Plateaus: 27%\n\nKey Concept:\nIndia's diverse relief provides facilities for agriculture (Plains), ecological/perennial river balance (Mountains), and mineral wealth (Plateaus).",
        "step_by_step_solution": "Correct Answer: (A) Plains: 43%, Mountains: 30%, Plateaus: 27%\n\nKey Concept:\nIndia's diverse relief provides facilities for agriculture (Plains), ecological/perennial river balance (Mountains), and mineral wealth (Plateaus).",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p05_nsa_variation",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 5)",
        "question_number": "Page 5 - In-Text",
        "exercise": "In-Text (Page 5)",
        "questionNumber": "1",
        "text": "[Page 5 In-Text] How does the proportion of Net Sown Area (NSA) vary across Indian states according to official land-use data?",
        "options": [
            {
                "id": "A",
                "text": "Over 80% in Punjab and Haryana, but less than 10% in Arunachal Pradesh, Mizoram, Manipur, and Andaman & Nicobar Islands",
                "is_correct": True,
                "rationale": "NCERT Page 5 highlights this dramatic regional disparity due to flat fertile alluvial soils and canal networks in Punjab/Haryana versus rugged mountains, dense forests, and rocky terrain in the northeast."
            },
            {
                "id": "B",
                "text": "Over 90% in Rajasthan desert, but less than 5% in Punjab plains",
                "is_correct": False,
                "rationale": "Completely reversed; Rajasthan has arid soil and low net sown area."
            },
            {
                "id": "C",
                "text": "Exactly 50% uniformly across all 28 states of India",
                "is_correct": False,
                "rationale": "Land use varies widely based on relief, soil, and climate."
            },
            {
                "id": "D",
                "text": "Highest in the cold desert of Ladakh (>95%) and lowest in Uttar Pradesh (<2%)",
                "is_correct": False,
                "rationale": "Ladakh has negligible cropped area, while UP has vast agricultural land."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Over 80% in Punjab and Haryana, but less than 10% in Arunachal Pradesh, Mizoram, Manipur, and Andaman & Nicobar Islands\n\nKey Concept:\nTopography, soil fertility, rainfall, and irrigation infrastructure create large variations in cultivated Net Sown Area.",
        "step_by_step_solution": "Correct Answer: (A) Over 80% in Punjab and Haryana, but less than 10% in Arunachal Pradesh, Mizoram, Manipur, and Andaman & Nicobar Islands\n\nKey Concept:\nTopography, soil fertility, rainfall, and irrigation infrastructure create large variations in cultivated Net Sown Area.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p06_land_degradation_mining",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 6)",
        "question_number": "Page 6 - Degradation",
        "exercise": "In-Text (Page 6)",
        "questionNumber": "1",
        "text": "In which states has severe land degradation been caused primarily by deforestation resulting from open-cast mining and excavation sites?",
        "options": [
            {
                "id": "A",
                "text": "Jharkhand, Chhattisgarh, Madhya Pradesh, and Odisha",
                "is_correct": True,
                "rationale": "In these mineral-rich states, large-scale mining leads to forest clearing, deep excavation scars, and over-burdening of abandoned pits, causing acute land degradation."
            },
            {
                "id": "B",
                "text": "Punjab, Haryana, and western Uttar Pradesh",
                "is_correct": False,
                "rationale": "In these agrarian states, land degradation is caused by over-irrigation and waterlogging, not mining."
            },
            {
                "id": "C",
                "text": "Gujarat and Rajasthan",
                "is_correct": False,
                "rationale": "In Gujarat and Rajasthan, the primary cause of land degradation is overgrazing."
            },
            {
                "id": "D",
                "text": "Kerala and Tamil Nadu",
                "is_correct": False,
                "rationale": "These states are known for plantation agriculture and coastal soils."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Jharkhand, Chhattisgarh, Madhya Pradesh, and Odisha\n\nKey Concept:\nDifferent human activities drive degradation in different regions: Mining in central-eastern states, overgrazing in western states, and over-irrigation in northern plains.",
        "step_by_step_solution": "Correct Answer: (A) Jharkhand, Chhattisgarh, Madhya Pradesh, and Odisha\n\nKey Concept:\nDifferent human activities drive degradation in different regions: Mining in central-eastern states, overgrazing in western states, and over-irrigation in northern plains.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p06_soil_profile",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 6)",
        "question_number": "Page 6 - Soil Profile",
        "exercise": "In-Text (Page 6)",
        "questionNumber": "2",
        "text": "According to the Soil Profile diagram (Fig. 1.5, Page 6), which layer directly underlies the fertile 'Top soil' (upper soil layer)?",
        "options": [
            {
                "id": "A",
                "text": "Subsoil weathered rocks, sand, and silt clay",
                "is_correct": True,
                "rationale": "The second horizon directly below the topsoil is the subsoil, consisting of weathered rock fragments, sand, silt, and clay."
            },
            {
                "id": "B",
                "text": "Unweathered parent bed rock",
                "is_correct": False,
                "rationale": "Unweathered parent bed rock forms the lowest foundation layer of the soil profile."
            },
            {
                "id": "C",
                "text": "Substratum weathered parent rock material",
                "is_correct": False,
                "rationale": "The substratum lies between the subsoil and the unweathered bed rock."
            },
            {
                "id": "D",
                "text": "Pure molten volcanic basalt lava",
                "is_correct": False,
                "rationale": "Molten magma/lava is deep within the Earth's mantle/crust, not part of the soil profile."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Subsoil weathered rocks, sand, and silt clay\n\nKey Concept:\nSoil Profile sequence from top to bottom:\n1. Top soil (organic humus layer)\n2. Subsoil (weathered sand, silt, clay)\n3. Substratum (weathered parent rock)\n4. Unweathered parent bed rock.",
        "step_by_step_solution": "Correct Answer: (A) Subsoil weathered rocks, sand, and silt clay\n\nKey Concept:\nSoil Profile sequence from top to bottom:\n1. Top soil (organic humus layer)\n2. Subsoil (weathered sand, silt, clay)\n3. Substratum (weathered parent rock)\n4. Unweathered parent bed rock.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p07_alluvial_classification",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 7)",
        "question_number": "Page 7 - Alluvial Soils",
        "exercise": "In-Text (Page 7)",
        "questionNumber": "1",
        "text": "How are Alluvial soils classified on the basis of geological age, and how do they differ in fertility?",
        "options": [
            {
                "id": "A",
                "text": "Old alluvial (Bangar) with higher calcareous Kankar nodules; New alluvial (Khadar) with finer particles and higher fertility",
                "is_correct": True,
                "rationale": "NCERT Page 7 distinguishes Bangar (older floodplain terrace with kankar nodules) from Khadar (new flood plain silt renewed annually, very fertile)."
            },
            {
                "id": "B",
                "text": "Bangar is new volcanic ash, while Khadar is ancient marine limestone",
                "is_correct": False,
                "rationale": "Alluvial soils are river deposits, not volcanic or marine limestone."
            },
            {
                "id": "C",
                "text": "Khadar is found only in deserts, while Bangar is found only in the Himalayas",
                "is_correct": False,
                "rationale": "Both are river valley floodplain soils across the northern plains."
            },
            {
                "id": "D",
                "text": "Bangar is completely sterile, while Khadar consists only of coarse gravel",
                "is_correct": False,
                "rationale": "Both are fertile, but Khadar has finer silt and higher fertility."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Old alluvial (Bangar) with higher calcareous Kankar nodules; New alluvial (Khadar) with finer particles and higher fertility\n\nKey Concept:\nBangar = Old alluvium (coarser, kankar nodules).\nKhadar = New alluvium (finer, renewed by annual floods, more fertile).",
        "step_by_step_solution": "Correct Answer: (A) Old alluvial (Bangar) with higher calcareous Kankar nodules; New alluvial (Khadar) with finer particles and higher fertility\n\nKey Concept:\nBangar = Old alluvium (coarser, kankar nodules).\nKhadar = New alluvium (finer, renewed by annual floods, more fertile).",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p09_red_yellow_soils",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 9)",
        "question_number": "Page 9 - Red Soils",
        "exercise": "In-Text (Page 9)",
        "questionNumber": "1",
        "text": "Why do 'Red and Yellow soils' develop a reddish colour, and under what condition do they appear yellow?",
        "options": [
            {
                "id": "A",
                "text": "They develop a reddish colour due to the diffusion of iron in crystalline and metamorphic rocks, and look yellow when hydrated",
                "is_correct": True,
                "rationale": "NCERT Page 9 explains: 'These soils develop a reddish colour due to diffusion of iron in crystalline and metamorphic rocks. It looks yellow when it occurs in a hydrated form'."
            },
            {
                "id": "B",
                "text": "They turn red due to high nitrogen fertilizer runoff, and turn yellow when polluted by sulfur dioxide",
                "is_correct": False,
                "rationale": "Colour is due to natural geochemical iron oxide diffusion and hydration."
            },
            {
                "id": "C",
                "text": "They are red due to volcanic lava basalt, and yellow due to decomposing autumn tree leaves",
                "is_correct": False,
                "rationale": "Basalt lava forms black soil, not red soil."
            },
            {
                "id": "D",
                "text": "They turn red under freezing mountain snow, and yellow in extreme desert heat",
                "is_correct": False,
                "rationale": "Incorrect climatic explanation."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) They develop a reddish colour due to the diffusion of iron in crystalline and metamorphic rocks, and look yellow when hydrated\n\nKey Concept:\nFerric oxide ($Fe_2O_3$) gives red soil its reddish hue; upon chemical hydration ($Fe_2O_3 \\cdot nH_2O$), it appears yellow.",
        "step_by_step_solution": "Correct Answer: (A) They develop a reddish colour due to the diffusion of iron in crystalline and metamorphic rocks, and look yellow when hydrated\n\nKey Concept:\nFerric oxide ($Fe_2O_3$) gives red soil its reddish hue; upon chemical hydration ($Fe_2O_3 \\cdot nH_2O$), it appears yellow.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p10_gully_erosion",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 10)",
        "question_number": "Page 10 - Erosion",
        "exercise": "In-Text (Page 10)",
        "questionNumber": "1",
        "text": "When running rainwater cuts through clayey soils making deep channels, what is this erosion termed, and what are such badlands called in the Chambal basin?",
        "options": [
            {
                "id": "A",
                "text": "Gully erosion; ravines in the Chambal basin",
                "is_correct": True,
                "rationale": "NCERT Page 10 specifies: 'The running water cuts through the clayey soils and makes deep channels as gullies. The land becomes unfit for cultivation and is known as bad land. In the Chambal basin such lands are called ravines'."
            },
            {
                "id": "B",
                "text": "Sheet erosion; moraines in the Chambal basin",
                "is_correct": False,
                "rationale": "Sheet erosion washes away uniform topsoil sheets; moraines are glacial deposits."
            },
            {
                "id": "C",
                "text": "Wind deflation; sand dunes in the Chambal basin",
                "is_correct": False,
                "rationale": "Gully erosion is water-driven, not wind-driven."
            },
            {
                "id": "D",
                "text": "Glacial calving; fjords in the Chambal basin",
                "is_correct": False,
                "rationale": "Fjords are coastal glacial inlets, completely unrelated to Chambal badlands."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Gully erosion; ravines in the Chambal basin\n\nKey Concept:\nDeep channel incision by storm runoff = Gully erosion. Severely gullied uncultivable badland in Chambal = Ravines.",
        "step_by_step_solution": "Correct Answer: (A) Gully erosion; ravines in the Chambal basin\n\nKey Concept:\nDeep channel incision by storm runoff = Gully erosion. Severely gullied uncultivable badland in Chambal = Ravines.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    }
]

def main():
    out_dir = os.path.join('assets', 'data')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'ncert_sst_geo_ch1.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully generated {len(questions)} authentic NCERT questions in {out_file}!")

if __name__ == '__main__':
    main()
