class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        def addDiagonal(start_row, start_col, end_row, end_col, inc):
            row, col = start_row, start_col
            
            while row!=end_row and col!= end_col:
               
                res.append(mat[row][col])
                row -= inc
                col += inc
              
            res.append(mat[row][col])
        
        rows, cols = len(mat), len(mat[0])
        res = []
        go_to_top_right = True
        right = left = top = bottom = 0
        
        while len(res) < rows * cols:
            if go_to_top_right: #go from bottom-left to top-right
                addDiagonal(bottom, left, top, right, 1)
            else: #go from top-right to bottom-left
                addDiagonal(top, right, bottom, left, -1)
            
            if right + 1 < cols: 
                right += 1
            else:
                top += 1
            if bottom + 1 < rows:
                bottom += 1
            else:
                left += 1
            
            go_to_top_right = not go_to_top_right
        
        return res
        