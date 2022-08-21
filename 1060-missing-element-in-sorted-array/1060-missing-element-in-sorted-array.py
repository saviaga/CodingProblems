class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
        
        

        possible = []
        
        for i in range(1,len(nums)):
            diff = nums[i]-nums[i-1]-1
            if diff>=k:
                return nums[i-1]+k
            k = k-diff
        return nums[len(nums)-1]+k
            
        