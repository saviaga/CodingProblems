class Solution(object):
    def isToeplitzMatrix(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for row in range(len(m) - 1):
            for col in range(len(m[0]) - 1):
                if m[row][col] != m[row + 1][col + 1]:
                    return False
        return True
                   
                  
                    
        