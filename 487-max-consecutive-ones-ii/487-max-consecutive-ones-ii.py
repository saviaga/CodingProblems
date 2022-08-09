class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr_zero = 0
        max_ones = 0
        start= 0
        can_change = True
        
        for end in range(len(nums)):
            if nums[end]==1:
                max_ones = max(max_ones,end-start+1)
            elif can_change:
                can_change = False
                max_ones = max(max_ones,end-start+1)
                curr_zero = end
            else:
                start = curr_zero+1
                curr_zero = end
                max_ones = max(max_ones,end-start+1)
        return max_ones