class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        count=0
        curr_sum=0

        dic_remainder = {0:1}
        for i in range(len(nums)):
            curr_sum+=nums[i]
            remainder = curr_sum%k
            if remainder in dic_remainder:
                
                count+=dic_remainder[remainder]
                dic_remainder[remainder]+=1
                
            if remainder not in dic_remainder:                
                dic_remainder[remainder] = 1   

        return count
            
            
                