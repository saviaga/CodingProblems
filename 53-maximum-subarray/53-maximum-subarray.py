class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_sum = nums[0]
        together = nums[0]
        
        for i in range(1,len(nums)):           
            together += nums[i]
            if together < nums[i]:
                together = nums[i]
            max_sum = max(max_sum,together)
                
        return max_sum
            
        