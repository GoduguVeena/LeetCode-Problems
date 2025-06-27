class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        s = [ord(c) - ord('a') for c in s]
        count = Counter(s)
        allowed = sorted([c for c, v in count.items() if v >= k])
        s = tuple(c for c in s if c in allowed)
        n = len(s)
        max_len = n // k
        
        # Preprocess next positions for each character
        next_pos = []
        current_pos = [-1] * 26
        total_count = [0] * 26

        for i in range(n - 1, -1, -1):
            c = s[i]
            total_count[c] += 1
            next_pos.append(current_pos[:])
            current_pos[c] = i
        next_pos = next_pos[::-1]
        next_pos.append(current_pos[:])

        # Helper to check if a path is a valid subsequence repeated k times
        def is_valid(word):
            index = -1
            for _ in range(k):
                for c in word:
                    index = next_pos[index][c]
                    if index < 0:
                        return False
            return True

        result = []

        # Backtracking DFS to build candidate strings
        def dfs(path, path_count):
            nonlocal result
            if len(path) > max_len:
                return
            for c in reversed(allowed):  # Lexicographically largest first
                path.append(c)
                path_count[c] += 1
                if total_count[c] >= path_count[c] * k and is_valid(path):
                    if len(path) > len(result) or (len(path) == len(result) and path > result):
                        result = path[:]
                    dfs(path, path_count)
                path.pop()
                path_count[c] -= 1

        dfs([], [0] * 26)
        return "".join(chr(c + ord('a')) for c in result)
