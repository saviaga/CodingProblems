class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dic_nums = {}
        for i , value in enumerate(nums):
            if nums[i] in dic_nums and abs(i- dic_nums[nums[i]]) <=k:
                    return True
                
            dic_nums[value] = i
        return False
            