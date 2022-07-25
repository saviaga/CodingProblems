class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        if len(nums) < k: return 0
        nums.sort()
        cum_sum = sum(nums[:k])
        minimum_dif = abs(nums[k-1] -nums[0])
        for end in range(k,len(nums)):
            cum_sum+=(nums[end] - nums[end-k])
            minimum_dif = min(minimum_dif,abs(nums[end]-nums[end-k+1]))
        return minimum_dif
            
        