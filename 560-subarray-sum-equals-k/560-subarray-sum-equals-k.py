class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count = 0
        prefix_sum = {0:1}
        cum_sum = 0
        
        for elem in nums:
            cum_sum+=elem
            complement = cum_sum - k
            if complement in prefix_sum:
                count+=prefix_sum[complement]
            if cum_sum in prefix_sum:
                prefix_sum[cum_sum]+=1
            else:
                prefix_sum[cum_sum]=1
        return count
        
        
