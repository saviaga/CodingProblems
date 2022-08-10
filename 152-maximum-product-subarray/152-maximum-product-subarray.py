class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sofar = nums[0]
        min_sofar = nums[0]
        result = max_sofar
        
        for i in range (1,len(nums)):
            temp = max(nums[i],nums[i]*min_sofar, nums[i]*max_sofar)
            min_sofar =  min(nums[i],nums[i]*min_sofar, nums[i]*max_sofar)
            max_sofar = temp
            
            result = max(result,max_sofar)
        return result
        