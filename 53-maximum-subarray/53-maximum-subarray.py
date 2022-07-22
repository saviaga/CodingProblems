class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cs = nums[0]
        max_sum =  nums[0]
        for i in range(1,len(nums)):
            
            cs = max(cs+ nums[i],nums[i])
            max_sum = max(max_sum,cs)
        return max_sum
            
            
        