class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in temp:
                return [temp[complement],i]
            else:
                temp[nums[i]] = i 
                
        
                
            
        