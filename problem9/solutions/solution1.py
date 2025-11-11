def solve(n: int, l: int, kefa_distances: list[int], sasha_distances: list[int]) -> str:
    """
    Checks if Kefa's and Sasha's tracks coincide based on their barrier distance measurements.

    The tracks coincide if the cyclic sequence of distances between adjacent barriers
    is the same for both, potentially rotated.

    Args:
        n: The number of barriers on a track.
        l: The length of the track.
        kefa_distances: The distances from Kefa's start to each barrier.
        sasha_distances: The distances from Sasha's start to each barrier.

    Returns:
        "YES" if the tracks coincide, "NO" otherwise.
    """

    if n == 0:
        # A track with no barriers is always the same.
        return "NO"
    
    # 1. Calculate the cyclic inter-barrier distances for Kefa
    # Distance is k[i+1] - k[i] for i from 0 to n-2, and L - k[n-1] + k[0] for the last segment.
    
    # Python slicing makes this concise. We append the first barrier distance (k[0]) 
    # to the end of the list and then compute differences.
    kefa_full_cycle = kefa_distances + [l + kefa_distances[0]]
    kefa_diffs = []
    for i in range(n):
        kefa_diffs.append(kefa_full_cycle[i+1] - kefa_distances[i])

    # 2. Calculate the cyclic inter-barrier distances for Sasha
    sasha_full_cycle = sasha_distances + [l + sasha_distances[0]]
    sasha_diffs = []
    for i in range(n):
        sasha_diffs.append(sasha_full_cycle[i+1] - sasha_distances[i])

    # 3. Compare the cyclic sequences
    # A list 'A' is a cyclic shift of list 'B' if 'B' is a subsegment of 'A' + 'A'
    
    # Convert lists to strings for easy pattern matching of sequences, 
    # ensuring elements are properly separated to avoid false positives (e.g., [1, 2] and [12]).
    kefa_diffs_str = " ".join(map(str, kefa_diffs))
    sasha_diffs_str = " ".join(map(str, sasha_diffs))

    # Create the doubled sequence string
    kefa_diffs_double_str = kefa_diffs_str + " " + kefa_diffs_str

    # Check if the Sasha sequence is a subsegment of the doubled Kefa sequence
    if sasha_diffs_str in kefa_diffs_double_str:
        return "YES"
    else:
        return "NO"