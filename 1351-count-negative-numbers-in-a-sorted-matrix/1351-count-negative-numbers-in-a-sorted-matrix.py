class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        res = 0

        row = len(grid)-1
        col = 0
        count = 0
        while row>=0 and col< len(grid[0]):
            if grid[row][col] < 0:
                count +=len(grid[0])-col
                row -= 1  #if negative found move to the upper row
            else:
                col +=1  #if negative not found keep looking in next column
        return(count)
    
    