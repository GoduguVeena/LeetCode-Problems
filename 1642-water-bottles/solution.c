int numWaterBottles(int numBottles, int numExchange) {
    int res=0;
    int empty=0;
    while(numBottles){
        res+=numBottles;
        empty+=numBottles;
        numBottles=empty/numExchange;
        empty=empty%numExchange;
    }
    return res;
}
