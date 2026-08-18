class Solution {
    public int fib(int n) {
        // Handle base cases early to avoid out-of-bounds errors
        if (n <= 1) {
            return n;
        }
        
        // Array size must be n + 1 to include index n
        int[] tab = new int[n + 1]; 
        
        // Initial values
        tab[0] = 0;
        tab[1] = 1;
        
        // Iteration method
        for(int i = 2; i <= n; i++){
            tab[i] = tab[i - 1] + tab[i - 2];
        }
        
        return tab[n];
    }
}
