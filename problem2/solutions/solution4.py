def solve(n, k):
    MOD = 10**6 + 3
    
    # Helper function for modular exponentiation
    def pow_mod(base, exp, mod):
        result = 1
        base %= mod
        while exp > 0:
            if exp & 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp >>= 1
        return result
    
    # Helper function for GCD
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # Helper function for modular inverse
    def mod_inverse(a, mod):
        return pow_mod(a, mod - 2, mod)
    
    # Edge case: if k > 2^n, probability is 1
    # We check if k > 2^n by comparing log values
    # k > 2^n means log2(k) > n
    if n < 64:
        days = 1 << n  # 2^n
        if k > days:
            return "1 1"
    else:
        # For large n, if k <= 10^18 and n >= 64, then k <= 2^n
        # because 2^64 > 10^18
        pass
    
    # Calculate the numerator of P(all different)
    # = 2^n * (2^n - 1) * (2^n - 2) * ... * (2^n - k + 1)
    # Denominator = 2^(n*k)
    
    # Count factors of 2 in numerator
    # Numerator has k terms, starting with 2^n
    # We need to compute this mod MOD
    
    # Compute 2^n mod MOD
    two_power_n = pow_mod(2, n, MOD)
    
    # Compute product (2^n) * (2^n - 1) * ... * (2^n - k + 1) mod MOD
    numerator_complement = 1
    for i in range(k):
        term = (two_power_n - i) % MOD
        if term < 0:
            term += MOD
        numerator_complement = (numerator_complement * term) % MOD
        if numerator_complement == 0:
            break
    
    # Compute denominator = 2^(n*k) mod MOD
    denominator = pow_mod(2, (n * k) % (MOD - 1), MOD)
    
    # Final numerator = denominator - numerator_complement
    numerator = (denominator - numerator_complement) % MOD
    if numerator < 0:
        numerator += MOD
    
    # Reduce to coprime form
    g = gcd(numerator, denominator)
    numerator //= g
    denominator //= g
    
    return (numerator,denominator)