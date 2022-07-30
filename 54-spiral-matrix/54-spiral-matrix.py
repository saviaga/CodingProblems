class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        row_begin = 0
        col_begin = 0
        row_end = len(mat)-1 
        col_end = len(mat[0])-1
        
        
        while (row_begin <= row_end and col_begin <= col_end):
            
            #left to right
            for i in range(col_begin,col_end+1):
                res.append(mat[row_begin][i])  #add top row 
            row_begin += 1
            
            #top to bottom
            for i in range(row_begin,row_end+1):
                res.append(mat[i][col_end]) # add right column
            col_end -= 1
            
            #left to right
            if (row_begin <= row_end): #to avoid repeating left to right if only 1 col mat
                for i in range(col_end,col_begin-1,-1):
                    res.append(mat[row_end][i]) #add bottom row 
                row_end -= 1
                
            #bottom to top   
            if (col_begin <= col_end): #to avoid repeating bottom to top if only 1 row mat
                for i in range(row_end,row_begin-1,-1):
                    res.append(mat[i][col_begin]) #add bottom column
                col_begin += 1
        return res
            
            
            
            