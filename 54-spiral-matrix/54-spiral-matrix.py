class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        top = 0
        left = 0
        bottom = len(mat)
        right = len(mat[0])
        
        
        while (top < bottom and left < right):
            
            #left to right
            for col in range(left,right):
                res.append(mat[top][col])  #add top row 
            top += 1
            
            #top to bottom
            for row in range(top,bottom):
                res.append(mat[row][right-1]) # add right column
            right -= 1
            
            #right to left
            if (top < bottom): #to avoid repeating right to left if only 1 col mat
                for col in reversed(range(left,right)):
                    res.append(mat[bottom-1][col]) #add bottom row 
                bottom -= 1
                
            #bottom to top   
            if (left < right): #to avoid repeating bottom to top if only 1 row mat
                for row in reversed(range(top,bottom)):
                    res.append(mat[row][left]) #add bottom column
                left += 1
        return res
            
            
            
            