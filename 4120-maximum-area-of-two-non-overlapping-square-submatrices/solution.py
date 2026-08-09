class Solution:
    def maxArea(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        # Step 1: Compute maximum square side length ending at (r, c)
        dp = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1

        def can_fit_two(k: int) -> bool:
            # Collect top-left corners of all valid k x k squares
            squares = []
            for r in range(k - 1, m):
                for c in range(k - 1, n):
                    if dp[r][c] >= k:
                        squares.append((r - k + 1, c - k + 1))
            
            if len(squares) < 2:
                return False
            
            # Find overall min/max bounds of top-left corners
            min_r = min(r for r, c in squares)
            max_r = max(r for r, c in squares)
            min_c = min(c for r, c in squares)
            max_c = max(c for r, c in squares)
            
            # If two squares are separated globally along row or col axis
            if max_r - min_r >= k or max_c - min_c >= k:
                return True
            
            # Check mixed/diagonal separation in O(1) pass
            # For each square, check if a non-overlapping square exists to its top-left/top-right
            min_c_at_r = {}
            max_c_at_r = {}
            for r, c in squares:
                if r not in min_c_at_r:
                    min_c_at_r[r] = c
                    max_c_at_r[r] = c
                else:
                    min_c_at_r[r] = min(min_c_at_r[r], c)
                    max_c_at_r[r] = max(max_c_at_r[r], c)
            
            rows = sorted(min_c_at_r.keys())
            
            # Prefix minimum/maximum column coordinates for previous rows
            running_min_c = float('inf')
            running_max_c = float('-inf')
            
            p = 0
            for r in rows:
                # Update prefix bounds for rows that are at least k rows above current r
                while p < len(rows) and rows[p] <= r - k:
                    prev_r = rows[p]
                    running_min_c = min(running_min_c, min_c_at_r[prev_r])
                    running_max_c = max(running_max_c, max_c_at_r[prev_r])
                    p += 1
                
                # Check if current square at row r overlaps with any square at row <= r - k
                if running_min_c != float('inf'):
                    curr_max_c = max_c_at_r[r]
                    curr_min_c = min_c_at_r[r]
                    if abs(curr_max_c - running_min_c) >= k or abs(curr_min_c - running_max_c) >= k:
                        return True
                        
            return False

        # Step 2: Binary Search for maximum side length k
        low, high = 1, min(m, n)
        ans_k = 0
        
        while low <= high:
            mid = (low + high) // 2
            if can_fit_two(mid):
                ans_k = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return ans_k * ans_k
