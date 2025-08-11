"""
Problem: Reverse Words in a String (dot separated)
Platform: GeeksForGeeks
Difficulty: Easy

Problem Statement:
Given a string containing words separated by dots ('.'), 
reverse the order of the words so that the last word becomes the first 
and the first becomes the last. Ignore any leading or trailing dots 
and avoid extra dots in the result.

Example:
Input:  "v.f.gfc"
Output: "gfc.f.v"

Input:  "..v.f.gfc."
Output: "gfc.f.v"

Approach:
- Remove leading and trailing dots using strip(".")
- Split the string into parts using split(".")
- Filter out any empty strings caused by consecutive dots
- Reverse the list of words
- Join them back with '.' as the separator

Author: AnkushTheBeast
Date: August 2025
"""

class Solution:
    def reverseWords(self, s):
        s = s.strip(".")
        s1 = []
        for part in s.split("."):
            if part != "":
                s1.append(part)
        s2 = s1[::-1]
        s3 = '.'.join(s2)
        return s3


# Test the solution
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test1 = "v.f.gfc"
    print(f"Input: {test1}")
    print(f"Output: {solution.reverseWords(test1)}")  # gfc.f.v
    
    test2 = "..v.f.gfc."
    print(f"Input: {test2}")
    print(f"Output: {solution.reverseWords(test2)}")  # gfc.f.v
