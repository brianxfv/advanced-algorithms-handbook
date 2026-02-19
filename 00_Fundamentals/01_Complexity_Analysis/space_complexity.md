```markdown
# 🧠 Space Complexity Analysis

Space complexity quantifies the total amount of memory (RAM) an algorithm uses relative to the input size $n$. In high-performance engineering, optimizing space is often as critical as optimizing time, especially in embedded systems or cloud computing where memory usage translates directly to cost.

---

## ⚖️ Total Space vs. Auxiliary Space

It is vital to distinguish between these two concepts:

1.  **Total Space Complexity**: The sum of the space occupied by the input and the extra space used by the algorithm.
2.  **Auxiliary Space**: The extra or temporary space used by the algorithm logic (excluding the input). 
    * *In most technical contexts, when we say "Space Complexity", we are usually referring to **Auxiliary Space**.*

---

## 🔄 The Call Stack and Recursion

One of the most frequent errors in memory analysis is forgetting the **Call Stack**. Every time a function is called, a "Stack Frame" is created to store local variables, return addresses, and function parameters.

### Example: Linear Recursion
Even if a recursive function doesn't declare new arrays, its space complexity is proportional to the **depth of the recursion tree**.

```python
def factorial(n):
    if n <= 1: return 1
    return n * factorial(n - 1)

```

* **Time**: 
* **Space**:  (because  stack frames are active simultaneously).

---

## 🔋 Common Space Complexity Classes

| Complexity | Memory Growth | Typical Scenario |
| --- | --- | --- |
| **** | Constant | **In-place** algorithms (e.g., Bubble Sort, bit swapping). |
| **** | Logarithmic | Recursion depth of balanced trees or QuickSort. |
| **** | Linear | Storing a copy of the input, Adjacency Lists in graphs. |
| **** | Quadratic | 2D matrices, Adjacency Matrices for dense graphs. |

---

## 🚀 Optimization: Tail Call Optimization (TCO)

In languages like C++ (with `-O2` or `-O3` flags) or functional languages (Haskell, Scala), a "Tail Recursive" function can be optimized by the compiler to reuse the same stack frame. This reduces space complexity from  to .

> **Note for Pythonistas**: Python does **not** support TCO. Deep recursion in Python will always lead to a `RecursionError` if the limit is exceeded.

---

## 🎓 Professor's Note: The "In-place" Definition

An algorithm is considered **In-place** if its auxiliary space complexity is  (or  in some definitions that account for the stack). Always check if you can overwrite the input array instead of creating a new one to save memory!

---

**Author:** Brian Gimenez

```

```
