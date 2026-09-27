import json
import os

questions = [
    # -------------------------------------------------------------
    # SECTION 1: IN-TEXT "QUESTIONS" (Page 18)
    # -------------------------------------------------------------
    {
        "id": "sci_ch2_p18_q01",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 18)",
        "question_number": "1",
        "text": "You are given three test tubes containing distilled water, acidic solution, and basic solution respectively, and only red litmus paper. How can you identify the contents of each test tube?",
        "options": [
            {
                "id": "A",
                "text": "Dip red litmus into each; the one turning it blue is basic. Dip that blue litmus into the remaining two; the one turning it red is acidic, and the last is distilled water.",
                "is_correct": True,
                "rationale": "Red litmus turns blue strictly in basic medium. Once turned blue, it functions as blue litmus to identify the acid (which turns it back to red), leaving neutral distilled water unchanged."
            },
            {
                "id": "B",
                "text": "Dip red litmus into each; the one turning it colorless is acidic, the one turning it blue is distilled water, and the one turning it red is basic.",
                "is_correct": False,
                "rationale": "Litmus does not bleach to colorless in standard dilute acids, and neutral distilled water does not turn red litmus blue."
            },
            {
                "id": "C",
                "text": "Red litmus will turn blue in both distilled water and basic solution, but remain unchanged in acidic solution.",
                "is_correct": False,
                "rationale": "Distilled water is chemically neutral (pH ≈ 7) and does not turn red litmus blue."
            },
            {
                "id": "D",
                "text": "Dip red litmus into each; acidic solution turns it green, basic solution turns it red, and distilled water turns it yellow.",
                "is_correct": False,
                "rationale": "Litmus has only red and blue color states; green and yellow correspond to universal indicator, not litmus."
            }
        ],
        "difficulty": "medium"
    },

    # -------------------------------------------------------------
    # SECTION 2: IN-TEXT "QUESTIONS" (Page 22)
    # -------------------------------------------------------------
    {
        "id": "sci_ch2_p22_q01",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 22)",
        "question_number": "1",
        "text": "Why should curd and sour substances not be kept in brass and copper vessels?",
        "options": [
            {
                "id": "A",
                "text": "Curd contains lactic acid which reacts with brass and copper forming toxic, poisonous metal salts.",
                "is_correct": True,
                "rationale": "Sour food substances contain organic acids (like lactic acid) that corrode copper and zinc in brass, producing soluble toxic metallic salts that can cause severe food poisoning."
            },
            {
                "id": "B",
                "text": "Brass and copper metals absorb the natural fat and moisture from curd, causing the curd to dry out.",
                "is_correct": False,
                "rationale": "The hazard is a chemical reaction forming toxic salts, not physical fat absorption."
            },
            {
                "id": "C",
                "text": "Curd neutralizes copper to produce insoluble inert copper metal granules that solidify the food.",
                "is_correct": False,
                "rationale": "Acids do not reduce copper; they react with metallic oxides and copper to yield poisonous soluble copper compounds."
            },
            {
                "id": "D",
                "text": "Brass and copper act as refrigerants that lower the temperature of curd and freeze its microbial cultures.",
                "is_correct": False,
                "rationale": "Brass and copper are normal conductors of heat and do not have chemical refrigerating properties."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_p22_q02",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 22)",
        "question_number": "2",
        "text": "Which gas is usually liberated when an acid reacts with a metal, and how is its presence confirmed?",
        "options": [
            {
                "id": "A",
                "text": "Hydrogen gas ($\\text{H}_2$); confirmed because it burns with a characteristic 'pop' sound when a burning splinter is brought near.",
                "is_correct": True,
                "rationale": "Active metals displace hydrogen from dilute acids: $\\text{Zn} + \\text{H}_2\\text{SO}_4 \\rightarrow \\text{ZnSO}_4 + \\text{H}_2\\uparrow$. Hydrogen gas burns explosively in air with a distinctive 'pop' sound."
            },
            {
                "id": "B",
                "text": "Oxygen gas ($\\text{O}_2$); confirmed because it rekindles a glowing wooden splinter.",
                "is_correct": False,
                "rationale": "Acids reacting with metals yield hydrogen, not oxygen."
            },
            {
                "id": "C",
                "text": "Carbon dioxide ($\\text{CO}_2$); confirmed because it turns clear lime water milky.",
                "is_correct": False,
                "rationale": "$\\text{CO}_2$ is evolved when acids react with carbonates or hydrogencarbonates, not pure metals."
            },
            {
                "id": "D",
                "text": "Chlorine gas ($\\text{Cl}_2$); confirmed by its pungent choking odor and bleaching of moist litmus paper.",
                "is_correct": False,
                "rationale": "$\\text{Cl}_2$ is not the standard gas liberated in simple acid-metal displacement reactions."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_p22_q03",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 22)",
        "question_number": "3",
        "text": "Metal compound 'A' reacts with dilute $\\text{HCl}$ to produce effervescence. The gas evolved extinguishes a burning candle. Write the balanced equation if one product is $\\text{CaCl}_2$.",
        "options": [
            {
                "id": "A",
                "text": "$\\text{CaCO}_3(s) + 2\\text{HCl}(aq) \\rightarrow \\text{CaCl}_2(aq) + \\text{H}_2\\text{O}(l) + \\text{CO}_2(g)$",
                "is_correct": True,
                "rationale": "Compound A is calcium carbonate ($\\text{CaCO}_3$). Effervescence is caused by $\\text{CO}_2$ gas, which does not support combustion and extinguishes candles."
            },
            {
                "id": "B",
                "text": "$\\text{CaO}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{CaCl}_2(aq) + \\text{H}_2\\text{O}(l)$",
                "is_correct": False,
                "rationale": "Reaction with calcium oxide does not evolve gas effervescence."
            },
            {
                "id": "C",
                "text": "$\\text{Ca}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{CaCl}_2(aq) + \\text{H}_2(g)$",
                "is_correct": False,
                "rationale": "Elemental calcium is a metal, not a metal compound, and $\\text{H}_2$ gas burns with a pop rather than extinguishing flame without burning."
            },
            {
                "id": "D",
                "text": "$\\text{Ca(OH)}_2(aq) + 2\\text{HCl}(aq) \\rightarrow \\text{CaCl}_2(aq) + 2\\text{H}_2\\text{O}(l)$",
                "is_correct": False,
                "rationale": "Neutralisation of slaked lime does not produce gas effervescence."
            }
        ],
        "difficulty": "medium"
    },

    # -------------------------------------------------------------
    # SECTION 3: IN-TEXT "QUESTIONS" (Page 28)
    # -------------------------------------------------------------
    {
        "id": "sci_ch2_p28_q01",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 28)",
        "question_number": "1",
        "text": "Why do aqueous solutions of $\\text{HCl}$ and $\\text{HNO}_3$ show acidic character, whereas solutions of compounds like alcohol and glucose do not?",
        "options": [
            {
                "id": "A",
                "text": "$\\text{HCl}$ and $\\text{HNO}_3$ dissociate in water to produce free $\\text{H}^+(aq)$ (hydronium) ions, whereas glucose and alcohol do not ionize.",
                "is_correct": True,
                "rationale": "Acidic behavior depends strictly on the release of $\\text{H}^+(aq) / \\text{H}_3\\text{O}^+$ ions in aqueous solution. Covalent compounds like alcohol and glucose do not ionize."
            },
            {
                "id": "B",
                "text": "$\\text{HCl}$ and $\\text{HNO}_3$ contain oxygen atoms while glucose and alcohol do not contain any oxygen.",
                "is_correct": False,
                "rationale": "Glucose ($\\text{C}_6\\text{H}_{12}\\text{O}_6$) and alcohol ($\\text{C}_2\\text{H}_5\\text{OH}$) both contain oxygen; oxygen content does not dictate acidity."
            },
            {
                "id": "C",
                "text": "Glucose and alcohol react with water to form strongly basic hydroxide ions that suppress acidity.",
                "is_correct": False,
                "rationale": "Glucose and alcohol do not generate hydroxide ions; they remain neutral non-electrolytes."
            },
            {
                "id": "D",
                "text": "$\\text{HCl}$ and $\\text{HNO}_3$ evaporate instantly in water, leaving solid hydrogen ions behind.",
                "is_correct": False,
                "rationale": "Acids dissolve and ionize in water; they do not separate by instantaneous evaporation."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch2_p28_q02",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 28)",
        "question_number": "2",
        "text": "Why does an aqueous solution of an acid conduct electricity?",
        "options": [
            {
                "id": "A",
                "text": "Because it dissociates into mobile cations ($\\text{H}^+_3\\text{O}$) and anions that carry electric current through the liquid.",
                "is_correct": True,
                "rationale": "Electrolytic conduction in solution requires mobile ions. Acids ionize into $\\text{H}^+(aq)$ and corresponding anions, which migrate toward electrodes under an electric field."
            },
            {
                "id": "B",
                "text": "Because pure water molecules contain free metallic electrons that transmit current.",
                "is_correct": False,
                "rationale": "Water has covalent bonding and lacks free metallic electrons."
            },
            {
                "id": "C",
                "text": "Because the acid dissolves the copper connecting wires to complete the physical circuit.",
                "is_correct": False,
                "rationale": "Conduction is ionic through the electrolyte, not due to dissolving external wiring."
            },
            {
                "id": "D",
                "text": "Because acid molecules heat the solution to glowing incandescent temperatures.",
                "is_correct": False,
                "rationale": "Aqueous electrical conduction does not rely on thermal incandescence."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_p28_q03",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 28)",
        "question_number": "3",
        "text": "Why does dry $\\text{HCl}$ gas not change the colour of dry litmus paper?",
        "options": [
            {
                "id": "A",
                "text": "In the absence of moisture, $\\text{HCl}$ cannot dissociate to form $\\text{H}^+$ ions which are responsible for acidic color change.",
                "is_correct": True,
                "rationale": "Litmus indicator color change is triggered exclusively by hydrogen/hydronium ions. Dry $\\text{HCl}$ exists as covalent molecules and cannot ionize without water."
            },
            {
                "id": "B",
                "text": "Dry $\\text{HCl}$ gas is a strong base that neutralizes red litmus immediately.",
                "is_correct": False,
                "rationale": "$\\text{HCl}$ is an acidic gas, not a base."
            },
            {
                "id": "C",
                "text": "Litmus paper dye is insoluble in all gaseous states of matter.",
                "is_correct": False,
                "rationale": "Moist litmus paper readily changes color in dry $\\text{HCl}$ gas because moisture provides the medium for ionization."
            },
            {
                "id": "D",
                "text": "Dry $\\text{HCl}$ gas decomposes dry litmus dye into free nitrogen gas.",
                "is_correct": False,
                "rationale": "Litmus paper is not degraded into nitrogen gas by dry $\\text{HCl}$."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch2_p28_q04",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 28)",
        "question_number": "4",
        "text": "While diluting an acid, why is it strictly recommended that acid should be added to water and never water to acid?",
        "options": [
            {
                "id": "A",
                "text": "The dilution of acid is highly exothermic; adding water to concentrated acid causes violent boiling, acid splashes, and glass breakage.",
                "is_correct": True,
                "rationale": "Mixing concentrated acid with water releases massive heat. Adding acid slowly to a large volume of water with constant stirring allows water to absorb and dissipate the heat safely."
            },
            {
                "id": "B",
                "text": "Adding water to acid converts the acid into a non-reactive neutral hydrocarbon.",
                "is_correct": False,
                "rationale": "Dilution is a physical hydration process, not hydrocarbon synthesis."
            },
            {
                "id": "C",
                "text": "Water is denser than acid and sinks immediately, preventing any chemical interaction.",
                "is_correct": False,
                "rationale": "Concentrated sulphuric acid is denser than water ($1.84\\text{ g/cm}^3$ vs $1.0\\text{ g/cm}^3$)."
            },
            {
                "id": "D",
                "text": "Acid dissolves water molecules into oxygen and hydrogen gas, causing a gas fire.",
                "is_correct": False,
                "rationale": "Dilution does not electrolyze water into flammable hydrogen and oxygen gases."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_p28_q05",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 28)",
        "question_number": "5",
        "text": "How is the concentration of hydronium ions ($\\text{H}_3\\text{O}^+$) affected when a solution of an acid is diluted?",
        "options": [
            {
                "id": "A",
                "text": "The concentration of hydronium ions per unit volume decreases.",
                "is_correct": True,
                "rationale": "On adding water to an acid solution, the total volume increases while the number of $\\text{H}_3\\text{O}^+$ ions remains constant, so their concentration per unit volume decreases."
            },
            {
                "id": "B",
                "text": "The concentration of hydronium ions per unit volume increases significantly.",
                "is_correct": False,
                "rationale": "Dilution increases volume, decreasing concentration."
            },
            {
                "id": "C",
                "text": "The concentration remains completely unaffected because water cannot interact with ions.",
                "is_correct": False,
                "rationale": "Concentration is inversely proportional to volume ($C = n/V$)."
            },
            {
                "id": "D",
                "text": "Hydronium ions are completely converted into molecular hydroxide ions.",
                "is_correct": False,
                "rationale": "Diluting an acid decreases $[\text{H}_3\text{O}^+]$, but does not make the solution basic."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_p28_q06",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 28)",
        "question_number": "6",
        "text": "How is the concentration of hydroxide ions ($\\text{OH}^-$) affected when excess base is dissolved in a solution of sodium hydroxide?",
        "options": [
            {
                "id": "A",
                "text": "The concentration of hydroxide ions per unit volume increases.",
                "is_correct": True,
                "rationale": "Dissolving more base adds additional $\\text{OH}^-$ ions to the fixed volume, thereby increasing $[\text{OH}^-]$ per unit volume."
            },
            {
                "id": "B",
                "text": "The concentration of hydroxide ions decreases due to ionic saturation precipitation.",
                "is_correct": False,
                "rationale": "Adding solute before saturation increases concentration."
            },
            {
                "id": "C",
                "text": "Hydroxide ions decompose into gaseous oxygen and hydrogen.",
                "is_correct": False,
                "rationale": "Base dissolution does not cause decomposition into gaseous elements."
            },
            {
                "id": "D",
                "text": "The concentration remains unaltered as sodium hydroxide cannot dissociate further.",
                "is_correct": False,
                "rationale": "Added $\\text{NaOH}$ dissociates directly into $\\text{Na}^+$ and $\\text{OH}^-$, increasing the ion count."
            }
        ],
        "difficulty": "easy"
    },

    # -------------------------------------------------------------
    # SECTION 4: IN-TEXT "QUESTIONS" (Page 33)
    # -------------------------------------------------------------
    {
        "id": "sci_ch2_p33_q01",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 33)",
        "question_number": "1",
        "text": "You have two solutions, A and B. The pH of solution A is 6 and pH of solution B is 8. Which solution has higher hydrogen ion concentration, and which is acidic / basic?",
        "options": [
            {
                "id": "A",
                "text": "Solution A has higher $[\\text{H}^+]$ concentration; Solution A is acidic and Solution B is basic.",
                "is_correct": True,
                "rationale": "$\\text{pH} = -\\log_{10}[\\text{H}^+]$. A lower pH value denotes higher $[\\text{H}^+]$. $\\text{pH} < 7$ is acidic (Solution A), and $\\text{pH} > 7$ is basic (Solution B)."
            },
            {
                "id": "B",
                "text": "Solution B has higher $[\\text{H}^+]$ concentration; Solution B is acidic and Solution A is basic.",
                "is_correct": False,
                "rationale": "Higher pH means lower hydrogen ion concentration, not higher."
            },
            {
                "id": "C",
                "text": "Both solutions have equal $[\\text{H}^+]$ concentration because they are symmetrically spaced around pH 7.",
                "is_correct": False,
                "rationale": "Solution A has $[\\text{H}^+] = 10^{-6}\\text{ M}$ while B has $10^{-8}\\text{ M}$, a 100-fold difference."
            },
            {
                "id": "D",
                "text": "Solution A is neutral, while Solution B is strongly acidic.",
                "is_correct": False,
                "rationale": "Neutral pH is exactly 7.0 at $25^\\circ\\text{C}$."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_p33_q02",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 33)",
        "question_number": "2",
        "text": "What effect does increasing the concentration of $\\text{H}^+(aq)$ ions have on the nature of a solution?",
        "options": [
            {
                "id": "A",
                "text": "The solution becomes more strongly acidic and its pH value decreases.",
                "is_correct": True,
                "rationale": "Acidity is directly determined by $[\\text{H}^+(aq)]$. As $[\\text{H}^+]$ rises, the acidity increases and $\\text{pH}$ drops."
            },
            {
                "id": "B",
                "text": "The solution becomes alkaline and its pH value rises above 12.",
                "is_correct": False,
                "rationale": "Alkalinity corresponds to higher $[\\text{OH}^-]$, not higher $[\\text{H}^+]$."
            },
            {
                "id": "C",
                "text": "The solution becomes neutral as excess hydrogen ions cancel each other out.",
                "is_correct": False,
                "rationale": "Hydrogen ions do not cancel each other out."
            },
            {
                "id": "D",
                "text": "The electrical conductivity of the solution drops to zero.",
                "is_correct": False,
                "rationale": "More ions increase electrical conductivity."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_p33_q03",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 33)",
        "question_number": "3",
        "text": "Do basic solutions also have $\\text{H}^+(aq)$ ions? If yes, why are they classified as basic?",
        "options": [
            {
                "id": "A",
                "text": "Yes, basic solutions contain $\\text{H}^+$ ions from water auto-ionization, but $[\\text{OH}^-] \\gg [\\text{H}^+]$.",
                "is_correct": True,
                "rationale": "In all aqueous solutions, $[\\text{H}^+][\\text{OH}^-] = K_w = 10^{-14}$. Basic solutions have $\\text{H}^+$ ions, but the concentration of hydroxide ions is far greater."
            },
            {
                "id": "B",
                "text": "No, basic solutions contain zero $\\text{H}^+$ ions because bases destroy all protons.",
                "is_correct": False,
                "rationale": "Water always contains an equilibrium amount of $\\text{H}^+$ ions."
            },
            {
                "id": "C",
                "text": "Yes, but $\\text{H}^+$ ions in bases carry negative charges instead of positive charges.",
                "is_correct": False,
                "rationale": "Hydrogen ions are always positively charged cations ($H^+$)."
            },
            {
                "id": "D",
                "text": "No, bases are composed exclusively of pure sodium metal atoms.",
                "is_correct": False,
                "rationale": "Bases are compounds like hydroxides or oxides, not pure sodium metal."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch2_p33_q04",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Page 33)",
        "question_number": "4",
        "text": "Under what soil condition would a farmer treat the soil of his fields with quick lime ($\\text{CaO}$), slaked lime ($\\text{Ca(OH)}_2$), or chalk ($\\text{CaCO}_3$)?",
        "options": [
            {
                "id": "A",
                "text": "When the soil is overly acidic (pH too low for optimal crop growth).",
                "is_correct": True,
                "rationale": "Quick lime ($\\text{CaO}$), slaked lime ($\\text{Ca(OH)}_2$), and chalk ($\\text{CaCO}_3$) are basic in nature and neutralize excessive soil acidity."
            },
            {
                "id": "B",
                "text": "When the soil is excessively alkaline with pH greater than 10.",
                "is_correct": False,
                "rationale": "Adding basic calcium compounds to alkaline soil would make it even more alkaline."
            },
            {
                "id": "C",
                "text": "When the soil is saturated with excessive moisture from flooding.",
                "is_correct": False,
                "rationale": "Lining is applied to regulate chemical pH, not for physical flood drainage."
            },
            {
                "id": "D",
                "text": "When the farmer wants to dissolve earthworms and microbial organic matter.",
                "is_correct": False,
                "rationale": "The purpose is creating an optimal pH (around 6.5–7.5) for plant nutrition."
            }
        ],
        "difficulty": "easy"
    },

    # -------------------------------------------------------------
    # SECTION 5: IN-TEXT "QUESTIONS" (Pages 34-35)
    # -------------------------------------------------------------
    {
        "id": "sci_ch2_p34_q01",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Pages 34-35)",
        "question_number": "1",
        "text": "What is the common chemical name of the compound $\\text{CaOCl}_2$?",
        "options": [
            {
                "id": "A",
                "text": "Bleaching powder",
                "is_correct": True,
                "rationale": "Calcium oxychloride ($\\text{CaOCl}_2$) is commonly known as bleaching powder."
            },
            {
                "id": "B",
                "text": "Baking soda",
                "is_correct": False,
                "rationale": "Baking soda is sodium hydrogencarbonate ($\\text{NaHCO}_3$)."
            },
            {
                "id": "C",
                "text": "Washing soda",
                "is_correct": False,
                "rationale": "Washing soda is sodium carbonate decahydrate ($\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}$)."
            },
            {
                "id": "D",
                "text": "Plaster of Paris",
                "is_correct": False,
                "rationale": "Plaster of Paris is calcium sulphate hemihydrate ($\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O}$)."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_p34_q02",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Pages 34-35)",
        "question_number": "2",
        "text": "Name the substance which on treatment with chlorine gas yields bleaching powder.",
        "options": [
            {
                "id": "A",
                "text": "Dry slaked lime [$\\text{Ca(OH)}_2$]",
                "is_correct": True,
                "rationale": "Bleaching powder is manufactured by passing chlorine gas over dry slaked lime: $\\text{Ca(OH)}_2 + \\text{Cl}_2 \\rightarrow \\text{CaOCl}_2 + \\text{H}_2\\text{O}$."
            },
            {
                "id": "B",
                "text": "Limestone [$\\text{CaCO}_3$]",
                "is_correct": False,
                "rationale": "Limestone does not react with chlorine under standard conditions to form bleaching powder."
            },
            {
                "id": "C",
                "text": "Gypsum [$\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}$]",
                "is_correct": False,
                "rationale": "Gypsum is hydrated calcium sulphate, not the precursor for bleaching powder."
            },
            {
                "id": "D",
                "text": "Sodium chloride [$\\text{NaCl}$]",
                "is_correct": False,
                "rationale": "$\\text{NaCl}$ is used to generate chlorine gas via chlor-alkali, but the reactant that absorbs chlorine is slaked lime."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_p34_q03",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Pages 34-35)",
        "question_number": "3",
        "text": "Which sodium compound is used for softening hard water?",
        "options": [
            {
                "id": "A",
                "text": "Washing soda (Sodium carbonate decahydrate, $\\text{Na}_2\\text{CO}_3 \\cdot 10\\text{H}_2\\text{O}$)",
                "is_correct": True,
                "rationale": "Washing soda reacts with dissolved calcium and magnesium ions in hard water, precipitating them as insoluble carbonates."
            },
            {
                "id": "B",
                "text": "Sodium chloride ($\\text{NaCl}$)",
                "is_correct": False,
                "rationale": "Sodium chloride does not precipitate calcium and magnesium ions to soften water."
            },
            {
                "id": "C",
                "text": "Sodium hydroxide ($\\text{NaOH}$)",
                "is_correct": False,
                "rationale": "$\\text{NaOH}$ is caustic soda, used in soap manufacture, not primary domestic water softening."
            },
            {
                "id": "D",
                "text": "Sodium nitrate ($\\text{NaNO}_3$)",
                "is_correct": False,
                "rationale": "Sodium nitrate is a soluble fertilizer and does not soften hard water."
            }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_p34_q04",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Pages 34-35)",
        "question_number": "4",
        "text": "What happens when a solution of sodium hydrogencarbonate is heated? Give the balanced equation.",
        "options": [
            {
                "id": "A",
                "text": "It decomposes to form sodium carbonate, water, and carbon dioxide: $2\\text{NaHCO}_3 \\xrightarrow{\\Delta} \\text{Na}_2\\text{CO}_3 + \\text{H}_2\\text{O} + \\text{CO}_2$",
                "is_correct": True,
                "rationale": "Thermal decomposition of sodium hydrogencarbonate releases carbon dioxide gas, which causes bread and cakes to rise."
            },
            {
                "id": "B",
                "text": "It oxidizes into sodium peroxide and hydrogen gas: $2\\text{NaHCO}_3 \\xrightarrow{\\Delta} \\text{Na}_2\\text{O}_2 + 2\\text{CO} + \\text{H}_2$",
                "is_correct": False,
                "rationale": "Heating hydrogencarbonates yields carbonate and $\\text{CO}_2$, not peroxide."
            },
            {
                "id": "C",
                "text": "It sublimes into sodium metal vapors without any chemical reaction.",
                "is_correct": False,
                "rationale": "$\\text{NaHCO}_3$ undergoes chemical decomposition, not physical sublimation."
            },
            {
                "id": "D",
                "text": "It reduces to form sodium hydride and oxygen gas: $\\text{NaHCO}_3 \\xrightarrow{\\Delta} \\text{NaH} + \\text{CO}_2 + \\text{O}_2$",
                "is_correct": False,
                "rationale": "Sodium hydride is not formed by heating baking soda."
            }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch2_p34_q05",
        "chapter": "Acids, Bases and Salts",
        "section": "QUESTIONS (Pages 34-35)",
        "question_number": "5",
        "text": "Write the balanced chemical equation showing the reaction between Plaster of Paris and water.",
        "options": [
            {
                "id": "A",
                "text": "$\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O} + 1\\frac{1}{2}\\text{H}_2\\text{O} \\rightarrow \\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}$",
                "is_correct": True,
                "rationale": "Plaster of Paris (calcium sulphate hemihydrate) combines with one and a half molecules of water to reform gypsum (a hard solid mass)."
            },
            {
                "id": "B",
                "text": "$\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O} + \\text{H}_2\\text{O} \\rightarrow \\text{CaSO}_4 \\cdot 3\\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "$\\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}$ is gypsum, not Plaster of Paris."
            },
            {
                "id": "C",
                "text": "$\\text{CaSO}_4 + 2\\text{H}_2\\text{O} \\rightarrow \\text{Ca(OH)}_2 + \\text{H}_2\\text{SO}_4$",
                "is_correct": False,
                "rationale": "Anhydrous calcium sulphate does not hydrolyze into slaked lime and sulphuric acid."
            },
            {
                "id": "D",
                "text": "$\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O} \\rightarrow \\text{CaO} + \\text{SO}_3 + \\frac{1}{2}\\text{H}_2\\text{O}$",
                "is_correct": False,
                "rationale": "This represents destructive pyrolytic decomposition, not reaction with water."
            }
        ],
        "difficulty": "easy"
    },

    # -------------------------------------------------------------
    # SECTION 6: END-OF-CHAPTER "EXERCISES" (Pages 34-36)
    # -------------------------------------------------------------
    {
        "id": "sci_ch2_ex01",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "1",
        "text": "A solution turns red litmus blue, its pH is likely to be:",
        "options": [
            { "id": "A", "text": "1", "is_correct": False, "rationale": "pH 1 is strongly acidic; turns blue litmus red." },
            { "id": "B", "text": "4", "is_correct": False, "rationale": "pH 4 is acidic; leaves red litmus red." },
            { "id": "C", "text": "5", "is_correct": False, "rationale": "pH 5 is acidic; does not turn red litmus blue." },
            { "id": "D", "text": "10", "is_correct": True, "rationale": "Basic solutions (pH > 7) turn red litmus blue. Among the given options, only pH 10 is basic." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex02",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "2",
        "text": "A solution reacts with crushed egg-shells to give a gas that turns lime-water milky. The solution contains:",
        "options": [
            { "id": "A", "text": "$\\text{NaCl}$", "is_correct": False, "rationale": "Neutral salt; does not react with egg-shells." },
            { "id": "B", "text": "$\\text{HCl}$", "is_correct": True, "rationale": "Egg-shells are calcium carbonate ($\\text{CaCO}_3$). $\\text{HCl}$ reacts with $\\text{CaCO}_3$ releasing $\\text{CO}_2$, which turns lime water milky." },
            { "id": "C", "text": "$\\text{LiCl}$", "is_correct": False, "rationale": "Neutral salt; does not evolve $\\text{CO}_2$ from carbonate." },
            { "id": "D", "text": "$\\text{KCl}$", "is_correct": False, "rationale": "Neutral salt; unreactive toward calcium carbonate." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex03",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "3",
        "text": "$10\\text{ mL}$ of a solution of $\\text{NaOH}$ is completely neutralised by $8\\text{ mL}$ of a given solution of $\\text{HCl}$. If we take $20\\text{ mL}$ of the same solution of $\\text{NaOH}$, the amount of $\\text{HCl}$ solution required to neutralise it will be:",
        "options": [
            { "id": "A", "text": "$4\\text{ mL}$", "is_correct": False, "rationale": "Halving acid volume would only neutralize $5\\text{ mL}$ of base." },
            { "id": "B", "text": "$8\\text{ mL}$", "is_correct": False, "rationale": "This amount only neutralizes $10\\text{ mL}$ of $\\text{NaOH}$." },
            { "id": "C", "text": "$12\\text{ mL}$", "is_correct": False, "rationale": "Neutralizes $15\\text{ mL}$ of $\\text{NaOH}$." },
            { "id": "D", "text": "$16\\text{ mL}$", "is_correct": True, "rationale": "Neutralisation stoichiometry is linear: $20\\text{ mL } \\text{NaOH} = 2 \\times 10\\text{ mL}$, requiring $2 \\times 8\\text{ mL} = 16\\text{ mL}$ of $\\text{HCl}$." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex04",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "4",
        "text": "Which one of the following types of medicines is used for treating indigestion?",
        "options": [
            { "id": "A", "text": "Antibiotic", "is_correct": False, "rationale": "Used to treat bacterial infections, not stomach acidity." },
            { "id": "B", "text": "Analgesic", "is_correct": False, "rationale": "Used for pain relief." },
            { "id": "C", "text": "Antacid", "is_correct": True, "rationale": "Indigestion is caused by excess gastric $\\text{HCl}$. Antacids are mild bases (e.g., milk of magnesia) that neutralize excess acid." },
            { "id": "D", "text": "Antiseptic", "is_correct": False, "rationale": "Used on living tissues to prevent microbial infection." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex05_a",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "5(a)",
        "text": "Write the balanced chemical equation for the reaction: Dilute sulphuric acid reacts with zinc granules.",
        "options": [
            { "id": "A", "text": "$\\text{Zn}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{ZnSO}_4(aq) + \\text{H}_2(g)$", "is_correct": True, "rationale": "Zinc displaces hydrogen from dilute sulphuric acid forming zinc sulphate and hydrogen gas." },
            { "id": "B", "text": "$\\text{Zn}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{ZnO}(s) + \\text{SO}_2(g) + \\text{H}_2\\text{O}(l)$", "is_correct": False, "rationale": "This requires hot concentrated sulphuric acid, not dilute." },
            { "id": "C", "text": "$2\\text{Zn}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{Zn}_2\\text{SO}_4(aq) + \\text{H}_2(g)$", "is_correct": False, "rationale": "Zinc valency is $+2$; $\\text{Zn}_2\\text{SO}_4$ is an incorrect formula." },
            { "id": "D", "text": "$\\text{Zn}(s) + 2\\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{Zn(HSO}_4)_2(aq) + \\text{H}_2(g)$", "is_correct": False, "rationale": "Standard reaction yields neutral sulphate, not bisulphate." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex05_b",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "5(b)",
        "text": "Write the balanced chemical equation for the reaction: Dilute hydrochloric acid reacts with magnesium ribbon.",
        "options": [
            { "id": "A", "text": "$\\text{Mg}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{MgCl}_2(aq) + \\text{H}_2(g)$", "is_correct": True, "rationale": "Magnesium reacts vigorously with dilute hydrochloric acid producing magnesium chloride and hydrogen gas." },
            { "id": "B", "text": "$\\text{Mg}(s) + \\text{HCl}(aq) \\rightarrow \\text{MgCl}(aq) + \\text{H}(g)$", "is_correct": False, "rationale": "Magnesium is divalent ($\text{MgCl}_2$) and hydrogen is diatomic ($\text{H}_2$)." },
            { "id": "C", "text": "$\\text{Mg}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{MgCl}_2(aq) + 2\\text{H}_2(g)$", "is_correct": False, "rationale": "Hydrogen atoms are unbalanced." },
            { "id": "D", "text": "$2\\text{Mg}(s) + 2\\text{HCl}(aq) \\rightarrow 2\\text{MgCl}(aq) + \\text{H}_2(g)$", "is_correct": False, "rationale": "Formula $\\text{MgCl}$ is incorrect." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex05_c",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "5(c)",
        "text": "Write the balanced chemical equation for the reaction: Dilute sulphuric acid reacts with aluminium powder.",
        "options": [
            { "id": "A", "text": "$2\\text{Al}(s) + 3\\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{Al}_2(\\text{SO}_4)_3(aq) + 3\\text{H}_2(g)$", "is_correct": True, "rationale": "Two moles of trivalent aluminium react with three moles of sulphuric acid to produce aluminium sulphate and three moles of hydrogen." },
            { "id": "B", "text": "$\\text{Al}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{AlSO}_4(aq) + \\text{H}_2(g)$", "is_correct": False, "rationale": "$\\text{AlSO}_4$ violates aluminium $+3$ valency." },
            { "id": "C", "text": "$2\\text{Al}(s) + \\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{Al}_2\\text{SO}_4(aq) + \\text{H}_2(g)$", "is_correct": False, "rationale": "Incorrect chemical formula and unbalanced atoms." },
            { "id": "D", "text": "$\\text{Al}(s) + 3\\text{H}_2\\text{SO}_4(aq) \\rightarrow \\text{Al(SO}_4)_3(aq) + 3\\text{H}_2(g)$", "is_correct": False, "rationale": "Formula $\\text{Al(SO}_4)_3$ is chemically invalid." }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch2_ex05_d",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "5(d)",
        "text": "Write the balanced chemical equation for the reaction: Dilute hydrochloric acid reacts with iron filings.",
        "options": [
            { "id": "A", "text": "$\\text{Fe}(s) + 2\\text{HCl}(aq) \\rightarrow \\text{FeCl}_2(aq) + \\text{H}_2(g)$", "is_correct": True, "rationale": "Reaction of iron with dilute hydrochloric acid forms ferrous chloride (iron(II) chloride) and hydrogen gas." },
            { "id": "B", "text": "$2\\text{Fe}(s) + 6\\text{HCl}(aq) \\rightarrow 2\\text{FeCl}_3(aq) + 3\\text{H}_2(g)$", "is_correct": False, "rationale": "Dilute $\\text{HCl}$ yields iron(II) chloride, not iron(III) chloride." },
            { "id": "C", "text": "$\\text{Fe}(s) + \\text{HCl}(aq) \\rightarrow \\text{FeCl}(aq) + \\text{H}(g)$", "is_correct": False, "rationale": "Monoatomic hydrogen and $\\text{FeCl}$ are chemically incorrect." },
            { "id": "D", "text": "$\\text{Fe}(s) + 4\\text{HCl}(aq) \\rightarrow \\text{FeCl}_4(aq) + 2\\text{H}_2(g)$", "is_correct": False, "rationale": "$\\text{FeCl}_4$ does not form in standard aqueous displacement." }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch2_ex07",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "7",
        "text": "Why does distilled water not conduct electricity, whereas rain water does?",
        "options": [
            { "id": "A", "text": "Distilled water is pure and devoid of ionic species, whereas rain water dissolves atmospheric gases like $\\text{CO}_2$ and $\\text{SO}_2$ forming conducting ions like $\\text{H}^+$ and $\\text{CO}_3^{2-}$.", "is_correct": True, "rationale": "Electrical conduction requires mobile ions. Distilled water contains virtually no free ions, while rain water forms weak acids (e.g., $\\text{H}_2\\text{CO}_3$) providing free ions." },
            { "id": "B", "text": "Distilled water contains excessive oil molecules that insulate against current.", "is_correct": False, "rationale": "Distilled water is pure water without oils." },
            { "id": "C", "text": "Rain water contains free copper electrons transferred from clouds.", "is_correct": False, "rationale": "Conduction in rain water is ionic, not metallic copper conduction." },
            { "id": "D", "text": "Distilled water is frozen at molecular levels, preventing current flow.", "is_correct": False, "rationale": "Liquid distilled water is not frozen." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex08",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "8",
        "text": "Why do acids not show acidic behaviour in the absence of water?",
        "options": [
            { "id": "A", "text": "Dissociation of acid molecules into hydrogen ions ($\\text{H}^+$) occurs strictly in the presence of water, as water stabilizes $\\text{H}^+$ as hydronium ($\\text{H}_3\\text{O}^+$).", "is_correct": True, "rationale": "Protons cannot exist independently; they must coordinate with water to form $\\text{H}_3\\text{O}^+$. Without water, no ionization occurs." },
            { "id": "B", "text": "In the absence of water, acids freeze solid and turn into alkaline hydroxides.", "is_correct": False, "rationale": "Acids do not turn into alkaline hydroxides." },
            { "id": "C", "text": "Water acts as a fuel that burns acid molecules into acidic fumes.", "is_correct": False, "rationale": "Acid behavior is ionic, not combustion-driven." },
            { "id": "D", "text": "Dry acid molecules are blocked by atmospheric nitrogen from changing litmus.", "is_correct": False, "rationale": "Nitrogen does not chemically block acid ionization." }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch2_ex09",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "9",
        "text": "Five solutions A, B, C, D and E tested with universal indicator showed pH values 4, 1, 11, 7 and 9 respectively. Which solution is neutral and which is strongly acidic?",
        "options": [
            { "id": "A", "text": "Solution D (pH 7) is neutral; Solution B (pH 1) is strongly acidic.", "is_correct": True, "rationale": "pH 7 indicates a neutral solution (D). The lowest pH value (1) denotes the highest $[\text{H}^+]$ concentration, which is strongly acidic (B)." },
            { "id": "B", "text": "Solution C (pH 11) is neutral; Solution A (pH 4) is strongly acidic.", "is_correct": False, "rationale": "pH 11 is strongly alkaline, not neutral." },
            { "id": "C", "text": "Solution D (pH 7) is strongly alkaline; Solution E (pH 9) is neutral.", "is_correct": False, "rationale": "pH 7 is neutral; pH 9 is weakly alkaline." },
            { "id": "D", "text": "Solution B (pH 1) is neutral; Solution D (pH 7) is strongly acidic.", "is_correct": False, "rationale": "Inverted logic; pH 1 is strongly acidic." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex10",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "10",
        "text": "Equal lengths of magnesium ribbons are placed in test tubes A (with $\\text{HCl}$) and B (with $\\text{CH}_3\\text{COOH}$). In which test tube will fizzing occur more vigorously and why?",
        "options": [
            { "id": "A", "text": "Test tube A; $\\text{HCl}$ is a strong acid that completely ionizes, producing a much higher $[\\text{H}^+]$ concentration than weak $\\text{CH}_3\\text{COOH}$.", "is_correct": True, "rationale": "Higher $[\text{H}^+]$ in strong acid $\\text{HCl}$ leads to a faster reaction rate with magnesium ribbon, evolving $\\text{H}_2$ gas much more vigorously." },
            { "id": "B", "text": "Test tube B; acetic acid is an organic acid containing more carbon atoms which accelerate fizzing.", "is_correct": False, "rationale": "Acetic acid is a weak acid with lower $[\text{H}^+]$, reacting much more slowly." },
            { "id": "C", "text": "Both test tubes will fizz at identical rates because equal lengths of magnesium were used.", "is_correct": False, "rationale": "Reaction rate depends heavily on the concentration of $\\text{H}^+$ ions." },
            { "id": "D", "text": "Test tube B; acetic acid dissolves the glass test tube to produce excess gas.", "is_correct": False, "rationale": "Acetic acid does not dissolve laboratory borosilicate glass." }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch2_ex11",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "11",
        "text": "Fresh milk has a pH of 6. How will its pH change as it turns into curd, and why?",
        "options": [
            { "id": "A", "text": "Its pH decreases below 6 because bacteria convert lactose into lactic acid, which increases $[\\text{H}^+]$.", "is_correct": True, "rationale": "Lactobacillus bacteria ferment lactose sugar into lactic acid. Acid formation increases $[\text{H}^+]$ and decreases the pH below 6." },
            { "id": "B", "text": "Its pH increases above 10 because curd is strongly alkaline.", "is_correct": False, "rationale": "Curd is sour and acidic, not alkaline." },
            { "id": "C", "text": "Its pH remains fixed at exactly 6 because milk fats buffer against all acid changes.", "is_correct": False, "rationale": "pH drops significantly as lactic acid builds up." },
            { "id": "D", "text": "Its pH fluctuates between 0 and 14 every minute.", "is_correct": False, "rationale": "The pH drop is steady and irreversible under normal conditions." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex12_a",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "12(a)",
        "text": "A milkman adds a very small amount of baking soda to fresh milk. Why does he shift the pH from 6 to slightly alkaline?",
        "options": [
            { "id": "A", "text": "To prevent the milk from turning sour quickly, as alkaline milk takes longer to reach the acidic curdling threshold.", "is_correct": True, "rationale": "Making milk slightly alkaline neutralizes initial lactic acid, preserving freshness during transport in warm weather." },
            { "id": "B", "text": "To make the milk sweeter and carbonated like a fizzy soft drink.", "is_correct": False, "rationale": "The trace amount does not sweeten or carbonate milk for beverage flavor." },
            { "id": "C", "text": "To bleach the natural yellow tint of milk into pure bright white.", "is_correct": False, "rationale": "Baking soda is a mild alkali, not a bleaching agent." },
            { "id": "D", "text": "To increase the boiling point of milk above $300^\\circ\\text{C}$.", "is_correct": False, "rationale": "Boiling point elevation by trace solute is negligible." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex12_b",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "12(b)",
        "text": "Why does this milk (with added baking soda) take a much longer time to set as curd?",
        "options": [
            { "id": "A", "text": "The lactic acid produced by bacteria must first neutralize the added alkaline baking soda before the pH can drop enough to curdle proteins.", "is_correct": True, "rationale": "Milk coagulates into curd at an acidic pH. The added $\\text{NaHCO}_3$ buffers against acid, requiring extra time for sufficient lactic acid to accumulate." },
            { "id": "B", "text": "Baking soda permanently kills all lactic acid bacteria in the milk.", "is_correct": False, "rationale": "Trace baking soda does not sterilize milk; bacteria continue to grow." },
            { "id": "C", "text": "Baking soda turns milk into a solid crystal that cannot coagulate.", "is_correct": False, "rationale": "Milk remains liquid until acidification causes casein precipitation." },
            { "id": "D", "text": "Baking soda converts milk proteins into gaseous carbon dioxide.", "is_correct": False, "rationale": "Proteins are not converted into gas." }
        ],
        "difficulty": "medium"
    },
    {
        "id": "sci_ch2_ex13",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "13",
        "text": "Why should Plaster of Paris be stored in a moisture-proof container?",
        "options": [
            { "id": "A", "text": "Because it readily absorbs atmospheric moisture to set into hard, unusable gypsum mass.", "is_correct": True, "rationale": "$\\text{CaSO}_4 \\cdot \\frac{1}{2}\\text{H}_2\\text{O} + 1\\frac{1}{2}\\text{H}_2\\text{O} \\rightarrow \\text{CaSO}_4 \\cdot 2\\text{H}_2\\text{O}$ (gypsum). Exposure to moisture causes it to harden and lose its setting property." },
            { "id": "B", "text": "Because moisture causes Plaster of Paris to ignite into an explosive flame.", "is_correct": False, "rationale": "Hydration is mildly exothermic, not flammable or explosive." },
            { "id": "C", "text": "Because moisture evaporates Plaster of Paris into toxic gaseous sulphur.", "is_correct": False, "rationale": "It hydrates to solid gypsum; no toxic gas is released." },
            { "id": "D", "text": "Because water molecules chemically dissolve gypsum into liquid metallic calcium.", "is_correct": False, "rationale": "Calcium metal is never produced by water exposure." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex14",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "14",
        "text": "What is a neutralisation reaction, and which equation correctly illustrates it?",
        "options": [
            { "id": "A", "text": "Reaction between an acid and a base to form salt and water: $\\text{NaOH}(aq) + \\text{HCl}(aq) \\rightarrow \\text{NaCl}(aq) + \\text{H}_2\\text{O}(l)$", "is_correct": True, "rationale": "$\\text{H}^+(aq) + \\text{OH}^-(aq) \\rightarrow \\text{H}_2\\text{O}(l)$. The acid and base neutralize each other's properties to produce neutral salt and water." },
            { "id": "B", "text": "Reaction between two metals to form an alloy: $\\text{Cu} + \\text{Zn} \\rightarrow \\text{Brass}$", "is_correct": False, "rationale": "Alloy formation is a physical mixture, not an acid-base neutralisation." },
            { "id": "C", "text": "Decomposition of water by electricity: $2\\text{H}_2\\text{O} \\rightarrow 2\\text{H}_2 + \\text{O}_2$", "is_correct": False, "rationale": "This is electrolytic decomposition." },
            { "id": "D", "text": "Combustion of charcoal in oxygen: $\\text{C} + \\text{O}_2 \\rightarrow \\text{CO}_2$", "is_correct": False, "rationale": "This is oxidation/combustion." }
        ],
        "difficulty": "easy"
    },
    {
        "id": "sci_ch2_ex15",
        "chapter": "Acids, Bases and Salts",
        "section": "EXERCISES",
        "question_number": "15",
        "text": "Which pair correctly pairs important industrial/domestic uses of washing soda and baking soda?",
        "options": [
            { "id": "A", "text": "Washing soda: glass and soap manufacture; Baking soda: constituent of baking powder and fire extinguishers", "is_correct": True, "rationale": "$\\text{Na}_2\\text{CO}_3$ is used in glass, soap, paper industries and water softening; $\\text{NaHCO}_3$ is used in baking powder, antacids, and soda-acid extinguishers." },
            { "id": "B", "text": "Washing soda: dental anesthesia; Baking soda: airplane jet fuel", "is_correct": False, "rationale": "Neither compound serves as aircraft propellant or anesthetic." },
            { "id": "C", "text": "Washing soda: direct consumption as food condiment; Baking soda: industrial metal welding", "is_correct": False, "rationale": "Washing soda is caustic and toxic if ingested." },
            { "id": "D", "text": "Washing soda: synthesis of radioactive isotopes; Baking soda: motor vehicle engine coolant", "is_correct": False, "rationale": "Fictitious uses unrelated to chemical properties." }
        ],
        "difficulty": "easy"
    }
]

# Validation assertions
assert len(questions) == 37, f"Expected 37 questions, got {len(questions)}"
for q in questions:
    assert len(q["options"]) == 4, f"Question {q['id']} must have exactly 4 options"
    correct_count = sum(1 for o in q["options"] if o["is_correct"])
    assert correct_count == 1, f"Question {q['id']} must have exactly 1 correct option"
    
    correct_opt = next(o for o in q["options"] if o["is_correct"])
    sol_lines = [
        f"Correct Answer: ({correct_opt['id']}) {correct_opt['text']}",
        f"\nScientific Principle / Key Concept:\n{correct_opt['rationale']}",
        "\nDetailed Distractor & Misconception Analysis:"
    ]
    for o in q["options"]:
        if not o["is_correct"]:
            sol_lines.append(f"• Option ({o['id']}): Incorrect. {o['rationale']}")
            
    solution_text = "\n".join(sol_lines)
    q["solution"] = solution_text
    q["step_by_step_solution"] = solution_text
    q["subject"] = "science"
    q["chapterId"] = "sci_ch_02_acids_bases_salts"
    
    sec = q.get("section", "")
    if "Page 18" in sec:
        q["exercise"] = "In-Text (Page 18)"
    elif "Page 22" in sec:
        q["exercise"] = "In-Text (Page 22)"
    elif "Page 28" in sec:
        q["exercise"] = "In-Text (Page 28)"
    elif "Page 33" in sec:
        q["exercise"] = "In-Text (Page 33)"
    elif "Page 34" in sec:
        q["exercise"] = "In-Text (Pages 34-35)"
    else:
        q["exercise"] = "Exercises (Pages 34-36)"
        
    q["questionNumber"] = q.get("question_number", "")
    for o in q["options"]:
        o["correct"] = o["is_correct"]

os.makedirs("assets/data", exist_ok=True)
with open("assets/data/ncert_science_ch2.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2, ensure_ascii=False)

print(f"SUCCESS: Generated {len(questions)} textbook questions for Science Chapter 2 into assets/data/ncert_science_ch2.json")
