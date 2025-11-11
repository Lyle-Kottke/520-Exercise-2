def solve(s: str) -> int:
    """
    Finds the maximum length of a substring of s that is not a palindrome.

    If all substrings are palindromes, returns 0.

    Args:
        s: The input string (non-empty, length at most 50, lowercase English letters).

    Returns:
        The maximum length of a non-palindrome substring, or 0.
    
    Examples:
        >>> get_max_non_palindrome_substring_length("mew")
        3
        >>> get_max_non_palindrome_substring_length("wuffuw")
        5
        >>> get_max_non_palindrome_substring_length("qqqqqqqq")
        0
        >>> get_max_non_palindrome_substring_length("aabbaa")
        5
    """
    n = len(s)

    # Helper to check if a string is a palindrome
    def is_palindrome(sub: str) -> bool:
        return sub == sub[::-1]

    # Case 1: All characters in s are the same (e.g., "aaaaa", "qq").
    # If all characters are the same, every substring is a palindrome.
    # The set of unique characters will have size 1.
    if len(set(s)) == 1:
        return 0

    # Case 2: The entire string s is not a palindrome (e.g., "mew", "abb").
    # The longest possible substring is s itself, and since it's not a palindrome,
    # its length n is the answer.
    if not is_palindrome(s):
        return n
    
    # Case 3: The string s is a palindrome, but not all characters are the same
    # (e.g., "wuffuw", "abacaba").
    # The longest non-palindrome substring must have a length less than n.
    # The next longest possible length is n - 1.
    # Since s is a palindrome but has different characters, at least one of its
    # substrings of length n-1 (s[1:] or s[:-1]) must be a non-palindrome.
    # (Proof is in the plan).
    return n - 1