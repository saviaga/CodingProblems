class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        max_ones = 0
        for end in range(len(nums)):
            if nums[end]==1:
                max_ones = max(max_ones,end-start+1)
                end+=1
            else:
                start = end+1
        return max_ones
                
                
                
                
            
        