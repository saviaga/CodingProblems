class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        count = 0
        nums.sort()

        #[-2,0,1,3]
        #.   s.e.
        #.      
        #-2 + 0 + 3 = 1 < target-> trye both counter left and right
        #-2 + 1 + 3 = 2
        
        for i in range(len(nums)):
            
            s=i+1
            e = len(nums)-1

            while s<e:

                if  nums[i] + nums[s] + nums[e] < target:
                    count+=e-s
                    s+=1
                else:
                    e-=1
        return count
        
        