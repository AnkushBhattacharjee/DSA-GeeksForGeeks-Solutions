"""
Problem: Check if Array is Sorted
Platform: GeeksForGeeks
Difficulty: Easy

Problem Statement:
Given an array/list, determine whether it is sorted in non-decreasing order.
Return True if sorted, otherwise False.

Example:
Input:  [1, 2, 3, 4, 5]
Output: True

Input:  [3, 1, 4, 2]
Output: False

Approach 1 (Using sorted()):
- Create a copy of the input array to avoid modifying the original
- Use Python's built-in sorted() function to get a sorted version of the array
- Compare the original copy with the sorted copy; if equal, it is sorted
- Time Complexity: O(n log n)
- Space Complexity: O(n)

Approach 2 (Iterative check):
- Loop through the array and check if every element is <= its next element
- If any element is greater than its next, return False
- Time Complexity: O(n)
- Space Complexity: O(1)
- More optimal for interviews

Author: AnkushTheBeast
Date: August 2025
"""

class Solution:
    def isSorted_using_sorted(self, arr) -> bool:
        """Approach 1: Using sorted()"""
        arr_copy = list(arr)
        return arr_copy == sorted(arr_copy)

    def isSorted_iterative(self, arr) -> bool:
        """Approach 2: Iterative comparison"""
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test1 = [1, 2, 3, 4, 5]
    test2 = [3, 1, 4, 2]
    
    print("Approach 1: Using sorted()")
    print(f"Input: {test1} → Output: {solution.isSorted_using_sorted(test1)}")  # True
    print(f"Input: {test2} → Output: {solution.isSorted_using_sorted(test2)}")  # False
    
    print("\nApproach 2: Iterative check")
    print(f"Input: {test1} → Output: {solution.isSorted_iterative(test1)}")  # True
    print(f"Input: {test2} → Output: {solution.isSorted_iterative(test2)}")  # False
