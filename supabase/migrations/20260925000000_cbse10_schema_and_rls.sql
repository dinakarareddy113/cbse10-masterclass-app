-- ==============================================================================
-- Migration: 20260925000000_cbse10_schema_and_rls.sql
-- Project: CBSE Class 10 Masterclass
-- Description: Core Schema, RBAC Profiles, Question Bank, and Row Level Security
-- ==============================================================================

-- Enable UUID extension if not already present
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- ==============================================================================
-- 1. PROFILES TABLE (Extension of auth.users)
-- ==============================================================================
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    full_name TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'student' CHECK (role IN ('student', 'teacher', 'admin')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT TIMEZONE('utc'::text, NOW())
);

-- Enable RLS on Profiles
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;

-- Profiles Policies
DROP POLICY IF EXISTS "Users can read own profile or admin can read all" ON public.profiles;
CREATE POLICY "Users can read own profile or admin can read all"
ON public.profiles FOR SELECT
USING (
    auth.uid() = id 
    OR EXISTS (
        SELECT 1 FROM public.profiles p 
        WHERE p.id = auth.uid() AND p.role = 'admin'
    )
);

DROP POLICY IF EXISTS "Users can update own profile" ON public.profiles;
CREATE POLICY "Users can update own profile"
ON public.profiles FOR UPDATE
USING (auth.uid() = id)
WITH CHECK (auth.uid() = id);

-- Trigger to automatically create a profile record when a new user signs up via Supabase Auth
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.profiles (id, full_name, role)
    VALUES (
        NEW.id,
        COALESCE(NEW.raw_user_meta_data->>'full_name', 'Student User'),
        COALESCE(NEW.raw_user_meta_data->>'role', 'student')
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();


-- ==============================================================================
-- 2. QUESTIONS TABLE (Central Content Repository)
-- ==============================================================================
CREATE TABLE IF NOT EXISTS public.questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    subject TEXT NOT NULL CHECK (subject IN ('math', 'science', 'social_science')),
    chapter_id TEXT NOT NULL,
    question_text TEXT NOT NULL,
    options JSONB, -- Formatted as [{"id": "A", "text": "...", "is_correct": true}, ...] for MCQs
    step_by_step_solution TEXT NOT NULL,
    difficulty_level TEXT NOT NULL CHECK (difficulty_level IN ('easy', 'medium', 'hard', 'hots')),
    status TEXT NOT NULL DEFAULT 'pending_review' CHECK (status IN ('pending_review', 'approved', 'rejected')),
    rejection_feedback TEXT,
    submitted_by UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    reviewed_by UUID REFERENCES auth.users(id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT TIMEZONE('utc'::text, NOW())
);

-- Performance Indexes
CREATE INDEX IF NOT EXISTS idx_questions_subject_status ON public.questions(subject, status);
CREATE INDEX IF NOT EXISTS idx_questions_chapter_id ON public.questions(chapter_id);
CREATE INDEX IF NOT EXISTS idx_questions_difficulty ON public.questions(difficulty_level);
CREATE INDEX IF NOT EXISTS idx_questions_status ON public.questions(status);
CREATE INDEX IF NOT EXISTS idx_questions_submitted_by ON public.questions(submitted_by);

-- Enable RLS on Questions
ALTER TABLE public.questions ENABLE ROW LEVEL SECURITY;

-- ==============================================================================
-- 3. ROW LEVEL SECURITY (RLS) POLICIES
-- ==============================================================================

-- Policy 1: Student Read Policy
-- Students and unauthenticated users can only read questions where status = 'approved'.
-- Admins can read all questions (pending_review, approved, rejected) across all subjects.
DROP POLICY IF EXISTS "Public read approved questions" ON public.questions;
CREATE POLICY "Public read approved questions" 
ON public.questions FOR SELECT 
USING (
    status = 'approved' 
    OR auth.uid() IN (SELECT id FROM public.profiles WHERE role = 'admin')
    OR auth.uid() = submitted_by
);

-- Policy 2: Submission Policy
-- Authenticated users (teachers/admins/system ingestion scripts) can insert new items.
-- Must set submitted_by to their own user id and default to 'pending_review' (unless admin).
DROP POLICY IF EXISTS "Users can insert questions" ON public.questions;
CREATE POLICY "Users can insert questions" 
ON public.questions FOR INSERT 
WITH CHECK (
    auth.uid() = submitted_by
);

-- Policy 3: Admin Review Policy
-- Only users with role = 'admin' can update question statuses (approve, reject, edit).
DROP POLICY IF EXISTS "Admins can update review status" ON public.questions;
CREATE POLICY "Admins can update review status" 
ON public.questions FOR UPDATE 
USING (
    EXISTS (
        SELECT 1 FROM public.profiles 
        WHERE id = auth.uid() AND role = 'admin'
    )
);

-- Policy 4: Admin Delete Policy
-- Only admins can purge question entries
DROP POLICY IF EXISTS "Admins can delete questions" ON public.questions;
CREATE POLICY "Admins can delete questions" 
ON public.questions FOR DELETE 
USING (
    EXISTS (
        SELECT 1 FROM public.profiles 
        WHERE id = auth.uid() AND role = 'admin'
    )
);
