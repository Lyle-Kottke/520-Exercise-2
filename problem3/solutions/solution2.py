def solve(n, instructions):
    """
    Validate if Limak's journey satisfies all conditions.
    
    Args:
        n: Number of instructions
        instructions: List of tuples (distance, direction)
    
    Returns:
        "YES" if valid, "NO" otherwise
    
    Examples:
        - validate_limak_journey(5, [(7500, "South"), (10000, "East"), (3500, "North"), (4444, "West"), (4000, "North")]) == "YES"
        - validate_limak_journey(2, [(15000, "South"), (4000, "East")]) == "NO"
        - validate_limak_journey(2, [(1000, "North"), (1000, "South")]) == "NO"
    """
    
    position = 0  # Start at North Pole (distance 0 from North Pole)
    
    # Check initial condition: at North Pole, must move South
    if n > 0 and instructions[0][1] != "South":
        return "NO"
    
    for distance, direction in instructions:
        # Check pole constraints before moving
        if position == 0 and direction != "South":
            # At North Pole, can only go South
            return "NO"
        if position == 20000 and direction != "North":
            # At South Pole, can only go North
            return "NO"
        
        # Can't move East or West at poles
        if (position == 0 or position == 20000) and direction in ["East", "West"]:
            return "NO"
        
        # Update position based on direction
        if direction == "South":
            position += distance
        elif direction == "North":
            position -= distance
        # East and West don't change the North-South position
        
        # Handle wraparound and pole constraints during movement
        # Position can go from 0 to 40000 on a meridian (circular)
        # 0 = North Pole, 20000 = South Pole, back to 0
        
        # Normalize position to be within [0, 40000)
        position = position % 40000
        
        # Check if we're at a pole after the move
        if position == 0 or position == 20000:
            continue  # Poles are valid endpoints of moves
    
    # Final condition: must end at North Pole
    if position != 0:
        return "NO"
    
    return "YES"