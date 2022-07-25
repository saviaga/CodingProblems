class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        start = 0
        longest = 1
        
        for end in range(1,len(nums)):
            if nums[end] > nums[end-1]:
                longest = max(longest,end-start+1)
            else:
                start = end
        return longest
            
        
        
        