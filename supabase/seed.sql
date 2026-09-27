-- ==============================================================================
-- Seed Script: supabase/seed.sql
-- Project: CBSE Class 10 Masterclass
-- High-yield authentic NCERT & Board Exam questions, MCQs, and solutions
-- ==============================================================================

-- Mock Admin & Teacher User IDs for local seeding
DO $$
DECLARE
    v_admin_id UUID := '00000000-0000-0000-0000-000000000001';
    v_teacher_id UUID := '00000000-0000-0000-0000-000000000002';
    v_student_id UUID := '00000000-0000-0000-0000-000000000003';
BEGIN
    -- Insert mock profiles for testing local emulation
    INSERT INTO public.profiles (id, full_name, role)
    VALUES 
        (v_admin_id, 'Lead Examiner (Admin)', 'admin'),
        (v_teacher_id, 'Prof. R.K. Sharma (Teacher)', 'teacher'),
        (v_student_id, 'Aarav Patel (Student)', 'student')
    ON CONFLICT (id) DO UPDATE SET role = EXCLUDED.role, full_name = EXCLUDED.full_name;

    -- ==========================================================================
    -- 1. MATHEMATICS SEED DATA (Approved & Pending)
    -- ==========================================================================
    
    -- Approved Math Q1: Quadratic Equations (HOTS)
    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '10000000-0000-0000-0000-000000000001',
        'math',
        'ch_04_quadratic_equations',
        'Find the value of k for which the quadratic equation (k - 12)x^2 + 2(k - 12)x + 2 = 0 has two equal real roots, given k ≠ 12.',
        jsonb_build_array(
            jsonb_build_object('id', 'A', 'text', 'k = 12', 'is_correct', false),
            jsonb_build_object('id', 'B', 'text', 'k = 14', 'is_correct', true),
            jsonb_build_object('id', 'C', 'text', 'k = 10', 'is_correct', false),
            jsonb_build_object('id', 'D', 'text', 'k = 16', 'is_correct', false)
        ),
        'Step 1: Standard form ax^2 + bx + c = 0 has equal roots when discriminant D = b^2 - 4ac = 0.\nStep 2: Here a = (k - 12), b = 2(k - 12), c = 2.\nStep 3: D = [2(k - 12)]^2 - 4(k - 12)(2) = 0\nStep 4: 4(k - 12)^2 - 8(k - 12) = 0\nStep 5: Factor out 4(k - 12): 4(k - 12)[(k - 12) - 2] = 0\nStep 6: Either k - 12 = 0 => k = 12 (rejected as condition states k ≠ 12) or k - 14 = 0 => k = 14.\nTherefore, k = 14.',
        'hots',
        'approved',
        v_teacher_id,
        v_admin_id,
        NOW() - INTERVAL '2 days'
    );

    -- Approved Math Q2: Trigonometry Identity
    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '10000000-0000-0000-0000-000000000002',
        'math',
        'ch_08_introduction_to_trigonometry',
        'If sin(θ) + cos(θ) = √3, find the value of sin(θ) * cos(θ).',
        jsonb_build_array(
            jsonb_build_object('id', 'A', 'text', '1/2', 'is_correct', false),
            jsonb_build_object('id', 'B', 'text', '1', 'is_correct', true),
            jsonb_build_object('id', 'C', 'text', '√3/2', 'is_correct', false),
            jsonb_build_object('id', 'D', 'text', '1/4', 'is_correct', false)
        ),
        'Step 1: Given: sin(θ) + cos(θ) = √3\nStep 2: Square both sides: [sin(θ) + cos(θ)]^2 = (√3)^2\nStep 3: Expand: sin^2(θ) + cos^2(θ) + 2sin(θ)cos(θ) = 3\nStep 4: Using Pythagorean identity sin^2(θ) + cos^2(θ) = 1:\n1 + 2sin(θ)cos(θ) = 3\nStep 5: 2sin(θ)cos(θ) = 3 - 1 = 2\nStep 6: sin(θ)cos(θ) = 2 / 2 = 1.',
        'medium',
        'approved',
        v_teacher_id,
        v_admin_id,
        NOW() - INTERVAL '1 day'
    );

    -- PENDING Math Q3: Arithmetic Progression (Awaiting Moderation)
    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '10000000-0000-0000-0000-000000000003',
        'math',
        'ch_05_arithmetic_progressions',
        'In an AP, if the sum of the first n terms is given by Sn = 3n^2 + 5n, find the 20th term of this progression.',
        jsonb_build_array(
            jsonb_build_object('id', 'A', 'text', '118', 'is_correct', false),
            jsonb_build_object('id', 'B', 'text', '122', 'is_correct', true),
            jsonb_build_object('id', 'C', 'text', '120', 'is_correct', false),
            jsonb_build_object('id', 'D', 'text', '126', 'is_correct', false)
        ),
        'Step 1: nth term an = Sn - Sn-1\nStep 2: a20 = S20 - S19\nStep 3: S20 = 3(20)^2 + 5(20) = 3(400) + 100 = 1300\nStep 4: S19 = 3(19)^2 + 5(19) = 3(361) + 95 = 1083 + 95 = 1178\nStep 5: a20 = 1300 - 1178 = 122.\n(Alternative method: an = d/dn(3n^2 - 3n) + ... common difference d = 6, a1 = 8, a20 = 8 + 19(6) = 122).',
        'hard',
        'pending_review',
        v_teacher_id,
        NULL,
        NOW() - INTERVAL '3 hours'
    );

    -- ==========================================================================
    -- 2. SCIENCE SEED DATA (Approved & Pending)
    -- ==========================================================================

    -- Approved Science Q1: Physics - Light (Ray Diagram)
    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '20000000-0000-0000-0000-000000000001',
        'science',
        'sci_ch_09_light_reflection_refraction',
        'An object is placed at a distance of 10 cm in front of a concave mirror of focal length 15 cm. What are the characteristics of the image formed?',
        jsonb_build_array(
            jsonb_build_object('id', 'A', 'text', 'Real, inverted, and diminished', 'is_correct', false),
            jsonb_build_object('id', 'B', 'text', 'Virtual, erect, and magnified', 'is_correct', true),
            jsonb_build_object('id', 'C', 'text', 'Real, inverted, and magnified', 'is_correct', false),
            jsonb_build_object('id', 'D', 'text', 'Virtual, erect, and same size', 'is_correct', false)
        ),
        'Step 1: Sign convention: Focal length f = -15 cm (concave mirror), Object distance u = -10 cm.\nStep 2: Note that |u| < |f| (the object is placed between the Focus and the Pole of the mirror).\nStep 3: Mirror formula: 1/f = 1/v + 1/u => 1/v = 1/f - 1/u\nStep 4: 1/v = 1/(-15) - 1/(-10) = -1/15 + 1/10 = (-2 + 3)/30 = +1/30\nStep 5: v = +30 cm (positive sign implies the image is formed behind the mirror).\nStep 6: Magnification m = -v/u = -(30)/(-10) = +3. Positive magnification signifies a virtual, erect, and magnified image.',
        'medium',
        'approved',
        v_teacher_id,
        v_admin_id,
        NOW() - INTERVAL '3 days'
    );

    -- Approved Science Q2: Chemistry - Redox & Balancing
    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '20000000-0000-0000-0000-000000000002',
        'science',
        'sci_ch_01_chemical_reactions_equations',
        'In the reaction: MnO2 + 4HCl → MnCl2 + 2H2O + Cl2, identify the substance oxidized and the oxidizing agent respectively.',
        jsonb_build_array(
            jsonb_build_object('id', 'A', 'text', 'Oxidized: MnO2, Oxidizing Agent: HCl', 'is_correct', false),
            jsonb_build_object('id', 'B', 'text', 'Oxidized: HCl, Oxidizing Agent: MnO2', 'is_correct', true),
            jsonb_build_object('id', 'C', 'text', 'Oxidized: Cl2, Oxidizing Agent: MnCl2', 'is_correct', false),
            jsonb_build_object('id', 'D', 'text', 'Oxidized: MnO2, Oxidizing Agent: H2O', 'is_correct', false)
        ),
        'Step 1: Oxidation is the loss of hydrogen or gain of oxygen. Reduction is the loss of oxygen or gain of hydrogen.\nStep 2: In HCl, hydrogen is removed to form Cl2. Thus, HCl is oxidized to Cl2.\nStep 3: In MnO2, oxygen is removed to form MnCl2. Thus, MnO2 is reduced to MnCl2.\nStep 4: The substance that gets reduced acts as the oxidizing agent. Therefore, MnO2 is the oxidizing agent and HCl is the substance oxidized.',
        'easy',
        'approved',
        v_teacher_id,
        v_admin_id,
        NOW() - INTERVAL '2 days'
    );

    -- PENDING Science Q3: Biology - Nephron Excretion (Awaiting Moderation)
    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '20000000-0000-0000-0000-000000000003',
        'science',
        'sci_ch_06_life_processes',
        'Which component of the human nephron is primarily responsible for selective reabsorption of glucose, amino acids, and major amounts of water?',
        jsonb_build_array(
            jsonb_build_object('id', 'A', 'text', 'Bowman''s capsule', 'is_correct', false),
            jsonb_build_object('id', 'B', 'text', 'Glomerulus', 'is_correct', false),
            jsonb_build_object('id', 'C', 'text', 'Tubular part of nephron (PCT/Loop of Henle)', 'is_correct', true),
            jsonb_build_object('id', 'D', 'text', 'Collecting duct only', 'is_correct', false)
        ),
        'Step 1: Ultrafiltration occurs at the glomerulus where blood enters Bowman''s capsule under high pressure.\nStep 2: The filtrate contains glucose, amino acids, salts, and excess water.\nStep 3: As the filtrate moves along the long coiled tubular part (especially the Proximal Convoluted Tubule and Henle''s loop), selective reabsorption occurs back into surrounding blood capillaries depending on the body''s hydration balance.\nStep 4: Waste fluid enters the collecting duct as urine.',
        'medium',
        'pending_review',
        v_teacher_id,
        NULL,
        NOW() - INTERVAL '1 hour'
    );

    -- ==========================================================================
    -- 3. SOCIAL SCIENCE SEED DATA (Approved & Pending)
    -- ==========================================================================

    -- Approved SST Q1: History - Nationalism in India
    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '30000000-0000-0000-0000-000000000001',
        'social_science',
        'sst_hist_ch_02_nationalism_in_india',
        'Why did Mahatma Gandhi decide to withdraw the Non-Cooperation Movement in February 1922?',
        jsonb_build_array(
            jsonb_build_object('id', 'A', 'text', 'Passing of the Rowlatt Act', 'is_correct', false),
            jsonb_build_object('id', 'B', 'text', 'The violent incident at Chauri Chaura', 'is_correct', true),
            jsonb_build_object('id', 'C', 'text', 'Execution of Bhagat Singh', 'is_correct', false),
            jsonb_build_object('id', 'D', 'text', 'Arrival of the Simon Commission', 'is_correct', false)
        ),
        'Step 1: In February 1922, at Chauri Chaura in Gorakhpur (Uttar Pradesh), a peaceful demonstration in a bazaar turned into a violent clash with the police.\nStep 2: Hearing of the clash, demonstrators set fire to a police station, resulting in the death of 22 policemen.\nStep 3: Mahatma Gandhi felt that the movement was turning violent in many places and satyagrahis needed to be properly trained before they would be ready for mass struggles.\nStep 4: He immediately halted the nationwide Non-Cooperation Movement.',
        'easy',
        'approved',
        v_teacher_id,
        v_admin_id,
        NOW() - INTERVAL '4 days'
    );

    -- Approved SST Q2: Geography - Map Work (Major Sea Ports)
    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '30000000-0000-0000-0000-000000000002',
        'social_science',
        'sst_geo_ch_07_lifelines_of_national_economy',
        'Which tidal port in Gujarat was developed soon after Independence to ease the volume of trade on Mumbai port following the loss of Karachi port to Pakistan?',
        jsonb_build_array(
            jsonb_build_object('id', 'A', 'text', 'Marmagao Port', 'is_correct', false),
            jsonb_build_object('id', 'B', 'text', 'Kandla (Deendayal Port)', 'is_correct', true),
            jsonb_build_object('id', 'C', 'text', 'Paradip Port', 'is_correct', false),
            jsonb_build_object('id', 'D', 'text', 'Tuticorin Port', 'is_correct', false)
        ),
        'Step 1: Kandla in Kachchh was the first port developed soon after Independence.\nStep 2: Reason: Partition led to Karachi port going to Pakistan, putting extreme strain on Mumbai.\nStep 3: Kandla is a tidal port and caters to convenient handling of exports and imports of highly productive granary and industrial belts across Jammu & Kashmir, Himachal, Punjab, Haryana, and Rajasthan.\nStep 4: Renamed as Deendayal Port Authority.',
        'easy',
        'approved',
        v_teacher_id,
        v_admin_id,
        NOW() - INTERVAL '2 days'
    );

    -- PENDING SST Q3: Civics - Federalism (Awaiting Moderation)
    INSERT INTO public.questions (
        id, subject, chapter_id, question_text, options, step_by_step_solution,
        difficulty_level, status, submitted_by, reviewed_by, created_at
    ) VALUES (
        '30000000-0000-0000-0000-000000000003',
        'social_science',
        'sst_civ_ch_02_federalism',
        'Under the 73rd Constitutional Amendment Act (1992), which of the following provisions was made mandatory for local self-government in India?',
        jsonb_build_array(
            jsonb_build_object('id', 'A', 'text', 'Holding regular elections every 5 years and 1/3rd seats reserved for women', 'is_correct', true),
            jsonb_build_object('id', 'B', 'text', 'Abolishing the State Election Commission', 'is_correct', false),
            jsonb_build_object('id', 'C', 'text', 'Direct control of village panchayats by the Governor', 'is_correct', false),
            jsonb_build_object('id', 'D', 'text', 'Exempting municipalities from state revenue sharing', 'is_correct', false)
        ),
        'Step 1: The 1992 constitutional amendment transformed decentralization in India.\nStep 2: Key mandatory provisions:\n- Regular elections to local government bodies every 5 years.\n- At least 1/3rd of all positions are reserved for women.\n- Reservation of seats for SC, ST, and OBCs.\n- Creation of an independent State Election Commission in each state.\n- State governments must share revenue and powers with local bodies.',
        'medium',
        'pending_review',
        v_teacher_id,
        NULL,
        NOW() - INTERVAL '30 minutes'
    );

END $$;
