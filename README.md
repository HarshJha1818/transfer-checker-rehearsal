# Transfer Credit Gap Checker

> **Note:** Practice rehearsal by Harsh Jha. Code is not yet written; sections marked (TBD) fill in during the build.

**One-sentence pitch:** Upload your Florida college transcript and your target major's requirements, and see exactly which courses transfer, which prerequisites you still need, and why.

## The problem
Transfer students lose credits and time because matching a transcript against a new degree's requirements is done by hand. A 2017 federal GAO report estimated transfer students lost 43% of their credits on average (22% for public 2-year to public 4-year transfers). Florida's Statewide Course Numbering System (SCNS) makes equivalent courses transferable, but students still have to do the matching themselves. Full details: [PRD](docs/prd.md).

## How it works
1. Upload your transcript and your target major's requirements.
2. **AI (one call):** extracts the course codes from both documents.
3. **Plain code:** verifies each code appears in the uploaded text, then matches courses using the SCNS rule (same prefix + same last 3 digits).
4. Results appear in three groups: Transfers, Still needed, Check with an advisor, each with the rule that was applied.

## How to run it
```
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```
## Tech stack and frameworks
- Python 3.12
- Streamlit (web interface)
- Anthropic Claude API (course-code extraction)
- pytest (automated tests) and GitHub Actions (CI)

## Project documents
- [Product Requirements Document](docs/prd.md): problem, persona, user stories, scope, risks
- [Decision log](docs/decisions.md): key choices and why
- [Test plan](docs/test-plan.md): expected versus actual results
- [AI usage log](docs/ai-log.md): every use of AI, and what I changed
- [Design](docs/design.md): screen, data, AI call, and logic

## AI usage
- **AI used to build the app:** Claude helped draft the documents and will help draft code; I review, edit and test everything. Full record in the [AI usage log](docs/ai-log.md).
- **AI inside the app:** the Claude API does one job, extracting course codes. Matching is done in plain, tested code.

## Credits
- U.S. Government Accountability Office (GAO), 2017 report on college credit transfer.
- Florida Statewide Course Numbering System (SCNS).
- The PPCA framework from my father's go-to-market book, used to frame the AI's role (Perceive + Create, not Act).