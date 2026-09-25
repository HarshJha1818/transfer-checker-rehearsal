   # Decision log
   Format: Decision / Why / Rejected alternative

   ## D1: Repo lives in C:\Users\harsh\Projects, not OneDrive
   - Why: OneDrive sync interferes with Git and Python files.
   - Rejected: OneDrive Documents folder.

   ## D2: Use Python 3.12 via the `python` command
   - Why: Laptop has 3.12 and 3.14; 3.12 is widely supported by Streamlit and other libraries.
   - Rejected: `py` launcher (defaults to 3.14).

   ## D3: Rehearse with the real idea (transfer checker) in a practice-only repo
 - Why: Deep domain practice before Friday; MLH allows prior ideas but not reused code or materials.
 - Rejected: Lease decoder as the practice idea.

   ## D4: Course matching in code, not AI
 - Why: The SCNS rule is exact and testable; AI only extracts course codes.
 - Rejected: Asking the AI to decide equivalence.
 
   ## D5: Streamlit for the web page
  - Why: One Python file, file upload built in, free hosting; no HTML or JavaScript to learn.
  - Rejected: Flask or React (more code, more to learn in 36 hours).

  ## D6: Deploy early to Streamlit Community Cloud
- Why: Proves code → GitHub → live works at the start; every sync redeploys automatically.
- Rejected: Deploying only at the end (risk of surprises at hour 30).