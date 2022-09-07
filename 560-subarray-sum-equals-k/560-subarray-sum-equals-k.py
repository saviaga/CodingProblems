class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        
        curr_sum = 0
        counter = 0
        dic_nums = {0:1}
        for i in range(len(nums)):
            curr_sum+=nums[i]
            complement = curr_sum-k
            if complement in dic_nums:
                counter+=dic_nums[complement]
           
            if curr_sum in dic_nums:
                dic_nums[curr_sum]+=1
            else:
                dic_nums[curr_sum]=1
                
            
            
            
        return counter
            
        
        