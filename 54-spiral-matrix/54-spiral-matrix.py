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
            
            #right- > top to bottom 
            for row in range(top,bottom):
                res.append(mat[row][right-1]) # add right column
            right -= 1
            
            #bottom = > right to left
            #if the top < bottom then there at least 1 row from right to left to add
            if (top < bottom): #to avoid repeating right to left if only 1 col mat
                for col in reversed(range(left,right)):
                    res.append(mat[bottom-1][col]) #add bottom row 
                bottom -= 1
            
            #left -> bottom to top
            #if the left  < right there is at least one left columm to add 
            if (left < right): #to avoid repeating bottom to top if only 1 row mat
                for row in reversed(range(top,bottom)):
                    res.append(mat[row][left]) #add left column
                left += 1
        return res
            
            
            
            