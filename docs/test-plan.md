# Test plan and results
Expected results are written before the code. Actual and Pass? are filled in during each sprint's Test step.

| ID | Story | Type | Test | Input | Expected | Actual | Pass? |
|----|-------|------|------|-------|----------|--------|-------|
| T1 | US1 | Manual | Upload a valid PDF | transcript_A.pdf | File name shown | | |
| T2 | US1 | Manual | Upload a non-PDF | notes.docx | Clear error message | | |
| T3 | US1 | Manual | Upload a PDF with no text | scanned image PDF | "Couldn't read text from this file." | | |
| T4 | US2 | Manual | Paste requirements list | requirements_datascience.txt | Count of required courses shown | | |
| T5 | US3 | Auto | Same prefix + last 3 digits | ENC 1101 vs ENC 2101 | Transfers | | |
| T6 | US3 | Auto | Different last 3 digits | ENC 1101 vs ENC 1102 | No match (Still needed) | | |
| T7 | US3 | Auto | Different prefix | MAC 2311 vs MAT 2311 | No match | | |
| T8 | US3 | Auto | W grade | ENC 1101, grade W | Check with an advisor | | |
| T9 | US3 | Auto | Lab suffix mismatch | BSC 2010C vs BSC 2010 | Check with an advisor | | |
| T10 | US4 | Auto | Rule shown for each match | ENC 1101 vs ENC 2101 | "same prefix + last 3 digits" shown | | |
| T11 | US4 | Auto | AI returns a code not in the text | code XYZ 9999 | Marked "Unverified" | | |
| T12 | US5 | Auto | Credit totals | transcript_A + requirements list | Matches hand-calculated totals | | |
| T13 | US6 | Manual | Advisor reminder visible | any results page | Reminder text shown | Reminder shown | ✅ |
| T14 | US2 | Auto | AI returns invalid JSON | broken AI reply (simulated) | "Couldn't read courses. Try again." | | |
| T15 | — | Manual | API key missing | no .env file | "API key missing. Check your .env file." | | |
