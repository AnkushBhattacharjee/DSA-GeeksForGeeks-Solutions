# Reverse String - Multiple Solutions
# Author: Ankush Bhattacharjee
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(1) for in-place methods, O(n) for string methods

class Solution:
    """
    Multiple solutions to reverse a string.
    
    Different approaches demonstrate various Python string manipulation techniques:
    1. Slicing (most Pythonic)
    2. Built-in reversed() function
    3. Manual iteration
    4. Recursive approach
    5. Two-pointer in-place (for list of characters)
    """
    
    def reverseString(self, s: str) -> str:
        """
        Method 1: String slicing (Your original solution)
        Most concise and Pythonic approach.
        
        Args:
            s (str): Input string to reverse
            
        Returns:
            str: Reversed string
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return s[::-1]
    
    def reverseStringBuiltIn(self, s: str) -> str:
        """
        Method 2: Using built-in reversed() function
        Alternative using Python's reversed() function.
        
        Args:
            s (str): Input string to reverse
            
        Returns:
            str: Reversed string
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return ''.join(reversed(s))
    
    def reverseStringManual(self, s: str) -> str:
        """
        Method 3: Manual iteration approach
        Building reversed string character by character.
        
        Args:
            s (str): Input string to reverse
            
        Returns:
            str: Reversed string
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = ""
        for i in range(len(s) - 1, -1, -1):
            result += s[i]
        return result
    
    def reverseStringRecursive(self, s: str) -> str:
        """
        Method 4: Recursive approach
        Demonstrates recursion for string reversal.
        
        Args:
            s (str): Input string to reverse
            
        Returns:
            str: Reversed string
            
        Time Complexity: O(n)
        Space Complexity: O(n) due to recursion stack
        """
        # Base case
        if len(s) <= 1:
            return s
        
        # Recursive case: last char + reverse of remaining string
        return s[-1] + self.reverseStringRecursive(s[:-1])
    
    def reverseStringInPlace(self, s: list) -> None:
        """
        Method 5: In-place reversal using two pointers
        Modifies the input list directly (common in LeetCode problems).
        
        Args:
            s (list): List of characters to reverse in-place
            
        Returns:
            None: Modifies the input list directly
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap characters
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Test cases
def test_reverse_string():
    """Test function with various test cases for all methods"""
    solution = Solution()
    
    test_cases = [
        "hello",
        "world", 
        "Python",
        "a",
        "",
        "racecar",
        "12345"
    ]
    
    print("Testing String Reversal Methods:")
    print("=" * 60)
    
    for i, test_input in enumerate(test_cases, 1):
        print(f"Test {i}: Input = '{test_input}'")
        
        # Method 1: Slicing
        result1 = solution.reverseString(test_input)
        print(f"  Slicing:           '{result1}'")
        
        # Method 2: Built-in reversed()
        result2 = solution.reverseStringBuiltIn(test_input)
        print(f"  Built-in reversed: '{result2}'")
        
        # Method 3: Manual iteration
        result3 = solution.reverseStringManual(test_input)
        print(f"  Manual iteration:  '{result3}'")
        
        # Method 4: Recursive
        result4 = solution.reverseStringRecursive(test_input)
        print(f"  Recursive:         '{result4}'")
        
        # Method 5: In-place (using list)
        char_list = list(test_input)
        solution.reverseStringInPlace(char_list)
        result5 = ''.join(char_list)
        print(f"  In-place:          '{result5}'")
        
        # Verify all methods give same result
        all_same = result1 == result2 == result3 == result4 == result5
        status = "✓ All methods match" if all_same else "✗ Methods differ"
        print(f"  Status: {status}")
        print()

def benchmark_methods():
    """Simple performance comparison of different methods"""
    import time
    
    solution = Solution()
    test_string = "abcdefghijklmnopqrstuvwxyz" * 100  # Long string for testing
    
    methods = [
        ("Slicing", solution.reverseString),
        ("Built-in reversed", solution.reverseStringBuiltIn),
        ("Manual iteration", solution.reverseStringManual),
        ("Recursive", solution.reverseStringRecursive)
    ]
    
    print("Performance Benchmark (1000 iterations):")
    print("=" * 50)
    
    for name, method in methods:
        start_time = time.time()
        for _ in range(1000):
            method(test_string)
        end_time = time.time()
        
        print(f"{name:20}: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    # Run tests
    test_reverse_string()
    
    # Performance benchmark
    print("\n" + "=" * 60)
    benchmark_methods()
    
    # Interactive examples
    print("\n" + "=" * 60)
    print("Interactive Examples:")
    solution = Solution()
    
    examples = ["hello", "world", "Python"]
    for example in examples:
        result = solution.reverseString(example)
        print(f"reverseString('{example}') = '{result}'")
