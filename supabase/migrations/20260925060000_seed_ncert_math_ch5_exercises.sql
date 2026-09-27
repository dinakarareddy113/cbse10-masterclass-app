--
-- Migration: Seed NCERT Class 10 Mathematics Chapter 5 ("Arithmetic Progressions") Exercises
-- Total items: 35 covering Exercises 5.1, 5.2, and 5.3 (Reprint 2026-27)
--

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
) VALUES (
  '10000000-0000-0000-0005-000000000001',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q1(i)] The taxi fare after each km when the fare is ₹ 15 for the first km and ₹ 8 for each additional km. Does this situation make an arithmetic progression?',
  '[{"id": "A", "text": "Yes, it forms an AP because each term is obtained by adding a constant \u20b9 8 (series: 15, 23, 31, 39, ...)", "is_correct": true}, {"id": "B", "text": "No, taxi fares follow geometric compounding", "is_correct": false}, {"id": "C", "text": "No, the initial fare is higher than the per-km rate", "is_correct": false}, {"id": "D", "text": "Yes, but only for distances less than 10 km", "is_correct": false}]'::jsonb,
  'Step 1: Fare for 1 km = ₹ 15.
Step 2: Fare for 2 km = 15 + 8 = ₹ 23; Fare for 3 km = 23 + 8 = ₹ 31; Fare for 4 km = 31 + 8 = ₹ 39.
Step 3: The series of terms is 15, 23, 31, 39, ... Here, the difference between consecutive terms is constant (d = 8).
Hence, it forms an Arithmetic Progression (AP).',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000002',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q1(ii)] The amount of air present in a cylinder when a vacuum pump removes 1/4 of the air remaining in the cylinder at a time. Does this situation form an arithmetic progression?',
  '[{"id": "A", "text": "No, each stroke leaves 3/4 of the remaining volume, so differences are not constant (V, 3/4 V, 9/16 V, ...)", "is_correct": true}, {"id": "B", "text": "Yes, it is an AP with common difference d = -1/4", "is_correct": false}, {"id": "C", "text": "Yes, because air is continuously removed at equal intervals", "is_correct": false}, {"id": "D", "text": "No, because volume cannot be measured in an arithmetic progression", "is_correct": false}]'::jsonb,
  'Step 1: Let initial volume = V.
Step 2: After 1st stroke, volume left = V - (1/4)V = (3/4)V.
Step 3: After 2nd stroke, volume left = (3/4)V - (1/4)(3/4)V = (9/16)V.
Step 4: Difference a2 - a1 = -1/4 V, but a3 - a2 = -3/16 V != -1/4 V.
Since successive differences are not constant, it does NOT form an AP.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000003',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q1(iii)] The cost of digging a well after every metre of digging, when it costs ₹ 150 for the first metre and rises by ₹ 50 for each subsequent metre. Does this situation form an arithmetic progression?',
  '[{"id": "A", "text": "Yes, it forms an AP with first term a = 150 and common difference d = 50 (150, 200, 250, 300, ...)", "is_correct": true}, {"id": "B", "text": "No, digging costs increase exponentially with depth", "is_correct": false}, {"id": "C", "text": "No, because the first metre costs more than subsequent metres", "is_correct": false}, {"id": "D", "text": "Yes, but with common difference d = 100", "is_correct": false}]'::jsonb,
  'Step 1: Cost for 1 m = ₹ 150.
Step 2: Cost for 2 m = 150 + 50 = ₹ 200; for 3 m = 200 + 50 = ₹ 250; for 4 m = ₹ 300.
Step 3: List of numbers: 150, 200, 250, 300, ...
Step 4: Common difference d = 200 - 150 = 250 - 200 = 50 (constant).
Hence, it forms an AP.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000004',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q1(iv)] The amount of money in the account every year, when ₹ 10,000 is deposited at compound interest at 8% per annum. Does this situation form an arithmetic progression?',
  '[{"id": "A", "text": "No, compound interest increases the principal geometrically each year, so successive differences are not equal", "is_correct": true}, {"id": "B", "text": "Yes, it is an AP with common difference d = 800", "is_correct": false}, {"id": "C", "text": "Yes, it is an AP with common ratio r = 1.08", "is_correct": false}, {"id": "D", "text": "No, money can never form an AP", "is_correct": false}]'::jsonb,
  'Step 1: Year 1 amount = 10000(1 + 8/100) = ₹ 10,800.
Step 2: Year 2 amount = 10000(1 + 8/100)^2 = ₹ 11,664.
Step 3: Year 3 amount = 10000(1 + 8/100)^3 = ₹ 12,597.12.
Step 4: a2 - a1 = 800, while a3 - a2 = 864 != 800.
Since successive differences are not constant, compound interest does NOT form an AP.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000005',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q2(i)] Write the first four terms of the AP, when the first term a = 10 and the common difference d = 10.',
  '[{"id": "A", "text": "10, 20, 30, 40", "is_correct": true}, {"id": "B", "text": "10, 100, 1000, 10000", "is_correct": false}, {"id": "C", "text": "10, 0, -10, -20", "is_correct": false}, {"id": "D", "text": "0, 10, 20, 30", "is_correct": false}]'::jsonb,
  'Step 1: a1 = a = 10.
Step 2: a2 = a + d = 10 + 10 = 20.
Step 3: a3 = a2 + d = 20 + 10 = 30.
Step 4: a4 = a3 + d = 30 + 10 = 40.
First four terms are 10, 20, 30, 40.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000006',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q2(ii)] Write the first four terms of the AP, when the first term a = -2 and the common difference d = 0.',
  '[{"id": "A", "text": "-2, -2, -2, -2", "is_correct": true}, {"id": "B", "text": "-2, 0, 2, 4", "is_correct": false}, {"id": "C", "text": "-2, -4, -6, -8", "is_correct": false}, {"id": "D", "text": "0, -2, -4, -6", "is_correct": false}]'::jsonb,
  'Step 1: a1 = -2.
Step 2: a2 = -2 + 0 = -2.
Step 3: a3 = -2 + 0 = -2.
Step 4: a4 = -2 + 0 = -2.
When d = 0, every term is equal to a. The terms are -2, -2, -2, -2.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000007',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q2(iii)] Write the first four terms of the AP, when the first term a = 4 and the common difference d = -3.',
  '[{"id": "A", "text": "4, 1, -2, -5", "is_correct": true}, {"id": "B", "text": "4, 7, 10, 13", "is_correct": false}, {"id": "C", "text": "4, -3, -7, -11", "is_correct": false}, {"id": "D", "text": "4, 1, 0, -3", "is_correct": false}]'::jsonb,
  'Step 1: a1 = 4.
Step 2: a2 = 4 + (-3) = 1.
Step 3: a3 = 1 + (-3) = -2.
Step 4: a4 = -2 + (-3) = -5.
First four terms are 4, 1, -2, -5.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000008',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q2(iv)] Write the first four terms of the AP, when a = -1 and d = 1/2.',
  '[{"id": "A", "text": "-1, -1/2, 0, 1/2", "is_correct": true}, {"id": "B", "text": "-1, -3/2, -2, -5/2", "is_correct": false}, {"id": "C", "text": "-1, 0, 1, 2", "is_correct": false}, {"id": "D", "text": "-1, -1/2, -1/4, 0", "is_correct": false}]'::jsonb,
  'Step 1: a1 = -1.
Step 2: a2 = -1 + 1/2 = -1/2.
Step 3: a3 = -1/2 + 1/2 = 0.
Step 4: a4 = 0 + 1/2 = 1/2.
First four terms are -1, -1/2, 0, 1/2.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000009',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q2(v)] Write the first four terms of the AP, when a = -1.25 and d = -0.25.',
  '[{"id": "A", "text": "-1.25, -1.50, -1.75, -2.00", "is_correct": true}, {"id": "B", "text": "-1.25, -1.00, -0.75, -0.50", "is_correct": false}, {"id": "C", "text": "-1.25, -1.50, -1.70, -1.90", "is_correct": false}, {"id": "D", "text": "-1.25, -2.50, -3.75, -5.00", "is_correct": false}]'::jsonb,
  'Step 1: a1 = -1.25.
Step 2: a2 = -1.25 + (-0.25) = -1.50.
Step 3: a3 = -1.50 + (-0.25) = -1.75.
Step 4: a4 = -1.75 + (-0.25) = -2.00.
First four terms are -1.25, -1.50, -1.75, -2.00.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000010',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q3(i)] For the AP: 3, 1, -1, -3, ... write the first term and the common difference.',
  '[{"id": "A", "text": "First term a = 3, Common difference d = -2", "is_correct": true}, {"id": "B", "text": "First term a = 3, Common difference d = 2", "is_correct": false}, {"id": "C", "text": "First term a = 1, Common difference d = -2", "is_correct": false}, {"id": "D", "text": "First term a = -3, Common difference d = 1", "is_correct": false}]'::jsonb,
  'Step 1: First term is the first number in the sequence: a = 3.
Step 2: Common difference d = a2 - a1 = 1 - 3 = -2.
Step 3: Check: a3 - a2 = -1 - 1 = -2. Verified.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000011',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q3(ii)] For the AP: -5, -1, 3, 7, ... write the first term and the common difference.',
  '[{"id": "A", "text": "First term a = -5, Common difference d = 4", "is_correct": true}, {"id": "B", "text": "First term a = -5, Common difference d = -4", "is_correct": false}, {"id": "C", "text": "First term a = -1, Common difference d = 4", "is_correct": false}, {"id": "D", "text": "First term a = 7, Common difference d = 2", "is_correct": false}]'::jsonb,
  'Step 1: First term a = -5.
Step 2: Common difference d = a2 - a1 = -1 - (-5) = -1 + 5 = 4.
Step 3: Check: 3 - (-1) = 4, 7 - 3 = 4. Verified.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000012',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q3(iii)] For the AP: 1/3, 5/3, 9/3, 13/3, ... write the first term and the common difference.',
  '[{"id": "A", "text": "First term a = 1/3, Common difference d = 4/3", "is_correct": true}, {"id": "B", "text": "First term a = 1/3, Common difference d = 5/3", "is_correct": false}, {"id": "C", "text": "First term a = 5/3, Common difference d = 4/3", "is_correct": false}, {"id": "D", "text": "First term a = 1/3, Common difference d = 1", "is_correct": false}]'::jsonb,
  'Step 1: First term a = 1/3.
Step 2: Common difference d = 5/3 - 1/3 = 4/3.
Step 3: Check: 9/3 - 5/3 = 4/3. Verified.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000013',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.1 - Q4] Check whether the following sequences form an AP: (i) 2, 4, 8, 16, ... ; (ii) √2, √8, √18, √32, ... If they form an AP, find the common difference d and write three more terms.',
  '[{"id": "A", "text": "(i) is NOT an AP (differences 2, 4, 8); (ii) IS an AP with d = \u221a2 (terms are \u221a2, 2\u221a2, 3\u221a2, 4\u221a2), next terms: \u221a50, \u221a72, \u221a98", "is_correct": true}, {"id": "B", "text": "Both are APs with common difference d = 2 and d = \u221a2", "is_correct": false}, {"id": "C", "text": "(i) is an AP with d = 2; (ii) is not an AP because radicals cannot form AP", "is_correct": false}, {"id": "D", "text": "Neither is an AP", "is_correct": false}]'::jsonb,
  'Step 1: In (i): a2 - a1 = 4 - 2 = 2, but a3 - a2 = 8 - 4 = 4 != 2. Successive differences not equal, hence NOT an AP.
Step 2: In (ii): √2, √8 = 2√2, √18 = 3√2, √32 = 4√2.
Step 3: Common difference d = 2√2 - √2 = √2 (constant). Hence IS an AP.
Step 4: Next three terms are 5√2 = √50, 6√2 = √72, 7√2 = √98.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000014',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q1(i)] In the AP table, given first term a = 7, common difference d = 3, number of terms n = 8, find the nth term a_n.',
  '[{"id": "A", "text": "a_8 = 28", "is_correct": true}, {"id": "B", "text": "a_8 = 24", "is_correct": false}, {"id": "C", "text": "a_8 = 31", "is_correct": false}, {"id": "D", "text": "a_8 = 21", "is_correct": false}]'::jsonb,
  'Step 1: Formula: an = a + (n - 1)d.
Step 2: Substitute a = 7, d = 3, n = 8.
Step 3: a8 = 7 + (8 - 1) × 3 = 7 + 7 × 3 = 7 + 21 = 28.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000015',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q1(ii)] Given first term a = -18, number of terms n = 10, and nth term a_n = 0, find the common difference d.',
  '[{"id": "A", "text": "d = 2", "is_correct": true}, {"id": "B", "text": "d = -2", "is_correct": false}, {"id": "C", "text": "d = 1.8", "is_correct": false}, {"id": "D", "text": "d = 9", "is_correct": false}]'::jsonb,
  'Step 1: an = a + (n - 1)d.
Step 2: 0 = -18 + (10 - 1)d => 0 = -18 + 9d.
Step 3: 9d = 18 => d = 2.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000016',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q1(iv)] Given first term a = -18.9, common difference d = 2.5, and nth term a_n = 3.6, find the number of terms n.',
  '[{"id": "A", "text": "n = 10", "is_correct": true}, {"id": "B", "text": "n = 9", "is_correct": false}, {"id": "C", "text": "n = 11", "is_correct": false}, {"id": "D", "text": "n = 8", "is_correct": false}]'::jsonb,
  'Step 1: an = a + (n - 1)d.
Step 2: 3.6 = -18.9 + (n - 1)(2.5).
Step 3: 3.6 + 18.9 = 22.5 = 2.5(n - 1).
Step 4: n - 1 = 22.5 / 2.5 = 9 => n = 10.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000017',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q2(i)] Choose the correct choice: The 30th term of the AP: 10, 7, 4, ... is:',
  '[{"id": "A", "text": "97", "is_correct": false}, {"id": "B", "text": "77", "is_correct": false}, {"id": "C", "text": "-77", "is_correct": true}, {"id": "D", "text": "-87", "is_correct": false}]'::jsonb,
  'Step 1: a = 10, d = 7 - 10 = -3, n = 30.
Step 2: a30 = a + 29d.
Step 3: a30 = 10 + 29(-3) = 10 - 87 = -77.
Hence, choice C is correct.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000018',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q2(ii)] Choose the correct choice: The 11th term of the AP: -3, -1/2, 2, ... is:',
  '[{"id": "A", "text": "28", "is_correct": false}, {"id": "B", "text": "22", "is_correct": true}, {"id": "C", "text": "-38", "is_correct": false}, {"id": "D", "text": "-46.5", "is_correct": false}]'::jsonb,
  'Step 1: a = -3, d = -1/2 - (-3) = -1/2 + 3 = 5/2.
Step 2: a11 = a + 10d = -3 + 10(5/2) = -3 + 25 = 22.
Hence, choice B is correct.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000019',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q3] In the following APs, find the missing terms in the boxes: (i) 2, [ ], 26; (ii) [ ], 13, [ ], 3.',
  '[{"id": "A", "text": "(i) Box = 14; (ii) First box = 18, Third box = 8", "is_correct": true}, {"id": "B", "text": "(i) Box = 12; (ii) First box = 16, Third box = 10", "is_correct": false}, {"id": "C", "text": "(i) Box = 14; (ii) First box = 15, Third box = 9", "is_correct": false}, {"id": "D", "text": "(i) Box = 13; (ii) First box = 17, Third box = 7", "is_correct": false}]'::jsonb,
  'Step 1: For (i): Middle term of a, b, c in AP is (a + c)/2 = (2 + 26)/2 = 14.
Step 2: For (ii): a + d = 13 and a + 3d = 3. Subtracting gives 2d = -10 => d = -5.
Step 3: a = 13 - (-5) = 18, and third term = 13 + (-5) = 8.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000020',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q4] Which term of the AP: 3, 8, 13, 18, ... is 78?',
  '[{"id": "A", "text": "16th term", "is_correct": true}, {"id": "B", "text": "15th term", "is_correct": false}, {"id": "C", "text": "17th term", "is_correct": false}, {"id": "D", "text": "14th term", "is_correct": false}]'::jsonb,
  'Step 1: a = 3, d = 8 - 3 = 5, an = 78.
Step 2: 78 = 3 + (n - 1)5 => 75 = 5(n - 1).
Step 3: n - 1 = 15 => n = 16.
Hence, 78 is the 16th term.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000021',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q5(i)] Find the number of terms in the AP: 7, 13, 19, ..., 205.',
  '[{"id": "A", "text": "34 terms", "is_correct": true}, {"id": "B", "text": "33 terms", "is_correct": false}, {"id": "C", "text": "35 terms", "is_correct": false}, {"id": "D", "text": "32 terms", "is_correct": false}]'::jsonb,
  'Step 1: a = 7, d = 13 - 7 = 6, an = 205.
Step 2: 205 = 7 + (n - 1)6 => 198 = 6(n - 1).
Step 3: n - 1 = 33 => n = 34.
Hence, there are 34 terms.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000022',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q6] Check whether -150 is a term of the AP: 11, 8, 5, 2, ...',
  '[{"id": "A", "text": "No, because solving for n gives n = 164/3 = 54 2/3, which is not a positive integer", "is_correct": true}, {"id": "B", "text": "Yes, it is the 54th term", "is_correct": false}, {"id": "C", "text": "Yes, it is the 55th term", "is_correct": false}, {"id": "D", "text": "No, because terms of an AP cannot be negative", "is_correct": false}]'::jsonb,
  'Step 1: a = 11, d = 8 - 11 = -3. Let an = -150.
Step 2: -150 = 11 + (n - 1)(-3) => -161 = -3(n - 1).
Step 3: n - 1 = 161/3 => n = 164/3 = 54 2/3.
Since n must be a positive integer, -150 is NOT a term of this AP.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000023',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q7] Find the 31st term of an AP whose 11th term is 38 and the 16th term is 73.',
  '[{"id": "A", "text": "178", "is_correct": true}, {"id": "B", "text": "185", "is_correct": false}, {"id": "C", "text": "171", "is_correct": false}, {"id": "D", "text": "168", "is_correct": false}]'::jsonb,
  'Step 1: a11 = a + 10d = 38 ... (1) and a16 = a + 15d = 73 ... (2).
Step 2: Subtracting (1) from (2): 5d = 35 => d = 7.
Step 3: a + 10(7) = 38 => a = 38 - 70 = -32.
Step 4: a31 = a + 30d = -32 + 30(7) = -32 + 210 = 178.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000024',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q8] An AP consists of 50 terms of which 3rd term is 12 and the last term is 106. Find the 29th term.',
  '[{"id": "A", "text": "64", "is_correct": true}, {"id": "B", "text": "62", "is_correct": false}, {"id": "C", "text": "68", "is_correct": false}, {"id": "D", "text": "56", "is_correct": false}]'::jsonb,
  'Step 1: Total terms = 50 => a50 = a + 49d = 106.
Step 2: a3 = a + 2d = 12.
Step 3: Subtracting gives 47d = 94 => d = 2.
Step 4: a = 12 - 2(2) = 8.
Step 5: a29 = a + 28d = 8 + 28(2) = 8 + 56 = 64.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000025',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q10] The 17th term of an AP exceeds its 10th term by 7. Find the common difference.',
  '[{"id": "A", "text": "d = 1", "is_correct": true}, {"id": "B", "text": "d = 2", "is_correct": false}, {"id": "C", "text": "d = 7", "is_correct": false}, {"id": "D", "text": "d = 0.5", "is_correct": false}]'::jsonb,
  'Step 1: a17 - a10 = 7.
Step 2: (a + 16d) - (a + 9d) = 7.
Step 3: 7d = 7 => d = 1.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000026',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q13] How many three-digit numbers are divisible by 7?',
  '[{"id": "A", "text": "128", "is_correct": true}, {"id": "B", "text": "127", "is_correct": false}, {"id": "C", "text": "129", "is_correct": false}, {"id": "D", "text": "130", "is_correct": false}]'::jsonb,
  'Step 1: First 3-digit number divisible by 7 is 105; last is 994.
Step 2: AP: 105, 112, ..., 994 with a = 105, d = 7, an = 994.
Step 3: 994 = 105 + (n - 1)7 => 889 = 7(n - 1).
Step 4: n - 1 = 127 => n = 128.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000027',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q17] Find the 20th term from the last term of the AP: 3, 8, 13, ..., 253.',
  '[{"id": "A", "text": "158", "is_correct": true}, {"id": "B", "text": "163", "is_correct": false}, {"id": "C", "text": "153", "is_correct": false}, {"id": "D", "text": "148", "is_correct": false}]'::jsonb,
  'Step 1: Reverse AP from the end: 253, 248, 243, ..., 3.
Step 2: First term a = 253, common difference d = -5.
Step 3: a20 = a + 19d = 253 + 19(-5) = 253 - 95 = 158.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000028',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.2 - Q19] Subba Rao started work in 1995 at an annual salary of ₹ 5000 and received an increment of ₹ 200 each year. In which year did his income reach ₹ 7000?',
  '[{"id": "A", "text": "11th year (Year 2005)", "is_correct": true}, {"id": "B", "text": "10th year (Year 2004)", "is_correct": false}, {"id": "C", "text": "12th year (Year 2006)", "is_correct": false}, {"id": "D", "text": "9th year (Year 2003)", "is_correct": false}]'::jsonb,
  'Step 1: Series forms an AP: 5000, 5200, 5400, ..., 7000 with a = 5000, d = 200, an = 7000.
Step 2: 7000 = 5000 + (n - 1)200 => 2000 = 200(n - 1) => n - 1 = 10 => n = 11.
Step 3: 11th year from 1995: 1995 + (11 - 1) = 2005.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000029',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.3 - Q1(i)] Find the sum of the AP: 2, 7, 12, ... to 10 terms.',
  '[{"id": "A", "text": "245", "is_correct": true}, {"id": "B", "text": "250", "is_correct": false}, {"id": "C", "text": "240", "is_correct": false}, {"id": "D", "text": "255", "is_correct": false}]'::jsonb,
  'Step 1: a = 2, d = 5, n = 10.
Step 2: Sn = (n/2)[2a + (n - 1)d].
Step 3: S10 = (10/2)[2(2) + 9(5)] = 5[4 + 45] = 5(49) = 245.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000030',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.3 - Q1(ii)] Find the sum of the AP: -37, -33, -29, ... to 12 terms.',
  '[{"id": "A", "text": "-180", "is_correct": true}, {"id": "B", "text": "-192", "is_correct": false}, {"id": "C", "text": "-168", "is_correct": false}, {"id": "D", "text": "-200", "is_correct": false}]'::jsonb,
  'Step 1: a = -37, d = 4, n = 12.
Step 2: S12 = (12/2)[2(-37) + 11(4)] = 6[-74 + 44] = 6(-30) = -180.',
  'easy',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000031',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.3 - Q2(i)] Find the sum: 7 + 10 1/2 + 14 + ... + 84.',
  '[{"id": "A", "text": "1046 1/2 (1046.5)", "is_correct": true}, {"id": "B", "text": "1040", "is_correct": false}, {"id": "C", "text": "1050 1/2", "is_correct": false}, {"id": "D", "text": "1036", "is_correct": false}]'::jsonb,
  'Step 1: a = 7, d = 7/2, l = an = 84.
Step 2: 84 = 7 + (n - 1)(7/2) => 77 = (7/2)(n - 1) => n - 1 = 22 => n = 23.
Step 3: S23 = (n/2)(a + l) = (23/2)(7 + 84) = (23 × 91)/2 = 2093/2 = 1046 1/2.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000032',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.3 - Q4] How many terms of the AP: 9, 17, 25, ... must be taken to give a sum of 636?',
  '[{"id": "A", "text": "12 terms", "is_correct": true}, {"id": "B", "text": "14 terms", "is_correct": false}, {"id": "C", "text": "10 terms", "is_correct": false}, {"id": "D", "text": "16 terms", "is_correct": false}]'::jsonb,
  'Step 1: a = 9, d = 8, Sn = 636.
Step 2: 636 = (n/2)[2(9) + (n - 1)8] = n(4n + 5) => 4n² + 5n - 636 = 0.
Step 3: Factorise: (n - 12)(4n + 53) = 0 => n = 12 (since n > 0).
Hence, 12 terms must be taken.',
  'hard',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000033',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.3 - Q7] Find the sum of first 22 terms of an AP in which d = 7 and 22nd term is 149.',
  '[{"id": "A", "text": "1661", "is_correct": true}, {"id": "B", "text": "1650", "is_correct": false}, {"id": "C", "text": "1672", "is_correct": false}, {"id": "D", "text": "1640", "is_correct": false}]'::jsonb,
  'Step 1: n = 22, d = 7, a22 = 149.
Step 2: a + 21(7) = 149 => a + 147 = 149 => a = 2.
Step 3: S22 = (22/2)[a + a22] = 11[2 + 149] = 11 × 151 = 1661.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000034',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.3 - Q12] Find the sum of the first 40 positive integers divisible by 6.',
  '[{"id": "A", "text": "4920", "is_correct": true}, {"id": "B", "text": "4860", "is_correct": false}, {"id": "C", "text": "4980", "is_correct": false}, {"id": "D", "text": "4800", "is_correct": false}]'::jsonb,
  'Step 1: Integers divisible by 6 are: 6, 12, 18, ... to 40 terms.
Step 2: a = 6, d = 6, n = 40.
Step 3: S40 = (40/2)[2(6) + 39(6)] = 20[12 + 234] = 20 × 246 = 4920.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;

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
) VALUES (
  '10000000-0000-0000-0005-000000000035',
  'math',
  'math_ch_05_arithmetic_progressions',
  '[Exercise 5.3 - Q14] Find the sum of the odd numbers between 0 and 50.',
  '[{"id": "A", "text": "625", "is_correct": true}, {"id": "B", "text": "600", "is_correct": false}, {"id": "C", "text": "650", "is_correct": false}, {"id": "D", "text": "576", "is_correct": false}]'::jsonb,
  'Step 1: Odd numbers between 0 and 50: 1, 3, 5, ..., 49.
Step 2: a = 1, d = 2, an = 49 => 49 = 1 + (n - 1)2 => 2(n - 1) = 48 => n = 25.
Step 3: S25 = (25/2)(1 + 49) = (25 × 50)/2 = 25 × 25 = 625.',
  'medium',
  'approved',
  '00000000-0000-0000-0000-000000000001',
  '00000000-0000-0000-0000-000000000001',
  NOW()
) ON CONFLICT (id) DO UPDATE SET
  question_text = EXCLUDED.question_text,
  options = EXCLUDED.options,
  step_by_step_solution = EXCLUDED.step_by_step_solution,
  difficulty_level = EXCLUDED.difficulty_level,
  status = EXCLUDED.status;
