def solve(m, x):
    """
    Find minimum number of traps needed.
    
    The number of orbits under the map i -> i*x mod m equals the
    number of divisors of m (when gcd(x,m)=1).
    
    This is a known result from group theory: for a cyclic group
    acting by multiplication, the orbits correspond to divisors.
    """
    
    def count_divisors(n):
        """Count divisors of n efficiently for n up to 10^14"""
        count = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                count += 1
                if i * i != n:
                    count += 1
            i += 1
        return count
    
    return count_divisors(m)