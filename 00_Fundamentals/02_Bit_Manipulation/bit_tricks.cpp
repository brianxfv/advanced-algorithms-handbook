/**
 * @file bit_tricks.cpp
 * @author Brian Gimenez
 * @brief Implementation of high-performance bitwise operations and tricks.
 */

#include <iostream>
#include <bitset>
#include <string>

// 1. Kernighan's Algorithm: Counts set bits (1s) in O(set_bits)
int countSetBits(int n) {
    int count = 0;
    while (n > 0) {
        n &= (n - 1); // Clears the rightmost set bit
        count++;
    }
    return count;
}

// 2. Power of Two Check: O(1)
bool isPowerOfTwo(int n) {
    return n > 0 && !(n & (n - 1));
}

// 3. Bit Masking: Managing User Permissions
namespace Permissions {
    const int READ    = 1 << 0; // 0001 (1)
    const int WRITE   = 1 << 1; // 0010 (2)
    const int EXECUTE = 1 << 2; // 0100 (4)
    const int DELETE  = 1 << 3; // 1000 (8)
}

int main() {
    int number = 42; // Binary: 00101010
    
    std::cout << "--- Bit Manipulation Fundamentals ---" << std::endl;
    std::cout << "Number: " << number << " | Binary: " << std::bitset<8>(number) << std::endl;

    // Trick 1: Even or Odd
    std::cout << "Is Odd? " << ((number & 1) ? "Yes" : "No") << std::endl;

    // Trick 2: Counting Bits
    std::cout << "Set Bits in 42: " << countSetBits(number) << std::endl;

    // Trick 3: Power of Two
    int p = 16;
    std::cout << "Is " << p << " power of 2? " << (isPowerOfTwo(p) ? "Yes" : "No") << std::endl;

    // Trick 4: Permission System Simulation
    int userPerms = Permissions::READ | Permissions::WRITE; // 0011
    std::cout << "\n--- Permission System (Masking) ---" << std::endl;
    std::cout << "User Perms: " << std::bitset<4>(userPerms) << std::endl;
    
    bool canWrite = userPerms & Permissions::WRITE;
    bool canDelete = userPerms & Permissions::DELETE;
    
    std::cout << "Can Write? " << (canWrite ? "YES" : "NO") << std::endl;
    std::cout << "Can Delete? " << (canDelete ? "YES" : "NO") << std::endl;

    return 0;
}
