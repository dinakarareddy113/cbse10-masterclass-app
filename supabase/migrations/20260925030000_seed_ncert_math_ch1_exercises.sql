-- ==============================================================================
-- Migration: 20260925030000_seed_ncert_math_ch1_exercises.sql
-- Project: CBSE Class 10 Masterclass
-- Description: 100% Textbook-Accurate Ingestion of Real Numbers Exercise 1.1 & 1.2
-- ==============================================================================

INSERT INTO public.questions (
    id, subject, chapter_id, question_text, options, step_by_step_solution,
    difficulty_level, status, submitted_by, reviewed_by, created_at
) VALUES
(
    '10000000-0000-0000-0001-000000000001',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q1(i)] Express the number as a product of its prime factors:
(i) 140',
    '[{"id": "A", "text": "2² × 5 × 7", "is_correct": true}, {"id": "B", "text": "2 × 5² × 7", "is_correct": false}, {"id": "C", "text": "2³ × 5 × 7", "is_correct": false}, {"id": "D", "text": "4 × 35", "is_correct": false}]'::jsonb,
    'Step 1: Using the prime factorisation method (factor tree):
  140 ÷ 2 = 70
  70 ÷ 2 = 35
  35 ÷ 5 = 7
  7 ÷ 7 = 1
Step 2: Therefore, 140 = 2 × 2 × 5 × 7 = 2² × 5 × 7.',
    'easy',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000002',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q1(ii)] Express the number as a product of its prime factors:
(ii) 156',
    '[{"id": "A", "text": "2² × 3 × 13", "is_correct": true}, {"id": "B", "text": "2 × 3² × 13", "is_correct": false}, {"id": "C", "text": "4 × 39", "is_correct": false}, {"id": "D", "text": "2 × 78", "is_correct": false}]'::jsonb,
    'Step 1: Divide 156 by prime factors:
  156 ÷ 2 = 78
  78 ÷ 2 = 39
  39 ÷ 3 = 13
  13 ÷ 13 = 1
Step 2: Therefore, 156 = 2 × 2 × 3 × 13 = 2² × 3 × 13.',
    'easy',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000003',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q1(iii)] Express the number as a product of its prime factors:
(iii) 3825',
    '[{"id": "A", "text": "3² × 5² × 17", "is_correct": true}, {"id": "B", "text": "3 × 5² × 17", "is_correct": false}, {"id": "C", "text": "3² × 5 × 17²", "is_correct": false}, {"id": "D", "text": "9 × 25 × 17", "is_correct": false}]'::jsonb,
    'Step 1: Divide 3825 by successive prime numbers:
  3825 ÷ 3 = 1275
  1275 ÷ 3 = 425
  425 ÷ 5 = 85
  85 ÷ 5 = 17
  17 ÷ 17 = 1
Step 2: Therefore, 3825 = 3 × 3 × 5 × 5 × 17 = 3² × 5² × 17.',
    'easy',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000004',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q1(iv)] Express the number as a product of its prime factors:
(iv) 5005',
    '[{"id": "A", "text": "5 × 7 × 11 × 13", "is_correct": true}, {"id": "B", "text": "5² × 7 × 13", "is_correct": false}, {"id": "C", "text": "5 × 11² × 13", "is_correct": false}, {"id": "D", "text": "35 × 143", "is_correct": false}]'::jsonb,
    'Step 1: Divide 5005 by successive prime numbers:
  5005 ÷ 5 = 1001
  1001 ÷ 7 = 143
  143 ÷ 11 = 13
  13 ÷ 13 = 1
Step 2: Therefore, 5005 = 5 × 7 × 11 × 13.',
    'easy',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000005',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q1(v)] Express the number as a product of its prime factors:
(v) 7429',
    '[{"id": "A", "text": "17 × 19 × 23", "is_correct": true}, {"id": "B", "text": "13 × 19 × 29", "is_correct": false}, {"id": "C", "text": "17² × 23", "is_correct": false}, {"id": "D", "text": "19 × 23 × 29", "is_correct": false}]'::jsonb,
    'Step 1: Testing initial prime factors shows 2, 3, 5, 7, 11, 13 do not divide 7429.
Step 2: 7429 ÷ 17 = 437
Step 3: 437 ÷ 19 = 23
Step 4: 23 ÷ 23 = 1
Step 5: Therefore, 7429 = 17 × 19 × 23.',
    'medium',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000006',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q2(i)] Find the LCM and HCF of 26 and 91 and verify that LCM × HCF = product of the two numbers.',
    '[{"id": "A", "text": "HCF = 13, LCM = 182", "is_correct": true}, {"id": "B", "text": "HCF = 26, LCM = 91", "is_correct": false}, {"id": "C", "text": "HCF = 1, LCM = 2366", "is_correct": false}, {"id": "D", "text": "HCF = 7, LCM = 364", "is_correct": false}]'::jsonb,
    'Step 1: Prime factorisation:
  26 = 2 × 13
  91 = 7 × 13
Step 2: HCF(26, 91) = 13 (common factor with smallest power).
Step 3: LCM(26, 91) = 2 × 7 × 13 = 182.
Step 4: Verification:
  LCM × HCF = 182 × 13 = 2366
  Product of numbers = 26 × 91 = 2366
  Hence, LCM × HCF = Product of the two numbers verified.',
    'easy',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000007',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q2(ii)] Find the LCM and HCF of 510 and 92 and verify that LCM × HCF = product of the two numbers.',
    '[{"id": "A", "text": "HCF = 2, LCM = 23460", "is_correct": true}, {"id": "B", "text": "HCF = 4, LCM = 11730", "is_correct": false}, {"id": "C", "text": "HCF = 2, LCM = 46920", "is_correct": false}, {"id": "D", "text": "HCF = 6, LCM = 7820", "is_correct": false}]'::jsonb,
    'Step 1: Prime factorisation:
  510 = 2 × 3 × 5 × 17
  92 = 2² × 23
Step 2: HCF(510, 92) = 2¹ = 2.
Step 3: LCM(510, 92) = 2² × 3 × 5 × 17 × 23 = 4 × 15 × 391 = 23460.
Step 4: Verification:
  LCM × HCF = 23460 × 2 = 46920
  Product of numbers = 510 × 92 = 46920
  Hence, LCM × HCF = Product of the two numbers verified.',
    'medium',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000008',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q2(iii)] Find the LCM and HCF of 336 and 54 and verify that LCM × HCF = product of the two numbers.',
    '[{"id": "A", "text": "HCF = 6, LCM = 3024", "is_correct": true}, {"id": "B", "text": "HCF = 12, LCM = 1512", "is_correct": false}, {"id": "C", "text": "HCF = 3, LCM = 6048", "is_correct": false}, {"id": "D", "text": "HCF = 18, LCM = 1008", "is_correct": false}]'::jsonb,
    'Step 1: Prime factorisation:
  336 = 2⁴ × 3 × 7
  54 = 2 × 3³
Step 2: HCF(336, 54) = 2¹ × 3¹ = 6.
Step 3: LCM(336, 54) = 2⁴ × 3³ × 7 = 16 × 27 × 7 = 3024.
Step 4: Verification:
  LCM × HCF = 3024 × 6 = 18144
  Product of numbers = 336 × 54 = 18144
  Hence, LCM × HCF = Product of the two numbers verified.',
    'medium',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000009',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q3(i)] Find the LCM and HCF of 12, 15 and 21 by applying the prime factorisation method.',
    '[{"id": "A", "text": "HCF = 3, LCM = 420", "is_correct": true}, {"id": "B", "text": "HCF = 6, LCM = 210", "is_correct": false}, {"id": "C", "text": "HCF = 1, LCM = 1260", "is_correct": false}, {"id": "D", "text": "HCF = 3, LCM = 840", "is_correct": false}]'::jsonb,
    'Step 1: Prime factorisation:
  12 = 2² × 3
  15 = 3 × 5
  21 = 3 × 7
Step 2: HCF = 3¹ = 3 (common factor in all three).
Step 3: LCM = 2² × 3 × 5 × 7 = 4 × 3 × 5 × 7 = 420.',
    'easy',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000010',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q3(ii)] Find the LCM and HCF of 17, 23 and 29 by applying the prime factorisation method.',
    '[{"id": "A", "text": "HCF = 1, LCM = 11339", "is_correct": true}, {"id": "B", "text": "HCF = 1, LCM = 22678", "is_correct": false}, {"id": "C", "text": "HCF = 17, LCM = 667", "is_correct": false}, {"id": "D", "text": "HCF = 29, LCM = 391", "is_correct": false}]'::jsonb,
    'Step 1: Notice that 17, 23, and 29 are all prime numbers:
  17 = 1 × 17
  23 = 1 × 23
  29 = 1 × 29
Step 2: Since there is no common prime factor, HCF = 1.
Step 3: LCM = 17 × 23 × 29 = 391 × 29 = 11339.',
    'easy',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000011',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q3(iii)] Find the LCM and HCF of 8, 9 and 25 by applying the prime factorisation method.',
    '[{"id": "A", "text": "HCF = 1, LCM = 1800", "is_correct": true}, {"id": "B", "text": "HCF = 2, LCM = 900", "is_correct": false}, {"id": "C", "text": "HCF = 3, LCM = 3600", "is_correct": false}, {"id": "D", "text": "HCF = 1, LCM = 72", "is_correct": false}]'::jsonb,
    'Step 1: Prime factorisation:
  8 = 2³
  9 = 3²
  25 = 5²
Step 2: No common prime factor exists across all three numbers, so HCF = 1.
Step 3: LCM = 2³ × 3² × 5² = 8 × 9 × 25 = 72 × 25 = 1800.',
    'easy',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000012',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q4] Given that HCF (306, 657) = 9, find LCM (306, 657).',
    '[{"id": "A", "text": "22338", "is_correct": true}, {"id": "B", "text": "22383", "is_correct": false}, {"id": "C", "text": "201042", "is_correct": false}, {"id": "D", "text": "22438", "is_correct": false}]'::jsonb,
    'Step 1: Formula connecting HCF and LCM of two positive integers a and b:
  HCF(a, b) × LCM(a, b) = a × b
Step 2: Here a = 306, b = 657, and HCF = 9.
  9 × LCM(306, 657) = 306 × 657
Step 3: LCM(306, 657) = (306 × 657) / 9
  306 ÷ 9 = 34
  LCM = 34 × 657 = 22338.',
    'medium',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000013',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q5] Check whether 6ⁿ can end with the digit 0 for any natural number n.',
    '[{"id": "A", "text": "No, because the prime factorisation of 6ⁿ contains only 2 and 3, not 5", "is_correct": true}, {"id": "B", "text": "Yes, for any even value of n", "is_correct": false}, {"id": "C", "text": "Yes, when n is a multiple of 5", "is_correct": false}, {"id": "D", "text": "Yes, because 6 ends with an even digit", "is_correct": false}]'::jsonb,
    'Step 1: If any number ends with the digit 0, it must be divisible by 10 = 2 × 5.
  That is, its prime factorisation must contain both 2 and 5 as prime factors.
Step 2: Prime factorisation of 6ⁿ = (2 × 3)ⁿ = 2ⁿ × 3ⁿ.
Step 3: The only primes in the factorisation of 6ⁿ are 2 and 3.
Step 4: By the uniqueness of the Fundamental Theorem of Arithmetic, there are no other primes in the factorisation of 6ⁿ.
Step 5: Since 5 is not a factor, 6ⁿ cannot be divisible by 5.
  Therefore, 6ⁿ cannot end with the digit 0 for any natural number n.',
    'medium',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000014',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q6] Explain why 7 × 11 × 13 + 13 and 7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 are composite numbers.',
    '[{"id": "A", "text": "Both expressions have factors other than 1 and themselves (13 and 5 can be factored out)", "is_correct": true}, {"id": "B", "text": "Because they are products of consecutive integers", "is_correct": false}, {"id": "C", "text": "Because both result in even numbers", "is_correct": false}, {"id": "D", "text": "Because their sum is divisible by 2", "is_correct": false}]'::jsonb,
    'Step 1: A composite number has factors other than 1 and the number itself.
Step 2: First expression:
  7 × 11 × 13 + 13 = 13 × (7 × 11 + 1)
  = 13 × (77 + 1) = 13 × 78 = 13 × 13 × 6 = 2 × 3 × 13².
  Since it has factors 2, 3, 13 besides 1 and itself, it is a composite number.
Step 3: Second expression:
  7 × 6 × 5 × 4 × 3 × 2 × 1 + 5 = 5 × (7 × 6 × 4 × 3 × 2 × 1 + 1)
  = 5 × (1008 + 1) = 5 × 1009.
  Since 1009 is a prime, the number has 5 and 1009 as factors besides 1 and itself.
  Hence, both are composite numbers.',
    'easy',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000015',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.1 - Q7] There is a circular path around a sports field. Sonia takes 18 minutes to drive one round of the field, while Ravi takes 12 minutes for the same. Suppose they both start at the same point and at the same time, and go in the same direction. After how many minutes will they meet again at the starting point?',
    '[{"id": "A", "text": "36 minutes", "is_correct": true}, {"id": "B", "text": "6 minutes", "is_correct": false}, {"id": "C", "text": "60 minutes", "is_correct": false}, {"id": "D", "text": "216 minutes", "is_correct": false}]'::jsonb,
    'Step 1: Sonia and Ravi start simultaneously and travel in the same direction.
Step 2: They will meet again at the starting point after a time period which is the Lowest Common Multiple (LCM) of the times taken by both:
  Required time = LCM(18, 12)
Step 3: Prime factorisation:
  18 = 2 × 3²
  12 = 2² × 3
Step 4: LCM(18, 12) = 2² × 3² = 4 × 9 = 36 minutes.
Step 5: Hence, they will meet again at the starting point after 36 minutes.',
    'medium',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000016',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.2 - Q1] Prove that √5 is irrational.',
    '[{"id": "A", "text": "Proof by contradiction: 5 divides both a and b, contradicting that gcd(a,b)=1", "is_correct": true}, {"id": "B", "text": "Proof by division: √5 cannot be written as a terminating fraction", "is_correct": false}, {"id": "C", "text": "Proof by geometry: diagonal of unit square is irrational", "is_correct": false}, {"id": "D", "text": "Proof by induction: √n is irrational for all primes n", "is_correct": false}]'::jsonb,
    'Step 1: Assume to the contrary that √5 is rational.
  Then there exist coprime integers a and b (b ≠ 0, gcd(a,b) = 1) such that:
  √5 = a / b => a = b√5
Step 2: Squaring both sides:
  a² = 5b²  ... (Equation 1)
  This means 5 divides a². By Theorem 1.2, if a prime p divides a², then p divides a.
  Therefore, 5 divides a.
Step 3: Let a = 5c for some integer c. Substitute a in Equation 1:
  (5c)² = 5b² => 25c² = 5b² => b² = 5c²
  This means 5 divides b², which implies 5 divides b.
Step 4: From Steps 2 and 3, both a and b share a common factor 5.
  This contradicts the fact that a and b are coprime (share no common factor other than 1).
Step 5: This contradiction arises from our incorrect assumption that √5 is rational.
  Hence, √5 is irrational.',
    'hard',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000017',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.2 - Q2] Prove that 3 + 2√5 is irrational.',
    '[{"id": "A", "text": "Proof by contradiction: √5 = (a - 3b)/(2b) equates an irrational to a rational", "is_correct": true}, {"id": "B", "text": "Proof by approximation: 3 + 2(2.236) is non-terminating", "is_correct": false}, {"id": "C", "text": "Proof by squaring: (3 + 2√5)² = 29 + 12√5 has no integer root", "is_correct": false}, {"id": "D", "text": "Proof by decimal expansion: remainder never repeats", "is_correct": false}]'::jsonb,
    'Step 1: Assume to the contrary that 3 + 2√5 is rational.
  Then there exist coprime integers a and b (b ≠ 0) such that:
  3 + 2√5 = a / b
Step 2: Rearranging the equation to isolate √5:
  2√5 = (a / b) - 3
  2√5 = (a - 3b) / b
  √5 = (a - 3b) / (2b)
Step 3: Since a and b are integers, (a - 3b) and 2b are also integers (2b ≠ 0).
  Therefore, (a - 3b) / (2b) is a rational number.
Step 4: This implies that √5 is rational. But this contradicts the known fact that √5 is irrational.
Step 5: This contradiction has arisen because of our incorrect assumption that 3 + 2√5 is rational.
  Hence, 3 + 2√5 is irrational.',
    'medium',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000018',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.2 - Q3(i)] Prove that the following is irrational:
(i) 1 / √2',
    '[{"id": "A", "text": "Proof: 1/√2 = a/b => √2 = b/a, equating irrational √2 to rational b/a", "is_correct": true}, {"id": "B", "text": "Proof: Rationalising denominator gives √2 / 2 which cannot be solved", "is_correct": false}, {"id": "C", "text": "Proof: 1 divided by any root is non-terminating", "is_correct": false}, {"id": "D", "text": "Proof: Reciprocal of an irrational number is always undefined", "is_correct": false}]'::jsonb,
    'Step 1: Let us assume to the contrary that 1/√2 is rational.
  Then there exist coprime integers a and b (where a ≠ 0, b ≠ 0) such that:
  1 / √2 = a / b
Step 2: Taking reciprocals on both sides:
  √2 = b / a
Step 3: Since b and a are integers and a ≠ 0, b / a is a rational number.
Step 4: This implies that √2 is a rational number.
  But this contradicts the established fact that √2 is irrational.
Step 5: Hence, our assumption was false. Therefore, 1/√2 is irrational.',
    'medium',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000019',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.2 - Q3(ii)] Prove that the following is irrational:
(ii) 7√5',
    '[{"id": "A", "text": "Proof: 7√5 = a/b => √5 = a/(7b), equating irrational √5 to rational a/(7b)", "is_correct": true}, {"id": "B", "text": "Proof: Product of any integer and root is an imaginary number", "is_correct": false}, {"id": "C", "text": "Proof: Multiplying by 7 preserves prime factorisation", "is_correct": false}, {"id": "D", "text": "Proof: 7² × 5 = 245 has no square root", "is_correct": false}]'::jsonb,
    'Step 1: Let us assume to the contrary that 7√5 is rational.
  Then there exist coprime integers a and b (b ≠ 0) such that:
  7√5 = a / b
Step 2: Rearranging for √5:
  √5 = a / (7b)
Step 3: Since 7, a, and b are integers and 7b ≠ 0, a / (7b) is a rational number.
Step 4: This implies that √5 is rational.
  However, this contradicts the fact that √5 is irrational.
Step 5: Hence, our assumption is false. Therefore, 7√5 is irrational.',
    'medium',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
),
(
    '10000000-0000-0000-0001-000000000020',
    'math',
    'math_ch_01_real_numbers',
    '[Exercise 1.2 - Q3(iii)] Prove that the following is irrational:
(iii) 6 + √2',
    '[{"id": "A", "text": "Proof: 6 + √2 = a/b => √2 = (a - 6b)/b, equating irrational √2 to rational", "is_correct": true}, {"id": "B", "text": "Proof: 6 is composite so adding √2 makes it transcendental", "is_correct": false}, {"id": "C", "text": "Proof: (6 + √2)² = 38 + 12√2 is non-repeating", "is_correct": false}, {"id": "D", "text": "Proof: Sum of rational and irrational is always undefined", "is_correct": false}]'::jsonb,
    'Step 1: Let us assume to the contrary that 6 + √2 is rational.
  Then there exist coprime integers a and b (b ≠ 0) such that:
  6 + √2 = a / b
Step 2: Rearranging to isolate √2:
  √2 = (a / b) - 6
  √2 = (a - 6b) / b
Step 3: Since a, b, and 6 are integers, (a - 6b) / b is a rational number.
Step 4: This implies that √2 is rational, which contradicts the theorem that √2 is irrational.
Step 5: Therefore, our assumption was incorrect. We conclude that 6 + √2 is irrational.',
    'medium',
    'approved',
    '00000000-0000-0000-0000-000000000001',
    '00000000-0000-0000-0000-000000000001',
    TIMEZONE('utc'::text, NOW())
)
ON CONFLICT (id) DO UPDATE SET
    question_text = EXCLUDED.question_text,
    options = EXCLUDED.options,
    step_by_step_solution = EXCLUDED.step_by_step_solution,
    status = EXCLUDED.status;
