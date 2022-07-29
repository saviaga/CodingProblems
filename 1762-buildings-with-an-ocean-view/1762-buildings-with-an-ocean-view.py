class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        

        right_max = 0
        res = deque()
        for i in range(len(heights)-1, -1, -1):
            if right_max < heights[i]:
                res.appendleft(i)
                right_max = heights[i]
        return res
            
                
        
                
                
            
            
        