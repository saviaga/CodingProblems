class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(mat)==0 or r*c !=len(mat[0])*len(mat):
            return mat

        new_rows =0
        new_cols = 0
        
        new_elem = [[ 0 for y in range( c ) ]
                    for x in range( r )]

        
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                elem = mat[row][col]
                
                new_elem[new_rows][new_cols]=elem
                new_cols+=1
                if new_cols >= c:
                    new_rows +=1
                    new_cols = 0
                
                
        return new_elem