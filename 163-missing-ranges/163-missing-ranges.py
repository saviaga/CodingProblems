class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        prev = lower-1
        nums

        res = []
        for i in range(len(nums)+1):
            if i < len(nums):
                curr = nums[i]                
            else:
                curr = upper + 1          

            if prev+1 < curr-1:
                res.append(str(prev+1) + "->" + str(curr-1))
            elif prev+1 == curr-1:
                 res.append(str(prev+1))
            
            prev = curr
        
        return res
        
        


                
            
        