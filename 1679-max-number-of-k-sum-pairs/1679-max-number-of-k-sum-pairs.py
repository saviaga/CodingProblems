class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        count=0
        nums.sort()
        
        s = 0
        e = len(nums)-1
        
        while s<e:
            if nums[s] + nums[e] <k:
                s+=1
            elif  nums[s] + nums[e] >k:
                e-=1
            else:
                count+=1
                s+=1
                e-=1
        
        return count
        