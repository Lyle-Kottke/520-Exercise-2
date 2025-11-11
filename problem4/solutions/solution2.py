def extended_gcd(a, b):
    """Extended Euclidean algorithm. Returns (gcd, x, y) where ax + by = gcd."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def solve(a1, b1, a2, b2, L, R):
    """
    Count integers x in [L, R] that belong to both arithmetic progressions.
    
    First progression: x = a1*k' + b1 for some k' >= 0
    Second progression: x = a2*l' + b2 for some l' >= 0
    
    Args:
        a1, b1, a2, b2: Parameters of the two progressions
        L, R: Range boundaries
    
    Returns:
        Number of integers in [L, R] belonging to both progressions
    """
    # Use extended GCD to find if solutions exist
    g, p, q = extended_gcd(a1, a2)
    
    diff = b2 - b1
    if diff % g != 0:
        return 0
    
    # Particular solution for a1*k - a2*l = diff
    mult = diff // g
    k0 = p * mult
    l0 = -q * mult
    
    # General solution parameters
    a2_g = a2 // g
    a1_g = a1 // g
    lcm = a1_g * a2
    
    # Value of x for t=0
    x0 = a1 * k0 + b1
    
    # Helper function for ceiling division
    def ceil_div(num, denom):
        if num >= 0:
            return (num + denom - 1) // denom
        return num // denom
    
    # Constraint 1: k' >= 0 means k0 + a2_g*t >= 0
    t_min_k = ceil_div(-k0, a2_g)
    
    # Constraint 2: l' >= 0 means l0 + a1_g*t >= 0
    t_min_l = ceil_div(-l0, a1_g)
    
    # Constraint 3: L <= x0 + lcm*t <= R
    t_min_range = ceil_div(L - x0, lcm)
    t_max_range = (R - x0) // lcm
    
    # Find the valid range for t
    t_min = max(t_min_k, t_min_l, t_min_range)
    t_max = t_max_range
    
    return max(0, t_max - t_min + 1)