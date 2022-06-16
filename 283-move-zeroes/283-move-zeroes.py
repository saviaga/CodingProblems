class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        idx0 = 0
        idxn = 0
        
        while idxn < len(nums):
            if nums[idx0]==0 and nums[idxn]!=0:
                nums[idx0], nums[idxn] = nums[idxn],nums[idx0]
                idx0+=1
                idxn+=1
            
            elif nums[idx0]==0 and nums[idxn]==0:
                idxn+=1
            else:
                idx0+=1
                idxn+=1
                
                
        return nums
            
            
        