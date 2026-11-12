# Numerical Analysis — University Assignment

A university coursework project for the **Numerical Analysis** course at **Aristotle University of Thessaloniki (AUTH)**.

The assignment covers numerical methods for finding roots, solving systems of linear equations, and studying the PageRank algorithm. The sections below summarize the **assignment requirements**, rather than claiming that every task has been implemented.

## Assignment overview

### 1. Root-Finding Methods

Study a nonlinear function on the interval [0, 3] and find its roots using:

- Bisection
- Newton–Raphson
- Secant method

Compare iteration counts across different starting values, and investigate when Newton–Raphson achieves quadratic convergence.

### 2. Modified Root-Finding Methods

Implement modified versions of the Newton–Raphson, bisection, and secant methods. Find the roots of a polynomial on the interval [-2, 2] and compare their convergence behavior with the classical methods through repeated experiments.

### 3. Systems of Linear Equations

Implement and explore:

- **PLU decomposition** for solving linear systems
- **Cholesky decomposition** for symmetric positive-definite matrices
- **Gauss–Seidel iteration** for sparse tridiagonal systems with 10 and 5,000 unknowns

The assignment requires implementing these methods without relying on built-in decomposition or direct-solve functions.

### 4. PageRank and the Power Method

Explore how search engines can rank web pages using a directed network of **15 pages**. Construct the Google matrix, use the **power method** to study PageRank, and investigate how changing links, the jump probability, or removing a page affects the rankings.

## Full assignment statement

The original **five-page assignment brief (in Greek)** contains all mathematical formulas, the 15-page network diagram, complete instructions, and detailed questions.

**[View the original assignment PDF](assignment.pdf)**[assignment.pdf](https://github.com/user-attachments/files/34753831/assignment.pdf)


## About this repository

This README provides an English-language overview of the coursework. Refer to the source files in this repository for the actual implementation, where available.
