# Dynamic Programming

### Introduction

Dynamic programming is an approach/technique used to solve the complex problem by **breaking down** the problem into **sub-problems** and **storing** the results of the **sub-problem** to avoid the re-computation of the same sub-problem again and again.

### Properties

* Overlapping Subproblem
* Optimal Substructure

### Overlapping Subproblems:

After breaking down the main problem into **sub-problems** if some of those **sub-problem** **results** are **needed or re-calculated** again and again to calculate another **sub-problem result** then those sub-problems are called **overlapping subproblems** as they are overlapped.

Let's consider about the fibonaccai number calculation:

**Fibonacci sequence:** 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ... ...\
Here we can see that&#x20;

* 1st fib is 0
* 2nd fib is 1
* 3rd fib is 1 which is equal of (1st fib + 2nd fib) = (0+1)
* 4th fib is 2 which is equal of (1 + 1) = (2nd fib + 3rd fib)
* 5th fib is 3 is equal of (2 + 1) = (4th fib + 3rd fib)

We can say that $$fib(n) = fib(n-1) + fib(n+2)$$

If we draw a tree for $$fib(7)$$

<img src="../.gitbook/assets/file.drawing (1).svg" alt="​" class="gitbook-drawing">

Here we can see we need to re-calculate the value $$fib(2), fib(3), fib(4), fib(5)$$​. Also, each of them is a subproblem. As these subproblem results are needed again and again to calculate other subproblems, these subproblems are called overlapping subproblems.

### Optimal Substructure

&#x20;**** A given problem has Optimal Substructure Property if the optimal solution of the given problem can be obtained by using optimal solutions of its subproblems.&#x20;

In another word, the Optimal substructure is just an equation that relates the solution of a larger problem to the solution of a smaller subproblem.\
That means, If the solution of a larger problem can be found by combining the solutions of the smaller subproblem then the problem has the **optimal substructure property**.

In another word, If the optimal solution to a problem, **S**, of **size** **n** can be calculated by **JUST** looking at the optimal solution of a subproblem, **s**, with **size < n** and **NOT ALL** solutions to the subproblem, **AND** it will also result in an optimal solution for problem **S**, then this problem **S** is considered to have **optimal substructure.**

In the above example, the $$fib(n)$$​can be found by the summation of the solutions of subproblems to $$fib(n-1) and fib(n-2)$$​. So **Fibonacci** has the optimal substructure property.

Another example could be the shortest path algorithm.\
**(Shortest Path Problem)**: consider a **undirected** graph with **vertices a,b,c,d,e** and **edges (a,b), (a,e), (b,c), (c,d), (d,a) & (e,b)** then shortest path between **a & c** is **a -- b -- c** and this problem can be broken down into finding shortest path between **a & b** and then shortest path between **b & c** and **this will give us a valid solution**. Note that we have **two** ways of **reaching b from a:**

* **a -- b (Shortest path)**
* **a -- e -- b**

![](../.gitbook/assets/file.drawing.svg)

But the **Longest Path Problem** does not have the **optimal substructure property**. **Longest** path between **a & d** is **a -- e -- b -- c -- d**, but **sum** of longest paths between **a & c** **(a -- e -- b -- c)** and **c & d** **(c -- b -- e -- a -- d)** won't give us a valid (non-repeating vertices) l**ongest path between a & d.**
