class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
    int[] res = new int[nums1.length]; 
    Stack<Integer> s1 = new Stack<>();
    HashMap<Integer, Integer> hm = new HashMap<>();
    //use stack and fill hashmap = nums2 
    //[1,3,4,2]
    for(int n:nums2){
        while(!s1.isEmpty() && n>s1.peek()){
            //fill the hashmap
            hm.put(s1.pop(),n);
        }    
        s1.push(n);
    }
    //result is in hashmap = collect it and put in res 
    //check in hashmap
    //[4,1,2]  
    int idx = 0;
    for(int k:nums1){
        if(hm.containsKey(k)) res[idx]=hm.get(k);
        else res[idx] = -1;
        idx++;
    }
    return res;
    }
}

