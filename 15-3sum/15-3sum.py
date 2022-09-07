class Solution:
    #[-1,0,1,2,-1,-4]
    #[-1,-1,0,1,2]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        stack = []
        nums.sort()
        for i in range(len(nums)):
            #check two numbers that sum to the complement of nums
            #If the current value > zero, break from the loop. Remaining values cannot sum to zero.
            
            if i== 0 or nums[i]!=nums[i-1]:
                
                seen = set()
                j = i+1

                while j<len(nums):
                        complement = - nums[i] - nums[j]
                        if complement in seen:
                            stack.append([nums[i],nums[j],complement])
                            while j+1 < len(nums) and nums[j] == nums[j+1]:
                                j+=1
                        else:
                            seen.add(nums[j])
                        j+=1
                            
        return stack
        