"""
Problem: Print Alternates in List
Platform: GeeksForGeeks
Difficulty: Easy

Problem Statement:
Given a list/array, print all the alternate elements starting from the first element.
For example: [1, 2, 3, 4, 5] → [1, 3, 5]

Approach:
- Create a copy of the input array to avoid modifying original
- Use Python slicing with step=2 to get every alternate element
- arr[0::2] means start from index 0, go till end, with step size 2

Author: AnkushTheBeast
Date: August 2025
"""

class Solution:
    def getAlternates(self, arr):
        # Create a copy to avoid modifying original array
        arr1 = list(arr)
        # Return alternate elements starting from index 0
        return arr1[0::2]

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test1 = [1, 2, 3, 4, 5]
    print(f"Input: {test1}")
    print(f"Output: {solution.getAlternates(test1)}")  # [1, 3, 5]
    
    test2 = [10, 20, 30, 40]
    print(f"Input: {test2}")
    print(f"Output: {solution.getAlternates(test2)}")  # [10, 30]
