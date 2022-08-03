class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        def robhelper(newnums):
            #print(newnums)
            m = [0]*len(nums)
        
       
            if len(nums)==1:
                return nums[0]
            m[0] = nums[0]
            m[1] = max(nums[0],nums[1])
            for i in range(2,len(nums)):

                m[i] = max((nums[i]+m[i-2]), m[i-1])
            return m[-1]
        
        
        
        return max(robhelper(nums[1:]), robhelper(nums[:-1]))
    
    
        
     