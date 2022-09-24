class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        cum_sum = 0
        freq = {0:-1}
        for i  in range(len(nums)):
            cum_sum+=nums[i]
            remainder = cum_sum%k
            
            if remainder not in freq:
                freq[remainder] = i
            elif i-freq[remainder]>1:
                return True
        return False
  
        