# Manifest

Source of truth for what is in this repo. **Read `catalog.json` to find the actual files** (logical path → real path(s), parts in page order).
Process once, then read the transcription: `raw` → `split` → `transcribed` → `verified` → `built`. Everything below is `raw` unless stated.

## Textbooks (student books)
| Grade | Subjects |
|---|---|
| 1 | amharic, english, maths (2 parts), science |
| 2 | amharic, english, maths (2 parts), science |
| 3 | amharic, english, maths (2 parts), science |
| 4 | amharic, english, maths (3 parts), science |
| 5 | amharic, english, maths (2 parts), science |
| 6 | amharic, english, maths (2 parts), science |
| 7 | amharic, citizenship, cte, english, it, maths (2 parts), science, social |
| 8 | amharic, citizenship, cte, english, it, maths, science, social |
| 9 | amharic, biology, citizenship, economics (2 editions), english, geography, history, hpe, it, maths, physics, pva |
| 10 | biology, citizenship, economics (2 editions), english, geography, hpe, it, maths, physics |
| 11 | agriculture, biology, chemistry, economics, english (2 parts), geography, history, it, maths (2 parts), physics |
| 12 | agriculture, biology (3 parts), chemistry, economics, geography, history, it, maths (2 parts), physics |

Built chapters: Grade 8 Maths U1, Grade 5 Maths U1.
Transcribed (`source.md` ready, no PDF needed): **Grade 12 Maths U1, U2**. Big books are cut into parts in page order (GitHub's 100 MB file limit).

## Teacher guides
| Grade | Subjects |
|---|---|
| 9 | biology, citizenship, economics, english, geography, history, hpe, it, maths, physics, pva |
| 10 | biology, citizenship, economics, english, geography, history, hpe, it, maths |

## Past exam books (with keys, to be checked)
| Book | parts | MB |
|---|---|---|
| Extreme Exam book Social Science 2010-2015 (1) | 5 | 399 |
| Extreme series Exam Book 2002-2010 | 5 | 248 |
| Key Exam Book 2001-2006 | 2 | 142 |
| Key Exam Book 2009_2015 | 2 | 103 |
| Solar Exam Book EUEE 2002-2006 | 5 | 333 |

## Reference / revision books (Extreme series etc.). Mark old vs new curriculum when each is read
| Book | parts | MB |
|---|---|---|
| EXTREME MATHS G12.pdf | 1 | 17 |
| Extreme Aptitude | 2 | 100 |
| Extreme Biology Grade 11_12 | 3 | 221 |
| Extreme Biology Grade 9_10 (1) | 8 | 591 |
| Extreme Chemistry  Grade 9_10 | 2 | 108 |
| Extreme Chemistry Grade11.pdf | 1 | 88 |
| Extreme Economics Grade 11 | 2 | 121 |
| Extreme English Grade 11_12.pdf | 1 | 10 |
| Extreme Geography Grade 11.pdf | 1 | 47 |
| Extreme Geography Grade 12.pdf | 1 | 55 |
| Extreme History Grade11.pdf | 1 | 47 |
| Extreme History Grade12.pdf | 1 | 60 |
| Extreme Mathematics Grade 10.pdf | 1 | 66 |
| Extreme Physics  Grade 9_10 | 2 | 116 |
| Extreme Physics Grade 10 New Curriculum.pdf | 1 | 14 |
| Extreme Physics Grade 11 New Curriculum.pdf | 1 | 43 |
| Extreme Physics Grade 9 New Curriculum.pdf | 1 | 18 |
| Extreme_Biology_Grade_11_12_New_Curriculum_Telegram__extremeseries | 4 | 231 |
| Extreme_Chemistry_Grade_11_12_New_Curriculum_Telegram_extremeseries | 3 | 152 |
| Extreme_Math_Grade_11_12_New_Curriculum_Telegram__Extremeseries | 3 | 176 |
| G11 Physics extreme series book | 4 | 219 |
| G11 maths extreme series book | 3 | 150 |
| G12 Maths extrene series book | 2 | 112 |
| G12 Physics extreme series book | 5 | 290 |
| Scholastic Aptitude Test Extreme Series.pdf | 1 | 24 |
| unsorted/Blue print grade 9 textbook.pdf | 1 | 65 |
| unsorted/blue print grade 10 textbook.pdf | 1 | 49 |
| unsorted/blue print teacher guide grade 10.pdf | 1 | 9 |
| unsorted/grade 10 sb.pdf | 1 | 1 |

## Other
| Item | parts | MB |
|---|---|---|
| curriculum/Chemistry 9-12_Curriculum_Revised By HST_2014 Bishoftu B.pdf | 1 | 3 |

## Known gaps
- Grades 5–6 Social Studies and Citizenship; Grades 1–6 Health & PE, Arts, Moral/Citizenship: not in the channel.
- Grades 11–12: only the 2023 new-curriculum student books so far; no teacher guides.
- `reference/unsorted/`: two Grade 9/10 "blue print" books and a "grade 10 sb" file: purpose to be checked.

## Storage note
Repo is ~4.3 GB (GitHub recommends staying under 5 GB). Do not add more PDFs here. Renaming big files by push fails with HTTP 500, so files stay where the Telegram fetcher put them (`inbox/`, `Grade-9-teachers-guide/`); always go through the catalog.
