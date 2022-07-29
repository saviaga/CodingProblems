class Solution(object):
    def findBuildings(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        max_height = heights[-1]
        
        i = len(heights)-1
        view = collections.deque([i])
        while i>0:
            
            if heights[i] < heights[i-1] and heights[i-1] > max_height:
                max_height = max(max_height,heights[i-1])
                view.appendleft(i-1)
            i-=1
        if heights[0]>max_height:
            view.appendleft(i-1)
        return view
            
                
        
                
                
            
            
        