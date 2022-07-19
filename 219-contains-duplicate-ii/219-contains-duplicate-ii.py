class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dic_nums = {}
        for i in range(len(nums)):
            if nums[i] not in dic_nums:
                dic_nums[nums[i]] = i
            else:
                if  abs(i- dic_nums[nums[i]]) <=k:
                    return True
                else:
                    dic_nums[nums[i]] = i
        return False
            