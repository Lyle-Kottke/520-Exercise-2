def solve(a: int, b: int, c: int) -> str:
    """
    Checks if exactly 'c' units of damage can be dealt using two guns:
    Ebony (a damage per shot) and Ivory (b damage per shot),
    with a non-negative number of shots for each.

    The problem is to find if there exist non-negative integers x and y such that:
    a*x + b*y = c.

    Args:
        a: Damage dealt by Ebony per shot (1 <= a <= 100).
        b: Damage dealt by Ivory per shot (1 <= b <= 100).
        c: Total damage required (1 <= c <= 10000).

    Returns:
        "Yes" if possible, "No" otherwise.

    Examples:
        >>> check_damage_possible(4, 6, 15)
        'No'
        >>> check_damage_possible(3, 2, 7)
        'Yes'  # 1*3 + 2*2 = 7
        >>> check_damage_possible(6, 11, 6)
        'Yes'  # 1*6 + 0*11 = 6
        >>> check_damage_possible(10, 10, 5)
        'No'
        >>> check_damage_possible(5, 5, 20)
        'Yes' # 4*5 + 0*5 = 20 (or 2*5 + 2*5, etc.)
    """
    # Maximum number of Ebony shots possible before total damage exceeds c.
    # Since a >= 1, we don't have to worry about division by zero.
    max_x = c // a

    # Iterate through all possible non-negative shots from Ebony (x).
    for x in range(max_x + 1):
        # Calculate the damage dealt by Ebony
        ebony_damage = a * x
        
        # Calculate the remaining damage required from Ivory
        c_rem = c - ebony_damage
        
        # If the remaining damage is a non-negative multiple of b, 
        # then a non-negative integer number of Ivory shots (y) exists.
        # This is a solution (x, y) where x >= 0 and y >= 0.
        # Since x is in range(max_x + 1), ebony_damage <= c, so c_rem >= 0 is guaranteed.
        if c_rem % b == 0:
            return "Yes"

    # If the loop finishes without finding a valid combination
    return "No"