class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = longest_sub = 0
        indices = {}
        
        for i, num in enumerate(nums):
            prefix_sum += num
            
            # Check if all of the numbers seen so far sum to k.
            if prefix_sum == k:
                longest_sub = i + 1
                
            # If any subarray seen so far sums to k, then
            # update the length of the longest_subarray. 
            complement = prefix_sum - k
            if complement in indices:
                longest_sub = max(longest_sub, i - indices[complement])
                
            # Only add the current prefix_sum index pair to the 
            # map if the prefix_sum is not already in the map.
            if prefix_sum not in indices:
                indices[prefix_sum] = i
        
        return longest_sub        