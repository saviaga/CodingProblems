class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = sum_max = nums[0]
        
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        
        for i in range(1,len(nums)):
            curr = max(nums[i],nums[i]+curr)
            sum_max = max(sum_max,curr)
        return sum_max
        