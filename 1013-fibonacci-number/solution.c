int fib(int n){
        if(n<=1){
            return n;
        }
        int c=0;
        int p=1;
        int p1=0;
        for(int i=2;i<=n;i++){
            c=p+p1;
            p1=p;
            p=c;
        }
        return c;
}
