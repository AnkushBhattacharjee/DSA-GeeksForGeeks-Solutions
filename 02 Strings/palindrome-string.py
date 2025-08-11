# Palindrome String - Basic Solutions
# Author: Ankush Bhattacharjee
# Difficulty: Easy
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    """
    Basic solutions to check if a string is a palindrome.
    
    Three fundamental approaches:
    1. String slicing (most Pythonic)
    2. Manual iteration
    3. Recursive approach
    """
    
    def isPalindrome(self, s: str) -> bool:
        """
        Method 1: String slicing (Your original concept, simplified)
        Compare string with its reverse using slicing.
        
        Args:
            s (str): Input string to check
            
        Returns:
            bool: True if palindrome, False otherwise
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        return s == s[::-1]
    
    def isPalindromeManual(self, s: str) -> bool:
        """
        Method 2: Manual iteration approach
        Compare characters from start and end manually.
        
        Args:
            s (str): Input string to check
            
        Returns:
            bool: True if palindrome, False otherwise
            
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        n = len(s)
        
        # Compare each character with its mirror position
        for i in range(n):
            if s[i] != s[n - 1 - i]:
                return False
        
        return True
    
    def isPalindromeRecursive(self, s: str) -> bool:
        """
        Method 3: Recursive approach
        Recursively check first and last characters.
        
        Args:
            s (str): Input string to check
            
        Returns:
            bool: True if palindrome, False otherwise
            
        Time Complexity: O(n)
        Space Complexity: O(n) due to recursion stack
        """
        # Base cases
        if len(s) <= 1:
            return True
        
        # Check first and last characters
        if s[0] != s[-1]:
            return False
        
        # Recursively check the middle part
        return self.isPalindromeRecursive(s[1:-1])

# Test cases
def test_palindrome_string():
    """Test function with various test cases for all methods"""
    solution = Solution()
    
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("madam", True),
        ("python", False),
        ("a", True),
        ("", True),
        ("aa", True),
        ("ab", False),
        ("level", True),
        ("world", False)
    ]
    
    print("Testing Palindrome String Methods:")
    print("=" * 60)
    
    for i, (test_input, expected) in enumerate(test_cases, 1):
        print(f"Test {i}: Input = '{test_input}' | Expected = {expected}")
        
        # Test all methods
        methods = [
            ("Slicing", solution.isPalindrome),
            ("Manual", solution.isPalindromeManual),
            ("Recursive", solution.isPalindromeRecursive)
        ]
        
        for name, method in methods:
            result = method(test_input)
            status = "✓" if result == expected else "✗"
            print(f"  {name:12}: {result} {status}")
        print()

def demonstrate_your_original_code():
    """Demonstrate your original code and explain the fix"""
    print("Your Original Code Analysis:")
    print("=" * 50)
    
    # Your original approach (fixed)
    def your_original_fixed(s):
        s1 = list(s)
        # Fixed: Compare list with its reverse
        if s1 == s1[::-1]:  # Instead of s1[0::1] == s1[-1::-1]
            return True
        return False
    
    # Show the difference
    def your_original_concept(s):
        s1 = list(s)
        # Your original slicing (which actually worked correctly!)
        if s1[0::1] == s1[-1::-1]:
            return True
        return False
    
    test_cases = ["racecar", "hello", "madam"]
    
    for test in test_cases:
        original = your_original_concept(test)
        simplified = test == test[::-1]
        
        print(f"Input: '{test}'")
        print(f"  Your original: {original}")
        print(f"  Simplified:    {simplified}")
        print(f"  Explanation:")
        print(f"    s1[0::1] = {list(test)} (same as s1)")
        print(f"    s1[-1::-1] = {list(test)[::-1]} (reversed s1)")
        print(f"    Your logic was actually correct!")
        print()

if __name__ == "__main__":
    # Explain your original code
    demonstrate_your_original_code()
    
    # Run comprehensive tests
    test_palindrome_string()
    
    # Interactive examples
    print("Interactive Examples:")
    print("=" * 30)
    solution = Solution()
    
    examples = ["racecar", "hello", "level", "python"]
    for example in examples:
        result = solution.isPalindrome(example)
        print(f"isPalindrome('{example}') = {result}")
    
    print("\nNote: Your original code s1[0::1] == s1[-1::-1] actually worked!")
    print("It's just more complex than needed. s == s[::-1] is simpler.")
