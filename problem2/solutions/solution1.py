def solve(n: int, k: int) -> tuple[int, int]:
    """
    Calculates the irreducible fraction A/B for the probability of at least two out of k
    people sharing a birthday in a year with 2^n days, and returns A mod (10^6+3) and B mod (10^6+3).

    :param n: Exponent such that 2^n is the number of days in a year.
    :param k: Number of people interviewed.
    :return: A and B modulo 10^6 + 3.
    """
    M = 1000003  # Modulo 10^6 + 3
    M_P = M - 1  # Modulo for exponent in Fermat's Little Theorem

    # 1. Edge Case: k > 2^n (Guaranteed shared birthday)
    # Since k <= 10^18, we only need to check for n <= 60.
    # If n is large (e.g., n=10^18), 2^n is much larger than k, so k <= 2^n.
    if n < 60 and k > (1 << n):
        return 1, 1

    # 2. Calculate V = v_2((k-1)!) using Legendre's formula: V = sum(floor((k-1)/2^j))
    def v2_factorial(x):
        if x < 0: return 0
        v = 0
        power_of_2 = 2
        while power_of_2 <= x:
            v += x // power_of_2
            # Check for overflow before multiplication if not using Python's arbitrary precision
            # Here, we can rely on Python's large integers for intermediate steps, but
            # we will only need the final result modulo M_P.
            if x // power_of_2 == 0: break # Safety break, though the condition above covers it
            if power_of_2 > x // 2: # Check to avoid overflow in power_of_2 * 2 if k was smaller
                break
            power_of_2 *= 2
        return v

    V = v2_factorial(k - 1)

    # 3. Calculate P2 = n + V
    P2_mod_M_P = (n % M_P + V % M_P) % M_P

    # 4. Calculate B mod M: B = 2^(n(k-1) - V)
    # Exponent E = n(k-1) - V
    n_mod_M_P = n % M_P
    k_minus_1_mod_M_P = (k - 1) % M_P
    V_mod_M_P = V % M_P
    
    # E mod M_P = ( (n mod M_P) * ((k-1) mod M_P) - (V mod M_P) ) mod M_P
    # Ensure intermediate product is also modulo M_P to prevent overflow if M_P was smaller
    E_mod_M_P = (n_mod_M_P * k_minus_1_mod_M_P) % M_P
    E_mod_M_P = (E_mod_M_P - V_mod_M_P + M_P) % M_P

    B = pow(2, E_mod_M_P, M)

    # 5. Calculate A mod M:
    # A = (2^(nk) - product(2^n - i for i=0..k-1)) / 2^P2

    # Modular inverse of 2^P2: I = (2^P2)^(-1) mod M = 2^(M - 2 - P2 mod M_P) mod M
    # The exponent for the inverse is M - 2 - (P2 mod M_P).
    # Since we need to compute pow(2, P2, M)^(-1), it's pow(pow(2, P2_mod_M_P, M), M-2, M).
    # Easier: pow(2, M - 2 - P2_mod_M_P, M)
    inverse_exp = (M_P - P2_mod_M_P) % M_P # M-1 - (P2 mod M-1)
    I = pow(2, inverse_exp, M)

    # Calculate A_comp mod M
    A_comp = 0 # Default for k >= M case
    
    # Case k < M: Compute A_comp = product(2^n - i) mod M
    if k < M:
        D_m = pow(2, n % M_P, M) # 2^n mod M
        A_comp = 1
        for i in range(k):
            term = (D_m - i) % M
            A_comp = (A_comp * term) % M
            
    # Case k >= M: A_comp must be 0 mod M because 2^n - i will be 0 mod M for some i < k
    # since D_m will hit D_m mod M = i for some i in {0, ..., M-1}.
    # The term 'i' in the product will reach D_m mod M.
    # e.g., i = D_m. term = D_m - D_m = 0. Product is 0.

    # Calculate B_total mod M
    # B_total = 2^(nk)
    nk_mod_M_P = ((n % M_P) * (k % M_P)) % M_P
    B_total = pow(2, nk_mod_M_P, M)
    
    # Calculate A' = B_total - A_comp mod M
    A_prime = (B_total - A_comp + M) % M

    # Calculate A = A' * I mod M
    A = (A_prime * I) % M
    
    return A, B