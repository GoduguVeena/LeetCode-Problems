class Solution {
    public int reverse(int x) {
  double rev=0;
    while(x!=0){
    if(rev>214748364||rev<-214748364)
    return 0;
    rev=rev*10+x%10;
    x=x/10;
  } return (int) rev;
}
    }

