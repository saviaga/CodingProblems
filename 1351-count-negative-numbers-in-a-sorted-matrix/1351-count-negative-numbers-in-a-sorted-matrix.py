class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        res = 0

        col_s = len(grid[0])
        for row in range(len(grid)):
             
            for col in range(col_s):
                if grid[row][col] < 0:
                    res += col_s-col      # once we met the first negative, break the loop
                    break
        return res     