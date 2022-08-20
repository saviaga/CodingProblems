class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
            max_count = 0
            start = 0
            for end in range (0, len(nums)):
                if nums[end]==1:                
                    max_count = max(max_count, end-start+1)
                   
                else:
                    start = end + 1
                   
            return max_count
        