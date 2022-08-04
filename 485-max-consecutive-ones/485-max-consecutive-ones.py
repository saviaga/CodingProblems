class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            #Sliding window
            max_count = 0
            start = 0
            count = 0
            for end in range (0, len(nums)):
                if nums[end]==1:                
                    max_count = max(max_count, end-start+1)
                    end = start + 1
                else:
                    start = end + 1
            return max_count
