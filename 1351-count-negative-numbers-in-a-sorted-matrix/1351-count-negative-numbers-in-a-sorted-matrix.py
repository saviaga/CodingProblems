class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def search_negative(row):
            start = 0
            end = len(row)
            
            while start<end:
                mid = start + (end-start)//2
                if row[mid] <0:
                    end = mid
                else:
                    start = mid+1
                
            return len(row)- start
        
        count = 0
        for row in grid:
            count +=search_negative(row)
        return count
    
    
        #Time complexity O(n+m)
        #Space complexity O(1)
    