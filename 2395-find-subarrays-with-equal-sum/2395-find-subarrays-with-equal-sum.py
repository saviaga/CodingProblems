class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        
        #[4,2,4]
        
        i=0
        j=1
        the_sums = {}
       
        while i<len(nums) and j<len(nums):
            this_sum =  nums[i]+nums[j]
            if this_sum in the_sums:
                return True
            else: 
                the_sums[this_sum]=1
            
            i+=1
            j+=1
            print(the_sums)
        return False
            
            
                
        
        