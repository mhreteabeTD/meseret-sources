# Meseret sources

Everything a Meseret session needs to build a chapter, processed **once** so no session reads a PDF twice.
Start with `SOURCES.md` (the manifest). The rule: a session reads `source.md` / `bank.json`, never the PDF;
it opens a page image only when the transcription says `[check figure p.N]`.

## Layout
- `textbooks/g<grade>/<subject>/full.pdf` – the MoE book (source of truth, rarely opened)
- `textbooks/g<grade>/<subject>/u<n>/` – one unit: `source.md` (transcription), `figures/`, `pages/` (fallback), `meta.json`
- `exams/<exam>/<year>/<subject>/` – `paper.pdf`, `bank.json` (every question with answer + explanation), `figures/`
  - exams: `esslce` (Grade 12), `grade8` (regional), `grade6` (regional)
- `guides/` – teacher guides, revision books: same shape as a textbook unit
- `tools/` – scripts used to process a PDF (split per unit, render pages)

## Rules for a transcription (`source.md`)
1. Faithful to the book, in the book's language (Grades 1–6 Amharic). Fractions as `3/4`, mixed as `2 1/2`, negatives as `−3/4`.
2. Keep the book's structure and names: unit, section numbers, key words, Example 1.31, Exercise 1.6 Q2, page numbers as `(p.12)`.
3. Every exercise question gets `**Answer:**` and `**Why:**` with every step (LCM scaling, simplification, mixed↔improper, borrowing).
4. A figure that matters is cropped into `figures/` and referenced; one that doesn't is described in one line.
5. Anything unsure: `[review: …]` for a teacher; never guess silently.

## Rules for an exam bank (`bank.json`)
See `exams/BANK-SCHEMA.md`. Every question: text, options, answer, explanation, topic tags, the textbook section it tests,
difficulty 1–3, and `key: "paper" | "generated"`, `verified: true | false`. Where the paper's key disagrees with the worked
answer, keep both and set `review`.
