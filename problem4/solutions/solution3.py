import math

def egcd(a, b):
    """
    Extended Euclidean Algorithm: computes (g, s, t) such that a*s + b*t = g = gcd(a, b).
    Returns (gcd, s, t).
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, s_prime, t_prime = egcd(b % a, a)
        s = t_prime - (b // a) * s_prime
        t = s_prime
        return (g, s, t)

def solve_congruence(a1, b1, a2, b2):
    """
    Solves the system of congruences:
    x == b1 (mod a1)
    x == b2 (mod a2)

    Returns the smallest non-negative solution x_CRT and the common difference A = lcm(a1, a2).
    Returns (None, None) if no solution exists.
    """
    # System: a1*k == b2 - b1 (mod a2)
    C = b2 - b1
    g, s, _ = egcd(a1, a2)

    if C % g != 0:
        return None, None # No solution
    
    # Solve (a1/g) * k == (C/g) (mod a2/g)
    a1_prime = a1 // g
    a2_prime = a2 // g
    C_prime = C // g
    
    # s is the inverse of a1_prime modulo a2_prime, from a1*s + a2*t = g
    # After dividing by g: a1_prime*s + a2_prime*t = 1.
    # We need to ensure s is in the range [0, a2_prime-1] for the formula, 
    # but the general modulo operation handles it for any s returned by egcd.
    
    # k_part = (C_prime * s) mod a2_prime
    # Python's % operator works correctly for negative numbers with positive modulus:
    # a % n = a - n * floor(a/n)
    k_part = (C_prime * s) % a2_prime
    
    # The smallest non-negative solution x_CRT
    x_CRT = b1 + a1 * k_part
    
    # Common difference A = lcm(a1, a2) = (a1 * a2) / g
    # Use the division form to prevent overflow if a1*a2 is too large, though
    # a1*a2 is at most 4e18, which fits in standard 64-bit int.
    # a1 * a2_prime is safer.
    A = a1 * a2_prime 
    
    return x_CRT, A

def solve(a1, b1, a2, b2, L, R):
    """
    Finds the number of integers x such that L <= x <= R and x is in both APs 
    a1*k' + b1 and a2*l' + b2 for k', l' >= 0.
    """
    # 1. Find the general solution to the congruence system
    x_CRT, A = solve_congruence(a1, b1, a2, b2)

    if x_CRT is None:
        return 0

    # 2. Find the smallest valid term x_start satisfying k', l' >= 0
    # x must be >= max(b1, b2). Let B = max(b1, b2).
    B = max(b1, b2)
    
    # We need x_CRT + A * m >= B, or A * m >= B - x_CRT.
    Delta = B - x_CRT
    
    # Helper to calculate ceil(P/Q) for integer P and Q > 0
    def ceil_div(P, Q):
        if P <= 0:
            return P // Q
        else:
            return (P + Q - 1) // Q

    m_start = ceil_div(Delta, A)
    x_start = x_CRT + A * m_start
    
    # If the smallest valid term is already greater than R, there are no solutions.
    if x_start > R:
        return 0

    # 3. Count terms x = x_start + A * m in range [L, R] for m >= 0
    
    # The sequence of intersection points starts at x_start, so we only need to 
    # find the range of m for the segment [max(L, x_start), R].
    
    # New lower bound for the sequence: max(L, x_start)
    L_eff = max(L, x_start)

    # Find m_max: x_start + A * m_max <= R => A * m_max <= R - x_start
    # m_max = floor((R - x_start) / A)
    m_max = (R - x_start) // A
    
    # Find m_min: x_start + A * m_min >= L_eff => A * m_min >= L_eff - x_start
    # m_min = ceil((L_eff - x_start) / A)
    # Since L_eff >= x_start, L_eff - x_start >= 0.
    L_diff = L_eff - x_start
    m_min = ceil_div(L_diff, A)
    
    # The number of integers is m_max - m_min + 1, if m_max >= m_min
    count = m_max - m_min + 1
    
    return max(0, count)