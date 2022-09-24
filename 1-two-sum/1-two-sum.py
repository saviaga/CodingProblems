class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in seen:
                seen[nums[i]] = i
            else:
                return [i, seen[complement]]
        
        