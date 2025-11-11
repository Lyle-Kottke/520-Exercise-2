import sys

# Set a higher recursion limit for potential deep calls, although not strictly necessary here.
# sys.setrecursionlimit(2000)

def power_mod(base, exponent, modulus):
    """Computes (base^exponent) % modulus using modular exponentiation."""
    result = 1
    base %= modulus
    if exponent < 0:
        # Should not happen with current logic, but a safeguard for a full inverse power function
        raise ValueError("Negative exponent not supported for this logic.")
    
    # Exponent is reduced modulo phi(modulus) for Fermat's Little Theorem (if modulus is prime)
    # or Euler's Totient Theorem (otherwise).
    # Since M = 10^6 + 3 is prime, phi(M) = M-1.
    exp_mod = exponent % (modulus - 1)
    
    while exp_mod > 0:
        if exp_mod % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exp_mod //= 2
    return result

def v2_factorial(n_val):
    """Calculates v_2(n_val!) using Legendre's formula. n_val is (k-1) here."""
    if n_val < 0:
        return 0
    p2 = 2
    exponent = 0
    # Since n_val is up to 10^18, we can use a loop up to 60 as 2^60 > 10^18.
    while n_val // p2 > 0 and p2 <= 2**60: 
        exponent += n_val // p2
        p2 *= 2
    return exponent

def solve(n, k):
    """
    Calculates the irreducible fraction A/B for the birthday paradox probability
    with 2^n days and k people, and returns A mod M, B mod M.
    M = 10^6 + 3.
    """
    M = 10**6 + 3

    # --- 1. Pigeonhole Principle Check ---
    # k > 2^n guarantees probability 1 (A=1, B=1).
    # Since k <= 10^18, this only happens for n < 61.
    if n < 62 and k > (1 << n):
        return 1, 1

    # --- 2. Calculate Exponents for Power of 2 Reduction ---
    # k is large, so k-1 is also large.
    k_minus_1 = k - 1
    
    # v_2((k-1)!)
    v2_k_minus_1_fact = v2_factorial(k_minus_1)

    # Power of 2 dividing the product P(D, k): p_prod = n + v_2((k-1)!)
    # Since n is up to 10^18 and v_2 is up to 10^18, this can exceed standard 64-bit int.
    # Python handles large integers, but we only need to compare it with n*k, so a direct
    # computation is safe, as n*k will be even larger and comparison won't overflow.
    p_prod = n + v2_k_minus_1_fact

    # Power of 2 dividing the unreduced denominator: p_den = n * k
    p_den = n * k

    # Reduction factor exponent: p = min(p_den, p_prod).
    # Since k >= 2, k-1 >= 1. We know p_prod <= p_den must hold:
    # n + v2_k_minus_1_fact <= nk => v2_k_minus_1_fact <= n(k-1). 
    # This is true because v2(m!) < m.
    # Therefore, p = p_prod.
    p = p_prod
    
    # Denominator exponent: E_B = nk - p
    E_B = p_den - p
    
    # --- 3. Calculate Denominator B (mod M) ---
    B = power_mod(2, E_B, M)

    # --- 4. Calculate P_odd (mod M) ---
    # P_odd = product_{i=0}^{k-1} [ (2^n - i) / 2^(v2(2^n-i)) ] (mod M)
    
    # Pre-calculate 2^n mod M
    # Since n is large, use (n mod M-1) for the exponent.
    n_mod_M_minus_1 = n % (M - 1)
    D_M = power_mod(2, n_mod_M_minus_1, M) # 2^n mod M
    
    P_odd = 1
    
    # We only need to compute the product up to i=M, because if k-1 >= M, 
    # one of the terms (D_M - i) will be 0 mod M, making the entire product 0 mod M.
    # The max index to iterate is min(k-1, M).
    max_i = min(k_minus_1, M)
    
    # The product is for i = 0 to k-1.
    for i in range(max_i + 1):
        # Current term: (2^n - i) / 2^(v_2(i)) (mod M)
        
        # Numerator: (2^n - i) mod M
        # Using 2^n mod M is D_M.
        num = (D_M - i + M) % M 
        
        # Denominator: 2^(v_2(i)) mod M
        if i == 0:
            # i=0 term: (2^n) / 2^(v_2(2^n)) = 2^n / 2^n = 1
            term_mod = 1
        else:
            # Denominator: 2^(v_2(i)) mod M
            v2_i = 0
            temp_i = i
            while temp_i > 0 and temp_i % 2 == 0:
                v2_i += 1
                temp_i //= 2
            
            # Modular Inverse: 1 / 2^v2_i = (2^v2_i)^(-1) mod M
            # inv_den = 2^(-v2_i) = 2^(M-1 - (v2_i mod M-1)) mod M
            # Since v2_i will be small (at most 60 for i <= M), we don't need M-1 mod.
            inv_den_exp = (M - 1) - v2_i
            inv_den = power_mod(2, inv_den_exp, M)
            
            # Final term for P_odd: (num * inv_den) mod M
            term_mod = (num * inv_den) % M
        
        P_odd = (P_odd * term_mod) % M

    # If k-1 > M (i.e., max_i = M), one term in the product must have been 0 mod M, 
    # so P_odd should be 0. The loop already handles this implicitly if k-1 >= D_M.
    # Since i runs up to M, and D_M is in [1, M-1], the loop will hit i=D_M, where num=0.
    # The exception is if k-1 < D_M, but k-1 >= M, which is impossible since D_M < M.
    # Therefore, P_odd = 0 if k-1 >= M.
    if k_minus_1 >= M:
        P_odd = 0
        
    # --- 5. Calculate Numerator A (mod M) ---
    # A = (2^(nk-p_prod) - P_odd) mod M = (B - P_odd) mod M
    A = (B - P_odd + M) % M

    return A, B
