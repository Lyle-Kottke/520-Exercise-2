def solve(m, x):
    """
    Minimum number of traps needed to guarantee catching an x-mouse on campus.
    
    The x-mouse moves from room i to (i*x) mod m each second.
    We need to place traps such that regardless of the starting room,
    the mouse is guaranteed to be caught.
    
    Args:
        m: Number of rooms (2 <= m <= 10^14)
        x: Movement parameter (1 <= x < m, gcd(x,m) = 1)
    
    Returns:
        Minimum number of traps needed
    
    Examples:
        >>> catch_x_mouse(4, 3)
        3
        >>> catch_x_mouse(5, 2)
        2
    """
    
    def factorize(n):
        """Return prime factorization as dict {prime: exponent}"""
        factors = {}
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors[d] = factors.get(d, 0) + 1
                n //= d
            d += 1
        if n > 1:
            factors[n] = factors.get(n, 0) + 1
        return factors
    
    def multiplicative_order(x, n):
        """Find the multiplicative order of x modulo n"""
        factors = factorize(n)
        order = 1
        
        for p, e in factors.items():
            # Compute order of x modulo p^e
            pe = p ** e
            phi = p ** (e - 1) * (p - 1)
            
            divisors = []
            # Find divisors of phi
            d = 1
            while d * d <= phi:
                if phi % d == 0:
                    divisors.append(d)
                    if d != phi // d:
                        divisors.append(phi // d)
                d += 1
            
            divisors.sort()
            
            ord_pe = 1
            for div in divisors:
                if pow(x, div, pe) == 1:
                    ord_pe = div
                    break
            
            # LCM
            order = order * ord_pe // gcd(order, ord_pe)
        
        return order
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    ord_m_x = multiplicative_order(x, m)
    return 1 + (m - 1) // ord_m_x
