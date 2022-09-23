class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        curr_sum = 0
        freq = {0:-1}
        for i in range(len(nums)):
            curr_sum+=nums[i]
            remainder = curr_sum%k
          
            if remainder not in freq:

                freq[remainder]=i
            elif i - freq[remainder]>1:
                return True
                
        return False
            
        