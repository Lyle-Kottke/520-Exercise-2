def solve(n: int, L: int, kefa_distances: list[int], sasha_distances: list[int]) -> str:
    """
    Checks if Kefa's and Sasha's track barrier arrangements coincide by comparing
    the circular sequences of inter-barrier distances.

    Args:
        n: The number of barriers.
        L: The length of the circular track.
        kefa_distances: Sorted list of distances from Kefa's start to each barrier.
        sasha_distances: Sorted list of distances from Sasha's start to each barrier.

    Returns:
        "YES" if the tracks coincide, otherwise "NO".
    """

    # 1. Calculate Kefa's inter-barrier distances (D_K)
    # Distances between consecutive barriers (k_{i+1} - k_i)
    d_k_consecutive = [kefa_distances[i+1] - kefa_distances[i] for i in range(n - 1)]
    # Distance from the last barrier back to the first barrier (L - k_n + k_1)
    d_k_wrap = L - kefa_distances[n - 1] + kefa_distances[0]
    D_K = d_k_consecutive + [d_k_wrap]

    # 2. Calculate Sasha's inter-barrier distances (D_S)
    # Distances between consecutive barriers (s_{i+1} - s_i)
    d_s_consecutive = [sasha_distances[i+1] - sasha_distances[i] for i in range(n - 1)]
    # Distance from the last barrier back to the first barrier (L - s_n + s_1)
    d_s_wrap = L - sasha_distances[n - 1] + sasha_distances[0]
    D_S = d_s_consecutive + [d_s_wrap]

    # 3. Check if D_S is a circular shift of D_K
    # The tracks coincide if and only if the two sequences of relative
    # distances are circular permutations of each other.
    
    # We can check this by iterating through all n possible circular shifts of D_K.
    
    is_circular_shift = False
    
    # Optimization: if the sets of distances are not the same, they cannot be a circular shift
    # This also handles the case where L might not be the same for the two tracks (although L is given as the same).
    if sorted(D_K) != sorted(D_S):
        return "NO"

    for i in range(n):
        # Create the i-th circular shift of D_K: D_K[i], D_K[i+1], ..., D_K[n-1], D_K[0], ..., D_K[i-1]
        shifted_D_K = D_K[i:] + D_K[:i]
        
        if shifted_D_K == D_S:
            is_circular_shift = True
            break
            
    if is_circular_shift:
        return "YES"
    else:
        return "NO"

# Example 1 Test (from problem statement)
# n=3, L=8
# Kefa: [2, 4, 6] -> D_K = [2, 2, 4]
# Sasha: [1, 5, 7] -> D_S = [4, 2, 2]
# print(f"Example 1: {check_tracks(3, 8, [2, 4, 6], [1, 5, 7])}") # Expected: YES

# Example 2 Test (from problem statement)
# n=4, L=9
# Kefa: [2, 3, 5, 8] -> D_K = [1, 2, 3, 3]
# Sasha: [0, 1, 3, 6] -> D_S = [1, 2, 3, 3] (No shift, they match directly)
# print(f"Example 2: {check_tracks(4, 9, [2, 3, 5, 8], [0, 1, 3, 6])}") # Expected: YES

# Example 3 Test (from problem statement)
# n=2, L=4
# Kefa: [1, 3] -> D_K = [2, 2]
# Sasha: [1, 2] -> D_S = [1, 3]
# print(f"Example 3: {check_tracks(2, 4, [1, 3], [1, 2])}") # Expected: NO