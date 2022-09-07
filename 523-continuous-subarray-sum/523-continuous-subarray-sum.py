class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        dic_rem = {0:-1}
        curr_sum = 0
        
        for end in range(len(nums)):
            curr_sum+=nums[end]
            
            remainder = curr_sum%k
            if remainder not in dic_rem:
                dic_rem[remainder]=end
            elif end - dic_rem[remainder] > 1:
                    return True 
            
        return False
                
            
        