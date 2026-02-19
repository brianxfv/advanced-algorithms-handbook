"""
Master Theorem Examples & Growth Comparison
Author: Brian Gimenez

This script demonstrates the three main cases of the Master Theorem 
by simulating the number of operations in different recursive patterns.

The Master Theorem: T(n) = aT(n/b) + f(n)
"""

import math
import matplotlib.pyplot as plt

def simulate_work(n, a, b, k):
    """
    Simulates the total operations for a recurrence T(n) = aT(n/b) + n^k
    """
    if n <= 1:
        return 1
    # a * T(n/b) + n^k
    return a * simulate_work(n // b, a, b, k) + (n ** k)

def compare_cases():
    sizes = [2**i for i in range(1, 11)]  # n = 2, 4, 8, ..., 1024
    
    # Case 1: T(n) = 8T(n/2) + O(n) -> Work is dominated by subproblems (n^3)
    case1 = [simulate_work(n, 8, 2, 1) for n in sizes]
    
    # Case 2: T(n) = 2T(n/2) + O(n) -> Work is balanced (Merge Sort: n log n)
    case2 = [simulate_work(n, 2, 2, 1) for n in sizes]
    
    # Case 3: T(n) = T(n/2) + O(n) -> Work is dominated by the root (O(n))
    case3 = [simulate_work(n, 1, 2, 1) for n in sizes]

    plt.figure(figsize=(12, 6))
    plt.plot(sizes, case1, label="Case 1: T(n)=8T(n/2)+n -> O(n³)", marker='o')
    plt.plot(sizes, case2, label="Case 2: T(n)=2T(n/2)+n -> O(n log n)", marker='s')
    plt.plot(sizes, case3, label="Case 3: T(n)=T(n/2)+n -> O(n)", marker='^')

    plt.yscale('log') # Log scale to see all curves clearly
    plt.title("Master Theorem: Growth Comparison of the 3 Cases")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Total Operations (Log Scale)")
    plt.legend()
    plt.grid(True, which="both", ls="-")
    
    print("Generating Master Theorem growth visualization...")
    plt.show()

if __name__ == "__main__":
    compare_cases()
