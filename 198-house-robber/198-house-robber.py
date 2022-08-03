class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        m = [0]*(len(nums)+1)
        
       
        if len(nums)==0:
            return 0
        m[0] = 0
        m[1] = nums[0]
        for i in range(1,len(nums)):
        
            m[i+1] = max((nums[i]+m[i-1]), m[i])
        return m[-1]
                              