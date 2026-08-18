class Solution {
    public int climbStairs(int n) {
        if(n==1||n==2){
            return n;
        }
        int a1=1;
        int a2=2;
        int b=0;
        for(int i=2;i<n;i++){
            b=a1+a2;
            a1=a2;
            a2=b;
        }
        return a2;
    }
}
