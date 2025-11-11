def solve(n, L, kefa, sasha):
    """
    Determine if Kefa and Sasha ran on the same track.
    
    Two sequences represent the same track if one is a rotation of the other
    when we consider the gaps between consecutive barriers.
    
    Args:
        n: number of barriers
        L: track length
        kefa: list of n distances from Kefa's start to each barrier
        sasha: list of n distances from Sasha's start to each barrier
    
    Returns:
        "YES" if they ran the same track, "NO" otherwise
    
    Edge cases:
        - n=1: single barrier (trivial case, always YES)
        - gaps that wrap around the track
        - different orderings due to different starting positions
    """
    # Calculate gaps between consecutive barriers for Kefa
    kefa_gaps = []
    for i in range(n):
        next_i = (i + 1) % n
        gap = (kefa[next_i] - kefa[i]) % L
        kefa_gaps.append(gap)
    
    # Calculate gaps between consecutive barriers for Sasha
    sasha_gaps = []
    for i in range(n):
        next_i = (i + 1) % n
        gap = (sasha[next_i] - sasha[i]) % L
        sasha_gaps.append(gap)
    
    # Check if sasha_gaps is a rotation of kefa_gaps
    # This is done by checking if sasha_gaps appears in kefa_gaps + kefa_gaps
    kefa_doubled = kefa_gaps + kefa_gaps
    
    # Check if sasha_gaps is a contiguous subsequence in kefa_doubled
    for i in range(n):
        if kefa_doubled[i:i+n] == sasha_gaps:
            return "YES"
    
    return "NO"