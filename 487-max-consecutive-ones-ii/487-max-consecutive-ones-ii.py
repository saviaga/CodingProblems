class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr_zero = 0
        max_ones = 0
        can_change = True
        start = 0
        for end in range(len(nums)):
           
            if nums[end]==0 and can_change:
                can_change = False
                curr_zero = end
            elif nums[end]==0 and not can_change:
                start = curr_zero+1
                curr_zero = end
            max_ones = max(max_ones,end-start+1)
        return max_ones