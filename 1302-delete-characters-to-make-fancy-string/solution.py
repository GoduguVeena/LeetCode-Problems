class Solution:
    def makeFancyString(self, s: str) -> str:
        result = s[0]
        count = 1
        lastChar = s[0]
        
        for i in range(1, len(s)):
            if s[i] == lastChar:
                count = count + 1
                if count == 3:
                    count = count - 1
                    continue
            else:
                count = 1
            
            result += s[i]
            lastChar = s[i]
        
        return result
