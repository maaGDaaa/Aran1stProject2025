# Numerical Analysis — First Mandatory Assignment

**Course:** Numerical Analysis  
**Assignment:** 1st Mandatory Assignment  
**Submission deadline:** December 21, 2025, at 24:00

> This README is an English translation of the original assignment statement. It describes the **requirements**, not necessarily which parts have been implemented in this repository.

## General instructions

This is an individual assignment. A written report must be prepared in **LaTeX** (for the optional assignment to count) or in any other word processor (in which case the optional assignment does not count). The report must describe the solutions to the exercises, present and discuss the results, and explain how to run the code.

The report (as a `.pdf` file) and the source code files (in any programming language of your choice) must be compressed into one archive and submitted via eLearning by **December 21, 2025, at 24:00**.

For each day of late submission, up to five days, the grade is reduced by **10%**. After all assignments have been submitted, selected assignments will be subject to an oral examination or presentation, including an oral examination of the code in cases of suspected copying.

The use of language models (e.g., ChatGPT) is permitted **after first attempting to write the code independently**. If used, the assignment must explicitly state, at the beginning of the relevant exercise, which language model was used, what prompt was given, and which code it produced. The report must include both the student's independent attempt and the language model's output, together with an analysis of the differences between their code. Properly documented language-model use does not result in a grade reduction. Undisclosed use results in a grade of zero. In all cases, students must understand exactly what their code does and why.

For questions regarding the assignments, contact `avramell@csd.auth.gr` or `tefas@csd.auth.gr`.

---

## Exercise 1 — Root-finding methods (1 point)

Consider the function

$$
f(x)=14xe^{x-2}-12e^{x-2}-7x^3+20x^2-26x+12
$$

on the interval $[0,3]$.

1. Plot the function on this interval.
2. Write a program to calculate **all its roots to six decimal places** using:
   - (a) the **bisection method**;
   - (b) the **Newton–Raphson method**;
   - (c) the **secant method**.
3. For each root, compare the number of iterations needed by running the code **10 times with different initializations**.
4. For the Newton–Raphson method, demonstrate experimentally for which roots it converges quadratically and for which it does not.
5. Explain the characteristic of the roots for which Newton–Raphson does not exhibit quadratic convergence, justifying your explanation for this specific function.

---

## Exercise 2 — Modified root-finding methods (1 point)

Implement the following methods:

**(a) Modified Newton–Raphson method**, defined by

$$
x_{n+1}=x_n-\frac{1}{\dfrac{f'(x_n)}{f(x_n)}-\dfrac{1}{2}\dfrac{f''(x_n)}{f'(x_n)}}.
$$

**(b) Modified bisection method**, in which the root estimate at each step is not the midpoint of the search interval, but rather the point **one-third of the way along the interval**, closer to the endpoint whose function value is closer to zero.

**(c) Modified secant method**, which requires three initial points $x_n$, $x_{n+1}$, and $x_{n+2}$, and computes the next root estimate as

$$
x_{n+3}=x_{n+2}-\frac{r(r-q)(x_{n+2}-x_{n+1})+(1-r)s(x_{n+2}-x_n)}{(q-1)(r-1)(s-1)},
$$

where

$$
q=\frac{f(x_n)}{f(x_{n+1})},\qquad
r=\frac{f(x_{n+2})}{f(x_{n+1})},\qquad
s=\frac{f(x_{n+2})}{f(x_n)}.
$$

The new point $x_{n+3}$ replaces the oldest of the previous three points, $x_n$, and the algorithm repeats until the desired accuracy is achieved. In practice, the method fits a parabola through three points and then finds its intersection with the $x$-axis.

### Tasks

1. Find **all roots** of

   $$
   f(x)=54x^6+45x^5-102x^4-69x^3+35x^2+16x-4
   $$

   on $[-2,2]$, **to seven decimal places**, using the modified methods above and appropriate initializations.
2. Run algorithm **(b)** 20 times and determine whether it always converges in the same number of iterations.
3. Experimentally compare the convergence speeds of the modified methods against the classical methods over **100 runs**.

---

## Exercise 3 — Solving linear systems (1 point)

Consider the linear system

$$Ax=b.$$

1. In a programming language of your choice, implement a function that takes matrix $A$ as input and returns the matrices $P$, $L$, and $U$ from the factorization **$PA=LU$**. Then implement a second function that uses these matrices and vector $b$ to return the solution vector $x$.
2. Implement a function that takes a **symmetric positive-definite** matrix $A$ and returns a lower triangular matrix $L$ representing its **Cholesky decomposition** (e.g., `[L] = cholesky(A)`).
3. Implement the **Gauss–Seidel method** and use it to solve, to **five decimal places** (in terms of the infinity norm of the solution error), the sparse $n\times n$ system $Ax=b$ for **$n=10$ and $n=5000$**, with

   $$
   A_{i,i}=5,\qquad A_{i+1,i}=A_{i,i+1}=-2,
   $$

   and

   $$
   b=[3,1,1,\ldots,1,1,3]^T.
   $$

   In other words, the system has the tridiagonal form

   $$
   \begin{bmatrix}
   5&-2& & & \\
   -2&5&-2& & \\
   &\ddots&\ddots&\ddots& \\
   & &-2&5&-2\\
   & & &-2&5
   \end{bmatrix}
   \begin{bmatrix}x_1\\x_2\\\vdots\\x_{n-1}\\x_n\end{bmatrix}
   =
   \begin{bmatrix}3\\1\\\vdots\\1\\3\end{bmatrix}.
   $$

**Note:** The use of built-in functions/operators such as `chol()`, `lu()`, or the left-division operator is **not allowed**.

---

## Exercise 4 — PageRank and the power method (3 points)

Search engines such as [Google](http://www.google.com/) are known for the high-quality results they return in response to queries. This exercise gives an approximate explanation of how such results are ranked by using information about hyperlinks between pages on the World Wide Web.

Google assigns a positive real number, called the **PageRank**, to each page it returns. The PageRank is computed using the **power method** in a large-scale eigenvector computation.

In Figure 1, each node $n$ represents a webpage, and an edge from node $i$ to node $j$ represents a hyperlink from webpage $i$ to webpage $j$.

![Figure 1 — Directed graph of 15 webpages](assets/page_rank_graph.png)

*Figure 1. The graph of 15 webpages from the original assignment.*

Let $A\in\mathbb{R}^{n\times n}$, with $n=15$, denote the adjacency matrix of this graph:

$$
A=\begin{bmatrix}
0&1&0&0&0&0&0&0&1&0&0&0&0&0&0\\
0&0&1&0&1&0&1&0&0&0&0&0&0&0&0\\
0&1&0&0&0&1&0&1&0&0&0&0&0&0&0\\
0&0&1&0&0&0&0&0&0&0&0&1&0&0&0\\
1&0&0&0&0&0&0&0&0&1&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0&1&1&0&0&0&0\\
0&0&0&0&0&0&0&0&0&1&1&0&0&0&0\\
0&0&0&1&0&0&0&0&0&0&1&0&0&0&0\\
0&0&0&0&1&1&0&0&0&1&0&0&0&0&0\\
0&0&0&0&0&0&0&0&0&0&0&0&1&0&0\\
0&0&0&0&0&0&0&0&0&0&0&0&0&0&1\\
0&0&0&0&0&0&1&1&0&0&1&0&0&0&0\\
0&0&0&0&0&0&0&0&1&0&0&0&0&1&0\\
0&0&0&0&0&0&0&0&0&1&1&0&1&0&1\\
0&0&0&0&0&0&0&0&0&0&0&1&0&1&0
\end{bmatrix}.
$$

Here, $A_{i,j}=1$ when there is a link from node $i$ to node $j$, and $A_{i,j}=0$ otherwise.

Imagine a user browsing this network who is on page $i$ with probability $p_i$. The user either jumps to a random page with a specified probability $q$ (usually $q=0.15$), or, with probability $1-q$, randomly chooses one of the hyperlinks on page $i$.

The probability of moving from page $i$ to page $j$ is

$$
p_{i\to j}=\frac{q}{n}+(1-q)\frac{A_{i,j}}{n_i},
$$

where $n_i$ is the sum of the entries in the $i$-th row of $A$, i.e., the number of outgoing links from page $i$.

The probability of being on page $j$ at any given time is obtained by summing the contributions from all pages $i$:

$$
p_j=\sum_{i=1}^{n}\left(\frac{q p_i}{n}+(1-q)A_{i,j}\frac{p_i}{n_i}\right). \tag{1}
$$

Equation (1) can be written in matrix form as

$$p=Gp, \tag{2}$$

where $p$ is the vector of probabilities of the user being on the $n$ webpages, and $G$ is the **Google matrix**, whose entries are

$$
G_{i,j}=\frac{q}{n}+(1-q)\frac{A_{j,i}}{n_j}.
$$

Every column of $G$ sums to $1$, so $G$ is a **stochastic matrix**, and its largest eigenvalue is $1$. The eigenvector corresponding to eigenvalue $1$ gives the stationary probabilities, i.e., the PageRanks.

For the example above, with $q=0.15$, the PageRanks are given as

$$
\begin{aligned}
p=[&0.0268238,\ 0.0298611,\ 0.0298612,\ 0.0268241,\\
   &0.0395877,\ 0.0395878,\ 0.039588,\ 0.0395881,\\
   &0.074565,\ 0.106319,\ 0.10632,\ 0.0745657,\\
   &0.125089,\ 0.11633,\ 0.12509]^T.
\end{aligned}
$$

This eigenvector has been normalized so that its entries sum to $1$, as required for probabilities.

Pages **13 and 15** have the highest PageRanks, followed by pages **14, 10, and 11**. PageRank depends on more than just the **in-degree** of a page (the number of incoming links). Although nodes 10 and 11 have the highest in-degrees, their links to nodes 13 and 15 transfer importance to those nodes. This is the basic idea behind **Google bombing**: increasing a page's apparent importance by persuading other heavily visited pages to link to it.

Notice the connection between PageRank and the idea of importance. The assignment describes PageRank as a way to represent a page's importance, while noting that "importance" is itself difficult to define and that better models may be developed.

### Tasks

1. **Prove analytically** that matrix $G$ is stochastic.
2. **Construct** $G$ for the given example and verify, **using the power method**, that the eigenvector corresponding to the largest eigenvalue matches the one given above.
3. **Add four links** of your choice and **remove one existing link** from the graph. Construct the new matrix $G$ so as to increase the importance (PageRank) of a page of your choice.
4. Change the jump probability $q$ in your modified graph to **(a) $q=0.02$** and **(b) $q=0.6$**. Describe how the PageRanks change. What is the purpose of the jump probability?
5. In the original graph in Figure 1, suppose webpage **11** wants to improve its ranking relative to competitor webpage **10** by persuading pages **8 and 12** to link more strongly to page 11. Model this by replacing **$A_{8,11}$ and $A_{12,11}$ with $3$** in the adjacency matrix. Does this strategy work?
6. Study the effect of **removing page 10** from the graph. Which PageRanks increase and which decrease?

---<img width="966" height="912" alt="page_rank_graph" src="https://github.com/user-attachments/assets/028025a9-72d2-43be-bb77-38b99273d441" />


*Translated from the Greek assignment statement for the Numerical Analysis course. Mathematical content, requirements, and original problem data have been retained.*
