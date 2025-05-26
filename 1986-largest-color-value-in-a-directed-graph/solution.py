class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        color_count = [[0] * 26 for _ in range(n)]

        # Build graph and indegree array
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # Initialize queue with nodes having indegree 0
        queue = deque(i for i in range(n) if indegree[i] == 0)
        processed = 0
        max_value = 0

        while queue:
            node = queue.popleft()
            processed += 1

            color_index = ord(colors[node]) - ord('a')
            color_count[node][color_index] += 1
            max_value = max(max_value, color_count[node][color_index])

            for neighbor in graph[node]:
                for c in range(26):
                    color_count[neighbor][c] = max(color_count[neighbor][c], color_count[node][c])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return max_value if processed == n else -1
