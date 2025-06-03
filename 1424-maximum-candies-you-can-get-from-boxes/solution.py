class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        queue = deque()
        toOpen = set()
        res = 0
        for box in initialBoxes:
            if status[box]==0:
                toOpen.add(box)
            else:
                queue.append(box)
        while queue:
            box = queue.popleft()
            for contained in containedBoxes[box]:
                if status[contained]==0:
                    toOpen.add(contained)
                else:
                    queue.append(contained)
            for key in keys[box]:
                if key in toOpen:
                    queue.append(key)
                    toOpen.discard(key)
                status[key]=1
            res+=candies[box]
        return res                
