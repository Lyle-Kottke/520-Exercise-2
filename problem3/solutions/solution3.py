import sys

def check_limak_journey(journey_data):
    """
    Checks if Limak's journey satisfies the validity conditions.

    The Earth is modeled as a sphere. The distance from the North Pole (NP) 
    to the South Pole (SP) along a meridian is 20,000 km.

    Args:
        journey_data (list): A list of tuples/lists, where each element 
                             is (t_i, dir_i) - distance and direction.

    Returns:
        str: "YES" if the journey is valid, "NO" otherwise.
    """
    
    # Distance from North Pole to South Pole
    MAX_DIST = 20000 
    
    # current_dist: Distance from the North Pole (Latitude tracking)
    # Starts at North Pole
    current_dist = 0  

    for t, direction in journey_data:
        # --- A. Pole Constraint Check (Before Movement) ---
        
        # 1. Check for North Pole (current_dist = 0)
        if current_dist == 0:
            # Must move South
            if direction != "South":
                return "NO"
        
        # 2. Check for South Pole (current_dist = MAX_DIST)
        elif current_dist == MAX_DIST:
            # Must move North
            if direction != "North":
                return "NO"

        # 3. Check for East/West movements
        # East/West movements are only valid when NOT on a pole.
        # This is already implicitly handled by the previous checks:
        # If current_dist is 0 or 20000, any East/West direction would have
        # resulted in an early "NO".
        if direction in ["East", "West"]:
            # East/West movements do not change the distance from the NP.
            # No change to current_dist, and no boundary check is needed.
            continue
            
        # --- B. Movement Update ---

        if direction == "North":
            new_dist = current_dist - t
        elif direction == "South":
            new_dist = current_dist + t
        else:
            # This should not be reached if the input is guaranteed to be one of the four
            # but is good practice to handle.
            return "NO" 

        # --- C. Boundary Check (During/After Movement) ---

        # The new position must be between NP (0) and SP (MAX_DIST) inclusive.
        if new_dist < 0 or new_dist > MAX_DIST:
            # Limak crossed a pole, violating the "at any moment" condition.
            return "NO"
        
        # Update position for the next step
        current_dist = new_dist

    # --- 3. Final Check ---
    # The journey must end on the North Pole (current_dist = 0)
    if current_dist == 0:
        return "YES"
    else:
        return "NO"

# The final, callable function based on the problem statement
def solve(n, steps):
    """
    The main function to call the logic with the problem's parameters.
    
    Args:
        n (int): The number of steps.
        steps (list): A list of (t_i, dir_i) pairs.
        
    Returns:
        str: "YES" or "NO".
    """
    # The structure of `steps` already matches the expected journey_data format
    return check_limak_journey(steps)