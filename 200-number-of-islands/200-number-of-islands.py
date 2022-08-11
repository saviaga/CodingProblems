class Solution(object):
    
    def mark_curr_island(self,mat,x,y,r,c):
        
        #boundary cases
        if x<0 or x>=r or y<0 or y>=c or mat[x][y]!='1':
            return
        mat[x][y]='2'
        self.mark_curr_island(mat,x-1,y,r,c)  #up
        self.mark_curr_island(mat,x+1,y,r,c)  #down
        self.mark_curr_island(mat,x,y-1,r,c)  #left
        self.mark_curr_island(mat,x,y+1,r,c)  #right
        
        
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == '1':
                    self.mark_curr_island(grid,i,j,rows,cols)
                    num_islands+=1
        return num_islands
                    
        