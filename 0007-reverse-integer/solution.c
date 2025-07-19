#include<math.h>
double reverse(int x){
  double  rev=0;
  while(x){
    if(rev>214748364||rev<-214748364)
    return 0;
    rev=rev*10+x%10;
    x=x/10;
  } return   rev;
}
