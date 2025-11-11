import math

def is_palindrome(s):
    """
    Checks if a string s is a palindrome.
    """
    return s == s[::-1]

def solve(s: str) -> int:
    """
    Finds the maximum length of a substring of s that is not a palindrome.
    
    Args:
        s: The input string.
        
    Returns:
        The maximum length of a non-palindrome substring, or 0 if all 
        substrings are palindromes.
    """
    
    n = len(s)
    
    # 1. Check the entire string (length n).
    # If the whole string is not a palindrome, it's the longest possible 
    # non-palindrome substring.
    if not is_palindrome(s):
        return n
    
    # At this point, s is a palindrome (e.g., "wuffuw", "qqqqqqqq").
    
    # 2. Check for substrings of length n - 1.
    # The two possible substrings of length n-1 are the prefix and the suffix.
    prefix_n_minus_1 = s[:-1] # s[0...n-2]
    suffix_n_minus_1 = s[1:]   # s[1...n-1]
    
    # If either the prefix or the suffix is NOT a palindrome, 
    # then n-1 is the longest possible length.
    if not is_palindrome(prefix_n_minus_1) or not is_palindrome(suffix_n_minus_1):
        return n - 1
        
    # 3. Base Case: All characters are the same.
    # If s is a palindrome AND both the prefix and suffix of length n-1 
    # are palindromes, then all characters in s must be the same (e.g., "qqqq").
    # In this case, every substring is a palindrome.
    return 0
