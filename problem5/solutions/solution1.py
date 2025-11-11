import math

def solve(n: int, a: int, b: int) -> int:
    """
    Calculates the maximum possible number x such that the cakes can be distributed
    among n plates where each plate has at least x pieces and no plate has
    pieces from both cakes.

    The problem is solved using binary search on the possible answer x, which
    maximizes the minimum number of pieces per plate.

    Args:
        n: The total number of plates (people). (2 <= n <= a + b)
        a: The number of pieces of the first cake. (1 <= a <= 100)
        b: The number of pieces of the second cake. (1 <= b <= 100)

    Returns:
        The maximum possible minimum number of pieces per plate, x.

    Examples:
        >>> calculate_max_min_pieces(5, 2, 3)
        1
        >>> calculate_max_min_pieces(4, 7, 10)
        3
        >>> calculate_max_min_pieces(2, 10, 10)
        10
        >>> calculate_max_min_pieces(10, 10, 10)
        2
        >>> calculate_max_min_pieces(100, 100, 100)
        2
        >>> calculate_max_min_pieces(2, 1, 100)
        1
    """
    
    # 1. Define the search space for x.
    # The minimum is at least 1 (since a, b >= 1 and n <= a+b).
    # The maximum is the average number of pieces, or a/1, b/1. max(a,b) is a safe upper bound.
    # The smallest possible maximum is the floor of the average.
    low = 1
    high = (a + b) // n # A tighter upper bound for x
    max_x = 0

    # If the combined pieces is less than n, then (a+b)//n will be less than 1 (if n>a+b)
    # but the problem constraints ensure 2 <= n <= a + b, so high >= 1.

    # 2. Binary search for the maximum x.
    while low <= high:
        mid = low + (high - low) // 2
        
        # Check if it's possible to distribute the cakes such that each plate has at least 'mid' pieces.
        # Plates for Cake 1: max_plates_a = floor(a / mid)
        # Plates for Cake 2: max_plates_b = floor(b / mid)
        # The distribution is possible if the total available plates is at least n.
        
        # Avoid division by zero, though mid >= 1 ensures this isn't strictly necessary.
        if mid == 0:
            low = 1
            continue
            
        max_plates_a = a // mid
        max_plates_b = b // mid
        
        total_available_plates = max_plates_a + max_plates_b
        
        if total_available_plates >= n:
            # 'mid' is a possible minimum. We store it and try for a larger minimum.
            max_x = mid
            low = mid + 1
        else:
            # 'mid' is too large to be the minimum. We must search in the lower half.
            high = mid - 1
            
    # 3. Return the maximum possible minimum x found.
    return max_x