# 🏗️ Module 00: Fundamentals

The foundation of advanced algorithms is not just writing code, but understanding the underlying constraints of hardware, memory, and mathematical limits. This module covers the essential toolkit every engineer must master before approaching complex data structures.

---

## 📑 Table of Contents

1.  **[Complexity Analysis](./01_Complexity_Analysis)**: Beyond $O(n)$ — Master the Master Theorem and Amortized Analysis.
2.  **[Bit Manipulation](./02_Bit_Manipulation)**: High-performance computing using binary logic and masks.
3.  **[Recursion & Backtracking](./03_Recursion_Backtracking)**: Optimizing state-space search and understanding the Stack.
4.  **[Memory Management](./04_Memory_Management)**: Cache locality, Pointers, and the Stack vs. Heap dichotomy.

---

## 🎯 Core Learning Objectives

### 1. Asymptotic Rigor
Understanding that $O(n \log n)$ is a category, but constant factors and memory access patterns (cache misses) define real-world performance.
> **Key Concept**: The Master Theorem for divide and conquer recurrences:
> $$T(n) = aT\left(\frac{n}{b}\right) + f(n)$$

### 2. Binary Proficiency
Algorithms at the bit level are the fastest possible operations on modern CPUs. We cover:
* Masking and Bitwise logic (`AND`, `OR`, `XOR`, `NOT`).
* Clearing/Setting bits in $O(1)$.
* Using Bitsets to reduce space complexity by a factor of 32 or 64.

### 3. Memory & Locality
A professional engineer knows that a `std::vector` (C++) or `list` (Python) is more than just a collection; it is a contiguous block of memory. 
* **Spatial Locality**: Why arrays outperform linked lists in modern CPUs.
* **Temporal Locality**: Reusing data while it's still in the L1/L2 cache.

---

## 🛠️ Implementation Standards

Each sub-module includes:
* **`Theory.md`**: The mathematical or architectural "why".
* **`src/`**: Clean, production-ready code in C++ or Python.
* **`benchmarks/`**: Real-world timing to prove theoretical complexities.

---

## 🎓 Professor's Note: Common Pitfalls
* **The "Recursion Limit"**: Forgetting that deep recursion leads to `StackOverflowError` if Tail Call Optimization (TCO) is not present.
* **Integer Overflow**: Using `int` instead of `long long` or `uint64_t` in competitive programming and large-scale systems.
* **Big O vs. Reality**: Assuming $O(N^2)$ is always slower than $O(N \log N)$ for very small values of $N$.

---
**Author:** Brian Gimenez
