class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
       
        counter = 0 
        start = 0
        prod = 1
        if k<=1: return 0
        for end in range(len(nums)):
                prod*=nums[end]
                while prod >= k:
                        prod/=nums[start]
                        start+=1
                
                
                counter+= (end - start +1)
        return counter   
        
                    