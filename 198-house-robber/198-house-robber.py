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
        
        
    
        rob_curr, not_rob_curr = 0, 0
        for num in nums:
            rob_curr, not_rob_curr = not_rob_curr + num, max(rob_curr, not_rob_curr)
            
        return max(rob_curr, not_rob_curr)
   
    
    
        
     