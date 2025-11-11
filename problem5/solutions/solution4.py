def solve(n, a, b):
    """
    Find the maximum possible minimum number of pieces per plate.
    
    Args:
        n: number of plates
        a: number of pieces in cake 1
        b: number of pieces in cake 2
    
    Returns:
        The maximum value x such that every plate has at least x pieces
    """
    max_min = 0
    
    # Try all possible distributions of plates between the two cakes
    for p1 in range(1, n):
        p2 = n - p1
        
        # Calculate minimum pieces per plate for each cake
        min_per_plate_cake1 = a // p1
        min_per_plate_cake2 = b // p2
        
        # The minimum across all plates for this distribution
        min_pieces = min(min_per_plate_cake1, min_per_plate_cake2)
        
        # Update the maximum of minimums
        max_min = max(max_min, min_pieces)
    
    return max_min