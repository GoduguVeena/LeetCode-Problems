class Solution:
    def findDiagonalOrder(self, g: List[List[int]]) -> List[int]:
        m,n,d = len(g),len(g[0]),defaultdict(list)
        for i,j in product(range(m),range(n)): d[i+j].append(g[i][j])
        return [v for k,b in d.items() for v in b[::k%2*2-1]]
