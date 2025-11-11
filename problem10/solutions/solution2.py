def solve(s: str) -> int:
    """
    Find the length of the longest substring that is not a palindrome.
    
    Args:
        s: A string of lowercase English letters
        
    Returns:
        The length of the longest non-palindrome substring, or 0 if all substrings are palindromes
        
    Examples:
        longest_non_palindrome_substring("mew") -> 3
        longest_non_palindrome_substring("wuffuw") -> 5
        longest_non_palindrome_substring("qqqqqqqq") -> 0
    """
    def is_palindrome(text):
        return text == text[::-1]
    
    # Check lengths from longest to shortest
    for length in range(len(s), 0, -1):
        # Check all substrings of this length
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if not is_palindrome(substring):
                return length
    
    return 0