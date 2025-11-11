def solve(s: str) -> int:
    """
    Find the length of the longest substring that is not a palindrome.
    
    Args:
        s: A string containing lowercase English letters
        
    Returns:
        The length of the longest non-palindrome substring, or 0 if all substrings are palindromes
    """
    def is_palindrome(text):
        """Check if a string is a palindrome."""
        return text == text[::-1]
    
    n = len(s)
    
    # Start from the longest possible length and work downwards
    # Single characters are always palindromes, so start from n
    for length in range(n, 1, -1):
        # Check all substrings of this length
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if not is_palindrome(substring):
                # Found a non-palindrome of this length
                # Since we iterate lengths in descending order,
                # this is the maximum length
                return length
    
    # All substrings are palindromes
    return 0