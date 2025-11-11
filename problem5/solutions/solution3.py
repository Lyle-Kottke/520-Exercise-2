
def solve(n: int, a: int, b: int) -> int:
    """
    Calculates the maximum possible minimum number of cake pieces (x) per plate.

    The distribution must satisfy:
    1. All pieces (a+b) are used on n plates.
    2. Each plate has at least one piece.
    3. No plate contains pieces of both cakes.

    This is solved using binary search on the answer (x).
    """

    def is_possible(x: int, n: int, a: int, b: int) -> bool:
        """
        Checks if it's possible to distribute the cakes such that every plate has
        at least x pieces.
        
        For a minimum x pieces per plate, the maximum number of plates for cake 'a' is 
        floor(a/x), and for cake 'b' is floor(b/x).

        We need to find an integer k (plates for cake 'a') such that:
        1 <= k <= n-1 (must use at least one plate for each cake type)
        k <= floor(a/x)
        n-k <= floor(b/x)  => k >= n - floor(b/x)

        Thus, we need to find k such that:
        max(1, n - floor(b/x)) <= k <= min(n - 1, floor(a/x))

        A solution exists if the lower bound is less than or equal to the upper bound.
        """
        if x == 0:
            return False
            
        # Max plates for cake a such that each has at least x pieces
        max_plates_a = a // x
        
        # Max plates for cake b such that each has at least x pieces
        max_plates_b = b // x

        # Lower bound for k (plates for cake a): k >= n - max_plates_b
        lower_bound_k = n - max_plates_b
        
        # Upper bound for k (plates for cake a): k <= max_plates_a
        upper_bound_k = max_plates_a

        # The range of k must also be within [1, n-1] for both cakes to be distributed
        # (Since a, b >= 1, we must have at least one plate for each).
        lower_k = max(1, lower_bound_k)
        upper_k = min(n - 1, upper_bound_k)

        # A valid split k exists if the lower bound is less than or equal to the upper bound.
        return lower_k <= upper_k

    # Binary search range for x.
    # Lower bound is 1.
    # Upper bound is a safe maximum, max(a, b) + 2 is sufficient since a, b <= 100.
    low = 1
    high = max(a, b) + 2
    max_x = 0

    while low < high:
        mid = low + (high - low) // 2
        
        if is_possible(mid, n, a, b):
            # mid is possible, try for a larger x
            max_x = mid
            low = mid + 1
        else:
            # mid is too large, search the lower half
            high = mid

    return max_x