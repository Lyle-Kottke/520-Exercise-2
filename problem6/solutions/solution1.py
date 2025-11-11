import collections

def solve(n: int, m: int, grid: list[str]) -> str:
    """
    Checks if an n x m grid of 'R', 'G', 'B' represents a correct flag of Berland.

    The flag must consist of three equal-width and equal-height stripes, parallel 
    to the sides, with each of the three colors ('R', 'G', 'B') used exactly once.

    :param n: The number of rows (height of the grid).
    :param m: The number of columns (width of the grid).
    :param grid: A list of strings representing the grid.
    :return: "YES" if the grid is a valid flag, "NO" otherwise.
    
    Examples:
    >>> check_berland_flag(6, 5, ["RRRRR", "RRRRR", "BBBBB", "BBBBB", "GGGGG", "GGGGG"])
    'YES'
    >>> check_berland_flag(4, 3, ["BRG", "BRG", "BRG", "BRG"])
    'YES'
    >>> check_berland_flag(6, 7, ["RRRGGGG", "RRRGGGG", "RRRGGGG", "RRRBBBB", "RRRBBBB", "RRRBBBB"])
    'NO'
    >>> check_berland_flag(4, 4, ["RRRR", "RRRR", "BBBB", "GGGG"])
    'NO'
    """
    
    # Helper function to check if a sub-rectangle is monochromatic
    def is_monochromatic(r_start, r_end, c_start, c_end):
        """Checks if the sub-grid from [r_start, c_start] to [r_end-1, c_end-1] 
        is composed of a single color. Returns the color, or None if not monochromatic."""
        if r_start >= r_end or c_start >= c_end:
            return None # Should not happen with correct stripe definitions
        
        color = grid[r_start][c_start]
        for r in range(r_start, r_end):
            for c in range(c_start, c_end):
                if grid[r][c] != color:
                    return None
        return color

    # --- 1. Check for Horizontal Stripes ---
    if n % 3 == 0:
        h = n // 3
        
        # Define stripe boundaries
        stripes = [
            (0, h, 0, m),      # Stripe 1: Rows 0 to h-1
            (h, 2 * h, 0, m),  # Stripe 2: Rows h to 2h-1
            (2 * h, n, 0, m)   # Stripe 3: Rows 2h to n-1
        ]
        
        colors = []
        is_valid_horizontal = True
        for r_start, r_end, c_start, c_end in stripes:
            color = is_monochromatic(r_start, r_end, c_start, c_end)
            if color is None:
                is_valid_horizontal = False
                break
            colors.append(color)
            
        if is_valid_horizontal:
            # Check for distinct colors and that all three 'R', 'G', 'B' are present (implicitly)
            # Since the problem constraints only use R, G, B, checking for distinctness is enough.
            if len(set(colors)) == 3:
                return "YES"

    # --- 2. Check for Vertical Stripes ---
    if m % 3 == 0:
        w = m // 3
        
        # Define stripe boundaries
        stripes = [
            (0, n, 0, w),      # Stripe 1: Cols 0 to w-1
            (0, n, w, 2 * w),  # Stripe 2: Cols w to 2w-1
            (0, n, 2 * w, m)   # Stripe 3: Cols 2w to m-1
        ]
        
        colors = []
        is_valid_vertical = True
        for r_start, r_end, c_start, c_end in stripes:
            color = is_monochromatic(r_start, r_end, c_start, c_end)
            if color is None:
                is_valid_vertical = False
                break
            colors.append(color)
            
        if is_valid_vertical:
            # Check for distinct colors
            if len(set(colors)) == 3:
                return "YES"

    # --- 3. Final Output ---
    return "NO"