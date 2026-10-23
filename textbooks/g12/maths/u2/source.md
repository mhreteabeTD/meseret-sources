# Grade 12 Mathematics (2023, new curriculum) — Unit 2 Introduction to Calculus

Source: `textbooks/g12/maths/full.pdf` (see catalog.json), book pages 61–158 (PDF page = book page + 10).
Transcribed once from page images; every exercise, activity and review question answered with full working and checked. `[review: …]` = for a teacher. `[added step: …]` = a step the book skips.

# Unit 2 Introduction to Calculus

(p.61)

[figure: unit opener banner "UNIT 2" with a red circle containing the numeral 2; title "INTRODUCTION TO CALCULUS"]

## Unit Outcomes

By the end of this unit, you will be able to:

- Deduce rate of change of different quantities.
- Calculate rate of change of different quantities.
- Understand gradient of functions at a point.
- Analyze the geometrical and mechanical meaning of derivative.
- Find the derivative of simple functions using gradient method.
- Find area of a region bounded by a function and x-axis on a given interval.
- Understand definite integral.
- Value the real world contributions of having skills of derivatives and integrations.
- Apply the knowledge of integral calculus to solve real life mathematical problems.
- Apply the concept of derivatives to solve basic problems in business, economics, and road taxation.

(p.62)

## Unit Contents

- 2.1 Introduction to Derivatives
- 2.2 Applications of Derivative
- 2.3 Introduction to Integration
- Summary
- Review Exercise

## Key Words

- Absolute maximum
- Partial sums
- Extreme values
- Differentiation
- Absolute minimum
- Rate of change
- Anti-derivative
- Area
- Critical number
- Definite integral
- Derivative
- First derivative test
- Fundamental theorem
- Gradient
- Indefinite integral
- Partial fraction
- Relative maximum
- Relative minimum
- Secant
- Tangent
- Volume

## Introduction

In our daily life, we come across things that change according to some well recognizable rules. Many physical phenomena involve changing quantities such as the speed of a rocket, the inflation of currency, the number of bacteria in a culture, the shock intensity of an earthquake, the AC voltage of an electric signal, and so on.

Calculus is one of the components of mathematics that is concerned with change and motion; it deals with quantities that approach other quantities. Thus, the knowledge of calculus is essential, especially when dealing with quantities that change at a variable rate; you need to understand the concept of a derivative, which is the mathematical tool that is used to study the rates at which physical quantities change. The derivative is the exact rate at which one quantity changes with respect to another. Geometrically, the derivative is the slope of a curve at a point on the curve, defined as the slope of the tangent to the curve at the same point. The process of finding the derivative is called differentiation. This process is central to the branch of

(p.63)

mathematics called differential calculus. In this unit, you are going to study the meaning and techniques of differentiation, applications of derivatives, and integration.

### Historical Notes

Calculus, known in its early history as infinitesimal calculus, is a mathematical discipline focused on limits, continuity, derivatives, integrals, and infinite series. Isaac Newton and Gottfried Wilhelm Leibniz independently developed the theory of infinitesimal calculus in the late 17th century. Newton was only 22 at the time.

## 2.1 Introduction to Derivatives

### 2.1.1 Understanding Rates of Change

#### Rate of change

### Activity 2.1

1. Consider a square of length of side 4 cm.

   a. If the length of the side of the square increases by 1 cm, find the change in the perimeter of the square.

   **Answer:** The perimeter increases by 4 cm (from 16 cm to 20 cm).
   **Why:**
   Perimeter of a square: P = 4s.
   Original side s = 4 cm, so P = 4 × 4 = 16 cm.
   New side s = 4 + 1 = 5 cm, so P = 4 × 5 = 20 cm.
   Change in perimeter ΔP = 20 − 16 = 4 cm.
   (Check: ΔP = 4 × Δs = 4 × 1 = 4 cm.)

   b. If the length of the side of the square increases by 1 cm/s find the perimeter of the square when t = 1s, 2s, 3s.

   **Answer:** P = 20 cm at t = 1 s, 24 cm at t = 2 s, 28 cm at t = 3 s.
   **Why:**
   Assume the side is 4 cm at t = 0 and grows by 1 cm each second. [review: the book does not say when t = 0; working assumes the side is 4 cm at t = 0]
   Side at time t: s(t) = 4 + 1·t = 4 + t.
   Perimeter: P(t) = 4s(t) = 4(4 + t) = 16 + 4t.
   t = 1: s = 5 cm, P = 4 × 5 = 20 cm.
   t = 2: s = 6 cm, P = 4 × 6 = 24 cm.
   t = 3: s = 7 cm, P = 4 × 7 = 28 cm.

   c. What is the time rate of change of the perimeter of the square when its length of side increases by 2 cm/s?

   **Answer:** 8 cm/s.
   **Why:**
   P = 4s.
   If s increases by 2 cm every second, then in Δt seconds Δs = 2Δt.
   ΔP = 4Δs = 4 × 2Δt = 8Δt.
   Rate of change of perimeter = ΔP/Δt = 8Δt/Δt = 8 cm/s.
   (It does not depend on the current side length, because P is a linear function of s.)

2. What does a rate of change mean?

   **Answer:** A rate of change tells how much one quantity changes for each unit change in another quantity: (change in output)/(change in input).
   **Why:**
   In part 1c the perimeter changes by 8 cm for each 1 s of time, so its rate of change with respect to time is 8 cm per second.
   In general, if y changes by Δy when x changes by Δx, the rate of change of y with respect to x is Δy/Δx, measured in output units per input unit (this is Definition 2.1 below).

The fundamental philosophical truth is that everything changes. In physics, the change in position is known as displacement, in economics, the price change is known as inflation, in business, the change in costs is sometimes known as a trend, in mathematics, the change in values of a function is known as the derivative. But, to understand the derivatives, which measure instantaneous change, we need to understand the concepts of change and average change over intervals.

(p.64)

### Definition 2.1

**A rate of change** is a rate that describes how one quantity changes in relation to another quantity. The units on a rate of change are output units per input units.

For Example: Cost per minute, plants per hectare, kilometers per liter of benzene, salary per month, population per square kilometer, etc.

Rates of change can be positive or negative or even zero. When a quantity does not change over time, it has zero rates of change.

1. **A positive rate of change** is the case when the values of the two quantities (say x and y) increases at the same time and the graph slopes upward (See Figure 2.1).

   [figure: Figure 2.1 — a straight line starting at the origin O and rising to the right (blue arrow), with a second marked point on it; positive slope]

2. **Negative rate of change** is the case when the value of one quantity (say x) increases and the value of the other quantity (say y) decreases. The graph slopes downward (See Figure 2.2).

   [figure: Figure 2.2 — a straight line segment in the first quadrant falling from upper left to lower right (green arrow), with two marked points; negative slope]

(p.65)

3. **Zero rate of change** is the case when the value of one quantity (say x) increases, the value of the other quantity (say y) remains constant. The graph is a horizontal line.

   [figure: Figure 2.3 — a horizontal line starting on the y-axis above the origin and running to the right (purple arrow), with two marked points at the same height; zero slope]

### Example

Calculate the rate of change for the following pair of numbers.

a. (1, 2) and (3, 4)  b. (2, 3) and (3, 1)  c. (0, 2) and (2, 2)  d. (2, 0) and (2, 2)

**Solution**

a. Rate of change = (change in y)/(change in x) = (y₂ − y₁)/(x₂ − x₁) = (4 − 2)/(3 − 1) = 2/2 = 1.
Thus, the rate of change is positive.

b. Rate of change = (change in y)/(change in x) = (y₂ − y₁)/(x₂ − x₁) = (1 − 3)/(3 − 2) = −2/1 = −2.
Thus, the rate of change is negative.

c. Rate of change = (change in y)/(change in x) = (y₂ − y₁)/(x₂ − x₁) = (2 − 2)/(2 − 0) = 0/2 = 0.
Thus, the rate of change is zero.

d. Rate of change = (change in y)/(change in x) = (y₂ − y₁)/(x₂ − x₁) = (2 − 0)/(2 − 2) = 2/0 (undefined).
Thus, the rate of change is undefined.
[added step: division by zero is not defined; the two points lie on the vertical line x = 2.]

(p.66)

### Remark

A function is increasing where its rate of change is positive and decreasing where its rate of change is negative.

### Exercise 2.1

Calculate the rate of change for the following pairs of numbers:

a. (4, 6) and (5, 9)

**Answer:** 3
**Why:**
Rate of change = (y₂ − y₁)/(x₂ − x₁).
y₂ − y₁ = 9 − 6 = 3.
x₂ − x₁ = 5 − 4 = 1.
Rate of change = 3/1 = 3 (positive).

b. (4, 7) and (5, 6)

**Answer:** −1
**Why:**
y₂ − y₁ = 6 − 7 = −1.
x₂ − x₁ = 5 − 4 = 1.
Rate of change = −1/1 = −1 (negative).

c. (1, 2) and (3, −4)

**Answer:** −3
**Why:**
y₂ − y₁ = −4 − 2 = −6.
x₂ − x₁ = 3 − 1 = 2.
Rate of change = −6/2 = −3 (negative).

d. (−2, 4) and (3, −6)

**Answer:** −2
**Why:**
y₂ − y₁ = −6 − 4 = −10.
x₂ − x₁ = 3 − (−2) = 3 + 2 = 5.
Rate of change = −10/5 = −2 (negative).

e. (0, 9) and (9, 9)

**Answer:** 0
**Why:**
y₂ − y₁ = 9 − 9 = 0.
x₂ − x₁ = 9 − 0 = 9.
Rate of change = 0/9 = 0 (zero; horizontal line y = 9).

f. (8, 0) and (8, 8)

**Answer:** Undefined
**Why:**
y₂ − y₁ = 8 − 0 = 8.
x₂ − x₁ = 8 − 8 = 0.
Rate of change = 8/0, which is undefined (vertical line x = 8).

g. (3, −1) and (1, −1)

**Answer:** 0
**Why:**
y₂ − y₁ = −1 − (−1) = −1 + 1 = 0.
x₂ − x₁ = 1 − 3 = −2.
Rate of change = 0/(−2) = 0 (zero; horizontal line y = −1).

### Note

The two kinds of rate of change are average rate of change and instantaneous rate of change.

#### Average rate of change

### Definition 2.2

If y = f(x) is a function, then the **average rate of change** of y with respect to x on the interval [a, b] is given by the expression:

Average rate of change = (change in y)/(change in x) = Δy/Δx = (f(b) − f(a))/(b − a).

### Example 1

Find the average rate of change of a function f(x) = 2x − 9 beteween x₁ = 3 and x₂ = 6. ("beteween" is the book's spelling.)

(p.67)

**Solution**

**Step 1:** Write the formula for the average rate of change over the interval x₁ ≤ x ≤ x₂

(f(x₂) − f(x₁))/(x₂ − x₁).

**Step 2:** Solve for f(x₁) and f(x₂).

f(x₂) = f(6) = 2(6) − 9 = 12 − 9 = 3 and f(x₁) = f(3) = 2(3) − 9 = 6 − 9 = −3

**Step 3:** Substitute the known values into the formula and simplify.

(f(x₂) − f(x₁))/(x₂ − x₁) = (f(6) − f(3))/(6 − 3) = (3 − (−3))/3 = 2.
[added step: 3 − (−3) = 3 + 3 = 6, and 6/3 = 2.]

### Example 2

Examine the motion of a car that travels along a straight road and assume that we can measure the distance traveled by the car (in meter) at 1-second intervals as in the following chart:

| T(s) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| S(m) | 0 | 2 | 10 | 25 | 43 | 78 |

a. Find the average velocity during the time interval 2 ≤ t ≤ 4.
b. Find the average velocity during the time interval 2 ≤ t ≤ 3.

**Solution**

a. **Step 1:** Write the formula for the average rate of change over the interval a ≤ x ≤ b

Average rate of change = (f(b) − f(a))/(b − a)

**Step 2:** Identify the two points corresponding to the interval

(a, f(a)) = (2, 10) and (b, f(b)) = (4, 43)

**Step 3:** Substitute the values into the formula and simplify

Average rate of change = (f(b) − f(a))/(b − a) = (43 − 10)/(4 − 2) = 16.5 m/s.
[added step: 43 − 10 = 33, 4 − 2 = 2, 33/2 = 16.5.]

(p.68)

b. Similarly, Average velocity = (distance travelled)/(time elapsed) = (25 − 10)/(3 − 2) = 15 m/s.
[added step: (2, 10) and (3, 25) are the points; 25 − 10 = 15, 3 − 2 = 1, 15/1 = 15.]

### Example 3

The accompanying figure shows the graph of a function f. Find the average rate of change of the function f over the interval 0 ≤ x ≤ 9:

[figure: Figure 2.4 — graph of y = f(x) on a grid with x from about −8 to 9 and y from −8 to 10. The curve starts as a short horizontal piece near y ≈ 5 around x ≈ −5 to −4, drops steeply to a minimum (blue dot) of about y = −7 near x = 0, rises to a small bump near x ≈ 2, levels off near y ≈ 1 around x ≈ 6–7, then rises to a blue dot at about (9, 3).]

**Solution**

**Step 1:** Write the formula for the average rate of change over the interval 0 ≤ x ≤ 9

(f(x₂) − f(x₁))/(x₂ − x₁), where x₁ = 0 and x₂ = 9.

**Step 2:** Observe from the graph the value of f(0) and f(9). We can see from the graph that f(0) = −7 and f(9) = 3.

**Step 3:** Substitute the known values into the formula.

Average rate of change = (f(x₂) − f(x₁))/(x₂ − x₁) = (f(9) − f(0))/(9 − 0) = (3 − (−7))/9 = 10/9.

**Note:** The average rate of change is a measure of how much the function changed per unit, on average, over the interval. Geometrically, the average rate of change of a function y = f(x) on the interval [a, b] is the slope of the **secant line** through (a, f(a)) and (b, f(b)) See Figure 2.5.

[figure: Figure 2.5 — a curve (red) that rises to a maximum and then falls; points (a, f(a)) on the rising part and (b, f(b)) on the falling part are joined by a straight blue "Secant line" that extends beyond both points; a and b marked on the x-axis]

(p.69)

### Exercise 2.2

1. Compute the average rate of change of

   a. f(x) = 3x − 2 over the interval 0 ≤ x ≤ 2

   **Answer:** 3
   **Why:**
   Average rate of change = (f(2) − f(0))/(2 − 0).
   f(2) = 3(2) − 2 = 6 − 2 = 4.
   f(0) = 3(0) − 2 = −2.
   f(2) − f(0) = 4 − (−2) = 6.
   Average rate of change = 6/2 = 3.
   (Check: f is linear with slope 3, so every average rate of change is 3.)

   b. f(x) = x³ − 3x over the interval 1 ≤ x ≤ 6

   **Answer:** 40
   **Why:**
   Average rate of change = (f(6) − f(1))/(6 − 1).
   f(6) = 6³ − 3(6) = 216 − 18 = 198.
   f(1) = 1³ − 3(1) = 1 − 3 = −2.
   f(6) − f(1) = 198 − (−2) = 200.
   6 − 1 = 5.
   Average rate of change = 200/5 = 40.

   c. f(x) = 3x − 2 on the interval [1, 5]

   **Answer:** 3
   **Why:**
   Average rate of change = (f(5) − f(1))/(5 − 1).
   f(5) = 3(5) − 2 = 15 − 2 = 13.
   f(1) = 3(1) − 2 = 1.
   f(5) − f(1) = 13 − 1 = 12.
   5 − 1 = 4.
   Average rate of change = 12/4 = 3 (same as part a, because f is a straight line of slope 3).

   d. f(x) = x² + 3x + 1 on the interval [0, k]

   **Answer:** k + 3 (for k > 0)
   **Why:**
   Average rate of change = (f(k) − f(0))/(k − 0).
   f(k) = k² + 3k + 1.
   f(0) = 0² + 3(0) + 1 = 1.
   f(k) − f(0) = k² + 3k + 1 − 1 = k² + 3k.
   Average rate of change = (k² + 3k)/k.
   Factor the numerator: k² + 3k = k(k + 3).
   Cancel k (k ≠ 0, since [0, k] must be an interval): k(k + 3)/k = k + 3.
   (Check with k = 1: f(1) = 5, (5 − 1)/1 = 4 = 1 + 3. ✓)

2. In the following table, the average cost in Birr of a gallon of gasoline for the years 2005–2013 is illustrated. Using the data in the table, find the average rate of change of the price of gasoline between 2007 and 2009.

   | x | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 |
   |---|---|---|---|---|---|---|---|---|---|
   | c(x) | 2.31 | 2.62 | 2.84 | 3.30 | 2.41 | 2.84 | 3.58 | 3.68 | 4.21 |

   **Answer:** −0.215 Birr per gallon per year (the price fell on average by about 0.22 Birr per year).
   **Why:**
   Average rate of change = (c(2009) − c(2007))/(2009 − 2007).
   From the table: c(2009) = 2.41 and c(2007) = 2.84.
   c(2009) − c(2007) = 2.41 − 2.84 = −0.43.
   2009 − 2007 = 2.
   Average rate of change = −0.43/2 = −0.215 Birr per year.
   The negative sign means the price decreased over this period.

3. A candle has a starting length of 10 cm. Thirty minutes after lighting it, the length became 7 cm. Determine the rate of change in the length of the candle as it burns. Determine how long the candle takes to completely burn out.

   **Answer:** Rate of change = −0.1 cm/min (it gets shorter by 0.1 cm each minute, i.e. −6 cm per hour); it burns out after 100 minutes (1 hour 40 minutes).
   **Why:**
   Assume the candle burns at a constant rate.
   Points (time in min, length in cm): (0, 10) and (30, 7).
   Change in length = 7 − 10 = −3 cm.
   Change in time = 30 − 0 = 30 min.
   Rate of change = −3/30 = −0.1 cm/min.
   Length after t minutes: L(t) = 10 − 0.1t.
   Burnt out when L(t) = 0: 10 − 0.1t = 0.
   0.1t = 10.
   t = 10/0.1 = 100 minutes.
   (Check: L(100) = 10 − 0.1 × 100 = 0. ✓)

#### Instantaneous Rate of Change

For many of the functions such as polynomial, trigonometric, exponential, logarithmic, and rational functions, it is possible to find their instantaneous rate of change for values of x in their domain.

### Activity 2.2

Let y = x³.

i. Find the average rate of change of the given function on the following intervals.

a. x = 1 and x = 1.1

**Answer:** 3.31
**Why:**
Average rate of change = (f(1.1) − f(1))/(1.1 − 1).
f(1.1) = 1.1³ = 1.1 × 1.1 × 1.1 = 1.21 × 1.1 = 1.331.
f(1) = 1³ = 1.
f(1.1) − f(1) = 1.331 − 1 = 0.331.
1.1 − 1 = 0.1.
Average rate of change = 0.331/0.1 = 3.31.

b. x = 1 and x = 1.001

**Answer:** 3.003001
**Why:**
f(1.001) = 1.001³. Using (1 + a)³ = 1 + 3a + 3a² + a³ with a = 0.001:
1.001³ = 1 + 0.003 + 0.000003 + 0.000000001 = 1.003003001.
f(1.001) − f(1) = 1.003003001 − 1 = 0.003003001.
1.001 − 1 = 0.001.
Average rate of change = 0.003003001/0.001 = 3.003001.

c. x = 1 and x = 1 + Δx

**Answer:** 3 + 3Δx + (Δx)²
**Why:**
Average rate of change = (f(1 + Δx) − f(1))/((1 + Δx) − 1) = ((1 + Δx)³ − 1)/Δx.
Expand: (1 + Δx)³ = 1 + 3Δx + 3(Δx)² + (Δx)³.
Numerator: 1 + 3Δx + 3(Δx)² + (Δx)³ − 1 = 3Δx + 3(Δx)² + (Δx)³.
Factor Δx: Δx(3 + 3Δx + (Δx)²).
Divide by Δx (Δx ≠ 0): 3 + 3Δx + (Δx)².
(Check: Δx = 0.1 gives 3 + 0.3 + 0.01 = 3.31, matching part a. ✓)

ii. Determine what happens as Δx approaches 0.

**Answer:** The average rate of change approaches 3.
**Why:**
From i c, average rate of change = 3 + 3Δx + (Δx)².
As Δx → 0: 3Δx → 0 and (Δx)² → 0.
So the average rate of change → 3 + 0 + 0 = 3.
This matches the numbers in a (3.31) and b (3.003001), which get closer to 3 as the interval shrinks. The value 3 is the instantaneous rate of change of y = x³ at x = 1.

(p.70)

### Definition 2.3

The instantaneous rate of change is the change at that particular moment.

Instantaneous rate of change = Δy/Δx = (y₂ − y₁)/(x₂ − x₁), where Δx gets closer and closer to zero.

### Note

**Average rate** of change is the rate of change over the entire period. The **instantaneous rate** of change is the change at a certain period of time.

Therefore, when h gets closer and closer to zero, the instantaneous rate of change of a function f at x = x₀ is Δy/Δx = (f(x₀ + h) − f(x₀))/h.

### Example 1

Evaluate the instantaneous rate of change of f(x) = 2x² + 9 at x = −3.

**Solution**

The instantaneous rate of change of a function f at x = x₀ is

Δy/Δx = (f(x₀ + h) − f(x₀))/h, as h gets closer and closer to zero. For the given function f(x) = 2x² + 9 at x = −3, the instantaneous rate of change is

Instantaneous rate of change = (f(−3 + h) − f(−3))/h
= (2(−3 + h)² + 9 − (2(−3)² + 9))/h = (2(h² − 6h + 9) + 9 − (18 + 9))/h
= (2h² − 12h + 18 + 9 − (18 + 9))/h = (2h² − 12h)/h
= 2h − 12, as h gets closer and closer to zero
= −12.

Thus, the instantaneous rate of change is −12.

[added step: (−3 + h)² = 9 − 6h + h² = h² − 6h + 9; 2(−3)² = 2 × 9 = 18; (2h² − 12h)/h = h(2h − 12)/h = 2h − 12 for h ≠ 0; as h → 0, 2h → 0.]

(p.71)

### Example 2

Find the instantaneous rate of change of f(x) = √x at x = x₀ > 0.

**Solution**

Recall that the instantaneous rate of change of a function f(x) when x = x₀ is

Instantaneous rate of change = (f(x₀ + h) − f(x₀))/h
= (√(x₀ + h) − √x₀)/h, rationalizing the numerator
= ((√(x₀ + h) − √x₀)/h) × ((√(x₀ + h) + √x₀)/(√(x₀ + h) + √x₀))
= h/(h(√(x₀ + h) + √x₀))
= 1/(√(x₀ + h) + √x₀), as h gets closer and closer to zero
= 1/(2√x₀).

[added step: numerator (√(x₀ + h) − √x₀)(√(x₀ + h) + √x₀) = (x₀ + h) − x₀ = h (difference of squares); cancel h (h ≠ 0); as h → 0, √(x₀ + h) → √x₀, so the denominator → √x₀ + √x₀ = 2√x₀.]

Instantaneous rates of change have many real-world applications; for example, the velocity of a moving body at a particular time is the instantaneous rate of change of the displacement at that time. In the final example, we will consider a real-world problem and determine the instantaneous rate of change at a particular time for a polynomial function representing the biomass of a bacterial culture.

### Example 3

The biomass of a bacterial culture in milligrams as a function of time in minutes is given by f(t) = 71t³ + 63. What is the instantaneous rate of growth of the culture when t = 2 minutes?

(p.72)

**Solution**

In this example, we want to determine the instantaneous rate of change of a cubic function representing the biomass of a bacterial culture.

Recall that the instantaneous rate of change of a function f(t) when t = t₀ is

Instantineous rate of change = (f(2 + h) − f(2))/h
= (71(2 + h)³ + 63 − (71 × 2³ + 63))/h
= (71(h³ + 6h² + 12h + 8) − 71 × 8)/h
= (71h³ + 426h² + 852h)/h
= 71h² + 426h + 852, as h gets closer and closer to zero
= 852.

Since the rate of change is positive, it is equivalent to the rate of growth. Hence, the rate of growth of the biomass of a bacterial culture when t = 2 minutes is 852 mg/min.

[added step: (2 + h)³ = 8 + 12h + 6h² + h³; the +63 and −63 cancel; 71 × 8 = 568 cancels with 71 × 8; 71 × 6 = 426 and 71 × 12 = 852; dividing by h (h ≠ 0) gives 71h² + 426h + 852; as h → 0 the first two terms → 0. "Instantineous" is the book's spelling.]

The instantaneous rate of change is also related to the derivative, at an arbitrary point x. In particular, the instantaneous rate of change at x = x₀ of a function is the derivative of a function evaluated at x = x₀.

### Exercise 2.3

1. Evaluate the instantaneous rate of change of f(x) = 6x² − 3 at x = 1.

   **Answer:** 12
   **Why:**
   Instantaneous rate of change = (f(1 + h) − f(1))/h as h → 0.
   f(1 + h) = 6(1 + h)² − 3.
   Expand: (1 + h)² = 1 + 2h + h².
   f(1 + h) = 6(1 + 2h + h²) − 3 = 6 + 12h + 6h² − 3 = 3 + 12h + 6h².
   f(1) = 6(1)² − 3 = 6 − 3 = 3.
   f(1 + h) − f(1) = 3 + 12h + 6h² − 3 = 12h + 6h².
   Divide by h (h ≠ 0): (12h + 6h²)/h = 12 + 6h.
   As h → 0: 12 + 6h → 12.
   (Check with the power rule later in the unit: f′(x) = 12x, f′(1) = 12. ✓)

2. Find the instantaneous rate of change of f(x) = 2√x at x = x₀ > 0.

   **Answer:** 1/√x₀
   **Why:**
   Instantaneous rate of change = (f(x₀ + h) − f(x₀))/h as h → 0.
   = (2√(x₀ + h) − 2√x₀)/h = 2(√(x₀ + h) − √x₀)/h.
   Rationalize the numerator: multiply top and bottom by (√(x₀ + h) + √x₀).
   Numerator: 2(√(x₀ + h) − √x₀)(√(x₀ + h) + √x₀) = 2((x₀ + h) − x₀) = 2h.
   So the quotient = 2h/(h(√(x₀ + h) + √x₀)).
   Cancel h (h ≠ 0): 2/(√(x₀ + h) + √x₀).
   As h → 0: √(x₀ + h) → √x₀, so the quotient → 2/(√x₀ + √x₀) = 2/(2√x₀) = 1/√x₀.
   (Check: this is 2 × the result 1/(2√x₀) of Example 2. ✓ Numerically at x₀ = 4, h = 0.0001: (2√4.0001 − 4)/0.0001 ≈ 0.49999, and 1/√4 = 0.5. ✓)

3. The biomass of a bacterial culture in milligrams as a function of time in minutes is given by f(t) = 81t³ + 90. What is the instantaneous rate of growth of the culture when t = 3 minutes?

   **Answer:** 2187 mg/min
   **Why:**
   Instantaneous rate of change = (f(3 + h) − f(3))/h as h → 0.
   Expand: (3 + h)³ = 27 + 27h + 9h² + h³.
   f(3 + h) = 81(27 + 27h + 9h² + h³) + 90 = 2187 + 2187h + 729h² + 81h³ + 90.
   f(3) = 81(3)³ + 90 = 81 × 27 + 90 = 2187 + 90 = 2277.
   f(3 + h) − f(3) = 2187h + 729h² + 81h³ (the 2187 and the 90 cancel).
   Divide by h (h ≠ 0): 2187 + 729h + 81h².
   As h → 0: → 2187.
   The rate is positive, so the culture is growing at 2187 mg/min when t = 3 minutes.
   (Check: f′(t) = 243t², f′(3) = 243 × 9 = 2187. ✓)

(p.73)

### 2.1.2 Gradient of Curves and Rate of Changes

### Activity 2.3

1. What is a secant line to a curve? What is a tangent line to a curve?

   **Answer:** A secant line is a straight line that passes through two points of a curve. A tangent line is a straight line that touches the curve at one point and has the same direction (steepness) as the curve at that point.
   **Why:**
   A secant cuts the curve at (at least) two points, for example P(a, f(a)) and Q(b, f(b)); its slope is the average rate of change of f on [a, b].
   A tangent "just touches" the curve at the point of tangency; it is the limiting position of the secant lines PQ as Q moves along the curve towards P (Definition 2.4 and Figures 2.7, 2.8 below).

2. What is slope of a line? How can we calculate the slope of a line?

   **Answer:** The slope (gradient) of a line is the number that describes its steepness and direction: the vertical change divided by the horizontal change between any two points on the line, m = (y₂ − y₁)/(x₂ − x₁), x₁ ≠ x₂.
   **Why:**
   Take two points (x₁, y₁) and (x₂, y₂) on the line.
   Vertical change (rise) = y₂ − y₁; horizontal change (run) = x₂ − x₁.
   Slope m = rise/run = (y₂ − y₁)/(x₂ − x₁).
   If the line is written as y = mx + c, the slope is the coefficient m of x.
   m > 0: line goes up from left to right; m < 0: goes down; m = 0: horizontal; vertical line: slope undefined.

### Definition 2.4

a. **A tangent line** to a curve or a graph of a function y = f(x) is a line that touches the curve exactly at one point, but does not cross the curve. The point where the tangent line touches the graph is said to be the **point of tangency.**

b. **Gradient (slope)** is a number that describes steepness and direction of a line. If slope is positive, then the line is increasing, which means it goes up as we move from left to right. If slope is negative then the line is decreasing, which means it goes down when we move from left to right. If the slope is zero, then the line is horizontal.

[review: Definition 2.4a as printed ("touches the curve exactly at one point, but does not cross the curve") is only a simplified description: a tangent line can meet the curve again elsewhere (e.g. y = x³ − x at x = 1), and at an inflection point it does cross the curve (e.g. y = x³ at x = 0, tangent y = 0). Keep the book's wording but lessons should not test this as a precise rule.]

[figure: Figure 2.6 — a curve y = f(x) (red) on a grid with x from −1 to 6 and y from −0.5 to 2. The curve rises steeply from below the x-axis near x ≈ −0.5, passes a point A at about (−0.2, 0.55), reaches a maximum at point P ≈ (1.6, 1.45), then falls, passing point B at about (4, 0.75) and continuing down towards y ≈ 0.2 at x = 6. A green "Tangent line" touches the curve at P (drawn nearly horizontal, from about (−1, 1.35) to (4, 1.55)). A blue "Secant line" passes through A and B (from about (−1, 0.45) to (5, 0.85)), with a small positive slope ≈ 0.07.] [review: on p.73 Figure 2.6 the point coordinates are read from the grid and are approximate; the tangent at the maximum P should be horizontal but is drawn with a slight upward tilt]

**Note:** If we are given two points A(x₀, y₀) and B(x₁, y₁) on the graph of y = f(x), then using definition 2.2 and understanding that 'change' is the difference between

(p.74)

the two values we get the general formula for the slope of a secant line through the two points, which is given as:

Slope = (vertical change)/(horizontal change) = (change in y)/(change in x) = Δy/Δx = (y₁ − y₀)/(x₁ − x₀).

From this formula, we can see that the gradient of the secant line to the curve of a function is equal to the average rate of change.

> The slope of a secant line = average rate of change.

### Example 1

Find the slope of a line passing through the given two points.

a. (−5, 7) and (0, 0)  b. (3, −5) and (−2, 9)

**Solution**

a. Slope = Δy/Δx = (y₁ − y₀)/(x₁ − x₀) = (0 − (7))/(0 − (−5)) = −7/5 = −7/5.

b. Slope = Δy/Δx = (y₁ − y₀)/(x₁ − x₀) = (9 − (−5))/((−2 − 3)) = 14/(−5) = −14/5.

[added step: in a, 0 − (−5) = 0 + 5 = 5; in b, 9 − (−5) = 9 + 5 = 14 and −2 − 3 = −5.]

### Example 2

Find the slope of a secant line to the graph of the function f(x) = 2x³ + 3x − 5 over the interval [1, 3].

**Solution**

Given f(x) = 2x³ + 3x − 5

**Step 1:** Write the formula for the slope of a secant line over the interval 1 ≤ x ≤ 3.

Average rate of change = (f(3) − f(1))/(3 − 1).

(p.75)

**Step 2:** Solve for f(3) and f(1).

f(3) = 2(3)³ + 3(3) − 5 = 58 and f(1) = 2(1)³ + 3(1) − 5 = 0

[added step: 2(3)³ = 2 × 27 = 54, so f(3) = 54 + 9 − 5 = 58; f(1) = 2 + 3 − 5 = 0.]

**Step 3:** Substitute the known values into the formula and simplify.

Average rate of change = (f(3) − f(1))/(3 − 1) = (58 − 0)/2 = 29.

Therefore, the slope of a secant line to the graph of f(x) = 2x³ + 3x − 5 with respect to x over the interval [1, 3] is 29.

### Exercise 2.4

1. Find the slope of a line passing through the two given points.

   a. (−3, −5) and (3, 11)

   **Answer:** 8/3
   **Why:**
   Slope = (y₁ − y₀)/(x₁ − x₀).
   y₁ − y₀ = 11 − (−5) = 11 + 5 = 16.
   x₁ − x₀ = 3 − (−3) = 3 + 3 = 6.
   Slope = 16/6.
   Simplify by dividing top and bottom by 2: 16/6 = 8/3.

   b. (4, −9) and (5, −7)

   **Answer:** 2
   **Why:**
   y₁ − y₀ = −7 − (−9) = −7 + 9 = 2.
   x₁ − x₀ = 5 − 4 = 1.
   Slope = 2/1 = 2.

2. For each of the following functions, find the slope of a secant line to the graph of the functions over the given intervals.

   a. f(x) = x² + 1; [−1, 3]

   **Answer:** 2
   **Why:**
   Slope of secant = (f(3) − f(−1))/(3 − (−1)).
   f(3) = 3² + 1 = 9 + 1 = 10.
   f(−1) = (−1)² + 1 = 1 + 1 = 2.
   f(3) − f(−1) = 10 − 2 = 8.
   3 − (−1) = 4.
   Slope = 8/4 = 2.
   (Check: for f(x) = x² + c the secant slope on [a, b] is a + b = −1 + 3 = 2. ✓)

   b. g(x) = x³ − 4x + 6; [1, 2].

   **Answer:** 3
   **Why:**
   Slope of secant = (g(2) − g(1))/(2 − 1).
   g(2) = 2³ − 4(2) + 6 = 8 − 8 + 6 = 6.
   g(1) = 1³ − 4(1) + 6 = 1 − 4 + 6 = 3.
   g(2) − g(1) = 6 − 3 = 3.
   2 − 1 = 1.
   Slope = 3/1 = 3.

### 2.1.3 Gradient at a Point on a Curve

### Activity 2.4

1. Let f(x) = x². Compute and simplify the algebraic expression

   a. (f(x + h) − f(x))/h

   **Answer:** 2x + h (h ≠ 0)
   **Why:**
   f(x + h) = (x + h)².
   Expand: (x + h)² = x² + 2xh + h².
   f(x + h) − f(x) = x² + 2xh + h² − x² = 2xh + h².
   Factor h: 2xh + h² = h(2x + h).
   Divide by h (h ≠ 0): h(2x + h)/h = 2x + h.

   b. (f(x) − f(x₀))/(x − x₀)

   **Answer:** x + x₀ (x ≠ x₀)
   **Why:**
   f(x) − f(x₀) = x² − x₀².
   Factor as a difference of two squares: x² − x₀² = (x − x₀)(x + x₀).
   Divide by (x − x₀) (x ≠ x₀): (x − x₀)(x + x₀)/(x − x₀) = x + x₀.
   (Both forms tend to 2x (resp. 2x₀) as h → 0 (resp. x → x₀).)

2. Let y = x³.

   i. Find the slope of the secant line to the curve of the function between

   a. x = 1 and x = 1.1

   **Answer:** 3.31
   **Why:**
   Slope = (1.1³ − 1³)/(1.1 − 1).
   1.1³ = 1.21 × 1.1 = 1.331.
   1.331 − 1 = 0.331; 1.1 − 1 = 0.1.
   Slope = 0.331/0.1 = 3.31.

   b. x = 1 and x = 1.001

   **Answer:** 3.003001
   **Why:**
   1.001³ = 1 + 3(0.001) + 3(0.001)² + (0.001)³ = 1 + 0.003 + 0.000003 + 0.000000001 = 1.003003001.
   1.003003001 − 1 = 0.003003001; 1.001 − 1 = 0.001.
   Slope = 0.003003001/0.001 = 3.003001.

   c. x = 1 and x = 1 + h.

   **Answer:** 3 + 3h + h² (h ≠ 0)
   **Why:**
   Slope = ((1 + h)³ − 1³)/((1 + h) − 1) = ((1 + h)³ − 1)/h.
   Expand: (1 + h)³ = 1 + 3h + 3h² + h³.
   Numerator: 1 + 3h + 3h² + h³ − 1 = 3h + 3h² + h³ = h(3 + 3h + h²).
   Divide by h: 3 + 3h + h².
   (Check: h = 0.1 → 3 + 0.3 + 0.01 = 3.31 ✓; h = 0.001 → 3 + 0.003 + 0.000001 = 3.003001 ✓.)

   ii. Determine what happens as h approaches 0.

   **Answer:** The slope of the secant line approaches 3, the slope of the tangent line to y = x³ at (1, 1).
   **Why:**
   Slope of secant = 3 + 3h + h².
   As h → 0: 3h → 0 and h² → 0.
   So the slope → 3 + 0 + 0 = 3.
   (This is the same limit as in Activity 2.2.)

(p.76)

Suppose you are given some curve, and a point P on the curve as shown below in figures 2.7 a and b.

[figure: Figure 2.7a — a circle with its centre marked. Point P on the lower-left of the circle has a red tangent line L through it. Point Q₁ is on the upper-right of the circle; the blue line L₁ passes through P and Q₁ (a secant).]

[figure: Figure 2.7b — the same circle with point P, red tangent line L, blue secant L₁ through P and Q₁, and a green secant L₂ through P and a point Q₂ that lies closer to P than Q₁. L₂ is steeper than L₁ and closer in direction to L.]

- The line L passing through the point P is called a tangent line.
- Given another point Q₁ on the curve, let L₁ be the line passing through the points P and Q₁.
- L₁ is a secant line and is sometimes written as PQ₁.
- Pick a point Q₂ closer to P. Notice that the slope of the secant line L₂ is closer to the slope of L compared to the slope of L₁.
- As we pick points closer and closer to P, the slope of the associated secant lines will get closer and closer to the slope of the tangent line L.
- Let P (a, f (a)) be any point on the graph of a function f. Another point on the graph may be denoted by Q (a + h, f (a + h)), where h is the difference between the x-coordinates of Q and P (see Figure 2.8 a). By definition the slope m of the secant line through P and Q is

  m_PQ = m_secant = (f(a + h) − f(a))/h.

### Note

m_PQ denotes the slope of the secant line through P and Q and m_secant represents the slope of the secant line to the graph of f(x).

(p.77)

[figure: Figure 2.8 a — a wavy curve y = f(x) with point P(a, f(a)) above x = a and point Q(a + h, f(a + h)) above x = a + h; a straight purple secant line passes through P and Q; dashed vertical lines drop from P and Q to a and a + h on the x-axis.]

[figure: Figure 2.8 b — the same curve y = f(x) with only the point P(a, f(a)) above x = a; a straight purple line touches the curve at P (the tangent line, the limiting position of the secant as Q approaches P).]

If f is a given function, then we can make Q approach P by letting h approach 0 (see figure 2.8b) and we get the slope of the tangent line to the curve. It is natural, therefore, to define m as follows:

### Definition 2.5

If f is a function defined on an open interval containing a, then **as h gets closer and closer to zero**, the slope m of the tangent line to the graph of y = f(x) at the point P(a, f(a)) is given by: m = (f(a + h) − f(a))/h.

### Note

1. If we allow the quantity h to get smaller and smaller, the point (a + h, f(a + h)) is getting closer to (a, f(a)), which in turn means that the slope of the secant line through (a + h, f(a + h)) is getting closer to the slope of the tangent line at (a, f(a)).

   Hence, the slope of the graph of a function at a point is the same as the slope of the tangent line at that point.

2. The slope of a tangent line represents the **instantaneous rate of change** of the function at that one point. That is:

   The slope of a tangent line = instantaneous rate of change.

(p.78)

### Procedure to find gradient of a curve at a point

To find the gradient of a curve y = f(x) at x = a use the following procedure:

**Step 1:** Write the quotient difference (f(x) − f(a))/(x − a) of f at x = a.

**Step 2:** Compute the algebraic expression in step1 and simplify.

**Step 3:** Find the value of the result obtained in step 2 as the value of x approaches a.

The final result is the gradient of the tangent line to the curve y = f(x) at x = a.

### Example 1

Find the gradient (slope) of the functions f(x) = x² at x = 2.

**Solution**

Slope = (f(x) − f(2))/(x − 2) = (x² − 4)/(x − 2) = ((x − 2)(x + 2))/(x − 2) = x + 2.

Therefore, the slope of the function at x = 2 becomes

x + 2 |_{x=2} = 2 + 2 = 4

Note: x + 2 |_{x=2} means value obtained by substituting x = 2 to x + 2.

[added step: f(2) = 2² = 4; x² − 4 is a difference of two squares; cancel (x − 2) because x ≠ 2; then let x approach 2.]

### Example 2

If f(x) = x² find the gradient of the tangent line to the graph of f(x) at the point P(a, a²).

**Solution**

Given y = f(x) = x², using the above procedure, we have

i. (f(x) − f(a))/(x − a) = (x² − a²)/(x − a) = ((x − a)(x + a))/(x − a) = x + a

ii. As x approaches to a, the expression or the quantity x + a approaches 2a.

(p.79)

Therefore, the gradient of the tangent line to the curve y = f(x) = x² at the point P(a, a²) is m_tan = 2a, where m_tan denotes the slope of the tangent line to the graph of the function at the specified point of tangency.

This means that the instantaneous rate of change of the function at the point P is 2a, and that the gradient of the tangent to the graph of the curve f(x) = x² at any point is found by doubling the x-coordinate. For example, the gradient of the function f(x) = x² at the point P(4, 16) is equal to m_tan = 2(2) = 8, at P(−5, 25) is m_tan = −10, at the origin P(0, 0) is m_tan = 0. See Figure 2.9.

[review: book says "at the point P(4, 16) is equal to m_tan = 2(2) = 8", working gives m_tan = 2(4) = 8 because the gradient is double the x-coordinate 4; the final value 8 is right, the "2(2)" is a misprint]

[figure: Figure 2.9 — the parabola y = x² for x from −5 to 5 (y up to 25) with short green tangent segments at five points, labelled P(−5, 25), m_tan = −10; P(−2, 4), m_tan = −4; P(0, 0), m_tan = 0 (horizontal tangent along the x-axis); P(3, 9), m_tan = 6; P(4, 16), m_tan = 8.]

To clarify this idea condider the following table:

| x | −5 | −2 | 0 | 3 | 4 |
|---|---|---|---|---|---|
| f(x) = x² | 25 | 4 | 0 | 9 | 16 |
| Gradient (m) | −10 | −4 | 0 | 6 | 8 |

("condider" is the book's spelling.)

### Exercise 2.5

1. Find the gradients of the tangent lines to the graph of the following function at specified points.

   a. f(x) = x² at x = −1 and x = 4.

   **Answer:** Gradient −2 at x = −1; gradient 8 at x = 4.
   **Why:**
   Use the procedure with x = a:
   Step 1: (f(x) − f(a))/(x − a) = (x² − a²)/(x − a).
   Step 2: factor the difference of squares: (x − a)(x + a)/(x − a) = x + a (x ≠ a).
   Step 3: as x → a, x + a → 2a. So m_tan = 2a (as in Example 2).
   At x = −1: (x² − 1)/(x + 1) = (x + 1)(x − 1)/(x + 1) = x − 1 → −1 − 1 = −2.
   At x = 4: (x² − 16)/(x − 4) = (x − 4)(x + 4)/(x − 4) = x + 4 → 4 + 4 = 8.
   (Check with the table above: gradient at x = 4 is 8. ✓)

   b. f(x) = 3x² − 5x + 4 at x = 2 and x = −√2.

   **Answer:** Gradient 7 at x = 2; gradient −6√2 − 5 (≈ −13.49) at x = −√2.
   **Why:**
   Step 1: (f(x) − f(a))/(x − a) = ((3x² − 5x + 4) − (3a² − 5a + 4))/(x − a).
   The +4 and −4 cancel: numerator = 3x² − 3a² − 5x + 5a = 3(x² − a²) − 5(x − a).
   Factor: 3(x − a)(x + a) − 5(x − a) = (x − a)(3(x + a) − 5).
   Step 2: divide by (x − a) (x ≠ a): 3(x + a) − 5 = 3x + 3a − 5.
   Step 3: as x → a: 3a + 3a − 5 = 6a − 5.
   At x = 2: 6(2) − 5 = 12 − 5 = 7.
   Direct check at a = 2: f(2) = 12 − 10 + 4 = 6; (3x² − 5x + 4 − 6)/(x − 2) = (3x² − 5x − 2)/(x − 2) = (x − 2)(3x + 1)/(x − 2) = 3x + 1 → 3(2) + 1 = 7. ✓
   At x = −√2: 6(−√2) − 5 = −6√2 − 5 ≈ −8.485 − 5 = −13.485.
   (Check by the rules: f′(x) = 6x − 5, f′(−√2) = −6√2 − 5 ≈ −13.485. Numerically, (f(−√2 + 0.000001) − f(−√2))/0.000001 ≈ −13.485. ✓)

   c. g(x) = √x and x = 4.

   **Answer:** 1/4
   **Why:**
   Step 1: (g(x) − g(4))/(x − 4) = (√x − 2)/(x − 4).
   Step 2: write x − 4 = (√x)² − 2² = (√x − 2)(√x + 2) (x ≥ 0).
   So (√x − 2)/((√x − 2)(√x + 2)) = 1/(√x + 2) (x ≠ 4).
   Step 3: as x → 4, √x → 2, so 1/(√x + 2) → 1/(2 + 2) = 1/4.
   (Check with Example 2 on p.71: 1/(2√x₀) = 1/(2 × 2) = 1/4. ✓)

   d. f(x) = 1/x at the point (2, 1/2).

   **Answer:** −1/4
   **Why:**
   Step 1: (f(x) − f(2))/(x − 2) = (1/x − 1/2)/(x − 2).
   Combine the fractions in the numerator: 1/x − 1/2 = (2 − x)/(2x).
   So the quotient = (2 − x)/(2x(x − 2)).
   Step 2: 2 − x = −(x − 2), so the quotient = −(x − 2)/(2x(x − 2)) = −1/(2x) (x ≠ 2).
   Step 3: as x → 2: −1/(2 × 2) = −1/4.
   (Check: f′(x) = −1/x², f′(2) = −1/4. ✓)

(p.80)

2. If f(x) = x³, find the gradient of the tangent line to the graph of f(x) at the point P(a, a³).

   **Answer:** m_tan = 3a²
   **Why:**
   Step 1: (f(x) − f(a))/(x − a) = (x³ − a³)/(x − a).
   Factor the difference of cubes: x³ − a³ = (x − a)(x² + ax + a²).
   Step 2: divide by (x − a) (x ≠ a): x² + ax + a².
   Step 3: as x → a: a² + a·a + a² = 3a².
   (Check: at a = 1 this gives 3, the limit found in Activity 2.4. ✓)

### 2.1.4 Definition of Derivative

The slope concept usually pertains to straight lines. When a function is non-linear, its slope may vary from one point to the next. We must therefore introduce the notion of derivative which allows us to obtain the slope at all points of these non-linear functions.

#### 2.1.4.1 Derivative of function at a point

### Activity 2.5

Let f(x) = 1/x². Then

a. Simplify (f(x) − f(1))/(x − 1).

**Answer:** −(x + 1)/x² (x ≠ 0, x ≠ 1)
**Why:**
f(1) = 1/1² = 1.
f(x) − f(1) = 1/x² − 1 = (1 − x²)/x².
Factor: 1 − x² = (1 − x)(1 + x) = −(x − 1)(x + 1).
So (f(x) − f(1))/(x − 1) = −(x − 1)(x + 1)/(x²(x − 1)).
Cancel (x − 1) (x ≠ 1): −(x + 1)/x².
(As x → 1 this tends to −2/1 = −2, which is f′(1).)

b. Simplify (f(x + h) − f(x))/h.

**Answer:** −(2x + h)/(x²(x + h)²) (h ≠ 0, x ≠ 0, x + h ≠ 0)
**Why:**
f(x + h) − f(x) = 1/(x + h)² − 1/x².
Common denominator x²(x + h)²: = (x² − (x + h)²)/(x²(x + h)²).
Expand: (x + h)² = x² + 2xh + h², so x² − (x + h)² = x² − x² − 2xh − h² = −2xh − h² = −h(2x + h).
Divide by h: −h(2x + h)/(h x²(x + h)²) = −(2x + h)/(x²(x + h)²).
(As h → 0 this tends to −2x/x⁴ = −2/x³. Check at x = 1: −2/1 = −2, matching part a. ✓)

### Definition 2.6 (Derivatives of functions at a point)

The derivative of a function f(x) at a number "a" in the domain of f, denoted by f′(a), is the gradient of the tangent line to the graph of y = f(x) at (a, f(a)). That is, as h gets closer and closer to zero from both directions, (f(a + h) − f(a))/h becomes closer to f′(a).

### Note

- f′(a) is the slope of the line tangent to the graph of f at the point (a, f(a)).
- If y = f′(x) is defined, then we say that f has a derivative at a or f is differentiable at a.

[review: the note on p.80 prints "If y = f′(x) is defined"; the intended statement is "If f′(a) is defined (exists), then f has a derivative at a / f is differentiable at a"]

(p.81)

### Example

Use definition 2.6, to find the derivatives of the following functions at the given value of a.

a. f(x) = 5x − 3; a = −2  b. f(x) = x² + 3; a = 5  c. f(x) = √(2x + 4); a = 6

**Solution**

Using the definition, as h gets closer and closer to zero f′(a) = (f(a + h) − f(a))/h, and we have the following results:

a. f′(−2) = (f(−2 + h) − f(−2))/h
= ([5(−2 + h) − 3] − (−2 × 5 − 3))/h
= ((−10 + 5h − 3) − (−13))/h = 5h/h = 5.

[added step: −10 + 5h − 3 + 13 = 5h; 5h/h = 5 for h ≠ 0, and this stays 5 as h → 0.]

b. f′(5) = (f(5 + h) − f(5))/h
= ([(5 + h)² + 3] − (5² + 3))/h,
= (25 + 10h + h² + 3 − (25 + 3))/h
= (h² + 10h)/h
= h + 10 = 10 as h approaches to 0

c. f′(6) = (f(6 + h) − f(6))/h = (√(2(6 + h) + 4) − √(2(6) + 4))/h
= ((√(2h + 16) − √16)/h) × ((√(2h + 16) + √16)/(√(2h + 16) + √16)), rationalization
= (2h + 16 − 16)/(h(√(2h + 16) + √16)), simplification

(p.82)

= 2/(√(2h + 16) + √16) as h approaches to 0,
= 2/(√16 + √16) = 1/4.

[added step: 2(6 + h) + 4 = 12 + 2h + 4 = 2h + 16; (2h + 16 − 16) = 2h and 2h/h = 2; √16 + √16 = 4 + 4 = 8, and 2/8 = 1/4.]

### Exercise 2.6

Use definition 2.6, to find the derivatives of the following functions at the given value.

a. f(x) = 9x − 7, a = 2

**Answer:** f′(2) = 9
**Why:**
f′(2) = (f(2 + h) − f(2))/h as h → 0.
f(2 + h) = 9(2 + h) − 7 = 18 + 9h − 7 = 11 + 9h.
f(2) = 9(2) − 7 = 18 − 7 = 11.
f(2 + h) − f(2) = 11 + 9h − 11 = 9h.
9h/h = 9 (h ≠ 0), which stays 9 as h → 0.
f′(2) = 9. (Check: a straight line y = 9x − 7 has slope 9 everywhere. ✓)

b. f(x) = x² − 1, a = 2

**Answer:** f′(2) = 4
**Why:**
f(2 + h) = (2 + h)² − 1 = 4 + 4h + h² − 1 = 3 + 4h + h².
f(2) = 2² − 1 = 3.
f(2 + h) − f(2) = 4h + h².
(4h + h²)/h = 4 + h (h ≠ 0).
As h → 0: 4 + h → 4.
f′(2) = 4. (Check: f′(x) = 2x, f′(2) = 4. ✓)

c. f(x) = x³ + 2x, a = 3

**Answer:** f′(3) = 29
**Why:**
Expand: (3 + h)³ = 27 + 27h + 9h² + h³.
f(3 + h) = (3 + h)³ + 2(3 + h) = 27 + 27h + 9h² + h³ + 6 + 2h = 33 + 29h + 9h² + h³.
f(3) = 3³ + 2(3) = 27 + 6 = 33.
f(3 + h) − f(3) = 29h + 9h² + h³.
Divide by h (h ≠ 0): 29 + 9h + h².
As h → 0: → 29.
f′(3) = 29. (Check: f′(x) = 3x² + 2, f′(3) = 27 + 2 = 29. ✓)

d. f(x) = √(3x − 6), a = 3

**Answer:** f′(3) = 3/(2√3) = √3/2 ≈ 0.866
**Why:**
f(3 + h) = √(3(3 + h) − 6) = √(9 + 3h − 6) = √(3 + 3h).
f(3) = √(9 − 6) = √3.
Quotient: (√(3 + 3h) − √3)/h.
Rationalize: multiply top and bottom by (√(3 + 3h) + √3).
Numerator: (3 + 3h) − 3 = 3h.
Quotient = 3h/(h(√(3 + 3h) + √3)) = 3/(√(3 + 3h) + √3) (h ≠ 0).
As h → 0: √(3 + 3h) → √3, so the quotient → 3/(√3 + √3) = 3/(2√3).
Rationalize the denominator: 3/(2√3) × √3/√3 = 3√3/6 = √3/2.
(Check: by the chain rule f′(x) = 3/(2√(3x − 6)), f′(3) = 3/(2√3) = √3/2. ✓)

#### 2.1.4.2 The derivative as a function

### Activity 2.6

For each of the following functions, find the set of values of x₀ such that f′(x₀) is defined and is unique.

a. f(x) = x²

**Answer:** All real numbers, ℝ (f′(x₀) = 2x₀).
**Why:**
(f(x₀ + h) − f(x₀))/h = ((x₀ + h)² − x₀²)/h = (x₀² + 2x₀h + h² − x₀²)/h = (2x₀h + h²)/h = 2x₀ + h.
As h → 0 from either side, 2x₀ + h → 2x₀.
This works for every real x₀, so f′(x₀) exists and is unique for all x₀ ∈ ℝ.

b. f(x) = |x|

**Answer:** All real numbers except 0, i.e. ℝ \ {0} (f′(x₀) = 1 if x₀ > 0, −1 if x₀ < 0).
**Why:**
If x₀ > 0: for small h, x₀ + h > 0, so (|x₀ + h| − |x₀|)/h = (x₀ + h − x₀)/h = h/h = 1 → f′(x₀) = 1.
If x₀ < 0: for small h, x₀ + h < 0, so (|x₀ + h| − |x₀|)/h = (−(x₀ + h) + x₀)/h = −h/h = −1 → f′(x₀) = −1.
If x₀ = 0: (|0 + h| − |0|)/h = |h|/h.
For h > 0: |h|/h = h/h = 1. For h < 0: |h|/h = −h/h = −1.
The quotient approaches 1 from the right and −1 from the left; these are different, so there is no single (unique) value: f′(0) is not defined (the graph has a sharp corner at 0).

c. f(x) = 1/x

**Answer:** All real numbers except 0, i.e. ℝ \ {0} (f′(x₀) = −1/x₀²).
**Why:**
f is not defined at x₀ = 0, so f′(0) cannot exist.
For x₀ ≠ 0: (f(x₀ + h) − f(x₀))/h = (1/(x₀ + h) − 1/x₀)/h.
Common denominator: 1/(x₀ + h) − 1/x₀ = (x₀ − (x₀ + h))/(x₀(x₀ + h)) = −h/(x₀(x₀ + h)).
Divide by h: −1/(x₀(x₀ + h)).
As h → 0 (from both sides): → −1/(x₀ · x₀) = −1/x₀².
So f′(x₀) exists and is unique for every x₀ ≠ 0.

From Activity 2.6, you have observed that there are functions that are differentiable at all numbers in their domains and there are also functions that are not differentiable at some numbers in their domain. We are now ready to define derivatives.

### Definition 2.7

The function f′ whose domain consists of those values of x at which f is differentiable and whose value at any such number as h gets closer and closer to zero is given by f′(x) = (f(x + h) − f(x))/h

Here, we represent the derivative of a function by a prime symbol. For example, writing f′(x) represents the derivative of the function f evaluated at a point x.

(p.83)

Similarly, writing (5x² + 2x + 3)′ indicates we are carrying out the derivative of the function 5x² + 2x + 3. The prime symbol disappears as soon as the derivative has been calculated. If we let t = x + h, as h gets closer and closer to zero, t approaches x and the definition above can be re-written as

f′(x) = (f(t) − f(x))/(t − x) as t gets very close to x.

### Note

The derivative is the exact rate at which one quantity changes with respect to another.

#### The different notations for the derivative

The following are some of the other notations for derivatives. If y = f(x), then f′(x) is denoted by either of the following notations: dy/dx, d/dx f(x), Df(x), D_x f

### Example

Find the derivative of the following functions.

a. f(x) = k, k be any constant  b. f(x) = x²  c. f(x) = √x

**Solution**

Use the definition and let h get closer and closer to 0.

Now, from f′(x) = (f(x + h) − f(x))/h, we obtain:

a. For f(x) = k, k be any constant, the quotient (f(x + h) − f(x))/h = (k − k)/h = 0.

Thus, by definition 2.6 f′(x) = 0 or d/dx (k) = 0.

[added step: f(x + h) = k because a constant function has the same value k at every input; 0/h = 0 for every h ≠ 0, so the limit is 0.]

(p.84)

b. When f(x) = x², the quotient difference

(f(x + h) − f(x))/h = ((x + h)² − x²)/h
= ((x² + 2xh + h²) − x²)/h
= (2xh + h²)/h = 2x + h.

As h gets closer and closer to 0, the quantity 2x + h gets closer to 2x. Therefore, by definition 2.6

f′(x) = 2x or d/dx (x²) = 2x.

[review: parts a and b of this Example on p.83–84 cite "definition 2.6" (derivative at a point) where the derivative-as-a-function is Definition 2.7 (which part c cites); the results are correct either way]

c. For f(x) = √x the quotient

(f(x + h) − f(x))/h = (√(x + h) − √x)/h, using rationalization
= ((√(x + h) − √x)/h) × ((√(x + h) + √x)/(√(x + h) + √x))
= (x + h − x)/(h(√(x + h) + √x)) = 1/(√(x + h) + √x)

As h tends to 0, this quantity approaches 1/(2√x).

Hence, by definition 2.7,

f′(x) = (√x)′ = 1/(2√x) or d/dx (√x) = 1/(2√x).

[added step: (√(x + h) − √x)(√(x + h) + √x) = (x + h) − x = h; cancel h; as h → 0, √(x + h) + √x → 2√x; valid for x > 0.]

### Exercise 2.7

Use definition 2.7, find the derivative of the function with respect to x.

a. f(x) = x

**Answer:** f′(x) = 1
**Why:**
f(x + h) = x + h.
f(x + h) − f(x) = x + h − x = h.
(f(x + h) − f(x))/h = h/h = 1 (h ≠ 0).
As h → 0 the quotient stays 1, so f′(x) = 1.
(Check: power rule n = 1: 1·x⁰ = 1. ✓)

b. f(x) = x³

**Answer:** f′(x) = 3x²
**Why:**
Expand: (x + h)³ = x³ + 3x²h + 3xh² + h³.
f(x + h) − f(x) = x³ + 3x²h + 3xh² + h³ − x³ = 3x²h + 3xh² + h³.
Factor h: h(3x² + 3xh + h²).
Divide by h (h ≠ 0): 3x² + 3xh + h².
As h → 0: 3xh → 0 and h² → 0, so the quotient → 3x².
f′(x) = 3x².
(Check: power rule n = 3: 3x². At x = 1 this gives 3, matching Activity 2.2. ✓)

c. f(x) = 1/x

**Answer:** f′(x) = −1/x² (x ≠ 0)
**Why:**
f(x + h) − f(x) = 1/(x + h) − 1/x.
Common denominator x(x + h): = (x − (x + h))/(x(x + h)) = −h/(x(x + h)).
Divide by h (h ≠ 0): −1/(x(x + h)).
As h → 0: x + h → x, so the quotient → −1/(x · x) = −1/x².
f′(x) = −1/x².
(Check: power rule with n = −1: (x^(−1))′ = −1·x^(−2) = −1/x². At x = 2: −1/4, matching Exercise 2.5 1d. ✓)

d. f(x) = 2√x

**Answer:** f′(x) = 1/√x (x > 0)
**Why:**
f(x + h) − f(x) = 2√(x + h) − 2√x = 2(√(x + h) − √x).
Quotient: 2(√(x + h) − √x)/h.
Rationalize: multiply top and bottom by (√(x + h) + √x).
Numerator: 2((x + h) − x) = 2h.
Quotient = 2h/(h(√(x + h) + √x)) = 2/(√(x + h) + √x) (h ≠ 0).
As h → 0: → 2/(√x + √x) = 2/(2√x) = 1/√x.
f′(x) = 1/√x.
(Check: constant multiple of part c of the Example: 2 × 1/(2√x) = 1/√x. ✓)

(p.85)

#### 2.1.4.3 Derivatives of various functions

**i. Differentiation of power functions**

### Activity 2.7

Using definition 2.7, find the derivative of each of the following power functions.

1. a. f(x) = x

   **Answer:** f′(x) = 1
   **Why:**
   (f(x + h) − f(x))/h = ((x + h) − x)/h = h/h = 1 (h ≠ 0).
   As h → 0 it stays 1, so f′(x) = 1.

   b. f(x) = x²

   **Answer:** f′(x) = 2x
   **Why:**
   (x + h)² = x² + 2xh + h².
   ((x + h)² − x²)/h = (2xh + h²)/h = h(2x + h)/h = 2x + h (h ≠ 0).
   As h → 0: 2x + h → 2x.
   f′(x) = 2x.

   c. f(x) = x^(−2).

   **Answer:** f′(x) = −2x^(−3) = −2/x³ (x ≠ 0)
   **Why:**
   f(x) = x^(−2) = 1/x².
   f(x + h) − f(x) = 1/(x + h)² − 1/x².
   Common denominator x²(x + h)²: = (x² − (x + h)²)/(x²(x + h)²).
   Expand: x² − (x² + 2xh + h²) = −2xh − h² = −h(2x + h).
   Divide by h (h ≠ 0): −(2x + h)/(x²(x + h)²).
   As h → 0: → −2x/(x² · x²) = −2x/x⁴ = −2/x³ = −2x^(−3).
   (Check: same expression as Activity 2.5 b; and n x^(n−1) with n = −2 gives −2x^(−3). ✓ Numerically at x = 1, h = 0.001: (1/1.002001 − 1)/0.001 ≈ −1.997, close to −2. ✓)

2. What is the derivative of f(x) = xⁿ?

   **Answer:** f′(x) = n x^(n−1)
   **Why:**
   Pattern from part 1: (x)′ = 1 = 1·x⁰, (x²)′ = 2x = 2·x¹, (x³)′ = 3x² (Exercise 2.7 b), (x^(−1))′ = −1·x^(−2) (Exercise 2.7 c), (x^(−2))′ = −2·x^(−3).
   In each case: bring the exponent down as a factor and reduce the exponent by 1.
   So (xⁿ)′ = n x^(n−1). This is proved for positive integers n in Theorem 2.1.

### Theorem 2.1

Let f(x) = xⁿ, where n is a positive integer. Then f′(x) = n x^(n−1).

**Proof**

Let f(x) = xⁿ. The quotient difference

(f(t) − f(x))/(t − x) = (tⁿ − xⁿ)/(t − x)
= ((t − x)(t^(n−1) + x t^(n−2) + … + t x^(n−2) + x^(n−1)))/(t − x)
= t^(n−1) + x t^(n−2) + … + t x^(n−2) + x^(n−1), t ≠ x

Thus, by definition of the derivatives as t gets very close to x

f′(x) = x^(n−1) + x^(n−1) + … + x^(n−1) + x^(n−1) (n-times) = n x^(n−1)

[added step: there are n terms in the bracket t^(n−1), x t^(n−2), x² t^(n−3), …, x^(n−1); when t is replaced by x, each term x^k t^(n−1−k) becomes x^(n−1), so the sum is n copies of x^(n−1).]

**Note**: By long division, we have

tⁿ − xⁿ = (t − x)(t^(n−1) + x t^(n−2) + x² t^(n−3) + … + x^(n−2) t + x^(n−1)).

i.e.,

(The page ends with "i.e.," — the text continues on book p.86, which is outside this batch.)

# Unit 2 Introduction to Calculus — Part B (book pp. 86–110)

## 2.1 (continued) — Rules of differentiation

### i. Derivative of a power function (continued)

(p.86)

[The page opens in the middle of the proof of Theorem 2.1 (power rule), begun on p.85 (outside this chunk). It shows the long division of tⁿ − xⁿ by t − x:]

```
                t^(n−1) + x t^(n−2) + x² t^(n−3) + … + x^(n−2) t + x^(n−1)
       t − x ) tⁿ                                              − xⁿ
              −(tⁿ − x t^(n−1))
               ─────────────────
                    x t^(n−1) − xⁿ
                  −(x t^(n−1) − x² t^(n−2))
                   ─────────────────────────
                          x² t^(n−2) − xⁿ
                        −(x² t^(n−2) − x³ t^(n−3))
                         ──────────────────────────
                                  ⋮
                                  x^(n−1) t − xⁿ
                                −(x^(n−1) t − xⁿ)
                                 ─────────────────
                                         0
```

So (tⁿ − xⁿ)/(t − x) = t^(n−1) + x t^(n−2) + x² t^(n−3) + … + x^(n−2) t + x^(n−1). [added step: letting t → x, each of the n terms tends to x^(n−1), so f′(x) = lim_{t→x} (tⁿ − xⁿ)/(t − x) = n x^(n−1).]

### Example 1

Find the derivatives of each of the following functions.

a. f(x) = x¹⁵   b. f(x) = x²⁴

**Solution**

a. f′(x) = 15x^(15−1) = 15x¹⁴   b. f′(x) = 24x^(24−1) = 24x²³

### Corollary 2.1

If f(x) = x^(−n), where n is a positive integer, then f′(x) = −n x^(−(n+1)).

### Example 2

Find the derivatives of each of the following functions.

a. f(x) = x⁻⁵   b. f(x) = x⁻¹⁷

**Solution**

a. f′(x) = −5x^(−5−1) = −5x⁻⁶   b. f′(x) = −17x^(−17−1) = −17x⁻¹⁸

(p.87)

### Example 3

Let f(x) = x⁻⁶, find

a. f′(1)   b. f′(1/3)   c. f′(k), k ≠ 0.

**Solution**

f′(x) = −6x⁻⁷ ⇒ a) f′(1) = −6(1)⁻⁷ = −6

b) f′(1/3) = −6(1/3)⁻⁷ = −6(3)⁷ = −13,122 [added step: 3⁷ = 2187, and −6 × 2187 = −13,122]

c) f′(k) = −6(k)⁻⁷ = −6k⁻⁷

### Corollary 2.2

Let f(x) = kxⁿ, then f′(x) = knx^(n−1), where n is any non-zero integer and k is a constant number.

### Example 4

Find the derivative of each of the following functions.

a. f(x) = −2x¹¹   b. f(x) = 4x²⁰   c. f(x) = −3/x⁷   d. f(x) = 1/(3x¹⁵)

**Solution**

Using corollary 2.2, we obtain

a. f′(x) = −2(11)x¹⁰ = −22x¹⁰

b. f′(x) = 4(20)x¹⁹ = 80x¹⁹

c. [added step: f(x) = −3x⁻⁷] f′(x) = −3(−7)x⁻⁸ = 21x⁻⁸ = 21/x⁸

d. [added step: f(x) = (1/3)x⁻¹⁵] f′(x) = (1/3)(−15)x⁻¹⁶ = −5/x¹⁶

(p.88)

### Exercise 2.8

1. Find the derivative of each of the following functions.

a. f(x) = x⁸

**Answer:** f′(x) = 8x⁷
**Why:**
Power rule: d/dx xⁿ = n x^(n−1) with n = 8.
f′(x) = 8x^(8−1) = 8x⁷.

b. f(x) = x²⁷

**Answer:** f′(x) = 27x²⁶
**Why:**
Power rule with n = 27.
f′(x) = 27x^(27−1) = 27x²⁶.

c. f(x) = 2x⁶

**Answer:** f′(x) = 12x⁵
**Why:**
Constant multiple rule (Corollary 2.2): d/dx (kxⁿ) = knx^(n−1), k = 2, n = 6.
f′(x) = 2(6)x^(6−1) = 12x⁵.

d. f(x) = 10x¹⁵

**Answer:** f′(x) = 150x¹⁴
**Why:**
Constant multiple rule with k = 10, n = 15.
f′(x) = 10(15)x^(15−1) = 150x¹⁴.

e. f(x) = 4x⁻⁷

**Answer:** f′(x) = −28x⁻⁸ = −28/x⁸
**Why:**
Constant multiple rule with k = 4, n = −7.
f′(x) = 4(−7)x^(−7−1) = −28x⁻⁸.
Write with a positive exponent: −28/x⁸.

f. f(x) = 3x⁻²⁰

**Answer:** f′(x) = −60x⁻²¹ = −60/x²¹
**Why:**
Constant multiple rule with k = 3, n = −20.
f′(x) = 3(−20)x^(−20−1) = −60x⁻²¹ = −60/x²¹.

g. f(x) = 4x^(−3/2)

**Answer:** f′(x) = −6x^(−5/2) = −6/(x²√x), x > 0
**Why:**
The power rule also holds for rational exponents (the exponent here is not an integer, so this goes beyond Corollary 2.2 as stated; it is justified later in the unit by the rule for rational powers).
Constant multiple rule with k = 4, n = −3/2.
n − 1 = −3/2 − 2/2 = −5/2.
f′(x) = 4(−3/2)x^(−5/2) = −6x^(−5/2).
x^(−5/2) = 1/x^(5/2) = 1/(x²√x), so f′(x) = −6/(x²√x).

h. f(x) = −10x^(−2/5)

**Answer:** f′(x) = 4x^(−7/5)
**Why:**
Constant multiple rule with k = −10, n = −2/5.
n − 1 = −2/5 − 5/5 = −7/5.
f′(x) = −10(−2/5)x^(−7/5) = (20/5)x^(−7/5) = 4x^(−7/5).
Check numerically at x = 1: (f(1.001) − f(0.999))/0.002 ≈ 4.000, and 4(1)^(−7/5) = 4. Agrees.

[review: Exercise 2.8 items g and h use rational exponents (−3/2, −2/5), but Corollary 2.2 is stated only for non-zero integers n. The answers use the general power rule for rational exponents.]

2. Let f(x) = x⁻⁹, find

First: f′(x) = −9x^(−9−1) = −9x⁻¹⁰ (Corollary 2.1 with n = 9).

a. f′(1)

**Answer:** f′(1) = −9
**Why:**
f′(x) = −9x⁻¹⁰ (power rule).
f′(1) = −9(1)⁻¹⁰ = −9(1) = −9.

b. f′(1/3)

**Answer:** f′(1/3) = −531,441
**Why:**
f′(1/3) = −9(1/3)⁻¹⁰.
(1/3)⁻¹⁰ = 3¹⁰ = 59,049.
f′(1/3) = −9 × 59,049 = −531,441 (= −3¹²).

c. f′(k) = k, k ≠ 0.

**Answer:** f′(k) = −9k⁻¹⁰ = −9/k¹⁰
**Why:**
Substitute x = k in f′(x) = −9x⁻¹⁰: f′(k) = −9k⁻¹⁰ = −9/k¹⁰ (k ≠ 0 so that k⁻¹⁰ is defined).
[review: the book prints "c. f′(k) = k, k ≠ 0." This is almost certainly a typo for "f′(k), k ≠ 0" (compare Example 3c). Read literally, −9/k¹⁰ = k would mean k¹¹ = −9, k = −9^(1/11) ≈ −1.221; the answer above follows the Example 3 pattern.]

3. Based on Theorem 2.1, show the proof of corollary 2.1 and corollary 2.2.

**Answer:** If f(x) = x^(−n) (n a positive integer) then f′(x) = −n x^(−n−1); and if f(x) = kxⁿ then f′(x) = knx^(n−1).
**Why (Corollary 2.1):**
Let f(x) = x^(−n) = 1/xⁿ, x ≠ 0, n a positive integer.
Definition: f′(x) = lim_{h→0} (f(x+h) − f(x))/h = lim_{h→0} (1/(x+h)ⁿ − 1/xⁿ)/h.
Common denominator: 1/(x+h)ⁿ − 1/xⁿ = (xⁿ − (x+h)ⁿ)/(xⁿ(x+h)ⁿ).
So f′(x) = lim_{h→0} [−((x+h)ⁿ − xⁿ)/h] × 1/(xⁿ(x+h)ⁿ).
By Theorem 2.1, lim_{h→0} ((x+h)ⁿ − xⁿ)/h = d/dx (xⁿ) = n x^(n−1).
And lim_{h→0} 1/(xⁿ(x+h)ⁿ) = 1/(xⁿ · xⁿ) = 1/x^(2n).
So f′(x) = −n x^(n−1) · x^(−2n) = −n x^(n−1−2n) = −n x^(−n−1) = −n x^(−(n+1)).
**Why (Corollary 2.2):**
Let f(x) = kxⁿ.
f′(x) = lim_{h→0} (k(x+h)ⁿ − kxⁿ)/h = lim_{h→0} k · ((x+h)ⁿ − xⁿ)/h.
A constant factor comes out of the limit: = k · lim_{h→0} ((x+h)ⁿ − xⁿ)/h.
For n a positive integer, by Theorem 2.1 this limit is n x^(n−1); for n a negative integer, by Corollary 2.1 it is also n x^(n−1).
So f′(x) = knx^(n−1).

### ii. Derivatives of combinations of functions

#### a. Derivatives of a sum and difference of a functions

### Activity 2.8

Given the functions f(x) = x², and g(x) = x³ + 2x, then find

First: f′(x) = 2x (power rule); g′(x) = 3x² + 2 (power rule on x³, constant multiple rule on 2x).

a. f′(x) + g′(x)

**Answer:** 3x² + 2x + 2
**Why:**
f′(x) = 2x.
g′(x) = 3x² + 2.
f′(x) + g′(x) = 2x + 3x² + 2 = 3x² + 2x + 2.

b. (f + g)′(x)

**Answer:** 3x² + 2x + 2
**Why:**
(f + g)(x) = x² + x³ + 2x = x³ + x² + 2x.
Differentiate term by term with the power rule: (f + g)′(x) = 3x² + 2x + 2.
This equals the answer to (a).

c. f′(x) − g′(x)

**Answer:** −3x² + 2x − 2
**Why:**
f′(x) − g′(x) = 2x − (3x² + 2) = 2x − 3x² − 2 = −3x² + 2x − 2.

d. (f − g)′(x)

**Answer:** −3x² + 2x − 2
**Why:**
(f − g)(x) = x² − (x³ + 2x) = −x³ + x² − 2x.
(f − g)′(x) = −3x² + 2x − 2.
This equals the answer to (c), which leads to Theorem 2.2.

### Theorem 2.2

If f and g are differentiable functions at a, then f + g and f − g are also differentiable at a and are given by (f + g)′(a) = f′(a) + g′(a), and (f − g)′(a) = f′(a) − g′(a)

(p.89)

**Proof**

From the definition of derivative, we have:

((f + g)(x) − (f + g)(a))/(x − a) = (f(x) + g(x) − f(a) − g(a))/(x − a)
= (f(x) − f(a) + g(x) − g(a))/(x − a)
= (f(x) − f(a))/(x − a) + (g(x) − g(a))/(x − a)   (i)

By definition of derivatives, as x gets close to a,

((f + g)(x) − (f + g)(a))/(x − a) = (f + g)′(a),

(f(x) − f(a))/(x − a) = f′(a) and (g(x) − g(a))/(x − a) = g′(a)   (ii)

From Eq. (i) and Eq. (ii), we obtain

(f + g)′(a) = f′(a) + g′(a).

This theorem, implies for all x at which both f and g are differentiable,

(f + g)′(x) = f′(x) + g′(x).

### Corollary 2.3

If f₁, f₂, f₃, …, fₙ are differentiable at a number a, then

(f₁ + f₂ + f₃ + … + fₙ)′(a) = f₁′(a) + f₂′(a) + f₃′(a) + … + fₙ′(a) and

(f₁ − f₂ − f₃ − … − fₙ)′(a) = f₁′(a) − f₂′(a) − f₃′(a) − … − fₙ′(a)

### Example 1

If f(x) = x³ + 3x², find a formula for f′(x) and compute f′(2).

**Solution**

f′(x) = 3x² + 6x ⇒ f′(2) = 3 × 2² + 6 × 2 = 24. [added step: 3 × 4 + 12 = 12 + 12 = 24]

(p.90)

### Example 2

Find the derivative of the function f(x) = 3x⁴ − 2x³ + 10x + √x + 1/√x

**Solution**

[added step: write √x = x^(1/2) and 1/√x = x^(−1/2); then d/dx x^(1/2) = (1/2)x^(−1/2) = 1/(2√x) and d/dx x^(−1/2) = −(1/2)x^(−3/2) = −1/(2x√x).]

f′(x) = 12x³ − 6x² + 10 + 1/(2√x) − 1/(2x√x)

### Exercise 2.9

1. If f(x) = x⁴ − 3x² + 2, find a formula for f′(x) and compute f′(3).

**Answer:** f′(x) = 4x³ − 6x; f′(3) = 90
**Why:**
Sum/difference rule (Theorem 2.2, Corollary 2.3): differentiate term by term.
d/dx x⁴ = 4x³ (power rule).
d/dx (3x²) = 3(2x) = 6x (constant multiple rule).
d/dx 2 = 0 (derivative of a constant).
f′(x) = 4x³ − 6x + 0 = 4x³ − 6x.
f′(3) = 4(3)³ − 6(3) = 4(27) − 18 = 108 − 18 = 90.

2. Find the derivative of each of the following functions.

a. f(x) = 5x⁴ + √x

**Answer:** f′(x) = 20x³ + 1/(2√x)
**Why:**
Rewrite √x = x^(1/2).
Sum rule: f′(x) = d/dx(5x⁴) + d/dx(x^(1/2)).
Constant multiple + power rule: d/dx(5x⁴) = 5(4x³) = 20x³.
Power rule: d/dx x^(1/2) = (1/2)x^(1/2 − 1) = (1/2)x^(−1/2) = 1/(2√x).
f′(x) = 20x³ + 1/(2√x).

b. f(x) = x + 1/x²

**Answer:** f′(x) = 1 − 2/x³
**Why:**
Rewrite 1/x² = x⁻².
Sum rule: f′(x) = d/dx(x) + d/dx(x⁻²).
Power rule: d/dx x = 1.
Power rule (Corollary 2.1): d/dx x⁻² = −2x⁻³ = −2/x³.
f′(x) = 1 − 2/x³.

c. f(x) = (1/6)x⁶ − 2x − 4

**Answer:** f′(x) = x⁵ − 2
**Why:**
Sum/difference rule, term by term.
Constant multiple + power rule: d/dx((1/6)x⁶) = (1/6)(6x⁵) = x⁵.
d/dx(2x) = 2.
d/dx(4) = 0.
f′(x) = x⁵ − 2 − 0 = x⁵ − 2.

d. f(x) = √x − 1/√x

**Answer:** f′(x) = 1/(2√x) + 1/(2x√x)
**Why:**
Rewrite: f(x) = x^(1/2) − x^(−1/2).
Difference rule, then power rule on each term.
d/dx x^(1/2) = (1/2)x^(−1/2) = 1/(2√x).
d/dx x^(−1/2) = (−1/2)x^(−1/2 − 1) = −(1/2)x^(−3/2) = −1/(2x√x).
f′(x) = 1/(2√x) − (−1/(2x√x)) = 1/(2√x) + 1/(2x√x).
(Equivalent form: (x + 1)/(2x√x).)

e. f(x) = x¹⁰ + 1/x + 6x^(5/3)

**Answer:** f′(x) = 10x⁹ − 1/x² + 10x^(2/3)
**Why:**
Rewrite 1/x = x⁻¹.
Sum rule, term by term.
Power rule: d/dx x¹⁰ = 10x⁹.
Power rule: d/dx x⁻¹ = −1x⁻² = −1/x².
Constant multiple + power rule: d/dx(6x^(5/3)) = 6 · (5/3)x^(5/3 − 1) = 10x^(2/3).
f′(x) = 10x⁹ − 1/x² + 10x^(2/3).

f. f(x) = 6x^(4/3) − 1/(3x³) − (1/2)x²

**Answer:** f′(x) = 8x^(1/3) + 1/x⁴ − x
**Why:**
Rewrite 1/(3x³) = (1/3)x⁻³.
Difference rule, term by term.
Constant multiple + power rule: d/dx(6x^(4/3)) = 6 · (4/3)x^(4/3 − 1) = 8x^(1/3).
Constant multiple + power rule: d/dx((1/3)x⁻³) = (1/3)(−3)x⁻⁴ = −x⁻⁴.
Constant multiple + power rule: d/dx((1/2)x²) = (1/2)(2x) = x.
f′(x) = 8x^(1/3) − (−x⁻⁴) − x = 8x^(1/3) + 1/x⁴ − x.

3. Based on the proof of the sum rule of derivative, show the proof of the difference rule.

**Answer:** (f − g)′(a) = f′(a) − g′(a).
**Why:**
((f − g)(x) − (f − g)(a))/(x − a) = (f(x) − g(x) − f(a) + g(a))/(x − a).
Regroup: = (f(x) − f(a) − (g(x) − g(a)))/(x − a).
Split the fraction: = (f(x) − f(a))/(x − a) − (g(x) − g(a))/(x − a).   (i)
As x → a, (f(x) − f(a))/(x − a) → f′(a) and (g(x) − g(a))/(x − a) → g′(a) (f, g differentiable at a).   (ii)
The limit of a difference is the difference of the limits, so from (i) and (ii), (f − g)′(a) = f′(a) − g′(a).

#### b. Derivative of a constant multiple of a function

### Activity 2.9

Given the function f(x) = x², find a. (3f)′(x)   b. 3(f′(x))

a. (3f)′(x)

**Answer:** 6x
**Why:**
(3f)(x) = 3x².
Power rule on x² gives 2x, so (3f)′(x) = 3 · 2x = 6x. [using the definition: lim_{h→0} (3(x+h)² − 3x²)/h = lim_{h→0} (6xh + 3h²)/h = lim_{h→0} (6x + 3h) = 6x]

b. 3(f′(x))

**Answer:** 6x
**Why:**
f′(x) = 2x (power rule).
3(f′(x)) = 3(2x) = 6x.
Same as (a): this leads to Theorem 2.3.

### Theorem 2.3

If f is differentiable at a, then for any constant number k, the function kf is differentiable at a and (kf)′(a) = k(f′(a)).

**Proof**

By definition of the derivative as x → a,

(kf)′(a) = ((kf)(x) − (kf)(a))/(x − a) = k[f(x) − f(a)]/(x − a) = k [f(x) − f(a)]/(x − a) = kf′(a).

Thus, for all x at which f is differentiable,

(kf)′(x) = kf′(x).

(p.91)

### Example 1

Let f(x) = 6√x, find the formula for f′(x) and compute f′(4).

**Solution**

f′(x) = (6√x)′ = 6/(2√x) = 3/√x and f′(4) = 3/√4 = 3/2.

**Derivative of polynomial functions**

If f(x) = aₙxⁿ + aₙ₋₁x^(n−1) + aₙ₋₂x^(n−2) + … + a₁x + a₀, then

f′(x) = naₙx^(n−1) + (n − 1)aₙ₋₁x^(n−2) + (n − 2)aₙ₋₂x^(n−3) + … + a₁.

### Example 2

Given y = 3x⁸ − √2x⁵ + (3/2)x³ + 20x + 1, compute dy/dx|_{x=−1}.

**Solution**

Using differentiation rule

d/dx (3x⁸ − √2x⁵ + (3/2)x³ + 20x + 1) = 24x⁷ − 5√2x⁴ + (9/2)x² + 20

Then, we evaluate the derivative at x = −1.

dy/dx|_{x=−1} = −24 − 5√2 + 9/2 + 20 = 1/2 − 5√2.

[added step: (−1)⁷ = −1, (−1)⁴ = 1, (−1)² = 1; −24 + 9/2 + 20 = −4 + 9/2 = 1/2]

**Note:** dy/dx|_{x=−1} means value obtained by substituting x = −1 into dy/dx.

### Exercise 2.10

1. Find the derivatives of the following functions.

a. f(x) = (1/10)x¹⁰

**Answer:** f′(x) = x⁹
**Why:**
Constant multiple rule (Theorem 2.3) with power rule: f′(x) = (1/10)(10x⁹) = x⁹.

b. f(x) = 3x^(4/3)

**Answer:** f′(x) = 4x^(1/3) (= 4∛x)
**Why:**
Constant multiple rule with power rule, n = 4/3.
n − 1 = 4/3 − 3/3 = 1/3.
f′(x) = 3 · (4/3)x^(1/3) = 4x^(1/3).

c. f(x) = √3 x³

**Answer:** f′(x) = 3√3 x²
**Why:**
√3 is a constant (the radical covers only the 3).
Constant multiple rule with power rule: f′(x) = √3 · 3x² = 3√3 x².

d. f(x) = x⁴ − 2x³ + 3x − 2

**Answer:** f′(x) = 4x³ − 6x² + 3
**Why:**
Sum/difference rule, term by term (polynomial rule).
d/dx x⁴ = 4x³ (power rule).
d/dx(2x³) = 2(3x²) = 6x² (constant multiple rule).
d/dx(3x) = 3.
d/dx(2) = 0.
f′(x) = 4x³ − 6x² + 3.

(p.92)

2. Find the derivatives of the following functions, and compute the indicated values.

a. y = 2√x, evaluate dy/dx|_{x=1} and dy/dx|_{x=4}.

**Answer:** dy/dx = 1/√x; dy/dx|_{x=1} = 1; dy/dx|_{x=4} = 1/2
**Why:**
y = 2x^(1/2).
Constant multiple + power rule: dy/dx = 2 · (1/2)x^(−1/2) = x^(−1/2) = 1/√x.
At x = 1: 1/√1 = 1.
At x = 4: 1/√4 = 1/2.

b. y = 9/x³, evaluate dy/dx|_{x=−1} and dy/dx|_{x=3}.

**Answer:** dy/dx = −27/x⁴; dy/dx|_{x=−1} = −27; dy/dx|_{x=3} = −1/3
**Why:**
y = 9x⁻³.
Constant multiple + power rule: dy/dx = 9(−3)x⁻⁴ = −27x⁻⁴ = −27/x⁴.
At x = −1: (−1)⁴ = 1, so dy/dx = −27/1 = −27.
At x = 3: 3⁴ = 81, so dy/dx = −27/81 = −1/3.

c. y = x³ + (1/2)x² − 2/√x, evaluate dy/dx|_{x=1} and dy/dx|_{x=4}.

**Answer:** dy/dx = 3x² + x + 1/(x√x); dy/dx|_{x=1} = 5; dy/dx|_{x=4} = 417/8 (= 52 1/8)
**Why:**
Rewrite 2/√x = 2x^(−1/2).
Sum/difference rule, term by term.
d/dx x³ = 3x² (power rule).
d/dx((1/2)x²) = (1/2)(2x) = x (constant multiple rule).
d/dx(2x^(−1/2)) = 2(−1/2)x^(−3/2) = −x^(−3/2).
dy/dx = 3x² + x − (−x^(−3/2)) = 3x² + x + x^(−3/2) = 3x² + x + 1/(x√x).
At x = 1: 3(1) + 1 + 1/(1·1) = 3 + 1 + 1 = 5.
At x = 4: 3(16) + 4 + 1/(4 · 2) = 48 + 4 + 1/8 = 52 1/8 = 417/8.

#### c. Derivative of a product

### Activity 2.10

Given the functions f(x) = x², and g(x) = x, find

a. (fg)′(x)

**Answer:** 3x²
**Why:**
(fg)(x) = x² · x = x³.
Power rule: (fg)′(x) = 3x².

b. f′(x)g(x) + f(x)g′(x)

**Answer:** 3x²
**Why:**
f′(x) = 2x, g′(x) = 1 (power rule).
f′(x)g(x) + f(x)g′(x) = (2x)(x) + (x²)(1) = 2x² + x² = 3x².
Same as (a). Note that f′(x)g′(x) = 2x · 1 = 2x is NOT equal to (fg)′(x) — this leads to Theorem 2.4.

### Theorem 2.4

If f and g are differentiable at a, then fg is also differentiable at a, and (fg)′(a) = f′(a)g(a) + f(a)g′(a).

**Proof**

By definition of the derivative as x gets very close to a,

((fg)(x) − (fg)(a))/(x − a) = (fg)′(a).   (i)

and

((fg)(x) − (fg)(a))/(x − a) = (f(x)g(x) − f(a)g(a))/(x − a)
= (f(x)g(x) − f(a)g(x) + f(a)g(x) − f(a)g(a))/(x − a)
= (g(x)(f(x) − f(a)) + f(a)(g(x) − g(a)))/(x − a)
= g(x)(f(x) − f(a))/(x − a) + f(a)(g(x) − g(a))/(x − a)
= g(x) (f(x) − f(a))/(x − a) + f(a) (g(x) − g(a))/(x − a)

(p.93)

As x → a, the expression (f(x) − f(a))/(x − a) = f′(a) and (g(x) − g(a))/(x − a) = g′(a). Thus,

(fg)′(a) = f′(a)g(a) + f(a)g′(a).

[added step: g(x) → g(a) as x → a, because a function differentiable at a is continuous at a.]

From this theorem, we generalize that, for all x at which both f and g are differentiable

(fg)′(x) = f′(x)g(x) + f(x)g′(x).

### Example

1. Find the derivative of the following functions.

a. g(x) = (x + 6)(x² + 4)   b. f(x) = x²(√x + 2x)

**Solution**

a. Using product property,

g′(x) = (x + 6)′(x² + 4) + (x + 6)(x² + 4)′ = (x² + 4) + 2x(x + 6) = 3x² + 12x + 4.

[added step: (x² + 4) + 2x² + 12x = 3x² + 12x + 4]

b. Using product property,

f′(x) = (x²)′(√x + 2x) + x²(√x + 2x)′
= 2x(√x + 2x) + x²(1/(2√x) + 2)
= 2x√x + 4x² + x²/(2√x) + 2x²
= 6x² + 5x√x/2

[added step: x²/(2√x) = x√x/2 (since x² = x·√x·√x), and 2x√x + x√x/2 = (4/2 + 1/2)x√x = 5x√x/2; 4x² + 2x² = 6x²]

### Exercise 2.11

Find f′(x) of the following functions using product rule.

a. f(x) = (2x + 1)(x² + x − 5)

**Answer:** f′(x) = 6x² + 6x − 9
**Why:**
Let u = 2x + 1, v = x² + x − 5.
u′ = 2; v′ = 2x + 1 (sum and power rules).
Product rule: f′(x) = u′v + uv′ = 2(x² + x − 5) + (2x + 1)(2x + 1).
2(x² + x − 5) = 2x² + 2x − 10.
(2x + 1)(2x + 1) = 4x² + 4x + 1.
f′(x) = 2x² + 2x − 10 + 4x² + 4x + 1 = 6x² + 6x − 9.
Check by expanding first: f(x) = 2x³ + 2x² − 10x + x² + x − 5 = 2x³ + 3x² − 9x − 5, so f′(x) = 6x² + 6x − 9. Agrees.

b. f(x) = (x² − 2)(x³ + 4x)

**Answer:** f′(x) = 5x⁴ + 6x² − 8
**Why:**
Let u = x² − 2, v = x³ + 4x.
u′ = 2x; v′ = 3x² + 4.
Product rule: f′(x) = u′v + uv′ = 2x(x³ + 4x) + (x² − 2)(3x² + 4).
2x(x³ + 4x) = 2x⁴ + 8x².
(x² − 2)(3x² + 4) = 3x⁴ + 4x² − 6x² − 8 = 3x⁴ − 2x² − 8.
f′(x) = 2x⁴ + 8x² + 3x⁴ − 2x² − 8 = 5x⁴ + 6x² − 8.
Check by expanding first: f(x) = x⁵ + 4x³ − 2x³ − 8x = x⁵ + 2x³ − 8x, so f′(x) = 5x⁴ + 6x² − 8. Agrees.

c. f(x) = x(x² + √x)

**Answer:** f′(x) = 3x² + (3/2)√x
**Why:**
Let u = x, v = x² + √x = x² + x^(1/2).
u′ = 1; v′ = 2x + 1/(2√x) (power rule).
Product rule: f′(x) = u′v + uv′ = 1·(x² + √x) + x(2x + 1/(2√x)).
x(2x + 1/(2√x)) = 2x² + x/(2√x) = 2x² + √x/2.
f′(x) = x² + √x + 2x² + √x/2 = 3x² + (3/2)√x.
Check by expanding first: f(x) = x³ + x^(3/2), so f′(x) = 3x² + (3/2)x^(1/2). Agrees.

d. f(x) = (x + 2√x)(x² − 2)

**Answer:** f′(x) = 3x² + 5x√x − 2 − 2/√x
**Why:**
Let u = x + 2√x = x + 2x^(1/2), v = x² − 2.
u′ = 1 + 2 · (1/2)x^(−1/2) = 1 + 1/√x; v′ = 2x.
Product rule: f′(x) = u′v + uv′ = (1 + 1/√x)(x² − 2) + (x + 2√x)(2x).
(1 + 1/√x)(x² − 2) = x² − 2 + x²/√x − 2/√x = x² − 2 + x√x − 2/√x.
(x + 2√x)(2x) = 2x² + 4x√x.
f′(x) = x² − 2 + x√x − 2/√x + 2x² + 4x√x = 3x² + 5x√x − 2 − 2/√x.
Check by expanding first: f(x) = x³ − 2x + 2x^(5/2) − 4x^(1/2), so f′(x) = 3x² − 2 + 5x^(3/2) − 2x^(−1/2). Agrees.

(p.94)

#### d. Derivative of a quotient

### Theorem 2.5

If f and g are differentiable at a, and g(a) ≠ 0, then 1/g, f/g are differentiable at a and

i. (1/g)′(a) = ((1)′g(a) − 1(g′(a)))/(g(a))² = −g′(a)/(g(a))²

ii. (f/g)′(a) = (f′(a)g(a) − f(a)g′(a))/(g(a))².

**Proof**

i. By definition of derivative as x gets very close to a,

(1/g(x) − 1/g(a))/(x − a) = (1/g)′(a)

And (1/g)′(a) = (1/g(x) − 1/g(a))/(x − a) = (g(a) − g(x))/((x − a)g(x)g(a)) = −(g(x) − g(a))/(x − a) · 1/(g(x)g(a))

As x → a, the quantity (g(x) − g(a))/(x − a) = g′(a)

Thus (1/g)′(a) = −g′(a)/(g(a))²

[added step: as x → a, g(x) → g(a) (g is continuous at a), so 1/(g(x)g(a)) → 1/(g(a))².]

ii. (f/g)′(a) = (f · 1/g)′(a)

Using product rule (f · 1/g)′(a) = f′(a)(1/g)(a) + f(a)(1/g)′(a)
= f′(a) · 1/g(a) + f(a)(−g′(a)/(g(a))²)
= (f′(a)g(a) − f(a)g′(a))/(g(a))²

[added step: common denominator (g(a))²: f′(a)/g(a) = f′(a)g(a)/(g(a))²]

From this theorem, we see that, for all x at which both f and g are differentiable

(f/g)′(x) = (f′(x)g(x) − f(x)g′(x))/(g(x))².

(p.95)

### Example

Find f′(x)   a. f(x) = 1/(x² + 3x − 1)   b. f(x) = 8x⁵/(x³ + 2x)

**Solution**

Using quotient rule

a. f′(x) = −(x² + 3x − 1)′/(x² + 3x − 1)² = −(2x + 3)/(x² + 3x − 1)²

b. f′(x) = ((8x⁵)′(x³ + 2x) − 8x⁵(x³ + 2x)′)/(x³ + 2x)²
= ((40x⁴)(x³ + 2x) − 8x⁵(3x² + 2))/(x³ + 2x)² = (40x⁷ + 80x⁵ − 24x⁷ − 16x⁵)/(x³ + 2x)²
= (16x⁷ + 64x⁵)/(x³ + 2x)².

[added step: 40x⁷ − 24x⁷ = 16x⁷ and 80x⁵ − 16x⁵ = 64x⁵. (The printed middle line has a stray closing bracket after 16x⁵; it does not change the result.) Optional further simplification: (16x⁷ + 64x⁵)/(x²(x² + 2))² = 16x³(x² + 4)/(x² + 2)², x ≠ 0.]

### Exercise 2.12

Find the derivative of each of the following functions.

a. f(x) = 1/(x² + 1)

**Answer:** f′(x) = −2x/(x² + 1)²
**Why:**
Reciprocal form of the quotient rule (Theorem 2.5 i): (1/g)′ = −g′/g², with g(x) = x² + 1.
g′(x) = 2x (power rule; derivative of 1 is 0).
f′(x) = −2x/(x² + 1)².
Numerical check at x = 1: (f(1.001) − f(0.999))/0.002 ≈ −0.5000; formula gives −2/4 = −0.5. Agrees.

b. f(x) = (2x³ + 3)/(x − 5)

**Answer:** f′(x) = (4x³ − 30x² − 3)/(x − 5)²
**Why:**
Quotient rule: (f/g)′ = (f′g − fg′)/g², with numerator u = 2x³ + 3, denominator v = x − 5.
u′ = 6x² (constant multiple and power rule); v′ = 1.
f′(x) = (6x²(x − 5) − (2x³ + 3)(1))/(x − 5)².
6x²(x − 5) = 6x³ − 30x².
6x³ − 30x² − 2x³ − 3 = 4x³ − 30x² − 3.
f′(x) = (4x³ − 30x² − 3)/(x − 5)².

c. f(x) = (x³ + 3x)/x²

**Answer:** f′(x) = 1 − 3/x² = (x² − 3)/x²
**Why:**
Quotient rule with u = x³ + 3x, v = x².
u′ = 3x² + 3; v′ = 2x.
f′(x) = ((3x² + 3)(x²) − (x³ + 3x)(2x))/(x²)².
(3x² + 3)x² = 3x⁴ + 3x².
(x³ + 3x)(2x) = 2x⁴ + 6x².
Numerator: 3x⁴ + 3x² − 2x⁴ − 6x² = x⁴ − 3x².
f′(x) = (x⁴ − 3x²)/x⁴ = (x² − 3)/x² = 1 − 3/x².
Check by simplifying first: f(x) = x + 3x⁻¹, so f′(x) = 1 − 3x⁻². Agrees.

d. f(x) = 2x⁴/√x

**Answer:** f′(x) = 7x^(5/2) = 7x²√x
**Why:**
Quotient rule with u = 2x⁴, v = √x = x^(1/2).
u′ = 8x³; v′ = 1/(2√x).
f′(x) = (8x³ · √x − 2x⁴ · 1/(2√x))/(√x)².
2x⁴ · 1/(2√x) = x⁴/√x = x³√x.
Numerator: 8x³√x − x³√x = 7x³√x.
Denominator: (√x)² = x.
f′(x) = 7x³√x/x = 7x²√x = 7x^(5/2).
Check by simplifying first: f(x) = 2x^(4 − 1/2) = 2x^(7/2), so f′(x) = 2 · (7/2)x^(5/2) = 7x^(5/2). Agrees.

### 2.1.4.4 The chain rule

### Activity 2.11

1. Let f(x) = 2x + 3 and g(x) = x² − 1. Find each of the following functions.

a. f′(x)

**Answer:** f′(x) = 2
**Why:**
d/dx(2x) = 2 (constant multiple rule), d/dx(3) = 0; sum rule gives f′(x) = 2.

b. f′(g(x))

**Answer:** f′(g(x)) = 2
**Why:**
f′ is the constant function 2, so f′ evaluated at g(x) is still 2.

c. f(g(x))

**Answer:** f(g(x)) = 2x² + 1
**Why:**
Substitute g(x) for x in f: f(g(x)) = 2(x² − 1) + 3.
2(x² − 1) + 3 = 2x² − 2 + 3 = 2x² + 1.

d. f′(g(x)) · g′(x)

**Answer:** 4x
**Why:**
g′(x) = 2x (power rule; derivative of −1 is 0).
f′(g(x)) · g′(x) = 2 · 2x = 4x.
Note: d/dx f(g(x)) = d/dx(2x² + 1) = 4x, the same — this leads to the chain rule (Theorem 2.6).

2. Find the derivatives of the following functions.

a. f(x) = (3x² + 2)²

**Answer:** f′(x) = 12x(3x² + 2) = 36x³ + 24x
**Why:**
Outer function u², inner function u = 3x² + 2.
Chain rule: f′(x) = 2(3x² + 2) · (3x² + 2)′.
(3x² + 2)′ = 6x.
f′(x) = 2(3x² + 2)(6x) = 12x(3x² + 2) = 36x³ + 24x.
Check by expanding first: f(x) = 9x⁴ + 12x² + 4, so f′(x) = 36x³ + 24x. Agrees.

b. f(x) = (√(x³) + 2x − 7)³

**Answer:** f′(x) = 3(√(x³) + 2x − 7)² ((3/2)√x + 2)
**Why:**
Outer function u³, inner function u = √(x³) + 2x − 7 = x^(3/2) + 2x − 7.
u′ = (3/2)x^(1/2) + 2 = (3/2)√x + 2 (power rule, constant multiple rule, sum rule).
Chain rule: f′(x) = 3u² · u′ = 3(√(x³) + 2x − 7)² ((3/2)√x + 2).
Equivalent form: (3/2)(3√x + 4)(x√x + 2x − 7)².
Numerical check at x = 4: u = 8 + 8 − 7 = 9, u′ = 3 + 2 = 5, so f′(4) = 3 · 81 · 5 = 1215; difference quotient (f(4.001) − f(3.999))/0.002 ≈ 1215.0. Agrees.

(p.96)

### Theorem 2.6

Let g be differentiable at a, and f be differentiable at g(a). Then f ∘ g is differentiable at a, and (f ∘ g)′(a) = f′(g(a)) · g′(a).

The Chain rule can be interpreted as saying that (f ∘ g)′(x) = f′(g(x))g′(x) for all x such that g is differentiable at x and f is differentiable at g(x).

**Proof**

For g(x) − g(a) ≠ 0,

(f(g(x)) − f(g(a)))/(x − a) = (f(g(x)) − f(g(a)))/(x − a) · (g(x) − g(a))/(g(x) − g(a))

By definition of derivative as x gets very close to a,

((f ∘ g)(x) − (f ∘ g)(a))/(x − a) = (f(g(x)) − f(g(a)))/(x − a)
= (f(g(x)) − f(g(a)))/(g(x) − g(a)) · (g(x) − g(a))/(x − a)

As x → a, the expressions

(f(g(x)) − f(g(a)))/(g(x) − g(a)) = f′(g(a)) and (g(x) − g(a))/(x − a) = g′(a)

Thus, (f ∘ g)′(a) = f′(g(a)) g′(a).

[added step: as x → a, g(x) → g(a) because g is continuous at a, which is why the first quotient tends to f′(g(a)). The book's proof assumes g(x) − g(a) ≠ 0 for x near a; the general case needs a slightly different argument not given here.]

### Example 1

For each of the following functions find a formula for f′(x).

a. f(x) = √(x⁴ + 3x² − 5)   b. f(x) = (5x + 4)²¹

**Solution**

Using the Chain rule

a. f is the composition of two simple functions g(x) = √x and h(x) = x⁴ + 3x² − 5. That is, f(x) = g(h(x)).

(p.97)

By the chain rule, f′(x) = g′(h(x)) h′(x).

But g′(x) = 1/(2√x) and h′(x) = 4x³ + 6x

Thus, f′(x) = g′(h(x)) h′(x) = 1/(2√(x⁴ + 3x² − 5)) · (4x³ + 6x) = (2x³ + 3x)/√(x⁴ + 3x² − 5).

[added step: (4x³ + 6x)/2 = 2x³ + 3x]

b. f′(x) = 21(5x + 4)^(21−1) = 21(5x + 4)²⁰(5) = 105(5x + 4)²⁰.

[added step: the inner function 5x + 4 has derivative 5, so 21(5x + 4)²⁰ is multiplied by 5. The printed first equality "21(5x + 4)^(21−1)" omits the inner derivative; the factor (5) is included in the next step.]

### Example 2

Let y = √(4 + x⁵). Find a formula for dy/dx and compute dy/dx|_{x=2}.

**Solution**

dy/dx = 1/(2√(4 + x⁵)) · d/dx(x⁵ + 4) = 5x⁴/(2√(4 + x⁵)) and dy/dx|_{x=2} = 20/3.

[added step: at x = 2, 5x⁴ = 5 × 16 = 80 and 4 + x⁵ = 4 + 32 = 36, √36 = 6; so dy/dx = 80/(2 × 6) = 80/12 = 20/3]

### Exercise 2.13

Find the derivative of the following functions using the chain rule.

a. f(x) = (2x + 1)⁴

**Answer:** f′(x) = 8(2x + 1)³
**Why:**
Outer u⁴, inner u = 2x + 1, u′ = 2.
Chain rule: f′(x) = 4(2x + 1)³ · 2 = 8(2x + 1)³.
Check: expanding, 8(2x + 1)³ = 64x³ + 96x² + 48x + 8, and f(x) = 16x⁴ + 32x³ + 24x² + 8x + 1 gives f′(x) = 64x³ + 96x² + 48x + 8. Agrees.

b. f(x) = (x³ + 2x)²⁵

**Answer:** f′(x) = 25(x³ + 2x)²⁴(3x² + 2)
**Why:**
Outer u²⁵, inner u = x³ + 2x.
u′ = 3x² + 2 (power rule, constant multiple rule, sum rule).
Chain rule: f′(x) = 25u²⁴ · u′ = 25(x³ + 2x)²⁴(3x² + 2).

c. f(x) = √(x² + 3x − 1)

**Answer:** f′(x) = (2x + 3)/(2√(x² + 3x − 1))
**Why:**
Outer √u = u^(1/2), inner u = x² + 3x − 1.
d/du u^(1/2) = 1/(2√u); u′ = 2x + 3.
Chain rule: f′(x) = 1/(2√(x² + 3x − 1)) · (2x + 3) = (2x + 3)/(2√(x² + 3x − 1)).

d. f(x) = 1/(3x + 2)²

**Answer:** f′(x) = −6/(3x + 2)³
**Why:**
Rewrite: f(x) = (3x + 2)⁻².
Outer u⁻², inner u = 3x + 2, u′ = 3.
Chain rule: f′(x) = −2(3x + 2)⁻³ · 3 = −6(3x + 2)⁻³ = −6/(3x + 2)³.

e. f(x) = √(x² + 1/x²)

**Answer:** f′(x) = (x − 1/x³)/√(x² + 1/x²)  (for x > 0 this equals (x⁴ − 1)/(x²√(x⁴ + 1)))
**Why:**
Rewrite inner u = x² + x⁻².
u′ = 2x − 2x⁻³ = 2x − 2/x³ (power rule).
Outer √u: derivative 1/(2√u).
Chain rule: f′(x) = (2x − 2/x³)/(2√(x² + 1/x²)).
Cancel the factor 2: f′(x) = (x − 1/x³)/√(x² + 1/x²).
Simplify for x > 0: √(x² + 1/x²) = √((x⁴ + 1)/x²) = √(x⁴ + 1)/x, and x − 1/x³ = (x⁴ − 1)/x³.
So f′(x) = ((x⁴ − 1)/x³) · (x/√(x⁴ + 1)) = (x⁴ − 1)/(x²√(x⁴ + 1)).
Numerical check at x = 2: formula gives 15/(4√17) ≈ 0.9095; difference quotient ≈ 0.9095. Agrees.

f. f(x) = ((3x − 5)/(2 − 7x))⁶

**Answer:** f′(x) = −174(3x − 5)⁵/(2 − 7x)⁷  (equivalently 174(3x − 5)⁵/(7x − 2)⁷)
**Why:**
Outer u⁶, inner u = (3x − 5)/(2 − 7x).
Quotient rule for u: u′ = (3(2 − 7x) − (3x − 5)(−7))/(2 − 7x)².
3(2 − 7x) = 6 − 21x.
−(3x − 5)(−7) = 7(3x − 5) = 21x − 35.
Numerator: 6 − 21x + 21x − 35 = −29.
u′ = −29/(2 − 7x)².
Chain rule: f′(x) = 6u⁵ · u′ = 6 · (3x − 5)⁵/(2 − 7x)⁵ · (−29)/(2 − 7x)².
f′(x) = −174(3x − 5)⁵/(2 − 7x)⁷.

(p.98)

### 2.1.5 Maximum and Minimum Points

The differentiation of various functions renders great services in solving the problems concerned with finding out the maximum and minimum values of quantities. In the various fields of engineering and technology, we have to find the maximum or minimum values of one quantity with respect to another quantity. For example, in finding the radius and height of a cylinder that is to be manufactured with the metal sheet of a given surface area, so that the capacity of cylinder is maximum. Sometimes it is necessary to find the least cost for the transmission of given horsepower. We can find the dimensions of a plot of a given perimeter so that its area is maximum and so on.

#### 2.1.5.1 Increasing and Decreasing Functions

### Activity 2.12

1. Find the real zeros of each of the following functions.

a. f(x) = 4x − 8

**Answer:** x = 2
**Why:**
Set f(x) = 0: 4x − 8 = 0.
4x = 8.
x = 2.

b. f(x) = x² − x − 12

**Answer:** x = −3 or x = 4
**Why:**
Set x² − x − 12 = 0.
Factor: two numbers with product −12 and sum −1 are −4 and 3, so (x − 4)(x + 3) = 0.
x − 4 = 0 or x + 3 = 0, so x = 4 or x = −3.

c. f(x) = (1 − √x)/(x − 2)²

**Answer:** x = 1
**Why:**
Domain: x ≥ 0 (for √x) and x ≠ 2 (denominator ≠ 0).
A fraction is zero when its numerator is zero and denominator is not: 1 − √x = 0.
√x = 1, so x = 1.
At x = 1 the denominator is (1 − 2)² = 1 ≠ 0, so x = 1 is a zero.

2. Consider the graph of the following function.

[figure: Figure 2.10 — graph of a function on [a, b]. It starts at x = a with a positive y-value, rises to a peak at x = p, falls, crossing the x-axis, down to x = q where it is below the x-axis; it is a horizontal line segment (constant) from x = q to x = r below the x-axis; from r it rises, crossing the x-axis, to its highest point at x = b. Dashed vertical lines mark a, p, q, r, b.]

a. Identify the intervals in which the graph is rising and falling as you move from left to right starting at a.

**Answer:** Rising on [a, p] and on [r, b]; falling on [p, q].
**Why:**
From a to p the y-values go up (graph rises to the peak at p).
From p to q the y-values go down.
From r to b the y-values go up again.

b. Identify the intervals in which the graph is neither rising nor falling.

**Answer:** [q, r]
**Why:**
Between q and r the graph is a horizontal segment: y is constant, so it neither rises nor falls.

3. Solve each of the following inequalities using sign chart method:

a. 2x² + 3x − 2 ≥ 0

**Answer:** x ≤ −2 or x ≥ 1/2, i.e. (−∞, −2] ∪ [1/2, ∞)
**Why:**
Factor: 2x² + 3x − 2 = (2x − 1)(x + 2) [check: 2x² + 4x − x − 2 = 2x² + 3x − 2].
Zeros: x = 1/2 and x = −2.
Sign chart:

| | x < −2 | −2 | −2 < x < 1/2 | 1/2 | x > 1/2 |
|---|---|---|---|---|---|
| x + 2 | − | 0 | + | | + |
| 2x − 1 | − | | − | 0 | + |
| product | + | 0 | − | 0 | + |

Product ≥ 0 where it is + or 0: x ≤ −2 or x ≥ 1/2.

b. x² + 3x − 4 < 0

**Answer:** −4 < x < 1, i.e. (−4, 1)
**Why:**
Factor: x² + 3x − 4 = (x + 4)(x − 1) [check: x² − x + 4x − 4 = x² + 3x − 4].
Zeros: x = −4 and x = 1.

| | x < −4 | −4 | −4 < x < 1 | 1 | x > 1 |
|---|---|---|---|---|---|
| x + 4 | − | 0 | + | | + |
| x − 1 | − | | − | 0 | + |
| product | + | 0 | − | 0 | + |

Product < 0 (strictly) only on −4 < x < 1.

(p.99)

### Definition 2.8

Let f be a function on an interval I. If x₁ and x₂ are in I,

i. For x₁ < x₂ if f(x₁) ≤ f(x₂), then f is said to be increasing on I.

ii. For x₁ < x₂ if f(x₁) ≥ f(x₂), then f is said to be decreasing on I.

iii. For x₁ < x₂ if f(x₁) < f(x₂), then f is strictly increasing on I.

iv. For x₁ < x₂ if f(x₁) > f(x₂), then f is strictly decreasing on I.

Geometrically, a function is increasing if its graph rises and decreases if its graph falls while x moves to the right.

[figure: Figure 2.11a — a rising curve f with an arrow labelled "Increasing"; points a < b on the x-axis with f(a) < f(b) marked on the y-axis.]
[figure: Figure 2.11b — a falling curve g with an arrow labelled "Decreasing"; points a < b on the x-axis with g(a) > g(b) marked on the y-axis.]

**Increasing and decreasing test**

Suppose that f(x₁) ≥ f(x₂), f is differentiable in the interior of an interval I.

a. If f′(x) ≥ 0, for all x in the interior of I, then f is increasing on I.

b. If f′(x) ≤ 0, for all x in the interior of I, then f is decreasing on I.

c. If f′(x) > 0 and f′(x) = 0 on I, then f is strictly increasing on I.

d. If f′(x) < 0 and f′(x) = 0 on I, then f is strictly decreasing on I.

[review: the printed test has two apparent misprints. (1) "Suppose that f(x₁) ≥ f(x₂), f is differentiable…" — the clause "f(x₁) ≥ f(x₂)" does not belong; it should read "Suppose that f is continuous on I and differentiable in the interior of I." (2) In c and d, "f′(x) > 0 and f′(x) = 0 on I" is self-contradictory; the intended statement is "If f′(x) > 0 for all x in the interior of I (f′ may be 0 only at isolated points), then f is strictly increasing on I", and similarly for d with f′(x) < 0. Transcribed as printed.]

> **Note**
> A function that is either increasing or decreasing is known as a monotonic function.

(p.100)

### Definition 2.9

A number c in the domain of a function f is said to be a **critical number** of f if and only if either f′(c) = 0 or f has no derivative at c.

### Example 1

Find the critical numbers of the given functions.

a. f(x) = 4x³ − 5x² − 8x + 20   b. f(x) = 2√x(6 − x)

**Solution**

a. f′(x) = 12x² − 10x − 8

f′(x) = 0 ⇒ 2(6x² − 5x − 4) = 2(2x + 1)(3x − 4) = 0 ⇒ x = −1/2 or x = 4/3

Hence, the critical numbers of f are x = −1/2 and x = 4/3.

[added step: check the factorisation (2x + 1)(3x − 4) = 6x² − 8x + 3x − 4 = 6x² − 5x − 4]

b. Applying the product rule of derivatives:

f′(x) = (2/(2√x))(6 − x) − 2√x = (6 − x)/√x − 2x/√x = (6 − 3x)/√x = 3(2 − x)/√x ⇒

f′(x) = 0 ⇒ x = 2

and f′(x) does not exist when x = 0. Hence, the critical numbers of f are x = 0 and x = 2.

[added step: (2√x)′ = 2 · 1/(2√x) = 1/√x and (6 − x)′ = −1; so f′(x) = (1/√x)(6 − x) + 2√x(−1). Also 2√x = 2√x·√x/√x = 2x/√x. x = 0 is in the domain of f (f(0) = 0), which is why it counts as a critical number.]

### Example 2

Find the interval on which the function f(x) = 3x⁴ − 4x³ − 12x² + 5 is increasing and decreasing.

(p.101)

**Solution**

f′(x) = 12x³ − 12x² − 24x = 12x(x² − x − 2) = 12x(x − 2)(x + 1)

Hence, the critical numbers f are x = −1, 0, 2

| | x < −1 | −1 | −1 < x < 0 | 0 | 0 < x < 2 | 2 | x > 2 |
|---|---|---|---|---|---|---|---|
| 12x | − | | − | 0 | + | | + |
| x + 1 | − | 0 | + | | + | | + |
| x − 2 | − | | − | | − | 0 | + |
| f′(x) = 12x(x − 2)(x + 1) | − | 0 | + | 0 | − | 0 | + |

From the sign chart above,

f′(x) ≥ 0 on [−1, 0] ∪ [2, ∞) and f′(x) ≤ 0 on (−∞, −1] ∪ [0, 2].

Therefore, the function is increasing on an interval [−1, 0] ∪ [2, ∞) and decreasing on (−∞, −1] ∪ [0, 2].

[added step: f is increasing on each of the intervals [−1, 0] and [2, ∞) separately, and decreasing on each of (−∞, −1] and [0, 2] separately; it is not increasing on the union as a single set (e.g. f(0) = 5 > f(1) = −8).]

### Exercise 2.14

1. Find all the critical numbers of the following functions.

a. f(x) = x³ + 6x²

**Answer:** x = −4 and x = 0
**Why:**
f′(x) = 3x² + 12x (power rule, constant multiple rule, sum rule).
f′ exists for every real x, so critical numbers come only from f′(x) = 0.
3x² + 12x = 3x(x + 4) = 0.
x = 0 or x = −4.

b. f(x) = 2x²/(1 − x²)

**Answer:** x = 0
**Why:**
Domain: 1 − x² ≠ 0, so x ≠ ±1.
Quotient rule with u = 2x², v = 1 − x²: u′ = 4x, v′ = −2x.
f′(x) = (4x(1 − x²) − 2x²(−2x))/(1 − x²)².
Numerator: 4x − 4x³ + 4x³ = 4x.
f′(x) = 4x/(1 − x²)².
f′(x) = 0 ⇒ 4x = 0 ⇒ x = 0.
f′ fails to exist only at x = ±1, which are not in the domain, so they are not critical numbers.

c. f(x) = 2x³ + 9x² − 24x

**Answer:** x = −4 and x = 1
**Why:**
f′(x) = 6x² + 18x − 24 (power and constant multiple rules).
6x² + 18x − 24 = 6(x² + 3x − 4) = 6(x + 4)(x − 1).
f′(x) = 0 ⇒ x = −4 or x = 1.
f′ exists everywhere.

d. f(x) = 8x√(1 − x²)

**Answer:** x = −1, −√2/2, √2/2, 1
**Why:**
Domain: 1 − x² ≥ 0, so −1 ≤ x ≤ 1.
Product rule with u = 8x, v = √(1 − x²): u′ = 8.
Chain rule: v′ = 1/(2√(1 − x²)) · (−2x) = −x/√(1 − x²).
f′(x) = 8√(1 − x²) + 8x(−x/√(1 − x²)) = 8√(1 − x²) − 8x²/√(1 − x²).
Common denominator: f′(x) = (8(1 − x²) − 8x²)/√(1 − x²) = 8(1 − 2x²)/√(1 − x²).
f′(x) = 0 ⇒ 1 − 2x² = 0 ⇒ x² = 1/2 ⇒ x = ±1/√2 = ±√2/2.
f′ does not exist at x = ±1 (denominator 0), and ±1 are in the domain, so by Definition 2.9 they are critical numbers too (same reasoning as x = 0 in Example 1b).

2. Find the interval on which the following functions are increasing and decreasing.

a. f(x) = x³ + 6x²

**Answer:** Increasing on (−∞, −4] and [0, ∞); decreasing on [−4, 0].
**Why:**
f′(x) = 3x² + 12x = 3x(x + 4); zeros x = −4, 0.

| | x < −4 | −4 | −4 < x < 0 | 0 | x > 0 |
|---|---|---|---|---|---|
| 3x | − | | − | 0 | + |
| x + 4 | − | 0 | + | | + |
| f′(x) | + | 0 | − | 0 | + |

f′ ≥ 0 ⇒ increasing; f′ ≤ 0 ⇒ decreasing.

b. f(x) = 2x² + 6x − 10

**Answer:** Decreasing on (−∞, −3/2]; increasing on [−3/2, ∞).
**Why:**
f′(x) = 4x + 6.
f′(x) = 0 ⇒ x = −6/4 = −3/2.
For x < −3/2, 4x + 6 < 0 (e.g. x = −2: −2); for x > −3/2, 4x + 6 > 0 (e.g. x = 0: 6).

c. f(x) = −2x³ + 3x² + 12x + 6

**Answer:** Increasing on [−1, 2]; decreasing on (−∞, −1] and [2, ∞).
**Why:**
f′(x) = −6x² + 6x + 12.
Factor: −6(x² − x − 2) = −6(x − 2)(x + 1); zeros x = −1, 2.

| | x < −1 | −1 | −1 < x < 2 | 2 | x > 2 |
|---|---|---|---|---|---|
| −6 | − | − | − | − | − |
| x + 1 | − | 0 | + | | + |
| x − 2 | − | | − | 0 | + |
| f′(x) | − | 0 | + | 0 | − |

Test value: f′(0) = 12 > 0, consistent.

d. f(x) = x − 6√(x − 1)

**Answer:** Decreasing on [1, 10]; increasing on [10, ∞).
**Why:**
Domain: x − 1 ≥ 0, so x ≥ 1.
Chain rule: d/dx √(x − 1) = 1/(2√(x − 1)).
f′(x) = 1 − 6 · 1/(2√(x − 1)) = 1 − 3/√(x − 1) = (√(x − 1) − 3)/√(x − 1).
f′(x) = 0 ⇒ √(x − 1) = 3 ⇒ x − 1 = 9 ⇒ x = 10.
f′ does not exist at x = 1 (critical number, endpoint of domain).
For 1 < x < 10: √(x − 1) < 3, so f′ < 0 (e.g. x = 2: 1 − 3 = −2).
For x > 10: √(x − 1) > 3, so f′ > 0 (e.g. x = 17: 1 − 3/4 = 1/4).

e. f(x) = (x + 3)²(x − 1)²

**Answer:** Decreasing on (−∞, −3] and [−1, 1]; increasing on [−3, −1] and [1, ∞).
**Why:**
Product rule with chain rule: f′(x) = 2(x + 3)(x − 1)² + (x + 3)² · 2(x − 1).
Factor out 2(x + 3)(x − 1): f′(x) = 2(x + 3)(x − 1)[(x − 1) + (x + 3)].
(x − 1) + (x + 3) = 2x + 2 = 2(x + 1).
f′(x) = 4(x + 3)(x + 1)(x − 1); zeros x = −3, −1, 1.

| | x < −3 | −3 | −3 < x < −1 | −1 | −1 < x < 1 | 1 | x > 1 |
|---|---|---|---|---|---|---|---|
| x + 3 | − | 0 | + | | + | | + |
| x + 1 | − | | − | 0 | + | | + |
| x − 1 | − | | − | | − | 0 | + |
| f′(x) | − | 0 | + | 0 | − | 0 | + |

Test value: f′(0) = 4(3)(1)(−1) = −12 < 0, consistent.

(p.102)

#### 2.1.5.2 Minimum and maximum values of a function

### Activity 2.13

Consider the graph of the following function.

[figure: Figure 2.12 — the same graph as Figure 2.10: starts at x = a above the x-axis, peak at x = p, falls below the x-axis to x = q, constant (horizontal segment) from q to r below the axis, then rises to its highest point at the right end x = b.]

a. Where does the function attain maximum value and a minimum value?

**Answer:** Local (relative) maximum at x = p; the greatest (absolute) maximum value on [a, b] is at the endpoint x = b. The minimum value is attained at every x in [q, r] (the flat lowest part of the graph).
**Why:**
Near p the graph is higher at p than at the points on either side, so p gives a local maximum.
The highest point of the whole graph is at x = b (the right endpoint), so f(b) is the absolute maximum.
The lowest y-value of the graph is the constant value on the horizontal segment from q to r, so the minimum value is attained at all points of [q, r].

b. What happens to the gradient at a maximum point and at a minimum point?

**Answer:** At the turning point p and along the flat minimum segment the gradient (slope of the tangent) is zero. At the endpoint maximum x = b the gradient is not zero (the graph is still rising there).
**Why:**
At p the tangent line is horizontal: the graph changes from rising (positive slope) to falling (negative slope), so the slope passes through 0.
On [q, r] the graph is a horizontal line, slope 0.
At b the graph is rising up to the end of the interval, so the slope there is positive; an extreme value at an endpoint need not have zero gradient.

### Definition 2.10

If there exists an open interval (a, b) containing c such that f(x) < f(c) for all x in (a, b) other than c in the interval, then f(c) is a relative (local) maximum value of f and a point (c, f(c)) is called relative maximum point. If f(x) > f(c) for all x in (a, b) other than c, then f(c) is a relative (local) minimum value of f and the point (c, f(c)) is known as relative(local) minimum point (See Figure 2.13 below). Functions may have any number of relative extrema.

(p.103)

[figure: Figure 2.13 — a wavy curve y = f(x) with two local maxima (marked with dots and horizontal dashed tangent lines, labelled "Local Maximum") and one local minimum between them (dot with horizontal dashed tangent, labelled "Local Minimum").]

### Definition 2.11

If c is in the domain of f and for all x in the domain of the function, f(x) ≤ f(c), then (c, f(c)) is an absolute maximum piont of the function f. If for all x in the domain f(x) ≥ f(c) then (c, f(c)) is an absolute minimum point of the function f. (see Figure 2.14). The absolute maximum and minimum values of f are called absolute extreme values.

> **Note**
> - Absolute extrema are not necessarily unique.
> - At either local maximum or local minimum point the gradient is zero.

[review: the second note bullet is only true when f is differentiable at that point. For example f(x) = |x| has a local minimum at x = 0 where the derivative does not exist (consistent with Definition 2.9: extrema occur at critical numbers). Also "piont" in Definition 2.11 is the book's misspelling of "point". Transcribed as printed.]
[review: Definition 2.10 uses strict inequalities f(x) < f(c); with this definition, the points on the flat segment [q, r] in Figure 2.12 are not strict local minima. Worth handling carefully in the lesson.]

(p.104)

[figure: Figure 2.14 — a curve over a closed interval with labelled points from left to right: "Absolute minimum" at the left endpoint; "Relative maximum" (a peak); "Relative minimum" (a valley); "Relative maximum" (a lower, rounded peak); "Relative minimum" (a valley); "Point of inflection" (where the curve flattens while still rising); "Absolute maximum" at the right endpoint (highest point). Dashed vertical lines drop from each marked point to the x-axis.]

> **Procedure to find absolute extreme values on closed intervals**
>
> We can find the absolute maximum and minimum values of a function f on a closed interval [a, b] by the following steps:
>
> **Step 1**: Find all the critical numbers of a function f.
>
> **Step 2**: Evaluate f at all critical numbers and at the end points a and b.
>
> **Step 3**: Choose the largest and the smallest values obtained in step2. These values are the maximum and the minimum of a function f on [a, b].

### Example

Find the absolute maximum and minimum values of the function f(x) = x² − 2x on [−1, 2].

**Solution**

f′(x) = 2x − 2 = 2(x − 1)

f′(x) = 0 ⇒ x = 1.

Thus, the critical number of f is x = 1.

(p.105)

Thus, to determine the extreme value of the function we need to evaluate the value of the function at the boundary and critical number.

f(−1) = 1 + 2 = 3, f(1) = 1 − 2 = −1 and f(2) = 4 − 4 = 0.

Therefore, the absolute maximum value is f(−1) = 3 and the absolute minimum value is f(1) = −1. Thus, (−1, 3) is the maximum point and (1, −1) is the minimum point of f.

### Exercise 2.15

Find the absolute maximum and minimum values of the following functions on a given interval.

a. f(x) = x² + 2x + 3, [−2, 2]

**Answer:** Absolute maximum 11 (at x = 2); absolute minimum 2 (at x = −1).
**Why:**
Step 1: f′(x) = 2x + 2 = 2(x + 1); f′(x) = 0 ⇒ x = −1, which lies in [−2, 2].
Step 2: f(−2) = 4 − 4 + 3 = 3.
f(−1) = 1 − 2 + 3 = 2.
f(2) = 4 + 4 + 3 = 11.
Step 3: largest value 11, smallest value 2.

b. f(x) = x³ + 3x² − 9x + 5, [−2, 2]

**Answer:** Absolute maximum 27 (at x = −2); absolute minimum 0 (at x = 1).
**Why:**
Step 1: f′(x) = 3x² + 6x − 9 = 3(x² + 2x − 3) = 3(x + 3)(x − 1).
f′(x) = 0 ⇒ x = −3 or x = 1; only x = 1 is in [−2, 2].
Step 2: f(−2) = −8 + 12 + 18 + 5 = 27.
f(1) = 1 + 3 − 9 + 5 = 0.
f(2) = 8 + 12 − 18 + 5 = 7.
Step 3: largest 27, smallest 0.

c. f(x) = 3x⁴ − 26x³ − 60x² − 11 on [1, 5].

**Answer:** Absolute maximum −94 (at x = 1); absolute minimum −2886 (at x = 5).
**Why:**
Step 1: f′(x) = 12x³ − 78x² − 120x = 6x(2x² − 13x − 20).
f′(x) = 0 ⇒ x = 0 or 2x² − 13x − 20 = 0.
Quadratic formula: x = (13 ± √(169 + 160))/4 = (13 ± √329)/4 ≈ 7.785 or −1.285.
None of 0, 7.785, −1.285 lies in [1, 5], so there are no critical numbers in the interval (f′ < 0 throughout, e.g. f′(2) = 96 − 312 − 240 = −456, so f is decreasing on [1, 5]).
Step 2: f(1) = 3 − 26 − 60 − 11 = −94.
f(5) = 3(625) − 26(125) − 60(25) − 11 = 1875 − 3250 − 1500 − 11 = −2886.
Step 3: largest −94, smallest −2886.
[review: transcription is clear, but the numbers are unusual for a textbook item (no critical number inside [1, 5]). If the intended function or interval differs (e.g. a printing slip), the answer changes; with the function as printed the answer above is correct.]

d. f(x) = (x² − 2x + 4)/(x − 2), [−3, 1]

**Answer:** Absolute maximum −2 (at x = 0); absolute minimum −19/5 (at x = −3).
**Why:**
f is defined on [−3, 1] (x = 2 is outside the interval).
Quotient rule with u = x² − 2x + 4, v = x − 2: u′ = 2x − 2, v′ = 1.
f′(x) = ((2x − 2)(x − 2) − (x² − 2x + 4)(1))/(x − 2)².
(2x − 2)(x − 2) = 2x² − 4x − 2x + 4 = 2x² − 6x + 4.
Numerator: 2x² − 6x + 4 − x² + 2x − 4 = x² − 4x = x(x − 4).
f′(x) = x(x − 4)/(x − 2)²; f′(x) = 0 ⇒ x = 0 or x = 4; only x = 0 is in [−3, 1].
Step 2: f(−3) = (9 + 6 + 4)/(−5) = −19/5 = −3.8.
f(0) = 4/(−2) = −2.
f(1) = (1 − 2 + 4)/(−1) = −3.
Step 3: largest −2, smallest −19/5.

**The first derivative test**

Let c be a critical number of a function f on an open interval I containing c.

a. If the sign of f′ changes from negative to positive at c, then f has a relative minimum at c.

b. If the sign of f′ changes from positive to negative at c, then f has a relative maximum at c.

c. If the sign of f′ does not change at c, then f has no relative maximum or minimum at c.

(p.106)

> **Procedure to find relative extreme value**
>
> To determine relative extreme value of a function using the first derivative test, one can follow the following steps.
>
> **Step 1**: Find all the critical numbers of f.
>
> **Step 2**: Form the sign chart for f′(x) using the critical number as poles.
>
> **Step 3**: Apply first derivative test and decide the extreme values if any.

### Example 1

Find the relative maximum and minimum values of

a. f(x) = 2x³ + 3x² − 12x − 3   b. f(x) = (x − 1)²(x − 3)²

**Solution**

a. f′(x) = 6x² + 6x − 12 = 6(x² + x − 2) = 6(x + 2)(x − 1)

Hence, the critical numbers are x = −2, 1

| | x < −2 | −2 | −2 < x < 1 | 1 | x > 1 |
|---|---|---|---|---|---|
| 6(x + 2) | − | 0 | + | | + |
| x − 1 | − | | − | 0 | + |
| f′(x) = 6(x + 2)(x − 1) | + | 0 | − | 0 | + |

From the sign chart above we see that, f′ changes its sign from positive to negative at x = −2 and changes from negative to positive x = 1, therefore, the function has a local maximum value at x = −2 and a local minimum value at x = 1. This implies the point (−2, f(−2)) = (−2, 17) is a relative maximum and (1, f(1)) = (1, −10) is a relative minimum point of the function.

Thus, 17 is a relative maximum value and − 10 is a relative minimum value.

[added step: f(−2) = 2(−8) + 3(4) − 12(−2) − 3 = −16 + 12 + 24 − 3 = 17; f(1) = 2 + 3 − 12 − 3 = −10]

(p.107)

b.

f′(x) = 2(x − 1)(x − 3)² + 2(x − 1)²(x − 3)
= 2(x − 1)(x − 3)(x − 3 + x − 1)
= 2(x − 1)(x − 3)(2x − 4)
= 4(x − 1)(x − 2)(x − 3)

[added step: product rule with chain rule — d/dx (x − 1)² = 2(x − 1) and d/dx (x − 3)² = 2(x − 3); then factor out 2(x − 1)(x − 3), and 2x − 4 = 2(x − 2).]

Hence, the critical numbers are x = 1, 2, 3.

| | x < 1 | 1 | 1 < x < 2 | 2 | 2 < x < 3 | 3 | x > 3 |
|---|---|---|---|---|---|---|---|
| 4(x − 1) | − | 0 | + | | + | | + |
| x − 2 | − | | − | 0 | + | | + |
| x − 3 | − | | − | | − | 0 | + |
| f′(x) = 4(x − 1)(x − 2)(x − 3) | − | 0 | + | 0 | − | 0 | + |

From the sign chart, we see that f′ changes its sign from negative to positive at x = 1 and x = 3 and changes from positive to negative at x = 2. Therefore, (1, f(1)) = (1, 0) and (3, f(3)) = (3, 0) are relative minimum points and (2, f(2)) = (2, 1) is the relative maximum point of the function.

Thus, 0 is a relative maximum value and 1 is a relative minimum value.

[review: book says "0 is a relative maximum value and 1 is a relative minimum value"; the working (and the book's own previous sentence) gives the reverse: 1 is the relative maximum value (at x = 2, f(2) = (1)²(−1)² = 1) and 0 is the relative minimum value (at x = 1 and x = 3). The final sentence has max/min swapped.]

### Example 2

If f(x) = ax³ + bx − 5 has a relative minimum value of −6 at x = 1/2, find a and b.

**Solution**

Given f(1/2) = (1/8)a + (1/2)b − 5 = −6 ⇔ a + 4b = −8   (i)

and f′(1/2) = 0, f′(x) = 3ax² + b ⇒ 3a/4 + b = 0 ⇔ 3a + 4b = 0   (ii)

(i) and (ii) imply { a + 4b = −8 ; 3a + 4b = 0 } ⇒ a = 4 and b = −3.

[added step: from (i), (1/8)a + (1/2)b = −1; multiply by 8: a + 4b = −8. From (ii), multiply by 4: 3a + 4b = 0. Subtract (i) from (ii): 2a = 8, so a = 4; then 4 + 4b = −8 gives b = −3. Check: f(x) = 4x³ − 3x − 5, f′(x) = 12x² − 3 = 3(2x − 1)(2x + 1) changes from − to + at x = 1/2, and f(1/2) = 1/2 − 3/2 − 5 = −6. ✓]

(p.108)

### Exercise 2.16

1. Find the relative extreme value of the following functions (if any).

a. f(x) = 2x³ − 9x² − 24

**Answer:** Relative maximum value −24 (at x = 0); relative minimum value −51 (at x = 3).
**Why:**
Step 1: f′(x) = 6x² − 18x = 6x(x − 3); critical numbers x = 0, 3.
Step 2: sign chart:

| | x < 0 | 0 | 0 < x < 3 | 3 | x > 3 |
|---|---|---|---|---|---|
| 6x | − | 0 | + | | + |
| x − 3 | − | | − | 0 | + |
| f′(x) | + | 0 | − | 0 | + |

Step 3: f′ changes + to − at x = 0 ⇒ relative maximum; − to + at x = 3 ⇒ relative minimum.
f(0) = −24.
f(3) = 2(27) − 9(9) − 24 = 54 − 81 − 24 = −51.

b. f(x) = (1/4)x³ − 3x

**Answer:** Relative maximum value 4 (at x = −2); relative minimum value −4 (at x = 2).
**Why:**
Step 1: f′(x) = (3/4)x² − 3 = (3/4)(x² − 4) = (3/4)(x − 2)(x + 2); critical numbers x = −2, 2.
Step 2: sign chart:

| | x < −2 | −2 | −2 < x < 2 | 2 | x > 2 |
|---|---|---|---|---|---|
| x + 2 | − | 0 | + | | + |
| x − 2 | − | | − | 0 | + |
| f′(x) | + | 0 | − | 0 | + |

Step 3: + to − at x = −2 ⇒ relative maximum; − to + at x = 2 ⇒ relative minimum.
f(−2) = (1/4)(−8) − 3(−2) = −2 + 6 = 4.
f(2) = (1/4)(8) − 6 = 2 − 6 = −4.

c. f(x) = (x² + x + 1)/(x² − x + 1)

**Answer:** Relative minimum value 1/3 (at x = −1); relative maximum value 3 (at x = 1).
**Why:**
Domain: x² − x + 1 has discriminant 1 − 4 = −3 < 0, so it is never 0; domain is all real numbers.
Quotient rule with u = x² + x + 1, v = x² − x + 1: u′ = 2x + 1, v′ = 2x − 1.
f′(x) = ((2x + 1)(x² − x + 1) − (x² + x + 1)(2x − 1))/(x² − x + 1)².
(2x + 1)(x² − x + 1) = 2x³ − 2x² + 2x + x² − x + 1 = 2x³ − x² + x + 1.
(x² + x + 1)(2x − 1) = 2x³ − x² + 2x² − x + 2x − 1 = 2x³ + x² + x − 1.
Numerator: (2x³ − x² + x + 1) − (2x³ + x² + x − 1) = −2x² + 2 = −2(x − 1)(x + 1).
f′(x) = −2(x − 1)(x + 1)/(x² − x + 1)²; critical numbers x = −1, 1.

| | x < −1 | −1 | −1 < x < 1 | 1 | x > 1 |
|---|---|---|---|---|---|
| −2(x − 1)(x + 1) | − | 0 | + | 0 | − |
| (x² − x + 1)² | + | + | + | + | + |
| f′(x) | − | 0 | + | 0 | − |

− to + at x = −1 ⇒ relative minimum: f(−1) = (1 − 1 + 1)/(1 + 1 + 1) = 1/3.
+ to − at x = 1 ⇒ relative maximum: f(1) = (1 + 1 + 1)/(1 − 1 + 1) = 3.

2. If f(x) = x³ + ax + b has a relative minimum value of 4 at x = 2, find a and b.

**Answer:** a = −12, b = 20
**Why:**
f′(x) = 3x² + a.
A relative minimum at x = 2 (f differentiable) ⇒ f′(2) = 0: 3(4) + a = 0 ⇒ a = −12.
Minimum value 4 ⇒ f(2) = 4: 8 + 2a + b = 4.
Substitute a = −12: 8 − 24 + b = 4 ⇒ −16 + b = 4 ⇒ b = 20.
Check: f(x) = x³ − 12x + 20, f′(x) = 3x² − 12 = 3(x − 2)(x + 2) changes from − to + at x = 2 (minimum ✓), and f(2) = 8 − 24 + 20 = 4 ✓.

### 2.1.6 Equation of Tangents and Normal Lines to Curves

### Activity 2.14

1. Find the equation of a line containing the points (1, 3) and (−2, 3).

**Answer:** y = 3
**Why:**
Slope m = (3 − 3)/(−2 − 1) = 0/(−3) = 0.
Point-slope form through (1, 3): y − 3 = 0(x − 1) ⇒ y = 3 (a horizontal line).

2. Find the equation of a line perpendicular to the line found in question 1 above containing the point (1, 3).

**Answer:** x = 1
**Why:**
The line in question 1 is horizontal (slope 0).
A line perpendicular to a horizontal line is vertical (its slope is undefined; the rule m₁m₂ = −1 does not apply to horizontal/vertical pairs).
The vertical line through (1, 3) is x = 1.

3. Write the equation of a tangent line to a curve if its slope is 3 at the point (−2, 5).

**Answer:** y = 3x + 11
**Why:**
Point-slope form: y − 5 = 3(x − (−2)) = 3(x + 2).
y − 5 = 3x + 6.
y = 3x + 11.

4. What is the relationship between the slopes of a tangent line and a normal line to a curve at a point of tangency?
Is there any relation ship between the first derivative of a function at a point of tengency and the slope of a tangent line to the curve of the function?

**Answer:** The tangent and normal are perpendicular, so (slope of tangent) × (slope of normal) = −1, i.e. slope of normal = −1/(slope of tangent) (when the tangent is neither horizontal nor vertical). Yes: the slope of the tangent line at (a, f(a)) equals f′(a).
**Why:**
The normal line is, by definition, perpendicular to the tangent line at the point of tangency.
Two non-vertical perpendicular lines have slopes whose product is −1.
The derivative f′(a) = lim_{h→0} (f(a + h) − f(a))/h is the limit of slopes of secant lines through (a, f(a)), which is the slope of the tangent line there.
Special cases: if f′(a) = 0 the tangent is horizontal and the normal is vertical (x = a).

We have seen in section 2.1.5 that the first derivative of a function at a given point is interpreted as the slope of the tangent line at that point. This implies f′ is the slope of the line tangent to the graph of f at a point (a, f(a)). Thus, the equation of the tangent line to the curve y = f(x) at x = a is given by y = f′(a)(x − a) + f(a).

A line that is perpendicular to the tangent line at the point of tangency is known as the **normal line** to the curve. Since the product of the slope of two non-vertical perpendicular lines is −1, the slope of the normal line at the point of tangency (a, f(a)) is −1/f′(a) and its equation is given by y = −(1/f′(a))(x − a) + f(a).

[review: "We have seen in section 2.1.5" — the slope-of-tangent interpretation of f′ was introduced earlier in 2.1 (before this chunk), not in 2.1.5 (Maximum and Minimum Points). Possibly a wrong cross-reference in the book; transcribed as printed.]

(p.109)

> **Note**
> 1. If the first derivative of f at x = a is zero, then f has a horizontal tangent line with equation y = f(a) and vertical normal line given by x = a.
> 2. If the first derivative of f at x = a undefined, then f has a vertical tangent line with equation x = a and a horizontal normal line given by y = f(a).

[review: Note 2 is not true in general — f′(a) can be undefined because of a corner (e.g. f(x) = |x| at 0) or a discontinuity, where there is no tangent line at all. It holds when the graph is continuous at a and |f′(x)| → ∞ as x → a (e.g. f(x) = ∛x at 0). Transcribed as printed.]

### Example 1

Find the equation of the line tangent and the normal line to the graph of the following functions at the given point.

a. f(x) = x³ − 2x; (1, −1)   b. f(x) = √(20 − x²); (2, 4)

c. f(x) = { x, if x > 3 ; x² − 6, if x ≤ 3 }   d. f(x) = x√(x² + 16); (0, 0)

[review: item c prints no point. The solution works at (1, −5) (f(1) = 1² − 6 = −5), so the intended question is "at (1, −5)".]

**Solution**

a. f′(x) = 3x² − 2 ⇒ f′(1) = 1

Thus,

i. The equation of the tangent line to the graph of f at (1, −1) is

y = f′(1)(x − 1) + f(1) = 1(x − 1) − 1 = x − 2. ⇔ y = x − 2.

ii. The equation of the normal line to the graph of f at (1, −1) is

y = −(1/f′(1))(x − 1) + f(1)
= −1(x − 1) − 1
= −x.

⇔ y = −x

[added step: −(x − 1) − 1 = −x + 1 − 1 = −x]

b. f′(x) = −x/√(20 − x²) ⇒ f′(2) = −1/2

[added step: chain rule — f′(x) = 1/(2√(20 − x²)) · (−2x) = −x/√(20 − x²); f′(2) = −2/√16 = −2/4 = −1/2]

(p.110)

i. The equation of the tangent line to the graph of f at (2, 4) is

y = f′(2)(x − 2) + f(2) = −(1/2)(x − 2) + 4 = −(1/2)x + 5

⇔ y = −(1/2)x + 5.

ii. Since the slope of a normal line is negative reciprocal of that of the tangent line, the slope of the normal line in this problem is 2. Hence, the equation of the normal line to the graph of f at (2, 4) is

y = (−1/f′(2))(x − 2) + f(2) = 2(x − 2) + 4 = 2x.

⇔ y = 2x.

c. f′(x) = { 1, if x > 3 ; 2x, if x > 3 } ⇒ f′(1) = 2.

[review: the second line of the printed f′(x) reads "2x, if x > 3"; it should be "2x, if x < 3" (f is not differentiable at x = 3, since the left piece gives f(3) = 3 but the slopes 6 and 1 differ). f′(1) = 2(1) = 2 is correct.]

i. The equation of the tangent line to the graph of f at (1, −5) is

y = f′(1)(x − 1) + f(2) = 2(x − 1) − 5 = 2x − 7.

⇔ y = 2x − 7.

[review: book writes "+ f(2)" in the tangent-line formula; it should be "+ f(1)" (f(1) = −5, which is the value actually used). The result y = 2x − 7 is correct.]

ii. The equation of the normal line to the graph of f at (1, −5) is

y = −(1/f′(1))(x − 1) + f(1) = (−1/2)(x − 1) − 5 = (−1/2)x − 9/2.

⇔ y = −(1/2)x − 9/2.

[added step: −(1/2)(x − 1) − 5 = −(1/2)x + 1/2 − 5 = −(1/2)x − 9/2]

d. f′(x) = √(x² + 16) + x²/√(x² + 16) ⇒ f′(0) = 4

[added step: product rule — (x)′√(x² + 16) + x(√(x² + 16))′, and by the chain rule (√(x² + 16))′ = 2x/(2√(x² + 16)) = x/√(x² + 16); at x = 0: √16 + 0 = 4]

i. The equation of the tangent line to the graph of f at (0, 0) is

y = f′(0)(x − 0) + f(0) = 4(x − 0) + 0 = 4x.

⇔ y = 4x.

ii. The equation of the normal line to the graph of f at (0, 0) is

y = (−1/f′(0))(x − 0) + f(0) = (−1/4)(x − 0) = (−1/4)x.

⇔ y = −(1/4)x.

[End of this chunk at p.110. Subsection 2.1.6 continues on p.111 (handled separately).]

# Unit 2 Introduction to Calculus — Part C (book pp. 111–135)

## 2.1 (continued)

(p.111)

[The page opens with Example 2 of the subsection on tangent and normal lines / vertical tangents, begun before p.111 (outside this chunk).]

### Example 2

Find all points at where f(x) = √(x² − 6x) has vertical tangent line.

**Solution**

The function will have a vertical tangent line at its first derivative is undefined in its domain and f′(x) = (2x − 6)/(2√(x² − 6x)) = (x − 3)/√(x² − 6x) is undefined at the points where x(x − 6) = 0 ⇒ x = 0 or x = 6. Hence, f(x) has a vertical tangent line at (6, 0) and (0, 0).

[added step: the domain of f is x(x − 6) ≥ 0, i.e. x ≤ 0 or x ≥ 6, so x = 0 and x = 6 are in the domain; f(0) = √0 = 0 and f(6) = √(36 − 36) = 0, which gives the points (0, 0) and (6, 0). Near these points |f′(x)| grows without bound (the numerator x − 3 is −3 or 3, the denominator tends to 0), so the tangent becomes vertical.]

### Exercise 2.17

1. Find the equation of the line tangent and the normal line to the graph of the following functions at the given point.

a. f(x) = x³ + x + 2; (0, 2)

**Answer:** Tangent: y = x + 2. Normal: y = −x + 2.
**Why:**
Check the point: f(0) = 0 + 0 + 2 = 2, so (0, 2) is on the graph.
f′(x) = 3x² + 1.
Slope of tangent: m = f′(0) = 3(0)² + 1 = 1.
Tangent: y − 2 = 1(x − 0) ⇒ y = x + 2.
Slope of normal = −1/m = −1/1 = −1.
Normal: y − 2 = −1(x − 0) ⇒ y = −x + 2.

b. f(x) = (1 − x³)√(x + 2); (−1, 2).

**Answer:** Tangent: y = −2x. Normal: y = (1/2)x + 5/2 (i.e. x − 2y + 5 = 0).
**Why:**
Check the point: f(−1) = (1 − (−1)³)√(−1 + 2) = (1 + 1)(1) = 2. ✓
Product rule: f′(x) = (1 − x³)′ · √(x + 2) + (1 − x³) · (√(x + 2))′.
(1 − x³)′ = −3x²; (√(x + 2))′ = 1/(2√(x + 2)).
f′(x) = −3x²√(x + 2) + (1 − x³)/(2√(x + 2)).
f′(−1) = −3(1)(√1) + (1 + 1)/(2√1) = −3 + 2/2 = −3 + 1 = −2.
Tangent: y − 2 = −2(x + 1) ⇒ y = −2x − 2 + 2 ⇒ y = −2x.
Slope of normal = −1/(−2) = 1/2.
Normal: y − 2 = (1/2)(x + 1) ⇒ y = (1/2)x + 1/2 + 2 ⇒ y = (1/2)x + 5/2.

2. Find all points at where the following functions has vertical tangent line.

a. f(x) = √(x² − x)

**Answer:** (0, 0) and (1, 0).
**Why:**
Domain: x² − x = x(x − 1) ≥ 0 ⇒ x ≤ 0 or x ≥ 1.
f′(x) = (2x − 1)/(2√(x² − x)).
f′ is undefined where the denominator is 0: x² − x = 0 ⇒ x(x − 1) = 0 ⇒ x = 0 or x = 1 (both in the domain).
(x = 1/2 makes the numerator 0, but it is not in the domain, so it is not considered.)
At x = 0 the numerator is −1 and at x = 1 it is 1, while the denominator → 0, so |f′(x)| → ∞: the tangent is vertical.
f(0) = 0, f(1) = 0.
Points: (0, 0) and (1, 0).

b. f(x) = 2√x

**Answer:** (0, 0).
**Why:**
Domain: x ≥ 0.
f′(x) = 2 · 1/(2√x) = 1/√x.
f′ is undefined at x = 0 (in the domain), and f′(x) → +∞ as x → 0⁺.
f(0) = 2√0 = 0.
Point: (0, 0).

3. If f(x) = x² + ax + b and g(x) = x³ − c have the same tangent line at (1, 2) find the values of the constants a, b and c and the equation of their normal lines.

**Answer:** a = 1, b = 0, c = −1. Common tangent y = 3x − 1; common normal line y = −(1/3)x + 7/3 (i.e. x + 3y = 7).
**Why:**
Both graphs pass through (1, 2):
g(1) = 1 − c = 2 ⇒ c = −1.
f(1) = 1 + a + b = 2 ⇒ a + b = 1.
Same tangent ⇒ same slope at x = 1:
g′(x) = 3x² ⇒ g′(1) = 3.
f′(x) = 2x + a ⇒ f′(1) = 2 + a.
2 + a = 3 ⇒ a = 1; then b = 1 − a = 0.
So f(x) = x² + x, g(x) = x³ + 1. Check: f(1) = 2 ✓, g(1) = 2 ✓, f′(1) = 3 ✓.
Tangent: y − 2 = 3(x − 1) ⇒ y = 3x − 1.
Normal slope = −1/3: y − 2 = −(1/3)(x − 1) ⇒ y = −(1/3)x + 7/3 ⇒ x + 3y = 7 (the same normal line for both curves).

---

## 2.2 Application of Derivative

(p.112)

### Activity 2.15

1. Given a set S = {3, 4, 5, 6, 7} and f(x) = 3x + 2

a. Find K = {f(x) | x ∈ S}.

**Answer:** K = {11, 14, 17, 20, 23}
**Why:**
f(3) = 3(3) + 2 = 11
f(4) = 3(4) + 2 = 14
f(5) = 3(5) + 2 = 17
f(6) = 3(6) + 2 = 20
f(7) = 3(7) + 2 = 23

b. What is the smallest element of K?

**Answer:** 11
**Why:** f is increasing (slope 3 > 0), so the smallest input 3 gives the smallest output f(3) = 11.

c. What is the largest element of K?

**Answer:** 23
**Why:** the largest input 7 gives the largest output f(7) = 23.

2. Given a set S on an open interval (3, 7) and f(x) = 3x + 2

a. Find T = {f(x) | x ∈ S}.

**Answer:** T = (11, 23), the open interval from 11 to 23.
**Why:**
3 < x < 7.
Multiply by 3: 9 < 3x < 21.
Add 2: 11 < 3x + 2 < 23.

b. Can you list all the elements of T?

**Answer:** No.
**Why:** T is an interval of real numbers; it has infinitely many (uncountably many) elements, so they cannot be listed.

c. Can you guess the smallest element of T?

**Answer:** T has no smallest element.
**Why:** 11 is not in T (x = 3 is not in S). Any number in T, say 11 + ε, has a smaller one, 11 + ε/2, still in T. The values approach 11 but never reach it.

d. Can you guess the largest element of T?

**Answer:** T has no largest element.
**Why:** 23 is not in T (x = 7 is not in S); values approach 23 but never reach it.

3. Given a set S as a closed interval [3, 7] and f(x) = 3x + 2

a. Find H = {f(x) | x ∈ S}.

**Answer:** H = [11, 23]
**Why:**
3 ≤ x ≤ 7 ⇒ 9 ≤ 3x ≤ 21 ⇒ 11 ≤ 3x + 2 ≤ 23.

b. Can you list all the elements of H?

**Answer:** No.
**Why:** H is an interval with infinitely many real numbers.

c. Can you guess the smallest element of H?

**Answer:** 11
**Why:** 11 = f(3) and 3 ∈ [3, 7], so the minimum is attained at the left endpoint.

d. Can you guess the largest element of H?

**Answer:** 23
**Why:** 23 = f(7) and 7 ∈ [3, 7], so the maximum is attained at the right endpoint.

Applications of derivatives are varied not only in mathematics but also in real life. To give an example, derivatives have various important applications in mathematics such as finding the rate of change of a quantity, finding the approximate value, finding the equation of the tangent line and the normal line to a curve, and finding the minimum and maximum values of algebraic expressions. Derivatives also has a wide range of applications in real-life usage. For instance, in business, derivatives are used to find profit and loss for the future of the investment using graphs. It is used to calculate the rate of change of distance of a moving body with respect to time. Derivatives can have different interpretations in each of the sciences. For instance; chemists who study a chemical reaction may be interested in the rate of change in the concentration of a reactant with respect to time (the rate of reaction). A biologist is interested in the rate of change of the population of a colony of bacteria with respect to time. In section 2.1, you have studied derivatives and have developed methods to find derivatives of various functions. Once you have developed the properties of the

(p.113)

mathematical concepts once and for all, you can then turn around and apply these results to all of the sciences. You have already investigated some of the applications of derivatives, but now that you know the differentiation rules, you are in a better position to pursue the applications of differentiation in a greater depth.

In this section, you will study problems involving variables that are changing with respect to time. If two or more such variables are related to each other, then their rates of change with respect to time are also related.

### 2.2.1 Applications of Derivatives in Finding Rate of Change

### Example 1

If the radius of a circle is increasing at a rate of 1.5 cm/sec., find the rate at which the area is increasing at the instant when the diameter is 12 cm.

**Solution**

We know that area of a circle with radius r is given by A = πr² and we are given dr/dt = 1.5 cm/sec, to find dA/dt at diameter d = 12 cm.

A = πr² ⇒ dA/dt = π d(r²)/dt = π(2r dr/dt) = 2πr dr/dt

Besides when the diameter d = 12 cm, r = 6 cm.

Hence, dA/dt (6) = 2π(6)(1.5) = 18π cm²/sec.

[added step: 18π ≈ 56.55 cm²/sec.]

### Example 2

An object is moving along the path 3y = x². If the x-coordinate of the object is increasing at a rate of 2 ft/min at the instant when x = 6, find the rate at which the y-coordinate is increasing.

(p.114)

**Solution**

Given 3y = x² and dx/dt = 2 ft/min

3y = x² ⇒ 3 dy/dt = 2x dx/dt ⇔ dy/dt = (2x/3) dx/dt

Thus, at x = 6, dy/dt = (2/3)(6)(2 ft/min) = 8 ft/min

[added step: (2/3)(6) = 4, and 4 × 2 = 8.]

### Example 3

Suppose the side of an equilateral triangle is increasing at a rate of 2 cm/sec. Find the rate at which the area is increasing at the instant when the side is 4 cm.

**Solution**

The area of an equilateral triangle having one side of lenth s is given by A = (√3/4)s²

We are given, ds/dt = 2 cm/sec.

To find dA/dt when s = 4 cm

A = (√3/4)s² ⇒ dA/dt = 2s (√3/4) ds/dt

dA/dt |_{s=4} = 2 × √3/4 = 4√3 cm²/sec

[review: the middle expression printed on p.114 is "2 × √3/4", which equals √3/2, not 4√3. The correct substitution is dA/dt = 2(4)(√3/4)(2) = 4√3 cm²/sec. The book's final answer 4√3 cm²/sec agrees with the working; only the printed middle step is incomplete (s = 4 and ds/dt = 2 are missing).]

### Example 4

Air is being pumped into a spherical balloon at the rate of 4 cm³/min. Find the rate of change of the radius when the radius is 2 cm.

(p.115)

**Solution**

Let r be the radius of the sphere. The volume V of the sphere is given by

V = (4/3)πr³

V = (4/3)πr³ ⇒ dV/dt = 4πr² dr/dt

⇒ dr/dt = (1/(4πr²)) dV/dt = 1/(4π) cm/min.

[added step: substitute r = 2 and dV/dt = 4: dr/dt = 4/(4π(2)²) = 4/(16π) = 1/(4π) ≈ 0.0796 cm/min.]

### Example 5

The displacement of a particle at any time t is given by S = t³ − 3t² + 5t + 7. Find its velocity and acceleration at the end of 2 hrs, where S is in kilometers and t is in hrs.

**Solution**

Given S = t³ − 3t² + 5t + 7

Velocity v = dS/dt = 3t² − 6t + 5

Acceleration a = dv/dt = 6t − 6

Hence, the velocity at the end of 2 hrs is

v(2) = dS/dt |_{t=2hrs} = 3(2)² − 6(2) + 5 = 5 km/hr.

Acceleration at the end of 2 hrs is a = dv/dt = 6(2) − 6 = 6 km/hr².

[added step: 3(4) − 12 + 5 = 12 − 12 + 5 = 5; 12 − 6 = 6.]

### Exercise 2.18

1. A circular plate of metal is being expanded by heating. The radius of plate increases at the rate of 0.3 cm per second. Find the rate of increase of area when its radius becomes 15 cm.

**Answer:** 9π cm²/sec (≈ 28.27 cm²/sec)
**Why:**
Let r = radius (cm), A = area (cm²), t = time (sec). Given dr/dt = 0.3 cm/sec; find dA/dt when r = 15.
A = πr².
Differentiate with respect to t: dA/dt = 2πr dr/dt.
Substitute: dA/dt = 2π(15)(0.3) = 9π cm²/sec ≈ 28.27 cm²/sec.

(p.116)

2. The volume of a sphere is increasing at the rate of 0.2π cm³/sec. Find the rate of increase of radius when the radius is 10 cm.

**Answer:** 1/2000 cm/sec = 0.0005 cm/sec
**Why:**
Given dV/dt = 0.2π cm³/sec; find dr/dt when r = 10.
V = (4/3)πr³.
dV/dt = 4πr² dr/dt.
0.2π = 4π(10)² dr/dt = 400π dr/dt.
dr/dt = 0.2π/(400π) = 0.2/400 = 0.0005 cm/sec.

3. A square plate is being expanded by heating. If its side is increasing at the rate of 0.2 cm per second, then at what rate the area is increasing when the side is 20 cm?

**Answer:** 8 cm²/sec
**Why:**
Let s = side, A = s². Given ds/dt = 0.2 cm/sec; find dA/dt when s = 20.
dA/dt = 2s ds/dt.
dA/dt = 2(20)(0.2) = 8 cm²/sec.

4. A man 2 m tall walks at a uniform speed of 8 m/minute from a lamp post 6 m high. Find the rate at which the length of his shadow increases.

**Answer:** 4 m/minute
**Why:**
Let x = distance of the man from the foot of the lamp post (m), s = length of his shadow (m). Given dx/dt = 8 m/min.
The lamp top, the man's head and the tip of the shadow lie on one line, giving two similar right triangles:
Big triangle: height 6, base x + s. Small triangle: height 2, base s.
6/(x + s) = 2/s.
Cross-multiply: 6s = 2(x + s) = 2x + 2s.
4s = 2x ⇒ s = x/2.
Differentiate: ds/dt = (1/2) dx/dt = (1/2)(8) = 4 m/min.
(The rate is constant: it does not depend on where the man is.)

5. A varying force is applied on a body of unit mass and if the force increases at the rate of 2 N/sec., then find the rate at which the acceleration in the body is changing.

**Answer:** 2 m/s² per second (2 m/s³)
**Why:**
Newton's second law: F = ma, with m = 1 kg.
So a = F/m = F/1 = F.
Differentiate with respect to t: da/dt = (1/m) dF/dt = (1/1)(2) = 2.
Units: N/sec ÷ kg = (m/s²)/s, so the acceleration increases at 2 m/s² per second.

### 2.2.2 Applications of Derivatives in Business and Economics

### Activity 2.16

1. Where do you think we use the concept of derivative other than in mathematics?

**Answer:** (open question) In physics (velocity and acceleration as rates of change of position), chemistry (rate of reaction), biology (population growth rate), economics and business (marginal cost, marginal revenue, marginal profit, maximising profit), engineering (optimal design, minimum material), and road/traffic problems (speed, minimum running cost).
**Why:** A derivative measures how fast one quantity changes with respect to another; any field that studies change or looks for a maximum/minimum uses it (the text on pp.112–113 lists several of these).

2. Is the concept of derivative vital in the study of economics, road taxation and traffic education?

**Answer:** Yes.
**Why:**
Economics: marginal cost, revenue and profit are derivatives, and setting marginal profit = 0 finds the best production level (Examples 1–4 of 2.2.2).
Road taxation: the annual-mileage that minimises the average cost per mile is found by setting a derivative to 0 (Example of 2.2.3).
Traffic: speed is the derivative of distance with respect to time, and acceleration is the derivative of speed.

From this activity, one can see the development of multiple strategies, into which companies incorporate derivatives. Companies, both in and out of the financial industry have begun to use derivatives as a method of speculating and generating income.

### Example 1

The profit function of a company can be represented by P(x) = x − 0.00001x², where x represents units sold. Find the optimal sales volume and the amount of profit to be expected at that volume.

(p.117)

**Solution**

**Marginal profit:** MP = dP/dx = d/dx (x − 0.00001x²) = 1 − 0.00002x.

To get maximum profit now we put marginal profit equals to zero. So, 1 − 0.00002x = 0 ⇒ x = 1/0.00002 = 50,000 units.

Now, to check whether this value is maximum or minimum we can use the first derivative test.

| | x < 50,000 | 50,000 | x > 50,000 |
|---|---|---|---|
| P′(x) = 1 − 0.00002x | ++++ | 0 | −−−− |

From this sign chart the sign of P′(x) changes from positive to negative at x = 50,000. Thus, by the first derivative test, we get maximum profit when the company sold x = 50,000 units of production. Now, by putting the value of x in the profit function we get maximum profit.

P = f(50,000) = 50,000 − 0.00001(50000)²
 = 50,000 − 0.00001(2500,000,000) = 50,000 − 25,000 = 25,000

[added step: (50,000)² = 2,500,000,000 (the book prints "2500,000,000"); 0.00001 × 2,500,000,000 = 25,000. Test values: P′(0) = 1 > 0, P′(100,000) = 1 − 2 = −1 < 0.]

The optimum output for the company will be 50,000 units of x and the maximum profit at that volume will be 25,000 birr.

### Example 2

The demand equation for a certain product is P = 6 − (1/2)x birr, where x represents the amount of product. Find the level of production which results in maximum revenue.

**Solution**

The revenue functionis R(x).

Thus, R(x) = x(6 − (1/2)x) = 6x − (1/2)x² birr.

The marginal revenue is given by R′(x) = 6 − x

(p.118)

The graph of R(x) is a parabola that opens downward as shown in Figure 2.15.

[figure: Figure 2.15 — graph of R(x) = 6x − (1/2)x², revenue R on the vertical axis (0 to 18) against x (0 to 12); a downward-opening parabola starting at (0, 0), rising to the vertex (6, 18), marked with a dashed vertical line at x = 6 and a short horizontal tangent at the top, and falling back to (12, 0).]

It has a horizontal tangent precisely at that x for which R′(x) = 0, that is, for that x at which marginal revenue is 0. The only such value of x is x = 6. The corresponding value of revenue is R(6) = 6(6) − (1/2)(6)² = 18 birr.

[added step: R′(x) = 6 − x = 0 ⇒ x = 6; R(6) = 36 − 18 = 18.]

| | x < 6 | 6 | x > 6 |
|---|---|---|---|
| R′(x) = 6 − x | ++++ | 0 | −−−− |

Thus, by the first derivative test, the rate of production resulting in maximum revenue is x = 6, which results in total revenue of 18 birr.

### Example 3

Promoters of international fund-raising concerts must walk a fine line between profit and loss, especially when determining the price to charge for admission to closed-circuit TV showings in local theatres. By keeping records, a theatre determines that at an admission price of 26 birrs, it averages 1000 people in attendance. For every drop in price of 1 birr, it gains 50 customers. Each customer spends an average of 4 birrs on concessions. What admission price should the theatre charge to maximize total revenue?

(p.119)

**Solution**

Let x be the number of birr by which the price of 26 Birr should be decreased. (If x is negative, the price is increased.) We first express the total revenue R as a function of x. Note that the increase in ticket sales is 50x when the price drops x Birr:

R(x) = (revenue from tickets) + (revenue from concessions)
 = (number of people) · (Ticket price) + (number of people) · 4
 = (1000 + 50x) · (26 − x) + (1000 + 50x) · 4
 = 26,000 − 1000x + 1300x − 50x² + 4000 + 200x
 = −50x² + 500x + 30,000

To find x such that R(x) is a maximum, we first find R′(x):

R′(x) = −100x + 500

This derivative exists for all real numbers x. Thus, the only critical values are where R′(x) = 0; so we solve that equation:

−100x + 500 = 0 ⇒ x = 5

This corresponds to lowering the price by 5 Birr. To determine whether R(x) has a maximum value or not at this critical point we use the first derivative test.

| | x < 5 | 5 | x > 5 |
|---|---|---|---|
| R′(x) = 500 − 100x | ++++ | 0 | −−−− |

Since the sign chart changes from negative to positive at x = 5, by first derivative test, in order to maximize revenue, the theatre should charge 26 Birr − 5 Birr or 21 Birr per ticket.

[review: book says "the sign chart changes from negative to positive at x = 5", but its own sign chart (and the working: R′(0) = 500 > 0, R′(10) = −500 < 0) shows R′ changes from positive to negative, which is what gives a maximum. A change from negative to positive would give a minimum. The conclusion (charge 21 Birr) is correct.]

[added step: maximum revenue R(5) = −50(25) + 500(5) + 30,000 = −1250 + 2500 + 30,000 = 31,250 Birr; check: 1250 people × (21 + 4) Birr = 31,250 Birr.]

### Example 4

For a company, the total revenue R and the total cost C for yard maintenance of x homes are given by R(x) = 1000x − x², and C(x) = 3000 + 20x.

Suppose that the company is adding 10 homes per day at the moment when the 400th customer is signed. At that moment, what is the rate of change of

a. total revenue?  b. total cost?  c. total profit?

(p.120)

**Solution**

a. dR/dt = (dR/dx)(dx/dt) = (1000 − 2x) dx/dt

dR/dt |_{x=400} = (1000 − 2 × 400)(10) = 2000 birr per day.

b. dC/dt = (dC/dx)(dx/dt) = (20) dx/dt = 20 × 10 = 200 birr per day.

c. Since p(x) = R(x) − C(x), we have

dp/dt = dR/dt − dC/dt = 2000 birr per day − 200 birr per day
 = 1800 birr per day.

[added step: in (a), 1000 − 800 = 200 and 200 × 10 = 2000.]

### Exercise 2.19

Given C(x) = 62x² + 27,500 and R(x) = x³ − 12x² + 40x + 10 where C(x) and R(x) represent, respectively, the total cost and revenue from the production and sale of x items. Find each of the following:

a. Total profit, P(x).

**Answer:** P(x) = x³ − 74x² + 40x − 27,490
**Why:**
P(x) = R(x) − C(x)
= (x³ − 12x² + 40x + 10) − (62x² + 27,500)
= x³ − 12x² − 62x² + 40x + 10 − 27,500
= x³ − 74x² + 40x − 27,490

b. Total cost, revenue, and profit from the production and sale of 50 units of the product.

**Answer:** C(50) = 182,500; R(50) = 97,010; P(50) = −85,490 (a loss of 85,490).
**Why:**
C(50) = 62(50)² + 27,500 = 62(2500) + 27,500 = 155,000 + 27,500 = 182,500.
R(50) = 50³ − 12(50)² + 40(50) + 10 = 125,000 − 30,000 + 2,000 + 10 = 97,010.
P(50) = R(50) − C(50) = 97,010 − 182,500 = −85,490.
Check with the formula from (a): 125,000 − 74(2500) + 2,000 − 27,490 = 125,000 − 185,000 + 2,000 − 27,490 = −85,490 ✓.

c. The marginal cost, revenue, and profit when 50 units are produced and sold.

**Answer:** C′(50) = 6200; R′(50) = 6340; P′(50) = 140.
**Why:**
C′(x) = 124x ⇒ C′(50) = 124(50) = 6200.
R′(x) = 3x² − 24x + 40 ⇒ R′(50) = 3(2500) − 24(50) + 40 = 7500 − 1200 + 40 = 6340.
P′(x) = 3x² − 148x + 40 ⇒ P′(50) = 7500 − 7400 + 40 = 140.
Check: P′(50) = R′(50) − C′(50) = 6340 − 6200 = 140 ✓.
(Meaning: producing the 51st item adds about 140 to profit, even though total profit is still negative.)

(p.121)

### 2.2.3 Application of Derivative in Road Taxation

### Example

A motorist has to pay an annual road tax of 50 birrs and 110 birrs for insurance. His car does 30 miles to the gallon which costs 75 pence (per gallon). The car is serviced every 3000 miles for 20 birrs, and depreciation is calculated in pence by multiplying the square of the mileage by 0.001. Obtain an expression for the total annual cost of running the car. Hence find an expression for the average total cost per mile and calculate the annual mileage which will minimize the average cost per mile.

**Solution**

Suppose he covers x miles in a year.

Tax per annum = 50 birrs; Insurance per annum = 110 birrs;

Cost of petrol = 0.75x/30; service charge = 20x/3000; depreciation = 0.001x²/100 (0.001 is in pence and is divided by 100 to get the amount in birr).

[added step: x miles need x/30 gallons; at 75 pence = 0.75 (in birr, taking 100 pence = 1 birr as the book does) per gallon the petrol costs 0.75x/30. The car is serviced x/3000 times, each costing 20, so service = 20x/3000. Depreciation = 0.001x² pence = 0.001x²/100 = 0.00001x².]

Total cost (TC): C = 50 + 110 + (0.75x/30) + 20x/3000 + 0.00001x²

Average total cost (TC) per mile: C/x = M = 160/x + 0.75/30 + 20/3000 + 0.00001x

dM/dx = 0

⇒ −160/x² + 0.00001 = 0

⇔ 0.00001x² = 160

⇔ x² = 160/0.00001 = 16,000,000

⇔ x = ±4,000

[added step: dividing each term of C by x: 160/x, 0.75/30 = 0.025, 20/3000 ≈ 0.00667 and 0.00001x. The two constant terms have derivative 0, d/dx(160/x) = −160/x², d/dx(0.00001x) = 0.00001. Mileage cannot be negative, so x = −4000 is rejected and x = 4000.]

Now, to check whether this critical number (x = 4000) gives a maximum or minimum cost, we can use a sign chart and apply the first derivative test.

(p.122)

| | x < −4000 | −4000 | −4000 < x < 4000 | 4000 | x > 4000 |
|---|---|---|---|---|---|
| x − 4000 | −−−− | | −−−− | 0 | ++++ |
| x + 4000 | −−−− | 0 | ++++ | | ++++ |
| x² − 16,000,000 | +++ | | −−−− | | ++++ |

[added step: dM/dx = −160/x² + 0.00001 = (0.00001x² − 160)/x² = 0.00001(x² − 16,000,000)/x² = 0.00001(x − 4000)(x + 4000)/x². Since x² > 0, dM/dx has the same sign as x² − 16,000,000, which is the last row of the chart. (x = 0 is excluded from the domain of M.)]

From the sign chart, we see that the sign of the derivative changes from negative to positive at x = 4000. So, the motorist can cover 4000 miles in a year to minimize the average cost per mile.

[added step: second-derivative check: M″(x) = 320/x³ > 0 at x = 4000, so it is a minimum. The minimum average cost is M(4000) = 160/4000 + 0.025 + 0.00667 + 0.04 ≈ 0.1117 birr per mile.]

### Exercise 2.20

1. A rectangular area of 3200 ft² is to be fenced off. Two opposite sides will use fencing costing 1 dollar per foot and the remaining sides will use fencing costing 2 dollars per foot. Find the dimensions of the rectangle of the least cost.

**Answer:** 80 ft (the two sides with $1/ft fencing) by 40 ft (the two sides with $2/ft fencing); least cost $320.
**Why:**
Let x = length (ft) of each of the two sides fenced at $1/ft, and y = length (ft) of each of the two sides fenced at $2/ft.
Area: xy = 3200 ⇒ y = 3200/x.
Cost: C = 1·(2x) + 2·(2y) = 2x + 4y = 2x + 4(3200/x) = 2x + 12,800/x, x > 0.
C′(x) = 2 − 12,800/x².
C′(x) = 0 ⇒ 2 = 12,800/x² ⇒ x² = 6400 ⇒ x = 80 (x > 0).
y = 3200/80 = 40.
Sign chart of C′(x) = 2(x² − 6400)/x² = 2(x − 80)(x + 80)/x²:

| | 0 < x < 80 | 80 | x > 80 |
|---|---|---|---|
| C′(x) | −−−− | 0 | ++++ |

C′ changes from − to + ⇒ minimum. (Also C″(x) = 25,600/x³ > 0.)
C(80) = 160 + 12,800/80 = 160 + 160 = $320.

2. A manufacturer wants to design an open box that has a square base and a surface area of 48 square unit. What dimensions will produce a box with a maximum volume?

**Answer:** Base 4 units by 4 units, height 2 units (maximum volume 32 cubic units).
**Why:**
Let x = side of the square base, h = height.
Open box (no top): surface area = base + 4 sides = x² + 4xh = 48.
h = (48 − x²)/(4x), with 0 < x < √48.
V = x²h = x²(48 − x²)/(4x) = (48x − x³)/4 = 12x − x³/4.
V′(x) = 12 − (3/4)x².
V′(x) = 0 ⇒ (3/4)x² = 12 ⇒ x² = 16 ⇒ x = 4 (x > 0).
Sign chart of V′(x) = (3/4)(16 − x²) = (3/4)(4 − x)(4 + x):

| | 0 < x < 4 | 4 | 4 < x < √48 |
|---|---|---|---|
| V′(x) | ++++ | 0 | −−−− |

V′ changes from + to − ⇒ maximum. (Also V″(x) = −(3/2)x = −6 < 0 at x = 4.)
h = (48 − 16)/(4·4) = 32/16 = 2.
V = 4²·2 = 32 cubic units.
Check surface: 16 + 4(4)(2) = 16 + 32 = 48 ✓.

3. A closed cylindrical can having a volume of 128π cm³ is to be formed. Find the dimensions (the radius and height) of the cylinder that will minimize the amount of material to be used?

**Answer:** Radius 4 cm, height 8 cm (minimum surface area 96π cm²).
**Why:**
Let r = radius, h = height (cm). Material = total surface area S (closed: top + bottom + side).
Volume: πr²h = 128π ⇒ h = 128/r².
S = 2πr² + 2πrh = 2πr² + 2πr(128/r²) = 2πr² + 256π/r, r > 0.
S′(r) = 4πr − 256π/r².
S′(r) = 0 ⇒ 4πr = 256π/r² ⇒ 4r³ = 256 ⇒ r³ = 64 ⇒ r = 4.
Sign chart of S′(r) = 4π(r³ − 64)/r²:

| | 0 < r < 4 | 4 | r > 4 |
|---|---|---|---|
| S′(r) | −−−− | 0 | ++++ |

S′ changes from − to + ⇒ minimum. (Also S″(r) = 4π + 512π/r³ > 0.)
h = 128/4² = 128/16 = 8 cm (height = diameter).
S = 2π(16) + 256π/4 = 32π + 64π = 96π cm².
Check volume: π(16)(8) = 128π ✓.

---

## 2.3 Introduction to Integration

(p.123)

### Activity 2.17

1. Is it possible to determine the distance a vehicle has traveled if we know its velocity function?

**Answer:** Yes.
**Why:** Velocity is the rate of change of distance. Over a time interval, the distance travelled is the area under the velocity–time graph (for v ≥ 0), i.e. we "undo" differentiation. Example 1 of 2.3.1 shows this for constant velocity: distance = velocity × time = area of a rectangle.

2. Can we determine a company's total profit if we know its marginal-profit function?

**Answer:** Yes.
**Why:** Marginal profit P′(x) is the rate of change of profit. The total profit over an interval is the area under the graph of P′(x) (an antiderivative of P′), as in Exercise 2.21 Q2. (To get the exact profit function we also need one known value, e.g. the profit at x = 0.)

3. An object moves with a velocity of v(t) = (1/2)t, where t is in minutes and v is in feet per minute.

a) How far does the object travel during the first 30 min?

**Answer:** 225 feet
**Why:**
The distance is the area under v(t) = (1/2)t from t = 0 to t = 30.
The region is a triangle with base 30 and height v(30) = 15.
Area = (1/2)(30)(15) = 225 ft.
(Check with an antiderivative: s(t) = t²/4; s(30) − s(0) = 900/4 = 225.)

b) How far does the object travel between the first hour and the second hour?

**Answer:** 2700 feet
**Why:**
First hour: t = 60 min; second hour: t = 120 min.
v(60) = 30 ft/min, v(120) = 60 ft/min.
The region under v from t = 60 to t = 120 is a trapezoid with parallel sides 30 and 60 and width 60.
Area = (1/2)(30 + 60)(60) = (1/2)(90)(60) = 2700 ft.
(Check: s(120) − s(60) = 14400/4 − 3600/4 = 3600 − 900 = 2700.)

4. Find the areas of the region below y = 2x and above the x-axis shown in the figure 2.16 (a) below.

[figure: Figure 2.16 (a) — the line y = 2x through the origin, with rectangles under it ending at x = 6; the top-left corner of each rectangle touches the line (lower / inscribed rectangles), so the rectangles lie below the line.]
[figure: Figure 2.16 (b) — the same line y = 2x, with rectangles ending at x = 6 whose top-right corner touches the line (upper / circumscribed rectangles), so the rectangles stick out above the line.]

[review: Figure 2.16 is schematic. The rectangles are drawn only over part of [0, 6] (about x = 2 to 6, five rectangles in (a) and five in (b)) and their widths look unequal, so the number of subintervals cannot be read reliably. The answers below use an equal partition of [0, 6] into n = 6 subintervals of width 1, and give the general formula too.]

**Answer:** Lower sum (inscribed rectangles, n = 6): 30 square units. (In general, with n equal subintervals, the lower sum is 36 − 36/n.)
**Why:**
Partition [0, 6] into 6 parts: Δx = (6 − 0)/6 = 1, points 0, 1, 2, 3, 4, 5, 6.
Inscribed rectangles use the left endpoint (the smaller height, since y = 2x is increasing): heights 2(0), 2(1), 2(2), 2(3), 2(4), 2(5) = 0, 2, 4, 6, 8, 10.
Lower sum = (0 + 2 + 4 + 6 + 8 + 10)(1) = 30.
General n: Δx = 6/n, heights 2(6i/n) for i = 0, …, n − 1; sum = (72/n²)(0 + 1 + … + (n − 1)) = (72/n²)(n(n − 1)/2) = 36(n − 1)/n = 36 − 36/n.

5. Find the area of the region below the line y = 2x shown in the fig 2.16 (b). Upper sum on the interval [0, 6], with equal partition of [0, 6].

**Answer:** Upper sum (n = 6): 42 square units. (In general 36 + 36/n.)
**Why:**
Same partition, Δx = 1.
Circumscribed rectangles use the right endpoint (the larger height): heights 2(1), 2(2), …, 2(6) = 2, 4, 6, 8, 10, 12.
Upper sum = (2 + 4 + 6 + 8 + 10 + 12)(1) = 42.
General n: (72/n²)(1 + 2 + … + n) = (72/n²)(n(n + 1)/2) = 36(n + 1)/n = 36 + 36/n.

6. Find the area of the region just below the line y = 2x over the interval [0, 6].)

**Answer:** 36 square units
**Why:**
The region under y = 2x from x = 0 to x = 6 is a right triangle with base 6 and height 2(6) = 12.
Area = (1/2)(6)(12) = 36.

7. Compare the values of 4 up to 6 above.

**Answer:** Lower sum ≤ exact area ≤ upper sum: 30 < 36 < 42. As the number of subintervals n increases, both sums get closer to 36 (36 − 36/n → 36 and 36 + 36/n → 36).
**Why:**
Inscribed rectangles miss small triangles above them, so the lower sum is too small; circumscribed rectangles include extra triangles, so the upper sum is too big.
The error in each is 36/n, which tends to 0 as n → ∞. This leads to the idea of the definite integral.

(p.124)

### 2.3.1 Areas of Regions

Integral calculus is primarily concerned with the area below the graph of a function (specifically, the area between the graph of a function and the x-axis). In this section, we assume that all functions are non-negative; that is, f(x) ≥ 0.

### Example 1

A vehicle travels 50 mi/hr for 2 hr. How far has the vehicle traveled?

**Solution**

The answer is 100 miles. We treat the vehicle's velocity as a function, v(x) = 50. We graph this function, sketch a vertical line at x = 2, and obtain a rectangle. This rectangle measures 2 units horizontally and 50 units vertically. Its area is the distance the vehicle has traveled:

v(t) = 50

Distance A = 2 × 50 = 100

2 hr × (50 miles)/(1 hr) = 100 miles.

[figure: Figure 2.17 — horizontal line v = 50 on a v–t graph; the region under it from t = 0 to t = 2 is a shaded rectangle of width 2 and height 50.]

### Example 2

Green Leaf Skateboards determines that for the first 50 skateboards produced, its cost is 40 birr per skateboard. What is the total cost to produce 50 skateboards?

(p.125)

**Solution**

The marginal-cost function is C′(x) = 40, 0 ≤ x ≤ 50. Its graph is a horizontal line. If we mark off 50 units along the x-axis, we get a rectangle, as in Example 1.

The area of this rectangle is 40 × 50 = 2000. Therefore, the total cost to produce 50 skateboards is 2000 birr:

(50 skateboards × 40 Birr/skateboard = 2000 Birr).

[figure: Figure 2.18 — horizontal line C′(x) = 40 (cost in Birr on the vertical axis, number of skateboards on the horizontal axis); shaded rectangle from x = 0 to x = 50 with height 40.]

### Example 3

The velocity of a moving object is given by the function v(x) = 3x, where x is in hours and v is in miles per hour. Use geometry to find the area under the graph, which is the distance the object has traveled during the first 3 hours (0 ≤ x ≤ 3).

[figure: Figure 2.19 — line v(x) = 3x through the origin (velocity in miles/hour, 0 to 15, against time in hours, 0 to 5); the region under the line from x = 0 to x = 3 is a shaded triangle reaching height 9 at x = 3.]

(p.126)

**Solution**

The graph of the velocity function is shown above. We see the region corresponding to the time interval 0 ≤ x ≤ 3 is a triangle with base 3 and height 9 (since v(3) = 9).

Therefore, the area of this region is A = (1/2)(3)(9) = 27/2 = 13.5.

The object that traveled 13.5 miles during the first 3 hours.

In each of the Examples 1 through 3, the function was a rate function; its output units formed a rate (miles per hour in Examples 1 and 3, Birr per skateboard in Example 2). The units of the area were derived by multiplying input units by output units.

### Exercise 2.21

1. The velocity of a moving object is given by the function v(x) = 3x, where x is in hours and v is in miles per hour. Use geometry to find the area under the graph, which is the distance the object has traveled between the third hour and the fifth hour (3 ≤ x ≤ 5).

**Answer:** 24 miles
**Why:**
v(3) = 3(3) = 9 mi/hr; v(5) = 3(5) = 15 mi/hr.
The region under v(x) = 3x from x = 3 to x = 5 is a trapezoid with parallel sides 9 and 15 and width 5 − 3 = 2.
Area = (1/2)(9 + 15)(2) = (1/2)(24)(2) = 24.
Units: hours × miles/hour = miles.
(Check: big triangle (1/2)(5)(15) = 37.5 minus small triangle (1/2)(3)(9) = 13.5 gives 24 ✓.)

2. A company has a marginal profit function modeled by the linear function P′(x) = 0.15x, where x is in months and P′ is in thousands of dollars per month. Sketch this graph and use it to determine the total profit earned by the company in a year (0 ≤ x ≤ 12).

**Answer:** 10.8 thousand dollars = $10,800
**Why:**
Sketch: P′(x) = 0.15x is a straight line through the origin with slope 0.15; at x = 12, P′(12) = 0.15(12) = 1.8.
[figure: line P′(x) = 0.15x from (0, 0) to (12, 1.8); region under it is a triangle.]
The region under the graph from x = 0 to x = 12 is a triangle with base 12 and height 1.8.
Area = (1/2)(12)(1.8) = 10.8.
Units: months × thousands of dollars per month = thousands of dollars ⇒ $10,800.

(p.127)

### Riemann summation

### Activity 2.18

1. Examples 1 through 3 in this section suggest a pattern:

✓ If f(x) = k, where k is a non-negative constant, its graph is a horizontal line of height k. The region under this graph over the interval [0, x] is a rectangle, and its area is A = k.x (height times base).

✓ If f(x) = mx, its graph is a line of slope m ≥ 0, passing through the origin. The region under this graph over an interval [0, x] is a triangle, and its area is A = (1/2)(x)(mx) = (1/2)mx².

[figure: Figure 2.20 — horizontal line f(x) = k; the shaded rectangle from 0 to x has height k and area A(x) = kx; corner point (x, k).]
[figure: Figure 2.21 — line f(x) = mx through the origin; the shaded triangle from 0 to x has height mx and area A(x) = (1/2)mx²; corner point (x, mx).]

In these two cases, the area function is an anti-derivative of the function that generated the graph.

a. Is this always true?

**Answer:** Yes, for a continuous function f: the area function A(x) (area under f from a fixed starting point to x) always satisfies A′(x) = f(x), so A is an anti-derivative of f.
**Why:**
Check the two cases: A(x) = kx ⇒ A′(x) = k = f(x); A(x) = (1/2)mx² ⇒ A′(x) = mx = f(x).
In general, increasing x by a small h adds a thin strip of width h and height about f(x), so A(x + h) − A(x) ≈ f(x)·h, and (A(x + h) − A(x))/h → f(x) as h → 0. (This is the idea behind the Fundamental Theorem of Calculus, studied later.)

b. Is the formula for the area under the graph of any function that function's anti-derivative?

**Answer:** Yes, up to a constant: the area from a to x is the anti-derivative F with F(a) = 0; the area from a to b is F(b) − F(a) for any anti-derivative F.
**Why:**
Anti-derivatives of f differ only by a constant (Activity 2.20), so we choose the one that gives area 0 at the starting point. E.g. for f(x) = mx from 0: F(x) = (1/2)mx² + C with F(0) = 0 ⇒ C = 0.

c. How do we handle curved graphs for which area formulas may not be known?

**Answer:** Approximate the region with many thin rectangles, add their areas (a Riemann sum), and let the number of rectangles grow without bound (width → 0); the limit is the exact area (the definite integral).
**Why:** This is exactly the method developed in the rest of 2.3.1 and 2.3.2 (Figures 2.23–2.25, Definition 2.12, Definition 2.13).

2. Write summation notation for

i) 5 + 10 + 15 + 20 + 25

**Answer:** Σ_{i=1}^{5} 5i
**Why:**
Each term is 5 times its position: 5(1), 5(2), 5(3), 5(4), 5(5).
So the sum is Σ_{i=1}^{5} 5i (= 75).

ii) g(x₁)Δx + g(x₂)Δx + … + g(x₁₉)Δx.

**Answer:** Σ_{i=1}^{19} g(xᵢ)Δx
**Why:** The i-th term is g(xᵢ)Δx, and i runs from 1 to 19.

(p.128)

### Example 1

A Skateboard has the following marginal-cost function for producing skateboards: For up to 50 skateboards, the cost is 40 ETB per skateboard. For quantities from 51 through 125 skateboards, the cost drops to 30 ETB per skateboard. After 125 skateboards, it drops to 25 ETB per skateboard. If x represents the number of skateboards produced, the marginal cost function C′ is

C′(x) = 40, for 0 ≤ x ≤ 50,
 30, for 50 < x ≤ 125,
 25, for 125 < x ≤ 150.

Find the total cost to produce 150 skateboards.

**Solution**

We are extending Example 2. We calculate the areas of the rectangles formed by the horizontal lines of the graph of the marginal-cost function:

[figure: Figure 2.22 — step graph of C′(x) (cost per skateboard in Birr against number of skateboards produced): height 40 from x = 0 to 50, height 30 from 50 to 125, height 25 from 125 to 150; the three rectangles under the steps are shaded, with dashed lines at x = 50 and x = 125.]

The total cost to produce 150 skateboards is found by summing those areas:

Total cost = (40)(50) + (30)(75) + (25)(25) = 4875 Birr.

[added step: widths are 50 − 0 = 50, 125 − 50 = 75 and 150 − 125 = 25; areas 2000 + 2250 + 625 = 4875.]

(p.129)

Example 1 illustrates the first steps of a Riemann summation, a method that allows us to determine the area under a curved graph. We use rectangles to approximate the area under a curve given by y = f(x), a continuous function, over an interval [a, b]. Riemann summation is accomplished with the use of summation notation, introduced below. In Figure 2.23, [a, b] is divided into four subintervals, each having width Δx = (b − a)/4.

[figure: Figure 2.23 — a curve f over [a, b] with four rectangles of equal width Δx; the left ends of the subintervals are a = x₁, x₂, x₃, x₄; each rectangle's height is the value of f at the left endpoint, f(x₁), f(x₂), f(x₃), f(x₄) (red dots on the curve at the top-left corners).]

The heights of the rectangles shown are

f(x₁), f(x₂), f(x₃) and f(x₄).

The area of the region under the curve is approximately the sum of the areas of the four rectangles:

f(x₁)Δx + f(x₂)Δx + f(x₃)Δx + f(x₄)Δx

We can denote this sum with summation notation, or sigma notation, which uses the Greek capital letter sigma, Σ:

Σ_{i=1}^{4} f(xᵢ)Δx

This is read "the sum of the product f(xᵢ)Δx from i = 1 to i = 4."

Before we continue, let's consider some examples involving summation notation.

(p.130)

### Example 2

Find the sum of expression Σ_{i=1}^{4} 3ⁱ.

**Solution**

Σ_{i=1}^{4} 3ⁱ = 3¹ + 3² + 3³ + 3⁴ = 120.

[added step: 3 + 9 + 27 + 81 = 120.]

### Example 3

Express Σ_{i=1}^{30} h(xᵢ)Δx without using summation notation.

**Solution**

Σ_{i=1}^{30} h(xᵢ)Δx = h(x₁)Δx + h(x₂)Δx + … + h(x₃₀)Δx.

Approximation of area by rectangles becomes more accurate as we use smaller subintervals and hence more rectangles, as shown in the following figures.

[figure: Figure 2.24a — the same curve f over [a, b] approximated by 8 rectangles (a = x₁, x₂, …, x₈, b), heights at left endpoints, f(x₃) marked; visible gaps and overlaps between rectangles and curve.]
[figure: Figure 2.24b — the same curve approximated by 24 thin rectangles (a = x₁, …, x₂₄, b); the rectangles follow the curve much more closely.]

In general, suppose that the interval [a, b] is divided into n equally sized subintervals, each of width Δx = (b − a)/n and we then construct rectangles with heights f(x₁), f(x₂), …, f(xₙ).

(p.131)

[figure: Figure 2.25 — the curve f over [a, b] with n rectangles of width Δx at a = x₁, x₂, x₃, x₄, x₅, …, xₙ, b; the middle rectangles are replaced by "…".]

The width of each rectangle is Δx, so the first rectangle has an area of f(x₁)Δx, the second rectangle has an area of f(x₂)Δx, and so on. The area of the region under the curve is approximated by the sum of the areas of the rectangles Aₙ:

Area(Aₙ) = Σ_{i=1}^{n} f(xᵢ)Δx.

### Definition 2.12

Let p = {x₀, x₁, x₂, …, xₙ} be any partition on [a, b] of a given function f. For each k between 1 and n, let tₖ be an arbitrary number in [xₖ₋₁, xₖ]. Then the sum

f(t₁)Δx₁ + f(t₂)Δx₂ + f(t₃)Δx₃ + … + f(tₙ)Δxₙ

is called **a Riemann sum for** f on [a, b] and is denoted

Σ_{k=1}^{n} f(tₖ)Δxₖ.

Thus, Σ_{k=1}^{n} f(tₖ)Δxₖ = f(t₁)Δx₁ + f(t₂)Δx₂ + f(t₃)Δx₃ + … + f(tₙ)Δxₙ

[added step: here Δxₖ = xₖ − xₖ₋₁ is the width of the k-th subinterval, and a = x₀ < x₁ < … < xₙ = b. Note that Definition 2.12 numbers the partition points from x₀, while Figures 2.23–2.25 label the left endpoints from x₁.]

Riemann sum (pronounced "Ree-mahn") was developed by the great German mathematician G. F. Bernhard Riemann (1826–1866). Riemann sums can be calculated using any x-value within each subinterval. For simplicity, in this text, we will always use the left endpoint of each subinterval.

(p.132)

**Steps for the Process of Riemann Summation**

1. Draw the graph of f(x).
2. Subdivide the interval [a, b] into n subintervals of equal width. Calculate the width of each rectangle by using the formula Δx = (b − a)/n.
3. Construct rectangles above the subintervals such that the top left corner of each rectangle touches the graph.
4. Determine the area of each rectangle.
5. Sum these areas to arrive at an approximation for the total area under the curve.

### Exercise 2.22

1. Find the approximate area of the region enclosed by the graph of function f(x) = x² + 1, the x-axis, x = 1 and x = 5.

a. Use the following steps to find it.

Step 1: Interval [1, 5] is divided into four subintervals, each having width Δx = (5 − 1)/4 = 1

[figure: Figure 2.26 — graph of y = x² + 1 on a grid with x from 0 to 5; four shaded rectangles A₁, A₂, A₃, A₄ on [1, 2], [2, 3], [3, 4], [4, 5], each with height equal to f at its left endpoint x₁ = 1, x₂ = 2, x₃ = 3, x₄ = 4 (heights f(x₁), f(x₂), f(x₃), f(x₄) marked on the y-axis).]

(p.133)

Step 2: Find the values of f(x₁), f(x₂), f(x₃) and f(x₄), when x₁ = 1, x₂ = 2, x₃ = 3 and x₄ = 4.

Step 3: Since the area of the region is approximatily the sum of the areas of four rectangles A₁, A₂, A₃ and A₄, calculate A₁ + A₂ + A₃ + A₄ = Σ_{i=1}^{4} f(xᵢ)Δx.

**Answer:** Approximately 34 square units.
**Why:**
Step 1: Δx = (5 − 1)/4 = 1; left endpoints 1, 2, 3, 4.
Step 2:
f(1) = 1² + 1 = 2
f(2) = 2² + 1 = 5
f(3) = 3² + 1 = 10
f(4) = 4² + 1 = 17
Step 3:
A₁ = 2(1) = 2, A₂ = 5(1) = 5, A₃ = 10(1) = 10, A₄ = 17(1) = 17.
A₁ + A₂ + A₃ + A₄ = 2 + 5 + 10 + 17 = 34.
(Comparison: the exact area is ∫_{1}^{5} (x² + 1) dx = [x³/3 + x] from 1 to 5 = (125/3 + 5) − (1/3 + 1) = 124/3 + 4 = 136/3 ≈ 45.33. The left-endpoint sum is too small because f is increasing on [1, 5].)

b. Find the approximate area of the same region in the same way as a, when the interval [1, 5] is divided into eight subintervals, each having width Δx = (5 − 1)/8 = 0.5.

**Answer:** Approximately 39.5 square units.
**Why:**
Δx = 0.5; left endpoints 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5.
f(1) = 2
f(1.5) = 2.25 + 1 = 3.25
f(2) = 5
f(2.5) = 6.25 + 1 = 7.25
f(3) = 10
f(3.5) = 12.25 + 1 = 13.25
f(4) = 17
f(4.5) = 20.25 + 1 = 21.25
Sum of heights = 2 + 3.25 + 5 + 7.25 + 10 + 13.25 + 17 + 21.25 = 79.
Area ≈ 79 × 0.5 = 39.5.
(Closer to the exact 136/3 ≈ 45.33 than the 4-rectangle value 34, as expected with more rectangles.)

2. Express Σ_{i=1}^{6} (i² + i) without using summation notation

**Answer:** (1² + 1) + (2² + 2) + (3² + 3) + (4² + 4) + (5² + 5) + (6² + 6) = 2 + 6 + 12 + 20 + 30 + 42 (= 112)
**Why:**
Substitute i = 1, 2, …, 6 into i² + i and add:
i = 1: 1 + 1 = 2
i = 2: 4 + 2 = 6
i = 3: 9 + 3 = 12
i = 4: 16 + 4 = 20
i = 5: 25 + 5 = 30
i = 6: 36 + 6 = 42
Total = 2 + 6 + 12 + 20 + 30 + 42 = 112.

### 2.3.2 Definite Integrals

### Activity 2.19

Let f(x) = 3x² defined on the interval [0, 5]. Then, find the Riemann sum of f on [0, 5]

a. By dividing the interval [0, 5] in to 5 sub-intervals of equal width.

**Answer:** 90 (using left endpoints, as the book does)
**Why:**
Δx = (5 − 0)/5 = 1; left endpoints 0, 1, 2, 3, 4.
f(0) = 0, f(1) = 3, f(2) = 12, f(3) = 27, f(4) = 48.
Riemann sum = (0 + 3 + 12 + 27 + 48)(1) = 90.
(With right endpoints 1, …, 5: 3(1 + 4 + 9 + 16 + 25) = 165.)

b. By dividing the interval [0, 5] in to 10 sub-intervals of equal width.

**Answer:** 106.875 (left endpoints)
**Why:**
Δx = (5 − 0)/10 = 0.5; left endpoints 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5.
f values (3x²): 0, 0.75, 3, 6.75, 12, 18.75, 27, 36.75, 48, 60.75.
Sum of heights = 0 + 0.75 + 3 + 6.75 + 12 + 18.75 + 27 + 36.75 + 48 + 60.75 = 213.75.
Riemann sum = 213.75 × 0.5 = 106.875.
(With right endpoints: 144.375. The exact area is ∫_{0}^{5} 3x² dx = [x³] from 0 to 5 = 125; both sums move toward 125 as n increases: left 90 → 106.875, right 165 → 144.375.)

The key concept developed in this section is that the more subintervals we use, the more accurate the approximation of area becomes. As the number of subdivisions dx = (b − a)/n increases, the width of each rectangle Δx decreases. If n is allowed to approach infinity, then Δx approaches 0; these are limits, and the approximations of the area becomes closer and closer to the true area under the graph. The exact area underneath the graph of a continuous function y = f(x) over an interval [a, b] is, by definition, given by a definite integral.

[review: p.133 prints "As the number of subdivisions dx = (b − a)/n increases"; the phrase is garbled — it is the number of subdivisions n that increases, which makes the width dx = Δx = (b − a)/n decrease. Transcribed as printed.]

(p.134)

### Definition 2.13

Let a given piecewice contionous function y = f(x) be non-negative, f(x) ≥ 0, over an interval [a, b]. **A definite integral** is the Riemann sum of the areas of the rectangles under the graph of the function y = f(x) over the interval [a, b] as the value of n increases indefinitely (equivalently, dx = (b − a)/n approaches very close to 0). That is:

Exact area = Σ_{i=1}^{n} f(xᵢ)Δx = ∫_{a}^{b} f(x) dx, as Δx gets very close to 0.

[added step: in limit notation, ∫_{a}^{b} f(x) dx = lim_{n→∞} Σ_{i=1}^{n} f(xᵢ)Δx, with Δx = (b − a)/n. "piecewice contionous" is the book's spelling of "piecewise continuous".]

Notice that the summation symbol becomes an integral sign (the elongated "s" is Leibniz notation representing "sum") and Δx becomes dx. If f(x) ≥ 0 over an interval [a, b], the definite integral represents the area.

### Example

Determine the value of ∫_{0}^{2} (3x + 2) dx.

**Solution**

This definite integral is a command to calculate the exact area underneath the graph of the function f(x) = 3x + 2 over the interval [0, 2].

We sketch the graph and note that the region is a trapezoid. Thus, we can use geometry to determine this area (a Riemann sum is not needed here).

[figure: Figure 2.27 — line f(x) = 3x + 2 from (0, 2) to (2, 8); the region under it over [0, 2] is a shaded trapezoid.]

We find that the area is 10. Therefore, ∫_{0}^{2} (3x + 2) dx = 10.

[added step: f(0) = 2 and f(2) = 3(2) + 2 = 8; the trapezoid has parallel sides 2 and 8 and width 2, so area = (1/2)(2 + 8)(2) = 10.]

(p.135)

### Exercise 2.23

Derermine the values of the following definite integrals:

a. ∫_{0}^{2} (2x + 1) dx

**Answer:** 6
**Why:**
f(x) = 2x + 1 ≥ 0 on [0, 2], so the integral is the area under the line.
f(0) = 1, f(2) = 5.
The region is a trapezoid with parallel sides 1 and 5 and width 2.
Area = (1/2)(1 + 5)(2) = 6.
(Check with an antiderivative: F(x) = x² + x, F′(x) = 2x + 1 ✓; F(2) − F(0) = (4 + 2) − 0 = 6.)

b. ∫_{0}^{4} 2x dx

**Answer:** 16
**Why:**
f(0) = 0, f(4) = 8.
The region is a triangle with base 4 and height 8.
Area = (1/2)(4)(8) = 16.
(Check: F(x) = x², F(4) − F(0) = 16.)

c. ∫_{1}^{5} x dx

**Answer:** 12
**Why:**
f(1) = 1, f(5) = 5.
The region is a trapezoid with parallel sides 1 and 5 and width 5 − 1 = 4.
Area = (1/2)(1 + 5)(4) = 12.
(Check: F(x) = x²/2, F(5) − F(1) = 25/2 − 1/2 = 12.)

d. ∫_{−2}^{3} (x + 2) dx

**Answer:** 25/2 = 12.5
**Why:**
f(x) = x + 2 ≥ 0 on [−2, 3]; f(−2) = 0, f(3) = 5.
The region is a triangle with base 3 − (−2) = 5 and height 5.
Area = (1/2)(5)(5) = 12.5.
(Check: F(x) = x²/2 + 2x; F(3) = 4.5 + 6 = 10.5; F(−2) = 2 − 4 = −2; F(3) − F(−2) = 12.5.)

### Anti-derivative

### Activity 2.20

1. Find at least three different functions which have the derivative 2x. Describe the similarities (and differences) between the functions.

**Answer:** For example x², x² + 5, x² − 3 (in general x² + C).
**Why:**
d/dx(x²) = 2x; d/dx(x² + 5) = 2x + 0 = 2x; d/dx(x² − 3) = 2x − 0 = 2x.
Similarities: all have the same "x² part", the same shape (the same parabola) and the same slope 2x at every x.
Differences: they differ only by a constant, so their graphs are vertical shifts of y = x² (different y-intercepts).

2. Check that all of these functions:

f(x) = x² + 3x + 1, g(x) = x² + 3x, h(x) = x² + 3x + 12, and k(x) = x² + 3x + π

have the same derivative; 2x + 3.

**Answer:** Each derivative is 2x + 3.
**Why:**
f′(x) = 2x + 3 + 0 = 2x + 3
g′(x) = 2x + 3
h′(x) = 2x + 3 + 0 = 2x + 3
k′(x) = 2x + 3 + 0 = 2x + 3 (π is a constant, so its derivative is 0)
They differ only in the constant term, which disappears on differentiation.

### Definition 2.14

The process of finding f(x) from its derivative f′(x) is known as anti-differentiation or integration. f(x) is said to be the **anti-derivative** of f′(x).

[figure: diagram — f(x) → f′(x) labelled "differentiation" (arrow to the right); f′(x) → f(x) labelled "Anti-differentiation" (arrow to the left).]

Integration is the reverse operation of differentiation.

---

## 2.3 (continued)

### 2.3.2 (continued) — Anti-derivative

[review: the heading of 2.3.2 is not on these pages; the "Anti-derivative" part (Activity 2.20, Definition 2.14) starts on p.135, handled by the previous chunk. Section 2.3.3 on p.138 refers back to "Sections 2.3.1 and 2.3.2", so this material is taken to be inside 2.3.2.]

(p.136)

> - The set of all anti-derivatives of a function f(x) is called the **indefinite integral** of f(x).
> - The indefinite integral of f(x) is denoted by ∫ f(x) dx read as "the integral of f(x) with respect to x".
>   - The symbol ∫ is said to be the **integral sign**.
>   - dx denotes that the variable of integration is x.
>   - If a function has an integral, then it is said to be integrable.
>   - If F′(x) = f(x), then ∫ f(x) dx = F(x) + c.
>   - c is known as the constant of integration.

In this section, you will see how to find the integrals of constant and power functions.

#### i. Integration of a power function

### Example 1

∫ x dx = (1/2)x² + c   Because d/dx((1/2)x² + c) = (1/2) × 2x + 0 = x

∫ x² dx = (1/3)x³ + c   Because d/dx((1/3)x³ + c) = (1/3) × 3x² + 0 = x²

∫ x³ dx = (1/4)x⁴ + c   Because d/dx((1/4)x⁴ + c) = (1/4) × 4x³ + 0 = x³

∫ 1 dx = x + c   Because d/dx(x + c) = 1 + 0 = 1

> In general, the following formula holds. However, α is a real number and
> α ≠ −1,   ∫ x^α dx = (1/(α+1)) x^(α+1) + c   (c is the constant of integration)
>
> **Note:** Since 1 = x⁰, ∫ 1 dx = ∫ x⁰ dx = (1/(0+1)) x^(0+1) + c = x + c

(p.137)

### Example 2

Find the following indefinite integrals:

a. ∫ x⁷ dx   b. ∫ x^(−3) dx   c. ∫ x^(1/2) dx   d. ∫ x^(−4/3) dx

**Solution**

a. ∫ x⁷ dx = (1/(7+1)) x^(7+1) + c = (1/8)x⁸ + c.

b. ∫ x^(−3) dx = (1/(−3+1)) x^(−3+1) + c = −(1/2)x^(−2) + c = −1/(2x²) + c.

c. ∫ x^(1/2) dx = (1/(1/2 + 1)) x^(1/2 + 1) + c = (2/3)x^(3/2) + c = (2/3)x√x + c.

d. ∫ x^(−4/3) dx = (1/(−4/3 + 1)) x^(−4/3 + 1) + c = (5/2)x^(−1/3) + c = 5/(2∛x) + c.

[review: book says (5/2)x^(−1/3) + c = 5/(2∛x) + c, working gives −3x^(−1/3) + c = −3/∛x + c because −4/3 + 1 = −1/3, so 1/(−1/3) = −3. Check: d/dx(−3x^(−1/3)) = −3 × (−1/3)x^(−4/3) = x^(−4/3). The book's 5/2 is a misprint.]

**Note:** c is the constant of integration.

### Exercise 2.24

Find the following indefinite integrals:

**a. ∫ x⁵ dx**

**Answer:** (1/6)x⁶ + C

**Why:**
Power rule with α = 5: ∫ x^α dx = x^(α+1)/(α+1) + C
α + 1 = 6
∫ x⁵ dx = x⁶/6 + C
Check: d/dx(x⁶/6) = 6x⁵/6 = x⁵ ✓

**b. ∫ x^(−4) dx**

**Answer:** −1/(3x³) + C

**Why:**
Power rule with α = −4 (allowed, since α ≠ −1)
α + 1 = −3
∫ x^(−4) dx = x^(−3)/(−3) + C
= −(1/3)x^(−3) + C = −1/(3x³) + C
Check: d/dx(−(1/3)x^(−3)) = −(1/3)(−3)x^(−4) = x^(−4) ✓

**c. ∫ x^(1/3) dx**

**Answer:** (3/4)x^(4/3) + C  (= (3/4)x∛x + C)

**Why:**
Power rule with α = 1/3
α + 1 = 1/3 + 3/3 = 4/3
∫ x^(1/3) dx = x^(4/3)/(4/3) + C
Dividing by 4/3 is multiplying by 3/4: = (3/4)x^(4/3) + C
x^(4/3) = x · x^(1/3) = x∛x, so = (3/4)x∛x + C
Check: d/dx((3/4)x^(4/3)) = (3/4)(4/3)x^(1/3) = x^(1/3) ✓

**d. ∫ x^(−3/2) dx**

**Answer:** −2/√x + C

**Why:**
Power rule with α = −3/2
α + 1 = −3/2 + 2/2 = −1/2
∫ x^(−3/2) dx = x^(−1/2)/(−1/2) + C
Dividing by −1/2 is multiplying by −2: = −2x^(−1/2) + C
x^(−1/2) = 1/√x, so = −2/√x + C
Check: d/dx(−2x^(−1/2)) = −2(−1/2)x^(−3/2) = x^(−3/2) ✓

**e. ∫ x¹⁰ dx**

**Answer:** (1/11)x¹¹ + C

**Why:**
Power rule with α = 10, α + 1 = 11
∫ x¹⁰ dx = x¹¹/11 + C
Check: d/dx(x¹¹/11) = 11x¹⁰/11 = x¹⁰ ✓

**f. ∫ x^(−2) dx**

**Answer:** −1/x + C

**Why:**
Power rule with α = −2, α + 1 = −1
∫ x^(−2) dx = x^(−1)/(−1) + C = −x^(−1) + C = −1/x + C
Check: d/dx(−x^(−1)) = −(−1)x^(−2) = x^(−2) ✓

**g. ∫ x^(3/2) dx**

**Answer:** (2/5)x^(5/2) + C  (= (2/5)x²√x + C)

**Why:**
Power rule with α = 3/2
α + 1 = 3/2 + 2/2 = 5/2
∫ x^(3/2) dx = x^(5/2)/(5/2) + C = (2/5)x^(5/2) + C
x^(5/2) = x² · x^(1/2) = x²√x
Check: d/dx((2/5)x^(5/2)) = (2/5)(5/2)x^(3/2) = x^(3/2) ✓

**h. ∫ x^(−3/5) dx**

**Answer:** (5/2)x^(2/5) + C  (= (5/2)⁵√(x²) + C)

**Why:**
Power rule with α = −3/5
α + 1 = −3/5 + 5/5 = 2/5
∫ x^(−3/5) dx = x^(2/5)/(2/5) + C = (5/2)x^(2/5) + C
Check: d/dx((5/2)x^(2/5)) = (5/2)(2/5)x^(−3/5) = x^(−3/5) ✓

#### ii. Properties of the indefinite integral

> 1. Let k be a constant, ∫ k f(x) dx = k ∫ f(x) dx
> 2. ∫ (f(x) + g(x)) dx = ∫ f(x) dx + ∫ g(x) dx
> 3. ∫ (f(x) − g(x)) dx = ∫ f(x) dx − ∫ g(x) dx

> **Note**
> ∫ k dx = kx + c, where k is a given constant and c is the constant of integration.

(p.138)

### Example

Find the following indefinite integrals:

a. ∫ 10 dx   b. ∫ (2x⁵ − x) dx   c. ∫ (x² + √x) dx

**Solution**

a. ∫ 10 dx = 10x + c

b. ∫ (2x⁵ − x) dx = 2 · (1/6)x⁶ − (1/2)x² + c = (1/3)x⁶ − (1/2)x² + c

c. ∫ (x² + √x) dx = (1/3)x³ + (2/3)x^(3/2) + c
[added step: √x = x^(1/2), and ∫ x^(1/2) dx = x^(3/2)/(3/2) = (2/3)x^(3/2)]

**Note:** Add only one constant of integration c at the end.

### Exercise 2.25

Find the following indefinite integrals.

**a. ∫ 99 dx**

**Answer:** 99x + C

**Why:**
Constant rule: ∫ k dx = kx + C with k = 99
∫ 99 dx = 99x + C
Check: d/dx(99x) = 99 ✓

**b. ∫ 10x⁴ dx**

**Answer:** 2x⁵ + C

**Why:**
Constant multiple rule: ∫ 10x⁴ dx = 10 ∫ x⁴ dx
Power rule: ∫ x⁴ dx = x⁵/5
10 · x⁵/5 = 2x⁵
Result: 2x⁵ + C
Check: d/dx(2x⁵) = 10x⁴ ✓

**c. ∫ (3/x) dx**

**Answer:** 3 ln|x| + C

**Why:**
Constant multiple rule: ∫ (3/x) dx = 3 ∫ (1/x) dx = 3 ∫ x^(−1) dx
The power rule cannot be used here: α = −1 is exactly the excluded case (α + 1 = 0 would mean dividing by 0).
The function whose derivative is 1/x is ln|x| (d/dx ln|x| = 1/x for x ≠ 0)
Result: 3 ln|x| + C
Check: d/dx(3 ln|x|) = 3 · (1/x) = 3/x ✓

[review: this question needs ∫ (1/x) dx = ln|x| + C, which the book has not taught in this section (the power formula explicitly excludes α = −1). Students who only have this chapter cannot answer it; a teacher note or a hint is needed.]

**d. ∫ (x² − x) dx**

**Answer:** (1/3)x³ − (1/2)x² + C

**Why:**
Difference rule: ∫ (x² − x) dx = ∫ x² dx − ∫ x dx
Power rule: ∫ x² dx = x³/3, ∫ x dx = x²/2
Result: x³/3 − x²/2 + C
Check: d/dx(x³/3 − x²/2) = x² − x ✓

**e. ∫ (3x² − 2x + 5) dx**

**Answer:** x³ − x² + 5x + C

**Why:**
Sum/difference rule: = ∫ 3x² dx − ∫ 2x dx + ∫ 5 dx
Constant multiple + power rule: ∫ 3x² dx = 3 · x³/3 = x³
∫ 2x dx = 2 · x²/2 = x²
Constant rule: ∫ 5 dx = 5x
Result: x³ − x² + 5x + C
Check: d/dx(x³ − x² + 5x) = 3x² − 2x + 5 ✓

**f. ∫ (−2x² − x − 6) dx**

**Answer:** −(2/3)x³ − (1/2)x² − 6x + C

**Why:**
Sum/difference rule: = ∫ −2x² dx − ∫ x dx − ∫ 6 dx
∫ −2x² dx = −2 · x³/3 = −(2/3)x³
∫ x dx = x²/2
∫ 6 dx = 6x
Result: −(2/3)x³ − (1/2)x² − 6x + C
Check: d/dx(−(2/3)x³ − (1/2)x² − 6x) = −2x² − x − 6 ✓

**g. ∫ (x^(−2) − 4x³ + √x) dx**

**Answer:** −1/x − x⁴ + (2/3)x^(3/2) + C

**Why:**
Sum/difference rule: = ∫ x^(−2) dx − ∫ 4x³ dx + ∫ x^(1/2) dx
Power rule: ∫ x^(−2) dx = x^(−1)/(−1) = −1/x
Constant multiple + power rule: ∫ 4x³ dx = 4 · x⁴/4 = x⁴
Power rule: ∫ x^(1/2) dx = x^(3/2)/(3/2) = (2/3)x^(3/2)
Result: −1/x − x⁴ + (2/3)x^(3/2) + C
Check: d/dx = x^(−2) − 4x³ + x^(1/2) ✓

### 2.3.3 Area and Definite Integrals

In Sections 2.3.1 and 2.3.2, we considered the area under the graph of a function f. We have yet to establish the general rule to find the exact area under the graph of f. As we will see, we can use the anti-derivative of a function to determine the exact area under the graph of the function. This process is called integration.

### Definition 2.15

Let f be a given function over the interval [a, b] and F be any anti-derivative of f. Then the definite integral of f from a to b is: ∫_{a}^{b} f(x) dx = F(b) − F(a).

Evaluating definite integrals is called *integration*. The numbers a and b are known as *the limits of integration*.

(p.139)

### Theorem 2.7 (The Fundamental Theorem of Calculus)

Let f be a given non-negative function over an interval [0, b], and let A(x) be the area between the graph of f and the x-axis over the interval [0, x], with 0 < x < b. Then A(x) is a differentiable function of x and A′(x) = f(x).

> **Note**
> To find the area under the graph of a nonnegative function f over the interval [a, b]:
> 1. Find any anti-derivative F(x) of f(x). Let C = 0 for simplicity.
> 2. Evaluate F(x) at x = b and x = a, and compute F(b) − F(a).
>
> The result is the area under the graph over the interval [a, b].

[figure: Figure 2.28 — a curve y = f(x) above the x-axis; the region under it between x = a and x = b is shaded green and labelled "Area = F(b) − F(a)".]

### Example 1

Find the area under the graph of y = x² + 1 over the interval [−1, 2].

**Solution**

In this case, f(x) = x² + 1, with a = −1 and b = 2.

1. Find any anti-derivative of x = b of f(x). We choose the simplest one:
   [review: "of x = b" is a stray misprint in the book; the sentence should read "Find any anti-derivative F(x) of f(x)".]

   F(x) = x³/3 + x.

(p.140)

2. Substitute 2 and −1, and find the difference F(2) − F(−1):

∫_{−1}^{2} (x² + 1) dx = [x³/3 + x]_{−1}^{2}
= [2³/3 + 2] − [(−1)³/3 + (−1)]
[added step: = (8/3 + 2) − (−1/3 − 1) = 14/3 − (−4/3) = 14/3 + 4/3 = 18/3]
= 6

[figure: Figure 2.29 — graph of y = x² + 1 on a square grid; the region under the parabola from x = −1 to x = 2 is shaded orange (heights from 2 at x = −1, down to 1 at x = 0, up to 5 at x = 2).]

We can make a partial check by counting the squares and parts of squares shaded on the graph in Figure 2.29.

### Exercise 2.26

1. Refer to the function and graph in Example 1.

**a. Calculate the area over the interval [0, 5].**

**Answer:** 140/3 = 46 2/3 square units

**Why:**
f(x) = x² + 1 ≥ 0, so area = ∫_{0}^{5} (x² + 1) dx
Anti-derivative (power rule + constant rule): F(x) = x³/3 + x
Upper limit: F(5) = 125/3 + 5 = 125/3 + 15/3 = 140/3
Lower limit: F(0) = 0 + 0 = 0
F(5) − F(0) = 140/3 − 0 = 140/3 ≈ 46.67
Second check: average of f over [0,5] must lie between f(0)=1 and f(5)=26; 140/3 ÷ 5 = 9.33 ✓

**b. Calculate the area over the interval [−2, 2].**

**Answer:** 28/3 = 9 1/3 square units

**Why:**
Area = ∫_{−2}^{2} (x² + 1) dx, F(x) = x³/3 + x
Upper limit: F(2) = 8/3 + 2 = 8/3 + 6/3 = 14/3
Lower limit: F(−2) = −8/3 − 2 = −14/3
F(2) − F(−2) = 14/3 − (−14/3) = 28/3 ≈ 9.33

**c. Can you suggest a shortcut for part (b)?**

**Answer:** The graph is symmetric about the y-axis (f(−x) = f(x)), so the area over [−2, 2] is twice the area over [0, 2]: 2 × 14/3 = 28/3.

**Why:**
f(−x) = (−x)² + 1 = x² + 1 = f(x), so the region on [−2, 0] is the mirror image of the region on [0, 2]
∫_{0}^{2} (x² + 1) dx = F(2) − F(0) = 14/3 − 0 = 14/3
Area over [−2, 2] = 2 × 14/3 = 28/3 ✓ (same as part b)

2. Evaluate each of these integrals.

**a. ∫_{1}^{3} (3x² + 2x) dx**

**Answer:** 34

**Why:**
Anti-derivative: ∫ 3x² dx = x³, ∫ 2x dx = x², so F(x) = x³ + x²
Upper limit: F(3) = 27 + 9 = 36
Lower limit: F(1) = 1 + 1 = 2
F(3) − F(1) = 36 − 2 = 34
Check: F′(x) = 3x² + 2x ✓

**b. ∫_{−1}^{0} (x³ − 3x + 1) dx**

**Answer:** 9/4 = 2 1/4

**Why:**
Anti-derivative: F(x) = x⁴/4 − 3x²/2 + x
Upper limit: F(0) = 0
Lower limit: F(−1) = 1/4 − 3/2 + (−1) = 1/4 − 6/4 − 4/4 = −9/4
F(0) − F(−1) = 0 − (−9/4) = 9/4
Check: F′(x) = x³ − 3x + 1 ✓

**c. ∫_{4}^{15} (0.002x⁴ − 0.3x² + 4x − 7) dx**

**Answer:** 313.2404

**Why:**
Anti-derivative: ∫ 0.002x⁴ dx = 0.002x⁵/5 = 0.0004x⁵
∫ 0.3x² dx = 0.3x³/3 = 0.1x³
∫ 4x dx = 2x², ∫ 7 dx = 7x
F(x) = 0.0004x⁵ − 0.1x³ + 2x² − 7x
Upper limit: 15⁵ = 759375, 15³ = 3375, 15² = 225
F(15) = 0.0004(759375) − 0.1(3375) + 2(225) − 7(15) = 303.75 − 337.5 + 450 − 105 = 311.25
Lower limit: 4⁵ = 1024, 4³ = 64, 4² = 16
F(4) = 0.0004(1024) − 0.1(64) + 2(16) − 7(4) = 0.4096 − 6.4 + 32 − 28 = −1.9904
F(15) − F(4) = 311.25 − (−1.9904) = 313.2404
Check: exact fractions give 783101/2500 = 313.2404 ✓

(p.141)

### Example 2

Let y = x³ represent the number of kilowatts (kW) generated by a new power plant each day, x days after going online. Find the area under the graph of y = x³ over the interval [0, 5] and interpret the significance of the area.

**Solution**

In this case, f(x) = x³, a = 0, and b = 5.

1. Find any anti-derivative F(x) of f(x). We choose the simplest one:

   F(x) = x⁴/4

2. Substitute 5 and 0, and find the difference F(5) − F(0):

   F(5) − F(0) = 5⁴/4 − 0⁴/4 = 625/4 = 156 1/4.

[figure: Figure 2.30 — graph of f(x) = x³; the region under the curve from x = 0 to x = 5 is marked by a vertical line at x = 5.]

The area represents the total number of kilowatts generated during the first 5 days.

The difference F(b) − F(a) has the same value for all anti-derivatives F of a function f(x) whether the function is nonnegative or not. It is called the definite integral of f(x) from a to b.

(p.142)

> **Properties of definite integrals**
> If f and g are given function on [a, b], k ∈ ℜ, and c ∈ [a, b], then
> a. ∫_{a}^{a} f(x) dx = 0
> b. ∫_{a}^{b} f(x) dx = ∫_{a}^{c} f(x) dx + ∫_{c}^{b} f(x) dx
> c. ∫_{a}^{b} f(x) dx = −∫_{b}^{a} f(x) dx
> d. ∫_{a}^{b} k f(x) dx = k ∫_{a}^{b} f(x) dx
> e. ∫_{a}^{b} (f(x) ± g(x)) dx = ∫_{b}^{a} f(x) dx ± ∫_{b}^{a} g(x) dx

[review: property e is misprinted in the book with the limits on the right-hand side reversed (lower b, upper a). The correct statement is ∫_{a}^{b} (f(x) ± g(x)) dx = ∫_{a}^{b} f(x) dx ± ∫_{a}^{b} g(x) dx, as the Summary on p.154 gives it.]

### Example 3

Evaluate ∫_{a}^{b} x² dx.

**Solution**

Using the anti-derivative F(x) = x³/3, we have ∫_{a}^{b} x² dx = b³/3 − a³/3.

It is convenient to use an intermediate notation: ∫_{a}^{b} f(x) dx = [F(x)]_{a}^{b} = F(b) − F(a), where F(x) is an anti-derivative of f(x).

### Example 4

Evaluate ∫_{−1}^{4} (x² − x) dx

**Solution**

a) ∫_{−1}^{4} (x² − x) dx = [x³/3 − x²/2]_{−1}^{4}
= (4³/3 − 4²/2) − ((−1)³/3 − (−1)²/2)
[added step: = (64/3 − 8) − (−1/3 − 1/2)]
= 64/3 − 8 + 1/3 + 1/2 = 14 1/6.
[added step: 64/3 + 1/3 = 65/3; 65/3 − 8 = 41/3; 41/3 + 1/2 = 82/6 + 3/6 = 85/6 = 14 1/6]

(p.143)

### Exercise 2.27

Evaluate the following definite integrals:

**a. ∫_{1}^{3} x² dx**

**Answer:** 26/3 = 8 2/3

**Why:**
Power rule: F(x) = x³/3
Upper limit: F(3) = 27/3 = 9
Lower limit: F(1) = 1/3
F(3) − F(1) = 9 − 1/3 = 27/3 − 1/3 = 26/3
Check with Example 3: b³/3 − a³/3 = 27/3 − 1/3 = 26/3 ✓

**b. ∫_{0}^{2} (x² − 2x + 8) dx**

**Answer:** 44/3 = 14 2/3

**Why:**
Anti-derivative: F(x) = x³/3 − x² + 8x
Upper limit: F(2) = 8/3 − 4 + 16 = 8/3 + 12 = 8/3 + 36/3 = 44/3
Lower limit: F(0) = 0
F(2) − F(0) = 44/3
Check: F′(x) = x² − 2x + 8 ✓

**c. ∫_{−2}^{3} (−3x² + 4x − 5) dx**

**Answer:** −50

**Why:**
Anti-derivative: ∫ −3x² dx = −x³, ∫ 4x dx = 2x², ∫ 5 dx = 5x
F(x) = −x³ + 2x² − 5x
Upper limit: F(3) = −27 + 18 − 15 = −24
Lower limit: F(−2) = −(−8) + 2(4) − 5(−2) = 8 + 8 + 10 = 26
F(3) − F(−2) = −24 − 26 = −50
Sense check: −3x² + 4x − 5 < 0 for every x (discriminant 16 − 60 < 0), so a negative answer is expected ✓

**d. ∫_{1}^{4} (2x + 1/x²) dx**

**Answer:** 63/4 = 15 3/4

**Why:**
Write 1/x² = x^(−2)
∫ 2x dx = x², ∫ x^(−2) dx = x^(−1)/(−1) = −1/x
F(x) = x² − 1/x
Upper limit: F(4) = 16 − 1/4 = 63/4
Lower limit: F(1) = 1 − 1 = 0
F(4) − F(1) = 63/4 − 0 = 63/4
Check: F′(x) = 2x + 1/x² ✓

### 2.3.4 More on Area

When we evaluate the definite integral of a nonnegative function, we get the area under the graph over an interval.

### Activity 2.21

Find the areas of a region bounded by the function f(x) and the interval [a, b], where

**a. f(x) = k, k > 0.**

**Answer:** k(b − a)

**Why:**
f(x) = k > 0, so area = ∫_{a}^{b} k dx
Constant rule: F(x) = kx
F(b) − F(a) = kb − ka = k(b − a)
Geometric check: the region is a rectangle of width b − a and height k ✓

**b. f(x) = x.**

**Answer:** (b² − a²)/2 (for 0 ≤ a < b, where f(x) = x ≥ 0)

**Why:**
Area = ∫_{a}^{b} x dx (taking 0 ≤ a < b so the graph is above the x-axis)
Power rule: F(x) = x²/2
F(b) − F(a) = b²/2 − a²/2 = (b² − a²)/2
Geometric check: the region is a trapezium with parallel sides a and b and width b − a: (a + b)/2 × (b − a) = (b² − a²)/2 ✓

**c. f(x) = x².**

**Answer:** (b³ − a³)/3

**Why:**
x² ≥ 0 for all x, so area = ∫_{a}^{b} x² dx
Power rule: F(x) = x³/3
F(b) − F(a) = b³/3 − a³/3 = (b³ − a³)/3 (matches Example 3)

### Example 1

Find the area under y = 1/x² over the interval [1, b].

[figure: Figure 2.31 — graph of y = 1/x², two branches symmetric about the y-axis, both above the x-axis, rising steeply near x = 0 and approaching 0 as |x| grows.]

**Solution**

∫_{1}^{b} dx/x² = ∫_{1}^{b} x^(−2) dx = [x^(−2+1)/(−2+1)]_{1}^{b} = [x^(−1)/(−1)]_{1}^{b} = [−1/x]_{1}^{b} = (−1/b) − (−1/1) = 1 − 1/b.

The definite integral is also defined for f(x) < 0. We can use geometry to determine the value of some definite integrals, as the following example suggests.

(p.144)

### Example 2

Compare the definite integrals of the functions y = x² and y = −x²

**Solution**

∫_{0}^{2} x² dx = [x³/3]_{0}^{2} = 2³/3 − 0³/3 = 8/3.

and

∫_{0}^{2} −x² dx = [−x³/3]_{0}^{2} = −2³/3 − 0³/3 = −8/3.
[added step: the second term is −(−0³/3) = 0, so the value is −8/3]

The graphs of the functions y = x² and y = −x² are reflections of each other across the x-axis (see Figure 2.32a and Figure 2.32b). Thus, the shaded areas are the same, 8/3. The evaluation procedure for y = −x² gave us −8/3. This illustrates that for negative-valued functions, the definite integral gives us the opposite of the area between the curve and the x-axis.

[figure: Figure 2.32a — y = x² from x = 0 to x = 2, region A between the curve and the x-axis shaded purple (height 4 at x = 2).]
[figure: Figure 2.32b — y = −x² from x = 0 to x = 2, region between the x-axis and the curve shaded green, below the axis (depth −4 at x = 2).]

When f(x) ≥ 0 in the interval [a, b], the area S which is enclosed by the graph of f(x), the two straight lines x = a, x = b and the x-axis is S = ∫_{a}^{b} f(x) dx

[figure: Figure 2.33 — increasing curve above the x-axis; region S between x = a and x = b under the curve.]

(p.145)

When f(x) ≤ 0 in the interval [a, b], the areas S which is enclosed by the graph of f(x), the two straight lines x = a, x = b, and the x-axis is

S = −∫_{a}^{b} f(x) dx

[figure: Figure 2.34 — curve below the x-axis; region S between x = a and x = b, between the curve and the x-axis.]

### Example 3

Find the area S which is enclosed by the graph of f(x) and the x-axis.

a. f(x) = −x² + 1   b. f(x) = x² − 1

**Solution**

a. From the figure on the right, the area S is

S = ∫_{−1}^{1} (−x² + 1) dx
= [−x³/3 + x]_{−1}^{1}
= (−1³/3 + 1) − {−(−1)³/3 + (−1)}
= 2/3 + 2/3 = 4/3
[added step: −1/3 + 1 = 2/3; −(−1)/3 − 1 = 1/3 − 1 = −2/3; 2/3 − (−2/3) = 4/3]

[figure: Figure 2.35 — downward parabola y = −x² + 1 crossing the x-axis at −1 and 1, vertex (0, 1); region between the arch and the x-axis shaded.]

a. From the figure on the right, the area S is
[review: the book labels this second part "a." again; it is part b.]

S = −∫_{−1}^{1} (x² − 1) dx
= −[x³/3 − x]_{−1}^{1}
= −[(1³/3 − 1) − {(−1)³/3 − (−1)}] = −(−2/3 − 2/3) = 4/3

[figure: Figure 2.36 — upward parabola y = x² − 1 crossing the x-axis at −1 and 1, vertex (0, −1); region between the x-axis and the curve (below the axis) shaded.]

When the area S is divided into the upper side and the lower side of the x-axis, the upper area and the lower side area are obtained respectively and added them.

(p.146)

In the figure below, the area S of the area enclosed by the graph of f(x) and the x-axis can be found by S = A + B.

In the interval [a, b], f(x) ≤ 0. In the interval [b, c], f(x) ≥ 0.

So, we can find the area S,

S = −∫_{a}^{b} f(x) dx + ∫_{b}^{c} f(x) dx

[figure: Figure 2.37 — curve y = f(x) crossing the x-axis at a, b and c; region A below the axis between a and b, region B above the axis between b and c.]

### Example 4

Find the area S of the region enclosed between the graph of f(x) = x² − 1, the x-axis, and the y-axis in the interval [0, 2].

**Solution**

Note that 1 is the x-intercept of the function f(x) = x² − 1 in [0, 2].

[figure: Figure 2.38 — graph of f(x) = x² − 1; region between the curve and the x-axis from x = 0 to x = 1 (below the axis) shaded pink, region from x = 1 to x = 2 (above the axis) shaded blue.]

S = ∫_{0}^{2} (x² − 1) dx = −∫_{0}^{1} (x² − 1) dx + ∫_{1}^{2} (x² − 1) dx
= −[x³/3 − x]_{0}^{1} + [x³/3 − x]_{1}^{2}
= −[(1³/3 − 1) − (0³/3 − 0)] + [(2³/3 − 2) − (1³/3 − 1)]
= −(−2/3) + 4/3 = 2/3 + 4/3 = 2
[added step: 2³/3 − 2 = 8/3 − 6/3 = 2/3; 1/3 − 1 = −2/3; 2/3 − (−2/3) = 4/3]

This shows that the area above the x-axis exceeds the area below the x-axis by 2 unit. So, the area of the region is 2 units.

[review: two errors in the book here. (1) The first equality "S = ∫_{0}^{2} (x² − 1) dx" is wrong: ∫_{0}^{2} (x² − 1) dx = (8/3 − 2) − 0 = 2/3, not the area; S equals −∫_{0}^{1} + ∫_{1}^{2}. (2) The sentence "the area above the x-axis exceeds the area below by 2" is wrong: area above = 4/3, area below = 2/3, so the excess is 2/3 (which is the value of ∫_{0}^{2}); the total area is 2 square units (the final answer 2 is correct).]

(p.147)

The definite integral of a continuous function over an interval is the sum of the areas above the x-axis minus the sum of the areas below the x-axis.

### Example 5

Consider ∫_{−1}^{2} (−x³ + 3x − 1) dx. Predict the sign of the result by examining the graph, and then evaluate the integral.

**Solution**

From the graph, it appears that there is considerably more area below the x-axis than above. Thus, we expect that

∫_{−1}^{2} (−x³ + 3x − 1) dx < 0.

Evaluating the integral, we have

∫_{−1}^{2} (−x³ + 3x − 1) dx = [−x⁴/4 + (3/2)x² − x]_{−1}^{2}
= (−2⁴/4 + (3/2)·2² − 2) − (−(−1)⁴/4 + (3/2)·(−1)² − (−1))
= (−4 + 6 − 2) − (−1/4 + 3/2 + 1)
= 0 − 2 1/4 = −2 1/4.
[added step: −1/4 + 3/2 + 1 = −1/4 + 6/4 + 4/4 = 9/4 = 2 1/4]

[figure: Figure 2.39 — graph of f(x) = −x³ + 3x − 1 from x = −1 to x = 2; a large region below the axis from x = −1 to about x = 0.35 shaded blue, a small region above the axis from about 0.35 to about 1.53 shaded green, and a region below the axis from about 1.53 to 2 shaded light orange.]

As a partial check, we note that the result is negative, as predicted.

(p.148)

### Exercise 2.28

1. Find the area S which is enclosed by the graph of f(x) and the x-axis.

**a. f(x) = x² − 4**

**Answer:** S = 32/3 = 10 2/3 square units

**Why:**
x-intercepts: x² − 4 = 0 → x = −2 or x = 2
Between −2 and 2, f(x) ≤ 0 (e.g. f(0) = −4), so S = −∫_{−2}^{2} (x² − 4) dx
Anti-derivative: F(x) = x³/3 − 4x
Upper limit: F(2) = 8/3 − 8 = −16/3
Lower limit: F(−2) = −8/3 + 8 = 16/3
∫_{−2}^{2} (x² − 4) dx = −16/3 − 16/3 = −32/3
S = −(−32/3) = 32/3

**b. f(x) = −x² + 4**

**Answer:** S = 32/3 square units

**Why:**
x-intercepts: −x² + 4 = 0 → x = ±2; between them f(x) ≥ 0 (f(0) = 4)
S = ∫_{−2}^{2} (−x² + 4) dx, F(x) = −x³/3 + 4x
Upper limit: F(2) = −8/3 + 8 = 16/3
Lower limit: F(−2) = 8/3 − 8 = −16/3
S = 16/3 − (−16/3) = 32/3
Check: this is the reflection of part a across the x-axis, so the area is the same ✓

**c. f(x) = x² − 2x**

**Answer:** S = 4/3 square units

**Why:**
x-intercepts: x(x − 2) = 0 → x = 0 or x = 2; between them f(x) ≤ 0 (f(1) = −1)
S = −∫_{0}^{2} (x² − 2x) dx, F(x) = x³/3 − x²
Upper limit: F(2) = 8/3 − 4 = −4/3
Lower limit: F(0) = 0
∫ = −4/3 − 0 = −4/3, so S = 4/3

**d. f(x) = −x² − 2x**

**Answer:** S = 4/3 square units

**Why:**
x-intercepts: −x(x + 2) = 0 → x = −2 or x = 0; between them f(x) ≥ 0 (f(−1) = 1)
S = ∫_{−2}^{0} (−x² − 2x) dx, F(x) = −x³/3 − x²
Upper limit: F(0) = 0
Lower limit: F(−2) = −(−8)/3 − 4 = 8/3 − 12/3 = −4/3
S = 0 − (−4/3) = 4/3

2. Find the area S which is enclosed by the graph of f(x), the two straight lines and the x-axis.

**a. f(x) = x², the two straight lines x = 0 and x = 4**

**Answer:** S = 64/3 = 21 1/3 square units

**Why:**
x² ≥ 0 on [0, 4], so S = ∫_{0}^{4} x² dx
F(x) = x³/3
Upper limit: F(4) = 64/3; lower limit: F(0) = 0
S = 64/3 − 0 = 64/3

**b. f(x) = x² + 3, the two straight lines x = −1 and x = 3**

**Answer:** S = 64/3 = 21 1/3 square units

**Why:**
x² + 3 > 0 everywhere, so S = ∫_{−1}^{3} (x² + 3) dx
F(x) = x³/3 + 3x
Upper limit: F(3) = 27/3 + 9 = 9 + 9 = 18
Lower limit: F(−1) = −1/3 − 3 = −10/3
S = 18 − (−10/3) = 54/3 + 10/3 = 64/3

**3. Find the area S which is enclosed between the graph of f(x) = x(x + 2)(x − 1) and the x-axis.**

**Answer:** S = 37/12 = 3 1/12 square units

**Why:**
x-intercepts: x = −2, x = 0, x = 1
Expand: x(x + 2)(x − 1) = x(x² + x − 2) = x³ + x² − 2x
Sign on [−2, 0]: f(−1) = (−1)(1)(−2) = 2 > 0, so the graph is above the axis
Sign on [0, 1]: f(1/2) = (1/2)(5/2)(−1/2) = −5/8 < 0, so below the axis
S = ∫_{−2}^{0} f(x) dx − ∫_{0}^{1} f(x) dx
F(x) = x⁴/4 + x³/3 − x²
F(0) = 0
F(−2) = 16/4 + (−8)/3 − 4 = 4 − 8/3 − 4 = −8/3
∫_{−2}^{0} f(x) dx = 0 − (−8/3) = 8/3
F(1) = 1/4 + 1/3 − 1 = 3/12 + 4/12 − 12/12 = −5/12
∫_{0}^{1} f(x) dx = −5/12 − 0 = −5/12
S = 8/3 − (−5/12) = 32/12 + 5/12 = 37/12
Note: ∫_{−2}^{1} f(x) dx alone = 8/3 − 5/12 = 27/12 = 9/4, which is NOT the area.

### 2.3.5 Application of Integration

### Activity 2.22

**Do you think that integration has any other applications than finding the area under the curve of the function? Write down what you think these applications might be.**

**Answer:** Yes. Whenever we know a rate of change, integrating it gives the total change (accumulated amount). For example: total profit or cost from marginal profit or cost; displacement or distance from velocity; total sales from a sales rate; total pollution from a rate of flow; also volumes, work and averages.

**Why:**
By the Fundamental Theorem, ∫_{a}^{b} F′(x) dx = F(b) − F(a): integrating a rate gives the total change of the quantity over [a, b]
The examples that follow (profit, displacement, distance while braking) are all of this form.

In this section, we will look at some applications of integrals. Integration is used in different fields of study such as business, physical sciences, economics, etc.

### Example 1

A certain Airlines determines that the marginal profit resulting from the sale of x seats on a plane traveling from Addis Ababa to New York City, in hundreds of dollars, is given by P′(x) = √x − 6.

Find the total profit when 60 seats are sold.

(p.149)

**Solution**

We integrate to find P(60):

P(60) = ∫_{0}^{60} P′(x) dx = ∫_{0}^{60} (√x − 6) dx = [(2/3)x^(3/2) − 6x]_{0}^{60} ≈ −50.1613.
[added step: 60^(3/2) = 60√60 ≈ 464.758; (2/3)(464.758) ≈ 309.839; 6 × 60 = 360; 309.839 − 360 ≈ −50.161; at x = 0 the value is 0. This also assumes P(0) = 0.]

When 60 seats are sold, the airline's profit is −$5016.13. That is, the airline will lose $5016.13 on the flight.

### Example 2

Suppose that the velocity function of a car is v(t) = 5t⁴ and that the displacement at t = 0 is s(0) = 9. Find s(t). Assume that s(t) is in meters and v(t) is in meter per second.

**Solution**

First s(t) = ∫ v(t) dt = ∫ 5t⁴ dt = t⁵ + C.

Next, we determine C by using the initial condition s(0) = 9, which is the displacement of the car at time t = 0: s(0) = 0⁵ + C = 9 ⇒ C = 9 Thus, s(t) = t⁵ = 9.

[review: book says "s(t) = t⁵ = 9", working gives s(t) = t⁵ + 9 because C = 9 is added to t⁵. Misprint of "=" for "+".]

### Example 3

The driver of a vehicle traveling at 40 mi/hr (58.67 ft/sec) applies the brakes, softly at first, then harder, coming to a complete stop after 7 seconds. The velocity as a function of time is modeled by v(t) = −1.197t² + 58.67, where v is in feet per second, t is in seconds, and 0 ≤ t ≤ 7. How far did the vehicle travel while the driver was braking?

(p.150)

**Solution**

The distance traveled s(t) is given by the definite integral of v(t):

s(t) = ∫_{0}^{7} (−1.197t² + 58.67) dt = [−(1.197/3)t³ + 58.67t]_{0}^{7}
= −(1.197/3)(7)³ + 58.67(7) − 0
≈ 273.83 ft
[added step: 7³ = 343; 1.197/3 = 0.399; 0.399 × 343 = 136.857; 58.67 × 7 = 410.69; 410.69 − 136.857 = 273.833]

### Exercise 2.29

**1. Pure Water Enterprises finds that the marginal profit, in dollars, from drilling a well that is x feet deep is given by P′(t) = ⁵√x. Find the profit when a well 250 ft deep is drilled.**

[review: the book writes P′(t) but the variable is x; read as P′(x) = ⁵√x. Root index read as 5 after zooming in.]

**Answer:** P(250) = (5/6)·250^(6/5) = (625/3)·⁵√250 ≈ $628.56

**Why:**
Assume P(0) = 0 (no profit when nothing is drilled), so P(250) = ∫_{0}^{250} x^(1/5) dx
Power rule with α = 1/5: α + 1 = 6/5, so F(x) = x^(6/5)/(6/5) = (5/6)x^(6/5)
Upper limit: 250^(6/5) = 250 × 250^(1/5) ≈ 250 × 3.01709 ≈ 754.27, so F(250) ≈ (5/6)(754.27) ≈ 628.56
Lower limit: F(0) = 0
P(250) ≈ 628.56 − 0 = 628.56 dollars
Check: F′(x) = (5/6)(6/5)x^(1/5) = x^(1/5) ✓

**2. A company estimates that its sales will grow continuously at a rate given by the function S′(t) = 20eᵗ, where S′(t) is the rate at which sales are increasing, in dollars per day, on day t.**

[review: this question needs ∫ eᵗ dt = eᵗ + C, which is not taught in the pages of this section.]

**a. Find the accumulated sales for the first 5 days.**

**Answer:** 20(e⁵ − 1) ≈ $2948.26

**Why:**
Accumulated sales = ∫_{0}^{5} 20eᵗ dt
Constant multiple rule and d/dt(eᵗ) = eᵗ: anti-derivative F(t) = 20eᵗ
Upper limit: F(5) = 20e⁵ ≈ 20 × 148.4132 = 2968.26
Lower limit: F(0) = 20e⁰ = 20
F(5) − F(0) = 20e⁵ − 20 = 20(e⁵ − 1) ≈ 2948.26

**b. Find the sales from the 2nd day through the 5th day.**

**Answer:** 20(e⁵ − e) ≈ $2913.90

**Why:**
The 2nd day starts at t = 1 and the 5th day ends at t = 5, so sales = ∫_{1}^{5} 20eᵗ dt
F(t) = 20eᵗ
Upper limit: F(5) = 20e⁵ ≈ 2968.26
Lower limit: F(1) = 20e ≈ 54.37
F(5) − F(1) ≈ 2968.26 − 54.37 = 2913.90

[review: interpretation choice. If "from the 2nd day" is read as t = 2 to t = 5, the answer is 20(e⁵ − e²) ≈ $2820.48. Confirm the intended reading with the answer key.]

## Summary

(p.151)

- **Rate of change, gradient, and derivative of functions**
  - A **rate of change** is a rate that describes how one quantity changes in relation to another quantity.
  - If y = f(x) then the **average rate of change** of y with respect to x on the interval [a, b] is Δy/Δx = (f(b) − f(a))/(b − a).
  - A **secant line** is a line that intersects the graph of the function y = f(x) at exactly two points.
  - A **tangent line** to a curve or a graph of a function y = f(x) is a line that touches the curve exactly at one point. The point where the tangent line touches the graph is said to be the point of tangency.
  - A **gradient** is a measure of steepness and direction of a line. Gradient = vertical change / horizontal change = Δy/Δx.
  - The derivative of a function f(x) at a number a in the domain of f, denoted by f′(a) is the gradient of a tangent line to the graph of f(x) at (a, f(a)). That is as h gets very close to zero from both sides, f′(a) = (f(a + h) − f(a))/h.
    [review: as printed, the formula has no "lim_{h→0}"; the words "as h gets very close to zero" stand in for it. Full form: f′(a) = lim_{h→0} (f(a + h) − f(a))/h.]
- **The derivatives of some functions**
  1. If f(x) = k, then f′(x) = 0.
  2. If f(x) = xⁿ, then f′(x) = nx^(n−1).
  3. If f(x) = √x, then f′(x) = 1/(2√x).

(p.152)

- **Derivatives of combinations of functions**
  If f and g are differentiable functions, then f + g, kf, fg and f/g are also differentiable and are given as follows:
  1. (f + g)′(x) = f′(x) + g′(x).
  2. (kf)′(x) = kf′(x), where k is a constant number.
  3. (fg)′(x) = f′(x)g(x) + f(x)g′(x).
  4. (f/g)′(x) = (f′(x)g(x) − f(x)g′(x))/(g(x))²
- **Differentiations of the composition of functions**
  - Let g be differentiable at x, and f be differentiable at g(x). Then fog is differentiable at x, and (fog)′(x) = f′(g(x))g′(x) for all x such that g is differentiable at x and f is differentiable at g(x).
  - If y is a function of u, and u is a function of x, then dy/dx = (dy/du)(du/dx)
- **Equation of tangent line and normal line to a curve**
  - a. The equation of the tangent line to the curve y = f(x) at x = a is given by y = f′(a)(x − a) + f(a).
  - b. The equation of the normal line to the curve y = f(x) at x = a and f′(x) ≠ 0 is given by y = (−1/f′(a))(x − a) + f(a).
- A **critical value** of a function f is any number c in the domain of f for which the tangent line at (c, f(c)) is horizontal or for which the derivative does not exist. That is, c is a critical value if f(c) exists and f′(c) = 0 or f′(c) does not exist.

(p.153)

- Let I be the domain of f. f(c) is a **relative minimum** if there exists within I an open interval I₁ containing c such that f(c) ≤ f(x), for all x in I₁ and is a **relative maximum** if there exists within I an open interval I₂ containing c such that f(c) ≥ f(x), for all x in I₂.
- **The First-Derivative Test for Relative Extrema**
  Let f be a function that is differentiable on an interval I. Then
  1. If f′ changes sign from positive to negative at c then f has **a local maximum** value at c for some critical value c.
  2. If f′ changes sign from negative to positive at c then f has **a local minimum** value at c for some critical value c.
- The **anti-derivative** of f(x) is the set of functions F(x) + C such that d/dx(F(x) + C) = f(x), where the constant C is called the **constant of integration.**
- Let f be continuous on [a, b], and let p = {x₀, x₁, x₂, …, xₙ} be any portion of [a, b]. Then the sum
  Σ_{k=1}^{n} f(t_k)Δx_k = f(t₁)Δx₁ + f(t₂)Δx₂ + f(t₃)Δx₃ + … + f(tₙ)Δxₙ is called **a Riemann sum for f on [a, b].**
  [review: "portion" is a misprint for "partition".]
- Fundamental Theorem of Calculus:
  If f(x) = F′(x), then ∫_{a}^{b} f(x) dx = F(b) − F(a).
- If a function has areas both below and above the x-axis, the definite integral gives the net total area or the difference between the sum of the areas above the x-axis and the sum of the areas below the x-axis.
  - If there is more area above the x-axis than below, the definite integral will be positive.

(p.154)

  - If there is more area below the x-axis than above, the definite integral will be negative.
  - If the areas above and below the x-axis are the same, the definite integral will be 0.
- Properties of definite integrals
  - a. ∫_{a}^{b} f(x) dx = ∫_{a}^{c} f(x) dx + ∫_{c}^{b} f(x) dx
  - b. ∫_{a}^{b} (f(x) ± g(x)) dx = ∫_{a}^{b} f(x) dx ± ∫_{a}^{b} g(x) dx
  - c. ∫_{a}^{b} (f(x) ± g(x)) dx = ∫_{a}^{b} f(x) dx ± ∫_{a}^{b} g(x) dx
  - d. ∫_{a}^{b} f(x) dx = −∫_{b}^{a} f(x) dx
  - e. ∫_{a}^{b} (f(x) ± g(x)) dx = ∫_{a}^{b} f(x) dx ± ∫_{a}^{b} g(x) dx

  [review: in the book's Summary, items b, c and e are the same property printed three times. The properties ∫_{a}^{a} f(x) dx = 0 and ∫_{a}^{b} k f(x) dx = k ∫_{a}^{b} f(x) dx (from p.142) are missing; they were probably meant to be two of these.]

## Review Exercise

(p.155)

**1. Find the derivative of each of the following functions at the given number.**

**a. f(x) = (x³ + 3x)/x² at x = 2**

**Answer:** f′(2) = 1/4

**Why:**
Simplify first (x ≠ 0): f(x) = x³/x² + 3x/x² = x + 3x^(−1)
Sum rule, power rule: f′(x) = 1 + 3(−1)x^(−2) = 1 − 3/x²
f′(2) = 1 − 3/4 = 1/4
Check with quotient rule: f′ = ((3x² + 3)x² − (x³ + 3x)(2x))/x⁴ = (3x⁴ + 3x² − 2x⁴ − 6x²)/x⁴ = (x⁴ − 3x²)/x⁴; at 2: (16 − 12)/16 = 4/16 = 1/4 ✓

**b. f(x) = 5/(x³ + 2) at x = −4**

**Answer:** f′(−4) = −60/961

**Why:**
Quotient rule (or chain rule on 5(x³ + 2)^(−1)): f′(x) = (0·(x³ + 2) − 5·3x²)/(x³ + 2)² = −15x²/(x³ + 2)²
At x = −4: x² = 16, x³ + 2 = −64 + 2 = −62, (−62)² = 3844
f′(−4) = −15(16)/3844 = −240/3844 = −60/961 ≈ −0.0624

**c. f(x) = x⁴/(x³ + 2) at x = 2**

**Answer:** f′(2) = 32/25

**Why:**
Quotient rule: f′(x) = (4x³(x³ + 2) − x⁴·3x²)/(x³ + 2)²
Numerator: 4x⁶ + 8x³ − 3x⁶ = x⁶ + 8x³
f′(x) = (x⁶ + 8x³)/(x³ + 2)²
At x = 2: x⁶ = 64, 8x³ = 64, numerator = 128; x³ + 2 = 10, denominator = 100
f′(2) = 128/100 = 32/25 = 1.28

**d. f(x) = 4√x/(2x + 1) at x = 4**

**Answer:** f′(4) = −7/81

**Why:**
Quotient rule with u = 4√x, v = 2x + 1
u′ = 4 · 1/(2√x) = 2/√x (derivative of √x from the Summary), v′ = 2
f′(x) = (u′v − uv′)/v² = ((2/√x)(2x + 1) − 4√x · 2)/(2x + 1)²
At x = 4: √x = 2, so u′ = 1, u = 8, v = 9, v′ = 2
f′(4) = (1·9 − 8·2)/9² = (9 − 16)/81 = −7/81 ≈ −0.0864

**2. The diagram in Figure 2.40 shows the graph of the function y = 1/x between x = 1/2 and x = 4.**

[figure: Figure 2.40 — graph of f(x) = 1/x for x > 0 on a grid, from about (0.33, 3) falling through (1, 1) and (2, 0.5) to about (5, 0.2).]

i. Find the slope of the secant line between

**a. x = 3 and x = 3.1.**

**Answer:** −10/93 ≈ −0.1075

**Why:**
Slope = (f(3.1) − f(3))/(3.1 − 3)
f(3.1) = 1/3.1 = 10/31, f(3) = 1/3
f(3.1) − f(3) = 10/31 − 1/3 = (30 − 31)/93 = −1/93
Divide by 0.1: (−1/93)/0.1 = −10/93 ≈ −0.10753

**b. x = 3 and x = 3.01.**

**Answer:** −100/903 ≈ −0.1107

**Why:**
f(3.01) = 1/3.01 = 100/301
f(3.01) − f(3) = 100/301 − 1/3 = (300 − 301)/903 = −1/903
Divide by 0.01: −100/903 ≈ −0.11074

**c. x = 3 and x = 3.001.**

**Answer:** −1000/9003 ≈ −0.1111

**Why:**
f(3.001) = 1000/3001
f(3.001) − f(3) = (3000 − 3001)/9003 = −1/9003
Divide by 0.001: −1000/9003 ≈ −0.11107

**ii. Find a formula for the slope of the secant line between (3, f(3)) and (3 + Δx, f(3 + Δx)) for a function f.**

**Answer:** Slope = (f(3 + Δx) − f(3))/Δx; for f(x) = 1/x this is −1/(3(3 + Δx)) = −1/(9 + 3Δx)

**Why:**
General: slope = change in y / change in x = (f(3 + Δx) − f(3))/((3 + Δx) − 3) = (f(3 + Δx) − f(3))/Δx
For f(x) = 1/x: f(3 + Δx) − f(3) = 1/(3 + Δx) − 1/3 = (3 − (3 + Δx))/(3(3 + Δx)) = −Δx/(3(3 + Δx))
Divide by Δx: −1/(3(3 + Δx))
Check with Δx = 0.1: −1/(3 × 3.1) = −1/9.3 = −10/93 ✓

**iii. Determine what happens when Δx approaches 0.**

**Answer:** The slope approaches −1/9 ≈ −0.111, the slope of the tangent line at x = 3 (f′(3) = −1/9).

**Why:**
As Δx → 0, 3(3 + Δx) → 9, so −1/(3(3 + Δx)) → −1/9
This matches the table: −0.1075, −0.1107, −0.1111 …
Check with the power rule: f′(x) = −x^(−2), f′(3) = −1/9 ✓

**3. If an object is dropped from an 80 m high window, its height y above the ground at the time t seconds is given by the formula y = f(t) = 80 − 4.9t² (neglect air resistance).**

i. Find the average velocity of the falling object between

**a. t = 1 sec and t = 1.1 sec.**

**Answer:** −10.29 m/s

**Why:**
f(1) = 80 − 4.9 = 75.1
f(1.1) = 80 − 4.9(1.21) = 80 − 5.929 = 74.071
Average velocity = (74.071 − 75.1)/(1.1 − 1) = −1.029/0.1 = −10.29 m/s (negative: height is decreasing)

**b. t = 1 sec and t = 1.01 sec.**

**Answer:** −9.849 m/s

**Why:**
f(1.01) = 80 − 4.9(1.0201) = 80 − 4.99849 = 75.00151
(75.00151 − 75.1)/0.01 = −0.09849/0.01 = −9.849 m/s

**c. t = 1 sec and t = 1.001 sec.**

**Answer:** −9.8049 m/s

**Why:**
f(1.001) = 80 − 4.9(1.002001) = 80 − 4.9098049 = 75.0901951
(75.0901951 − 75.1)/0.001 = −0.0098049/0.001 = −9.8049 m/s

(p.156)

**ii. Find a simple formula for the average velocity of the falling object between t = 1 sec and t = (1 + Δt) sec.**

**Answer:** Average velocity = −9.8 − 4.9Δt m/s

**Why:**
f(1 + Δt) = 80 − 4.9(1 + 2Δt + Δt²) = 80 − 4.9 − 9.8Δt − 4.9Δt²
f(1 + Δt) − f(1) = (75.1 − 9.8Δt − 4.9Δt²) − 75.1 = −9.8Δt − 4.9Δt²
Divide by Δt: −9.8 − 4.9Δt
Check Δt = 0.1: −9.8 − 0.49 = −10.29 ✓

**iii. Determine what happens to this average velocity as Δt approaches 0.**

**Answer:** It approaches −9.8 m/s, the instantaneous velocity at t = 1 s (the object falls at 9.8 m/s).

**Why:**
As Δt → 0, −4.9Δt → 0, so −9.8 − 4.9Δt → −9.8
Check: f′(t) = −9.8t, f′(1) = −9.8 ✓

**4. Let y = f(t) = t² where t is the time in seconds and y is the distance in meters that an object falls on a certain airless planet. Draw a graph of this function between t = 0 and t = 3.**

**Answer (graph):** the right half of a parabola through (0, 0), (1, 1), (2, 4), (3, 9), increasing and curving upward.

**Why:**
Table of values: t = 0, 1, 2, 3 gives y = 0, 1, 4, 9; plot and join with a smooth curve.

i. Make a table of the average speed of the falling object between

**a. t = 2 sec and t = 3 sec.**
**b. t = 2 sec and t = 2.1 sec.**
**c. t = 2 sec and t = 2.01 sec.**

**Answer:**

| Interval | Δt | f(2 + Δt) − f(2) | Average speed (m/s) |
|---|---|---|---|
| a. [2, 3] | 1 | 9 − 4 = 5 | 5 |
| b. [2, 2.1] | 0.1 | 4.41 − 4 = 0.41 | 4.1 |
| c. [2, 2.01] | 0.01 | 4.0401 − 4 = 0.0401 | 4.01 |

**Why:**
Average speed = (f(t₂) − f(t₁))/(t₂ − t₁)
a: (3² − 2²)/(3 − 2) = (9 − 4)/1 = 5
b: (2.1² − 2²)/0.1 = (4.41 − 4)/0.1 = 0.41/0.1 = 4.1
c: (2.01² − 2²)/0.01 = (4.0401 − 4)/0.01 = 0.0401/0.01 = 4.01

**ii. Find a simple formula for the average speed between time t = 2 sec and t = (2 + Δt) sec.**

**Answer:** Average speed = 4 + Δt m/s

**Why:**
f(2 + Δt) = (2 + Δt)² = 4 + 4Δt + Δt²
f(2 + Δt) − f(2) = 4Δt + Δt²
Divide by Δt: 4 + Δt
Check Δt = 0.1: 4.1 ✓

**iii. In your formula for average speed determine what happens as Δt approaches zero.**

**Answer:** It approaches 4 m/s (instantaneous velocity at t = 2).

**Why:**
As Δt → 0, 4 + Δt → 4
Check: f′(t) = 2t, f′(2) = 4 ✓

**iv. Draw the straight line through the point (2, 4) whose slope is the instantaneous velocity you just computed.**

**Answer:** y = 4t − 4 (the tangent line to y = t² at (2, 4)); it passes through (1, 0) and (3, 8).

**Why:**
Point-slope form: y − 4 = 4(t − 2)
y = 4t − 8 + 4 = 4t − 4
Points to plot: t = 1 → y = 0; t = 3 → y = 8; it touches the parabola only at (2, 4).

**5. Find the equation of the tangent and the normal lines f(x) = (1 − x³)√(x + 2).**

[review: the book gives no point at which to find the tangent and normal. Below: the general formulas, then worked at x = −1 (gives whole numbers) and at x = 1 (where the curve crosses the x-axis). The intended point needs to be confirmed.]

**Answer:** f′(x) = (1 − 12x² − 7x³)/(2√(x + 2)). At x = −1: tangent y = −2x, normal y = (1/2)x + 5/2. At x = 1: tangent y = −3√3(x − 1), normal y = (√3/9)(x − 1).

**Why:**
Product rule: u = 1 − x³, v = √(x + 2) = (x + 2)^(1/2)
u′ = −3x²
Chain rule: v′ = (1/2)(x + 2)^(−1/2) · 1 = 1/(2√(x + 2))
f′(x) = u′v + uv′ = −3x²√(x + 2) + (1 − x³)/(2√(x + 2))
Common denominator 2√(x + 2): −3x²√(x + 2) = −6x²(x + 2)/(2√(x + 2)) = (−6x³ − 12x²)/(2√(x + 2))
f′(x) = (−6x³ − 12x² + 1 − x³)/(2√(x + 2)) = (1 − 12x² − 7x³)/(2√(x + 2))
At x = −1: f(−1) = (1 − (−1))√1 = 2; f′(−1) = (1 − 12 + 7)/(2·1) = −4/2 = −2
Tangent: y = f′(a)(x − a) + f(a) = −2(x + 1) + 2 = −2x
Normal: y = (−1/f′(a))(x − a) + f(a) = (1/2)(x + 1) + 2 = (1/2)x + 5/2
At x = 1: f(1) = 0 · √3 = 0; f′(1) = (1 − 12 − 7)/(2√3) = −18/(2√3) = −9/√3 = −3√3
Tangent: y = −3√3(x − 1)
Normal: y = (1/(3√3))(x − 1) = (√3/9)(x − 1)

**6. Find the derivative of each of the following functions.**

**a. f(x) = x²(2x + 5)**

**Answer:** f′(x) = 6x² + 10x

**Why:**
Expand: f(x) = 2x³ + 5x²
Power rule, constant multiple, sum rule: f′(x) = 6x² + 10x
Check with product rule: 2x(2x + 5) + x²(2) = 4x² + 10x + 2x² = 6x² + 10x ✓

**b. f(x) = (x² + x)/(x³ − x + 2)**

**Answer:** f′(x) = (−x⁴ − 2x³ − x² + 4x + 2)/(x³ − x + 2)²

**Why:**
Quotient rule: u = x² + x, u′ = 2x + 1; v = x³ − x + 2, v′ = 3x² − 1
u′v = (2x + 1)(x³ − x + 2) = 2x⁴ − 2x² + 4x + x³ − x + 2 = 2x⁴ + x³ − 2x² + 3x + 2
uv′ = (x² + x)(3x² − 1) = 3x⁴ − x² + 3x³ − x = 3x⁴ + 3x³ − x² − x
u′v − uv′ = (2 − 3)x⁴ + (1 − 3)x³ + (−2 + 1)x² + (3 + 1)x + 2 = −x⁴ − 2x³ − x² + 4x + 2
f′(x) = (−x⁴ − 2x³ − x² + 4x + 2)/(x³ − x + 2)²
Numerical check at x = 0: formula gives 2/4 = 1/2; difference quotient (f(0.001) − f(0))/0.001 ≈ 0.5 ✓

**c. f(x) = x²/(x + 1)**

**Answer:** f′(x) = (x² + 2x)/(x + 1)² = x(x + 2)/(x + 1)²

**Why:**
Quotient rule: u = x², u′ = 2x; v = x + 1, v′ = 1
u′v − uv′ = 2x(x + 1) − x² = 2x² + 2x − x² = x² + 2x
f′(x) = (x² + 2x)/(x + 1)²

**d. f(x) = x³(1 − 1/x)(x² − 1/x²)**

**Answer:** f′(x) = 5x⁴ − 4x³ − 1

**Why:**
Multiply out first: (1 − 1/x)(x² − 1/x²) = x² − 1/x² − x + 1/x³
Multiply by x³: x⁵ − x − x⁴ + 1, so f(x) = x⁵ − x⁴ − x + 1 (for x ≠ 0)
Power rule, sum rule: f′(x) = 5x⁴ − 4x³ − 1
Check at x = 1: f(x) = (x − 1)(x⁴ − 1); product rule gives f′(1) = 1·0 + 0 = 0, and 5 − 4 − 1 = 0 ✓

**7. Consider the function f(x) = 6x⁵ − 50x³ − 120.**

f′(x) = 30x⁴ − 150x² = 30x²(x² − 5) = 30x²(x − √5)(x + √5). Critical values: x = −√5, 0, √5.

| Interval | sign of 30x² | sign of x² − 5 | f′(x) | f |
|---|---|---|---|---|
| x < −√5 | + | + | + | increasing |
| −√5 < x < 0 | + | − | − | decreasing |
| 0 < x < √5 | + | − | − | decreasing |
| x > √5 | + | + | + | increasing |

**a. Find the interval on which f is increasing.**

**Answer:** (−∞, −√5] and [√5, ∞)

**Why:**
f′(x) > 0 when x² − 5 > 0, i.e. x < −√5 or x > √5 (30x² > 0 there). Test x = 3: f′(3) = 30·9·4 = 1080 > 0 ✓

**b. Find the interval on which f is decreasing.**

**Answer:** [−√5, √5]

**Why:**
f′(x) < 0 when x² < 5 and x ≠ 0; at x = 0, f′(0) = 0 but f′ is negative on both sides, so f keeps decreasing through 0. Test x = 1: f′(1) = 30 − 150 = −120 < 0 ✓

**c. Find all values of x for which f have a relative maximum.**

**Answer:** x = −√5 (relative maximum value f(−√5) = 100√5 − 120 ≈ 103.6)

**Why:**
First-derivative test: f′ changes from + to − at x = −√5
f(−√5): (−√5)⁵ = −25√5, (−√5)³ = −5√5
f(−√5) = 6(−25√5) − 50(−5√5) − 120 = −150√5 + 250√5 − 120 = 100√5 − 120 ≈ 103.61

**d. Find all values of x for which f have a relative minimum.**

**Answer:** x = √5 (relative minimum value f(√5) = −100√5 − 120 ≈ −343.6)

**Why:**
f′ changes from − to + at x = √5
f(√5) = 6(25√5) − 50(5√5) − 120 = 150√5 − 250√5 − 120 = −100√5 − 120 ≈ −343.61
x = 0 is a critical value but f′ does not change sign there, so there is no extremum at 0.

(p.157)

**8. A particle moves along the curve 2y = x² + 4. Find the point(s) on the curve at which the y-coordinate changes 4 times as fast as the x-coordinate.**

**Answer:** (4, 10)

**Why:**
Differentiate both sides with respect to time t (chain rule): 2 dy/dt = 2x dx/dt
So dy/dt = x · dx/dt
Condition: dy/dt = 4 dx/dt
x · dx/dt = 4 dx/dt → x = 4 (dx/dt ≠ 0)
y = (x² + 4)/2 = (16 + 4)/2 = 10
Point: (4, 10)

**9. Let f(x) = x² + px + q. Find the values of p and q such that f(1) = 3 is an extreme value of f on the interval [0, 2]. Is this value maximum or minimum?**

**Answer:** p = −2, q = 4; f(1) = 3 is a minimum.

**Why:**
f′(x) = 2x + p
1 is inside (0, 2), so an extreme value there needs f′(1) = 0: 2 + p = 0 → p = −2
f(1) = 3: 1 + p + q = 3 → 1 − 2 + q = 3 → q = 4
f(x) = x² − 2x + 4 = (x − 1)² + 3 ≥ 3
f′ changes from − (x < 1) to + (x > 1), so f(1) = 3 is a minimum
Check endpoints: f(0) = 4, f(2) = 4 > 3 ✓

**10. Find the value of a, b, c, d so that h(x) = ax³ + bx² + cx + d will be extreme values at (1, 2) and (2, 3).**

**Answer:** a = −2, b = 9, c = −12, d = 7, so h(x) = −2x³ + 9x² − 12x + 7 (minimum at (1, 2), maximum at (2, 3))

**Why:**
h′(x) = 3ax² + 2bx + c
Extreme at x = 1: h′(1) = 3a + 2b + c = 0 … (1)
Extreme at x = 2: h′(2) = 12a + 4b + c = 0 … (2)
Point (1, 2): a + b + c + d = 2 … (3)
Point (2, 3): 8a + 4b + 2c + d = 3 … (4)
(2) − (1): 9a + 2b = 0 → b = −9a/2
(4) − (3): 7a + 3b + c = 1 … (5)
(5) − (1): 4a + b = 1
Substitute b: 4a − 9a/2 = 1 → −a/2 = 1 → a = −2
b = −9(−2)/2 = 9
From (1): 3(−2) + 2(9) + c = 0 → −6 + 18 + c = 0 → c = −12
From (3): −2 + 9 − 12 + d = 2 → −5 + d = 2 → d = 7
Check: h(1) = −2 + 9 − 12 + 7 = 2 ✓; h(2) = −16 + 36 − 24 + 7 = 3 ✓; h′(x) = −6x² + 18x − 12 = −6(x − 1)(x − 2) ✓
h′ changes − to + at 1 (minimum), + to − at 2 (maximum)

**11. Find the absolute maximum and the minimum values of the following function on the interval [0, 2].**

f(x) = x³ − x/3 ; 0 ≤ x ≤ 1
f(x) = x² + x − 4/3 ; 1 < x ≤ 2

**Answer:** Absolute maximum 14/3 (at x = 2); absolute minimum −2/27 (at x = 1/3)

**Why:**
Piece 1 (0 ≤ x ≤ 1): f′(x) = 3x² − 1/3 = 0 → x² = 1/9 → x = 1/3 (x = −1/3 is outside)
f(1/3) = 1/27 − 1/9 = 1/27 − 3/27 = −2/27
Piece 2 (1 < x ≤ 2): f′(x) = 2x + 1 > 0, no critical value inside
At x = 1: left value 1 − 1/3 = 2/3; right-hand limit 1 + 1 − 4/3 = 2/3, so f is continuous; left slope 3 − 1/3 = 8/3, right slope 2 + 1 = 3, so f′(1) does not exist → x = 1 is a critical value
Candidates: f(0) = 0, f(1/3) = −2/27, f(1) = 2/3, f(2) = 4 + 2 − 4/3 = 14/3
Largest: 14/3 at x = 2; smallest: −2/27 at x = 1/3

**12. A board 5 ft long slides down a wall. At the instant when the bottom end is 4 ft from the wall, the other end is moving down at a rate of 2 ft/s. At that moment**

Let x = distance of the bottom from the wall, y = height of the top. x² + y² = 25. At the instant: x = 4, y = √(25 − 16) = 3, dy/dt = −2 ft/s.

**a. How fast is the bottom end sliding along the ground?**

**Answer:** 3/2 = 1.5 ft/s (away from the wall)

**Why:**
Differentiate x² + y² = 25 with respect to t (chain rule): 2x dx/dt + 2y dy/dt = 0
Substitute: 2(4) dx/dt + 2(3)(−2) = 0
8 dx/dt − 12 = 0 → dx/dt = 12/8 = 3/2 ft/s

**b. How fast is the area of the region between the board, the ground, and the wall changing?**

**Answer:** −7/4 = −1.75 ft²/s (the area is decreasing at 1.75 ft²/s)

**Why:**
Area of the right triangle: A = (1/2)xy
Product rule: dA/dt = (1/2)(dx/dt · y + x · dy/dt)
Substitute: dA/dt = (1/2)((3/2)(3) + 4(−2)) = (1/2)(9/2 − 8) = (1/2)(−7/2) = −7/4 ft²/s

**13. A farmer has 240 m of fencing material and wants to fence a rectangular field that borders a straight river. (No fence is needed along the river). What are the dimensions of the field that has the largest area?**

**Answer:** 60 m (each side perpendicular to the river) by 120 m (the side parallel to the river); largest area 7200 m²

**Why:**
Let x = each side perpendicular to the river, y = side parallel to the river
Fence: 2x + y = 240 → y = 240 − 2x, with 0 < x < 120
Area: A(x) = x(240 − 2x) = 240x − 2x²
A′(x) = 240 − 4x = 0 → x = 60
A′ changes + to − at 60 (A″ = −4 < 0), so maximum
y = 240 − 120 = 120; A = 60 × 120 = 7200 m²

**14. The radius of the balloon is increasing at the rate of 0.5 cm/sec. At what rate the surface area of the balloon is increasing when the radius is 4 cm?**

**Answer:** 16π cm²/s ≈ 50.27 cm²/s

**Why:**
Surface area of a sphere: S = 4πr²
Chain rule: dS/dt = 8πr · dr/dt
Substitute r = 4, dr/dt = 0.5: dS/dt = 8π(4)(0.5) = 16π ≈ 50.27 cm²/s

**15. A cyclist decelerates at a constant rate from 30 km/hr to a standstill in 45 sec.**

Convert: 30 km/h = 30 × 1000/3600 m/s = 25/3 m/s ≈ 8.33 m/s. Constant deceleration: a = (0 − 25/3)/45 = −25/135 = −5/27 m/s². So v(t) = 25/3 − (5/27)t, 0 ≤ t ≤ 45.

**a. How fast is the bicyclist traveling after 20 sec?**

**Answer:** 125/27 ≈ 4.63 m/s (= 50/3 ≈ 16.7 km/h)

**Why:**
v(20) = 25/3 − (5/27)(20) = 225/27 − 100/27 = 125/27 ≈ 4.63 m/s
In km/h: 30 × (45 − 20)/45 = 30 × 25/45 = 50/3 ≈ 16.67 km/h ✓ (same speed)

**b. How far has the bicyclist traveled after 45 sec?**

**Answer:** 187.5 m

**Why:**
Distance = ∫_{0}^{45} v(t) dt = ∫_{0}^{45} (25/3 − (5/27)t) dt
Anti-derivative: s(t) = (25/3)t − (5/54)t²
Upper limit: s(45) = (25/3)(45) − (5/54)(2025) = 375 − 187.5 = 187.5
Lower limit: s(0) = 0
Distance = 187.5 − 0 = 187.5 m
Check (area of the triangle under the v–t graph): (1/2)(45)(25/3) = 187.5 ✓

**16. A factory is polluting a lake in such a way that the rate of pollutants entering the lake at time t, in months, is given by N′(t) = 280t^(3/2), where N is the total number of pounds of pollutants in the lake at time t.**

(p.158)

[figure: Figure 2.41 — photograph of a polluted lake/river with bright orange water and green vegetation on the bank.]

**a. How many pounds of pollutants enter the lake in 16 months?**

**Answer:** 114 688 pounds

**Why:**
Pollutants = ∫_{0}^{16} 280t^(3/2) dt
Power rule: ∫ t^(3/2) dt = t^(5/2)/(5/2) = (2/5)t^(5/2), so anti-derivative = 280 × (2/5)t^(5/2) = 112t^(5/2)
Upper limit: 16^(5/2) = (√16)⁵ = 4⁵ = 1024; 112 × 1024 = 114 688
Lower limit: 112 × 0 = 0
Total = 114 688 − 0 = 114 688 pounds

**b. An environmental board tells the factory that it must begin to clean up procedures after 50,000 pounds of pollutants has entered the lake. After what length of time will this occur?**

**Answer:** T = 25/7^(2/5) ≈ 11.48 months (about 11.5 months)

**Why:**
∫_{0}^{T} 280t^(3/2) dt = 112T^(5/2) − 0 = 50 000
T^(5/2) = 50 000/112 = 3125/7 ≈ 446.43
Raise both sides to the power 2/5: T = (3125/7)^(2/5) = 3125^(2/5)/7^(2/5)
3125 = 5⁵, so 3125^(2/5) = 5² = 25; 7^(2/5) ≈ 2.178
T ≈ 25/2.178 ≈ 11.48 months
Check: 112 × 11.48^(5/2) ≈ 112 × 446.5 ≈ 50 000 ✓

(p.159) Pages 159–161 are the start of Unit 3 "Statistics" (unit opener, key words and introduction, 3.1 Measures of Absolute Dispersions); not transcribed here.

## Notes for lesson design
### u2-a

**Key ideas by subsection**
- Unit opener / Introduction: calculus is the mathematics of change. The derivative is the exact rate of change, and geometrically it is the slope of the tangent line.
- 2.1.1 Rates of change: a rate of change is (change in output)/(change in input), measured in output units per input unit. It can be positive, negative, zero or undefined (vertical line). Average rate of change on [a, b] is (f(b) − f(a))/(b − a). The instantaneous rate is the limit of (f(x₀ + h) − f(x₀))/h as h → 0. The method is always: expand, cancel the constant terms, divide by h, then let h → 0.
- 2.1.2 Gradient of curves: slope of a secant line = average rate of change. Slope from two points: (y₁ − y₀)/(x₁ − x₀).
- 2.1.3 Gradient at a point: secant lines PQ tend to the tangent at P as Q → P (h → 0). Procedure: form (f(x) − f(a))/(x − a), simplify by factorising (difference of squares or cubes) or by rationalising, then let x → a. For y = x², m_tan = 2a.
- 2.1.4.1 Derivative at a point (Def 2.6): f′(a) = lim_{h→0} (f(a + h) − f(a))/h, the slope of the tangent line at (a, f(a)).
- 2.1.4.2 Derivative as a function (Def 2.7): f′(x) is defined only where the limit exists and is the same from both sides (|x| at 0 fails). The other form is (f(t) − f(x))/(t − x) with t → x. Notations: f′(x), dy/dx, d/dx f(x), Df(x), D_x f. Standard results: (k)′ = 0, (x²)′ = 2x, (√x)′ = 1/(2√x), (1/x)′ = −1/x².
- 2.1.4.3 Power rule (Theorem 2.1): (xⁿ)′ = n x^(n−1). It is proved here for positive integers using tⁿ − xⁿ = (t − x)(t^(n−1) + … + x^(n−1)). Activity 2.7 also checks it for n = −2.

**Common student mistakes to expect**
- Putting x₁ − x₂ under y₂ − y₁ (mixing the order of the points), and sign slips when subtracting a negative, e.g. 3 − (−3).
- Treating 2/0 as 0, or treating 0/2 as "undefined". Students need to keep the zero and undefined cases apart: a horizontal line has slope 0, a vertical line has an undefined slope.
- Expanding (a + h)² as a² + h². Forgetting to multiply every term by the coefficient, e.g. 2(h² − 6h + 9). Dropping the bracket in − (f(a)), so that the constant term does not cancel.
- Putting h = 0 before cancelling h, which gives 0/0. Or cancelling h in a term that does not contain h.
- When rationalising, multiplying only the numerator by the conjugate, or making errors with (√A − √B)(√A + √B) = A − B.
- Mixing up the average rate (over an interval) with the instantaneous rate (at a point). Also giving no units or the wrong units (mg/min, m/s, Birr/year).
- Reading |x| as differentiable at 0 because it is continuous there. Forgetting that 1/x and √x have restricted domains.
- Power rule with negative exponents: writing (x^(−2))′ = −2x^(−1) instead of −2x^(−3).
- Note for content review: Def 2.4a says a tangent "does not cross the curve". This is not true at inflection points, so avoid quiz items that depend on it.

**Interactive practice with generated numbers**
- Slope or rate of change from two random integer points (x₁, y₁), (x₂, y₂). Include cases where the slope is zero and where it is undefined. The learner also classifies the sign.
- Average rate of change of a random polynomial a x² + b x + c or a x³ + b x on a random interval [p, q].
- Reading average speed from a generated distance–time table, as in Example 2 (car).
- Instantaneous rate by the h-method for f(x) = a x² + c at a random x₀, with a step-by-step expansion checker. The answer is 2a x₀.
- Derivative at a point by Def 2.6 for: linear m x + c, quadratic x² + k, cubic x³ + b x, and √(p x + q). Choose numbers so that p a + q is a perfect square, which gives clean answers.
- Tangent gradient of y = x² at a random a (m = 2a), and of x³ (m = 3a²). Show a table like the one on p.79.
- Power rule drill: (a xⁿ)′ at x₀ with random a, n (including negative n) and x₀.
- Table that shrinks h (0.1, 0.01, 0.001, …). The learner computes the quotients and predicts the limit, as in Activity 2.2.

**Interactive pictures**
- Secant line sliding to the tangent as h → 0 on y = x³ at x = 1 (or a chosen f and a). Show the live slope readout 3.31 → 3.003… → 3.
- Draggable points A and B on a curve. The secant line and its slope (the average rate of change) update as they move, as in Figures 2.5 and 2.6.
- Tangent line moving along y = x², with the slope shown as 2a at each point, as in Figure 2.9. A companion plot traces the derivative graph y = 2x.
- Activity 2.6 explorer: zoom in on |x| at 0. Left and right secant slopes stay at −1 and +1, compared with x², where they meet.
- Sign-of-slope gallery (Figures 2.1–2.3): the learner drags a line and sees the rate change between positive, negative, zero and undefined.

### u2-b

**Key ideas by subsection**
- Power rule (Theorem 2.1, Corollaries 2.1–2.2): d/dx xⁿ = n x^(n−1) for positive and negative integers, and kxⁿ → knx^(n−1). The exercises quietly extend it to rational exponents (√x, x^(4/3)); lessons should say so explicitly.
- Sum/difference rule (Theorem 2.2, Corollary 2.3) and constant multiple rule (Theorem 2.3) together give the polynomial rule: differentiate term by term. Notation dy/dx|_{x=a} means "differentiate, then substitute".
- Product rule (Theorem 2.4): (fg)′ = f′g + fg′. Activity 2.10 shows (fg)′ ≠ f′g′.
- Quotient rule (Theorem 2.5): (1/g)′ = −g′/g² and (f/g)′ = (f′g − fg′)/g², proved by writing f/g = f · (1/g).
- Chain rule (2.1.4.4, Theorem 2.6): (f ∘ g)′(x) = f′(g(x)) · g′(x) — "derivative of the outside at the inside, times the derivative of the inside".
- 2.1.5.1 Increasing/decreasing: Definition 2.8, the sign of f′ decides rising/falling; critical numbers (Definition 2.9) are where f′ = 0 or f′ does not exist (in the domain); sign charts organise the work.
- 2.1.5.2 Extrema: local vs absolute (Definitions 2.10–2.11); closed-interval method (check critical numbers and endpoints); first derivative test (sign change − to + ⇒ min, + to − ⇒ max, no change ⇒ neither); finding unknown coefficients from f(c) and f′(c) = 0.
- 2.1.6 Tangent and normal lines: tangent y = f′(a)(x − a) + f(a); normal y = −(1/f′(a))(x − a) + f(a); special horizontal/vertical cases.

**Common student mistakes to anticipate**
- Power rule on negative exponents: writing x⁻⁷ → −7x⁻⁶ (adding instead of subtracting 1). On fractional exponents: −3/2 − 1 computed as −1/2.
- Treating a constant like √3 or (1/10) as a variable, or writing d/dx(constant) ≠ 0.
- Forgetting to rewrite 1/xⁿ and √x as powers before differentiating.
- Product rule: (fg)′ = f′g′. Quotient rule: reversing the order of the numerator (fg′ − f′g) or forgetting to square the denominator.
- Chain rule: forgetting the inner derivative (e.g. (5x + 4)²¹ → 21(5x + 4)²⁰ without × 5 — the book's own first line nearly does this).
- Sign errors when expanding −(x³ + 2x)(...) or −(2x³ + 3)(1) in quotient numerators.
- Critical numbers: forgetting points where f′ is undefined (x = 0 for √x, x = ±1 for √(1 − x²)), or including points not in the domain (x = ±1 for 2x²/(1 − x²)).
- Closed-interval extrema: forgetting the endpoints, or including critical numbers outside the interval.
- First derivative test: mixing up "max value" (the y-value) with "where" (the x-value); the book itself swaps max/min values in Example 1b.
- Normal line slope: using 1/f′(a) instead of −1/f′(a); confusion when f′(a) = 0.
- Writing "increasing on [−1, 0] ∪ [2, ∞)" and thinking f is increasing across the whole union.

**Good candidates for interactive practice with generated numbers**
- Power rule on k·x^n with random integer k and integer or simple fractional n (check by numerical difference quotient).
- Polynomial term-by-term differentiation, then evaluate dy/dx|_{x=a} at a random integer a.
- Product rule on (ax + b)(cx² + d) with random coefficients; let students verify by expanding first.
- Quotient rule on (ax + b)/(cx + d) and on 1/(x² + k); numerator simplification step by step.
- Chain rule on (ax + b)ⁿ, √(ax² + bx + c), and ((ax + b)/(cx + d))ⁿ.
- Critical numbers and sign charts for cubics built from chosen roots: f′(x) = k(x − r₁)(x − r₂) → integrate to get f; students build the sign chart and classify each root.
- Absolute extrema on [a, b] for quadratics/cubics with random intervals (some with critical numbers outside the interval).
- "Find a and b" from f(c) = value and f′(c) = 0 for f(x) = x³ + ax + b or ax³ + bx + k.
- Tangent and normal lines to polynomials at random integer points; drag-a-point visual showing the tangent slope equal to f′(a) and the perpendicular normal.

### u2-c

**Key ideas by subsection**
- 2.1 (end, vertical tangents): a vertical tangent occurs at a domain point where f′ is undefined because its denominator → 0 while |f′| → ∞ (typically endpoints of a square-root domain). Tangent slope m = f′(a); normal slope −1/m.
- Activity 2.15: an increasing function on a closed interval attains its min/max at the endpoints; on an open interval it may have no min/max. This is the motivation for optimisation.
- 2.2.1 Rate of change (related rates): write the relation between quantities (A = πr², V = (4/3)πr³, similar triangles), differentiate with respect to t using the chain rule, then substitute the instant's values last. Velocity = dS/dt, acceleration = dv/dt.
- 2.2.2 Business: marginal cost/revenue/profit = derivatives; profit P = R − C; revenue = price × quantity; optimum where the marginal function = 0, confirmed by a sign chart (+ to − ⇒ max). Chain rule for rates per day: dR/dt = R′(x)·dx/dt.
- 2.2.3 Road taxation: average cost per mile M = C/x; minimise by M′ = 0, reject negative roots, check − to + ⇒ min.
- Exercise 2.20 introduces classic optimisation (fencing, open box, can): use the constraint to eliminate a variable, then differentiate one-variable functions.
- 2.3.1 Areas of regions: for a rate function, area under the graph = accumulated total (distance, cost, profit); units = input × output units. Rectangles/triangles/trapezoids give exact areas for constant and linear functions.
- Riemann sums: sigma notation; Δx = (b − a)/n; the book uses left endpoints; more rectangles ⇒ better approximation; lower sum ≤ area ≤ upper sum.
- 2.3.2 Definite integral: the limit of Riemann sums as Δx → 0 = exact area (f ≥ 0); for linear f compute it by geometry. Anti-derivative: reverse of differentiation; all anti-derivatives differ by a constant (+ C).

**Foreseeable student mistakes**
- Substituting the instant's values (r = 6, x = 400) before differentiating, which turns a variable into a constant and gives a derivative of 0.
- Using the diameter instead of the radius (Example 1 of 2.2.1); forgetting the chain-rule factor dr/dt or ds/dt (the book's own printed step in Example 3 omits it).
- Normal slope written as 1/m or −m instead of −1/m.
- Calling any point where f′ = 0 a maximum without the sign chart; mixing up "+ to −" (max) and "− to +" (min) — the book itself slips in the theatre example.
- Not rejecting negative/impossible critical numbers (x = −4000 miles, negative radius).
- Open box: including a top in the surface area; can: forgetting top and bottom (2πr²).
- Shadow problem: setting up the similar triangles with x instead of x + s.
- Revenue: using the demand price P as revenue instead of R = x·P.
- Marginal profit at 50 units being positive while total profit is negative — students think they contradict.
- Riemann sums: using the right endpoint when told left (or vice versa), forgetting to multiply by Δx, or using the wrong number of endpoints (n + 1 instead of n).
- Sigma notation: starting the index at 0 or ending at the wrong value; for Σ(i² + i), adding only i².
- Definite integrals of lines: using the triangle formula when the region is a trapezoid (f(a) ≠ 0), e.g. ∫_{1}^{5} x dx.
- Anti-derivatives: forgetting + C, or thinking x² is "the" only anti-derivative of 2x.

**Ideas suited to interactive practice / interactive pictures**
- Tangent and normal at a draggable point on a curve; show f′(a) and −1/f′(a); move toward an endpoint of √(x² − 6x) to watch the tangent turn vertical.
- Activity 2.15: slider for the endpoints of S with an open/closed toggle; show the image set of f(x) = 3x + 2 and whether a min/max exists.
- Related rates with generated numbers: radius growth rate and radius → dA/dt; balloon dV/dt and r → dr/dt; animated lamp-post shadow (walker speed slider; shadow speed stays constant).
- Position–velocity–acceleration from S(t) = t³ − 3t² + 5t + 7 with a time slider (random cubic coefficients).
- Profit/revenue maximisation: slider on x showing P(x) and P′(x) together with the sign chart; theatre price-drop slider showing attendance, ticket + concession revenue and the peak at 21 Birr.
- Fencing with unequal costs (fixed area, slider on x showing cost); open box (fixed surface area, slider on the base side showing volume); cylinder (fixed volume, slider on r showing surface area, with the h = 2r result highlighted).
- Road tax: slider on annual mileage showing average cost per mile, minimum at 4000.
- Area under v(t) = mx or a constant as distance: drag the right end of the interval to see the triangle/rectangle/trapezoid area update (generated m, a, b).
- Riemann sums: slider for n, toggle left/right endpoint (lower/upper for increasing functions) on y = 2x, x² + 1 or 3x²; show the sum and the gap to the exact area shrinking.
- Sigma notation drill: generate Σ expressions to expand or write in sigma form, and evaluate small sums.
- Anti-derivative family: slider for C showing the parallel graphs of x² + C all with the same slope at a chosen x.

### u2-d

- **Indefinite integral / power rule (p.136–138):** key idea is "integration undoes differentiation": ∫ x^α dx = x^(α+1)/(α+1) + C, α ≠ −1, plus linearity (constants come out, sums split) and ∫ k dx = kx + C. Every answer can be checked by differentiating.
- **Area and definite integrals (2.3.3):** ∫_{a}^{b} f(x) dx = F(b) − F(a); any anti-derivative works (C cancels); FTC: A′(x) = f(x). Notation [F(x)]_{a}^{b}. Properties: reversing limits changes sign, splitting at c, linearity.
- **More on area (2.3.4):** the definite integral is a *signed* area. For f ≤ 0, area = −∫. For a graph crossing the axis, find the x-intercepts, split the interval, and add absolute values.
- **Applications (2.3.5):** integrating a rate gives the total change: marginal profit → profit, velocity → displacement/distance, rate of sales/pollution → total. Initial conditions fix C.
- **Mistakes students are likely to make:**
  - Adding 1 to a negative or fractional exponent wrongly (e.g. −4/3 + 1 = −1/3, not 1/3); the book's own Example 2(d) has this kind of slip.
  - Dividing by the old exponent instead of the new one; forgetting + C, or writing several C's.
  - Using the power rule on x^(−1) (Exercise 2.25c).
  - Sign errors when substituting the lower limit, especially with negative numbers: F(−1) for x³/3 is −1/3, and "minus a negative" becomes plus.
  - Treating ∫_{a}^{b} f dx as the area when f goes below the axis (Exercise 2.28 Q3: 9/4 vs the correct 37/12). The book's Example 4 on p.146 shows the same confusion.
  - Units in applications (km/h vs m/s in Q15; hundreds of dollars in the airline example).
  - Variable mix-ups (P′(t) written with x in Exercise 2.29).
- **Good for interactive practice with generated numbers:**
  - Power-rule drill: random α (integer, fraction, negative), student enters the anti-derivative and the app checks it by differentiating; include α = −1 as a "trap" card.
  - Definite-integral evaluator for a random polynomial on [a, b], scaffolded as F(x) → F(b) → F(a) → subtract, with each step checked separately.
  - Secant-to-tangent tables (Review Q2–Q4): pick f and a point, shrink Δx (1, 0.1, 0.01, …) and watch the average rate converge.
- **Good for interactive pictures:**
  - Area under y = x² from 0 to b as n rectangles (Riemann sum) with a slider for n → converges to b³/3; also for y = x² + 1 on [−1, 2] → 6 (Fig 2.29 "count the squares").
  - FTC slider: drag x, shade A(x) under f, and plot A(x) alongside; its slope equals f(x).
  - Signed area: f(x) = −x³ + 3x − 1 on [−1, 2] (Fig 2.39), with regions above the axis green (+) and below red (−), showing the net integral −9/4 next to the total area.
  - Reflection y = x² vs y = −x² on [0, 2] (8/3 vs −8/3).
  - Area-between-curve-and-axis tool: user drags a and b over x² − 1 or x(x + 2)(x − 1); the app finds the intercepts and splits the integral automatically.
  - Applications: a v–t graph whose shaded area is the distance (braking car, Example 3: 273.83 ft; cyclist Q15: triangle area 187.5 m); a slider for T in the pollution problem until the accumulated area reaches 50 000.
