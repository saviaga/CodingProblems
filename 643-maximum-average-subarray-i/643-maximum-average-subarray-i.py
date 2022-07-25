class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_sum = cumsum = sum(nums[:k])
        for end in range(k,len(nums)):      
            cumsum+= (nums[end] - nums[end-k])
            max_sum = max(max_sum,cumsum)
        return max_sum/k
        
        
        