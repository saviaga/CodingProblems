class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = 0
        nums.sort()
        
        max_prod = max(nums[0]*nums[1]*nums[len(nums)-1],nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3] ) 
        return max_prod
            
        