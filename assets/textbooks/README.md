# CBSE Class 10 Masterclass - Admin PDF and Q&A Ingestion Guide

This guide provides instructions for administrators and educators on how and where to upload NCERT textbook PDF documents to generate textbook-accurate Q&A for the app.

---

## 1. Where to Upload Textbook PDFs

There are three ways for administrators to process NCERT chapter PDFs:

```
+------------------------------------------------------------------------+
|                        ADMIN INGESTION OPTIONS                         |
+------------------------------------------------------------------------+
|                                                                        |
|  [METHOD 1: In-Chat Drag-and-Drop]  (Fastest and Recommended)          |
|    Drag and drop the NCERT PDF or textbook page screenshots directly   |
|    into this AI chat session with instructions:                        |
|    "Extract and ingest all Exercise questions for Chapter X."          |
|                                                                        |
|  [METHOD 2: Dedicated Folder]       (Batch Repository Storage)         |
|    Place PDF files in: assets/textbooks/                               |
|    e.g., assets/textbooks/math_ch_02_polynomials.pdf                   |
|    Then notify the assistant or run the ingestion script.              |
|                                                                        |
|  [METHOD 3: In-App Admin Screen]    (Direct In-App Bulk Publishing)    |
|    Navigate to Admin Tab in App -> Bulk Ingest and Direct Publish      |
|    Select target chapter -> Paste JSON -> Click "Publish Directly"     |
|                                                                        |
+------------------------------------------------------------------------+
```

---

## 2. Method 1: Direct In-Chat Upload (Fastest)

1. **Attach the PDF**: Click the attachment (+) button or drag and drop your NCERT chapter PDF directly into this AI conversation window.
2. **Specify Prompt**:
   > *"Attached is NCERT Class 10 Mathematics Chapter 2 (Polynomials). Please parse all questions and sub-parts from Exercise 2.1 and 2.2 with 100% textbook-accurate wording, step-by-step solutions, and publish to the student practice feed."*
3. **Automated Pipeline**:
   - The AI extracts all exercises and sub-questions.
   - Generates step-by-step mathematical proofs and solutions.
   - Creates the Supabase SQL migration (`status = 'approved'`).
   - Updates local datasets and Flutter practice screens with exercise filter chips.

---

## 3. Method 2: Repository Asset Directory (`assets/textbooks/`)

For structured file storage:

1. **Upload / Save PDF**: Place the chapter PDF into:
   ```
   g:\My Drive\AI_Projects\AntiGravity_Exam_Guide\assets\textbooks\
   ```
2. **Naming Convention**:
   - `math_ch_01_real_numbers.pdf`
   - `math_ch_02_polynomials.pdf`
   - `math_ch_03_linear_equations.pdf`
   - `math_ch_04_quadratic_equations.pdf`
   - `science_ch_01_chemical_reactions.pdf`
3. **Process**:
   Tell the assistant: *"I have added `assets/textbooks/math_ch_02_polynomials.pdf`. Ingest all exercise questions for Chapter 2."*

---

## 4. Method 3: In-App Admin Bulk Ingestion Hub

In the Flutter App or Mobile Web Harness (`http://localhost:8080`):

1. **Select Persona**: Switch top-right role dropdown to **Admin (Mod and Pipeline)**.
2. **Open Admin Tab**: Tap the **Admin** icon on the bottom navigation bar.
3. **Select Pipeline**: Click **Bulk Ingest and Direct Publish**.
4. **Choose Target Chapter**: Select any of the 14 bilingual chapters from the dropdown.
5. **Paste Parsed Question JSON**: Paste the structured array or click **"Load Sample NCERT JSON"**.
6. **Tap "Publish Directly to Student Feed"**:
   - The questions are marked `status = 'approved'`, stored in the database, and immediately appear in the student practice view.

---

## 5. Security and Access Control (RBAC)

- **Students (`role = 'student'`)**: Strictly read-only access. Cannot generate, edit, or moderate questions.
- **Faculty / Submissions (`role = 'teacher'`)**: Submissions enter `status = 'pending_review'` for moderation.
- **Admins (`role = 'admin'`)**: Can approve/reject queue items or publish directly to student feeds.
