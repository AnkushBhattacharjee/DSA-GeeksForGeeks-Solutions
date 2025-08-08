"""
Problem: Largest Element in Array
Platform: GeeksForGeeks
Difficulty: Easy

Problem Statement:
Given an array/list, find and return the largest element in the array.

Approach:
- Create a copy of the input array
- Sort the array in ascending order
- Return the last element (which will be the largest)

Alternative approaches:
- Using max() built-in function: max(arr)
- Manual iteration to find maximum

Author: AnkushTheBeast
Date: August 2025
"""

class Solution:
    def largest(self, arr):
        # Create a copy to avoid modifying original array
        arr1 = list(arr)
        
        # Sort the array (note: need parentheses to call the method)
        arr1.sort()
        
        # Return the last element (largest after sorting)
        res = arr1[-1]  # Fixed: should be arr1[-1], not arr[-1]
        return res

# Alternative solution using max() - more efficient
class AlternativeSolution:
    def largest(self, arr):
        # Direct approach using built-in max function
        return max(arr)

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    alt_solution = AlternativeSolution()
    
    # Test cases
    test1 = [1, 8, 7, 56, 90]
    print(f"Array: {test1}")
    print(f"Largest (sorting method): {solution.largest(test1)}")      # Output: 90
    print(f"Largest (max method): {alt_solution.largest(test1)}")      # Output: 90
    
    test2 = [5, 5, 5, 5]
    print(f"Array: {test2}")
    print(f"Largest: {solution.largest(test2)}")  # Output: 5
    
    test3 = [10]
    print(f"Array: {test3}")
    print(f"Largest: {solution.largest(test3)}")  # Output: 10
