class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        start = 0
        curr_prod = 1
        if k<=1: return 0
        for end in range(len(nums)):
            curr_prod *= nums[end]
            while curr_prod >=k:
                curr_prod/=nums[start]
                start+=1
            count+= end-start+1
        return count
        