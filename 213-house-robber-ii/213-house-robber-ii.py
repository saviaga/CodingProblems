class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def robhelper(subnums):
            
            
            rob1, rob2 = 0, 0
            for n in subnums:

                temp = max(n + rob1, rob2) #imagine we are in n position, we have two choices
                rob1 = rob2 #iterate n+1 we want to update rob1 to advance to rob2
                rob2 = temp #the choice we made in n
            return rob2

        if len(nums)==1:
            return nums[0]
        return max(robhelper(nums[1:]), robhelper(nums[:-1]))
    
    