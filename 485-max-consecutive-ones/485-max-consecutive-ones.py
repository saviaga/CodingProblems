class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end = 0
        max_c_ones = 0
        while start < len(nums) and end< len(nums):
            #find first 1
            while start < len(nums) and nums[start] == 0:
                start+=1

            end = start
            #find the end of that window of 1s
            while end < len(nums) and nums[end] == 1:
                end+=1
            max_c_ones= max(max_c_ones,end-start)
            start=end
        return max_c_ones