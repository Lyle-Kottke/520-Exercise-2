def solve(n: int, moves: list[tuple[int, str]]) -> str:
    """
    Checks if Limak's journey from the North Pole is valid according to the rules:
    1. Only South movement allowed at North Pole (distance 0).
    2. Only North movement allowed at South Pole (distance 20000).
    3. The journey must end at the North Pole.

    The Earth is a sphere, with the pole-to-pole distance being 20,000 km.
    We track Limak's position as the distance from the North Pole along a meridian.

    Args:
        n: The number of parts in the journey.
        moves: A list of tuples, where each tuple is (distance, direction).
               Example: [(7500, "South"), (10000, "East"), ...]

    Returns:
        "YES" if the journey is valid, "NO" otherwise.
    
    Examples:
        check_limak_journey(5, [(7500, "South"), (10000, "East"), (3500, "North"), (4444, "West"), (4000, "North")]) == "YES"
        check_limak_journey(2, [(15000, "South"), (4000, "East")]) == "NO"
        check_limak_journey(3, [(20000, "South"), (10, "East"), (20000, "North")]) == "NO"
        check_limak_journey(2, [(1000, "North"), (1000, "South")]) == "NO" # Starts at NP, can't move North
    """
    # Initialize position: distance from North Pole (NP).
    # NP is 0 km, South Pole (SP) is 20000 km.
    current_distance_from_NP = 0
    POLE_DISTANCE = 20000

    for distance, direction in moves:
        # Check pole constraints before the move (Conditions 1 and 2)
        if current_distance_from_NP == 0:  # At North Pole
            # Only South movement allowed.
            if direction != "South":
                return "NO"
        elif current_distance_from_NP == POLE_DISTANCE:  # At South Pole
            # Only North movement allowed.
            if direction != "North":
                return "NO"
        else:
            # If not at a pole, East/West/North/South are all fine to start the move.
            # However, East/West are only valid if not at a pole.
            if direction in ("West", "East"):
                # A movement East or West when not at a pole is valid for the start.
                # The position (distance from NP) does not change, and it remains within [0, 20000].
                continue

        # Execute the move and update position
        if direction == "South":
            current_distance_from_NP += distance
        elif direction == "North":
            current_distance_from_NP -= distance
        # East/West movements don't change the distance from the poles (handled above)

        # Check boundary constraint during/after the move.
        # If the move takes Limak past the poles, the journey is invalid.
        if not (0 <= current_distance_from_NP <= POLE_DISTANCE):
            return "NO"

    # Final check: The journey must end on the North Pole (Condition 3)
    if current_distance_from_NP == 0:
        return "YES"
    else:
        return "NO"