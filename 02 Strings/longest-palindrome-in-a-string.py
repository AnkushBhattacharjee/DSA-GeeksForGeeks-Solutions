# Longest Palindromic Substring - Basic Solution
# Author: Ankush Bhattacharjee
# Difficulty: Medium
# Time Complexity: O(n³)
# Space Complexity: O(n²)

class Solution:
    """
    Solution to find the longest palindromic substring in a given string.
    
    Approach:
    1. Generate all possible substrings using nested loops
    2. Check if each substring is a palindrome by comparing with its reverse
    3. Store all palindromic substrings in a list
    4. Sort by length and return the longest one
    
    Note: This is a brute force approach with O(n³) time complexity.
    While not optimal for large inputs, it demonstrates the basic logic clearly.
    """
    
    def longestPalindrome(self, s):
        """
        Find the longest palindromic substring in the given string.
        
        Args:
            s (str): Input string
            
        Returns:
            str: Longest palindromic substring
            
        Examples:
            >>> solution = Solution()
            >>> solution.longestPalindrome("babad")
            'bab'  # or 'aba'
            >>> solution.longestPalindrome("cbbd")
            'bb'
        """
        n = len(s)
        
        # Handle edge cases
        if n == 0:
            return ""
        if n == 1:
            return s
            
        palindromes = []
        
        # Generate all possible substrings
        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                
                # Check if substring is a palindrome
                if substring == substring[::-1]:
                    palindromes.append(substring)
        
        # Sort palindromes by length and return the longest
        palindromes.sort(key=len)
        return palindromes[-1] if palindromes else ""

# Test cases
def test_longest_palindrome():
    """Test function with various test cases"""
    solution = Solution()
    
    test_cases = [
        ("babad", ["bab", "aba"]),  # Multiple valid answers
        ("cbbd", ["bb"]),
        ("racecar", ["racecar"]),
        ("abcdef", ["a", "b", "c", "d", "e", "f"]),  # Any single character
        ("aa", ["aa"]),
        ("", [""]),
        ("a", ["a"])
    ]
    
    print("Testing Longest Palindromic Substring:")
    print("=" * 50)
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = solution.longestPalindrome(input_str)
        is_valid = result in expected if expected != [""] else result == ""
        status = "✓ PASS" if is_valid else "✗ FAIL"
        
        print(f"Test {i}: {status}")
        print(f"  Input: '{input_str}'")
        print(f"  Output: '{result}'")
        print(f"  Expected: {expected}")
        print()

if __name__ == "__main__":
    # Run tests
    test_longest_palindrome()
    
    # Interactive example
    print("Interactive Example:")
    solution = Solution()
    
    example_inputs = ["babad", "cbbd", "racecar"]
    for example in example_inputs:
        result = solution.longestPalindrome(example)
        print(f"longestPalindrome('{example}') = '{result}'")
