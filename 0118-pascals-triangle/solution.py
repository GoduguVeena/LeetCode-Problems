class Solution:
    def generate(self, numRows):
        a=0
# take 3 conditions as base condition if numRows = 1,2,3
        l=[[1],[1,1],[1,2,1]]
        if numRows==1:
            return [l[0]]
        elif numRows==2:
            return [l[0],l[1]]
        else:
            a=4
            while a<=numRows:
                p=l[-1]
                k=[]
                for i in range(len(p)-1):
                    k.append(p[i]+p[i+1])
# appending 1 at the end, appending 1 at the start
                k.append(1)
                k.reverse()
                k.append(1)
                k.reverse()
                l.append(k)
                a+=1
            return l
