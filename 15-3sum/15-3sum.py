class Solution:
    #[-1,0,1,2,-1,-4]
    #[-1,-1,0,1,2]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        stack = []
        nums.sort()
        for i in range(len(nums)-2):
            #check two numbers that sum to the complement of nums
            #If the current value > zero, break from the loop. Remaining values cannot sum to zero.
            
            if i== 0 or nums[i]!=nums[i-1]:
                
                s=i+1
                e = len(nums)-1

                while s<e:
                        if nums[i] + nums[s] + nums[e] > 0:
                            e-=1
                        elif  nums[i] + nums[s] + nums[e] < 0:
                            s+=1
                        else:
                            stack.append([nums[i],nums[s],nums[e]])
                            s+=1
                            while nums[s]==nums[s-1] and s<e:
                                s+=1
                            
        return stack
