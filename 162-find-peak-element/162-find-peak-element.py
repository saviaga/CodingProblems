class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        for i in range(1,len(nums)):
            
            if nums[i-1]>nums[i]:
                return i-1
        return len(nums)-1
            
            
        