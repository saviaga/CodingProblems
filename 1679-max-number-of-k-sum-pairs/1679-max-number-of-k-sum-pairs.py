class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        dic_nums = defaultdict(int)
        counter = 0
        
        for i in range(len(nums)):
            complement = k - nums[i] 
            if complement in dic_nums and dic_nums[complement]>0:
                counter+=1
                dic_nums[complement]-=1
            else:
                dic_nums[nums[i]]+=1
        
        return counter
        