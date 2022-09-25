class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dic_nums = {} 
        for i in range(len(nums)):
            if nums[i] in dic_nums  and  abs(i - dic_nums[nums[i]])<=k:
                    return True
            else:
               
                dic_nums[nums[i]] = i
                     
        return False
            