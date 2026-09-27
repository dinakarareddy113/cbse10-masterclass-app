-- Migration: 20260925050000_seed_ncert_math_ch4_exercises.sql
-- Seed complete NCERT Class 10 Mathematics Chapter 4 ("Quadratic Equations") Exercises
-- 29 verified questions across Exercise 4.1, 4.2, and 4.3 (Reprint 2026-27)

INSERT INTO public.questions (
  id,
  subject,
  chapter_id,
  question_text,
  options,
  step_by_step_solution,
  difficulty_level,
  status,
  submitted_by,
  reviewed_by,
  created_at
) VALUES
  ('10000000-0000-0000-0004-000000000001', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q1(i)] Check whether the following is a quadratic equation:
(x + 1)² = 2(x – 3)', '[{"id": "A", "text": "Yes, it is a quadratic equation (x\u00b2 + 7 = 0)", "is_correct": true}, {"id": "B", "text": "No, it is a linear equation", "is_correct": false}, {"id": "C", "text": "No, it is a cubic equation", "is_correct": false}, {"id": "D", "text": "None of the above", "is_correct": false}]'::jsonb, 'Step 1: Expand LHS: (x + 1)² = x² + 2x + 1.
Step 2: Expand RHS: 2(x – 3) = 2x – 6.
Step 3: Equating LHS and RHS:
  x² + 2x + 1 = 2x – 6
  => x² + 7 = 0.
Step 4: Since it is of the form ax² + bx + c = 0 with a = 1 ≠ 0, it is a quadratic equation.', 'easy', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000002', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q1(ii)] Check whether the following is a quadratic equation:
x² – 2x = (–2)(3 – x)', '[{"id": "A", "text": "Yes, it is a quadratic equation (x\u00b2 \u2013 4x + 6 = 0)", "is_correct": true}, {"id": "B", "text": "No, it is a linear equation", "is_correct": false}, {"id": "C", "text": "No, it is an identity", "is_correct": false}, {"id": "D", "text": "Yes, with degree 1", "is_correct": false}]'::jsonb, 'Step 1: LHS = x² – 2x.
Step 2: RHS = (–2)(3 – x) = –6 + 2x.
Step 3: Equating:
  x² – 2x = –6 + 2x
  => x² – 4x + 6 = 0.
Step 4: Degree is 2, hence it is a quadratic equation.', 'easy', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000003', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q1(iii)] Check whether the following is a quadratic equation:
(x – 2)(x + 1) = (x – 1)(x + 3)', '[{"id": "A", "text": "No, it is a linear equation (3x \u2013 1 = 0)", "is_correct": true}, {"id": "B", "text": "Yes, it is a quadratic equation", "is_correct": false}, {"id": "C", "text": "Yes, with roots 2 and \u20131", "is_correct": false}, {"id": "D", "text": "It is a cubic equation", "is_correct": false}]'::jsonb, 'Step 1: LHS = (x – 2)(x + 1) = x² – x – 2.
Step 2: RHS = (x – 1)(x + 3) = x² + 2x – 3.
Step 3: Equating:
  x² – x – 2 = x² + 2x – 3
  => 3x – 1 = 0.
Step 4: The x² term cancels out completely. Degree is 1, so it is NOT a quadratic equation.', 'easy', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000004', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q1(iv)] Check whether the following is a quadratic equation:
(x – 3)(2x + 1) = x(x + 5)', '[{"id": "A", "text": "Yes, it is a quadratic equation (x\u00b2 \u2013 10x \u2013 3 = 0)", "is_correct": true}, {"id": "B", "text": "No, it is a linear equation", "is_correct": false}, {"id": "C", "text": "No, it has no real terms", "is_correct": false}, {"id": "D", "text": "None of the above", "is_correct": false}]'::jsonb, 'Step 1: LHS = (x – 3)(2x + 1) = 2x² + x – 6x – 3 = 2x² – 5x – 3.
Step 2: RHS = x(x + 5) = x² + 5x.
Step 3: 2x² – 5x – 3 = x² + 5x => x² – 10x – 3 = 0.
Step 4: It is of the form ax² + bx + c = 0 (a = 1 ≠ 0), so it is a quadratic equation.', 'easy', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000005', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q1(v)] Check whether the following is a quadratic equation:
(2x – 1)(x – 3) = (x + 5)(x – 1)', '[{"id": "A", "text": "Yes, it is a quadratic equation (x\u00b2 \u2013 11x + 8 = 0)", "is_correct": true}, {"id": "B", "text": "No, it is linear (11x \u2013 8 = 0)", "is_correct": false}, {"id": "C", "text": "No, it has degree 3", "is_correct": false}, {"id": "D", "text": "Cannot be determined", "is_correct": false}]'::jsonb, 'Step 1: LHS = 2x² – 6x – x + 3 = 2x² – 7x + 3.
Step 2: RHS = x² – x + 5x – 5 = x² + 4x – 5.
Step 3: 2x² – 7x + 3 = x² + 4x – 5 => x² – 11x + 8 = 0.
Step 4: Degree is 2. Hence, it is a quadratic equation.', 'easy', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000006', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q1(vi)] Check whether the following is a quadratic equation:
x² + 3x + 1 = (x – 2)²', '[{"id": "A", "text": "No, it simplifies to a linear equation (7x \u2013 3 = 0)", "is_correct": true}, {"id": "B", "text": "Yes, it is a quadratic equation", "is_correct": false}, {"id": "C", "text": "Yes, degree is 2", "is_correct": false}, {"id": "D", "text": "It has infinite roots", "is_correct": false}]'::jsonb, 'Step 1: LHS = x² + 3x + 1.
Step 2: RHS = (x – 2)² = x² – 4x + 4.
Step 3: x² + 3x + 1 = x² – 4x + 4 => 7x – 3 = 0.
Step 4: Since x² cancels out, degree is 1. It is not a quadratic equation.', 'easy', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000007', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q1(vii)] Check whether the following is a quadratic equation:
(x + 2)³ = 2x(x² – 1)', '[{"id": "A", "text": "No, it is a cubic equation (x\u00b3 \u2013 6x\u00b2 \u2013 14x \u2013 8 = 0)", "is_correct": true}, {"id": "B", "text": "Yes, it is a quadratic equation", "is_correct": false}, {"id": "C", "text": "Yes, degree is 2", "is_correct": false}, {"id": "D", "text": "It is linear", "is_correct": false}]'::jsonb, 'Step 1: LHS = (x + 2)³ = x³ + 6x² + 12x + 8.
Step 2: RHS = 2x(x² – 1) = 2x³ – 2x.
Step 3: x³ + 6x² + 12x + 8 = 2x³ – 2x => x³ – 6x² – 14x – 8 = 0.
Step 4: Highest power is 3. Hence, it is cubic, NOT quadratic.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000008', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q1(viii)] Check whether the following is a quadratic equation:
x³ – 4x² – x + 1 = (x – 2)³', '[{"id": "A", "text": "Yes, it is a quadratic equation (2x\u00b2 \u2013 13x + 9 = 0)", "is_correct": true}, {"id": "B", "text": "No, it is a cubic equation", "is_correct": false}, {"id": "C", "text": "No, it is linear", "is_correct": false}, {"id": "D", "text": "None of the above", "is_correct": false}]'::jsonb, 'Step 1: LHS = x³ – 4x² – x + 1.
Step 2: RHS = (x – 2)³ = x³ – 6x² + 12x – 8.
Step 3: x³ – 4x² – x + 1 = x³ – 6x² + 12x – 8 => 2x² – 13x + 9 = 0.
Step 4: The x³ terms cancel out leaving degree 2. It is a quadratic equation.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000009', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q2(i)] Represent the situation as a quadratic equation:
The area of a rectangular plot is 528 m². The length of the plot (in metres) is one more than twice its breadth. We need to find the length and breadth of the plot.', '[{"id": "A", "text": "2x\u00b2 + x \u2013 528 = 0, where x is breadth in metres", "is_correct": true}, {"id": "B", "text": "x\u00b2 + 2x \u2013 528 = 0", "is_correct": false}, {"id": "C", "text": "2x\u00b2 \u2013 x + 528 = 0", "is_correct": false}, {"id": "D", "text": "2x\u00b2 + 2x \u2013 528 = 0", "is_correct": false}]'::jsonb, 'Step 1: Let the breadth of the rectangular plot be x metres.
Step 2: Length is one more than twice its breadth => Length = (2x + 1) metres.
Step 3: Area = Length × Breadth = x(2x + 1) = 2x² + x.
Step 4: Given area = 528 m² => 2x² + x = 528 => 2x² + x – 528 = 0.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000010', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q2(ii)] Represent the situation as a quadratic equation:
The product of two consecutive positive integers is 306. We need to find the integers.', '[{"id": "A", "text": "x\u00b2 + x \u2013 306 = 0, where x is the smaller integer", "is_correct": true}, {"id": "B", "text": "x\u00b2 + 2x \u2013 306 = 0", "is_correct": false}, {"id": "C", "text": "x\u00b2 \u2013 x \u2013 306 = 0", "is_correct": false}, {"id": "D", "text": "2x\u00b2 + x \u2013 306 = 0", "is_correct": false}]'::jsonb, 'Step 1: Let two consecutive positive integers be x and (x + 1).
Step 2: Their product = x(x + 1) = x² + x.
Step 3: Given product = 306 => x² + x = 306 => x² + x – 306 = 0.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000011', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q2(iii)] Represent the situation as a quadratic equation:
Rohan’s mother is 26 years older than him. The product of their ages (in years) 3 years from now will be 360. We would like to find Rohan’s present age.', '[{"id": "A", "text": "x\u00b2 + 32x \u2013 273 = 0, where x is Rohan''s present age", "is_correct": true}, {"id": "B", "text": "x\u00b2 + 26x \u2013 360 = 0", "is_correct": false}, {"id": "C", "text": "x\u00b2 + 29x \u2013 273 = 0", "is_correct": false}, {"id": "D", "text": "x\u00b2 + 32x + 273 = 0", "is_correct": false}]'::jsonb, 'Step 1: Let Rohan''s present age be x years.
Step 2: Mother''s present age = (x + 26) years.
Step 3: After 3 years: Rohan''s age = (x + 3); Mother''s age = (x + 26 + 3) = (x + 29).
Step 4: Product = (x + 3)(x + 29) = x² + 32x + 87.
Step 5: Given product = 360 => x² + 32x + 87 = 360 => x² + 32x – 273 = 0.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000012', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.1 - Q2(iv)] Represent the situation as a quadratic equation:
A train travels a distance of 480 km at a uniform speed. If the speed had been 8 km/h less, then it would have taken 3 hours more to cover the same distance. We need to find the speed of the train.', '[{"id": "A", "text": "x\u00b2 \u2013 8x \u2013 1280 = 0, where x is speed in km/h", "is_correct": true}, {"id": "B", "text": "x\u00b2 + 8x \u2013 1280 = 0", "is_correct": false}, {"id": "C", "text": "x\u00b2 \u2013 8x \u2013 480 = 0", "is_correct": false}, {"id": "D", "text": "3x\u00b2 \u2013 8x \u2013 1280 = 0", "is_correct": false}]'::jsonb, 'Step 1: Let speed of train be x km/h. Time taken to travel 480 km = 480/x hours.
Step 2: When speed is reduced by 8 km/h, speed = (x – 8) km/h. Time taken = 480/(x – 8) hours.
Step 3: Difference in time is 3 hours:
  480/(x – 8) – 480/x = 3
Step 4: 480 [ (x – (x – 8)) / (x(x – 8)) ] = 3
  => 480 × 8 / (x² – 8x) = 3
  => 3(x² – 8x) = 3840
  => x² – 8x = 1280
  => x² – 8x – 1280 = 0.', 'hard', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000013', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q1(i)] Find the roots of the quadratic equation by factorisation:
x² – 3x – 10 = 0', '[{"id": "A", "text": "x = 5 and x = \u20132", "is_correct": true}, {"id": "B", "text": "x = \u20135 and x = 2", "is_correct": false}, {"id": "C", "text": "x = 10 and x = \u20131", "is_correct": false}, {"id": "D", "text": "x = 3 and x = \u201310", "is_correct": false}]'::jsonb, 'Step 1: Split middle term: –3x = –5x + 2x and (–5)(2) = –10.
Step 2: x² – 5x + 2x – 10 = 0
  => x(x – 5) + 2(x – 5) = 0
  => (x – 5)(x + 2) = 0.
Step 3: x – 5 = 0 => x = 5; or x + 2 = 0 => x = –2.
Roots are 5 and –2.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000014', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q1(ii)] Find the roots of the quadratic equation by factorisation:
2x² + x – 6 = 0', '[{"id": "A", "text": "x = 3/2 and x = \u20132", "is_correct": true}, {"id": "B", "text": "x = \u20133/2 and x = 2", "is_correct": false}, {"id": "C", "text": "x = 2/3 and x = \u20133", "is_correct": false}, {"id": "D", "text": "x = 6 and x = \u20131", "is_correct": false}]'::jsonb, 'Step 1: Product = 2 × (–6) = –12. Split +x as +4x – 3x.
Step 2: 2x² + 4x – 3x – 6 = 0
  => 2x(x + 2) – 3(x + 2) = 0
  => (2x – 3)(x + 2) = 0.
Step 3: 2x – 3 = 0 => x = 3/2; x + 2 = 0 => x = –2.
Roots are 3/2 and –2.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000015', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q1(iii)] Find the roots of the quadratic equation by factorisation:
√2 x² + 7x + 5√2 = 0', '[{"id": "A", "text": "x = \u20135/\u221a2 and x = \u2013\u221a2", "is_correct": true}, {"id": "B", "text": "x = 5/\u221a2 and x = \u221a2", "is_correct": false}, {"id": "C", "text": "x = \u20135 and x = \u20132", "is_correct": false}, {"id": "D", "text": "x = \u2013\u221a2 and x = 5", "is_correct": false}]'::jsonb, 'Step 1: Product = √2 × 5√2 = 5 × 2 = 10. Split 7x as 2x + 5x.
Step 2: √2 x² + 2x + 5x + 5√2 = 0
  => √2 x(x + √2) + 5(x + √2) = 0
  => (√2 x + 5)(x + √2) = 0.
Step 3: Either √2 x + 5 = 0 => x = –5/√2, or x + √2 = 0 => x = –√2.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000016', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q1(iv)] Find the roots of the quadratic equation by factorisation:
2x² – x + 1/8 = 0', '[{"id": "A", "text": "x = 1/4 and x = 1/4", "is_correct": true}, {"id": "B", "text": "x = 1/2 and x = 1/4", "is_correct": false}, {"id": "C", "text": "x = \u20131/4 and x = \u20131/4", "is_correct": false}, {"id": "D", "text": "x = 1/8 and x = 1", "is_correct": false}]'::jsonb, 'Step 1: Multiply entire equation by 8:
  16x² – 8x + 1 = 0.
Step 2: Recognize identity: (4x – 1)² = 16x² – 8x + 1 = 0.
Step 3: (4x – 1)(4x – 1) = 0 => x = 1/4, 1/4.
Both equal roots are 1/4.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000017', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q1(v)] Find the roots of the quadratic equation by factorisation:
100x² – 20x + 1 = 0', '[{"id": "A", "text": "x = 1/10 and x = 1/10", "is_correct": true}, {"id": "B", "text": "x = \u20131/10 and x = \u20131/10", "is_correct": false}, {"id": "C", "text": "x = 1/20 and x = 1/5", "is_correct": false}, {"id": "D", "text": "x = 1/100 and x = 1", "is_correct": false}]'::jsonb, 'Step 1: Notice (10x – 1)² = 100x² – 20x + 1 = 0.
Step 2: (10x – 1)(10x – 1) = 0.
Step 3: 10x – 1 = 0 => x = 1/10.
Both equal roots are 1/10.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000018', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q2(i)] Solve the problem given in Example 1(i):
John and Jivanti together have 45 marbles. Both lost 5 marbles each, and the product of marbles they now have is 124. Find how many marbles they had to start with.', '[{"id": "A", "text": "36 and 9 marbles", "is_correct": true}, {"id": "B", "text": "30 and 15 marbles", "is_correct": false}, {"id": "C", "text": "40 and 5 marbles", "is_correct": false}, {"id": "D", "text": "28 and 17 marbles", "is_correct": false}]'::jsonb, 'Step 1: The mathematical formulation from Example 1 is x² – 45x + 324 = 0.
Step 2: Factorise: (x – 36)(x – 9) = 0.
Step 3: x = 36 or x = 9.
Hence, John and Jivanti had 36 and 9 marbles (or 9 and 36).', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000019', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q2(ii)] Solve the problem given in Example 1(ii):
A cottage industry produces a certain number of toys in a day. Cost of production of each toy was (55 – x). Total cost of production on that day was ₹ 750. Find the number of toys produced.', '[{"id": "A", "text": "30 or 25 toys", "is_correct": true}, {"id": "B", "text": "35 or 20 toys", "is_correct": false}, {"id": "C", "text": "40 or 15 toys", "is_correct": false}, {"id": "D", "text": "50 or 5 toys", "is_correct": false}]'::jsonb, 'Step 1: The equation from Example 1 is x² – 55x + 750 = 0.
Step 2: Factorise: (x – 30)(x – 25) = 0.
Step 3: x = 30 or x = 25.
The number of toys produced that day was either 30 or 25.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000020', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q3] Find two numbers whose sum is 27 and product is 182.', '[{"id": "A", "text": "13 and 14", "is_correct": true}, {"id": "B", "text": "12 and 15", "is_correct": false}, {"id": "C", "text": "11 and 16", "is_correct": false}, {"id": "D", "text": "10 and 17", "is_correct": false}]'::jsonb, 'Step 1: Let the two numbers be x and (27 – x).
Step 2: Product: x(27 – x) = 182 => 27x – x² = 182 => x² – 27x + 182 = 0.
Step 3: Factorise: 182 = 13 × 14, and –13 – 14 = –27.
Step 4: (x – 13)(x – 14) = 0 => x = 13 or x = 14.
Therefore, the required numbers are 13 and 14.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000021', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q4] Find two consecutive positive integers, sum of whose squares is 365.', '[{"id": "A", "text": "13 and 14", "is_correct": true}, {"id": "B", "text": "11 and 12", "is_correct": false}, {"id": "C", "text": "12 and 13", "is_correct": false}, {"id": "D", "text": "14 and 15", "is_correct": false}]'::jsonb, 'Step 1: Let the two consecutive positive integers be x and (x + 1).
Step 2: x² + (x + 1)² = 365 => x² + x² + 2x + 1 = 365 => 2x² + 2x – 364 = 0.
Step 3: Dividing by 2: x² + x – 182 = 0.
Step 4: (x + 14)(x – 13) = 0 => x = 13 (reject –14 since integers are positive).
Step 5: x + 1 = 14. The two integers are 13 and 14.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000022', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q5] The altitude of a right triangle is 7 cm less than its base. If the hypotenuse is 13 cm, find the other two sides.', '[{"id": "A", "text": "Base = 12 cm, Altitude = 5 cm", "is_correct": true}, {"id": "B", "text": "Base = 10 cm, Altitude = 3 cm", "is_correct": false}, {"id": "C", "text": "Base = 15 cm, Altitude = 8 cm", "is_correct": false}, {"id": "D", "text": "Base = 9 cm, Altitude = 2 cm", "is_correct": false}]'::jsonb, 'Step 1: Let base = x cm. Then altitude = (x – 7) cm. Hypotenuse = 13 cm.
Step 2: By Pythagoras theorem: x² + (x – 7)² = 13² = 169.
Step 3: x² + x² – 14x + 49 = 169 => 2x² – 14x – 120 = 0 => x² – 7x – 60 = 0.
Step 4: Factorise: (x – 12)(x + 5) = 0 => x = 12 (length cannot be negative).
Step 5: Base = 12 cm, Altitude = 12 – 7 = 5 cm.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000023', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.2 - Q6] A cottage industry produces a certain number of pottery articles in a day. The cost of production of each article was ₹ 3 more than twice the number of articles produced. If total cost was ₹ 90, find the number of articles produced and cost of each article.', '[{"id": "A", "text": "Number of articles = 6, Cost of each = \u20b9 15", "is_correct": true}, {"id": "B", "text": "Number of articles = 5, Cost of each = \u20b9 18", "is_correct": false}, {"id": "C", "text": "Number of articles = 10, Cost of each = \u20b9 9", "is_correct": false}, {"id": "D", "text": "Number of articles = 8, Cost of each = \u20b9 19", "is_correct": false}]'::jsonb, 'Step 1: Let number of articles = x. Cost of each article = ₹ (2x + 3).
Step 2: Total cost = x(2x + 3) = 90 => 2x² + 3x – 90 = 0.
Step 3: Factorise: 2x² – 12x + 15x – 90 = 0 => 2x(x – 6) + 15(x – 6) = 0 => (2x + 15)(x – 6) = 0.
Step 4: x = 6 (since articles cannot be negative or fractional).
Step 5: Cost of each article = 2(6) + 3 = ₹ 15.', 'hard', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000024', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.3 - Q1(i)] Find the nature of the roots of the quadratic equation. If real roots exist, find them:
2x² – 3x + 5 = 0', '[{"id": "A", "text": "No real roots (Discriminant D = \u201331 < 0)", "is_correct": true}, {"id": "B", "text": "Two distinct real roots", "is_correct": false}, {"id": "C", "text": "Two equal real roots", "is_correct": false}, {"id": "D", "text": "Roots are 3/4 and 5/2", "is_correct": false}]'::jsonb, 'Step 1: Comparing with ax² + bx + c = 0: a = 2, b = –3, c = 5.
Step 2: Discriminant D = b² – 4ac = (–3)² – 4(2)(5) = 9 – 40 = –31.
Step 3: Since D < 0, the quadratic equation has NO real roots.', 'easy', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000025', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.3 - Q1(ii)] Find the nature of the roots of the quadratic equation. If real roots exist, find them:
3x² – 4√3 x + 4 = 0', '[{"id": "A", "text": "Two equal real roots: 2/\u221a3, 2/\u221a3", "is_correct": true}, {"id": "B", "text": "No real roots (D < 0)", "is_correct": false}, {"id": "C", "text": "Two distinct real roots: \u221a3 and \u2013\u221a3", "is_correct": false}, {"id": "D", "text": "Two distinct real roots: 4 and 3", "is_correct": false}]'::jsonb, 'Step 1: Here a = 3, b = –4√3, c = 4.
Step 2: Discriminant D = b² – 4ac = (–4√3)² – 4(3)(4) = 48 – 48 = 0.
Step 3: Since D = 0, the equation has two equal real roots.
Step 4: Roots: x = –b / (2a) = –(–4√3) / (2 × 3) = 4√3 / 6 = 2√3 / 3 = 2/√3.
Hence, roots are 2/√3, 2/√3.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000026', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.3 - Q1(iii)] Find the nature of the roots of the quadratic equation. If real roots exist, find them:
2x² – 6x + 3 = 0', '[{"id": "A", "text": "Two distinct real roots: (3 \u00b1 \u221a3) / 2", "is_correct": true}, {"id": "B", "text": "Two equal real roots: 3/2, 3/2", "is_correct": false}, {"id": "C", "text": "No real roots (D < 0)", "is_correct": false}, {"id": "D", "text": "Two integer roots: 3 and 1", "is_correct": false}]'::jsonb, 'Step 1: a = 2, b = –6, c = 3.
Step 2: Discriminant D = b² – 4ac = (–6)² – 4(2)(3) = 36 – 24 = 12 > 0.
Step 3: Since D > 0, there are two distinct real roots.
Step 4: By quadratic formula:
  x = [–b ± √D] / 2a = [–(–6) ± √12] / (2 × 2) = (6 ± 2√3) / 4 = (3 ± √3) / 2.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000027', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.3 - Q2(i)] Find the value(s) of k so that the quadratic equation has two equal roots:
2x² + kx + 3 = 0', '[{"id": "A", "text": "k = \u00b1 2\u221a6", "is_correct": true}, {"id": "B", "text": "k = \u00b1 6", "is_correct": false}, {"id": "C", "text": "k = \u00b1 24", "is_correct": false}, {"id": "D", "text": "k = 12", "is_correct": false}]'::jsonb, 'Step 1: a = 2, b = k, c = 3.
Step 2: For two equal roots, Discriminant D = b² – 4ac = 0.
Step 3: k² – 4(2)(3) = 0 => k² – 24 = 0 => k² = 24.
Step 4: k = ± √24 = ± √(4 × 6) = ± 2√6.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000028', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.3 - Q2(ii)] Find the value(s) of k so that the quadratic equation has two equal roots:
kx(x – 2) + 6 = 0', '[{"id": "A", "text": "k = 6", "is_correct": true}, {"id": "B", "text": "k = 0 or 6", "is_correct": false}, {"id": "C", "text": "k = \u20136", "is_correct": false}, {"id": "D", "text": "k = 4", "is_correct": false}]'::jsonb, 'Step 1: Expand equation: kx² – 2kx + 6 = 0. Here a = k, b = –2k, c = 6.
Step 2: For equal roots, D = b² – 4ac = 0.
Step 3: (–2k)² – 4(k)(6) = 0 => 4k² – 24k = 0 => 4k(k – 6) = 0.
Step 4: Either k = 0 or k = 6.
Step 5: If k = 0, equation becomes 6 = 0 (not quadratic). Therefore, k = 6.', 'medium', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00'),
  ('10000000-0000-0000-0004-000000000029', 'math', 'math_ch_04_quadratic_equations', '[Exercise 4.3 - Q3 to Q5] Check feasibility of geometric situations:
(i) Rectangular mango grove length = 2b, area = 800 m²;
(ii) Sum of friend ages = 20, product 4 yrs ago was 48;
(iii) Rectangular park perimeter = 80 m, area = 400 m².
Which situations are mathematically possible?', '[{"id": "A", "text": "(i) and (iii) are possible; (ii) is not possible (D < 0)", "is_correct": true}, {"id": "B", "text": "All three situations are possible", "is_correct": false}, {"id": "C", "text": "Only (i) is possible", "is_correct": false}, {"id": "D", "text": "None of the situations are possible", "is_correct": false}]'::jsonb, 'Step 1: Mango grove: 2x² = 800 => x² = 400 => x = 20 m (breadth), length = 40 m. Real roots exist. Possible!
Step 2: Age problem: (x – 4)(16 – x) = 48 => x² – 20x + 112 = 0. D = 400 – 448 = –48 < 0. No real roots. Not possible!
Step 3: Park: l(40 – l) = 400 => l² – 40l + 400 = 0 => (l – 20)² = 0 => l = 20 m, b = 20 m. Real equal roots. Possible (square park of side 20 m)!
Hence, (i) and (iii) are possible, (ii) is not possible.', 'hard', 'approved', '00000000-0000-0000-0000-000000000001', '00000000-0000-0000-0000-000000000001', '2026-09-25 05:00:00+00')
ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;
