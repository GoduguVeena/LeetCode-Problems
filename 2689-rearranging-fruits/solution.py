class Solution:
    def minCost(self, a: List[int], b: List[int]) -> int:
        if any(v&1 for v in Counter(a+b).values()): return -1
        za,zb,mn = Counter(a),Counter(b),min(a+b)
        aa,bb = sorted((za-zb).elements()),sorted((zb-za).elements())
        return sum(min(v,u,2*mn) for v,u in zip(aa[::2],bb[::-2]))
