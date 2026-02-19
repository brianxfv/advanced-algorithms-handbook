# 📈 Complexity Analysis: The Language of Performance

Understanding complexity is the difference between a solution that works on your machine and a solution that scales to millions of users. This section covers the formal mathematical tools used to quantify algorithmic efficiency.

---

## 🔬 Asymptotic Notations

To compare algorithms independently of hardware, we use asymptotic bounds:

* **Big O ($O$ - Upper Bound)**: Defines the worst-case scenario. It guarantees that an algorithm will never perform slower than a specific rate.
* **Big Omega ($\Omega$ - Lower Bound)**: Defines the best-case scenario. It represents the minimum work required.
* **Big Theta ($\Theta$ - Tight Bound)**: Defines the exact asymptotic behavior. An algorithm is $\Theta(g(n))$ if it is both $O(g(n))$ and $\Omega(g(n))$.



---

## 🏛️ The Master Theorem

For divide and conquer algorithms, we use the Master Theorem to solve recurrences of the form:

$$T(n) = aT\left(\frac{n}{b}\right) + f(n)$$

Where:
- $a \ge 1$: Number of subproblems.
- $b > 1$: Factor by which the subproblem size is reduced.
- $f(n)$: Cost of the work done outside the recursive calls (e.g., merging).

### The Three Cases:
1. If $f(n) = O(n^{\log_b a - \epsilon})$, then $T(n) = \Theta(n^{\log_b a})$.
2. If $f(n) = \Theta(n^{\log_b a})$, then $T(n) = \Theta(n^{\log_b a} \log n)$.
3. If $f(n) = \Omega(n^{\log_b a + \epsilon})$, then $T(n) = \Theta(f(n))$.

---

## 🔋 Amortized Analysis

Not all operations take the same amount of time every time they are called. Amortized analysis provides a "long-term average" cost per operation.

**Classic Example: Dynamic Array (e.g., `std::vector` or Python `list`)**
- Most `push_back` operations are $O(1)$.
- When the capacity is full, a "resize" occurs ($O(n)$).
- **Amortized Cost**: Even with the occasional $O(n)$ cost, the average cost over $N$ operations is still **$O(1)$**.

> **Pro-Tip**: Use the **Potential Method** or the **Accounting Method** to formally prove amortized bounds in engineering interviews or academic papers.

---

## 🚀 Common Complexities Cheat Sheet

| Notation | Name | Example Algorithm |
| :--- | :--- | :--- |
| $O(1)$ | Constant | Accessing an array index |
| $O(\log n)$ | Logarithmic | Binary Search |
| $O(n)$ | Linear | Linear Search |
| $O(n \log n)$ | Linearithmic | Merge Sort, Quick Sort (average) |
| $O(n^2)$ | Quadratic | Bubble Sort, Insertion Sort |
| $O(2^n)$ | Exponential | Recursive Fibonacci |
| $O(n!)$ | Factorial | Traveling Salesperson (Brute Force) |

---

## 🎓 Professor's Note: Space vs. Time
A common mistake is focusing only on **Time Complexity**. In modern engineering (especially in cloud and embedded systems), **Space Complexity** (RAM usage) is just as critical. Always analyze the stack depth in recursive calls!

---
**Author:** Brian Gimenez
