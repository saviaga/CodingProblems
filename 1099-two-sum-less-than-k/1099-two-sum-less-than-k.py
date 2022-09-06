class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        
        nums.sort()
        max_sum = 0
        i=0
        j=len(nums)-1
        
        while i < j :
            #if the sum is less than k, but bigger than max_sum: save
            if nums[i] + nums[j] >=k:
                j-=1
            
            elif nums[i] + nums[j] < k:
                if nums[i] + nums[j] > max_sum:
                    max_sum = nums[i] + nums[j]
                i+=1
            
        
        if max_sum!=0:
            return max_sum 
        else:
            return -1
    
                    

        
        
        