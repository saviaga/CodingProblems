class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        
        dic_sum = {0:1}
        cum_sum = 0
        
        for elem in nums:
            cum_sum+=elem
            complement = cum_sum-k
            if complement in dic_sum:
                count+=dic_sum[complement]
            
            if cum_sum in dic_sum:
                dic_sum[cum_sum]+=1
            else:dic_sum[cum_sum]=1
        
           
        return count
    
                
            
                
                
            