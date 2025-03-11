class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        arr=[0]*3
        cnt=0
        n=len(s)

        i=n-1
        j=n-1

        while i>=0 and j>=0:
            arr[ord(s[i])-ord('a')]+=1

            while arr[0]>0 and arr[1]>0 and arr[2]>0:
                cnt+=i+1
                arr[ord(s[j])-ord('a')]-=1
                j-=1
            
            i-=1
        

        return cnt
