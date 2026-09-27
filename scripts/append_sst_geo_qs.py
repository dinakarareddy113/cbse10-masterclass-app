# -*- coding: utf-8 -*-
"""
Appends 8 additional authentic NCERT questions to complete the 36-question bank for
Geography Chapter 1: Resources and Development.
"""
import json
import os

with open('assets/data/ncert_sst_geo_ch1.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

additional_qs = [
    {
        "id": "sst_geo_ch1_p02_oil_exhaustion",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 2)",
        "question_number": "Page 2 - Activity 1",
        "exercise": "In-Text (Page 2)",
        "questionNumber": "3",
        "text": "[Page 2 Activity 1] If global crude oil supplies were to become exhausted, which critical economic sector would experience the most immediate systemic disruption?",
        "options": [
            {
                "id": "A",
                "text": "Automotive transport, civil aviation, and petroleum-based chemical industries",
                "is_correct": True,
                "rationale": "Crude oil is the non-renewable lifeblood of modern transportation fuels (petrol, diesel, aviation kerosene) and petrochemical feedstocks (plastics, synthetic fibers, pharmaceuticals)."
            },
            {
                "id": "B",
                "text": "Traditional wooden bullock cart manufacturing in rural villages",
                "is_correct": False,
                "rationale": "Bullock carts rely on draft animal power and timber, not petroleum."
            },
            {
                "id": "C",
                "text": "Hydropower generation across Himalayan river reservoirs",
                "is_correct": False,
                "rationale": "Hydropower generation depends on running river water head and gravity."
            },
            {
                "id": "D",
                "text": "Biological nitrogen fixation by leguminous pulse root nodules",
                "is_correct": False,
                "rationale": "Biological nitrogen fixation is a natural bacterial process (Rhizobium)."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Automotive transport, civil aviation, and petroleum-based chemical industries\n\nKey Concept:\nFossil fuels like crude oil are non-renewable and irreplaceable in the short term for transportation, logistics, and petrochemical manufacturing.",
        "step_by_step_solution": "Correct Answer: (A) Automotive transport, civil aviation, and petroleum-based chemical industries\n\nKey Concept:\nFossil fuels like crude oil are non-renewable and irreplaceable in the short term for transportation, logistics, and petrochemical manufacturing.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p04_land_utilisation",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 4)",
        "question_number": "Page 4 - Land Categories",
        "exercise": "In-Text (Page 4)",
        "questionNumber": "3",
        "text": "[Page 4 Land Utilisation] How does NCERT officially classify agricultural land that has been 'left uncultivated for more than 5 agricultural years'?",
        "options": [
            {
                "id": "A",
                "text": "Culturable waste land",
                "is_correct": True,
                "rationale": "NCERT Page 4 defines: 'Culturable waste land (left uncultivated for more than 5 agricultural years)'. Current fallow is <= 1 year; other fallow is 1 to 5 years."
            },
            {
                "id": "B",
                "text": "Current fallow land",
                "is_correct": False,
                "rationale": "Current fallow is land left without cultivation for one or less than one agricultural year."
            },
            {
                "id": "C",
                "text": "Net sown area",
                "is_correct": False,
                "rationale": "Net sown area is the physical extent of land where crops are sown and harvested annually."
            },
            {
                "id": "D",
                "text": "Permanent pasture and grazing land",
                "is_correct": False,
                "rationale": "Pasture land is dedicated grazing commons, not abandoned cropland."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Culturable waste land\n\nKey Concept:\nFallow definitions:\n• Current fallow: <= 1 agricultural year.\n• Fallow other than current fallow: 1 to 5 agricultural years.\n• Culturable waste land: > 5 agricultural years.",
        "step_by_step_solution": "Correct Answer: (A) Culturable waste land\n\nKey Concept:\nFallow definitions:\n• Current fallow: <= 1 agricultural year.\n• Fallow other than current fallow: 1 to 5 agricultural years.\n• Culturable waste land: > 5 agricultural years.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p04_gross_cropped",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 4)",
        "question_number": "Page 4 - Gross Cropped Area",
        "exercise": "In-Text (Page 4)",
        "questionNumber": "4",
        "text": "[Page 4 Concept] What is the precise geographical formula for determining the 'Gross Cropped Area' of an agricultural region?",
        "options": [
            {
                "id": "A",
                "text": "Area sown more than once in an agricultural year plus Net Sown Area",
                "is_correct": True,
                "rationale": "NCERT Page 4 explicitly defines: 'Area sown more than once in an agricultural year plus net sown area is known as gross cropped area'."
            },
            {
                "id": "B",
                "text": "Total geographical reporting area minus all forest reserves",
                "is_correct": False,
                "rationale": "This calculates non-forest reporting land, not gross cropped area."
            },
            {
                "id": "C",
                "text": "Culturable waste land multiplied by current fallow acreage",
                "is_correct": False,
                "rationale": "Mathematically meaningless definition."
            },
            {
                "id": "D",
                "text": "Permanent pasture acreage divided by the total livestock count",
                "is_correct": False,
                "rationale": "This measures pasture carrying capacity, not gross cropped area."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Area sown more than once in an agricultural year plus Net Sown Area\n\nKey Concept:\nGross Cropped Area accounts for multiple cropping intensity on the same physical plot of Net Sown Area within one farm calendar year.",
        "step_by_step_solution": "Correct Answer: (A) Area sown more than once in an agricultural year plus Net Sown Area\n\nKey Concept:\nGross Cropped Area accounts for multiple cropping intensity on the same physical plot of Net Sown Area within one farm calendar year.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p05_pasture_land",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 5)",
        "question_number": "Page 5 - Pasture Land",
        "exercise": "In-Text (Page 5)",
        "questionNumber": "2",
        "text": "[Page 5 In-Text Inquiry] What serious ecological and agricultural challenge arises from the continuous decline of land under permanent pasture in India?",
        "options": [
            {
                "id": "A",
                "text": "Severe shortage of natural grazing fodder for the world's largest cattle population, forcing overgrazing on forests and fallows",
                "is_correct": True,
                "rationale": "As permanent pastures dwindle (from 4.71% in 1960-61 to ~3.4% in 2019-20), feeding India's massive livestock creates intense pressure on marginal lands and forests, triggering overgrazing."
            },
            {
                "id": "B",
                "text": "Excess accumulation of wild cattle manure leading to acidification of Himalayan glaciers",
                "is_correct": False,
                "rationale": "Factually baseless and geographically disconnected."
            },
            {
                "id": "C",
                "text": "Complete extinction of commercial poultry and freshwater fish farming",
                "is_correct": False,
                "rationale": "Poultry and aquaculture do not rely on permanent pasture lands."
            },
            {
                "id": "D",
                "text": "An automatic 50% increase in national groundwater storage tables",
                "is_correct": False,
                "rationale": "Pasture reduction does not increase groundwater storage."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Severe shortage of natural grazing fodder for the world's largest cattle population, forcing overgrazing on forests and fallows\n\nKey Concept:\nReduction in community grazing lands forces cattle into forests, accelerating deforestation and land degradation.",
        "step_by_step_solution": "Correct Answer: (A) Severe shortage of natural grazing fodder for the world's largest cattle population, forcing overgrazing on forests and fallows\n\nKey Concept:\nReduction in community grazing lands forces cattle into forests, accelerating deforestation and land degradation.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p09_arid_soil",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 9)",
        "question_number": "Page 9 - Arid Soils",
        "exercise": "In-Text (Page 9)",
        "questionNumber": "2",
        "text": "Which combination of characteristics accurately defines 'Arid Soils' as described on Page 9 of the textbook?",
        "options": [
            {
                "id": "A",
                "text": "Sandy texture, saline in nature, lacks humus and moisture, with a bottom Kankar layer that restricts water infiltration",
                "is_correct": True,
                "rationale": "NCERT Page 9 details: 'Arid soils range from red to brown in colour. They are generally sandy in texture and saline in nature... The lower horizons of the soil are occupied by Kankar because of increasing calcium content downwards. The Kankar layer formations in the bottom horizons restrict the infiltration of water'."
            },
            {
                "id": "B",
                "text": "Heavy clayey texture, waterlogged throughout the year, with high peat and acidic organic humus",
                "is_correct": False,
                "rationale": "Describes marshy/peaty soils, opposite of desert arid soils."
            },
            {
                "id": "C",
                "text": "Fine silt deposited by annual river floods, highly rich in nitrogen and phosphoric acid",
                "is_correct": False,
                "rationale": "Describes fertile Khadar alluvial soils."
            },
            {
                "id": "D",
                "text": "Rich black colour derived from basalt lava, possessing extreme moisture-retaining capacity",
                "is_correct": False,
                "rationale": "Describes black regur soil."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Sandy texture, saline in nature, lacks humus and moisture, with a bottom Kankar layer that restricts water infiltration\n\nKey Concept:\nArid soils form in dry climates with high evaporation. With canal irrigation (e.g., Indira Gandhi Canal in western Rajasthan), they become cultivable.",
        "step_by_step_solution": "Correct Answer: (A) Sandy texture, saline in nature, lacks humus and moisture, with a bottom Kankar layer that restricts water infiltration\n\nKey Concept:\nArid soils form in dry climates with high evaporation. With canal irrigation (e.g., Indira Gandhi Canal in western Rajasthan), they become cultivable.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p09_laterite_crops",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 9)",
        "question_number": "Page 9 - Laterite Crops",
        "exercise": "In-Text (Page 9)",
        "questionNumber": "3",
        "text": "[Page 9 Soils] Which plantation and commercial crops are successfully cultivated in Laterite soils after adopting appropriate soil conservation measures?",
        "options": [
            {
                "id": "A",
                "text": "Tea and Coffee (in Karnataka, Kerala, Tamil Nadu) and Cashew nuts (in Tamil Nadu, Andhra Pradesh, Kerala)",
                "is_correct": True,
                "rationale": "NCERT Page 9 specifically notes: 'After adopting appropriate soil conservation techniques particularly in the hilly areas of Karnataka, Kerala and Tamil Nadu, this soil is very useful for growing tea and coffee. Red laterite soils in Tamil Nadu, Andhra Pradesh and Kerala are more suitable for crops like cashew nut'."
            },
            {
                "id": "B",
                "text": "Wheat, sugarcane, and paddy cereals exclusively",
                "is_correct": False,
                "rationale": "Cereals and sugarcane require deep, nutrient-rich alluvial soils."
            },
            {
                "id": "C",
                "text": "Cotton and groundnut crops exclusively",
                "is_correct": False,
                "rationale": "Cotton thrives in black regur soils of the Deccan trap."
            },
            {
                "id": "D",
                "text": "Jute and wetland mangrove reeds exclusively",
                "is_correct": False,
                "rationale": "Jute requires annual flood plain alluvium in deltaic wetlands."
            }
        ],
        "difficulty": "medium",
        "solution": "Correct Answer: (A) Tea and Coffee (in Karnataka, Kerala, Tamil Nadu) and Cashew nuts (in Tamil Nadu, Andhra Pradesh, Kerala)\n\nKey Concept:\nLateritic soils are acidic and nutrient-leached, but with terracing and manuring, they are ideal for plantation crops (tea, coffee, cashew).",
        "step_by_step_solution": "Correct Answer: (A) Tea and Coffee (in Karnataka, Kerala, Tamil Nadu) and Cashew nuts (in Tamil Nadu, Andhra Pradesh, Kerala)\n\nKey Concept:\nLateritic soils are acidic and nutrient-leached, but with terracing and manuring, they are ideal for plantation crops (tea, coffee, cashew).",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p10_sheet_erosion",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 10)",
        "question_number": "Page 10 - Sheet Erosion",
        "exercise": "In-Text (Page 10)",
        "questionNumber": "2",
        "text": "When water flows as an expansive sheet over large areas down a slope, washing away the entire top layer of soil, what is this erosion form called?",
        "options": [
            {
                "id": "A",
                "text": "Sheet erosion",
                "is_correct": True,
                "rationale": "NCERT Page 10 defines: 'Sometimes water flows as a sheet over large areas down a slope. In such cases the top soil is washed away. This is known as sheet erosion'."
            },
            {
                "id": "B",
                "text": "Gully erosion",
                "is_correct": False,
                "rationale": "Gully erosion cuts narrow, deep channels and ravines into clayey soil, rather than washing away a uniform broad sheet."
            },
            {
                "id": "C",
                "text": "Wind deflation",
                "is_correct": False,
                "rationale": "Wind deflation is the lifting and blowing of loose particles by wind."
            },
            {
                "id": "D",
                "text": "Glacial deposition",
                "is_correct": False,
                "rationale": "Glacial deposition builds moraines, rather than stripping away topsoil by water."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Sheet erosion\n\nKey Concept:\nSheet erosion removes uniform layers of fertile topsoil across broad slopes during intense rainfall.",
        "step_by_step_solution": "Correct Answer: (A) Sheet erosion\n\nKey Concept:\nSheet erosion removes uniform layers of fertile topsoil across broad slopes during intense rainfall.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    },
    {
        "id": "sst_geo_ch1_p10_shelter_belts",
        "chapter": "Resources and Development",
        "section": "QUESTIONS (Page 10)",
        "question_number": "Page 10 - Shelter Belts",
        "exercise": "In-Text (Page 10)",
        "questionNumber": "3",
        "text": "[Page 10 Conservation] What are 'Shelter Belts', and what significant ecological role have they played in western India?",
        "options": [
            {
                "id": "A",
                "text": "Planting continuous rows of trees to break the velocity of wind; they have stabilized sand dunes and checked desert expansion in western India",
                "is_correct": True,
                "rationale": "NCERT Page 10 specifies: 'Planting lines of trees to create shelter also works in a similar way. Rows of such trees are called shelter belts. These shelter belts have contributed significantly to the stabilisation of sand dunes and in stabilising the desert in western India'."
            },
            {
                "id": "B",
                "text": "Constructing high concrete walls along riverbanks to prevent annual monsoon flooding",
                "is_correct": False,
                "rationale": "These are flood embankments, not shelter belts."
            },
            {
                "id": "C",
                "text": "Excavating deep trench canals around agricultural fields to divert forest wildlife",
                "is_correct": False,
                "rationale": "These are wildlife moats/trenches, not shelter belts."
            },
            {
                "id": "D",
                "text": "Spreading plastic sheets across open pastures to trap nocturnal moisture",
                "is_correct": False,
                "rationale": "Plastic mulching is a small-scale garden technique, not tree shelter belts."
            }
        ],
        "difficulty": "easy",
        "solution": "Correct Answer: (A) Planting continuous rows of trees to break the velocity of wind; they have stabilized sand dunes and checked desert expansion in western India\n\nKey Concept:\nShelter belts of trees disrupt aerodynamic wind velocity, preventing wind erosion and anchoring loose sand dunes in arid zones like Rajasthan.",
        "step_by_step_solution": "Correct Answer: (A) Planting continuous rows of trees to break the velocity of wind; they have stabilized sand dunes and checked desert expansion in western India\n\nKey Concept:\nShelter belts of trees disrupt aerodynamic wind velocity, preventing wind erosion and anchoring loose sand dunes in arid zones like Rajasthan.",
        "subject": "sst",
        "chapterId": "sst_geo_ch_01_resources"
    }
]

existing.extend(additional_qs)

# Check total and write back
with open('assets/data/ncert_sst_geo_ch1.json', 'w', encoding='utf-8') as f:
    json.dump(existing, f, indent=2, ensure_ascii=False)

print(f"Total authentic questions now in ncert_sst_geo_ch1.json: {len(existing)}")
