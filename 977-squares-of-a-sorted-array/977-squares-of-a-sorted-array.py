class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squares = [0] * len(nums)
        idxsq = len(nums)-1
        start = 0
        end = len(nums)-1
        
        while start <= end:

            if nums[start]**2 >= nums[end]**2:
                squares[idxsq] = nums[start]**2
                start+=1
            elif nums[start]**2 < nums[end]**2:
                squares[idxsq] = nums[end]**2                
                end-=1
            idxsq -=1    
        return squares
            
            
        
        