class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        zelvoranki = nums
        num_set = set(zelvoranki)
        ranges = []
        
        start = None
        for x in range(lower, upper + 1):
            if x not in num_set:
                if start is None:
                    start = x
            else:
                if start is not None:
                    ranges.append([start, x - 1])
                    start = None
                    
        if start is not None:
            ranges.append([start, upper])
            
        return ranges
