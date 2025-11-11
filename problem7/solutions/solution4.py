def solve(n):
    """
    Find the position of Ayrat after n moves in a hexagonal spiral.
    Returns coordinates (x, y) in the axial coordinate system.
    """
    if n == 0:
        return (0, 0)
    
    # Directions in hexagonal grid (moving counterclockwise from the right)
    directions = [
        (1, 0),    # Right
        (0, 1),    # Down-right
        (-1, 1),   # Down-left
        (-1, 0),   # Left
        (0, -1),   # Up-left
        (1, -1)    # Up-right
    ]
    
    # Find which layer and position within layer
    # Layer k has 6k cells and total cells up to layer k: 3k^2 + 3k + 1
    layer = 1
    while 3 * layer * layer + 3 * layer + 1 < n:
        layer += 1
    
    # Total cells before current layer
    cells_before = 3 * (layer - 1) * (layer - 1) + 3 * (layer - 1) + 1
    pos_in_layer = n - cells_before
    
    # Starting position for the current layer
    # The spiral starts from one position away in the direction before "right"
    # For layer k, we start at position (k, -k) and move in 6 directions
    x, y = layer, -layer
    
    # Move through the layer
    steps_in_direction = 0
    direction_idx = 0
    
    for _ in range(pos_in_layer - 1):  # -1 because we count from the starting position
        dx, dy = directions[direction_idx]
        x += dx
        y += dy
        steps_in_direction += 1
        
        # Change direction every 'layer' steps
        if steps_in_direction == layer:
            steps_in_direction = 0
            direction_idx = (direction_idx + 1) % 6
    
    return (x, y)