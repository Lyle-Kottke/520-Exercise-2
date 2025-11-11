def solve(n, instructions):
    """
    Validate Limak's journey around Earth.
    
    Args:
        n: number of instructions
        instructions: list of tuples (distance, direction)
    
    Returns:
        "YES" if valid, "NO" otherwise
    """
    distance_from_north = 0  # Current distance from North Pole (0 to 20000)
    
    for distance, direction in instructions:
        # Check if we're at a pole and have an invalid instruction
        if distance_from_north == 0:  # At North Pole
            if direction != "South":
                return "NO"
        elif distance_from_north == 20000:  # At South Pole
            if direction != "North":
                return "NO"
        else:  # Not at a pole
            if direction in ["East", "West"]:
                # East/West movements are valid away from poles
                pass
            elif direction == "South":
                # Moving south (away from North Pole)
                pass
            elif direction == "North":
                # Moving north (toward North Pole)
                pass
        
        # Simulate the movement
        if direction == "South":
            distance_from_north += distance
            # Check if we exceeded South Pole
            if distance_from_north > 20000:
                return "NO"
        elif direction == "North":
            distance_from_north -= distance
            # Check if we went past North Pole
            if distance_from_north < 0:
                return "NO"
        elif direction in ["East", "West"]:
            # East/West at poles is invalid (checked above)
            pass
    
    # Must end at North Pole
    if distance_from_north == 0:
        return "YES"
    else:
        return "NO"