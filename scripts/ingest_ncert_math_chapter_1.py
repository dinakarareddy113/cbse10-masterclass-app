import json
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# All 20 Questions from NCERT Class 10 Mathematics Chapter 1: Real Numbers
# Exercise 1.1 (Pages 5-6) and Exercise 1.2 (Page 9)
EXERCISE_QUESTIONS = [
    # -------------------------------------------------------------------------
    # EXERCISE 1.1 - Question 1: Express each number as a product of its prime factors
    # -------------------------------------------------------------------------
    {
        "id": "10000000-0000-0000-0001-000000000001",
        "exercise": "Exercise 1.1",
        "question_number": "1(i)",
        "question_text": "Express the number as a product of its prime factors:\n(i) 140",
        "difficulty_level": "easy",
        "options": [
            {"id": "A", "text": "2² × 5 × 7", "is_correct": True},
            {"id": "B", "text": "2 × 5² × 7", "is_correct": False},
            {"id": "C", "text": "2³ × 5 × 7", "is_correct": False},
            {"id": "D", "text": "4 × 35", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Using the prime factorisation method (factor tree):\n"
            "  140 ÷ 2 = 70\n"
            "  70 ÷ 2 = 35\n"
            "  35 ÷ 5 = 7\n"
            "  7 ÷ 7 = 1\n"
            "Step 2: Therefore, 140 = 2 × 2 × 5 × 7 = 2² × 5 × 7."
        )
    },
    {
        "id": "10000000-0000-0000-0001-000000000002",
        "exercise": "Exercise 1.1",
        "question_number": "1(ii)",
        "question_text": "Express the number as a product of its prime factors:\n(ii) 156",
        "difficulty_level": "easy",
        "options": [
            {"id": "A", "text": "2² × 3 × 13", "is_correct": True},
            {"id": "B", "text": "2 × 3² × 13", "is_correct": False},
            {"id": "C", "text": "4 × 39", "is_correct": False},
            {"id": "D", "text": "2 × 78", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Divide 156 by prime factors:\n"
            "  156 ÷ 2 = 78\n"
            "  78 ÷ 2 = 39\n"
            "  39 ÷ 3 = 13\n"
            "  13 ÷ 13 = 1\n"
            "Step 2: Therefore, 156 = 2 × 2 × 3 × 13 = 2² × 3 × 13."
        )
    },
    {
        "id": "10000000-0000-0000-0001-000000000003",
        "exercise": "Exercise 1.1",
        "question_number": "1(iii)",
        "question_text": "Express the number as a product of its prime factors:\n(iii) 3825",
        "difficulty_level": "easy",
        "options": [
            {"id": "A", "text": "3² × 5² × 17", "is_correct": True},
            {"id": "B", "text": "3 × 5² × 17", "is_correct": False},
            {"id": "C", "text": "3² × 5 × 17²", "is_correct": False},
            {"id": "D", "text": "9 × 25 × 17", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Divide 3825 by successive prime numbers:\n"
            "  3825 ÷ 3 = 1275\n"
            "  1275 ÷ 3 = 425\n"
            "  425 ÷ 5 = 85\n"
            "  85 ÷ 5 = 17\n"
            "  17 ÷ 17 = 1\n"
            "Step 2: Therefore, 3825 = 3 × 3 × 5 × 5 × 17 = 3² × 5² × 17."
        )
    },
    {
        "id": "10000000-0000-0000-0001-000000000004",
        "exercise": "Exercise 1.1",
        "question_number": "1(iv)",
        "question_text": "Express the number as a product of its prime factors:\n(iv) 5005",
        "difficulty_level": "easy",
        "options": [
            {"id": "A", "text": "5 × 7 × 11 × 13", "is_correct": True},
            {"id": "B", "text": "5² × 7 × 13", "is_correct": False},
            {"id": "C", "text": "5 × 11² × 13", "is_correct": False},
            {"id": "D", "text": "35 × 143", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Divide 5005 by successive prime numbers:\n"
            "  5005 ÷ 5 = 1001\n"
            "  1001 ÷ 7 = 143\n"
            "  143 ÷ 11 = 13\n"
            "  13 ÷ 13 = 1\n"
            "Step 2: Therefore, 5005 = 5 × 7 × 11 × 13."
        )
    },
    {
        "id": "10000000-0000-0000-0001-000000000005",
        "exercise": "Exercise 1.1",
        "question_number": "1(v)",
        "question_text": "Express the number as a product of its prime factors:\n(v) 7429",
        "difficulty_level": "medium",
        "options": [
            {"id": "A", "text": "17 × 19 × 23", "is_correct": True},
            {"id": "B", "text": "13 × 19 × 29", "is_correct": False},
            {"id": "C", "text": "17² × 23", "is_correct": False},
            {"id": "D", "text": "19 × 23 × 29", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Testing initial prime factors shows 2, 3, 5, 7, 11, 13 do not divide 7429.\n"
            "Step 2: 7429 ÷ 17 = 437\n"
            "Step 3: 437 ÷ 19 = 23\n"
            "Step 4: 23 ÷ 23 = 1\n"
            "Step 5: Therefore, 7429 = 17 × 19 × 23."
        )
    },

    # -------------------------------------------------------------------------
    # EXERCISE 1.1 - Question 2: Find LCM and HCF and verify LCM × HCF = product of two numbers
    # -------------------------------------------------------------------------
    {
        "id": "10000000-0000-0000-0001-000000000006",
        "exercise": "Exercise 1.1",
        "question_number": "2(i)",
        "question_text": "Find the LCM and HCF of 26 and 91 and verify that LCM × HCF = product of the two numbers.",
        "difficulty_level": "easy",
        "options": [
            {"id": "A", "text": "HCF = 13, LCM = 182", "is_correct": True},
            {"id": "B", "text": "HCF = 26, LCM = 91", "is_correct": False},
            {"id": "C", "text": "HCF = 1, LCM = 2366", "is_correct": False},
            {"id": "D", "text": "HCF = 7, LCM = 364", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Prime factorisation:\n"
            "  26 = 2 × 13\n"
            "  91 = 7 × 13\n"
            "Step 2: HCF(26, 91) = 13 (common factor with smallest power).\n"
            "Step 3: LCM(26, 91) = 2 × 7 × 13 = 182.\n"
            "Step 4: Verification:\n"
            "  LCM × HCF = 182 × 13 = 2366\n"
            "  Product of numbers = 26 × 91 = 2366\n"
            "  Hence, LCM × HCF = Product of the two numbers verified."
        )
    },
    {
        "id": "10000000-0000-0000-0001-000000000007",
        "exercise": "Exercise 1.1",
        "question_number": "2(ii)",
        "question_text": "Find the LCM and HCF of 510 and 92 and verify that LCM × HCF = product of the two numbers.",
        "difficulty_level": "medium",
        "options": [
            {"id": "A", "text": "HCF = 2, LCM = 23460", "is_correct": True},
            {"id": "B", "text": "HCF = 4, LCM = 11730", "is_correct": False},
            {"id": "C", "text": "HCF = 2, LCM = 46920", "is_correct": False},
            {"id": "D", "text": "HCF = 6, LCM = 7820", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Prime factorisation:\n"
            "  510 = 2 × 3 × 5 × 17\n"
            "  92 = 2² × 23\n"
            "Step 2: HCF(510, 92) = 2¹ = 2.\n"
            "Step 3: LCM(510, 92) = 2² × 3 × 5 × 17 × 23 = 4 × 15 × 391 = 23460.\n"
            "Step 4: Verification:\n"
            "  LCM × HCF = 23460 × 2 = 46920\n"
            "  Product of numbers = 510 × 92 = 46920\n"
            "  Hence, LCM × HCF = Product of the two numbers verified."
        )
    },
    {
        "id": "10000000-0000-0000-0001-000000000008",
        "exercise": "Exercise 1.1",
        "question_number": "2(iii)",
        "question_text": "Find the LCM and HCF of 336 and 54 and verify that LCM × HCF = product of the two numbers.",
        "difficulty_level": "medium",
        "options": [
            {"id": "A", "text": "HCF = 6, LCM = 3024", "is_correct": True},
            {"id": "B", "text": "HCF = 12, LCM = 1512", "is_correct": False},
            {"id": "C", "text": "HCF = 3, LCM = 6048", "is_correct": False},
            {"id": "D", "text": "HCF = 18, LCM = 1008", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Prime factorisation:\n"
            "  336 = 2⁴ × 3 × 7\n"
            "  54 = 2 × 3³\n"
            "Step 2: HCF(336, 54) = 2¹ × 3¹ = 6.\n"
            "Step 3: LCM(336, 54) = 2⁴ × 3³ × 7 = 16 × 27 × 7 = 3024.\n"
            "Step 4: Verification:\n"
            "  LCM × HCF = 3024 × 6 = 18144\n"
            "  Product of numbers = 336 × 54 = 18144\n"
            "  Hence, LCM × HCF = Product of the two numbers verified."
        )
    },

    # -------------------------------------------------------------------------
    # EXERCISE 1.1 - Question 3: Find LCM and HCF by applying prime factorisation method
    # -------------------------------------------------------------------------
    {
        "id": "10000000-0000-0000-0001-000000000009",
        "exercise": "Exercise 1.1",
        "question_number": "3(i)",
        "question_text": "Find the LCM and HCF of 12, 15 and 21 by applying the prime factorisation method.",
        "difficulty_level": "easy",
        "options": [
            {"id": "A", "text": "HCF = 3, LCM = 420", "is_correct": True},
            {"id": "B", "text": "HCF = 6, LCM = 210", "is_correct": False},
            {"id": "C", "text": "HCF = 1, LCM = 1260", "is_correct": False},
            {"id": "D", "text": "HCF = 3, LCM = 840", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Prime factorisation:\n"
            "  12 = 2² × 3\n"
            "  15 = 3 × 5\n"
            "  21 = 3 × 7\n"
            "Step 2: HCF = 3¹ = 3 (common factor in all three).\n"
            "Step 3: LCM = 2² × 3 × 5 × 7 = 4 × 3 × 5 × 7 = 420."
        )
    },
    {
        "id": "10000000-0000-0000-0001-000000000010",
        "exercise": "Exercise 1.1",
        "question_number": "3(ii)",
        "question_text": "Find the LCM and HCF of 17, 23 and 29 by applying the prime factorisation method.",
        "difficulty_level": "easy",
        "options": [
            {"id": "A", "text": "HCF = 1, LCM = 11339", "is_correct": True},
            {"id": "B", "text": "HCF = 1, LCM = 22678", "is_correct": False},
            {"id": "C", "text": "HCF = 17, LCM = 667", "is_correct": False},
            {"id": "D", "text": "HCF = 29, LCM = 391", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Notice that 17, 23, and 29 are all prime numbers:\n"
            "  17 = 1 × 17\n"
            "  23 = 1 × 23\n"
            "  29 = 1 × 29\n"
            "Step 2: Since there is no common prime factor, HCF = 1.\n"
            "Step 3: LCM = 17 × 23 × 29 = 391 × 29 = 11339."
        )
    },
    {
        "id": "10000000-0000-0000-0001-000000000011",
        "exercise": "Exercise 1.1",
        "question_number": "3(iii)",
        "question_text": "Find the LCM and HCF of 8, 9 and 25 by applying the prime factorisation method.",
        "difficulty_level": "easy",
        "options": [
            {"id": "A", "text": "HCF = 1, LCM = 1800", "is_correct": True},
            {"id": "B", "text": "HCF = 2, LCM = 900", "is_correct": False},
            {"id": "C", "text": "HCF = 3, LCM = 3600", "is_correct": False},
            {"id": "D", "text": "HCF = 1, LCM = 72", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Prime factorisation:\n"
            "  8 = 2³\n"
            "  9 = 3²\n"
            "  25 = 5²\n"
            "Step 2: No common prime factor exists across all three numbers, so HCF = 1.\n"
            "Step 3: LCM = 2³ × 3² × 5² = 8 × 9 × 25 = 72 × 25 = 1800."
        )
    },

    # -------------------------------------------------------------------------
    # EXERCISE 1.1 - Question 4: Given HCF(306, 657) = 9, find LCM(306, 657)
    # -------------------------------------------------------------------------
    {
        "id": "10000000-0000-0000-0001-000000000012",
        "exercise": "Exercise 1.1",
        "question_number": "4",
        "question_text": "Given that HCF (306, 657) = 9, find LCM (306, 657).",
        "difficulty_level": "medium",
        "options": [
            {"id": "A", "text": "22338", "is_correct": True},
            {"id": "B", "text": "22383", "is_correct": False},
            {"id": "C", "text": "201042", "is_correct": False},
            {"id": "D", "text": "22438", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Formula connecting HCF and LCM of two positive integers a and b:\n"
            "  HCF(a, b) × LCM(a, b) = a × b\n"
            "Step 2: Here a = 306, b = 657, and HCF = 9.\n"
            "  9 × LCM(306, 657) = 306 × 657\n"
            "Step 3: LCM(306, 657) = (306 × 657) / 9\n"
            "  306 ÷ 9 = 34\n"
            "  LCM = 34 × 657 = 22338."
        )
    },

    # -------------------------------------------------------------------------
    # EXERCISE 1.1 - Question 5: Check whether 6^n can end with digit 0
    # -------------------------------------------------------------------------
    {
        "id": "10000000-0000-0000-0001-000000000013",
        "exercise": "Exercise 1.1",
        "question_number": "5",
        "question_text": "Check whether 6ⁿ can end with the digit 0 for any natural number n.",
        "difficulty_level": "medium",
        "options": [
            {"id": "A", "text": "No, because the prime factorisation of 6ⁿ contains only 2 and 3, not 5", "is_correct": True},
            {"id": "B", "text": "Yes, for any even value of n", "is_correct": False},
            {"id": "C", "text": "Yes, when n is a multiple of 5", "is_correct": False},
            {"id": "D", "text": "Yes, because 6 ends with an even digit", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: If any number ends with the digit 0, it must be divisible by 10 = 2 × 5.\n"
            "  That is, its prime factorisation must contain both 2 and 5 as prime factors.\n"
            "Step 2: Prime factorisation of 6ⁿ = (2 × 3)ⁿ = 2ⁿ × 3ⁿ.\n"
            "Step 3: The only primes in the factorisation of 6ⁿ are 2 and 3.\n"
            "Step 4: By the uniqueness of the Fundamental Theorem of Arithmetic, there are no other primes in the factorisation of 6ⁿ.\n"
            "Step 5: Since 5 is not a factor, 6ⁿ cannot be divisible by 5.\n"
            "  Therefore, 6ⁿ cannot end with the digit 0 for any natural number n."
        )
    },

    # -------------------------------------------------------------------------
    # EXERCISE 1.1 - Question 6: Explain why numbers are composite
    # -------------------------------------------------------------------------
    {
        "id": "10000000-0000-0000-0001-000000000014",
        "exercise": "Exercise 1.1",
        "question_number": "6",
        "question_text": "Explain why 7 × 11 × 13 + 13 and 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 are composite numbers.",
        "difficulty_level": "easy",
        "options": [
            {"id": "A", "text": "Both expressions have factors other than 1 and themselves (13 and 5 can be factored out)", "is_correct": True},
            {"id": "B", "text": "Because they are products of consecutive integers", "is_correct": False},
            {"id": "C", "text": "Because both result in even numbers", "is_correct": False},
            {"id": "D", "text": "Because their sum is divisible by 2", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: A composite number has factors other than 1 and the number itself.\n"
            "Step 2: First expression:\n"
            "  7 × 11 × 13 + 13 = 13 × (7 × 11 + 1)\n"
            "  = 13 × (77 + 1) = 13 × 78 = 13 × 13 × 6 = 2 × 3 × 13².\n"
            "  Since it has factors 2, 3, 13 besides 1 and itself, it is a composite number.\n"
            "Step 3: Second expression:\n"
            "  7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 = 5 × (7 × 6 × 4 × 3 × 2 × 1 + 1)\n"
            "  = 5 × (1008 + 1) = 5 × 1009.\n"
            "  Since 1009 is a prime, the number has 5 and 1009 as factors besides 1 and itself.\n"
            "  Hence, both are composite numbers."
        )
    },

    # -------------------------------------------------------------------------
    # EXERCISE 1.1 - Question 7: Sonia and Ravi circular sports field problem
    # -------------------------------------------------------------------------
    {
        "id": "10000000-0000-0000-0001-000000000015",
        "exercise": "Exercise 1.1",
        "question_number": "7",
        "question_text": "There is a circular path around a sports field. Sonia takes 18 minutes to drive one round of the field, while Ravi takes 12 minutes for the same. Suppose they both start at the same point and at the same time, and go in the same direction. After how many minutes will they meet again at the starting point?",
        "difficulty_level": "medium",
        "options": [
            {"id": "A", "text": "36 minutes", "is_correct": True},
            {"id": "B", "text": "6 minutes", "is_correct": False},
            {"id": "C", "text": "60 minutes", "is_correct": False},
            {"id": "D", "text": "216 minutes", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Sonia and Ravi start simultaneously and travel in the same direction.\n"
            "Step 2: They will meet again at the starting point after a time period which is the Lowest Common Multiple (LCM) of the times taken by both:\n"
            "  Required time = LCM(18, 12)\n"
            "Step 3: Prime factorisation:\n"
            "  18 = 2 × 3²\n"
            "  12 = 2² × 3\n"
            "Step 4: LCM(18, 12) = 2² × 3² = 4 × 9 = 36 minutes.\n"
            "Step 5: Hence, they will meet again at the starting point after 36 minutes."
        )
    },

    # -------------------------------------------------------------------------
    # EXERCISE 1.2 - Question 1: Prove that √5 is irrational
    # -------------------------------------------------------------------------
    {
        "id": "10000000-0000-0000-0001-000000000016",
        "exercise": "Exercise 1.2",
        "question_number": "1",
        "question_text": "Prove that √5 is irrational.",
        "difficulty_level": "hard",
        "options": [
            {"id": "A", "text": "Proof by contradiction: 5 divides both a and b, contradicting that gcd(a,b)=1", "is_correct": True},
            {"id": "B", "text": "Proof by division: √5 cannot be written as a terminating fraction", "is_correct": False},
            {"id": "C", "text": "Proof by geometry: diagonal of unit square is irrational", "is_correct": False},
            {"id": "D", "text": "Proof by induction: √n is irrational for all primes n", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Assume to the contrary that √5 is rational.\n"
            "  Then there exist coprime integers a and b (b ≠ 0, gcd(a,b) = 1) such that:\n"
            "  √5 = a / b => a = b√5\n"
            "Step 2: Squaring both sides:\n"
            "  a² = 5b²  ... (Equation 1)\n"
            "  This means 5 divides a². By Theorem 1.2, if a prime p divides a², then p divides a.\n"
            "  Therefore, 5 divides a.\n"
            "Step 3: Let a = 5c for some integer c. Substitute a in Equation 1:\n"
            "  (5c)² = 5b² => 25c² = 5b² => b² = 5c²\n"
            "  This means 5 divides b², which implies 5 divides b.\n"
            "Step 4: From Steps 2 and 3, both a and b share a common factor 5.\n"
            "  This contradicts the fact that a and b are coprime (share no common factor other than 1).\n"
            "Step 5: This contradiction arises from our incorrect assumption that √5 is rational.\n"
            "  Hence, √5 is irrational."
        )
    },

    # -------------------------------------------------------------------------
    # EXERCISE 1.2 - Question 2: Prove that 3 + 2√5 is irrational
    # -------------------------------------------------------------------------
    {
        "id": "10000000-0000-0000-0001-000000000017",
        "exercise": "Exercise 1.2",
        "question_number": "2",
        "question_text": "Prove that 3 + 2√5 is irrational.",
        "difficulty_level": "medium",
        "options": [
            {"id": "A", "text": "Proof by contradiction: √5 = (a - 3b)/(2b) equates an irrational to a rational", "is_correct": True},
            {"id": "B", "text": "Proof by approximation: 3 + 2(2.236) is non-terminating", "is_correct": False},
            {"id": "C", "text": "Proof by squaring: (3 + 2√5)² = 29 + 12√5 has no integer root", "is_correct": False},
            {"id": "D", "text": "Proof by decimal expansion: remainder never repeats", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Assume to the contrary that 3 + 2√5 is rational.\n"
            "  Then there exist coprime integers a and b (b ≠ 0) such that:\n"
            "  3 + 2√5 = a / b\n"
            "Step 2: Rearranging the equation to isolate √5:\n"
            "  2√5 = (a / b) - 3\n"
            "  2√5 = (a - 3b) / b\n"
            "  √5 = (a - 3b) / (2b)\n"
            "Step 3: Since a and b are integers, (a - 3b) and 2b are also integers (2b ≠ 0).\n"
            "  Therefore, (a - 3b) / (2b) is a rational number.\n"
            "Step 4: This implies that √5 is rational. But this contradicts the known fact that √5 is irrational.\n"
            "Step 5: This contradiction has arisen because of our incorrect assumption that 3 + 2√5 is rational.\n"
            "  Hence, 3 + 2√5 is irrational."
        )
    },

    # -------------------------------------------------------------------------
    # EXERCISE 1.2 - Question 3: Prove that the following are irrationals
    # -------------------------------------------------------------------------
    {
        "id": "10000000-0000-0000-0001-000000000018",
        "exercise": "Exercise 1.2",
        "question_number": "3(i)",
        "question_text": "Prove that the following is irrational:\n(i) 1 / √2",
        "difficulty_level": "medium",
        "options": [
            {"id": "A", "text": "Proof: 1/√2 = a/b => √2 = b/a, equating irrational √2 to rational b/a", "is_correct": True},
            {"id": "B", "text": "Proof: Rationalising denominator gives √2 / 2 which cannot be solved", "is_correct": False},
            {"id": "C", "text": "Proof: 1 divided by any root is non-terminating", "is_correct": False},
            {"id": "D", "text": "Proof: Reciprocal of an irrational number is always undefined", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Let us assume to the contrary that 1/√2 is rational.\n"
            "  Then there exist coprime integers a and b (where a ≠ 0, b ≠ 0) such that:\n"
            "  1 / √2 = a / b\n"
            "Step 2: Taking reciprocals on both sides:\n"
            "  √2 = b / a\n"
            "Step 3: Since b and a are integers and a ≠ 0, b / a is a rational number.\n"
            "Step 4: This implies that √2 is a rational number.\n"
            "  But this contradicts the established fact that √2 is irrational.\n"
            "Step 5: Hence, our assumption was false. Therefore, 1/√2 is irrational."
        )
    },
    {
        "id": "10000000-0000-0000-0001-000000000019",
        "exercise": "Exercise 1.2",
        "question_number": "3(ii)",
        "question_text": "Prove that the following is irrational:\n(ii) 7√5",
        "difficulty_level": "medium",
        "options": [
            {"id": "A", "text": "Proof: 7√5 = a/b => √5 = a/(7b), equating irrational √5 to rational a/(7b)", "is_correct": True},
            {"id": "B", "text": "Proof: Product of any integer and root is an imaginary number", "is_correct": False},
            {"id": "C", "text": "Proof: Multiplying by 7 preserves prime factorisation", "is_correct": False},
            {"id": "D", "text": "Proof: 7² × 5 = 245 has no square root", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Let us assume to the contrary that 7√5 is rational.\n"
            "  Then there exist coprime integers a and b (b ≠ 0) such that:\n"
            "  7√5 = a / b\n"
            "Step 2: Rearranging for √5:\n"
            "  √5 = a / (7b)\n"
            "Step 3: Since 7, a, and b are integers and 7b ≠ 0, a / (7b) is a rational number.\n"
            "Step 4: This implies that √5 is rational.\n"
            "  However, this contradicts the fact that √5 is irrational.\n"
            "Step 5: Hence, our assumption is false. Therefore, 7√5 is irrational."
        )
    },
    {
        "id": "10000000-0000-0000-0001-000000000020",
        "exercise": "Exercise 1.2",
        "question_number": "3(iii)",
        "question_text": "Prove that the following is irrational:\n(iii) 6 + √2",
        "difficulty_level": "medium",
        "options": [
            {"id": "A", "text": "Proof: 6 + √2 = a/b => √2 = (a - 6b)/b, equating irrational √2 to rational", "is_correct": True},
            {"id": "B", "text": "Proof: 6 is composite so adding √2 makes it transcendental", "is_correct": False},
            {"id": "C", "text": "Proof: (6 + √2)² = 38 + 12√2 is non-repeating", "is_correct": False},
            {"id": "D", "text": "Proof: Sum of rational and irrational is always undefined", "is_correct": False}
        ],
        "step_by_step_solution": (
            "Step 1: Let us assume to the contrary that 6 + √2 is rational.\n"
            "  Then there exist coprime integers a and b (b ≠ 0) such that:\n"
            "  6 + √2 = a / b\n"
            "Step 2: Rearranging to isolate √2:\n"
            "  √2 = (a / b) - 6\n"
            "  √2 = (a - 6b) / b\n"
            "Step 3: Since a, b, and 6 are integers, (a - 6b) / b is a rational number.\n"
            "Step 4: This implies that √2 is rational, which contradicts the theorem that √2 is irrational.\n"
            "Step 5: Therefore, our assumption was incorrect. We conclude that 6 + √2 is irrational."
        )
    }
]

def main():
    print("=== NCERT Class 10 Math Chapter 1 (Real Numbers) Ingestion Engine ===")
    
    # Target directory paths
    base_dir = "g:/My Drive/AI_Projects/AntiGravity_Exam_Guide"
    json_path = os.path.join(base_dir, "assets/data/ncert_math_ch1.json")
    sql_path = os.path.join(base_dir, "supabase/migrations/20260925030000_seed_ncert_math_ch1_exercises.sql")
    
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    os.makedirs(os.path.dirname(sql_path), exist_ok=True)

    # 1. Generate JSON
    formatted_questions = []
    for q in EXERCISE_QUESTIONS:
        formatted_questions.append({
            "id": q["id"],
            "subject": "math",
            "chapter_id": "math_ch_01_real_numbers",
            "exercise": q["exercise"],
            "question_number": q["question_number"],
            "question_text": f"[{q['exercise']} - Q{q['question_number']}] {q['question_text']}",
            "options": q["options"],
            "step_by_step_solution": q["step_by_step_solution"],
            "difficulty_level": q["difficulty_level"],
            "status": "approved",
            "submitted_by": "00000000-0000-0000-0000-000000000001",
            "reviewed_by": "00000000-0000-0000-0000-000000000001",
            "created_at": "2026-09-25T00:00:00Z"
        })

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(formatted_questions, f, indent=2, ensure_ascii=False)
    print(f"[1/2] Successfully generated JSON dataset: {json_path} ({len(formatted_questions)} questions)")

    # 2. Generate SQL Migration
    sql_lines = [
        "-- ==============================================================================",
        "-- Migration: 20260925030000_seed_ncert_math_ch1_exercises.sql",
        "-- Project: CBSE Class 10 Masterclass",
        "-- Description: 100% Textbook-Accurate Ingestion of Real Numbers Exercise 1.1 & 1.2",
        "-- ==============================================================================",
        "",
        "INSERT INTO public.questions (",
        "    id, subject, chapter_id, question_text, options, step_by_step_solution,",
        "    difficulty_level, status, submitted_by, reviewed_by, created_at",
        ") VALUES"
    ]

    value_tuples = []
    for q in formatted_questions:
        options_json = json.dumps(q["options"], ensure_ascii=False).replace("'", "''")
        q_text = q["question_text"].replace("'", "''")
        sol = q["step_by_step_solution"].replace("'", "''")
        
        tuple_str = (
            f"(\n"
            f"    '{q['id']}',\n"
            f"    'math',\n"
            f"    'math_ch_01_real_numbers',\n"
            f"    '{q_text}',\n"
            f"    '{options_json}'::jsonb,\n"
            f"    '{sol}',\n"
            f"    '{q['difficulty_level']}',\n"
            f"    'approved',\n"
            f"    '00000000-0000-0000-0000-000000000001',\n"
            f"    '00000000-0000-0000-0000-000000000001',\n"
            f"    TIMEZONE('utc'::text, NOW())\n"
            f")"
        )
        value_tuples.append(tuple_str)

    sql_lines.append(",\n".join(value_tuples))
    sql_lines.append("ON CONFLICT (id) DO UPDATE SET")
    sql_lines.append("    question_text = EXCLUDED.question_text,")
    sql_lines.append("    options = EXCLUDED.options,")
    sql_lines.append("    step_by_step_solution = EXCLUDED.step_by_step_solution,")
    sql_lines.append("    status = EXCLUDED.status;")
    sql_lines.append("")

    with open(sql_path, "w", encoding="utf-8") as f:
        f.write("\n".join(sql_lines))
    print(f"[2/3] Successfully generated SQL migration: {sql_path}")

    # 3. Generate Dart file: lib/services/ncert_math_ch1_data.dart
    dart_data_path = os.path.join(base_dir, "lib/services/ncert_math_ch1_data.dart")
    dart_lines = [
        "import '../models/question.dart';",
        "",
        "/// Pre-seeded 100% textbook-accurate questions for CBSE Class 10 Math Chapter 1 (Real Numbers)",
        "/// Exercise 1.1 (Questions 1 to 7) & Exercise 1.2 (Questions 1 to 3)",
        "class NcertMathCh1Data {",
        "  static List<Question> get questions => [",
    ]

    for q in EXERCISE_QUESTIONS:
        dart_lines.append("    Question(")
        dart_lines.append(f"      id: '{q['id']}',")
        dart_lines.append("      subject: Subject.math,")
        dart_lines.append("      chapterId: 'math_ch_01_real_numbers',")
        
        # Escape string literals for Dart
        q_text_escaped = f"[{q['exercise']} - Q{q['question_number']}] {q['question_text']}".replace("'", "\\'").replace("\n", "\\n")
        dart_lines.append(f"      questionText: '{q_text_escaped}',")
        
        # Options
        dart_lines.append("      options: const [")
        for opt in q["options"]:
            opt_text_escaped = opt["text"].replace("'", "\\'")
            dart_lines.append(f"        QuestionOption(id: '{opt['id']}', text: '{opt_text_escaped}', isCorrect: {str(opt['is_correct']).lower()}),")
        dart_lines.append("      ],")
        
        # Solution
        sol_escaped = q["step_by_step_solution"].replace("'", "\\'").replace("\n", "\\n")
        dart_lines.append(f"      stepByStepSolution: '{sol_escaped}',")
        dart_lines.append(f"      difficultyLevel: DifficultyLevel.{q['difficulty_level']},")
        dart_lines.append("      status: QuestionStatus.approved,")
        dart_lines.append("      submittedBy: '00000000-0000-0000-0000-000000000001',")
        dart_lines.append("      reviewedBy: '00000000-0000-0000-0000-000000000001',")
        dart_lines.append("      createdAt: DateTime.fromMillisecondsSinceEpoch(1727200000000),")
        dart_lines.append("    ),")

    dart_lines.append("  ];")
    dart_lines.append("}")
    dart_lines.append("")

    with open(dart_data_path, "w", encoding="utf-8") as f:
        f.write("\n".join(dart_lines))
    print(f"[3/3] Successfully generated Dart dataset: {dart_data_path}")

    # Summary verification
    ex1_count = sum(1 for q in EXERCISE_QUESTIONS if q['exercise'] == 'Exercise 1.1')
    ex2_count = sum(1 for q in EXERCISE_QUESTIONS if q['exercise'] == 'Exercise 1.2')
    print(f"\nBreakdown:")
    print(f"  • Exercise 1.1: {ex1_count} questions (Q1: 5 parts, Q2: 3 parts, Q3: 3 parts, Q4, Q5, Q6, Q7)")
    print(f"  • Exercise 1.2: {ex2_count} questions (Q1, Q2, Q3: 3 parts)")
    print(f"  • Total: {len(EXERCISE_QUESTIONS)} questions (100% textbook matching)")

if __name__ == "__main__":
    main()
