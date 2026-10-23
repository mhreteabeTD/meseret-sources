# Grade 12 Mathematics (2023, new curriculum) — Unit 1 Sequences and Series

Source: `textbooks/g12/maths/full.pdf` (see catalog.json), book pages 1–60 (PDF page = book page + 10).
Transcribed once from page images; every exercise, activity and review question answered with full working and checked. `[review: …]` = for a teacher. `[added step: …]` = a step the book skips.

# Unit 1: Sequences and Series

Source: Ethiopian Grade 12 Mathematics Student Textbook (2023, new curriculum), book pages 1–30.

(p.1)

## UNIT 1 — SEQUENCES AND SERIES

### Unit Outcomes

By the end of this unit, you will be able to:

- Understand sequence and series.
- Compute terms of a sequence from a given rule.
- Use given terms to develop a formula that represent the sequence.
- Identify different types of sequences and series.
- Compute the partial and infinite sum of some sequences.
- Apply your understanding the knowledge of sequences and series to real-life problems.

### Unit Contents

- 1.1 Sequence
- 1.2 Arithmetic and Geometric Sequences
- 1.3 The Sigma Notation and Partial Sums
- 1.4 Infinite Series
- 1.5 Applications of Sequence and Series in Daily Life
- Summary
- Review Exercise

(p.2)

### Key Words

- arithmetic sequence
- finite sequence
- partial sums
- common difference
- general term
- sequence
- common ratio
- geometric sequence
- series
- convergent series
- infinite sequence
- terms of a sequence
- divergent series
- infinite series
- recursion formula

### Introduction

Mathematics has an enormous number of uses in our daily life. There is, in fact, no area of life that is not affected by mathematics. For instance, civil engineers use mathematics to determine how to best design new structures; economists use mathematics to describe and predict how the economy will react to certain changes; investors use mathematics to price certain types of shares or calculate how risky particular investments are; software developers use mathematics for many of the algorithms (such as Google searches and data security) that make programs useful. Mathematics is present everywhere from distance, time and money to art, design and music.

A sequence is an arrangement of numbers in a definite order according to some rule. Sequences and Series play an important role in various aspects of our lives. They help us to predict, evaluate and monitor the outcome of a situation or event and help us in decision making.

## 1.1 Sequences

### Activity 1.1

1. People wants to plant trees in a certain pattern in the green area of a community like 20 plants in the first row, 34 plants in the second row and 48 plants in the third row, and so on. How many trees people will plant in the 5th and 6th row?

**Answer:** 5th row: 76 trees; 6th row: 90 trees.
**Why:**
- Differences between rows: 34 − 20 = 14 and 48 − 34 = 14, so each row has 14 more plants than the row before.
- 4th row: 48 + 14 = 62
- 5th row: 62 + 14 = 76
- 6th row: 76 + 14 = 90
- Check with a formula: a_n = 20 + (n − 1)×14. a_5 = 20 + 4×14 = 20 + 56 = 76 ✓; a_6 = 20 + 5×14 = 20 + 70 = 90 ✓

2. Find the next two terms of the following sequence.

a. {50, 47, 44, 41, …}

**Answer:** 38, 35
**Why:**
- Differences: 47 − 50 = −3, 44 − 47 = −3, 41 − 44 = −3, so subtract 3 each time.
- 41 − 3 = 38
- 38 − 3 = 35
- Check: a_n = 50 + (n − 1)(−3) = 53 − 3n; a_5 = 53 − 15 = 38 ✓, a_6 = 53 − 18 = 35 ✓

b. {2, 12, 22, 32, …}

**Answer:** 42, 52
**Why:**
- Differences: 12 − 2 = 10, 22 − 12 = 10, 32 − 22 = 10, so add 10 each time.
- 32 + 10 = 42
- 42 + 10 = 52
- Check: a_n = 2 + (n − 1)×10 = 10n − 8; a_5 = 50 − 8 = 42 ✓, a_6 = 60 − 8 = 52 ✓

(p.3)

### Definition 1.1

A sequence is a function whose domain is the collection of all integers greater than or equal to a given integer m (usually 0 or 1). A sequence is usually denoted by a_n. The functional values: a_1, a_2, a_3, …, a_n, … are called the terms of a sequence, and a_n is called the **general term**, or the nth term of the sequence. There are two types of sequences depending on its last term.

**Finite Sequence:** A sequence that has a last term. The domain of a finite sequence is 1, 2, 3, …, n.

**Infinite sequence:** A sequence that does not have a last term. The domain of an infinite sequence is the set of natural numbers (ℕ).

### Example 1

List the first five terms of each of the sequences whose general terms are given below where n is a positive integer.

(a) a_n = 2n − 1  (b) a_n = (−1/3)^(n−1)  (c) a_n = 1/n

**Solution**

(a) a_n = 2n − 1:
a_1 = 2(1) − 1 = 1, a_2 = 2(2) − 1 = 3, a_3 = 2(3) − 1 = 5,
a_4 = 2(4) − 1 = 7, a_5 = 2(5) − 1 = 9.

Therefore, the first five terms are 1, 3, 5, 7 and 9.

(b) a_n = (−1/3)^(n−1)
a_1 = (−1/3)^(1−1) = 1, a_2 = (−1/3)^(2−1) = −1/3, a_3 = (−1/3)^(3−1) = 1/9,
a_4 = (−1/3)^(4−1) = −1/27, a_5 = (−1/3)^(5−1) = 1/81.

[added step: (−1/3)⁰ = 1 because any non-zero number to the power 0 is 1; (−1/3)² = (−1)²/3² = 1/9; (−1/3)³ = (−1)³/3³ = −1/27; (−1/3)⁴ = (−1)⁴/3⁴ = 1/81. An even power of a negative number is positive, an odd power is negative.]

(p.4)

Therefore, the first five terms are 1, −1/3, 1/9, −1/27 and 1/81.

(c) a_n = 1/n:
a_1 = 1/1 = 1, a_2 = 1/2, a_3 = 1/3, a_4 = 1/4, a_5 = 1/5.

Therefore, the first five terms are 1, 1/2, 1/3, 1/4 and 1/5.

### Example 2

Draw the graph of sequence a_n = 2n + 1.

**Solution**

Make a table with n and a_n, as follows. Then plot each ordered pair (n, a_n).

| n | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| a_n | 3 | 5 | 7 | 9 | 11 |

[added step: a_1 = 2(1) + 1 = 3, a_2 = 2(2) + 1 = 5, a_3 = 2(3) + 1 = 7, a_4 = 2(4) + 1 = 9, a_5 = 2(5) + 1 = 11.]

[figure: Figure 1.1 — isolated points (not joined) plotted on a grid, n on the horizontal axis from 0 to 6, a_n on the vertical axis from 0 to 12; points at (1, 3), (2, 5), (3, 7), (4, 9), (5, 11), lying on a straight line.]

**Note**

From the Figure 1.1, we can observe that the graph of the sequence follows the pattern of a linear equation.

(p.5)

### Exercise 1.1

1. List the first five terms of each of the sequences whose general terms are given below where n is a positive integer:

a. a_n = 2n

**Answer:** 2, 4, 6, 8, 10
**Why:**
- a_1 = 2(1) = 2
- a_2 = 2(2) = 4
- a_3 = 2(3) = 6
- a_4 = 2(4) = 8
- a_5 = 2(5) = 10
- Check: each term is 2 more than the one before (even numbers), as expected for 2n. ✓

b. a_n = (1/2)^(n−1)

**Answer:** 1, 1/2, 1/4, 1/8, 1/16
**Why:**
- a_1 = (1/2)^(1−1) = (1/2)⁰ = 1
- a_2 = (1/2)^(2−1) = (1/2)¹ = 1/2
- a_3 = (1/2)^(3−1) = (1/2)² = 1²/2² = 1/4
- a_4 = (1/2)^(4−1) = (1/2)³ = 1³/2³ = 1/8
- a_5 = (1/2)^(5−1) = (1/2)⁴ = 1⁴/2⁴ = 1/16
- Check: each term is half the one before: 1 × 1/2 = 1/2, 1/2 × 1/2 = 1/4, 1/4 × 1/2 = 1/8, 1/8 × 1/2 = 1/16 ✓

c. a_n = n/(n+1)

**Answer:** 1/2, 2/3, 3/4, 4/5, 5/6
**Why:**
- a_1 = 1/(1 + 1) = 1/2
- a_2 = 2/(2 + 1) = 2/3
- a_3 = 3/(3 + 1) = 3/4
- a_4 = 4/(4 + 1) = 4/5
- a_5 = 5/(5 + 1) = 5/6
- Check: each numerator is n and each denominator is one more than the numerator ✓

d. a_n = n³

**Answer:** 1, 8, 27, 64, 125
**Why:**
- a_1 = 1³ = 1 × 1 × 1 = 1
- a_2 = 2³ = 2 × 2 × 2 = 8
- a_3 = 3³ = 3 × 3 × 3 = 27
- a_4 = 4³ = 4 × 4 × 4 = 64
- a_5 = 5³ = 5 × 5 × 5 = 125
- Check: 64 = 8 × 8 and 125 = 25 × 5 ✓

2. Draw the graph of the following sequences and observe the pattern of the sequence.

a. a_n = 3n − 1

**Answer:** Points (1, 2), (2, 5), (3, 8), (4, 11), (5, 14); they lie on a straight line (linear pattern), rising by 3 each step.
**Why:**
- a_1 = 3(1) − 1 = 2
- a_2 = 3(2) − 1 = 5
- a_3 = 3(3) − 1 = 8
- a_4 = 3(4) − 1 = 11
- a_5 = 3(5) − 1 = 14
- Table: n = 1, 2, 3, 4, 5 → a_n = 2, 5, 8, 11, 14
- Plot each ordered pair (n, a_n) as a separate dot; do not join them, because n takes only whole-number values.
- Pattern: each step to the right goes up by 3 (5 − 2 = 3, 8 − 5 = 3, …), so the dots lie on the line y = 3x − 1, like Figure 1.1.

b. a_n = 1/n

**Answer:** Points (1, 1), (2, 1/2), (3, 1/3), (4, 1/4), (5, 1/5); the terms decrease and get closer and closer to 0 but never reach it.
**Why:**
- a_1 = 1/1 = 1
- a_2 = 1/2 = 0.5
- a_3 = 1/3 ≈ 0.33
- a_4 = 1/4 = 0.25
- a_5 = 1/5 = 0.2
- Plot each ordered pair (n, a_n) as a separate dot.
- Pattern: the dots fall quickly at first and then flatten out, approaching the n-axis (a_n → 0 as n gets large); every term stays positive.

c. a_n = (−1)ⁿ

**Answer:** Points (1, −1), (2, 1), (3, −1), (4, 1), (5, −1); the terms alternate between −1 and 1.
**Why:**
- a_1 = (−1)¹ = −1
- a_2 = (−1)² = (−1)(−1) = 1
- a_3 = (−1)³ = (−1)²(−1) = 1 × (−1) = −1
- a_4 = (−1)⁴ = 1
- a_5 = (−1)⁵ = −1
- Rule used: an odd power of −1 is −1, an even power of −1 is 1.
- Pattern: the dots jump between the horizontal lines a_n = −1 (odd n) and a_n = 1 (even n).

3. Bontu's uncle gave 130 Ethiopian birr to her in January, in the next month she saves money and has 210 Ethiopian birr and in the third month she has 290 Ethiopian birr. How much money will she have in the fourth, fifth, sixth and seventh month respectively.

**Answer:** 370 birr, 450 birr, 530 birr and 610 birr.
**Why:**
- Increase each month: 210 − 130 = 80 and 290 − 210 = 80, so she adds 80 birr each month.
- 4th month: 290 + 80 = 370
- 5th month: 370 + 80 = 450
- 6th month: 450 + 80 = 530
- 7th month: 530 + 80 = 610
- Check with a formula: a_n = 130 + (n − 1)×80. a_7 = 130 + 6×80 = 130 + 480 = 610 ✓; a_4 = 130 + 3×80 = 130 + 240 = 370 ✓

### Fibonacci and Mulatu sequences

### Activity 1.2

Two squares with a side length of 1 are arranged side by side. The rectangle made has a vertical length of 1 and a horizontal length of 2. Place a square with a side length of 2 next to it. Then, the rectangle made has vertical length is 3, horizontal length is 2. After this, arrange a square with a side length of 3, a square with a length of 5, and a square with a length of 8 to make a large rectangle.

[figure: Figure 1.2 — a large rectangle built from squares of side 1, 1, 2, 3, 5 and 8: the 8-square fills the left side; on the right, the 5-square is at the bottom, and above it are the 3-square, the 2-square and the two 1-squares. The whole rectangle is 8 high and 8 + 5 = 13 wide.]

Based on Figure 1.2 above, answer the following questions:

a. What is the sum of the area of all the inner squares?

**Answer:** 104 square units
**Why:**
- Area of a square = side × side.
- Areas: 1² = 1, 1² = 1, 2² = 4, 3² = 9, 5² = 25, 8² = 64
- Sum: 1 + 1 = 2; 2 + 4 = 6; 6 + 9 = 15; 15 + 25 = 40; 40 + 64 = 104

b. What is the area of the outer rectangle?

**Answer:** 104 square units
**Why:**
- Height of the outer rectangle = side of the largest square = 8 (also 5 + 3 = 8 on the right side).
- Width of the outer rectangle = 8 + 5 = 13.
- Area = length × width = 13 × 8 = 104

c. What is the relation between your answer to parts a and b?

**Answer:** They are equal: 1² + 1² + 2² + 3² + 5² + 8² = 8 × 13 = 104.
**Why:**
- The inner squares exactly fill the outer rectangle with no gaps or overlaps, so the total area must be the same.
- The side lengths 1, 1, 2, 3, 5, 8 are Fibonacci numbers and 13 = 5 + 8 is the next one; the sum of the squares of the Fibonacci numbers equals the product of the last one and the next one.
- Check on a smaller case: 1² + 1² + 2² = 6 = 2 × 3 ✓

(p.6)

### Fibonacci's sequence

#### HISTORICAL NOTE — Leonardo Fibonacci (circa 1170, 1240)

Italian mathematician Leonardo Fibonacci made advances in number theory and algebra. Fibonacci, also called Leonardo of Pisa, produced numbers that have many interesting properties such as the birth rates of rabbits and the spiral growth of leaves on some trees.

He is especially known for his work on series of numbers, including the Fibonacci series. Each number in a Fibonacci series is equal to the sum of the two numbers that came before it. Fibonacci sequence arose when he was trying to solve a problem of the following kind concerning the breeding of rabbits.

*"Suppose that rabbits live forever and that every month each pair produces a new pair which becomes productive at the age of two months. If we start with one new born pair, how many pairs of rabbits will we have in the nth month?"*

[figure: portrait of Leonardo Fibonacci]

Fibonacci sequence is defined as:

F_n = 1 if n = 0
F_n = 1 if n = 1
F_n = F_(n−1) + F_(n−2) if n ≥ 2.

[figure: Figure 1.3 — rabbit family tree; the number of pairs in successive months is 1, 1, 2, 3, 5.]

(p.7)

### Example

List the first eight terms of the Fibonacci sequence and draw its graph.

**Solution**

Make a table with n and a_n, as follows. Then plot each ordered pair (n, F_n).

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| F_n | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55 |

[added step: F_2 = F_1 + F_0 = 1 + 1 = 2; F_3 = F_2 + F_1 = 2 + 1 = 3; F_4 = 3 + 2 = 5; F_5 = 5 + 3 = 8; F_6 = 8 + 5 = 13; F_7 = 13 + 8 = 21; F_8 = 21 + 13 = 34; F_9 = 34 + 21 = 55.]

[review: the question asks for the first eight terms (1, 1, 2, 3, 5, 8, 13, 21 = F_0 to F_7), but the book's table and graph show ten terms (F_0 to F_9). Also the text says "a table with n and a_n" while the table uses F_n. The values themselves are correct.]

So, the graph becomes

[figure: Figure 1.4 — isolated points (n, F_n) for n = 0 to 9 on a grid, n-axis 0 to 10, F_n-axis 0 to 60: (0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55). The points rise slowly at first then more and more steeply (not a straight line).]

(p.8)

### Mulatu sequence

#### HISTORICAL NOTE — Mulatu Lemma

Professor Mulatu Lemma is an Ethiopian Mathematician. He pursued an education through a university in Ethiopia, earning a Bachelor of Science in 1977 from Addis Ababa University. He continued his studies at the aforementioned university and obtained a Master of Science in applied mathematics in 1982. Following these accomplishments, he was enrolled at Kent State University, where he pursued a Master of Arts in pure mathematics in 1993. Prof. Mulatu completed his academic journey with a Doctor of Philosophy from Kent State University in 1994. In 2011, he introduced the Mulatu's Number (named after him) to the mathematical community and to the world.

[figure: photograph of Professor Mulatu Lemma]

Professor Mulatu introduced a sequence of the form:

M_n = 4 if n = 0
M_n = 1 if n = 1
M_n = M_(n−1) + M_(n−2) if n ≥ 2.

**Recursive Sequence**

A sequence that relates to the general term a_n of a sequence where one or more of the terms that comes before it is said to be defined recursively. The domain of recursive sequence can be the set of whole numbers. For Example, Mulatu and Fibonacci sequences are some of the examples of recursion formula.

### Exercise 1.2

1. Find the 12th term of the Fibonacci's sequence {1, 1, 2, 3, 5, 8, …}.

**Answer:** 144
**Why:**
- Rule: each term is the sum of the two terms before it.
- 1st = 1, 2nd = 1, 3rd = 2, 4th = 3, 5th = 5, 6th = 8 (given)
- 7th = 5 + 8 = 13
- 8th = 8 + 13 = 21
- 9th = 13 + 21 = 34
- 10th = 21 + 34 = 55
- 11th = 34 + 55 = 89
- 12th = 55 + 89 = 144
- Note: the 12th term counted from the start of the list is F_11 in the book's numbering (which starts at F_0).
- Check: the table on p.7 gives F_9 = 55 as the 10th listed term, which agrees with the 10th term above ✓

2. List the first eight terms of Mulatu's sequences and draw its graph.

**Answer:** 4, 1, 5, 6, 11, 17, 28, 45 — graph: isolated points (0, 4), (1, 1), (2, 5), (3, 6), (4, 11), (5, 17), (6, 28), (7, 45).
**Why:**
- M_0 = 4 (given)
- M_1 = 1 (given)
- M_2 = M_1 + M_0 = 1 + 4 = 5
- M_3 = M_2 + M_1 = 5 + 1 = 6
- M_4 = M_3 + M_2 = 6 + 5 = 11
- M_5 = M_4 + M_3 = 11 + 6 = 17
- M_6 = M_5 + M_4 = 17 + 11 = 28
- M_7 = M_6 + M_5 = 28 + 17 = 45
- Graph: plot each ordered pair (n, M_n) as a separate dot. After the dip from 4 to 1, the points rise faster and faster, like the Fibonacci graph in Figure 1.4.
- Check by subtraction (going backwards): 45 − 28 = 17 ✓, 28 − 17 = 11 ✓, 17 − 11 = 6 ✓, 11 − 6 = 5 ✓, 6 − 5 = 1 ✓, 5 − 1 = 4 ✓

(p.9)

## 1.2 Arithmetic and Geometric Sequences

### 1.2.1 Arithmetic Sequences

### Activity 1.3

Find the difference between consecutive terms for each of the following sequences.

a. 3, 7, 11, 15, …

**Answer:** 4
**Why:**
- 7 − 3 = 4
- 11 − 7 = 4
- 15 − 11 = 4
- The difference is the same each time: 4.

b. 3, −1, −5, −9, …

**Answer:** −4
**Why:**
- −1 − 3 = −4
- −5 − (−1) = −5 + 1 = −4
- −9 − (−5) = −9 + 5 = −4
- The difference is the same each time: −4.

c. 2, 7/3, 8/3, 3, …

**Answer:** 1/3
**Why:**
- Write 2 and 3 with denominator 3: 2 = (2×3)/(1×3) = 6/3 and 3 = (3×3)/(1×3) = 9/3.
- 7/3 − 6/3 = 1/3
- 8/3 − 7/3 = 1/3
- 9/3 − 8/3 = 1/3
- The difference is the same each time: 1/3.

### Definition 1.2

**Arithmetic sequence or arithmetic progression** is a sequence in which each term except the first is obtained by adding a fixed number (positive or negative) to the preceding term. The fixed number is called common difference of the sequence.

### Example 1

For the following arithmetic sequence 2, 5, 8, 11, 14, …, what is the first term, third term and common difference? Find the 6th term.

**Solution**

2 → 5 → 8 → 11 → 14 (+3 each step)

[figure: arrows between consecutive terms 2, 5, 8, 11, 14, each labelled +3]

1st term: 2, 3rd term: 8

The common difference is 3.

[added step: 5 − 2 = 3, 8 − 5 = 3, 11 − 8 = 3, 14 − 11 = 3.]

6th term: 5th term + 3 = 14 + 3 = 17.

### Example 2

Given that the 1st term of an arithmetic sequence is 10, and the common difference is −4, find the terms from 2nd to 5th term.

(p.10)

**Solution**

2nd term: 1st term + (−4) = 10 + (−4) = 6.
3rd term: 2nd term + (−4) = 6 + (−4) = 2.
4th term: 3rd term + (−4) = 2 + (−4) = −2.
5th term: 4th term + (−4) = −2 + (−4) = −6.

Therefore, the terms from 2nd to 5th term are 6, 2, −2, −6.

### Exercise 1.3

1. For the following arithmetic sequences, what are the first term, third term and common difference? Find the 6th term.

a. {3, 5, 7, 9, 11, …}

**Answer:** first term 3, third term 7, common difference 2, 6th term 13.
**Why:**
- 1st term: 3
- 3rd term: 7
- Common difference: 5 − 3 = 2 (also 7 − 5 = 2, 9 − 7 = 2, 11 − 9 = 2)
- 6th term = 5th term + d = 11 + 2 = 13
- Check: A_6 = A_1 + 5d = 3 + 5×2 = 3 + 10 = 13 ✓

b. {9, 6, 3, 0, −3, …}

**Answer:** first term 9, third term 3, common difference −3, 6th term −6.
**Why:**
- 1st term: 9
- 3rd term: 3
- Common difference: 6 − 9 = −3 (also 3 − 6 = −3, 0 − 3 = −3, −3 − 0 = −3)
- 6th term = 5th term + d = −3 + (−3) = −6
- Check: A_6 = A_1 + 5d = 9 + 5×(−3) = 9 − 15 = −6 ✓

2. Find the terms from 2nd to 5th of an arithmetic sequence when the

a. 1st term is 1, and the common difference is 5.

**Answer:** 6, 11, 16, 21
**Why:**
- 2nd term: 1 + 5 = 6
- 3rd term: 6 + 5 = 11
- 4th term: 11 + 5 = 16
- 5th term: 16 + 5 = 21
- Check: A_5 = 1 + 4×5 = 1 + 20 = 21 ✓

b. 1st term is 2, and the common difference is −1/2.

**Answer:** 3/2, 1, 1/2, 0
**Why:**
- Write 2 with denominator 2: 2 = (2×2)/(1×2) = 4/2.
- 2nd term: 4/2 + (−1/2) = (4 − 1)/2 = 3/2
- 3rd term: 3/2 + (−1/2) = (3 − 1)/2 = 2/2 = 1
- 4th term: 1 + (−1/2) = 2/2 − 1/2 = 1/2
- 5th term: 1/2 + (−1/2) = 0
- Check: A_5 = 2 + 4×(−1/2) = 2 − 4/2 = 2 − 2 = 0 ✓

### General term of arithmetic sequence

From the Activity 1.3, (a), 3, 7, 11, 15, 19, … the first term is 3, and the common difference is 4. Let the common difference be d, and let A_n be the nth term of the sequence, then,

A_1 = 3
A_2 = 3 + 4 = A_1 + d
A_3 = 3 + 4 + 4 = A_1 + 2d
A_4 = 3 + 4 + 4 + 4 = A_1 + 3d
…
A_n = 3 + 4 + 4 + 4 + … + 4 = A_1 + (n − 1)d

Suppose A_n : A_1, A_2, A_3, A_4, A_5, A_6, … is an arithmetic sequence.

A_2 = A_1 + d
A_3 = A_2 + d = A_1 + d + d = A_1 + 2d
A_4 = A_3 + d = A_1 + 2d + d = A_1 + 3d

(p.11)

A_5 = A_4 + d = A_1 + 3d + d = A_1 + 4d
A_6 = A_5 + d = A_1 + 4d + d = A_1 + 5d
⋮
A_n = A_(n−1) + d = A_1 + (n − 2)d + d = A_1 + (n − 1)d

Thus, the following formula is derived:

### Theorem 1.1

If A_n is an arithmetic sequence with the first term A_1 and a common difference d, then the nth term of the sequence is given by A_n = A_1 + (n − 1)d.

### Example 1

Find the general term of the sequence A_n, when the first term is 5, and the common difference is 4.

**Solution**

The given sequence is arithmetic sequence with A_1 = 5 and d = 4.

From the theorem 1.1, we have the formula A_n = A_1 + (n − 1)d. So,

A_n = A_1 + (n − 1)d = 5 + (n − 1)(4) = 5 + 4n − 4 = 4n + 1.

### Example 2

What is the 31st term of the sequence 1, 4, 7, 10, …?

**Solution**

The given sequence is arithmetic sequence with A_1 = 1 and d = 3

[added step: d = 4 − 1 = 3, also 7 − 4 = 3 and 10 − 7 = 3.]

A_n = A_1 + (n − 1)d = 1 + 3(n − 1) = 3n − 2.

[added step: 1 + 3(n − 1) = 1 + 3n − 3 = 3n − 2.]

Then,

A_31 = 3(31) − 2 = 93 − 2 = 91.

(p.12)

### Exercise 1.4

1. Find the general term of the sequence A_n, when

a. A_1 = 2, d = 3.

**Answer:** A_n = 3n − 1
**Why:**
- Theorem 1.1: A_n = A_1 + (n − 1)d
- Substitute: A_n = 2 + (n − 1)(3)
- Expand: A_n = 2 + 3n − 3
- Collect: A_n = 3n − 1
- Check: A_1 = 3(1) − 1 = 2 ✓; A_2 = 3(2) − 1 = 5 = 2 + 3 ✓

b. A_1 = 10, d = −5.

**Answer:** A_n = 15 − 5n
**Why:**
- Theorem 1.1: A_n = A_1 + (n − 1)d
- Substitute: A_n = 10 + (n − 1)(−5)
- Expand: A_n = 10 − 5n + 5
- Collect: A_n = 15 − 5n
- Check: A_1 = 15 − 5 = 10 ✓; A_2 = 15 − 10 = 5 = 10 + (−5) ✓

2. What is the 10th term of the sequence, 10, 6, 2, −2, …?

**Answer:** −26
**Why:**
- A_1 = 10; d = 6 − 10 = −4 (also 2 − 6 = −4, −2 − 2 = −4)
- A_10 = A_1 + (10 − 1)d = 10 + 9(−4)
- = 10 − 36
- = −26
- Check by listing: 10, 6, 2, −2, −6, −10, −14, −18, −22, −26 → the 10th is −26 ✓

### Further on arithmetic sequences

### Example 1

When the third term is 10 and the sixth term is 1,

a. Find the general term of sequence A_n.

b. Find A_8.

**Solution**

a. Applying arithmetic sequence formula and substituting existing values yields:

A_3 = A_1 + (3 − 1)d,  10 = A_1 + 2d
A_6 = A_1 + (6 − 1)d,  1 = A_1 + 5d

{ A_1 + 2d = 10
{ A_1 + 5d = 1

Subtracting these two equations,

3d = −9 ⇒ d = −3, A_1 + 2d = 10, A_1 + 2(−3) = 10, A_1 = 10 + 6 = 16.

[added step: (A_1 + 5d) − (A_1 + 2d) = 1 − 10, so 3d = −9 and d = −9/3 = −3.]

Therefore, the general term becomes

A_n = A_1 + (n − 1)d = 16 + (n − 1)(−3) = 16 − 3n + 3 = 19 − 3n.

b. A_n = 19 − 3n ⇒ A_8 = 19 − 3(8) = 19 − 24 = −5.

### Example 2

Determine whether or not the sequences with the following general terms are arithmetic.

a. a_n = 3n − 2  b. a_n = 3n² − 2

(p.13)

**Solution**

a. To solve such types of problem, we have to show the difference between successive terms is constant.

a_n = 3n − 2
a_(n+1) = 3(n + 1) − 2 = 3n + 1
a_(n+1) − a_n = 3n + 1 − (3n − 2) = 3.

Since, the difference between successive term is constant, it arithmetic sequence

b. a_n = 3n² − 2

a_n = 3n² − 2
a_(n+1) = 3(n + 1)² − 2 = 3(n² + 2n + 1) − 2 = 3n² + 6n + 1
a_(n+1) − a_n = 3n² + 6n + 1 − (3n² − 2) = 6n + 3.

Since, the difference between successive terms is not constant, it is not arithmetic sequence.

[added step: the difference 6n + 3 changes with n: for n = 1 it is 9 (a_1 = 1, a_2 = 10), for n = 2 it is 15 (a_3 = 25).]

### Exercise 1.5

1. Find the general term of the arithmetic sequence A_n, when

a. A_4 = 15, A_8 = 27.

**Answer:** A_n = 3n + 3
**Why:**
- A_4 = A_1 + 3d, so A_1 + 3d = 15
- A_8 = A_1 + 7d, so A_1 + 7d = 27
- Subtract the first equation from the second: (A_1 + 7d) − (A_1 + 3d) = 27 − 15
- 4d = 12
- d = 12/4 = 3
- Substitute into A_1 + 3d = 15: A_1 + 3(3) = 15, A_1 + 9 = 15, A_1 = 6
- A_n = A_1 + (n − 1)d = 6 + (n − 1)(3) = 6 + 3n − 3 = 3n + 3
- Check: A_4 = 3(4) + 3 = 15 ✓; A_8 = 3(8) + 3 = 27 ✓

b. A_5 = 20, A_10 = 0.

**Answer:** A_n = 40 − 4n
**Why:**
- A_5 = A_1 + 4d, so A_1 + 4d = 20
- A_10 = A_1 + 9d, so A_1 + 9d = 0
- Subtract: (A_1 + 9d) − (A_1 + 4d) = 0 − 20
- 5d = −20
- d = −20/5 = −4
- Substitute: A_1 + 4(−4) = 20, A_1 − 16 = 20, A_1 = 36
- A_n = 36 + (n − 1)(−4) = 36 − 4n + 4 = 40 − 4n
- Check: A_5 = 40 − 20 = 20 ✓; A_10 = 40 − 40 = 0 ✓

2. Given arithmetic sequence with A_2 = 3 and A_5 = 24. Find A_n and A_11.

**Answer:** A_n = 7n − 11; A_11 = 66
**Why:**
- A_2 = A_1 + d, so A_1 + d = 3
- A_5 = A_1 + 4d, so A_1 + 4d = 24
- Subtract: 3d = 24 − 3 = 21
- d = 21/3 = 7
- A_1 + 7 = 3, so A_1 = 3 − 7 = −4
- A_n = −4 + (n − 1)(7) = −4 + 7n − 7 = 7n − 11
- A_11 = 7(11) − 11 = 77 − 11 = 66
- Check: A_2 = 14 − 11 = 3 ✓; A_5 = 35 − 11 = 24 ✓; also A_11 = A_5 + 6d = 24 + 42 = 66 ✓

3. Determine whether or not the sequences with the following general terms are arithmetic.

a. a_n = 7n − 3

**Answer:** Arithmetic (common difference 7).
**Why:**
- a_(n+1) = 7(n + 1) − 3 = 7n + 7 − 3 = 7n + 4
- a_(n+1) − a_n = 7n + 4 − (7n − 3) = 7n + 4 − 7n + 3 = 7
- The difference is constant (7), so it is arithmetic.
- Check: terms 4, 11, 18, 25 differ by 7 ✓

b. a_n = 5n − 3

**Answer:** Arithmetic (common difference 5).
**Why:**
- a_(n+1) = 5(n + 1) − 3 = 5n + 5 − 3 = 5n + 2
- a_(n+1) − a_n = 5n + 2 − (5n − 3) = 5n + 2 − 5n + 3 = 5
- The difference is constant (5), so it is arithmetic.
- Check: terms 2, 7, 12, 17 differ by 5 ✓

c. a_n = n² + n + 1

**Answer:** Not arithmetic.
**Why:**
- a_(n+1) = (n + 1)² + (n + 1) + 1 = n² + 2n + 1 + n + 1 + 1 = n² + 3n + 3
- a_(n+1) − a_n = n² + 3n + 3 − (n² + n + 1) = 2n + 2
- The difference depends on n, so it is not constant; not arithmetic.
- Check: terms 3, 7, 13, 21; differences 4, 6, 8 — not equal ✓

d. a_n = 3ⁿ

**Answer:** Not arithmetic.
**Why:**
- a_(n+1) = 3^(n+1) = 3 × 3ⁿ
- a_(n+1) − a_n = 3 × 3ⁿ − 3ⁿ = 3ⁿ(3 − 1) = 2 × 3ⁿ
- The difference depends on n, so it is not constant; not arithmetic.
- Check: terms 3, 9, 27, 81; differences 6, 18, 54 — not equal ✓ (it is geometric, ratio 3)

(p.14)

### Arithmetic mean between two numbers

The term(s) of arithmetic sequence that lie between two given terms are called the arithmetic mean.

### Example 1

Given that 1, x, 8 is an arithmetic sequence, find x.

**Solution**

Since it is arithmetic sequence, the difference between two consecutive terms is constant.

x − 1 = 8 − x
2x = 9
x = 9/2

[added step: add x to both sides: x + x − 1 = 8, so 2x − 1 = 8; add 1 to both sides: 2x = 9; divide by 2: x = 9/2. Check: 9/2 − 1 = 7/2 and 8 − 9/2 = 16/2 − 9/2 = 7/2, equal ✓]

### Example 2

The first and sixth terms of an arithmetic sequence are 4 and 29. Find the values of terms 2, 3, 4 and 5.

**Solution**

Let the four terms be A_2, A_3, A_4, A_5.

So, 4, A_2, A_3, A_4, A_5, 29 form an arithmetic sequence. Then, A_n = A_1 + (n − 1)d.

A_1 = 4
A_6 = A_1 + (6 − 1)d
29 = 4 + 5d
d = 5

[added step: 29 − 4 = 5d, so 25 = 5d and d = 25/5 = 5.]

Thus, A_n = 4 + (n − 1)5 = 5n − 1

[added step: 4 + 5n − 5 = 5n − 1.]

A_2 = 4 + 5 × 1 = 9
A_3 = 4 + 5 × 2 = 14
A_4 = 4 + 5 × 3 = 19
A_5 = 4 + 5 × 4 = 24.

(p.15)

### Exercise 1.6

1. Given that the sequence 3, x, 7 is an arithmetic sequence, find x.

**Answer:** x = 5
**Why:**
- In an arithmetic sequence consecutive differences are equal: x − 3 = 7 − x
- Add x to both sides: 2x − 3 = 7
- Add 3 to both sides: 2x = 10
- Divide by 2: x = 5
- Check: 5 − 3 = 2 and 7 − 5 = 2 ✓ (also x is the average (3 + 7)/2 = 10/2 = 5 ✓)

2. Given that the sequence 1/12, 1/x, 1/6 is an arithmetic sequence, find x.

**Answer:** x = 8
**Why:**
- Equal differences: 1/x − 1/12 = 1/6 − 1/x
- Add 1/x to both sides and add 1/12 to both sides: 2/x = 1/6 + 1/12
- Common denominator 12: 1/6 = (1×2)/(6×2) = 2/12, so 1/6 + 1/12 = 2/12 + 1/12 = 3/12
- Simplify 3/12 by the common factor 3: (3÷3)/(12÷3) = 1/4
- So 2/x = 1/4
- Cross-multiply: x × 1 = 2 × 4, so x = 8
- Check: 1/8 − 1/12 = 3/24 − 2/24 = 1/24 and 1/6 − 1/8 = 4/24 − 3/24 = 1/24, equal ✓

3. Find the arithmetic mean of 4 and 14.

**Answer:** 9
**Why:**
- The arithmetic mean m makes 4, m, 14 an arithmetic sequence: m − 4 = 14 − m
- 2m = 14 + 4 = 18
- m = 18/2 = 9
- Check: 9 − 4 = 5 and 14 − 9 = 5 ✓

4. Insert four arithmetic means between 4 and 14 to create an arithmetic sequence.

**Answer:** 6, 8, 10, 12 (sequence 4, 6, 8, 10, 12, 14)
**Why:**
- With four means, 4 is A_1 and 14 is A_6 (4 + 2 = 6 terms in all).
- A_6 = A_1 + 5d, so 14 = 4 + 5d
- 5d = 14 − 4 = 10
- d = 10/5 = 2
- A_2 = 4 + 2 = 6, A_3 = 6 + 2 = 8, A_4 = 8 + 2 = 10, A_5 = 10 + 2 = 12
- Check: A_6 = 12 + 2 = 14 ✓

### 1.2.2 Geometric Sequences

### Activity 1.4

Find the ratio between the consecutive terms of each of the following sequences.

a. 2, 6, 18, 54, …

**Answer:** 3
**Why:**
- 6 ÷ 2 = 3
- 18 ÷ 6 = 3
- 54 ÷ 18 = 3
- The ratio is the same each time: 3.

b. 2, −2, 2, −2, …

**Answer:** −1
**Why:**
- −2 ÷ 2 = −1
- 2 ÷ (−2) = −1
- −2 ÷ 2 = −1
- The ratio is the same each time: −1.

c. 3, −3/2, 3/4, −3/8, …

**Answer:** −1/2
**Why:**
- (−3/2) ÷ 3 = (−3/2) × (1/3) = −3/6 = −1/2 (common factor 3)
- (3/4) ÷ (−3/2) = (3/4) × (−2/3) = −6/12 = −1/2 (common factor 6)
- (−3/8) ÷ (3/4) = (−3/8) × (4/3) = −12/24 = −1/2 (common factor 12)
- The ratio is the same each time: −1/2.

### Definition 1.3

A geometric sequence or geometric progression is one in which the ratio between consecutive terms is a non-zero constant. This constant is called the common ratio.

{G_n} is geometric sequence if and only if r = G_(n+1)/G_n, r ∈ ℝ & r ≠ 0 where r is the common ratio.

### Example 1

For the following geometric sequence 3, 6, 12, 24, 48, …, find the common ratio, r, and the 6th term.

(p.16)

**Solution**

The common ratio:

G_2/G_1 = 6/3 = 2, G_3/G_2 = 12/6 = 2, G_4/G_3 = 24/12 = 2, …

[figure: arrows between 3, 6, 12, 24, … each labelled ×2]

Thus, r = 2.

The 6th term: G_6 = G_5 r = 48 × 2 = 96.

### Example 2

The 1st term of a geometric sequence is −1/2, and its common ratio is 1/2, find the 2nd, 3rd, 4th and 5th term.

**Solution**

We are given G_1 = −1/2 and r = 1/2, then

G_2 = G_1 r = −1/2 × 1/2 = −1/4
G_3 = G_2 r = −1/4 × 1/2 = −1/8
G_4 = G_3 r = −1/8 × 1/2 = −1/16
G_5 = G_4 r = −1/16 × 1/2 = −1/32.

### Exercise 1.7

1. For the geometric sequence 1, 2, 4, 8, 16 …, find the common ratio, r, and the 6th term.

**Answer:** r = 2; 6th term = 32
**Why:**
- r = 2 ÷ 1 = 2 (also 4 ÷ 2 = 2, 8 ÷ 4 = 2, 16 ÷ 8 = 2)
- G_6 = G_5 × r = 16 × 2 = 32
- Check: G_6 = G_1 r⁵ = 1 × 2⁵ = 32 ✓

2. Given that the 1st term of a geometric sequence is 1, and its common ratio is 3, find the 2nd, 3rd, 4th and 5th term.

**Answer:** 3, 9, 27, 81
**Why:**
- G_2 = G_1 r = 1 × 3 = 3
- G_3 = G_2 r = 3 × 3 = 9
- G_4 = G_3 r = 9 × 3 = 27
- G_5 = G_4 r = 27 × 3 = 81
- Check: G_5 = 1 × 3⁴ = 81 ✓

(p.17)

### Determining the nth term of geometric sequence

From the activity 1.4, (a), we have the geometric sequence 2, 6, 18, 54, … which has a common ratio of 3.

G_1 = 2
G_2 = 6 = 2 × 3 = G_1 × 3¹
G_3 = 18 = 6 × 3 = G_2 × 3 = G_1 × 3 × 3 = G_1 × 3²
G_4 = 54 = 18 × 3 = G_3 × 3 = G_1 × 3 × 3 × 3 = G_1 × 3³
…
G_n = G_1 × 3 × 3 × 3 × … × 3 = G_1 × 3^(n−1)

From Definition 1.3,

G_2 = G_1 × r
G_3 = G_2 × r = G_1 × r × r = G_1 × r²
G_4 = G_3 × r = G_1 × r² × r = G_1 × r³
G_5 = G_4 × r = G_1 × r³ × r = G_1 × r⁴
…
G_n = G_1 × r^(n−1)

Thus, the following theorem is deduced:

### Theorem 1.2

If {G_n} is a geometric sequence with the first term G_1 and common ratio r, then the nth term of the sequence is given by G_n = G_1 r^(n−1).

### Example 1

Find G_n, when the first term is 3 and the common ratio is 2.

**Solution**

Given G_1 = 3 and r = 2, then

G_n = G_1 r^(n−1) = 3 × 2^(n−1).

(p.18)

### Example 2

Find the nth term, G_n of the sequence 1, −2, 4, −8, 16, … .

**Solution**

G_1 = 1, r = −2

[added step: r = −2 ÷ 1 = −2, also 4 ÷ (−2) = −2.]

Applying the formula for the nth term of a geometric sequence, G_n = G_1 r^(n−1).

G_n = (−2)^(n−1).

[added step: G_n = 1 × (−2)^(n−1) = (−2)^(n−1).]

### Example 3

Find the 6th term of the geometric sequence whose first term is 1 and common ratio is 2.

**Solution**

Given G_1 = 1 and r = 2, then G_n = G_1 r^(n−1) = 1 × 2^(n−1) = 2^(n−1).

Therefore, G_6 = 2^(6−1) = 2⁵ or 32.

### Exercise 1.8

1. For each of the following, find the nth term of the geometric sequence.

a. G_1 = 2, r = 5

**Answer:** G_n = 2 × 5^(n−1)
**Why:**
- Theorem 1.2: G_n = G_1 r^(n−1)
- Substitute G_1 = 2, r = 5: G_n = 2 × 5^(n−1)
- Check: G_1 = 2 × 5⁰ = 2 ✓; G_2 = 2 × 5¹ = 10 = 2 × 5 ✓

b. G_1 = 1, r = −3

**Answer:** G_n = (−3)^(n−1)
**Why:**
- G_n = G_1 r^(n−1) = 1 × (−3)^(n−1) = (−3)^(n−1)
- Check: terms 1, −3, 9, −27; each is the one before × (−3) ✓

c. G_1 = 2, r = −2

**Answer:** G_n = 2(−2)^(n−1)
**Why:**
- G_n = G_1 r^(n−1) = 2 × (−2)^(n−1)
- Check: G_1 = 2 × 1 = 2 ✓; G_2 = 2 × (−2) = −4 ✓; G_3 = 2 × 4 = 8 ✓
- (Equivalent form: 2(−2)^(n−1) = −(−2)ⁿ, since −(−2)ⁿ = −(−2)(−2)^(n−1) = 2(−2)^(n−1).)

d. G_1 = −3, r = 1/2

**Answer:** G_n = −3(1/2)^(n−1)  (= −3/2^(n−1))
**Why:**
- G_n = G_1 r^(n−1) = −3 × (1/2)^(n−1)
- (1/2)^(n−1) = 1/2^(n−1), so G_n = −3/2^(n−1)
- Check: G_1 = −3/1 = −3 ✓; G_2 = −3/2 = −3 × 1/2 ✓

2. Find the nth term G_n of the following sequences

a. 3, 6, 12, 24, …

**Answer:** G_n = 3 × 2^(n−1)
**Why:**
- G_1 = 3; r = 6 ÷ 3 = 2 (also 12 ÷ 6 = 2, 24 ÷ 12 = 2)
- G_n = G_1 r^(n−1) = 3 × 2^(n−1)
- Check: G_4 = 3 × 2³ = 3 × 8 = 24 ✓

b. 3/2, 3/4, 3/8, 3/16, …

**Answer:** G_n = (3/2)(1/2)^(n−1) = 3/2ⁿ
**Why:**
- G_1 = 3/2
- r = (3/4) ÷ (3/2) = (3/4) × (2/3) = 6/12 = 1/2 (common factor 6)
- G_n = G_1 r^(n−1) = (3/2) × (1/2)^(n−1)
- = 3/(2 × 2^(n−1)) = 3/2ⁿ (adding exponents: 2¹ × 2^(n−1) = 2^(1 + n − 1) = 2ⁿ)
- Check: G_4 = 3/2⁴ = 3/16 ✓

c. 27, 9, 3, 1, …

**Answer:** G_n = 27(1/3)^(n−1)  (= 3^(4−n))
**Why:**
- G_1 = 27; r = 9 ÷ 27 = 9/27 = 1/3 (common factor 9)
- G_n = G_1 r^(n−1) = 27 × (1/3)^(n−1)
- 27 = 3³ and (1/3)^(n−1) = 3^(−(n−1)), so G_n = 3^(3 − (n − 1)) = 3^(4−n)
- Check: G_4 = 3^(4−4) = 3⁰ = 1 ✓; G_2 = 3² = 9 ✓

3. Find the 5th term of the geometric sequence whose first term is −3 and common ratio is −1/2.

**Answer:** G_5 = −3/16
**Why:**
- G_5 = G_1 r^(5−1) = −3 × (−1/2)⁴
- (−1/2)⁴ = (−1)⁴/2⁴ = 1/16 (even power, so positive)
- G_5 = −3 × 1/16 = −3/16
- Check by listing: −3, 3/2, −3/4, 3/8, −3/16 (each term × (−1/2)) ✓

(p.19)

### Geometric mean between two numbers

When a, m, and b are terms in a geometric sequence, then m is called the geometric mean between a and b. (a ≠ 0, b ≠ 0, m ≠ 0). In a geometric sequence, the ratio between consecutive terms is constant.

r = m/a = b/m
m² = ab
m = ±√(ab)

### Example 1

When 2, x, 5, … is a geometric sequence, find x (x ≠ 0).

**Solution**

As the ratio between the consecutive terms is the same,

x/2 = 5/x, x² = 10, x = ±√10.

[added step: cross-multiply x/2 = 5/x: x × x = 2 × 5, so x² = 10.]

### Example 2

Find geometric mean between 2 and 8.

**Solution**

Let the geometric mean be m (m ≠ 0), then

r = m/2 = 8/m
m² = 2 × 8
m = ±√16 = ±4.

Therefore, the geometric mean between 2 and 8 is −4 or 4.

(p.20)

### Example 3

Find the 8th term of the geometric sequence whose 1st term is 5 and 4th term is 1/25. (Express the answer in the form of exponent).

**Solution**

G_1 = 5 and G_4 = 1/25,

G_4 = G_1 r³ = 5r³ = 1/25.

[added step: divide both sides by 5: r³ = 1/(25 × 5) = 1/125, and 125 = 5³.]

Then, r³ = (1/5)³, therefore r = 1/5.

G_8 = G_1 r⁷ = 5(1/5)⁷ = 1/5⁶.

[added step: 5 × 1/5⁷ = 5¹/5⁷ = 1/5^(7−1) = 1/5⁶ (cancel one factor 5).]

### Exercise 1.9

1. Find the geometric mean between 3 and 12.

**Answer:** −6 or 6 (m = ±6)
**Why:**
- r = m/3 = 12/m
- Cross-multiply: m² = 3 × 12 = 36
- m = ±√36 = ±6
- Check: 3, 6, 12 has ratio 6/3 = 2 and 12/6 = 2 ✓; 3, −6, 12 has ratio −6/3 = −2 and 12/(−6) = −2 ✓

2. In a geometric sequence, the 2nd term is 12 and the 6th term is 192. Find the 11th term.

**Answer:** G_11 = 6144 (if r = 2) or G_11 = −6144 (if r = −2)
**Why:**
- G_2 = G_1 r = 12
- G_6 = G_1 r⁵ = 192
- Divide: (G_1 r⁵)/(G_1 r) = 192/12, so r⁴ = 16
- r = ±⁴√16 = ±2 (since 2⁴ = 16 and (−2)⁴ = 16)
- G_11 = G_2 × r⁹ (going 9 steps from the 2nd term to the 11th)
- If r = 2: G_11 = 12 × 2⁹ = 12 × 512 = 6144
- If r = −2: G_11 = 12 × (−2)⁹ = 12 × (−512) = −6144
- Check (r = 2): G_1 = 12/2 = 6, G_11 = 6 × 2¹⁰ = 6 × 1024 = 6144 ✓; (r = −2): G_1 = 12/(−2) = −6, G_11 = −6 × (−2)¹⁰ = −6 × 1024 = −6144 ✓; G_6 = −6 × (−2)⁵ = −6 × (−32) = 192 ✓

3. If x, 4x + 3, 7x + 6 are consecutive terms of a geometric sequence, find the value(s) of x, x ≠ 0.

**Answer:** x = −1
**Why:**
- Equal ratios: (4x + 3)/x = (7x + 6)/(4x + 3)
- Cross-multiply: (4x + 3)² = x(7x + 6)
- Expand the left: (4x + 3)² = 16x² + 24x + 9
- Expand the right: 7x² + 6x
- 16x² + 24x + 9 = 7x² + 6x
- Move all terms to the left: 16x² − 7x² + 24x − 6x + 9 = 0, so 9x² + 18x + 9 = 0
- Divide by the common factor 9: x² + 2x + 1 = 0
- Factor: (x + 1)² = 0
- x = −1 (≠ 0, allowed)
- Check: terms −1, 4(−1) + 3 = −1, 7(−1) + 6 = −1, i.e. −1, −1, −1 with common ratio 1 ✓

4. Find three consecutive terms of a geometric sequence, such that their sum is 35 and their product is 1000. Let the terms be a/r, a and ar. (a ≠ 0, r ≠ 0)

**Answer:** 5, 10, 20 (with r = 2) or 20, 10, 5 (with r = 1/2)
**Why:**
- Product: (a/r) × a × (ar) = a³ (the r cancels: r/r = 1)
- a³ = 1000, so a = ∛1000 = 10
- Sum: a/r + a + ar = 35, so 10/r + 10 + 10r = 35
- Subtract 10: 10/r + 10r = 25
- Multiply every term by r (r ≠ 0): 10 + 10r² = 25r
- Rearrange: 10r² − 25r + 10 = 0
- Divide by the common factor 5: 2r² − 5r + 2 = 0
- Factor: (2r − 1)(r − 2) = 0 [check: 2r² − 4r − r + 2 = 2r² − 5r + 2 ✓]
- r = 1/2 or r = 2
- r = 2: terms 10/2 = 5, 10, 10 × 2 = 20
- r = 1/2: terms 10 ÷ (1/2) = 20, 10, 10 × 1/2 = 5
- Check: 5 + 10 + 20 = 35 ✓; 5 × 10 × 20 = 1000 ✓

(p.21)

## 1.3 The Sigma Notation and Partial Sums

In the previous sections, you learned about the individual terms of a sequence. In this section, you will learn how to add the terms of a sequence, i.e. find the sum of the terms.

### Partial sums

Given the sequence a_n

S_1 = a_1, S_1 is the first term of the sequence.
S_2 = a_1 + a_2, S_2 is the sum of the first two terms of the sequence.
S_3 = a_1 + a_2 + a_3, S_3 is the sum of the first three terms of the sequence.
S_4 = a_1 + a_2 + a_3 + a_4, S_4 is the sum of the first four terms of the sequence,

and so on.

S_n = a_1 + a_2 + a_3 + a_4 + … + a_n, S_n is the sum of the first n terms of the sequence called the partial sum.

### Definition 1.4

Let {a_n}_{n=1}^{n=∞} be a sequence. The sum of the first n terms of the sequence, denoted by S_n is called the partial sum of the sequence. Such summation is denoted as follows.

S_n = ∑_{k=1}^{n} a_k = a_1 + a_2 + a_3 + a_4 + … + a_n, where k is the index of the summation, 1 is the lower limit of summation, n is the upper limit of the summation and ∑ is the sigma notation or the summation notation.

### Example 1

Find the sum of the first five even natural numbers.

(p.22)

**Solution**

a_1 = 2, a_2 = 4, a_3 = 6, a_4 = 8, a_5 = 10. Then,

S_5 = a_1 + a_2 + a_3 + a_4 + a_5
= 2 + 4 + 6 + 8 + 10
= 30

### Example 2

Let a_n = 3n + 1, find S_6

**Solution**

a_n = 3n + 1

a_1 = 4, a_2 = 7, a_3 = 10, a_4 = 13, a_5 = 16, a_6 = 19

[added step: a_1 = 3(1) + 1 = 4, a_2 = 3(2) + 1 = 7, a_3 = 3(3) + 1 = 10, a_4 = 3(4) + 1 = 13, a_5 = 3(5) + 1 = 16, a_6 = 3(6) + 1 = 19.]

S_6 = a_1 + a_2 + a_3 + a_4 + a_5 + a_6
= 4 + 7 + 10 + 13 + 16 + 19
= 69

### Example 3

Given the general term a_n = 1/(n(n+1)), find the sum of the first

a. 99 terms  b. n terms

**Solution**

By using partial fraction decomposition:

1/(n(n+1)) = A/n + B/(n+1)

Solving for A and B gives A = 1 and B = −1

[added step: multiply both sides by n(n+1): 1 = A(n+1) + Bn. Put n = 0: 1 = A(1), so A = 1. Put n = −1: 1 = B(−1), so B = −1.]

1/(n(n+1)) = 1/n − 1/(n+1)

(p.23)

(a) S_99 = (1 − 1/2) + (1/2 − 1/3) + (1/3 − 1/4) + … + (1/99 − 1/100) = 1 − 1/100 = 0.99

[added step: every middle fraction appears once with + and once with −, so they cancel in pairs (−1/2 + 1/2 = 0, −1/3 + 1/3 = 0, …), leaving only the first part 1 and the last part −1/100. 1 − 1/100 = 100/100 − 1/100 = 99/100 = 0.99.]

(b) S_n = 1 − 1/2 + 1/2 − 1/3 + 1/3 − … + 1/(n−1) − 1/n + 1/n − 1/(n+1) = 1 − 1/(n+1) = n/(n+1)

[added step: 1 − 1/(n+1) = (n+1)/(n+1) − 1/(n+1) = (n + 1 − 1)/(n+1) = n/(n+1). Check with (a): n = 99 gives 99/100 = 0.99 ✓]

**Note:** Such a sequence is said to be telescoping sequence.

### Exercise 1.10

1. Find the sum of:

a. the first five odd natural numbers.

**Answer:** 25
**Why:**
- The first five odd natural numbers: 1, 3, 5, 7, 9
- S_5 = 1 + 3 + 5 + 7 + 9
- 1 + 3 = 4; 4 + 5 = 9; 9 + 7 = 16; 16 + 9 = 25
- Check: pairing first and last, 1 + 9 = 10, 3 + 7 = 10, middle 5: 10 + 10 + 5 = 25 ✓ (also 5² = 25: the sum of the first n odd numbers is n²)

b. the first ten odd natural numbers.

**Answer:** 100
**Why:**
- The first ten odd natural numbers: 1, 3, 5, 7, 9, 11, 13, 15, 17, 19
- Pair first with last: 1 + 19 = 20, 3 + 17 = 20, 5 + 15 = 20, 7 + 13 = 20, 9 + 11 = 20
- 5 pairs × 20 = 100
- Check by running total: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 ✓ (10² = 100)

2. Find the sums of the following sequences to the term given.

a. a_n = 4n − 3, S_5.

**Answer:** S_5 = 45
**Why:**
- a_1 = 4(1) − 3 = 1
- a_2 = 4(2) − 3 = 5
- a_3 = 4(3) − 3 = 9
- a_4 = 4(4) − 3 = 13
- a_5 = 4(5) − 3 = 17
- S_5 = 1 + 5 + 9 + 13 + 17
- 1 + 5 = 6; 6 + 9 = 15; 15 + 13 = 28; 28 + 17 = 45
- Check: pairs 1 + 17 = 18 and 5 + 13 = 18, middle 9: 18 + 18 + 9 = 45 ✓

b. a_n = 3 − 5n, S_8.

**Answer:** S_8 = −156
**Why:**
- a_1 = 3 − 5(1) = −2
- a_2 = 3 − 5(2) = −7
- a_3 = 3 − 5(3) = −12
- a_4 = 3 − 5(4) = −17
- a_5 = 3 − 5(5) = −22
- a_6 = 3 − 5(6) = −27
- a_7 = 3 − 5(7) = −32
- a_8 = 3 − 5(8) = −37
- S_8 = −2 − 7 − 12 − 17 − 22 − 27 − 32 − 37
- Running total: −2, −9, −21, −38, −60, −87, −119, −156
- Check: pairs first + last = −2 + (−37) = −39; 4 pairs × (−39) = −156 ✓

c. a_n = n² + 1, S_6.

**Answer:** S_6 = 97
**Why:**
- a_1 = 1² + 1 = 2
- a_2 = 2² + 1 = 5
- a_3 = 3² + 1 = 10
- a_4 = 4² + 1 = 17
- a_5 = 5² + 1 = 26
- a_6 = 6² + 1 = 37
- S_6 = 2 + 5 + 10 + 17 + 26 + 37
- 2 + 5 = 7; 7 + 10 = 17; 17 + 17 = 34; 34 + 26 = 60; 60 + 37 = 97
- Check: (1 + 4 + 9 + 16 + 25 + 36) + 6×1 = 91 + 6 = 97 ✓

3. Given the general term a_n = 2/(n² + 5n + 6), find the sum of the first nth terms.

(Read as: the sum of the first n terms.)

**Answer:** S_n = 2n/(3(n + 3)) = 2n/(3n + 9)
**Why:**
- Factor the denominator: n² + 5n + 6 = (n + 2)(n + 3) (because 2 + 3 = 5 and 2 × 3 = 6)
- So a_n = 2/((n + 2)(n + 3))
- Partial fractions: 1/((n + 2)(n + 3)) = 1/(n + 2) − 1/(n + 3) [check: (n + 3 − (n + 2))/((n + 2)(n + 3)) = 1/((n + 2)(n + 3)) ✓]
- So a_n = 2[1/(n + 2) − 1/(n + 3)]
- S_n = 2[(1/3 − 1/4) + (1/4 − 1/5) + (1/5 − 1/6) + … + (1/(n + 2) − 1/(n + 3))]
- The middle terms cancel (telescoping), leaving S_n = 2[1/3 − 1/(n + 3)]
- Common denominator 3(n + 3): 1/3 = (1×(n + 3))/(3×(n + 3)) = (n + 3)/(3(n + 3)) and 1/(n + 3) = (1×3)/((n + 3)×3) = 3/(3(n + 3))
- 1/3 − 1/(n + 3) = (n + 3 − 3)/(3(n + 3)) = n/(3(n + 3))
- S_n = 2 × n/(3(n + 3)) = 2n/(3(n + 3)) = 2n/(3n + 9)
- Check n = 1: a_1 = 2/(1 + 5 + 6) = 2/12 = 1/6; formula 2(1)/(3 × 4) = 2/12 = 1/6 ✓
- Check n = 2: a_2 = 2/(4 + 10 + 6) = 2/20 = 1/10; S_2 = 1/6 + 1/10 = 5/30 + 3/30 = 8/30 = 4/15; formula 2(2)/(3 × 5) = 4/15 ✓

### Sigma notation

Sigma notation is a method used to write out a long sum in a concise way. We use sigma notation for writing finite and infinite numbers of terms in a sequence. The sum is denoted by the sigma notation using the Greek letter ∑ (sigma).

### Example 1

Express the following sigma notation in the form of the sum

a. ∑_{k=1}^{8} 3k  b. ∑_{k=2}^{6} k²

**Solution**

a. ∑_{k=1}^{8} 3k = 3 + 6 + 9 + 12 + 15 + 18 + 21 + 24 = 108.

b. ∑_{k=2}^{6} k² = 4 + 9 + 16 + 25 + 36 = 90.

[added step: in (a) substitute k = 1, 2, …, 8 into 3k; in (b) substitute k = 2, 3, 4, 5, 6 into k² — the sum starts at k = 2, so 1² is not included.]

(p.24)

### Example 2

Which one of the following express the sum, 3² + 4² + 5² + 6² + 7²?

a. ∑_{k=3}^{7} k²  b. ∑_{i=3}^{7} i²  c. ∑_{k=2}^{6} (k+1)²

**Solution**

All of them express the given sum.

[added step: (b) only changes the name of the index (i instead of k), which does not change the sum. In (c), k = 2, 3, 4, 5, 6 gives (k + 1) = 3, 4, 5, 6, 7, so the terms are 3², 4², 5², 6², 7².]

### Exercise 1.11

1. Express the following sigma notations in the form of a sum.

a. ∑_{k=1}^{6} 2k

**Answer:** 2 + 4 + 6 + 8 + 10 + 12 (= 42)
**Why:**
- k = 1: 2(1) = 2; k = 2: 2(2) = 4; k = 3: 2(3) = 6; k = 4: 2(4) = 8; k = 5: 2(5) = 10; k = 6: 2(6) = 12
- Sum: 2 + 4 + 6 + 8 + 10 + 12 = 42
- Check: 2(1 + 2 + 3 + 4 + 5 + 6) = 2(21) = 42 ✓

b. ∑_{k=3}^{5} k²

**Answer:** 3² + 4² + 5² = 9 + 16 + 25 (= 50)
**Why:**
- The index starts at k = 3 and ends at k = 5 (3 terms).
- k = 3: 3² = 9; k = 4: 4² = 16; k = 5: 5² = 25
- Sum: 9 + 16 + 25 = 50

c. ∑_{k=1}^{n} 3^k

**Answer:** 3 + 3² + 3³ + … + 3ⁿ = 3 + 9 + 27 + … + 3ⁿ
**Why:**
- k = 1: 3¹ = 3; k = 2: 3² = 9; k = 3: 3³ = 27; …; k = n: 3ⁿ
- The upper limit is n, so the sum is written with "…" and the last term 3ⁿ.
- (Optional closed form, from the geometric sum later in the unit: 3(3ⁿ − 1)/2. Check n = 2: 3(9 − 1)/2 = 12 = 3 + 9 ✓)

d. ∑_{k=3}^{5} k³

**Answer:** 3³ + 4³ + 5³ = 27 + 64 + 125 (= 216)
**Why:**
- k = 3: 3³ = 27; k = 4: 4³ = 64; k = 5: 5³ = 125
- Sum: 27 + 64 = 91; 91 + 125 = 216

2. Express the following using the sigma notation

2² + 4² + 6² + 8² + 10² + 12².

**Answer:** ∑_{k=1}^{6} (2k)²  (equivalently ∑_{k=1}^{6} 4k²)
**Why:**
- The numbers being squared are 2, 4, 6, 8, 10, 12 = 2×1, 2×2, …, 2×6, i.e. 2k for k = 1 to 6.
- So each term is (2k)², and there are 6 terms.
- Check: k = 1 gives 2² ✓; k = 6 gives 12² ✓
- (2k)² = 4k², so ∑_{k=1}^{6} 4k² is the same sum. Value: 4 + 16 + 36 + 64 + 100 + 144 = 364.

### 1.3.1 Sigma Notation

### Properties of sigma notation

The sequence {a_n}, where all the terms are c, the sum of the first nth term is

∑_{k=1}^{n} a_n = c + c + c + … + c = nc

That is, ∑_{k=1}^{n} a_n = nc

In particular, ∑_{k=1}^{n} 1 = n(1) = n.

**Properties of Sigma Notation**

(1) ∑_{k=1}^{n} c·a_k = c ∑_{k=1}^{n} a_k, c is a constant
(2) ∑_{k=1}^{n} (a_k + b_k) = ∑_{k=1}^{n} a_k + ∑_{k=1}^{n} b_k
(3) ∑_{k=1}^{n} (a_k − b_k) = ∑_{k=1}^{n} a_k − ∑_{k=1}^{n} b_k
(4) ∑_{k=1}^{n} a_k = ∑_{k=1}^{m} a_k + ∑_{k=m+1}^{n} a_k, 1 ≤ m ≤ n

[review: in property (2) the book prints the first sum on the right as ∑_{k=1}^{n} a_i (index i); this is a typo for a_k, transcribed here as a_k.]

(p.25)

### Example

Evaluate each of the following sigma notations:

(a) ∑_{k=1}^{3} 4k  (b) ∑_{k=1}^{5} (3k − 2)  (c) ∑_{k=1}^{6} 2^(k−1)

**Solution**

(a) ∑_{k=1}^{3} 4k = 4 + 8 + 12 = 24

Using the above property (1), you can also calculate,

∑_{k=1}^{3} 4k = 4 ∑_{k=1}^{3} k = 4(1 + 2 + 3) = 4(6) = 24

(b) ∑_{k=1}^{5} (3k − 2) = 1 + 4 + 7 + 10 + 13 = 35

Using property (1) and (3), you can also calculate,

∑_{k=1}^{5} (3k − 2) = 3 ∑_{k=1}^{5} k − ∑_{k=1}^{5} 2 = 3(1 + 2 + 3 + 4 + 5) − (2 + 2 + 2 + 2 + 2)
= 3(1 + 2 + 3 + 4 + 5) − (2 + 2 + 2 + 2 + 2)
= 3(15) − 2(5)
= 35

[added step: 3(15) − 2(5) = 45 − 10 = 35.]

(c) ∑_{k=1}^{6} 2^(k−1) = 2⁰ + 2¹ + 2² + 2³ + 2⁴ + 2⁵
= 1 + 2 + 4 + 8 + 16 + 32
= 63

Using the above property (4), you can also calculate,

∑_{k=1}^{6} 2^(k−1) = ∑_{k=1}^{3} 2^(k−1) + ∑_{k=4}^{6} 2^(k−1)
= (2⁰ + 2¹ + 2²) + (2³ + 2⁴ + 2⁵)
= 63

[added step: (1 + 2 + 4) + (8 + 16 + 32) = 7 + 56 = 63.]

(p.26)

### Exercise 1.12

Evaluate each of the following sigma notations.

a. ∑_{k=1}^{4} 5k

**Answer:** 50
**Why:**
- 5(1) + 5(2) + 5(3) + 5(4) = 5 + 10 + 15 + 20 = 50
- Check with property (1): 5 ∑_{k=1}^{4} k = 5(1 + 2 + 3 + 4) = 5(10) = 50 ✓

b. ∑_{k=1}^{5} (4k − 1)

**Answer:** 55
**Why:**
- k = 1: 4 − 1 = 3; k = 2: 8 − 1 = 7; k = 3: 12 − 1 = 11; k = 4: 16 − 1 = 15; k = 5: 20 − 1 = 19
- 3 + 7 + 11 + 15 + 19 = 55
- Check with properties (1) and (3): 4 ∑k − ∑1 = 4(15) − 5(1) = 60 − 5 = 55 ✓

c. ∑_{k=3}^{6} (k² − 4)

**Answer:** 70
**Why:**
- k = 3: 9 − 4 = 5
- k = 4: 16 − 4 = 12
- k = 5: 25 − 4 = 21
- k = 6: 36 − 4 = 32
- 5 + 12 + 21 + 32 = 70
- Check: (9 + 16 + 25 + 36) − 4 × 4 = 86 − 16 = 70 ✓ (there are 4 terms, k = 3, 4, 5, 6)

d. ∑_{k=2}^{5} 3

**Answer:** 12
**Why:**
- Every term is the constant 3.
- Number of terms from k = 2 to k = 5: 5 − 2 + 1 = 4
- Sum = 4 × 3 = 12
- Check: 3 + 3 + 3 + 3 = 12 ✓ (common mistake: 5 × 3 = 15 — the sum does not start at k = 1)

e. ∑_{k=1}^{8} (k³ + 2k² − 3k + 5)

**Answer:** 1636
**Why:**
- k = 1: 1 + 2 − 3 + 5 = 5
- k = 2: 8 + 8 − 6 + 5 = 15
- k = 3: 27 + 18 − 9 + 5 = 41
- k = 4: 64 + 32 − 12 + 5 = 89
- k = 5: 125 + 50 − 15 + 5 = 165
- k = 6: 216 + 72 − 18 + 5 = 275
- k = 7: 343 + 98 − 21 + 5 = 425
- k = 8: 512 + 128 − 24 + 5 = 621
- Running total: 5, 20, 61, 150, 315, 590, 1015, 1636
- Check with properties (1)–(3) and the separate sums: ∑k³ = 1 + 8 + 27 + 64 + 125 + 216 + 343 + 512 = 1296; ∑k² = 1 + 4 + 9 + 16 + 25 + 36 + 49 + 64 = 204; ∑k = 36; ∑5 = 8 × 5 = 40. Total = 1296 + 2(204) − 3(36) + 40 = 1296 + 408 − 108 + 40 = 1636 ✓

### 1.3.2 Sum of Arithmetic Sequences

### Activity 1.5

Find the sum of the first ten terms of the sequence 5, 15, 25, 35, …

**Answer:** 500
**Why:**
- It is arithmetic: A_1 = 5, d = 15 − 5 = 10
- 10th term: A_10 = 5 + 9 × 10 = 5 + 90 = 95
- Terms: 5, 15, 25, 35, 45, 55, 65, 75, 85, 95
- Pair first and last (Gauss's method): 5 + 95 = 100, 15 + 85 = 100, 25 + 75 = 100, 35 + 65 = 100, 45 + 55 = 100
- 5 pairs × 100 = 500
- Check with Theorem 1.3 (p.28): S_10 = (10/2)[2(5) + 9(10)] = 5(10 + 90) = 5(100) = 500 ✓

#### HISTORICAL NOTE — Carl Friedrich Gauss (1777–1855)

A teacher of Gauss, at his elementary school, asked him to add all the integers from 1 to 100. When Gauss returned with the correct answer after only a few moments, the teacher could only look at him in astounded silence. This is what Gauss did:

  1 + 2 + 3 + … + 100
  100 + 99 + 98 + … + 1
  ─────────────────────
  101 + 101 + 101 + … + 101

  (100 × 101)/2 = 5050.

[figure: portrait of Carl Friedrich Gauss]

To find the sum of the first 100 natural numbers, Gauss worked as follows. Writing the sum forward and backward then adding them together yields:

S_100 = 1 + 2 + 3 + … + 98 + 99 + 100
S_100 = 100 + 99 + 98 + … + 3 + 2 + 1
2S_100 = 101 + 101 + 101 + … + 101 + 101 + 101
2S_100 = 100 × 101

(p.27)

Therefore, S_100 = (1/2) × 100 × 101 = 5050

The sum of the first n natural numbers can also be calculated as follows:

S_n = 1 + 2 + 3 + … + (n − 2) + (n − 1) + n
S_n = n + (n − 1) + (n − 2) + … 3 + 2 + 1
2S_n = (n + 1) + (n + 1) + … + (n + 1) + (n + 1)

Therefore, 2S_n = n(n + 1)

**The sum of the first n consecutive natural numbers is S_n = (n/2)(n + 1).**

### Example

Find the sum of the first a. 40 natural numbers b. 150 natural numbers

**Solution**

a) Using the formula S_n = (n/2)(n + 1), S_40 = (40/2)(40 + 1) = 20(41) = 820

b) Using the formula S_n = (n/2)(n + 1), S_150 = (150/2)(150 + 1) = 75(151) = 11,325

### Exercise 1.13

1. Find the sum of the first

a. 30 natural numbers.

**Answer:** 465
**Why:**
- S_n = (n/2)(n + 1)
- S_30 = (30/2)(30 + 1) = 15 × 31 = 465
- Check: Gauss pairing 1 + 30 = 31, 15 pairs: 15 × 31 = 465 ✓

b. 99 natural numbers.

**Answer:** 4950
**Why:**
- S_99 = (99/2)(99 + 1) = (99/2)(100) = 99 × 50 = 4950
- Check: S_100 − 100 = 5050 − 100 = 4950 ✓

c. 200 natural numbers.

**Answer:** 20,100
**Why:**
- S_200 = (200/2)(200 + 1) = 100 × 201 = 20,100
- Check: 100 pairs (1 + 200, 2 + 199, …) each 201: 100 × 201 = 20,100 ✓

2. If the sum of the first n natural numbers is 3240, what is the value of n?

**Answer:** n = 80
**Why:**
- (n/2)(n + 1) = 3240
- Multiply both sides by 2: n(n + 1) = 6480
- Expand: n² + n − 6480 = 0
- Look for two consecutive numbers whose product is 6480: √6480 ≈ 80.5, try 80 × 81 = 6480 ✓
- So n² + n − 6480 = (n − 80)(n + 81) = 0, giving n = 80 or n = −81
- n must be a natural number, so n = 80
- Check: S_80 = (80/2)(81) = 40 × 81 = 3240 ✓

### Derivation of sum of arithmetic sequence

Let {A_n}_{n=1}^{∞} be an arithmetic sequence.

S_n = A_1 + A_2 + A_3 + … + A_n, where A_n = A_1 + (n − 1)d
S_n = A_1 + (A_1 + d) + (A_1 + 2d) + (A_1 + 3d) + … + (A_1 + (n − 1)d)

(p.28)

By collecting all the A_1 terms (there are n of them) we get,

S_n = nA_1 + [d + 2d + 3d + … + (n − 1)d]

Now factoring out d from within the brackets,

S_n = nA_1 + d[1 + 2 + 3 + … + (n − 1)]

Inside the brackets you have the sum of the first (n − 1) positive integers. Thus by using the formula, S_n = (n/2)(n + 1),

S_n = nA_1 + d((n − 1)/2)n = (2nA_1 + n(n − 1)d)/2 = (n/2)[2A_1 + (n − 1)d].

[added step: replacing n by (n − 1) in (n/2)(n + 1) gives 1 + 2 + … + (n − 1) = ((n − 1)/2)((n − 1) + 1) = ((n − 1)/2)n. Then nA_1 = (2nA_1)/2, so the two parts share the denominator 2; finally take out the common factor n from the top: (n[2A_1 + (n − 1)d])/2.]

This formula can be written as:

S_n = (n/2)[A_1 + {A_1 + (n − 1)d}]
= (n/2)(A_1 + A_n)

Hence, the following theorem is derived:

### Theorem 1.3

The sum S_n of the first n terms of an arithmetic sequence with first term A_1 and common difference d is S_n = ∑_{k=1}^{n} A_k = (n/2)[2A_1 + (n − 1)d].

This formula can also be written as:

S_n = n((A_1 + A_n)/2), where A_n is the nth term.

This alternative formula is useful when the first and the last terms are known.

### Example 1

Find the sum of the first 35 terms of the sequence whose general term is A_n = 5n.

(p.29)

**Solution**

From the general term, we get A_1 = 5, A_2 = 10, A_3 = 15, …, this shows that the given sequence is an arithmetic sequence. So, A_35 = 5(35) = 175.

Since we can easily identify the first and the 35th terms, we use the formula

S_n = (n/2)(A_1 + A_n) = n((A_1 + A_n)/2)

Thus, substituting A_1 = 5, and A_35 = 175

S_35 = (35/2)(5 + 175) = 35((5 + 175)/2) = 35(90) = 3,150

[added step: (5 + 175)/2 = 180/2 = 90.]

### Example 2

If the 1st term of arithmetic sequence is 4, common difference is 5, then find the sum of the first 40 terms.

**Solution**

Given A_1 = 4, d = 5,

S_n = (n/2)[2A_1 + (n − 1)d] ⇒ S_40 = (40/2)[2(4) + (40 − 1)(5)] = 20(8 + 195) = 20(203) = 4060.

### Exercise 1.14

1. Find the partial sum of the following arithmetic sequences:

a. A_1 = 2, and last term A_10 = 21.

**Answer:** S_10 = 115
**Why:**
- First and last terms are known, so use S_n = (n/2)(A_1 + A_n)
- S_10 = (10/2)(2 + 21) = 5 × 23 = 115
- Check with the other form: A_10 = A_1 + 9d gives 21 = 2 + 9d, d = 19/9; S_10 = (10/2)[2(2) + 9(19/9)] = 5(4 + 19) = 5 × 23 = 115 ✓

b. A_1 = 40, and last term A_26 = 0.

**Answer:** S_26 = 520
**Why:**
- S_n = (n/2)(A_1 + A_n)
- S_26 = (26/2)(40 + 0) = 13 × 40 = 520
- Check: A_26 = A_1 + 25d gives 0 = 40 + 25d, d = −40/25 = −8/5; S_26 = 13[2(40) + 25(−8/5)] = 13(80 − 40) = 13 × 40 = 520 ✓

2. Find the sum of the following arithmetic sequences:

a. A_1 = 2, d = 3, n = 10

**Answer:** S_10 = 155
**Why:**
- S_n = (n/2)[2A_1 + (n − 1)d]
- S_10 = (10/2)[2(2) + (10 − 1)(3)]
- = 5[4 + 27]
- = 5 × 31 = 155
- Check: A_10 = 2 + 9 × 3 = 29; (10/2)(2 + 29) = 5 × 31 = 155 ✓

b. A_1 = 30, d = −5, n = 12

**Answer:** S_12 = 30
**Why:**
- S_12 = (12/2)[2(30) + (12 − 1)(−5)]
- = 6[60 − 55]
- = 6 × 5 = 30
- Check: A_12 = 30 + 11(−5) = 30 − 55 = −25; (12/2)(30 + (−25)) = 6 × 5 = 30 ✓ (terms 30, 25, …, 5, 0, −5, …, −25: the positives 5 to 25 cancel the negatives −5 to −25, leaving 30 + 0 = 30 ✓)

(p.30)

### Further on sum of arithmetic sequence

### Example 1

Find the sum S_7 of the arithmetic sequence whose 4th term is 2 and 7th term is 17.

**Solution**

Applying the formula A_n = A_1 + (n − 1)d

{ A_4 = A_1 + 3d = 2
{ A_7 = A_1 + 6d = 17

Subtracting the first equation from the second equation,

3d = 17 − 2
d = 5

[added step: 3d = 15, so d = 15/3 = 5.]

Thus,

A_1 = A_4 − 3d
A_1 = 2 − 3 × 5 = −13

S_n = n((A_1 + A_n)/2)

S_7 = 7((−13 + 17)/2) = 7(2) = 14.

[added step: (−13 + 17)/2 = 4/2 = 2. Check A_7 = −13 + 6 × 5 = −13 + 30 = 17 ✓]

### Example 2

For a given arithmetic sequence the sum S_10 = 165 and A_1 = 3, find A_10.

**Solution**

Since the first term and the sum are given, applying the formula gives:

S_n = n((A_1 + A_n)/2)

S_10 = 165, A_1 = 3, A_10 = ?

S_10 = 10((A_1 + A_10)/2)

[The book's solution continues on p.31, which is outside this file (pages 1–30).]
[added step (completion, to be checked against p.31): 165 = 10((3 + A_10)/2) = 5(3 + A_10); divide by 5: 33 = 3 + A_10; so A_10 = 30.]

# Grade 12 Mathematics — Unit 1: Sequences and Series (book pages 31–60)

Source: Ethiopian Grade 12 Mathematics Student Textbook (2023). Book page = image file number − 10.

## 1.3 (continued) — Sum of arithmetic sequences

(p.31)

[continuation of the worked example begun on p.30 — the book's solution ends here:]

165 = (10/2)(3 + A_10)

165/5 = 3 + A_10

A_10 = 33 − 3 = 30.

[added step: (10/2) = 5, so dividing both sides by 5 gives 165/5 = 33 = 3 + A_10.]

### Example 3

Find the sum of integers from 1 to 100 that are divisible by 10.

**Solution**

The number of such integer is 100/10 = 10

The 1st term is 10, and the last term is 100. Then, S_n = 10((10 + 100)/2) = 550.

[added step: the integers are 10, 20, …, 100, an arithmetic sequence with n = 10, A_1 = 10, A_10 = 100; S_n = (n/2)(A_1 + A_n) = 10 × (110/2) = 10 × 55 = 550.]

### Exercise 1.15

1. Find S_5 of the arithmetic sequence whose 3rd term is 5 and 5th term is 11.

**Answer:** S_5 = 25

**Why:**
A_n = A_1 + (n − 1)d
A_3 = A_1 + 2d = 5 … (1)
A_5 = A_1 + 4d = 11 … (2)
(2) − (1): 2d = 6
d = 6/2 = 3
From (1): A_1 = 5 − 2(3) = 5 − 6 = −1
S_n = (n/2)(2A_1 + (n − 1)d)
S_5 = (5/2)(2(−1) + 4(3))
S_5 = (5/2)(−2 + 12)
S_5 = (5/2)(10) = 50/2 = 25
Check (list the terms): −1, 2, 5, 8, 11 → −1 + 2 + 5 + 8 + 11 = 25 ✓ (A_3 = 5 and A_5 = 11 ✓)

2. Given the sum of an arithmetic sequence is S_8 = 120 and A_1 = 1, find A_8 and A_n.

**Answer:** A_8 = 29 and A_n = 4n − 3

**Why:**
S_n = (n/2)(A_1 + A_n)
120 = (8/2)(1 + A_8)
120 = 4(1 + A_8)
120/4 = 1 + A_8
30 = 1 + A_8
A_8 = 30 − 1 = 29
A_8 = A_1 + 7d, so 29 = 1 + 7d
7d = 28
d = 28/7 = 4
A_n = A_1 + (n − 1)d = 1 + (n − 1)(4) = 1 + 4n − 4 = 4n − 3
Check: terms 1, 5, 9, 13, 17, 21, 25, 29 → sum = (1 + 29) + (5 + 25) + (9 + 21) + (13 + 17) = 4 × 30 = 120 ✓; A_8 = 4(8) − 3 = 29 ✓

3. Find the sum of the integers from 1 to 100 that are divisible by 2 or 5.

**Answer:** 3050

**Why:**
Use inclusion–exclusion: sum(divisible by 2) + sum(divisible by 5) − sum(divisible by both, i.e. by 10).
Divisible by 2: 2, 4, …, 100; n = 100/2 = 50 terms
S = (50/2)(2 + 100) = 25 × 102 = 2550
Divisible by 5: 5, 10, …, 100; n = 100/5 = 20 terms
S = (20/2)(5 + 100) = 10 × 105 = 1050
Divisible by 10: 10, 20, …, 100; n = 10 terms; S = 550 (Example 3)
Total = 2550 + 1050 − 550 = 3050
Check (second method): divisible by 5 but odd = 5, 15, 25, …, 95 → 10 terms, sum = (10/2)(5 + 95) = 500; even numbers sum 2550; 2550 + 500 = 3050 ✓

4. Find the sum of odd integers from 1 to 2001.

**Answer:** 1 002 001

**Why:**
Odd integers 1, 3, 5, …, 2001: arithmetic with A_1 = 1, d = 2
A_n = 1 + (n − 1)(2) = 2001
(n − 1)(2) = 2000
n − 1 = 1000
n = 1001
S_n = (n/2)(A_1 + A_n) = (1001/2)(1 + 2001) = (1001/2)(2002) = 1001 × 1001 = 1 002 001
Check: the sum of the first n odd numbers is n², and 1001² = 1 002 001 ✓

### 1.3.2 Sum of Geometric Sequences

### Activity 1.6

1. Find the sum of the following geometric sequences:
   a. {2, 4, 8, 16, 32}
   b. {1, 2/3, 4/9, 8/27}
2. Find the sum of the first 5 terms of the sequence 1, 2/3, 4/9, 8/27, 16/81, ….

**1a. Answer:** 62

**Why:**
2 + 4 = 6
6 + 8 = 14
14 + 16 = 30
30 + 32 = 62
Check by formula: G_1 = 2, r = 2, n = 5 → S_5 = 2(2⁵ − 1)/(2 − 1) = 2(32 − 1)/1 = 2 × 31 = 62 ✓ (the book also gets 62 on p.33)

**1b. Answer:** 65/27

**Why:**
Common denominator 27:
1 = (1×27)/(1×27) = 27/27
2/3 = (2×9)/(3×9) = 18/27
4/9 = (4×3)/(9×3) = 12/27
8/27 = 8/27
Sum = (27 + 18 + 12 + 8)/27 = 65/27
Check by formula: G_1 = 1, r = 2/3, n = 4 → S_4 = (1 − (2/3)⁴)/(1 − 2/3) = (1 − 16/81)/(1/3) = (65/81) × 3 = 195/81 = 65/27 (dividing top and bottom by 3) ✓ (the book gets 65/27 on p.33)

**2. Answer:** 211/81

**Why:**
First 5 terms: 1, 2/3, 4/9, 8/27, 16/81
Common denominator 81:
1 = 81/81
2/3 = (2×27)/(3×27) = 54/81
4/9 = (4×9)/(9×9) = 36/81
8/27 = (8×3)/(27×3) = 24/81
16/81 = 16/81
Sum = (81 + 54 + 36 + 24 + 16)/81 = 211/81
Check by formula: S_5 = (1 − (2/3)⁵)/(1 − 2/3) = (1 − 32/243)/(1/3) = (211/243) × 3 = 633/243 = 211/81 (dividing top and bottom by 3) ✓

(p.32)

In order to answer such types of problems, consider the following:

Let {G_n}_{n=1}^{∞} be a geometric sequence, then its associated geometric sum, S_n is:

S_n = G_1 + G_2 + G_3 + … + G_(n−1) + G_n, where G_n = r^(n−1) G_1

S_n = G_1 + rG_1 + r²G_1 + … + r^(n−2) G_1 + r^(n−1) G_1

Factorizing out G_1,

S_n = G_1(1 + r + r² + … + r^(n−2) + r^(n−1))   (1)

Multiplying both sides of equation (1) by r

rS_n = G_1(r + r² + r³ + … + r^(n−1) + r^n)   (2)

Subtracting the equation (2) from equation (1),

S_n − rS_n = G_1(1 + r + r² + r³ + … + r^(n−2) + r^(n−1)) − G_1(r + r² + r³ + … + r^(n−1) + r^n)

(1 − r)S_n = G_1(1 − r^n)

S_n = G_1(1 − r^n)/(1 − r) for r ≠ 1

[added step: all the middle terms r, r², …, r^(n−1) cancel, leaving G_1 × 1 − G_1 × r^n; then divide both sides by (1 − r), which is allowed only when r ≠ 1.]

Thus, the following theorem is inferred:

### Theorem 1.4

Let {G_n}_{n=1}^{∞} be a geometric sequence with common ratio r. Then the sum of the first n terms S_n is given by,

- S_n = nG_1, if r = 1
- S_n = G_1 (1 − r^n)/(1 − r) = G_1 (r^n − 1)/(r − 1), if r ≠ 1.

### Example

Find the sum of the sequences in activity 1.6 using this theorem, and confirm the results.

(p.33)

**Solution**

a. r = 2, G_1 = 2 and n = 5

S_5 = 2((2⁵ − 1)/(2 − 1)) = 62

[added step: 2⁵ − 1 = 32 − 1 = 31; 2 − 1 = 1; 2 × 31 = 62.]

b. {1, 2/3, 4/9, 8/27}

G_1 = 1, r = 2/3 and n = 4

S_4 = 1(((2/3)⁴ − 1)/((2/3) − 1)) = 65/27

[added step: (2/3)⁴ = 16/81, so (2/3)⁴ − 1 = 16/81 − 81/81 = −65/81; 2/3 − 1 = −1/3; (−65/81) ÷ (−1/3) = (65/81) × 3 = 195/81 = 65/27.]

### Exercise 1.16

1. Find the sum of the from 1st to nth of the following geometric sequences:
   a. G_1 = 3, r = 2
   b. G_1 = 1, r = 1/2
2. Given the geometric sequence: 1, 3, 9, 27, …. find S_n.

[review: the book's wording "Find the sum of the from 1st to nth" is printed as-is (missing a word, presumably "terms"); transcribed faithfully.]

**1a. Answer:** S_n = 3(2^n − 1)

**Why:**
r = 2 ≠ 1, so use S_n = G_1(r^n − 1)/(r − 1)
S_n = 3(2^n − 1)/(2 − 1)
S_n = 3(2^n − 1)/1 = 3(2^n − 1) = 3 × 2^n − 3
Check: n = 3 → terms 3, 6, 12, sum 21; formula 3(8 − 1) = 21 ✓

**1b. Answer:** S_n = 2(1 − (1/2)^n) = 2 − 1/2^(n−1)

**Why:**
r = 1/2 ≠ 1, so use S_n = G_1(1 − r^n)/(1 − r)
S_n = 1 × (1 − (1/2)^n)/(1 − 1/2)
1 − 1/2 = 1/2
S_n = (1 − (1/2)^n) ÷ (1/2) = 2(1 − (1/2)^n)
= 2 − 2/2^n = 2 − 1/2^(n−1)
Check: n = 3 → terms 1, 1/2, 1/4, sum 7/4; formula 2 − 1/2² = 2 − 1/4 = 7/4 ✓

**2. Answer:** S_n = (3^n − 1)/2

**Why:**
G_1 = 1, r = 3/1 = 3 (also 9/3 = 3, 27/9 = 3)
r ≠ 1, so S_n = G_1(r^n − 1)/(r − 1)
S_n = 1 × (3^n − 1)/(3 − 1) = (3^n − 1)/2
Check: n = 4 → 1 + 3 + 9 + 27 = 40; formula (81 − 1)/2 = 80/2 = 40 ✓

### Further on the sum of geometric sequences

### Example

The sum of the first three terms of a geometric sequence is 7, and the sum from 4th to 6th terms is 56. Find the first term and the common ratio.

**Solution**

Let the first term be G_1 and common ratio r. Then,

G_1 + G_1r + G_1r² = 7   (1)

G_1r³ + G_1r⁴ + G_1r⁵ = 56   (2)

(p.34)

From (2),

r³(G_1 + G_1r + G_1r²) = 56

Substituting (1),

7r³ = 56

r³ = 8

r = 2

Then,

G_1 + 2G_1 + 4G_1 = 7

7G_1 = 7

G_1 = 1

Therefore, the common ratio is 2, and the 1st term is 1.

[added step: r³ = 56/7 = 8, and the only real cube root of 8 is 2. Check: 1 + 2 + 4 = 7 and 8 + 16 + 32 = 56 ✓]

### Exercise 1.17

1. The sum of the first three terms of a geometric sequence is 9, and the sum from the 4th to 6th term is −18. Find the first term and common ratio.

**Answer:** r = −∛2, G_1 = 9/(1 − ∛2 + ∛4) = 3(1 + ∛2) ≈ 6.78

**Why:**
G_1 + G_1r + G_1r² = 9 … (1)
G_1r³ + G_1r⁴ + G_1r⁵ = −18 … (2)
Factor (2): r³(G_1 + G_1r + G_1r²) = −18
Substitute (1): 9r³ = −18
r³ = −18/9 = −2
r = ∛(−2) = −∛2 (≈ −1.2599)
From (1): G_1(1 + r + r²) = 9
r² = (−∛2)² = ∛4
G_1(1 − ∛2 + ∛4) = 9
G_1 = 9/(1 − ∛2 + ∛4)
Simplify: use (a + b)(a² − ab + b²) = a³ + b³ with a = 1, b = ∛2:
(1 + ∛2)(1 − ∛2 + ∛4) = 1 + 2 = 3, so 1/(1 − ∛2 + ∛4) = (1 + ∛2)/3
G_1 = 9 × (1 + ∛2)/3 = 3(1 + ∛2) ≈ 3 × 2.2599 ≈ 6.780
Check (decimals): 1 + r + r² ≈ 1 − 1.2599 + 1.5874 = 1.3275; 6.780 × 1.3275 ≈ 9.00 ✓; r³ × 9 = −2 × 9 = −18 ✓
[review: the numbers in this question do not give a "nice" answer (r is the irrational −∛2); please confirm the question is printed as intended — the worked example on p.33–34 with 7 and 56 gives r = 2.]

2. How many terms of the sequence: 3, 3/2, 3/4, 3/8, … are needed to give the sum 3069/512?

**Answer:** 10 terms

**Why:**
G_1 = 3, r = (3/2) ÷ 3 = 1/2
S_n = G_1(1 − r^n)/(1 − r) = 3(1 − (1/2)^n)/(1/2) = 6(1 − 1/2^n)
Set 6(1 − 1/2^n) = 3069/512
1 − 1/2^n = 3069/(512 × 6) = 3069/3072
1/2^n = 1 − 3069/3072 = 3/3072 = 1/1024 (dividing top and bottom by 3)
2^n = 1024 = 2¹⁰
n = 10
Check: S_10 = 6(1 − 1/1024) = 6 × 1023/1024 = 6138/1024 = 3069/512 (dividing top and bottom by 2) ✓

3. Find the sum to indicated number of terms in each of the geometric sequence in questions a to d:
   a. 0.15, 0.015, 0.0015, … n terms.
   b. √7, √21, 3√7, … n terms.
   b. 1, −a, a², −a³, … n terms (if a ≠ −1).
   d. x³, x⁵, x⁷, … n terms (if x ≠ ±1).

[review: the book labels the parts a, b, b, d — the second "b" (1, −a, a², −a³, …) should be "c". Kept as printed; answered below as "b (second)".]

**3a. Answer:** S_n = (1/6)(1 − (0.1)^n) = (1 − 10^(−n))/6

**Why:**
G_1 = 0.15, r = 0.015/0.15 = 0.1
S_n = G_1(1 − r^n)/(1 − r) = 0.15(1 − (0.1)^n)/(1 − 0.1)
= 0.15(1 − (0.1)^n)/0.9
0.15/0.9 = 15/90 = (15÷15)/(90÷15) = 1/6
S_n = (1/6)(1 − (0.1)^n)
Check: n = 2 → 0.15 + 0.015 = 0.165; (1/6)(1 − 0.01) = 0.99/6 = 0.165 ✓

**3b. Answer:** S_n = √7((√3)^n − 1)/(√3 − 1) = (√7(√3 + 1)/2)((√3)^n − 1)

**Why:**
G_1 = √7, r = √21/√7 = √(21/7) = √3 (also 3√7/√21 = 3/√3 = √3)
r ≠ 1, so S_n = G_1(r^n − 1)/(r − 1) = √7((√3)^n − 1)/(√3 − 1)
Rationalise: 1/(√3 − 1) = (√3 + 1)/((√3 − 1)(√3 + 1)) = (√3 + 1)/(3 − 1) = (√3 + 1)/2
S_n = (√7(√3 + 1)/2)((√3)^n − 1)
Check: n = 2 → √7 + √21; formula √7(3 − 1)/(√3 − 1) = 2√7/(√3 − 1) = √7(√3 + 1) = √21 + √7 ✓

**3b (second, i.e. c). Answer:** S_n = (1 − (−a)^n)/(1 + a)

**Why:**
G_1 = 1, r = −a/1 = −a
r ≠ 1 because a ≠ −1
S_n = G_1(1 − r^n)/(1 − r) = (1 − (−a)^n)/(1 − (−a)) = (1 − (−a)^n)/(1 + a)
Check: n = 2 → 1 − a; formula (1 − a²)/(1 + a) = (1 − a)(1 + a)/(1 + a) = 1 − a ✓

**3d. Answer:** S_n = x³(1 − x^(2n))/(1 − x²) = x³(x^(2n) − 1)/(x² − 1)

**Why:**
G_1 = x³, r = x⁵/x³ = x²
r ≠ 1 because x ≠ ±1
r^n = (x²)^n = x^(2n)
S_n = G_1(1 − r^n)/(1 − r) = x³(1 − x^(2n))/(1 − x²)
Check: n = 2 → x³ + x⁵; formula x³(1 − x⁴)/(1 − x²) = x³(1 − x²)(1 + x²)/(1 − x²) = x³(1 + x²) = x³ + x⁵ ✓

(p.35)

## 1.4 Infinite Series

### Activity 1.7

Supposing that a tree grows by half its height in a year. It then grows half of the amount of the previous year. What would be the height of the tree be if it continues to grow at the same rate?

[figure: Figure 1.5 — three trees of increasing height; the first tree has height 1, the second is taller by 1/2, the third taller again by 1/4 (heights 1, 1 + 1/2, 1 + 1/2 + 1/4).]

**Answer:** The height approaches 2 times the original height (height → 2 if the original height is 1).

**Why:**
Height = 1 + 1/2 + 1/4 + 1/8 + … (geometric, G_1 = 1, r = 1/2)
|r| = 1/2 < 1, so the sum to infinity exists
S_∞ = G_1/(1 − r) = 1/(1 − 1/2) = 1/(1/2) = 2
Check with partial sums: 1, 1.5, 1.75, 1.875, 1.9375, … get closer and closer to 2 but never pass it ✓

Suppose we have the sequence: a_1, a_2, a_3, …, a_n, …

An infinite sum of the form: a_1 + a_2 + a_3 + … + a_n + … is called an infinite series and using summation, we can write as: a_1 + a_2 + a_3 + … + a_n + … = ∑_{n=1}^{∞} a_n

### 1.4.1. Divergence and Convergence of Infinite Sequence

### Activity 1.8

For each of the sequences i − v:
a. Write the formula for the nth term.
b. Find the sum where the sequence converges.

i. 1, 2, 3, 4, …
ii. 1/2, 1/4, 1/8, 1/16, …
iii. −1, 1, −1, 1, …
iv. 1, 1.5, 2.25, 3.375, …
v. 0.12, 0.0012, 0.000012, 0.00000012, …

[review: part b says "where the sequence converges", but what has a sum is the series. Read as: find the sum of the infinite series when that sum exists.]

**i. Answer:** a. a_n = n. b. No sum: 1 + 2 + 3 + … grows without bound (diverges to ∞).

**Why:**
Each term is 1 more than the last, and the first term is 1, so a_n = 1 + (n − 1)(1) = n
Partial sums S_n = n(n + 1)/2 → ∞ as n → ∞, so the series diverges

**ii. Answer:** a. a_n = 1/2^n = (1/2)^n. b. Sum = 1.

**Why:**
G_1 = 1/2, r = (1/4) ÷ (1/2) = 1/2, so a_n = (1/2)(1/2)^(n−1) = (1/2)^n
|r| = 1/2 < 1, so S_∞ = G_1/(1 − r) = (1/2)/(1 − 1/2) = (1/2)/(1/2) = 1
Check: partial sums 1/2, 3/4, 7/8, 15/16, … = 1 − 1/2^n → 1 ✓

**iii. Answer:** a. a_n = (−1)^n. b. No sum: the series vibrates (diverges).

**Why:**
n = 1 gives (−1)¹ = −1, n = 2 gives (−1)² = 1, … ✓
r = −1, so r ≤ −1
Partial sums are −1, 0, −1, 0, … and keep jumping back and forth, so there is no limit

**iv. Answer:** a. a_n = (1.5)^(n−1) = (3/2)^(n−1). b. No sum: the series diverges to ∞.

**Why:**
G_1 = 1, r = 1.5/1 = 1.5 (also 2.25/1.5 = 1.5, 3.375/2.25 = 1.5)
a_n = 1 × (1.5)^(n−1)
r = 1.5 > 1, so the terms grow and S_n → ∞

**v. Answer:** a. a_n = 0.12(0.01)^(n−1) = 12/100^n. b. Sum = 4/33 (= 0.121212…).

**Why:**
G_1 = 0.12, r = 0.0012/0.12 = 0.01
a_n = 0.12 × (0.01)^(n−1) = 12/100 × 1/100^(n−1) = 12/100^n
|r| = 0.01 < 1, so S_∞ = G_1/(1 − r) = 0.12/(1 − 0.01) = 0.12/0.99
0.12/0.99 = 12/99 = (12÷3)/(99÷3) = 4/33
Check: 0.12 + 0.0012 + 0.000012 + … = 0.121212… and 4/33 = 0.121212… ✓

(p.36)

For an infinite sequence, there are cases of convergence and divergence, when n approaches to infinity, as follows:

**Convergence**

a. Sequence a_n converges to α: n → ∞, a_n → α

**Divergence**

b. Sequence a_n diverges to positive infinity: n → ∞, a_n → ∞.
c. Sequence a_n diverges to negative infinity: n → ∞, a_n → −∞.
d. Sequence a_n vibrates: a_n has no limit. i.e. the value oscillate or vibrate back and forth between numbers.

**Divergence/convergence of infinite geometric sequence**

Considering infinite geometric sequence G_n = r^n, where G_1 = r, and the common ratio is r, there are cases of convergence and divergence, when n approaches to infinity, as follows:

i) r > 1, When n → ∞, then G_n → ∞ (diverge)
ii) r = 1, When n → ∞, then G_n → 1 (converge)
iii) |r| < 1, When n → ∞, then G_n → 0 (converge)
iv) r ≤ −1, When n → ∞, then G_n vibrates (no limit, diverge).

### Example

Find whether the given geometric sequences diverge, converge or vibrate as n approaches to infinity.

a. G_n = (√2)^n
b. G_n = (2/3)^n
c. G_n = (−3)^n

**Solution**

a. G_n = (√2)^n

As √2 > 1, when n → ∞, then G_n → ∞, it diverges.

(p.37)

b. G_n = (2/3)^n

As |2/3| < 1, when n → ∞, then G_n → 0, it diverges.

[review: book says "it diverges", working gives "it converges (to 0)" because |2/3| < 1 is case iii) on p.36, G_n → 0.]

c. G_n = (−3)^n

As −3 ≤ −1, when n → ∞, then G_n vibrates

[added step: (−3)^n = −3, 9, −27, 81, … — the sign alternates and the size grows, so there is no limit.]

### Exercise 1.18

Find whether the given geometric sequences diverge, converge or vibrates as n approaches infinity.

a. G_n = (√3)^n
b. G_n = (3/4)^n
c. G_n = (−1/2)^n

**a. Answer:** Diverges (to ∞).

**Why:**
r = √3 ≈ 1.732
√3 > 1 (case i), so as n → ∞, G_n → ∞
Check: (√3)² = 3, (√3)⁴ = 9, (√3)⁶ = 27, … growing without bound ✓

**b. Answer:** Converges (to 0).

**Why:**
r = 3/4
|3/4| < 1 (case iii), so as n → ∞, G_n → 0
Check: (3/4)¹⁰ ≈ 0.056, (3/4)²⁰ ≈ 0.0032 → shrinking towards 0 ✓

**c. Answer:** Converges (to 0). It alternates in sign, but it does not "vibrate" in the book's sense because it has a limit.

**Why:**
r = −1/2
|−1/2| = 1/2 < 1 (case iii), so as n → ∞, G_n → 0
Terms: −1/2, 1/4, −1/8, 1/16, … the sign alternates but the size halves each time, so the terms get closer and closer to 0
Note: "vibrates" (case iv) is only for r ≤ −1; here r = −1/2 > −1

### Infinite series

### Definition 1.5

Let {a_n}_{n=1}^{∞} be a sequence and S_n be the nth partial sum such that, as n gets larger and larger, S_n tends to s, where s is a real number, then we say the infinite series ∑_{n=1}^{∞} a_n converges and is written as ∑_{n=1}^{∞} a_n = s.

However, if such an s does not exist or is infinite, we say the infinite series ∑_{n=1}^{∞} a_n diverges.

Let us consider the geometric sequence 1, 2/3, 4/9, … where G_1 = 1 and r = 2/3. We have partial sum,

(p.38)

S_n = G_1(1 − r^n)/(1 − r) = 1(1 − (2/3)^n)/(1 − 2/3) = 3[1 − (2/3)^n]

[added step: 1 − 2/3 = 1/3, and dividing by 1/3 is multiplying by 3.]

Let us study the behavior of (2/3)^n as n becomes larger and larger, approaching to infinity.

| n | 1 | 5 | 10 | 20 |
|---|---|---|---|---|
| (2/3)^n | 0.6667 | 0.1316872428 | 0.01734152992 | 0.00030072866 |

We observe that as n becomes larger and larger, (2/3)^n becomes closer and closer to zero. Mathematically, we say that as n becomes increasingly large, (2/3)^n becomes increasingly small. In other words, as n → ∞, (2/3)^n → 0. Consequently, we find set on the line below the sum of infinitely many terms of the sequence above is S = 3.

[review: the phrase "we find set on the line below" is printed as-is; it appears garbled in the book. Meaning: the sum of infinitely many terms is S = 3.]

Thus, for an infinite geometric sequence G_1, G_1r, G_1r², …, if numerical value of the common ratio r is between −1 and 1, then S_n = G_1(1 − r^n)/(1 − r) = G_1/(1 − r) − G_1r^n/(1 − r).

In this case, r^n → 0 as n → ∞ since |r| < 1 and then G_1r^n/(1 − r) → 0. Therefore, S_n → G_1/(1 − r) as n → ∞. Symbolically, the sum to infinity of an infinite geometric series is denoted by S_∞. Thus, we have S_∞ = G_1/(1 − r).

(p.39)

### Note

Recall that if ∑_{n=1}^{∞} G_1 r^(n−1) = G_1 + G_1r + G_1r² + … is a geometric series with first term G_1 and common ratio r, then S_n = G_1(1 − r^n)/(1 − r) = G_1/(1 − r) − G_1r^n/(1 − r).

(i) If |r| < 1, as n → ∞, r^n → 0 so that S_n = G_1/(1 − r) − G_1r^n/(1 − r) → G_1/(1 − r), S_∞ = G_1/(1 − r).

(ii) If |r| ≥ 1, then the series diverges or vibrates as follows.

a. If r = 1, then ∑_{k=1}^{n} G_k = nG_1, when n → ∞, ∑_{k=1}^{∞} G_k = ∞ (G_1 > 0)
   ∑_{k=1}^{∞} G_k = −∞ (G_1 < 0)

b. If r ≠ 1, then S_n = ∑_{k=1}^{∞} G_k = G_1(1 − r^n)/(1 − r)
   Then, If r ≤ −1, when n → ∞, then ∑_{k=1}^{∞} G_k vibrates,
   If r > 1, when n → ∞, then ∑_{k=1}^{∞} G_k = ∞ (G_1 > 0)
   ∑_{k=1}^{∞} G_k = −∞ (G_1 < 0)

[review: in part b the book writes S_n = ∑_{k=1}^{∞} G_k; the upper limit should be n (S_n = ∑_{k=1}^{n} G_k). Transcribed as printed.]

### Example 1

Determine whether the series ∑_{n=1}^{∞} 3^n converges or diverges.

**Solution**

The series ∑_{n=1}^{∞} 3^n = 3 + 9 + 27 + … + … is a geometric series with first term G_1 = 3 and common ratio r = 3.

Hence, the partial sum is given by S_n = G_1(1 − r^n)/(1 − r)

(p.40)

Substituting the values, we obtain,

S_n = G_1(1 − r^n)/(1 − r) = 3[1 − 3^n]/(1 − 3) = −(3/2)[1 − 3^n] = −3/2 + (3/2)3^n.

Thus, as n → ∞, S_n → ∞. Therefore, the series diverges.

[added step: 1 − 3 = −2, so 3/(−2) = −3/2; as n → ∞, 3^n → ∞, so (3/2)3^n → ∞ and S_n → ∞.]

### Example 2

Find the sum of the geometric series 5 − 10/3 + 20/9 − 40/27 + …

**Solution**

The geometric series has the first term G_1 = 5 and the common ratio r = (−10/3)/5 = −2/3.

Since |r| = |−2/3| = 2/3 < 1, then the series converges and its sum is given by

S_∞ = 5 − 10/3 + 20/9 − 40/27 + … = G_1/(1 − r) = 5/(1 − (−2/3)) = 5/(5/3) = 3.

[review: on the page the line "then the series converges and its sum is given by" is printed below the formula for S_∞ (layout slip); reordered here into reading order, wording unchanged.]

[added step: (−10/3) ÷ 5 = −10/15 = −2/3; 1 − (−2/3) = 1 + 2/3 = 5/3; 5 ÷ (5/3) = 5 × 3/5 = 3.]

### Exercise 1.19

Find the sum for each of the following, if it exists, assuming the patterns continue as in the first few terms.

a. 3 + 1 + 1/3 + 1/9 + …
b. 1 + 3/4 + 9/16 + 27/64 + …
c. 1/5 + 1/10 + 1/20 + …
d. 1/5 + (−1)/10 + 1/20 + (−1)/40 + …
e. 7 + 7/10 + 7/100 + 7/1000 + …

**a. Answer:** 9/2

**Why:**
G_1 = 3, r = 1/3 (1 ÷ 3 = 1/3; (1/3) ÷ 1 = 1/3)
|r| = 1/3 < 1, so the sum exists
S_∞ = G_1/(1 − r) = 3/(1 − 1/3) = 3/(2/3) = 3 × 3/2 = 9/2
Check: partial sums 3, 4, 4.333, 4.444, 4.481, … → 4.5 = 9/2 ✓

**b. Answer:** 4

**Why:**
G_1 = 1, r = (3/4) ÷ 1 = 3/4 (also (9/16) ÷ (3/4) = 9/16 × 4/3 = 36/48 = 3/4)
|r| = 3/4 < 1, so the sum exists
S_∞ = 1/(1 − 3/4) = 1/(1/4) = 4
Check: partial sums 1, 1.75, 2.3125, 2.734, … S_n = 4(1 − (3/4)^n) → 4 ✓

**c. Answer:** 2/5

**Why:**
G_1 = 1/5, r = (1/10) ÷ (1/5) = 1/10 × 5/1 = 5/10 = 1/2
|r| = 1/2 < 1, so the sum exists
S_∞ = (1/5)/(1 − 1/2) = (1/5)/(1/2) = 1/5 × 2/1 = 2/5
Check: 1/5 = 0.2, partial sums 0.2, 0.3, 0.35, 0.375, … → 0.4 = 2/5 ✓

**d. Answer:** 2/15

**Why:**
G_1 = 1/5, r = (−1/10) ÷ (1/5) = −1/10 × 5/1 = −5/10 = −1/2
|r| = 1/2 < 1, so the sum exists
S_∞ = (1/5)/(1 − (−1/2)) = (1/5)/(3/2) = 1/5 × 2/3 = 2/15
Check: 2/15 ≈ 0.1333; partial sums 0.2, 0.1, 0.15, 0.125, 0.1375, … close in on 0.1333 from both sides ✓

**e. Answer:** 70/9 (= 7.777…)

**Why:**
G_1 = 7, r = (7/10) ÷ 7 = 1/10
|r| = 1/10 < 1, so the sum exists
S_∞ = 7/(1 − 1/10) = 7/(9/10) = 7 × 10/9 = 70/9
Check: 7 + 0.7 + 0.07 + 0.007 + … = 7.777… and 70/9 = 7.777… ✓

(p.41)

### Further on infinite series

### Example 1

Find the sum ∑_{k=1}^{∞} 5^(3−k)

**Solution**

5^(3−k) = 5³ × 5^(−k) = 5³(1/5)^k = 5²(1/5)^(k−1)

It is a geometric series whose first term G_1 = 25 and the common ratio r = 1/5.

Therefore, the sum becomes:

S_∞ = ∑_{k=1}^{∞} 5^(3−k) = 5² + 5¹ + 5⁰ + 5^(−1) + … = G_1/(1 − r) = 25/(1 − 1/5) = 125/4

[added step: 5³(1/5)^k = 5³ × (1/5) × (1/5)^(k−1) = 5²(1/5)^(k−1); 1 − 1/5 = 4/5; 25 ÷ (4/5) = 25 × 5/4 = 125/4.]

### Example 2

Find the sum ∑_{k=1}^{∞} (−1)^(k+1) (2/3)^k

**Solution**

(−1)^(k+1)(2/3)^k = (−1)^k(−1)(2/3)^k = (−1)(−2/3)^k = −(−2/3)^k

It is a geometric series whose first term G_1 = 2/3 and the common ratio r = −2/3.

Therefore, the sum becomes

S_∞ = ∑_{k=1}^{∞} (−1)^(k+1)(2/3)^k = 2/3 − (2/3)² + (2/3)³ − (2/3)⁴ + … = G_1/(1 − r) = (2/3)/(1 − (−2/3)) = 2/5

[added step: first term (k = 1): (−1)²(2/3)¹ = 2/3; 1 − (−2/3) = 5/3; (2/3) ÷ (5/3) = 2/3 × 3/5 = 2/5.]

(p.42)

### Exercise 1.20

Find the sums for each of these geometric series

a. ∑_{k=1}^{∞} 5(1/3)^(k−1)
b. ∑_{k=1}^{∞} 2^(1−k)
c. ∑_{k=1}^{∞} 5^(k−3)
d. ∑_{k=1}^{∞} (3/4)^(k+3) (2/3)^(k−2)

**a. Answer:** 15/2

**Why:**
k = 1: 5(1/3)⁰ = 5, so G_1 = 5
r = 1/3 (the base of the power k − 1)
|r| = 1/3 < 1, so the sum exists
S_∞ = 5/(1 − 1/3) = 5/(2/3) = 5 × 3/2 = 15/2
Check: 5 + 5/3 + 5/9 + … ; partial sums 5, 6.667, 7.222, 7.407, … → 7.5 ✓

**b. Answer:** 2

**Why:**
2^(1−k) = 2^(−(k−1)) = (1/2)^(k−1)
k = 1: (1/2)⁰ = 1, so G_1 = 1, r = 1/2
|r| < 1, so S_∞ = 1/(1 − 1/2) = 1/(1/2) = 2
Check: 1 + 1/2 + 1/4 + 1/8 + … = 2 ✓

**c. Answer:** The sum does not exist — the series diverges (to ∞).

**Why:**
5^(k−3) = 5^(−2) × 5^(k−1) = (1/25)(5)^(k−1)
G_1 = 1/25, r = 5
r = 5 > 1 and G_1 > 0, so S_n = (1/25)(5^n − 1)/(5 − 1) = (5^n − 1)/100 → ∞
Terms: 1/25, 1/5, 1, 5, 25, … grow without bound

**d. Answer:** 243/256

**Why:**
Split the powers so each has exponent (k − 1):
(3/4)^(k+3) = (3/4)⁴ × (3/4)^(k−1)
(2/3)^(k−2) = (2/3)^(−1) × (2/3)^(k−1) = (3/2) × (2/3)^(k−1)
Product = (3/4)⁴ × (3/2) × ((3/4)(2/3))^(k−1)
(3/4)(2/3) = 6/12 = 1/2, so r = 1/2
G_1 = (3/4)⁴ × 3/2 = (81/256) × (3/2) = 243/512
|r| < 1, so S_∞ = (243/512)/(1 − 1/2) = (243/512)/(1/2) = 243/512 × 2 = 486/512 = 243/256 (dividing top and bottom by 2)
Check: k = 2 term = (3/4)⁵(2/3)⁰ = 243/1024 = G_1 × 1/2 ✓; sum ≈ 0.949, and partial sums 0.4746, 0.7119, 0.8306, … → 0.9492 ✓

### 1.4.2. Recurring Decimals

Recurring or repeating decimals are rational numbers (fractions) whose representations as a decimal contain a pattern of digit that repeats indefinitely after decimal point. The decimal that start their recurring cycle immediately after the decimal point are called **purely recurring decimals.**

Purely recurring decimals are converted to an irreducible fraction whose prime factors in the denominator can only be the prime numbers other than 2 or 5, i.e. the prime numbers from the sequence {3, 7, 11, 13, 17, 19, …}. The decimals that have some extra digits before the repeating the sequence of digits are called the **mixed recurring decimals**.

The repeating sequence may consist of just one digit or of any finite number of digits. The number of digits in the repeating pattern is called **the period.**

Mixed requiring decimals are converted to an irreducible fraction whose denominator is a product of 2's and/or 5's besides the prime numbers from the sequence {3, 7, 11, 13, 17, 19, …}.

All recurring decimals are infinite decimals.

[review: "Mixed requiring decimals" is a misprint in the book for "Mixed recurring decimals"; kept as printed.]

### Converting purely recurring decimals to fraction

### Example 1

Convert the recurring decimal 0.3̇ to a fraction.

(p.43)

**Solution**

We can write the given decimal as the sum of the infinite converging geometric series as follows:

0.3̇ = 0.333333… = 0.3 + 0.03 + 0.003 + …
= 3/10 + 3/100 + 3/1000 + …

This is the infinite geometric series, where G_1 = 3/10 and r = (3/100)/(3/10) = 1/10

Since, |r| < 1 then S_∞ = G_1/(1 − r) = (3/10)/(1 − 1/10) = (3/10)/(9/10) = 1/3

[added step: (3/10) ÷ (9/10) = 3/10 × 10/9 = 3/9 = 1/3.]

### Example 2

Convert the recurring decimal 0.4̇7̇ to a fraction.

**Solution**

We can write the given recurring decimal as the sum of the infinite converging geometric series as follows:

0.4̇7̇ = 0.474747… = 0.47 + 0.0047 + 0.000047 + …
= 47/100 + 47/10000 + 47/1000000 + …

Since, r = G_n/G_(n−1) = 1/100, |r| < 1 then S_∞ = G_1/(1 − r),

Therefore, by substituting G_1 = 47/100 and r = 1/100 in to the formula:

0.4̇7̇ = G_1/(1 − r) = (47/100)/(1 − 1/100) = (47/100)/(99/100) = 47/99

[added step: (47/100) ÷ (99/100) = 47/100 × 100/99 = 47/99.]

(p.44)

Notice that when converting a recurring decimal that is less than one to a fraction, we write the repeating digits to the numerator and in the denominator of the equivalent fraction write as many 9's as is the number of digits in the repeating pattern.

### Exercise 1.21

Convert the following recurring decimals to fractions.

a. 0.4̇
b. 3.7̇
c. 0.5̇6̇

**a. Answer:** 4/9

**Why:**
0.4̇ = 0.444… = 4/10 + 4/100 + 4/1000 + …
G_1 = 4/10, r = (4/100) ÷ (4/10) = 1/10, |r| < 1
S_∞ = (4/10)/(1 − 1/10) = (4/10)/(9/10) = 4/10 × 10/9 = 4/9
Check: 4 ÷ 9 = 0.444… ✓ (also the "9's rule": one repeating digit 4 → 4/9 ✓)

**b. Answer:** 34/9

**Why:**
3.7̇ = 3 + 0.777…
0.777… = 7/10 + 7/100 + … ; G_1 = 7/10, r = 1/10
S_∞ = (7/10)/(9/10) = 7/9
3.7̇ = 3 + 7/9 = (3×9)/(1×9) + 7/9 = 27/9 + 7/9 = 34/9
Check: 34 ÷ 9 = 3.777… ✓

**c. Answer:** 56/99

**Why:**
0.5̇6̇ = 0.565656… = 56/100 + 56/10000 + 56/1000000 + …
G_1 = 56/100, r = (56/10000) ÷ (56/100) = 1/100, |r| < 1
S_∞ = (56/100)/(1 − 1/100) = (56/100)/(99/100) = 56/100 × 100/99 = 56/99
56 = 2³ × 7 and 99 = 3² × 11 share no common factor, so 56/99 is in lowest terms
Check: 56 ÷ 99 = 0.565656… ✓

## 1.5 Applications of Sequence and Series in Daily Life

This section is devoted to the application of arithmetic and geometric progressions or geometric series that are associated with real-life situations.

### Activity 1.9

1. A man accepts a position with an initial salary of 5200 ETB per month. It is understood that he will receive an automatic increase of 320 ETB in the very next month and each month thereafter.
   a. Find his salary for the tenth month.
   b. What are his total earnings during the first year?
2. A carpenter was hired to build 192 window frames. The first day he/she made five frames and each day, thereafter he/she made two more frames than he/she made the day before. How many days did it take him/her to finish the job?

**1a. Answer:** 8080 ETB

**Why:**
Monthly salaries form an arithmetic sequence: A_1 = 5200, d = 320
A_n = A_1 + (n − 1)d
A_10 = 5200 + (10 − 1)(320)
A_10 = 5200 + 9 × 320 = 5200 + 2880 = 8080
Check: list 5200, 5520, 5840, 6160, 6480, 6800, 7120, 7440, 7760, 8080 → 10th is 8080 ✓

**1b. Answer:** 83 520 ETB

**Why:**
First year = 12 months, n = 12
A_12 = 5200 + 11 × 320 = 5200 + 3520 = 8720
S_12 = (12/2)(A_1 + A_12) = 6(5200 + 8720) = 6 × 13920 = 83 520
Check with the other formula: S_12 = (12/2)[2(5200) + 11(320)] = 6[10400 + 3520] = 6 × 13920 = 83 520 ✓

**2. Answer:** 12 days

**Why:**
Frames per day: 5, 7, 9, … arithmetic with A_1 = 5, d = 2
S_n = (n/2)[2A_1 + (n − 1)d] = 192
(n/2)[10 + 2(n − 1)] = 192
(n/2)[10 + 2n − 2] = 192
(n/2)(2n + 8) = 192
n(n + 4) = 192
n² + 4n − 192 = 0
(n + 16)(n − 12) = 0 (since 16 × (−12) = −192 and 16 − 12 = 4)
n = −16 or n = 12; a number of days must be positive, so n = 12
Check: A_12 = 5 + 11 × 2 = 27; S_12 = (12/2)(5 + 27) = 6 × 32 = 192 ✓

Here are some examples followed by exercises. They illustrate some useful applications.

(p.45)

### Example 1

Observe the pattern in Figure 1.5:

a. If the pattern continues, find the number of letters in the column containing the letter M.
b. If the total number of letters in the pattern is 361, which letter will be in the last column?

[figure: Figure 1.5 — letters arranged in columns inside a triangle opening to the right: column A has 1 letter, column B has 3 letters (B B B), column C has 5 letters (C C C C C), column D has 7 letters (D D D D D D D).]

[review: the book numbers this figure "Figure 1.5", the same number already used for the tree figure in Activity 1.7 (p.35). Kept as printed.]

**Solution**

a. If you observe the structure of the letters in figure 1.5, it is of the form: 1, 3, 5, 7, 9, …

This is an arithmetic series with first term A_1 = 1 and common difference d = 2. Therefore, the n term of the arithmetic sequence is given by

A_n = A_1 + (n − 1)d

For the letter M: n = 13;

A_13 = A_1 + (n − 1)d = 1 + (13 − 1)(2) = 1 + (12)(2) = 25.

[added step: M is the 13th letter of the alphabet (A = 1, B = 2, …, M = 13).]

b.

S_n = (n/2)[2A_1 + (n − 1)d]

361 = (n/2)[2(1) + (n − 1)(2)]

361 = n[1 + n − 1]

361 = n²

n = ±19 (as n > 0)

∴ n = 19

So, the letter "S" will be in the last column.

[added step: (n/2)[2 + 2(n − 1)] = (n/2) × 2[1 + (n − 1)] = n × n; √361 = 19; the 19th letter of the alphabet is S.]

(p.46)

### Example 2

A theatre is filling up at a rate of 4 people in the first minute, 6 people in the second minute and 8 people in the third minute and so on. After 6 minutes, the theatre is half full. After how many minutes will the theatre be full?

**Solution**

The structure of the problem has an infinite arithmetic series of the form: 4 + 6 + 8 + …

So, the common difference of the problem is calculated as

d = A_2 − A_1 = A_3 − A_2 = 2

Therefore, the sum of arithmetic series whose first term A_1 = 4 and common difference d = 2, is written as

S_n = (n/2)[2A_1 + (n − 1)d] ⇒ S_6 = (6/2)[2(4) + (6 − 1)(2)] = 3(18) = 54 (theatre half full).

Therefore, the capacity of the theatre is 2 × 54 = 108

S_n = (n/2)[2A_1 + (n − 1)d]

108 = (n/2)[2(4) + (n − 1)(2)]

216 = n[8 + 2n − 2]

2n² + 6n − 216 = 0

n² + 3n − 108 = 0

(n + 12)(n − 9) = 0

∴ n = −12 or n = 9, where n must be a positive integer.

Therefore, n = 9. It takes 9 minutes for the theatre to be full.

[added step: 2(4) + 5(2) = 8 + 10 = 18; multiply both sides by 2 to get 216 = n(2n + 6) = 2n² + 6n; divide by 2 to get n² + 3n − 108 = 0; 12 × (−9) = −108 and 12 − 9 = 3. Check: S_9 = (9/2)[8 + 16] = (9/2)(24) = 108 ✓]

(p.47)

### Example 3

A job applicant finds that a firm offers a starting annual salary of Birr 32,500 with a guaranteed raise of Birr 1,400 per year.

a. What would the annual salary be in the tenth year?
b. How much would be earned at the firm over the first 10 years?

**Solution**

a. The annual salary at the firm forms the arithmetic sequence;

32,500, 33,900, 35,300, … with first term A_1 = 32,500 and common difference d = 1,400. Thus, A_n = A_1 + (n − 1)d, substituting the values we obtain;

A_10 = 32,500 + (10 − 1)(1,400) = Birr 45,100

[added step: 9 × 1,400 = 12,600; 32,500 + 12,600 = 45,100.]

b. To determine the amount that would be earned over the first 10 years, we need to add the first 10 annual salaries;

S_10 = A_1 + A_2 + A_3 + … + A_10 = 10((A_1 + A_10)/2) (It is 10 times the average of the first and the last term.)

S_10 = (10/2)(32,500 + 45,100) = Birr 388,000

Therefore, a total of Birr 388,000 would be earned at the firm over the first 10 years.

[added step: 32,500 + 45,100 = 77,600; 5 × 77,600 = 388,000.]

### Exercise 1.22

1. A person is scheduled to get a raise of Birr 250 every 6 months during his/her first 5 years on the job. If their starting salary is Birr 25,250 per year, what will his/her annual salary be at the end of the 3rd year?

**Answer:** Birr 26,750 per year

**Why:**
The annual salary after each 6-month period forms an arithmetic sequence with A_1 = 25,250 and d = 250
In 3 years there are 3 × 2 = 6 half-year periods, so by the end of the 3rd year there have been 6 raises
Salary after 6 raises = A_7 = A_1 + (7 − 1)d = 25,250 + 6 × 250 = 25,250 + 1,500 = 26,750
Check: 25,250 → 25,500 (6 months) → 25,750 (1 yr) → 26,000 (1.5 yr) → 26,250 (2 yr) → 26,500 (2.5 yr) → 26,750 (3 yr) ✓
[review: wording is ambiguous — if the raise "at" the 3-year mark is not yet counted (salary during the last half of year 3), the answer is 25,250 + 5 × 250 = Birr 26,500. Working above counts the raise received at the end of the 3rd year, giving 26,750.]

2. Bontu begins a saving program in which she will save Birr 1,000 the first year. Each subsequent year, she will save 200 more than she did the previous year. How much will she save during the eighth year?

**Answer:** Birr 2,400

**Why:**
Savings per year: arithmetic with A_1 = 1,000, d = 200
A_n = A_1 + (n − 1)d
A_8 = 1,000 + (8 − 1)(200) = 1,000 + 7 × 200 = 1,000 + 1,400 = 2,400
Check: 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400 → 8th is 2,400 ✓

(p.48)

### Example 4

A woman deposits Birr 3,500 in a bank account paying an annual interest at a rate of 6%. Show that whether the amounts she has in the account at the end of each year form a geometric sequence.

**Solution**

Let G_1 = 3,500. Then,

G_2 = G_1 + (6/100)G_1 = G_1(1 + 0.06) = G_1(1.06)

G_3 = G_2 + (6/100)G_2 = G_2(1 + 0.06) = G_1(1.06)(1.06) = G_1(1.06)²

G_4 = G_3 + (6/100)G_3 = G_3(1 + 0.06) = G_1(1.06)²(1.06) = G_1(1.06)³

Continuing in this way, you get G_n = G_1(1.06)^(n−1)

Since the ratio of any two consecutive terms is a constant, which is 1.06, this sequence is a geometric sequence.

[review: in this solution G_1 = 3,500 is the deposit itself, so G_2 is the amount at the end of year 1 and G_n is the amount at the end of year n − 1. Exercise 1.23 Q4 asks for "the amount at the end of the nth year", which is 3,500(1.06)^n — students may mix up the two indexings.]

### Example 5

Suppose a radioactive substance loses half of its mass per year. If we start with 100 grams of a radioactive substance, how much will be left after 10 years?

**Solution**

Let us record the amount of the radioactive substance left after each year starting with G_0 = 100. Note that each term is half of the previous term and hence,

G_1 = (1/2)G_0 = 100(1/2) is the amount left at the end of year 1.

G_2 = (1/2)G_1 = 100(1/2)² is the amount left at the end of year 2.

(p.49)

G_3 = (1/2)G_2 = 100(1/2)³ is the amount left at the end of year 3.

If you continue in this way, you see that the ratio of any two consecutive terms is a constant, which is 1/2, and hence this sequence is a geometric sequence.

Therefore, after ten years, the amount of the substance left is given by:

G_10 = G_0(1/2)¹⁰ = 100(1/2)¹⁰ = 100/1,024 = 0.09765625 g.

[added step: 2¹⁰ = 1,024; 100 ÷ 1,024 = 0.09765625.]

### Exercise 1.23

1. A certain item loses one-tenth of its value each year. If the item is worth Birr 28,000 today, how much will it worth 4 years from now?

**Answer:** Birr 18,370.80

**Why:**
Each year the value keeps 1 − 1/10 = 9/10 = 0.9 of the previous value, so the values form a geometric sequence with ratio r = 0.9
Value after n years = 28,000 × (0.9)^n
(0.9)² = 0.81
(0.9)⁴ = 0.81 × 0.81 = 0.6561
Value after 4 years = 28,000 × 0.6561 = 18,370.80
Check year by year: 28,000 → 25,200 → 22,680 → 20,412 → 18,370.80 ✓

2. A boat is now worth Birr 34,000 and loses 12% of its value each year. What will it worth after 5 years?

**Answer:** about Birr 17,942.89

**Why:**
Each year the value keeps 100% − 12% = 88% = 0.88
Value after n years = 34,000 × (0.88)^n
(0.88)² = 0.7744
(0.88)⁴ = 0.7744 × 0.7744 = 0.59969536
(0.88)⁵ = 0.59969536 × 0.88 = 0.5277319168
Value = 34,000 × 0.5277319168 = 17,942.885… ≈ 17,942.89
Check year by year: 34,000 → 29,920 → 26,329.60 → 23,170.05 → 20,389.64 → 17,942.89 ✓

3. The population of a certain town is increasing at a rate of 2.5% per year. If the population is currently 100,000, what will the population be 10 years from now?

**Answer:** about 128,008 people

**Why:**
Each year the population is multiplied by 1 + 0.025 = 1.025
Population after n years = 100,000 × (1.025)^n
(1.025)¹⁰ ≈ 1.2800845
Population ≈ 100,000 × 1.2800845 = 128,008.45 ≈ 128,008
Check: (1.025)⁵ ≈ 1.1314082 and (1.1314082)² ≈ 1.2800845 ✓

4. Sofia deposits Birr 3,500 in a bank account paying an annual interest rate of 6%. Find the amount she has at the end of the
   a. first year
   b. second year
   c. third year
   d. fourth year
   e. nth year
   f. Do the amounts she has at the end of each year form a geometric sequence? Explain.

**a. Answer:** Birr 3,710

**Why:**
Interest for the year = 6% of 3,500 = 0.06 × 3,500 = 210
Amount = 3,500 + 210 = 3,710 (= 3,500 × 1.06)

**b. Answer:** Birr 3,932.60

**Why:**
3,710 × 1.06 = 3,710 + 222.60 = 3,932.60 (= 3,500 × 1.06² = 3,500 × 1.1236)

**c. Answer:** Birr 4,168.56 (4,168.556)

**Why:**
3,932.60 × 1.06 = 3,932.60 + 235.956 = 4,168.556 ≈ 4,168.56 (= 3,500 × 1.191016)

**d. Answer:** Birr 4,418.67 (4,418.66936)

**Why:**
4,168.556 × 1.06 = 4,168.556 + 250.11336 = 4,418.66936 ≈ 4,418.67 (= 3,500 × 1.26247696)

**e. Answer:** A_n = 3,500(1.06)^n Birr

**Why:**
Each year the amount is multiplied by 1.06
End of year 1: 3,500(1.06)¹; end of year 2: 3,500(1.06)²; … ; end of year n: 3,500(1.06)^n
Check: n = 4 gives 3,500 × 1.26247696 = 4,418.67 ✓ (matches d)

**f. Answer:** Yes. The amounts 3,710; 3,932.60; 4,168.56; 4,418.67; … form a geometric sequence with first term 3,710 and common ratio 1.06.

**Why:**
3,932.60 ÷ 3,710 = 1.06
4,168.556 ÷ 3,932.60 = 1.06
4,418.66936 ÷ 4,168.556 = 1.06
The ratio of any two consecutive terms is the constant 1.06 (see Example 4).

(p.50)

### Example 6

A man was injured in an accident at work. He receives a disability grant of 4800 ETB in the first year. This grant increases by a fixed amount each year.

a. What is the annual rate of increase if he received a total of 143,500 ETB over 20 years?
b. His initial annual expenses are 2600 ETB, which increases at a rate of 400 ETB per year. After how many years will his expenses exceed his income?

**Solution**

a. Since the grant increases with a fixed amount each year, the problem is infinite arithmetic series and the sum is given as

4800 + (4800 + d) + (4800 + 2d) + …

This is an arithmetic series with first term is A_1 = 4800 and the common difference d. So, the sum of the arithmetic series is given by

S_n = (n/2)[2A_1 + (n − 1)d]

Therefore, the sum over 20 years is given by

S_20 = (20/2)[2(4800) + (20 − 1)d] = 143,500

143,500 = 10[9600 + 19d]

14,350 = 9600 + 19d

19d = 4750

d = 250.

Therefore, the annual increase if he received a total of 143,500 ETB over 20 years is 250 ETB.

[added step: divide both sides by 10 to get 14,350; 14,350 − 9600 = 4750; 4750 ÷ 19 = 250. Check: S_20 = 10[9600 + 19 × 250] = 10[9600 + 4750] = 10 × 14,350 = 143,500 ✓]

b. The structure of the series is given by

2600 + 3000 + 3400 + …

This is an arithmetic series whose first term A_1 = 2600 and common difference d = 400.

So, the sum of the arithmetic series is given by

(p.51)

S_n = (n/2)[2A_1 + (n − 1)d]

S_expenses = (n/2)[2(2600) + (n − 1)(400)]
= (n/2)[5200 + 400n − 400] = (n/2)[4800 + 400n]

S_income = (n/2)[2(4800) + (n − 1)(250)]
= (n/2)[9600 + 250n − 250] = (n/2)[9350 + 250n]

Let S_expenses = S_income

(n/2)[4800 + 400n] = (n/2)[9350 + 250n]

4800 + 400n = 9350 + 250n

150n = 4550

n = 4550/150 = 30.333…

Therefore, his expenses will exceed his income after 30 years.

[review: the book compares TOTAL (cumulative) expenses with TOTAL income. With n = 30.33…, at n = 30 total income 252,750 is still more than total expenses 252,000; at n = 31 total expenses 266,600 exceed total income 265,050. So the totals cross during the 31st year ("after 30 years" is acceptable only in that sense). If the question is read as ANNUAL expenses exceeding ANNUAL income: 2600 + 400(n − 1) > 4800 + 250(n − 1) ⇒ 150(n − 1) > 2200 ⇒ n − 1 > 14.67 ⇒ first in year 16. Teachers should decide which reading the lesson uses.]

[review: in part a the book says "the problem is infinite arithmetic series", but only 20 terms are summed (a finite series). Kept as printed.]

### Exercise 1.24

1. A job applicant finds that a firm A offers a starting salary of Birr 31,100 with a guaranteed raise of Birr 1,200 per year, whereas firm B offers a higher starting salary of Birr 35,100 but will guarantee a yearly raise of only Birr 900.
   a. What would the annual salary be in the 11th year at firm A?
   b. What would the annual salary be in the 11th year at firm B?
   c. Over the first 11 years, how much would be earned at firm A?
   d. Over the first 11 years, how much would be earned at firm B?
   e. Compare the amount earned in 11 years in firms A and B.

**1a. Answer:** Birr 43,100

**Why:**
Firm A: A_1 = 31,100, d = 1,200
A_11 = A_1 + (11 − 1)d = 31,100 + 10 × 1,200 = 31,100 + 12,000 = 43,100

**1b. Answer:** Birr 44,100

**Why:**
Firm B: B_1 = 35,100, d = 900
B_11 = 35,100 + 10 × 900 = 35,100 + 9,000 = 44,100

**1c. Answer:** Birr 408,100

**Why:**
S_11 = (11/2)(A_1 + A_11) = (11/2)(31,100 + 43,100) = (11/2)(74,200) = 11 × 37,100 = 408,100
Check: S_11 = (11/2)[2(31,100) + 10(1,200)] = (11/2)[62,200 + 12,000] = (11/2)(74,200) = 408,100 ✓

**1d. Answer:** Birr 435,600

**Why:**
S_11 = (11/2)(35,100 + 44,100) = (11/2)(79,200) = 11 × 39,600 = 435,600
Check: (11/2)[70,200 + 9,000] = (11/2)(79,200) = 435,600 ✓

**1e. Answer:** Firm B pays Birr 27,500 more than firm A over the 11 years.

**Why:**
435,600 − 408,100 = 27,500
(B also still pays more in year 11: 44,100 > 43,100. Firm A's yearly salary catches up only when 31,100 + 1,200(n − 1) ≥ 35,100 + 900(n − 1), i.e. 300(n − 1) ≥ 4,000, n − 1 ≥ 13.3, from year 15.)

2. A contest offers a total of 18 prizes. The first prize is worth Birr 10,000, and each consecutive prize is worth Birr 500 less than the next higher prize. Find the value of the eighteenth prize and the total value of the prizes.

**Answer:** 18th prize = Birr 1,500; total = Birr 103,500

**Why:**
Prizes form an arithmetic sequence with A_1 = 10,000, d = −500
A_18 = 10,000 + (18 − 1)(−500) = 10,000 − 8,500 = 1,500
S_18 = (18/2)(A_1 + A_18) = 9(10,000 + 1,500) = 9 × 11,500 = 103,500
Check: S_18 = 9[2(10,000) + 17(−500)] = 9[20,000 − 8,500] = 9 × 11,500 = 103,500 ✓

(p.52)

3. A contest offers 10 prizes with a total value of Birr 13,250. If the difference in value between consecutive prizes is Birr 250, what is the value of the first prize?

**Answer:** Birr 2,450

**Why:**
The first prize is the largest, so the prizes decrease: d = −250, n = 10, S_10 = 13,250
S_n = (n/2)[2A_1 + (n − 1)d]
13,250 = (10/2)[2A_1 + 9(−250)]
13,250 = 5[2A_1 − 2,250]
13,250/5 = 2A_1 − 2,250
2,650 = 2A_1 − 2,250
2A_1 = 2,650 + 2,250 = 4,900
A_1 = 2,450
Check: last prize A_10 = 2,450 − 9 × 250 = 200; S_10 = 5(2,450 + 200) = 5 × 2,650 = 13,250 ✓
[review: if d = +250 were used (prizes increasing), the "first" prize would be 200, the smallest; the answer 2,450 assumes the first prize is the highest, as in Q2.]

### Example 7

A flower 110 cm high is planted in a garden. At the end of the first year, the flower is 120 cm tall. Thereafter the growth of the flower each year is half of its growth in the previous year. Show that the height of the flower will never exceed 130 cm. Draw a graph of the relationship between time and growth.

**Solution**

The annual growth of the flower: 10, 5, 5/2, 5/4, … and the sum of the growth:

10 + 5 + 5/2 + 5/4 + …

This is a geometric series with the first term G_1 = 10 and common ratio r = 1/2.

S_∞ = G_1/(1 − r) = 10/(1 − 1/2) = 20.

**Note:** we may join the points on the graph because the growth is continuous.

[figure: Figure 1.6 — graph of Growth (cm) against Time (years), years 1 to 9; points (1, 10), (2, 5), (3, 2.5), (4, 1.25), (5, 0.625), … falling towards 0, joined by a dashed curve labelled T_n = 10(1/2)^(n−1).]

(p.53)

Therefore the growth of the flower is limited to 20 cm, and the maximum height of the shrub is therefore 110 cm + 20 cm = 130 cm.

[added step: first-year growth = 120 − 110 = 10 cm; 10 ÷ (1/2) = 20. Every partial sum S_n = 20(1 − (1/2)^n) is less than 20, so the height 110 + S_n is always less than 130 cm — it never reaches or exceeds 130 cm.]

### Example 8

Given a square with side length a. The side of the second square is half of its diagonal. The side of the third square is half of the diagonal of the second square and so on as shown in the figure below. Find the sum of the areas of all these squares.

[figure: a large square of side a; inside it a square of side a_1 standing on its corner (side = half the diagonal of the big square), then smaller squares a_2, a_3, … nested towards the top-left corner, each side half the diagonal of the previous one.]

**Solution**

Let the side of square be a_n and diagonal d_n.

Then,

a_0 = a

a_1 = (1/2)d_0 = (1/2)√2a = √2a/2

a_2 = (1/2)d_1 = (1/2)√2a_1 = (√2/2) × (√2a/2)

a_3 = (1/2)d_2 = (1/2)√2a_2 = (√2/2) × (√2/2) × (√2a/2)

…………………

S_n = a_0² + a_1² + a_2² + a_3² + …
= a² + (1/2)a² + (1/4)a² + (1/8)a² + …

Since, r = G_n/G_(n−1) = 1/2, |r| < 1, then S_∞ = G_1/(1 − r) = a²/(1 − 1/2) = 2a².

[added step: the diagonal of a square of side s is √2 s; a_1² = (√2a/2)² = 2a²/4 = a²/2; each new side is (√2/2) times the previous one, so each area is (√2/2)² = 2/4 = 1/2 of the previous area; G_1 = a² (area of the first square).]

[review: the book writes "S_n = a_0² + a_1² + …" for an infinite sum; it should be S_∞. Kept as printed.]

(p.54)

### Exercise 1.25

1. Suppose a ball is dropped from a height of h m and always rebounds to r % of the height from which it falls. Show that the total vertical distance that could be covered by the ball is h((r + 1)/(1 − r)) m. Assume that the ball will never stop bouncing.

[figure: diagram for Q2 — an equilateral triangle with side a and height h; the height is the side a_1 of a second equilateral triangle, whose height is the side a_2 of a third, and so on, the triangles turning around a common vertex like a fan.]

**Answer:** Total distance = h(1 + r)/(1 − r) m, where r is the rebound ratio written as a decimal fraction (0 < r < 1).

**Why:**
Fall 1: h (down only)
Bounce 1: up rh, then down rh → 2rh
Bounce 2: up r²h, then down r²h → 2r²h
Bounce k: 2r^k h
Total D = h + 2rh + 2r²h + 2r³h + …
= h + 2h(r + r² + r³ + …)
r + r² + r³ + … is geometric with G_1 = r and common ratio r, |r| < 1, so its sum is r/(1 − r)
D = h + 2h × r/(1 − r)
= h(1 − r)/(1 − r) + 2hr/(1 − r) [writing h with denominator (1 − r)]
= h(1 − r + 2r)/(1 − r)
= h(1 + r)/(1 − r) = h((r + 1)/(1 − r)) m ✓
Check with numbers: h = 10, r = 0.5 → 10 + 2(5 + 2.5 + 1.25 + …) = 10 + 2(10) = 30; formula 10(1.5)/(0.5) = 30 ✓
[review: the book says "rebounds to r % of the height", but the formula h(r + 1)/(1 − r) only works if r is the fraction, not the percentage (e.g. 60% must be entered as r = 0.6, not r = 60).]

2. Given an equilateral triangle with side length a, its height is the side of another equilateral triangle. The height of this triangle is then the side of the third equilateral triangle and so on, as shown in the diagram. Find the sum of the areas of all these triangles.

**Answer:** √3 a²

**Why:**
Height of an equilateral triangle with side s: h = √(s² − (s/2)²) = √(3s²/4) = (√3/2)s
So a_1 = (√3/2)a, a_2 = (√3/2)a_1 = (√3/2)²a, …
Area of an equilateral triangle with side s = (1/2) × s × (√3/2)s = (√3/4)s²
Areas: (√3/4)a², (√3/4)a_1² = (√3/4)(3/4)a², (√3/4)(3/4)²a², …
This is geometric with G_1 = (√3/4)a² and r = (√3/2)² = 3/4; |r| < 1
S_∞ = G_1/(1 − r) = ((√3/4)a²)/(1 − 3/4) = ((√3/4)a²)/(1/4) = (√3/4)a² × 4 = √3 a²
Check: a = 2 → first area √3 ≈ 1.732, sum should be 4√3 ≈ 6.928; partial sums 1.732, 3.031, 4.005, 4.736, 5.284, … → 6.928 ✓ (ratio 0.75 each time)

(p.55)

## Summary

1. **Sequence**
   - A sequence {a_n} is a function whose domain is the set of positive integers or a subset of consecutive integers starting with 1.
   - The sequence {a_1, a_2, a_3, …} is denoted by {a_n} or {a_n}_{n=1}^{∞}.
   - A sequence that has a last term is called a **finite sequence**. Otherwise it is called **infinite sequence**.
   - **Recursion formula** is a formula that relates the general term a_n of a sequence to one or more of the terms that come before it.

2. **Arithmetic and geometric progression**
   - **An arithmetic sequence** is one in which the difference between consecutive terms is a constant, and this constant is called the common difference.
   - If {A_n} is an arithmetic progression with the first term A_1 and the common difference d, then the nth term is given by: A_n = A_1 + (n − 1)d.
   - **A geometric progression** is one in which the ratio between consecutive terms is a constant, and this constant is called the common ratio.
   - If {G_n} is a geometric progression with the first term G_n and a common ratio r, then the nth term is given by: G_n = G_1 r^(n−1).
   - [review: book says "with the first term G_n"; should be "first term G_1". Kept as printed.]

3. **Partial sums:**
   - The sum of the first n terms of the sequence {a_n}_{n=1}^{∞}, denoted by S_n is called the partial sum of the sequence.
   - The sum S_n of the first n terms of an arithmetic sequence with first term A_1, and common difference d is:

(p.56)

     S_n = ∑_{k=1}^{n} A_k = (n/2)[2A_1 + (n − 1)d] or S_n = ∑_{k=1}^{n} A_k = (n/2)[A_1 + A_n].
   - In a geometric sequence, {G_n}_{n=1}^{∞}, with common ratio r, the sum of the first n terms S_n is given by:
     - S_n = nG_1, if r = 1
     - S_n = G_1(1 − r^n)/(1 − r), if r ≠ 1

4. **Convergent series and divergent series**
   - In a sequence if {a_n}_{n=1}^{∞}, S_n is the nth partial sum such that, as n → ∞, S_n → s where s is a real number, we say the infinite series ∑_{n=1}^{∞} a_n converges to s, otherwise the series diverges.

(p.57)

## Review Exercise

1. List the first five terms of each of the sequences whose general terms are given below where n is a positive integer:
   a. a_n = n^n/n!
   b. a_n = (−1)^n + (−1)^n sin(nπ)
   c. a_n = Sgn(3 − n)

**1a. Answer:** 1, 2, 9/2, 32/3, 625/24

**Why:**
a_1 = 1¹/1! = 1/1 = 1
a_2 = 2²/2! = 4/2 = 2
a_3 = 3³/3! = 27/6 = (27÷3)/(6÷3) = 9/2
a_4 = 4⁴/4! = 256/24 = (256÷8)/(24÷8) = 32/3
a_5 = 5⁵/5! = 3125/120 = (3125÷5)/(120÷5) = 625/24
Check: a_(n+1)/a_n = (1 + 1/n)^n; a_2/a_1 = 2 ✓, a_3/a_2 = (3/2)² = 9/4 and 2 × 9/4 = 9/2 ✓

**1b. Answer:** −1, 1, −1, 1, −1

**Why:**
sin(nπ) = 0 for every integer n (sin π = sin 2π = … = 0)
So a_n = (−1)^n + (−1)^n × 0 = (−1)^n
a_1 = −1, a_2 = 1, a_3 = −1, a_4 = 1, a_5 = −1

**1c. Answer:** 1, 1, 0, −1, −1

**Why:**
Sgn(x) = 1 if x > 0, 0 if x = 0, −1 if x < 0
n = 1: 3 − 1 = 2 > 0 → 1
n = 2: 3 − 2 = 1 > 0 → 1
n = 3: 3 − 3 = 0 → 0
n = 4: 3 − 4 = −1 < 0 → −1
n = 5: 3 − 5 = −2 < 0 → −1

2. List the first five terms of each of the sequences whose general terms are given below where n is a positive integer:
   a. a_n = 3^(1/n) (−1)^n
   b. a_n = ne^(−2n)
   c. a_n = ((−2)^n + 6)/(n − 1)!
   d. a_n = (−1)^n − 1/n²
   e. a_n = cos(nπ/2)

**2a. Answer:** −3, √3, −∛3, ∜3, −⁵√3 (≈ −3, 1.732, −1.442, 1.316, −1.246)

**Why:**
a_1 = 3^(1/1)(−1)¹ = −3
a_2 = 3^(1/2)(−1)² = √3
a_3 = 3^(1/3)(−1)³ = −∛3
a_4 = 3^(1/4)(−1)⁴ = ∜3
a_5 = 3^(1/5)(−1)⁵ = −3^(1/5)

**2b. Answer:** e^(−2), 2e^(−4), 3e^(−6), 4e^(−8), 5e^(−10) (≈ 0.1353, 0.0366, 0.0074, 0.0013, 0.0002)

**Why:**
a_1 = 1 × e^(−2×1) = e^(−2)
a_2 = 2 × e^(−4)
a_3 = 3 × e^(−6)
a_4 = 4 × e^(−8)
a_5 = 5 × e^(−10)

**2c. Answer:** 4, 10, −1, 11/3, −13/12

**Why:**
a_1 = ((−2)¹ + 6)/0! = (−2 + 6)/1 = 4 (0! = 1)
a_2 = ((−2)² + 6)/1! = (4 + 6)/1 = 10
a_3 = ((−2)³ + 6)/2! = (−8 + 6)/2 = −2/2 = −1
a_4 = ((−2)⁴ + 6)/3! = (16 + 6)/6 = 22/6 = (22÷2)/(6÷2) = 11/3
a_5 = ((−2)⁵ + 6)/4! = (−32 + 6)/24 = −26/24 = (−26÷2)/(24÷2) = −13/12

**2d. Answer:** −2, 3/4, −10/9, 15/16, −26/25

**Why:**
a_1 = −1 − 1/1 = −2
a_2 = 1 − 1/4 = 4/4 − 1/4 = 3/4
a_3 = −1 − 1/9 = −9/9 − 1/9 = −10/9
a_4 = 1 − 1/16 = 16/16 − 1/16 = 15/16
a_5 = −1 − 1/25 = −25/25 − 1/25 = −26/25

**2e. Answer:** 0, −1, 0, 1, 0

**Why:**
a_1 = cos(π/2) = 0
a_2 = cos(π) = −1
a_3 = cos(3π/2) = 0
a_4 = cos(2π) = 1
a_5 = cos(5π/2) = cos(2π + π/2) = cos(π/2) = 0

3. Determine whether the sequences with the following general terms are arithmetic.
   a. a_n = (n² + 5n + 6)/(n + 2)
   b. a_n = √(4n + 1)

**3a. Answer:** Yes, arithmetic: a_n = n + 3, common difference d = 1.

**Why:**
Factor the numerator: n² + 5n + 6 = (n + 2)(n + 3) (2 × 3 = 6, 2 + 3 = 5)
a_n = (n + 2)(n + 3)/(n + 2) = n + 3 (n + 2 ≠ 0 for positive n)
a_(n+1) − a_n = (n + 4) − (n + 3) = 1, a constant
Check: a_1 = 12/3 = 4, a_2 = 20/4 = 5, a_3 = 30/5 = 6 → 4, 5, 6 ✓

**3b. Answer:** No, it is not arithmetic.

**Why:**
a_1 = √5 ≈ 2.236, a_2 = √9 = 3, a_3 = √13 ≈ 3.606
a_2 − a_1 = 3 − √5 ≈ 0.764
a_3 − a_2 = √13 − 3 ≈ 0.606
The differences are not equal, so there is no common difference.

4. Find the arithmetic mean between 1 and 9.

**Answer:** 5

**Why:**
The arithmetic mean between a and b is (a + b)/2
(1 + 9)/2 = 10/2 = 5
Check: 1, 5, 9 has common difference 4 ✓

5. Find the 10th and nth terms of the geometric progression 5, 25, 125, …

**Answer:** G_10 = 5¹⁰ = 9,765,625; G_n = 5^n

**Why:**
G_1 = 5, r = 25/5 = 5
G_n = G_1 r^(n−1) = 5 × 5^(n−1) = 5^n
G_10 = 5¹⁰ = 9,765,625
Check: 5³ = 125 is the 3rd term ✓

6. Find three numbers in geometric progression such that their sum is 13/3 and the sum of their squares is 91/3.

**Answer:** 1/3, −4/3, 16/3 (or in the reverse order 16/3, −4/3, 1/3)

**Why:**
Let the numbers be a, ar, ar².
a(1 + r + r²) = 13/3 … (1)
a²(1 + r² + r⁴) = 91/3 … (2)
Use 1 + r² + r⁴ = (1 + r + r²)(1 − r + r²)
Divide (2) by (1): a(1 − r + r²) = (91/3) ÷ (13/3) = 91/13 = 7 … (3)
(1) − (3): 2ar = 13/3 − 21/3 = −8/3, so ar = −4/3 … (4)
(1) + (3): 2a(1 + r²) = 13/3 + 21/3 = 34/3, so a(1 + r²) = 17/3 … (5)
(5) ÷ (4): (1 + r²)/r = (17/3) ÷ (−4/3) = −17/4
4(1 + r²) = −17r
4r² + 17r + 4 = 0
(4r + 1)(r + 4) = 0
r = −4 or r = −1/4
r = −4: a = (−4/3) ÷ (−4) = 1/3 → numbers 1/3, −4/3, 16/3
r = −1/4: a = (−4/3) ÷ (−1/4) = 16/3 → numbers 16/3, −4/3, 1/3
Check: 1/3 − 4/3 + 16/3 = 13/3 ✓; 1/9 + 16/9 + 256/9 = 273/9 = 91/3 ✓

7. Find the sum of
   a. ∑_{k=1}^{8} (k³ + 2k² − 3k + 5)
   b. ∑_{k=2}^{5} 3
   c. ∑_{k=1}^{5} 1/(k² + 5k + 6)
   d. ∑_{m=1}^{10} ln(m/(m + 1))

**7a. Answer:** 1636

**Why:**
Split: ∑k³ + 2∑k² − 3∑k + ∑5, each from k = 1 to 8
∑k = n(n + 1)/2 = 8 × 9/2 = 36
∑k² = n(n + 1)(2n + 1)/6 = 8 × 9 × 17/6 = 1224/6 = 204
∑k³ = (n(n + 1)/2)² = 36² = 1296
∑5 = 5 × 8 = 40
Total = 1296 + 2(204) − 3(36) + 40 = 1296 + 408 − 108 + 40 = 1636
Check by listing: k = 1…8 give 5, 15, 41, 89, 165, 275, 425, 621; sum = 1636 ✓

**7b. Answer:** 12

**Why:**
k runs 2, 3, 4, 5 → 5 − 2 + 1 = 4 terms, each equal to 3
Sum = 4 × 3 = 12

**7c. Answer:** 5/24

**Why:**
k² + 5k + 6 = (k + 2)(k + 3)
1/((k + 2)(k + 3)) = 1/(k + 2) − 1/(k + 3) [check: ((k + 3) − (k + 2))/((k + 2)(k + 3)) = 1/((k + 2)(k + 3)) ✓]
Sum = (1/3 − 1/4) + (1/4 − 1/5) + (1/5 − 1/6) + (1/6 − 1/7) + (1/7 − 1/8)
Middle terms cancel (telescoping): = 1/3 − 1/8
= (1×8)/(3×8) − (1×3)/(8×3) = 8/24 − 3/24 = 5/24
Check directly: 1/12 + 1/20 + 1/30 + 1/42 + 1/56 = (70 + 42 + 28 + 20 + 15)/840 = 175/840 = 5/24 (dividing by 35) ✓

**7d. Answer:** −ln 11 (= ln(1/11) ≈ −2.398)

**Why:**
Sum of logs = log of product: ∑ ln(m/(m + 1)) = ln(1/2 × 2/3 × 3/4 × … × 10/11)
The product telescopes: 1/2 × 2/3 × … × 10/11 = 1/11
= ln(1/11) = −ln 11
Check (other way): ln(m/(m + 1)) = ln m − ln(m + 1); sum = ln 1 − ln 11 = 0 − ln 11 ✓

8. Let ∑_{i=1}^{5} x_i = 37, ∑_{i=1}^{5} y_i = 127, ∑_{i=1}^{5} x_i² = 303, ∑_{i=1}^{5} y_i² = 50 and ∑_{i=1}^{5} x_i y_i = 105.

(p.58)

   Evaluate the following
   a. ∑_{i=1}^{5} (2x_i − 3y_i)
   b. ∑_{i=1}^{5} (2x_i + 3y_i)
   c. ∑_{i=1}^{5} (2x_i − 3y_i)²
   d. (∑_{i=1}^{5} x_i)²
   e. ∑_{i=1}^{5} (2x_i − 5y_i + 3)

[review: the given data cannot come from real numbers — five real y_i with ∑y_i = 127 must have ∑y_i² ≥ 127²/5 ≈ 3225.8, but the book gives ∑y_i² = 50. The answers below use the sigma rules formally, which is what the question tests; a lesson using generated numbers should generate the x_i, y_i first and compute the sums from them.]

**8a. Answer:** −307

**Why:**
∑(2x_i − 3y_i) = 2∑x_i − 3∑y_i (sum rule and constant-multiple rule)
= 2(37) − 3(127) = 74 − 381 = −307

**8b. Answer:** 455

**Why:**
∑(2x_i + 3y_i) = 2∑x_i + 3∑y_i = 74 + 381 = 455

**8c. Answer:** 402

**Why:**
(2x_i − 3y_i)² = 4x_i² − 12x_i y_i + 9y_i²
∑(2x_i − 3y_i)² = 4∑x_i² − 12∑x_i y_i + 9∑y_i²
= 4(303) − 12(105) + 9(50)
= 1212 − 1260 + 450 = 402

**8d. Answer:** 1369

**Why:**
(∑x_i)² = 37² = 1369 (note: this is NOT ∑x_i² = 303)

**8e. Answer:** −546

**Why:**
∑(2x_i − 5y_i + 3) = 2∑x_i − 5∑y_i + ∑3
∑_{i=1}^{5} 3 = 5 × 3 = 15
= 2(37) − 5(127) + 15 = 74 − 635 + 15 = −546

9. Find the sum of all the natural numbers between 100 and 1000 which are multiples of 5.

**Answer:** 98,450

**Why:**
"Between" taken as strictly between: 105, 110, …, 995 (arithmetic, A_1 = 105, d = 5)
A_n = 105 + (n − 1)5 = 995
(n − 1)5 = 890
n − 1 = 178, n = 179
S_179 = (179/2)(105 + 995) = (179/2)(1100) = 179 × 550 = 98,450
Check: multiples of 5 from 5 to 995 sum to (199/2)(5 + 995) = 99,500; from 5 to 100 sum to (20/2)(105) = 1,050; 99,500 − 1,050 = 98,450 ✓
[review: if 100 and 1000 are included the answer is 98,450 + 100 + 1000 = 99,550. The answer above treats "between" as excluding the end values.]

10. In an arithmetic progression the 1st term is 2 and the sum of the 1st five terms is one-quarter of the next five terms. Show that the 20th term is −112.

**Answer:** d = −6, so A_20 = 2 + 19(−6) = −112 (shown).

**Why:**
A_1 = 2
Sum of first five: S_5 = (5/2)[2(2) + 4d] = (5/2)(4 + 4d) = 10 + 10d
Sum of first ten: S_10 = (10/2)[4 + 9d] = 20 + 45d
Next five terms (6th to 10th) = S_10 − S_5 = 20 + 45d − 10 − 10d = 10 + 35d
Condition: S_5 = (1/4)(S_10 − S_5)
10 + 10d = (10 + 35d)/4
4(10 + 10d) = 10 + 35d
40 + 40d = 10 + 35d
5d = −30
d = −6
A_20 = A_1 + 19d = 2 + 19(−6) = 2 − 114 = −112 ✓
Check: terms 2, −4, −10, −16, −22 sum −50; next five −28, −34, −40, −46, −52 sum −200; −50 = (1/4)(−200) ✓

11. How many terms of the arithmetic progression −6, −11/2, −5, … are needed to give the sum −25?

**Answer:** 5 terms or 20 terms (both give −25)

**Why:**
A_1 = −6, d = −11/2 − (−6) = −11/2 + 12/2 = 1/2
S_n = (n/2)[2A_1 + (n − 1)d] = (n/2)[−12 + (n − 1)/2] = −25
Multiply by 2: n[−12 + (n − 1)/2] = −50
Multiply by 2: n[−24 + n − 1] = −100
n(n − 25) = −100
n² − 25n + 100 = 0
(n − 5)(n − 20) = 0 (5 × 20 = 100, 5 + 20 = 25)
n = 5 or n = 20
Check n = 5: −6 − 5.5 − 5 − 4.5 − 4 = −25 ✓
Check n = 20: A_20 = −6 + 19/2 = 3.5; S_20 = (20/2)(−6 + 3.5) = 10(−2.5) = −25 ✓ (the terms from the 6th (−3.5) to the 20th (3.5) are symmetric about 0 and add to 0, so S_20 = S_5)

12. The sum of a certain number of terms of the arithmetic progression 25, 22, 19, … is 116. Find the last term.

**Answer:** The last term is 4 (8 terms).

**Why:**
A_1 = 25, d = 22 − 25 = −3
S_n = (n/2)[50 + (n − 1)(−3)] = (n/2)(53 − 3n) = 116
n(53 − 3n) = 232
53n − 3n² = 232
3n² − 53n + 232 = 0
Discriminant: 53² − 4(3)(232) = 2809 − 2784 = 25, √25 = 5
n = (53 ± 5)/6 → n = 58/6 = 29/3 (not a whole number, reject) or n = 48/6 = 8
Last term A_8 = 25 + 7(−3) = 25 − 21 = 4
Check: 25 + 22 + 19 + 16 + 13 + 10 + 7 + 4 = 116 ✓

13. If the sum of n terms of an arithmetic progression is (pn + qn²), where p and q are constants, find the common difference.

**Answer:** d = 2q

**Why:**
A_n = S_n − S_(n−1)
S_(n−1) = p(n − 1) + q(n − 1)² = pn − p + qn² − 2qn + q
A_n = (pn + qn²) − (pn − p + qn² − 2qn + q) = p + 2qn − q = (p − q) + 2qn
d = A_(n+1) − A_n = [(p − q) + 2q(n + 1)] − [(p − q) + 2qn] = 2q
Check: A_1 = S_1 = p + q; A_2 = S_2 − S_1 = (2p + 4q) − (p + q) = p + 3q; A_2 − A_1 = 2q ✓

14. If the nth partial sum of an arithmetic sequence {A_n} is 4n², find A_n and A_10.

**Answer:** A_n = 8n − 4, A_10 = 76

**Why:**
A_n = S_n − S_(n−1) = 4n² − 4(n − 1)²
= 4n² − 4(n² − 2n + 1) = 4n² − 4n² + 8n − 4 = 8n − 4
(also A_1 = S_1 = 4 = 8(1) − 4 ✓)
A_10 = 8(10) − 4 = 80 − 4 = 76
Check: S_10 − S_9 = 400 − 324 = 76 ✓

15. Convert this mixed recurring decimal 0.31̄7̄ to fraction. [the bar is over "17": 0.3171717…]

**Answer:** 157/495

**Why:**
0.3171717… = 0.3 + 0.0171717…
0.0171717… = 0.017 + 0.00017 + 0.0000017 + … ; G_1 = 17/1000, r = 1/100
S_∞ = (17/1000)/(1 − 1/100) = (17/1000)/(99/100) = 17/1000 × 100/99 = 17/990
0.3 = 3/10 = (3×99)/(10×99) = 297/990
Total = 297/990 + 17/990 = 314/990 = (314÷2)/(990÷2) = 157/495
Check (shortcut): (317 − 3)/990 = 314/990 = 157/495 ✓; 157 ÷ 495 = 0.317171… ✓

16. Convert the mixed recurring decimal to fraction.
   a. 0.37̄ [bar over 7: 0.3777…]
   b. 3.235̄4̄ [bar over "54": 3.235454…]

**16a. Answer:** 17/45

**Why:**
0.3777… = 0.3 + 0.0777…
0.0777… = 0.07 + 0.007 + … ; G_1 = 7/100, r = 1/10
S_∞ = (7/100)/(9/10) = 7/100 × 10/9 = 7/90
0.3 = 3/10 = (3×9)/(10×9) = 27/90
Total = 27/90 + 7/90 = 34/90 = (34÷2)/(90÷2) = 17/45
Check: (37 − 3)/90 = 34/90 ✓; 17 ÷ 45 = 0.3777… ✓

**16b. Answer:** 3559/1100 (= 3 259/1100)

**Why:**
3.235454… = 3 + 0.23 + 0.005454…
0.005454… = 0.0054 + 0.000054 + … ; G_1 = 54/10000, r = 1/100
S_∞ = (54/10000)/(99/100) = 54/10000 × 100/99 = 54/9900
0.23 = 23/100 = (23×99)/(100×99) = 2277/9900
0.235454… = 2277/9900 + 54/9900 = 2331/9900
2331 = 9 × 259 and 9900 = 9 × 1100, so 2331/9900 = 259/1100
3 + 259/1100 = (3×1100)/1100 + 259/1100 = 3300/1100 + 259/1100 = 3559/1100
Check: (2354 − 23)/9900 = 2331/9900 ✓; 3559 ÷ 1100 = 3.2354545… ✓

17. The first three terms of a convergent geometric series are: x + 1; x − 1; 2x − 5.
   a. Find the values of x (x ≠ 1 or −1).
   b. Find sum to infinity of the series.

**17a. Answer:** x = 3 (x = −2 also makes a geometric sequence, but it is rejected because that series does not converge)

**Why:**
For a geometric sequence, (middle)² = (first)(third)
(x − 1)² = (x + 1)(2x − 5)
x² − 2x + 1 = 2x² − 5x + 2x − 5 = 2x² − 3x − 5
0 = 2x² − 3x − 5 − x² + 2x − 1
0 = x² − x − 6
(x − 3)(x + 2) = 0
x = 3 or x = −2
x = 3: terms 4, 2, 1 → r = 1/2, |r| < 1, converges ✓
x = −2: terms −1, −3, −9 → r = 3, diverges ✗ (the question says the series is convergent)
So x = 3

**17b. Answer:** S_∞ = 8

**Why:**
G_1 = 4, r = 2/4 = 1/2
S_∞ = 4/(1 − 1/2) = 4/(1/2) = 8
Check: 4 + 2 + 1 + 0.5 + 0.25 + … → 8 ✓

18. Find p: ∑_{k=1}^{∞} 27p^k = ∑_{x=1}^{12} (24 − 3x).

**Answer:** p = 2/3

**Why:**
Right side: ∑_{x=1}^{12} (24 − 3x) = 12 × 24 − 3 × (12 × 13/2) = 288 − 3 × 78 = 288 − 234 = 54
(check: terms 21, 18, 15, …, −12; S = (12/2)(21 + (−12)) = 6 × 9 = 54 ✓)
Left side: geometric with G_1 = 27p, ratio p; converges only if |p| < 1; sum = 27p/(1 − p)
27p/(1 − p) = 54
27p = 54(1 − p) = 54 − 54p
81p = 54
p = 54/81 = (54÷27)/(81÷27) = 2/3
|2/3| < 1 ✓
Check: 27(2/3)/(1 − 2/3) = 18/(1/3) = 54 ✓

19. Find the product 4 × 4^(1/2) × 4^(1/4) × 4^(1/8) × … × 4^(1/2^n) × …

**Answer:** 16

**Why:**
Same base: add the exponents: 4^(1 + 1/2 + 1/4 + 1/8 + …)
1 + 1/2 + 1/4 + … is geometric with G_1 = 1, r = 1/2: sum = 1/(1 − 1/2) = 2
Product = 4² = 16
Check: partial products 4, 8, 11.31, 13.45, 14.67, … approach 16 ✓
[review: the book writes the general factor as 4^(1/2^n); with the first factor 4 = 4^(1/2⁰) the factors are 4^(1/2^n) for n = 0, 1, 2, …. The answer is unaffected.]

20. If ∑_{k=1}^{∞} 5^(kt) = 1/24, find the values of t.

**Answer:** t = −2

**Why:**
∑ 5^(kt) = 5^t + 5^(2t) + … is geometric with G_1 = 5^t, r = 5^t
It converges only if 5^t < 1, i.e. t < 0
Sum = 5^t/(1 − 5^t) = 1/24
24 × 5^t = 1 − 5^t
25 × 5^t = 1
5^t = 1/25 = 5^(−2)
t = −2 (and t < 0 ✓)
Check: 5^(−2) = 1/25; (1/25)/(1 − 1/25) = (1/25)/(24/25) = 1/24 ✓

(p.59)

21. If the product 5^k · 5^(k²) · 5^(k³) … = 5, find k.

**Answer:** k = 1/2

**Why:**
Same base: 5^(k + k² + k³ + …) = 5¹
So k + k² + k³ + … = 1
Geometric with G_1 = k, r = k; needs |k| < 1; sum = k/(1 − k)
k/(1 − k) = 1
k = 1 − k
2k = 1
k = 1/2 (|1/2| < 1 ✓)
Check: 1/2 + 1/4 + 1/8 + … = 1 ✓

22. Evaluate ∑_{k=1}^{11} (2 + 3^k).

**Answer:** 265,741

**Why:**
∑(2 + 3^k) = ∑2 + ∑3^k
∑_{k=1}^{11} 2 = 11 × 2 = 22
∑_{k=1}^{11} 3^k: geometric, G_1 = 3, r = 3, n = 11 → 3(3¹¹ − 1)/(3 − 1) = 3(177,147 − 1)/2 = 3 × 177,146/2 = 3 × 88,573 = 265,719
Total = 22 + 265,719 = 265,741
Check: (3¹² − 3)/2 = (531,441 − 3)/2 = 265,719 ✓

23. The sum of the first three terms of a geometric progression is 39/10 and their product is 1. Find the common ratio and the three terms.

**Answer:** r = 5/2 with terms 2/5, 1, 5/2; or r = 2/5 with terms 5/2, 1, 2/5

**Why:**
Let the terms be a/r, a, ar
Product: (a/r)(a)(ar) = a³ = 1, so a = 1
Sum: 1/r + 1 + r = 39/10
1/r + r = 39/10 − 10/10 = 29/10
Multiply by 10r: 10 + 10r² = 29r
10r² − 29r + 10 = 0
Discriminant: 29² − 4(10)(10) = 841 − 400 = 441, √441 = 21
r = (29 ± 21)/20 → r = 50/20 = 5/2 or r = 8/20 = 2/5
r = 5/2: terms 1/(5/2) = 2/5, 1, 5/2
r = 2/5: terms 5/2, 1, 2/5
Check: 2/5 + 1 + 5/2 = 4/10 + 10/10 + 25/10 = 39/10 ✓; (2/5)(1)(5/2) = 1 ✓

24. How many terms of geometric progression 3, 3², 3³, … are needed to give the sum 120?

**Answer:** 4 terms

**Why:**
G_1 = 3, r = 3
S_n = 3(3^n − 1)/(3 − 1) = 3(3^n − 1)/2 = 120
3^n − 1 = 120 × 2/3 = 80
3^n = 81 = 3⁴
n = 4
Check: 3 + 9 + 27 + 81 = 120 ✓

25. The sum of first three terms of a geometric progression is 16 and the sum of the next three terms is 128. Determine the first term, the common ratio and the sum to n terms of the geometric progression.

**Answer:** G_1 = 16/7, r = 2, S_n = (16/7)(2^n − 1)

**Why:**
G_1(1 + r + r²) = 16 … (1)
G_1r³(1 + r + r²) = 128 … (2)
(2) ÷ (1): r³ = 128/16 = 8, so r = 2
From (1): G_1(1 + 2 + 4) = 16 → 7G_1 = 16 → G_1 = 16/7
S_n = G_1(r^n − 1)/(r − 1) = (16/7)(2^n − 1)/1 = (16/7)(2^n − 1)
Check: first three 16/7 + 32/7 + 64/7 = 112/7 = 16 ✓; next three 128/7 + 256/7 + 512/7 = 896/7 = 128 ✓

26. Given a geometric progression with a = 729 and 7th term 64, determine S_7.

**Answer:** S_7 = 2059 (if r = 2/3) or S_7 = 463 (if r = −2/3)

**Why:**
G_7 = ar⁶ = 729r⁶ = 64
r⁶ = 64/729 = (2/3)⁶
r = 2/3 or r = −2/3 (even power)
r = 2/3: S_7 = 729(1 − (2/3)⁷)/(1 − 2/3) = 729(1 − 128/2187)/(1/3) = 3 × 729 × (2059/2187) = 2187 × 2059/2187 = 2059
r = −2/3: S_7 = 729(1 − (−2/3)⁷)/(1 + 2/3) = 729(1 + 128/2187)/(5/3) = 729 × (2315/2187) × 3/5 = (2315/3) × (3/5) = 2315/5 = 463
Check r = 2/3 by listing: 729 + 486 + 324 + 216 + 144 + 96 + 64 = 2059 ✓
Check r = −2/3: 729 − 486 + 324 − 216 + 144 − 96 + 64 = 463 ✓
[review: the question does not say whether r is positive; r = 2/3 gives 2059 and r = −2/3 gives 463. If the lesson expects one answer, it is probably 2059.]

27. If the 4th, 10th and 16th terms of a geometric progression are x, y and z, respectively. Prove that x, y, z are in geometric progression.

**Answer:** y/x = z/y = r⁶ (equivalently y² = xz), so x, y, z are in geometric progression.

**Why:**
Let the first term be G_1 and the common ratio R.
x = G_4 = G_1R³
y = G_10 = G_1R⁹
z = G_16 = G_1R¹⁵
y/x = G_1R⁹/(G_1R³) = R⁶
z/y = G_1R¹⁵/(G_1R⁹) = R⁶
The ratios are equal (both R⁶), so x, y, z form a geometric progression with common ratio R⁶.
Check: y² = G_1²R¹⁸ and xz = G_1R³ × G_1R¹⁵ = G_1²R¹⁸ ✓

28. Find the sum to n terms of the sequence 8, 88, 888, 8888, ….

**Answer:** S_n = (8/81)(10^(n+1) − 9n − 10)

**Why:**
8 = (8/9)(9) = (8/9)(10 − 1)
88 = (8/9)(99) = (8/9)(10² − 1)
888 = (8/9)(10³ − 1), and so on; the kth term is (8/9)(10^k − 1)
S_n = (8/9)[(10 + 10² + … + 10^n) − n]
10 + 10² + … + 10^n is geometric, G_1 = 10, r = 10: sum = 10(10^n − 1)/9
S_n = (8/9)[10(10^n − 1)/9 − n]
= (8/9)[(10^(n+1) − 10)/9 − 9n/9]
= (8/81)(10^(n+1) − 10 − 9n)
Check: n = 2 → (8/81)(1000 − 10 − 18) = (8/81)(972) = 8 × 12 = 96 = 8 + 88 ✓; n = 4 → (8/81)(100000 − 10 − 36) = (8/81)(99954) = 9872 = 8 + 88 + 888 + 8888 ✓

29. Show that the products of the corresponding terms of the sequences a, ar, ar², … ar^(n−1) and A, AR, AR², …AR^(n−1) form a geometric progression, and find the common ratio.

**Answer:** The products are aA, aA(rR), aA(rR)², …, aA(rR)^(n−1): a geometric progression with common ratio rR.

**Why:**
kth product = (ar^(k−1))(AR^(k−1)) = aA(rR)^(k−1)
Ratio of consecutive products: aA(rR)^k / (aA(rR)^(k−1)) = rR, a constant
So the products form a GP with first term aA and common ratio rR.
Check: a = 1, r = 2 and A = 1, R = 3: products 1, 6, 36, … ratio 6 = 2 × 3 ✓

30. If the pth, qth and rth terms of a geometric progression are a, b and c, respectively. Prove that a^(q−r) b^(r−p) c^(p−q) = 1

**Answer:** Proved: the product equals G_1⁰ × R⁰ = 1.

**Why:**
Let the first term be G_1 and the common ratio R (R to avoid mixing with the index r).
a = G_1R^(p−1), b = G_1R^(q−1), c = G_1R^(r−1)
a^(q−r) b^(r−p) c^(p−q) = G_1^((q−r) + (r−p) + (p−q)) × R^((p−1)(q−r) + (q−1)(r−p) + (r−1)(p−q))
Power of G_1: (q − r) + (r − p) + (p − q) = 0
Power of R: (p − 1)(q − r) + (q − 1)(r − p) + (r − 1)(p − q)
= [p(q − r) + q(r − p) + r(p − q)] − [(q − r) + (r − p) + (p − q)]
= [pq − pr + qr − pq + rp − rq] − 0
= 0
So the product = G_1⁰ × R⁰ = 1 × 1 = 1
Check with numbers: GP 1, 2, 4, 8 (G_1 = 1, R = 2); p = 1, q = 2, r = 4 → a = 1, b = 2, c = 8; 1^(−2) × 2^(3) × 8^(−1) = 1 × 8 × 1/8 = 1 ✓

31. If the first and the nth term of a geometric progression are a and b, respectively, and if P is the product of n terms, prove that P² = (ab)^n

**Answer:** Proved: P² = a^(2n) r^(n(n−1)) = (ab)^n.

**Why:**
Let the common ratio be r; the terms are a, ar, ar², …, ar^(n−1), and b = ar^(n−1)
P = a × ar × ar² × … × ar^(n−1) = a^n × r^(0 + 1 + 2 + … + (n−1)) = a^n r^(n(n−1)/2)
P² = a^(2n) r^(n(n−1))
(ab)^n = (a × ar^(n−1))^n = (a² r^(n−1))^n = a^(2n) r^(n(n−1))
So P² = (ab)^n
Check: GP 2, 6, 18 (n = 3, a = 2, b = 18): P = 216, P² = 46,656; (ab)³ = 36³ = 46,656 ✓

32. If a, b, c and d are in geometric progression. Show that (a² + b² + c²)(b² + c² + d²) = (ab + bc + cd)²

**Answer:** Both sides equal a⁴r²(1 + r² + r⁴)², so the identity holds.

**Why:**
Let b = ar, c = ar², d = ar³
a² + b² + c² = a² + a²r² + a²r⁴ = a²(1 + r² + r⁴)
b² + c² + d² = a²r² + a²r⁴ + a²r⁶ = a²r²(1 + r² + r⁴)
Left side = a²(1 + r² + r⁴) × a²r²(1 + r² + r⁴) = a⁴r²(1 + r² + r⁴)²
ab + bc + cd = a·ar + ar·ar² + ar²·ar³ = a²r + a²r³ + a²r⁵ = a²r(1 + r² + r⁴)
Right side = (a²r(1 + r² + r⁴))² = a⁴r²(1 + r² + r⁴)²
Left side = Right side ✓
Check: 1, 2, 4, 8 → (1 + 4 + 16)(4 + 16 + 64) = 21 × 84 = 1764; (2 + 8 + 32)² = 42² = 1764 ✓

33. Insert two numbers between 3 and 81 so that the resulting sequence is geometric progression.

**Answer:** 9 and 27 (sequence 3, 9, 27, 81)

**Why:**
G_1 = 3, G_4 = 81
G_4 = G_1r³ → 3r³ = 81 → r³ = 27 → r = 3
G_2 = 3 × 3 = 9, G_3 = 9 × 3 = 27
Check: 27 × 3 = 81 ✓

(p.60)

34. The sum of two numbers is 6 times their geometric mean, show that numbers are in the ratio (3 + 2√2) : (3 − 2√2).

**Answer:** Shown: a/b = (3 + 2√2)² = (3 + 2√2)/(3 − 2√2).

**Why:**
Let the positive numbers be a and b; their geometric mean is √(ab)
a + b = 6√(ab)
Divide by b: a/b + 1 = 6√(a/b)
Let t = √(a/b): t² + 1 = 6t
t² − 6t + 1 = 0
t = (6 ± √(36 − 4))/2 = (6 ± √32)/2 = (6 ± 4√2)/2 = 3 ± 2√2
Take the larger number as a: t = 3 + 2√2, so a/b = t² = (3 + 2√2)²
Since (3 + 2√2)(3 − 2√2) = 9 − 8 = 1, we have 3 + 2√2 = 1/(3 − 2√2)
So (3 + 2√2)² = (3 + 2√2) × 1/(3 − 2√2) = (3 + 2√2)/(3 − 2√2)
Therefore a : b = (3 + 2√2) : (3 − 2√2) ✓
Check: a = 3 + 2√2 ≈ 5.828, b = 3 − 2√2 ≈ 0.172; a + b = 6; √(ab) = √1 = 1; 6 = 6 × 1 ✓

35. If A and G are an arithmetic mean and geometric mean, respectively between two positive numbers, prove that the numbers are A ± √((A + G)(A − G)).

**Answer:** Proved: the numbers are the roots of x² − 2Ax + G² = 0, i.e. x = A ± √(A² − G²) = A ± √((A + G)(A − G)).

**Why:**
Let the numbers be a and b (positive)
A = (a + b)/2 → a + b = 2A
G = √(ab) → ab = G²
a and b are the roots of x² − (a + b)x + ab = 0, i.e. x² − 2Ax + G² = 0
x = (2A ± √(4A² − 4G²))/2 = A ± √(A² − G²)
A² − G² = (A + G)(A − G) (difference of two squares)
So the numbers are A ± √((A + G)(A − G))
Check: numbers 2 and 8 → A = 5, G = 4; 5 ± √(9 × 1) = 5 ± 3 = 8 and 2 ✓

36. 150 workers were hired to finish a job in a certain number of days. 4 workers dropped out on second day, four more workers dropped out on third day and so on. It took eight more days to finish the work. Find the number of days in which the work was completed.

**Answer:** 25 days

**Why:**
Let the work actually take m days; the planned time was m − 8 days.
Total work (worker-days) planned = 150(m − 8)
Workers each day: 150, 146, 142, … arithmetic with A_1 = 150, d = −4
Work done in m days = (m/2)[2(150) + (m − 1)(−4)] = (m/2)(300 − 4m + 4) = (m/2)(304 − 4m) = m(152 − 2m)
Set equal: m(152 − 2m) = 150(m − 8)
152m − 2m² = 150m − 1200
0 = 2m² − 2m − 1200
m² − m − 600 = 0
(m − 25)(m + 24) = 0 (25 × 24 = 600, 25 − 24 = 1)
m = 25 or m = −24 (reject, days must be positive)
Work was completed in 25 days (planned 17 days).
Check: worker-days = (25/2)(150 + 54) = (25/2)(204) = 2550 = 150 × 17 ✓; on day 25 there are still 150 − 24 × 4 = 54 workers ✓

## Notes for lesson design
### u1-a

**Key ideas by section**

- 1.1 Sequences: a sequence is a function on the integers ≥ m; the general term a_n produces terms by substituting n = 1, 2, 3, …; finite vs infinite sequences; the graph of a sequence is a set of separate dots (n, a_n), not a joined line. Recursive sequences (Fibonacci F_0 = F_1 = 1; Mulatu M_0 = 4, M_1 = 1; both with "add the two previous terms") — an Ethiopian mathematician's sequence is a good motivating hook.
- 1.2.1 Arithmetic sequences: constant common difference d = A_(n+1) − A_n; A_n = A_1 + (n − 1)d; finding A_1 and d from two given terms by subtracting two equations; testing "is it arithmetic?" by checking whether a_(n+1) − a_n is free of n; arithmetic mean(s) between two numbers.
- 1.2.2 Geometric sequences: constant non-zero ratio r = G_(n+1)/G_n; G_n = G_1 r^(n−1); finding r from two terms via r^(gap) = ratio of the terms (may give ± roots); geometric mean m = ±√(ab); the a/r, a, ar trick for three consecutive terms.
- 1.3 Partial sums and sigma: S_n = a_1 + … + a_n; ∑ notation with index, lower and upper limits; changing the index name or shifting the index leaves the sum unchanged; properties (constant multiple, sum/difference, splitting a sum, ∑ c = nc); telescoping sums via partial fractions 1/(n(n+1)) = 1/n − 1/(n+1).
- 1.3.2 Sum of arithmetic sequences: Gauss's forward-plus-backward trick; 1 + 2 + … + n = n(n + 1)/2; S_n = (n/2)[2A_1 + (n − 1)d] = n(A_1 + A_n)/2.

**Common student mistakes to anticipate**

- Using A_1 + nd instead of A_1 + (n − 1)d (off-by-one), and similarly G_1 rⁿ instead of G_1 r^(n−1).
- Counting terms in ∑_{k=m}^{n}: there are n − m + 1 terms, not n (e.g. ∑_{k=2}^{5} 3 = 12, not 15).
- Sign errors with negative d or r: subtracting a negative (−5 − (−1)), odd vs even powers of a negative number ((−1/3)³ < 0, (−1/2)⁴ > 0).
- Forgetting the ± when taking even roots (geometric mean ±√(ab); r⁴ = 16 ⇒ r = ±2) — and then forgetting that both signs give valid sequences.
- Finding the ratio as G_n/G_(n+1) (upside down) or the difference as a_n − a_(n+1).
- Thinking a sequence is arithmetic because the first few differences look regular; the test must show a_(n+1) − a_n is a constant (no n left).
- Joining the dots of a sequence graph into a continuous line.
- Fibonacci indexing confusion: the book starts at F_0, so the "12th term" of the list is F_11.
- In "insert k means between a and b", using n = k instead of n = k + 2 total terms.
- In telescoping sums, keeping the wrong surviving terms (only the first part of the first bracket and the last part of the last bracket survive).
- Solving n(n + 1)/2 = S and not rejecting the negative root.

**Ideas suited to interactive practice with generated numbers**

- List terms from a formula: random linear a_n = pn + q, quadratic, (±1/b)^(n−1), n/(n + c); ask for a_1…a_5 or a single a_k.
- nth term of an arithmetic sequence: a_n = a_1 + (n − 1)d, random a_1, d (including negatives and simple fractions), n.
- Two-term problems: random a_1, d, pick two indices p < q, show A_p and A_q, ask for A_1, d, A_n and a further term.
- Next terms / common difference / common ratio from the first four terms (random arithmetic or geometric; mix them so students must decide which).
- nth term of a geometric sequence: G_n = G_1 r^(n−1), random small G_1 and r ∈ {±2, ±3, ±1/2, ±1/3}, n ≤ 8.
- Arithmetic mean / inserting k arithmetic means between random a and b chosen so d is an integer.
- Geometric mean between a and b with ab a perfect square (answer ±√(ab)).
- "Is it arithmetic?" — generate pn + q (yes), n² + … or cⁿ (no); student computes a_(n+1) − a_n.
- Recursive sequences: random two seeds a_0, a_1 with a_n = a_(n−1) + a_(n−2); ask for the k-th term.
- Sigma expansion and evaluation: random ∑_{k=m}^{n} (pk + q) or k², with lower limit ≠ 1 to train term counting.
- Gauss sums: S_n = n(n + 1)/2 for random n; reverse problem (given S, find n) using triangular numbers.
- Arithmetic series: S_n = (n/2)[2A_1 + (n − 1)d] and S_n = n(A_1 + A_n)/2, random A_1, d, n; reverse problems (given S_n and A_1, find A_n).
- Telescoping: a_n = c/((n + p)(n + p + 1)) with random c, p; answer S_n = c[1/(p + 1) − 1/(n + p + 1)].
- Visual/drag activities: Fibonacci squares rectangle (Activity 1.2), sequence dot-plots where students place points, Gauss forward/backward pairing animation.

### u1-b

**Key ideas by section**
- 1.3.1 (end) Sum of arithmetic sequences: S_n = (n/2)(A_1 + A_n) = (n/2)[2A_1 + (n − 1)d]; counting "how many multiples of k up to N" (N/k); inclusion–exclusion for "divisible by 2 or 5".
- 1.3.2 Sum of geometric sequences: derivation by "multiply by r and subtract"; S_n = G_1(1 − r^n)/(1 − r) = G_1(r^n − 1)/(r − 1), r ≠ 1, and S_n = nG_1 if r = 1; splitting a sum of 6 terms as (first 3) + r³(first 3); solving for n from a given sum (2^n = 1024).
- 1.4.1 Convergence of the sequence r^n (r > 1 diverges, r = 1 → 1, |r| < 1 → 0, r ≤ −1 vibrates); Definition 1.5 (series converges when S_n → s); S_∞ = G_1/(1 − r) only when |r| < 1; rewriting a sigma term like 5^(3−k) or (−1)^(k+1)(2/3)^k into the form G_1 r^(k−1) to read off G_1 and r.
- 1.4.2 Recurring decimals: a repeating block is a geometric series with r = 1/10^(period); pure recurring → digits over 9s; mixed recurring → split off the non-repeating part (or the (whole − non-repeating)/(9s followed by 0s) rule).
- 1.5 Applications: salaries/savings/prizes/seating/frames (arithmetic: A_n and S_n, often a quadratic in n); depreciation, population growth, compound interest, radioactive decay (geometric, multiplier 1 ± rate); limiting totals (flower height, bouncing ball, nested squares/triangles: areas ratio = (side ratio)²).
- Review Exercise extras: sigma rules (∑(ax + by) = a∑x + b∑y, ∑c = nc, (∑x)² ≠ ∑x²), telescoping sums, A_n = S_n − S_(n−1), three-term GP set-up a/r, a, ar, exponent sums like 4^(1 + 1/2 + …).

**Common student mistakes to expect**
- Using S_∞ = G_1/(1 − r) when |r| ≥ 1 (e.g. Exercise 1.20c, r = 5), or forgetting to check |r| < 1 at the end (Q18, Q20).
- Getting r upside down (dividing the earlier term by the later one), or taking r = 0.12 instead of 0.01 in 0.12, 0.0012, ….
- Sign errors with negative ratios: (−2/3)^k, 1 − (−2/3) = 5/3, and r^6 = 64/729 having two roots r = ±2/3.
- Thinking an alternating sequence like (−1/2)^n "vibrates" — it converges to 0; only r ≤ −1 vibrates. (The book itself slips on p.37, writing "diverges" for (2/3)^n.)
- Mixing up the number of terms with the last term (Example 3: 10 terms, last term 100), or counting n wrongly for "between 100 and 1000" (inclusive vs exclusive) and for raises every 6 months.
- In compound-interest problems, confusing "amount at end of year n" (3500 × 1.06^n) with the book's G_n = G_1(1.06)^(n−1) where G_1 is the deposit.
- Using r as a percentage (r = 60) instead of a decimal in the bouncing-ball formula.
- Recurring decimals: treating a mixed recurring decimal like a pure one (0.37̄ ≠ 37/99); forgetting the whole-number part in 3.7̇.
- Writing (∑x_i)² = ∑x_i² and dropping the constant term ∑3 = 15 (not 3) in sigma problems.
- Quadratics in n: keeping a negative or fractional root (n = −16, n = 29/3) instead of rejecting it; or missing that both roots can be valid (Review Q11: n = 5 and n = 20).

**Ideas that suit interactive practice with generated numbers**
- Arithmetic partial sum: random A_1, d, n → compute S_n both ways; reverse problems: given S_n and A_1 find A_n or d.
- "Sum of multiples of k from 1 to N" and "divisible by p or q" (inclusion–exclusion) with random k, p, q, N.
- Finite geometric sum S_n = G_1(1 − r^n)/(1 − r) with random G_1 and fractional r; reverse: given S_n find n (choose r = 1/2 or 3 so 2^n or 3^n is recognisable).
- Sum of first 3 terms = s, next 3 terms = t → r³ = t/s (generate r first, e.g. r ∈ {2, 3, −2, 1/2}, so the answers are clean).
- Classify r^n: random r (including negatives, fractions, √2-type) → converge / diverge / vibrate.
- Sum of an infinite geometric series S = a/(1 − r), |r| < 1, random a and r; include some |r| ≥ 1 items where the right answer is "no sum".
- Sigma-to-geometric rewriting: random ∑ c·b^(k+m) → identify G_1 and r, then S_∞.
- Recurring decimal → fraction: random repeating block (1–3 digits) and optional non-repeating prefix; check by long division.
- Applications with sliders: compound interest/depreciation (random principal, rate, years); salary raise problems (random start, raise, year); bouncing ball total distance h(1 + r)/(1 − r) with random h and rebound fraction, showing partial sums approaching the limit; nested squares/triangles area sums.
- Sigma rules drill: generate actual lists x_i, y_i (so the data is consistent, unlike Review Q8), compute ∑x, ∑y, ∑x², ∑xy, then ask for ∑(ax + by + c) and ∑(ax + by)².
