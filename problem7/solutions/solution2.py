def solve(n):
    """
    Find the coordinates of position n in a hexagonal spiral starting at (0, 0).
    
    The spiral expands in rings around the origin. Ring k has 6k hexagons.
    Total positions through ring k: 1 + 3k(k+1)
    
    Args:
        n: Number of moves (0 ≤ n ≤ 10^18)
    
    Returns:
        Tuple (x, y) of the coordinates after n moves
        
    Examples:
        >>> hex_spiral_coordinates(0)
        (0, 0)
        >>> hex_spiral_coordinates(3)
        (-2, 0)
        >>> hex_spiral_coordinates(7)
        (3, 2)
    """
    if n == 0:
        return (0, 0)
    
    # Find which ring contains position n
    # Ring k ends at position: 1 + 3*k*(k+1)
    k = 0
    while 1 + 3 * (k + 1) * (k + 2) <= n:
        k += 1
    
    # Position within the ring (0-indexed)
    pos_in_ring = n - (1 + 3 * k * (k + 1))
    
    # Each ring has 6 sides, each with k steps
    # Six directions for hexagonal movement
    directions = [
        (1, -1),   # Direction 0
        (1, 0),    # Direction 1
        (0, 1),    # Direction 2
        (-1, 1),   # Direction 3
        (-1, 0),   # Direction 4
        (0, -1),   # Direction 5
    ]
    
    # Starting position at the beginning of ring k
    # Start at (k, -k) which is the starting point of ring k
    x, y = k, -k
    
    # Move within the ring
    side = pos_in_ring // k
    offset = pos_in_ring % k
    
    # Move along the appropriate sides
    for i in range(side):
        dx, dy = directions[i]
        x += dx * k
        y += dy * k
    
    # Move the remaining offset steps along the current side
    dx, dy = directions[side]
    x += dx * offset
    y += dy * offset
    
    return (x, y)