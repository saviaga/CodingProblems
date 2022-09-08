class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ordered = []
        for elem in nums:
            heapq.heappush(ordered,elem)
            if len(ordered)>k:
                 heapq.heappop(ordered)

        return ordered[0]
                
        
        
        