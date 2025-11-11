def check_horizontal(n: int, m: int, grid: list[str]) -> bool:
    """Checks if the grid is a valid Berland flag with three equal horizontal stripes."""
    
    # 1. Divisibility Check
    if n % 3 != 0:
        return False
    
    h = n // 3
    
    # Define the row boundaries for the three stripes
    stripes_rows = [
        (0, h),          # Stripe 1 (Top): rows 0 to h-1
        (h, 2 * h),      # Stripe 2 (Middle): rows h to 2h-1
        (2 * h, n)       # Stripe 3 (Bottom): rows 2h to n-1
    ]
    
    colors = []
    
    # 2. Color Verification for Each Stripe
    for start_r, end_r in stripes_rows:
        # Get the expected color from the first cell of the stripe
        expected_color = grid[start_r][0]
        colors.append(expected_color)
        
        # Check all cells in the stripe
        for r in range(start_r, end_r):
            for c in range(m):
                if grid[r][c] != expected_color:
                    return False  # Stripe is not uniform
    
    # 3. Distinct Color Check
    # Must have exactly 3 distinct colors (R, G, B)
    if len(set(colors)) != 3:
        return False
        
    # 4. Success
    return True


def check_vertical(n: int, m: int, grid: list[str]) -> bool:
    """Checks if the grid is a valid Berland flag with three equal vertical stripes."""
    
    # 1. Divisibility Check
    if m % 3 != 0:
        return False
    
    w = m // 3
    
    # Define the column boundaries for the three stripes
    stripes_cols = [
        (0, w),          # Stripe 1 (Left): cols 0 to w-1
        (w, 2 * w),      # Stripe 2 (Middle): cols w to 2w-1
        (2 * w, m)       # Stripe 3 (Right): cols 2w to m-1
    ]
    
    colors = []
    
    # 2. Color Verification for Each Stripe
    for start_c, end_c in stripes_cols:
        # Get the expected color from the first cell of the stripe
        # Use row 0 for consistency
        expected_color = grid[0][start_c]
        colors.append(expected_color)
        
        # Check all cells in the stripe
        for c in range(start_c, end_c):
            for r in range(n):
                if grid[r][c] != expected_color:
                    return False  # Stripe is not uniform
    
    # 3. Distinct Color Check
    # Must have exactly 3 distinct colors (R, G, B)
    if len(set(colors)) != 3:
        return False
        
    # 4. Success
    return True


def solve(n: int, m: int, grid: list[str]) -> str:
    """
    Determines if the n x m grid is a correct Berland flag.
    
    A Berland flag must have three equal, parallel, single-colored, and
    distinctly colored stripes (R, G, B).
    """
    
    # The flag is valid if it passes either the horizontal or the vertical check.
    is_valid = check_horizontal(n, m, grid) or check_vertical(n, m, grid)
    
    return "YES" if is_valid else "NO"