def solve(n, m, grid):
    """
    Validate if the given grid is a valid Berland flag.
    
    Args:
        n: number of rows
        m: number of columns
        grid: list of strings representing the flag
    
    Returns:
        "YES" if valid flag, "NO" otherwise
    """
    
    def get_region_color(row_start, row_end, col_start, col_end):
        """
        Check if a rectangular region has uniform color.
        Returns the color if uniform, None otherwise.
        """
        color = grid[row_start][col_start]
        for i in range(row_start, row_end):
            for j in range(col_start, col_end):
                if grid[i][j] != color:
                    return None
        return color
    
    def check_horizontal_stripes():
        """Check if grid forms valid horizontal stripes."""
        if n % 3 != 0:
            return False
        
        stripe_height = n // 3
        colors = []
        
        # Check each horizontal stripe
        for stripe_idx in range(3):
            row_start = stripe_idx * stripe_height
            row_end = row_start + stripe_height
            color = get_region_color(row_start, row_end, 0, m)
            
            if color is None:
                return False
            colors.append(color)
        
        # Verify all three colors are used and different
        return sorted(colors) == ['B', 'G', 'R']
    
    def check_vertical_stripes():
        """Check if grid forms valid vertical stripes."""
        if m % 3 != 0:
            return False
        
        stripe_width = m // 3
        colors = []
        
        # Check each vertical stripe
        for stripe_idx in range(3):
            col_start = stripe_idx * stripe_width
            col_end = col_start + stripe_width
            color = get_region_color(0, n, col_start, col_end)
            
            if color is None:
                return False
            colors.append(color)
        
        # Verify all three colors are used and different
        return sorted(colors) == ['B', 'G', 'R']
    
    # Check both horizontal and vertical configurations
    if check_horizontal_stripes() or check_vertical_stripes():
        return "YES"
    else:
        return "NO"