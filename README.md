# tyselles_assignment_5.py

# Python Challenges – README

## Overview

This project contains three small Python programs (challenges) that demonstrate problem solving with loops, conditionals, and formatted output:

1. **Collatz Conjecture Sequence**
2. **Prime Number Checker**
3. **Multiplication Table**

---

## Challenge 1: Collatz Conjecture

**Why this loop type?**
I used a **`while` loop** because the number of steps needed to reach `1` is unknown in advance. A `while` loop is best for problems where the end condition is not fixed but depends on the data being processed.

**How it works:**

* Start with an integer input.
* If the number is even, divide by 2. If odd, multiply by 3 and add 1.
* Repeat until the sequence reaches `1`.
* Count and display the total number of steps.

---

## Challenge 2: Prime Number Checker

**Why this loop type?**
I used a **`for` loop** because the range of possible divisors (`2` to `num-1`) is known in advance. A `for` loop naturally handles iterating through this fixed range.

**How it works:**

* Take an integer input.
* Test each number from `2` to `num-1` to see if it divides evenly into the input.
* If a divisor is found, the number is not prime and the loop ends early with `break`.
* If no divisor is found, the number is declared prime.

---

## Challenge 3: Multiplication Table

**Why this loop type?**
I used **nested `for` loops** because both the rows and columns of the table have a fixed range (`1` to `10`). This makes `for` loops the clearest choice for structured output like a table.

**How it works:**

* The first loop generates rows.
* The inner loop generates columns within each row.
* The product of the row and column numbers is formatted neatly in a grid.

---

## AI Assistance

I used AI assistance (ChatGPT) to help with:

* Structuring the README file in a professional way.
* Double-checking clarity of explanations about **why certain loop types were chosen**.
* Ensuring consistent formatting and readability.

All code was written and understood by me; AI was used only for feedback and explanation support.
