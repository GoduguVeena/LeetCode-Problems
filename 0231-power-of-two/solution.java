class Solution {
    public boolean isPowerOfTwo(int n) {
        for(int i=0;i<=(int)(Math.log(n)/Math.log(2));i++){
            if(Math.pow(2,i)==n) return true;
        }
        return false;
    }
}
