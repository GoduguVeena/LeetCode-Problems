int subtractProductAndSum(int n) {
    int Product=1;int Sum=0;
    while(n>0){
        int digit=n%10;
        Product=Product*digit;
        Sum=Sum+digit;
        n=n/10;
    }
    return Product-Sum;
}
