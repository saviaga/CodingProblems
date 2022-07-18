class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=0:
            return []
        
        res = [0]*len(nums)
        idx = len(nums)-1
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            if nums[start]**2 > nums[end]**2:
                res[idx]=nums[start]**2
                start+=1
            else:
                res[idx]=nums[end]**2
                end-=1
            idx -=1
        return res
            
        
        