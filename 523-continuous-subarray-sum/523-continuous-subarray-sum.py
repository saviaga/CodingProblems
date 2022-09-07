class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        dic_rem = {0:-1}
        curr_sum = 0
        
        for end in range(len(nums)):
            curr_sum+=nums[end]
            
            remainder = curr_sum%k
            if remainder in dic_rem:
                if end - dic_rem[remainder] > 1:
                    return True 
            else:
                dic_rem[remainder]=end
        return False
                
            
        