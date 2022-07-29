class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        neg_num = 0
        
        for row in range(len(grid)):
            for col in reversed(range(len(grid[0]))):
                if grid[row][col] < 0:
                    neg_num+=1
                    
        return neg_num
        