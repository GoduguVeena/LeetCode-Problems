class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        l=[[1],[1,1],[1,2,1]]
        if rowIndex<len(l):
            return l[rowIndex]
        else:
            while len(l)<=rowIndex:
                p=l[-1]
                k=[]
                for i in range(len(p)-1):
                    k.append(p[i]+p[i+1])
                k.append(1)
                k.reverse()
                k.append(1)
                k.reverse()
                l.append(k)
            return l[rowIndex]
                
