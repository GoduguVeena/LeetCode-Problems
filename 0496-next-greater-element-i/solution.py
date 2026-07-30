class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = []
        hm = {}
        
        # use stack and fill hashmap = nums2 
        # [1,3,4,2]
        for n in nums2:
            while s1 and n > s1[-1]:
                # fill the hashmap
                hm[s1.pop()] = n
            
            # This needs to be outside the while loop, but inside the for loop
            s1.append(n)
        
        # result is in hashmap = collect it and put in res 
        # check in hashmap
        # [4,1,2]  
        
        res = [0] * len(nums1) # Initialize the result array to avoid NameError
        idx = 0
        
        for k in nums1:
            if hm.get(k):
                res[idx] = hm.get(k)
            else:
                res[idx] = -1
            idx += 1
        
        return res
