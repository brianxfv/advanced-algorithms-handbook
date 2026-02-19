import time
import matplotlib.pyplot as plt

class AmortizedArray:
    """
    A simulation of a dynamic array (like Python's list or C++'s std::vector).
    It demonstrates how doubling the capacity leads to O(1) amortized time.
    """
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.history = []  # Stores time taken for each insertion

    def append(self, value):
        start_time = time.perf_counter()
        
        # Simulate a resize (the expensive O(n) operation)
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        
        self.size += 1
        
        end_time = time.perf_counter()
        # Record the time for this specific insertion
        self.history.append(end_time - start_time)

    def _resize(self, new_capacity):
        # In a real scenario, this involves copying elements to a new memory block
        # We simulate the O(n) work by iterating
        temp = [None] * new_capacity
        for i in range(self.size):
            pass # Simulating copy work
        self.capacity = new_capacity

def visualize_amortization(n_elements=1000):
    arr = AmortizedArray()
    for i in range(n_elements):
        arr.append(i)

    # Plotting the results
    plt.figure(figsize=(10, 5))
    plt.plot(range(n_elements), arr.history, label='Cost per Insertion')
    plt.axhline(y=sum(arr.history)/n_elements, color='r', linestyle='--', label='Amortized Mean')
    
    plt.title("Amortized Analysis of a Dynamic Array")
    plt.xlabel("Number of Insertions (n)")
    plt.ylabel("Time Taken (seconds)")
    plt.legend()
    plt.grid(True)
    print(f"Simulation finished for {n_elements} elements.")
    plt.show()

if __name__ == "__main__":
    print("--- Amortized Analysis Simulation ---")
    visualize_amortization(2000)
