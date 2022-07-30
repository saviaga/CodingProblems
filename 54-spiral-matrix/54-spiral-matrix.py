class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        left,right = 0, len(mat[0])
        top,bottom = 0, len(mat)
        
        
        while left < right and top <bottom:
            
            for i in range(left,right):#from left to right 
                res.append(mat[top][i]) #add elements in top row 
            top+=1
            
            for i in range(top,bottom): #from top to bottom
                res.append(mat[i][right-1]) #add elements in right col
            right-=1
            
            if not (left< right and top<bottom):
                break
            
            for i in reversed(range(left,right)):  #from right to left
                res.append(mat[bottom-1][i])       #add elements in the bottom row
            bottom-=1
            
            for i in reversed(range(top,bottom)):#from bottom to top
                res.append(mat[i][left])  #add elements in the left column
            left+=1
        return res
            
            