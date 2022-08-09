class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        curr_zero = 0
        max_ones = 0
        start = 0
        end=0
        prev_s = 0
        prev_e = 0
        while end < len(nums): # while our window is in bounds
           
            if nums[end]== 0:  # add the right most element into our window
                curr_zero+=1
            while curr_zero==2:
                if nums[start] == 0:    
                    curr_zero-=1
                start+=1
            if prev_e-prev_s+1 > end-start+1:
                max_ones= prev_e-prev_s+1
            else:
                max_ones= end-start+1
                prev_e = end
                prev_s = start
            end+=1
        return max_ones