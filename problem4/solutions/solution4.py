def gcd_extended(a, b):
    """Extended GCD: returns (gcd, x, y) such that a*x + b*y = gcd"""
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = gcd_extended(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def gcd(a, b):
    """Simple GCD"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Least common multiple"""
    return a * b // gcd(a, b)

def solve(a1, b1, a2, b2, L, R):
    """
    Find count of integers x in [L, R] such that:
    x = a1*k' + b1 (k' >= 0)
    x = a2*l' + b2 (l' >= 0)
    """
    g = gcd(a1, a2)
    
    # Check if solution exists
    if (b2 - b1) % g != 0:
        return 0
    
    # Find one solution using extended GCD
    # We need: a1*k' + b1 = a2*l' + b2
    # Rearranged: a1*k' - a2*l' = b2 - b1
    # Let a1*u + a2*v = g (using extended GCD on a1, a2)
    # Then a1*(u*(b2-b1)/g) + a2*(-v*(b2-b1)/g) = b2 - b1
    
    _, u, v = gcd_extended(a1, a2)
    diff = b2 - b1
    
    # k' = u * (diff / g), l' = -v * (diff / g)
    k0 = u * (diff // g)
    
    # x0 = a1*k0 + b1
    x0 = a1 * k0 + b1
    
    # The period of solutions
    period = lcm(a1, a2)
    
    # Normalize x0 to be the smallest non-negative solution
    # x = x0 + t*period for integer t
    # We need x >= max(b1, b2)
    
    min_x = max(b1, b2)
    
    # Find the smallest x0 such that x0 >= min_x
    # x0 + t*period >= min_x
    # t >= (min_x - x0) / period
    
    if x0 < min_x:
        t_min = (min_x - x0 + period - 1) // period  # ceiling division
        x0 = x0 + t_min * period
    else:
        # Reduce x0 to the fundamental solution
        t = x0 // period
        x0 = x0 - t * period
        if x0 < min_x:
            x0 = x0 + period
    
    # Now x0 is the smallest solution >= min_x
    if x0 > R:
        return 0
    
    # Count solutions in [L, R]
    # We need L <= x0 + t*period <= R
    # L <= x0 + t*period  =>  t >= (L - x0) / period
    # x0 + t*period <= R  =>  t <= (R - x0) / period
    
    t_min = max(0, (L - x0 + period - 1) // period)  # ceiling
    t_max = (R - x0) // period  # floor
    
    if t_max < t_min:
        return 0
    
    return t_max - t_min + 1