def solve(n, a, b):
    """
    Find the maximum possible minimum number of pieces on any plate.
    
    Args:
        n: number of plates (2 <= n <= a + b)
        a: number of pieces of cake 1 (1 <= a <= 100)
        b: number of pieces of cake 2 (1 <= b <= 100)
    
    Returns:
        Maximum possible value x such that each plate has at least x pieces
    
    Examples:
        >>> distribute_cakes(5, 2, 3)
        1
        >>> distribute_cakes(4, 7, 10)
        3
    """
    max_min_pieces = 0
    
    # Try all possible ways to split n plates between the two cakes
    # i plates for cake 1, (n-i) plates for cake 2
    for i in range(1, n):
        plates_for_cake1 = i
        plates_for_cake2 = n - i
        
        # Minimum pieces on any plate from cake 1
        min_pieces_cake1 = a // plates_for_cake1
        
        # Minimum pieces on any plate from cake 2
        min_pieces_cake2 = b // plates_for_cake2
        
        # The bottleneck is the minimum of these two
        min_pieces = min(min_pieces_cake1, min_pieces_cake2)
        
        # Update the maximum
        max_min_pieces = max(max_min_pieces, min_pieces)
    
    return max_min_pieces