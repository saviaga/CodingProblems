class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        #remove duplicates
        result =0
        no_dup = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                no_dup.append(nums[i])
     
        
        for i in range(1,len(no_dup)-1):
            #hill
            if no_dup[i]>no_dup[i-1] and no_dup[i]>no_dup[i+1]:
                result+=1
            #valley
            elif no_dup[i]<no_dup[i-1] and no_dup[i]<no_dup[i+1]:
                result+=1
        return result
        
     
       