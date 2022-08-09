class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_so_far = nums[0]
        min_so_far = nums[0]       
        result = max_so_far
        
        for i in range(1,len(nums)):
            
            curr =nums[i]
            temp_max = max(curr,curr*max_so_far, curr*min_so_far)
            min_so_far = min(curr,curr*min_so_far, curr*max_so_far)
            
            max_so_far = temp_max
            result = max(result, temp_max)

       
        return result
        