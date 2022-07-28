class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        #remove duplicates
        result=0
        prev = nums[0]
        
        for i in range(1,len(nums)-1):
            
            if nums[i] == prev:
                prev = nums[i]
                continue
            
            if nums[i] > prev and nums[i] > nums[i+1]:
                    result+=1
                    prev = nums[i]
            elif nums[i] < prev and nums[i] < nums[i+1]:
                    result+=1
                    prev = nums[i]
            
            
        return result
                
                
            
        
     
       