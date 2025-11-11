def solve(n, m, field):
    """
    Validates if a field represents a correct Berland flag.
    
    The flag must have:
    - 3 equal-width/height stripes parallel to sides
    - Each stripe is one color (R, G, or B)
    - All three colors used exactly once
    
    Args:
        n: number of rows
        m: number of columns
        field: list of m strings, each representing a row
    
    Returns:
        "YES" if valid flag, "NO" otherwise
    
    Examples:
        >>> is_valid_berland_flag(6, 5, ["RRRRR", "RRRRR", "BBBBB", "BBBBB", "GGGGG", "GGGGG"])
        'YES'
        >>> is_valid_berland_flag(4, 3, ["BRG", "BRG", "BRG", "BRG"])
        'YES'
    """
    
    def check_horizontal_stripes():
        """Check if field has valid horizontal stripes."""
        if n % 3 != 0:
            return False
        
        stripe_height = n // 3
        colors = []
        
        # Extract color for each of the 3 stripes
        for stripe_idx in range(3):
            start_row = stripe_idx * stripe_height
            end_row = start_row + stripe_height
            
            # Get the color of the first cell in this stripe
            stripe_color = field[start_row][0]
            
            # Verify all cells in this stripe have the same color
            for row in range(start_row, end_row):
                for col in range(m):
                    if field[row][col] != stripe_color:
                        return False
            
            colors.append(stripe_color)
        
        # Check all three colors are different and are R, G, B
        return len(set(colors)) == 3 and set(colors) == {'R', 'G', 'B'}
    
    def check_vertical_stripes():
        """Check if field has valid vertical stripes."""
        if m % 3 != 0:
            return False
        
        stripe_width = m // 3
        colors = []
        
        # Extract color for each of the 3 stripes
        for stripe_idx in range(3):
            start_col = stripe_idx * stripe_width
            end_col = start_col + stripe_width
            
            # Get the color of the first cell in this stripe
            stripe_color = field[0][start_col]
            
            # Verify all cells in this stripe have the same color
            for row in range(n):
                for col in range(start_col, end_col):
                    if field[row][col] != stripe_color:
                        return False
            
            colors.append(stripe_color)
        
        # Check all three colors are different and are R, G, B
        return len(set(colors)) == 3 and set(colors) == {'R', 'G', 'B'}
    
    # Try horizontal stripes first, then vertical
    if check_horizontal_stripes() or check_vertical_stripes():
        return "YES"
    else:
        return "NO"