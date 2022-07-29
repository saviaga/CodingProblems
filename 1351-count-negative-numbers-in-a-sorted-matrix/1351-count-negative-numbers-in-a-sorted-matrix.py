class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        res = 0
        n = len(grid)
        
        for i in range(n):
            m = len(grid[0])
            for j in range(m):
                if grid[i][j] < 0:
                    res += m-j      # once we met the first negative, break the loop
                    break
        return res     