def solve(a, b, c):
    """
    Determine if Dante can deal exactly c damage using guns Ebony (a damage) and Ivory (b damage).
    
    Args:
        a: Damage per shot from Ebony gun
        b: Damage per shot from Ivory gun
        c: Total damage required
    
    Returns:
        "Yes" if exactly c damage is possible, "No" otherwise
    
    Examples:
        >>> can_break_shield(4, 6, 15)
        'No'
        >>> can_break_shield(3, 2, 7)
        'Yes'
        >>> can_break_shield(6, 11, 6)
        'Yes'
    """
    # Try all possible numbers of shots from Ebony gun
    for x in range(c // a + 1):
        remaining = c - a * x
        # Check if remaining damage can be dealt by Ivory gun
        if remaining % b == 0:
            return "Yes"
    
    return "No"