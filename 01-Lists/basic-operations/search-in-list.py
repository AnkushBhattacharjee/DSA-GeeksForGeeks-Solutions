"""
Problem: Search in a List
Platform: GeeksForGeeks
Difficulty: Easy

Problem Statement:
Given an array/list and a target element x, find the index of x in the array.
If x is not found, return -1.

Approach:
- Create a copy of the input array
- Use enumerate() to get both index and value while iterating
- Compare each element with target x
- Return the index when match is found
- This is a linear search implementation

Author: AnkushTheBeast
Date: August 2025
"""

class Solution:
    def search(self, arr, x):
        # Create a copy to avoid modifying original array
        arr1 = list(arr)
        
        # Linear search using enumerate for index tracking
        for index, val in enumerate(arr1, start=0):
            if val == x:
                return index
        
        # Return -1 if element not found (good practice)
        return -1

# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_arr1 = [1, 2, 3, 4, 5]
    target1 = 3
    print(f"Array: {test_arr1}, Target: {target1}")
    print(f"Index found: {solution.search(test_arr1, target1)}")  # Output: 2
    
    test_arr2 = [10, 20, 30, 40]
    target2 = 25
    print(f"Array: {test_arr2}, Target: {target2}")
    print(f"Index found: {solution.search(test_arr2, target2)}")  # Output: -1
    
    test_arr3 = [5, 8, 3, 1, 9]
    target3 = 1
    print(f"Array: {test_arr3}, Target: {target3}")
    print(f"Index found: {solution.search(test_arr3, target3)}")  # Output: 3
