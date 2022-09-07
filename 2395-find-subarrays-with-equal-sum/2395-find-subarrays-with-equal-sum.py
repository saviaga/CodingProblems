class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        sums = {}
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] in  sums:
                    return True
            else:
                sums[nums[i] + nums[i+1]]=1
        return False
        