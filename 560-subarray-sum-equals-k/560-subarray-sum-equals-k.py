class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count=0
        start = 0
        curr_sum = 0
        freq = {0:1}
        
        for elem in nums:
            curr_sum+=elem
            complement = curr_sum - k
            if complement in freq:
                count+=freq[complement]
            if curr_sum in freq:
                freq[curr_sum]+=1
            else:
                freq[curr_sum]=1
        return count
        
