class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ordered = []
        for elem in nums:
            heapq.heappush(ordered,-1*elem) #min heap  #O(NlogN)
            
            
        for _ in range(k):
            num = -1*heapq.heappop(ordered)
        
        return num
            
        
        