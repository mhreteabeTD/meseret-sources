# bank.json

```json
{
  "exam": "esslce", "year": "2016", "subject": "maths", "lang": "en",
  "source": "paper.pdf", "key_in_paper": true, "questions": 60, "minutes": 150,
  "items": [
    {
      "n": 14, "page": 3,
      "text": "If 3/4 of a number is 18, the number is", "figure": null,
      "kind": "mcq", "opts": ["12", "24", "13.5", "54"], "answer": "24",
      "why": "3/4 × x = 18, so x = 18 ÷ 3/4 = 18 × 4/3 = 72/3 = 24.",
      "topics": ["fractions", "equations"], "maps_to": "g8-maths-u1/1.3.4",
      "level": 2, "key": "paper", "verified": true, "review": null
    }
  ]
}
```
- `kind`: `mcq` | `num` | `short` | `word` (word problem) | `proof`.
- `maps_to`: chapter id and section number in the app, or `null` if the topic has no chapter yet.
- `key`: `paper` (the paper's key, checked) or `generated` (worked by Claude).
- `review`: text for a teacher when the paper's key and the working disagree, or when unsure.
