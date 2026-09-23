   # Decision log
   Format: Decision / Why / Rejected alternative

   ## D1: Repo lives in C:\Users\harsh\Projects, not OneDrive
   - Why: OneDrive sync interferes with Git and Python files.
   - Rejected: OneDrive Documents folder.

   ## D2: Use Python 3.12 via the `python` command
   - Why: Laptop has 3.12 and 3.14; 3.12 is widely supported by Streamlit and other libraries.
   - Rejected: `py` launcher (defaults to 3.14).