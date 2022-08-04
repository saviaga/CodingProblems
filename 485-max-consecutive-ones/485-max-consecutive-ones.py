class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            start=0
            end = 0
            max_c_ones = 0
            while end< len(nums):
           
                if nums[end] == 0:
                    start=end+1
                else:
                    max_c_ones= max(max_c_ones,(end-start)+1)
                end+=1
            
            return max_c_ones