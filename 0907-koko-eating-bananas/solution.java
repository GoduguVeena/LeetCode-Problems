class Solution {
    private boolean kokoCanEat(int[] piles , int k,int h){
        int hours=0;
        for(int p :piles){
            hours+= (p+k-1)/k;
            if(hours>h)return false;
        }
        return hours<=h;
    }
    public int minEatingSpeed(int[] piles, int h) {
        int low_k=1;
        int high_k=-1;
        for(int n:piles){
            high_k=Math.max(high_k,n);
        }
        // int final_k=0;
        while(low_k<high_k){
            int mid=(low_k+high_k)/2;
            if(kokoCanEat(piles,mid,h)){
                high_k=mid;
            }
            else {
                low_k=mid+1;
            }
        }
    return  low_k;
    }
}
