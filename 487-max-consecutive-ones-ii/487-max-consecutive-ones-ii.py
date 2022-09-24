class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        start = 0
        flip_idx = -1
        max_ones = 0
        for end in range(len(nums)):
            curr = nums[end]
            if curr !=1:
                
                start = flip_idx + 1
                flip_idx= end
                
            max_ones = max(max_ones,end-start+1)
        return max_ones
                