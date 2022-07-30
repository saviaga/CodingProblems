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
            
            #from left to right 
            for i in range(left,right):
                res.append(mat[top][i])
            top+=1
            
            #from top to bottom
            for i in range(top,bottom):
                res.append(mat[i][right-1])
            right-=1
            
            if not (left< right and top<bottom):
                break
            
            #from right to left:
            for i in reversed(range(left,right)):
                res.append(mat[bottom-1][i])
            bottom-=1
            
            #from bottom to top:
            for i in reversed(range(top,bottom)):
                res.append(mat[i][left])
            left+=1
        return res
            
            