class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 
        elif len(nums) == 1:
            return nums[0]
        
        
    
        rob_curr, prev = 0, 0
        for money in nums:
        
            temp = prev
            prev = max(rob_curr, prev)
            rob_curr = temp + money
        return max(rob_curr, prev)
   
    
    
        
     