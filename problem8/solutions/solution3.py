import math

def solve(a: int, b: int, c: int) -> str:
    """
    Determines if it's possible to achieve exactly 'c' units of damage using
    non-negative integer shots from Ebony (a damage per shot) and Ivory (b damage per shot).
    
    The problem is to find non-negative integers x and y such that ax + by = c.

    Args:
        a: Damage dealt by one Ebony shot (1 <= a <= 100).
        b: Damage dealt by one Ivory shot (1 <= b <= 100).
        c: Total damage required (1 <= c <= 10000).

    Returns:
        "Yes" if the damage is possible, "No" otherwise.
    """
    
    # Iterate through all possible non-negative integer shots for the Ebony gun (x).
    # Since 'by' must be non-negative, the maximum possible damage from Ebony is 'c',
    # so the maximum number of shots 'x' is floor(c / a).
    
    max_x = c // a  # Integer division gives floor(c/a)

    for x in range(max_x + 1):
        # Calculate the damage dealt by Ebony: a * x
        ebony_damage = a * x
        
        # Calculate the remaining damage that must be dealt by Ivory.
        # This will be non-negative because we limited x by max_x.
        remaining_damage = c - ebony_damage
        
        # The remaining_damage must be a multiple of 'b' (Ivory's damage per shot)
        # for the number of Ivory shots (y) to be a non-negative integer.
        # This is checked using the modulo operator.
        if remaining_damage % b == 0:
            # A valid solution (x, y = remaining_damage / b) is found.
            return "Yes"
            
    # If the loop completes without finding a solution, it's impossible.
    return "No"