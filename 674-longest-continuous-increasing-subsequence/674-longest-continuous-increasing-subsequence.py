class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        start = 0
        longest = 0
        
        for end in range(len(nums)):
            if end > 0 and nums[end] <= nums[end-1]:
                start = end
            longest = max(longest,end-start+1)
        return longest
        
        
        