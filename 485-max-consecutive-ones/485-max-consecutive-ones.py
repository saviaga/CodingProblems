class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
            max_count = 0
            count=0
            start = 0
            for end in range (0, len(nums)):
                if nums[end]==1: 
                    count+=1
                    
                   
                else:
                    max_count = max(max_count, count)
                    count=0
            return max(max_count, count)
        