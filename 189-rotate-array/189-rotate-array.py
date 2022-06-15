class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        nums2 = [0]*len(nums)
        for i in range(len(nums)):
            nums2[(i+k)%len(nums)] = nums[i]
        
        
        for i in range(len(nums)):
            nums[i] = nums2[i]
        return nums            