"""
Problem: Reverse an Array
Platform: GeeksForGeeks
Difficulty: Easy

Problem Statement:
Given an array/list, reverse its elements so that the last element becomes the first and the first becomes the last.

Example:
Input:  [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Approach:
- Create a copy of the input array to avoid modifying the original
- Use Python slicing with step = -1 to reverse the array
- arr[::-1] means start from the last index and move backwards

Author: AnkushTheBeast
Date: August 2025
"""

class Solution:
    def reverseArray(self, arr):
        # Create a copy to avoid modifying original array
        arr_copy = list(arr)
        # Return reversed array
        return arr_copy[::-1]

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test1 = [1, 2, 3, 4, 5]
    print(f"Input: {test1}")
    print(f"Output: {solution.reverseArray(test1)}")  # [5, 4, 3, 2, 1]
    
    test2 = [10, 20, 30, 40]
    print(f"Input: {test2}")
    print(f"Output: {solution.reverseArray(test2)}")  # [40, 30, 20, 10]
