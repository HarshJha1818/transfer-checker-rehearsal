   
   
   # Product Requirements Document (PRD)
> **Note:** Practice rehearsal by Harsh Jha. Goal: help students minimize credit loss when transferring from one college or university to another.   

   ## Problem statement

Students who transfer lose credits and time because they can't easily see which courses
count toward their new degree. A 2017 federal GAO report found transfer students lost an
estimated 43% of their credits on average (22% for public 2-year to public 4-year transfers).
Florida's Statewide Course Numbering System (SCNS) guarantees transfer for equivalent courses,
but students still have to match their transcript against their target major's requirements
by hand. Transfer Credit Gap Checker does that matching and explains every result.

   ## Business requirements
- **BR1:** Students can see which of their completed courses count toward their target major.
- **BR2:** Students can see which required courses they still need to take.
- **BR3:** Every result is explained and traceable to the student's own documents.
- **BR4:** Students can see how many credits apply and how many remain.
- **BR5:** The tool protects privacy (stores nothing) and reminds students to confirm with an advisor.
- **BR6:** The first version covers Florida public college to Florida public university transfers.

**Success measures**
- Correct results on all three test transcripts.
- Results appear within 30 seconds of uploading.
- A student can understand the results without anyone explaining them.

   ## Persona
 Harsh, 19, earning an AA at Valencia College and planning to transfer to a Florida state
university for a data science degree. Wants to know, before registering, which courses
   will count and which prerequisites are still missing.
   
   
   ## User stories and acceptance checks
   ### Must-have
**US1: Upload my transcript.** As a transfer student, I want to upload my unofficial transcript PDF so that I don't retype my courses.
- The app accepts a PDF and shows its file name.
- A non-PDF file shows a clear error message.
- A PDF with no readable text shows "Couldn't read text from this file."

**US2: Add my target major's requirements.** As a transfer student, I want to upload or paste my target major's required courses so that the app knows what I need.
- Accepts a PDF or pasted text.
- Shows how many required courses were found.

**US3: See which courses transfer.** As a transfer student, I want my courses matched against the requirements so that I know where I stand.
- Matching is done in code using the SCNS rule: same prefix + same last 3 digits (first digit ignored).
- ENC 1101 matches ENC 2101 and is shown under "Transfers."
- Results appear in three groups: Transfers, Still needed, Check with an advisor.
- Courses with a W or F grade go to "Check with an advisor," not "Transfers."

**US4: See why.** As a transfer student, I want each result explained so that I can trust it and show my advisor.
- Every result shows the rule used, e.g. "ENC 1101 = ENC 2101 (same prefix + last 3 digits)."
- The code checks that each course code the AI extracted really appears in the uploaded text; if not, it's marked "Unverified."

### Should-have
**US5: Credit summary.** As a transfer student, I want totals so that I can plan my remaining semesters.
- Shows credits that apply and credits still needed, calculated in code.

**US6: Advisor reminder.** As a transfer student, I want to know the tool's limits so that I don't rely on it blindly.
- Every results page shows: "Confirm with your academic advisor before registering."

### Won't-have (this time)
- US7: Out-of-state or private institutions.
- US8: GPA or minimum-grade rules beyond W/F.
- US9: Multiple majors or saving results.

   
   ## Scope (in / out)
   **In scope**
- Florida public college to Florida public university transfers (SCNS rule applies).
- One transcript and one target major at a time.
- Results shown on screen.

**Out of scope**
- Out-of-state or private institutions (they don't follow SCNS).
- Official degree audits or registration decisions.
- Storing or saving uploaded files.
   
   
   ## Risks
   - **AI misreads a course code.** Mitigation: code verifies each extracted code appears in the uploaded text (US4), plus automated tests.
- **SCNS exceptions** (lab suffixes like C/L, special cases). Mitigation: suffix mismatches go to "Check with an advisor."
- **Privacy:** transcripts contain personal data. Mitigation: nothing is stored; the demo uses fake transcripts.
- **Requirement lists change each year.** Mitigation: the user supplies their current list instead of the app storing one.
- **API key exposure.** Mitigation: the key lives in `.env`, which `.gitignore` excludes.


## Test data
- Fake transcript A (clean), B (lab suffixes and a W grade), C (messy formatting).
- One fake requirements list for a data science major, with known correct answers for each transcript.

---
Drafted with Claude; reviewed and edited by Harsh. See docs/ai-log.md.