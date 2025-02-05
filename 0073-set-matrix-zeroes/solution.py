class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        r,c=len(matrix),len(matrix[0])
        rowstofill, colstofill = set(),set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rowstofill.add(i)
                    colstofill.add(j)
        for i in range(r):
            if i in rowstofill:
                for j in range(c):
                    matrix[i][j]=0
            else:
                for j in colstofill:
                    matrix[i][j]=0
                

        
