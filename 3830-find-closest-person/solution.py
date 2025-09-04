from functools import lru_cache
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        # put the two candidates in a list
        choices = [x, y]

        @lru_cache(None)
        def dp(i: int):
            # base case - nothing left to consider
            if i == len(choices):
                return (float('inf'), -1)

            # option 1 - skip this index
            best_dist, best_idx = dp(i + 1)

            # option 2 - take this index
            dist = abs(choices[i] - z)

            if dist < best_dist:
                return (dist, i)
            if dist == best_dist and best_idx != i:
                return (dist, -1) # tie
            return (best_dist, best_idx)

        dist, idx = dp(0)
        if idx == -1:
            return 0 # tie
        return 1 if idx == 0 else 2
