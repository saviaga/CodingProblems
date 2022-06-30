class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        res = [0]*size
        for i in range(size):
            res[(i + k)% size] = nums[i]
        
        nums[:] = res
        
    
    #time complexity O(n)
    #space complecity O(n)