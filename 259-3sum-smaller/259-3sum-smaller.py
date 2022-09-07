class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        count = 0
        nums.sort()
        
        for i in range(len(nums)-2):
            
            s=i+1
            e = len(nums)-1

            while s<e:

                if  nums[i] + nums[s] + nums[e] < target:
                    count+=e-s
                    s+=1
                else:
                    e-=1
        return count
        
        