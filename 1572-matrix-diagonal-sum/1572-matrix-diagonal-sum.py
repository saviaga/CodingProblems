class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        total = 0
        j = len(mat[0])-1
        for i in range(len(mat)):
            #add first diag
            total+=mat[i][i]
            if i == j-i:
                continue
            total+=mat[i][j-i]
             
        return total
    
