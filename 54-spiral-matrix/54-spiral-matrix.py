class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        top = 0
        left = 0
        bottom = len(mat)-1 
        right = len(mat[0])-1
        
        
        while (top <= bottom and left <= right):
            
            #left to right
            for i in range(left,right+1):
                res.append(mat[top][i])  #add top row 
            top += 1
            
            #top to bottom
            for i in range(top,bottom+1):
                res.append(mat[i][right]) # add right column
            right -= 1
            
            #left to right
            if (top <= bottom): #to avoid repeating left to right if only 1 col mat
                for i in range(right,left-1,-1):
                    res.append(mat[bottom][i]) #add bottom row 
                bottom -= 1
                
            #bottom to top   
            if (left <= right): #to avoid repeating bottom to top if only 1 row mat
                for i in range(bottom,top-1,-1):
                    res.append(mat[i][left]) #add bottom column
                left += 1
        return res
            
            
            
            