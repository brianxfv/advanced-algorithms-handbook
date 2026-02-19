```markdown
# ⚡ Module 02: Bit Manipulation

Bit manipulation is the art of operating on data at its most granular level: the individual bit. For a computer engineer, mastering bitwise operations is essential for high-performance computing, memory-constrained environments, and competitive programming.

---

## 🛠️ The Bitwise Toolbox

These are the fundamental operators that every engineer must have in their muscle memory:

| Operator | Syntax | Description |
| :--- | :--- | :--- |
| **AND** | `a & b` | Returns 1 if both bits are 1. Used for **masking**. |
| **OR** | `a | b` | Returns 1 if at least one bit is 1. Used for **setting** bits. |
| **XOR** | `a ^ b` | Returns 1 if bits are different. Useful for **toggling** and unique elements. |
| **NOT** | `~a` | Inverts all bits (One's complement). |
| **L-Shift** | `a << b` | Shifts bits to the left. Equivalent to multiplying by $2^b$. |
| **R-Shift** | `a >> b` | Shifts bits to the right. Equivalent to integer division by $2^b$. |



---

## 🚀 Common "Bit Magic" Tricks

These operations run in **$O(1)$** and are significantly faster than their arithmetic counterparts:

### 1. Check if a number is Even or Odd
```cpp
if (n & 1) // Odd
else       // Even

```

### 2. Check if Power of 2

A power of two has only one bit set (e.g., , ).

```cpp
bool isPowerOfTwo = n && !(n & (n - 1));

```

### 3. Clear the Rightmost Set Bit

This trick is the core of **Brian Kernighan’s Algorithm** for counting set bits.

```cpp
n = n & (n - 1);

```

### 4. Get/Set/Toggle the -th Bit

* **Get**: `(n >> i) & 1`
* **Set**: `n | (1 << i)`
* **Clear**: `n & ~(1 << i)`
* **Toggle**: `n ^ (1 << i)`

---

## 🧠 Memory Engineering: The Bitset

In C++, `std::bitset<N>` allows you to handle a large number of bits efficiently. Instead of using a `bool` array (where each bool typically takes 8 bits of memory), a bitset uses exactly **1 bit per element**, reducing the memory footprint by **8x**.

---

## 🎓 Professor's Note: Two's Complement

Remember that most modern systems use **Two's Complement** to represent signed integers.

* To get `-n`, the CPU performs `~n + 1`.
* This is why the range of a signed 8-bit integer is  to .
* Understanding this is crucial for preventing overflow bugs in low-level systems.

---

**Author:** Brian Gimenez

```

```
