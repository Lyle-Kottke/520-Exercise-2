# The final function call structure is required to be just the function itself.
# The following is the required final function.
def solve(a1: int, b1: int, a2: int, b2: int, L: int, R: int) -> int:
    """
    Calculates the number of integers x such that L <= x <= R and x is in the 
    intersection of the two arithmetic progressions:
    x = a1*k' + b1 and x = a2*l' + b2, for some integers k', l' >= 0.

    This is equivalent to solving the system of congruences:
    x === b1 (mod a1)
    x === b2 (mod a2)

    Args:
        a1: Common difference of the first AP (a1 > 0).
        b1: Initial offset of the first AP.
        a2: Common difference of the second AP (a2 > 0).
        b2: Initial offset of the second AP.
        L: Lower bound of the range.
        R: Upper bound of the range.

    Returns:
        The number of common terms in the range [L, R].
    
    Edge cases handled:
    - No solution to the system (b1-b2 not divisible by gcd(a1, a2)).
    - L > R.
    - Negative b1, b2, L, R, and intermediate x_base.
    - Large inputs (up to 2*10^9).
    """
    import math

    def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
        """
        Extended Euclidean Algorithm: finds g = gcd(a, b) and integers x, y
        such that ax + by = g.
        Returns (g, x, y).
        """
        if a == 0:
            return (b, 0, 1)
        g, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (g, x, y)

    if L > R:
        return 0
    
    # 1. Check for solvability
    g = math.gcd(a1, a2)
    
    if (b2 - b1) % g != 0:
        return 0

    # 2. Find the smallest non-negative solution x0
    
    # Solve the LDE: a1*k' - a2*l' = b2 - b1
    # We solve a1*k_aux + a2*l_aux = g using EEA
    g_e, k_aux, l_aux = extended_gcd(a1, a2)
    
    # Particular solution for a1*k' + a2*l' = b2 - b1:
    c_g_ratio = (b2 - b1) // g
    k_prime_p = k_aux * c_g_ratio
    
    # M is the modulus of the new AP: M = lcm(a1, a2)
    M = (a1 // g) * a2
    
    # x_base is the particular solution corresponding to t=0
    x_base = a1 * k_prime_p + b1
    
    # x0 is the smallest non-negative solution: x0 = x_base mod M
    # Python's % is mathematical modulo, ensuring 0 <= x0 < M
    x0 = x_base % M
    
    # 3. Count solutions in the range [L, R]
    
    # We need to find the number of integers k such that:
    # L <= M*k + x0 <= R  =>  (L - x0) / M <= k <= (R - x0) / M
    
    numerator_min = L - x0
    numerator_max = R - x0
    
    # k_max = floor((R - x0) / M)
    k_max = numerator_max // M
    
    # k_min = ceil((L - x0) / M) = -floor(-(L - x0) / M)
    k_min = -( (-numerator_min) // M )
    
    count = k_max - k_min + 1
    
    return max(0, count)