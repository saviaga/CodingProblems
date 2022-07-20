class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = 0
        z = 0
        
        while n < len(nums):
            if nums[z] == 0 and nums[n] == 0:
                n+=1
            elif nums[z] == 0 and nums[n] !=0:
                nums[z],nums[n] = nums[n],nums[z]
                n+=1
                z+=1
            elif nums[z] !=0 and nums[n] !=0:
                n+=1
                z+=1
        return nums
        
        
        