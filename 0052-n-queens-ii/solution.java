class Solution {
    int count = 0;
    private boolean isSafe(int row, int col, 
                        char[][] cboard, int n){
        //horizontal check 
        for(int i=0; i<n; i++){
            if(cboard[row][i]=='Q'){
                return false;
            }
        }
        //vertical check 
        for(int j=0; j<n; j++){
            if(cboard[j][col]=='Q'){
                return false;
            }
        }
        int i, j;
        //left diagonal check 
        for(i=row, j=col; i>=0 && j>=0; i--, j--){
            if(cboard[i][j]=='Q'){
                return false;
            }
        }
        //right diagonal check 
        for(i=row, j=col; i>=0 && j<n; i--, j++){
            if(cboard[i][j]=='Q'){
                return false;
            }
        }
        return true;
    }
    private void backTracking(int row,int n,char[][] cboard){
        //store the correct combinations in the res 
        if(row==n){
            count++;
            return  ;
        }
        //placing the queens on the board 
        for(int col=0; col<n; col++ ){
            if(isSafe(row, col, cboard, n)){
                cboard[row][col]= 'Q';
                backTracking(row+1, n, cboard);
                cboard[row][col]='.';
            }
        }
    }
    public int totalNQueens(int n) {
        char[][] cboard = new char[n][n];
        for(char[] c: cboard){
            Arrays.fill(c, '.');
        }
        backTracking(0, n, cboard);
        return count;
    }
}

