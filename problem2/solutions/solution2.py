def solve(n, k):
    MOD = 10**6 + 3
    
    # If k > 2^n, answer is 1/1
    if n <= 60 and k > (1 << n):
        return (1, 1)
    
    def pow_mod(base, exp, mod):
        result = 1
        base %= mod
        while exp > 0:
            if exp & 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp >>= 1
        return result
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # Calculate 2^n mod MOD
    two_n_mod = pow_mod(2, n, MOD)
    
    # Numerator of P(all different) = product of (2^n - i) for i in [0, k-1]
    num = 1
    for i in range(k):
        num = num * (two_n_mod - i % MOD + MOD) % MOD
    
    # Denominator = 2^(n*k) mod MOD
    # Since MOD is prime, use Fermat: 2^(MOD-1) ≡ 1, so 2^(n*k) = 2^(n*k mod (MOD-1))
    nk_mod = (n % (MOD - 1)) * (k % (MOD - 1)) % (MOD - 1)
    den = pow_mod(2, nk_mod, MOD)
    
    # P(at least 2 same) = 1 - num/den = (den - num)/den
    A = (den - num + MOD) % MOD
    B = den
    
    # Reduce by GCD
    g = gcd(A, B)
    A = A // g % MOD
    B = B // g % MOD
    
    return (A, B)