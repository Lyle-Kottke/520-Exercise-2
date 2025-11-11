def solve(a, b, c):
    """
    Determine if Dante can deal exactly c damage using two guns.
    
    Args:
        a: Damage per shot from Ebony gun
        b: Damage per shot from Ivory gun
        c: Total damage required
    
    Returns:
        "Yes" if exact damage is possible, "No" otherwise
    """
    # Try all possible numbers of shots from Ebony gun
    for x in range(c // a + 1):
        remaining = c - a * x
        
        # Check if remaining damage can be dealt by Ivory gun
        if remaining % b == 0:
            return "Yes"
    
    return "No"