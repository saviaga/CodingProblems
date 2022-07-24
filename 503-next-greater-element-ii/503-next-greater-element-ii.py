class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        stack = []
        
        for i in range(len(nums)*2-1,-1,-1):
            while stack and   nums[stack[-1]] <= nums[i%len(nums)] :
                stack.pop()
            
            
            if not stack:
                res[i%len(nums)] = -1
            else:
                res[i%len(nums)] = nums[stack[-1]]
            stack.append(i%len(nums))
        return res