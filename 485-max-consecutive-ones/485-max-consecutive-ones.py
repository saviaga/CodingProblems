class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        max_c_ones = 0
        
        for n in nums:
            if n == 1:
                count+=1
            else:
                
                max_c_ones=max(max_c_ones,count)
                count=0
        return max(max_c_ones,count)