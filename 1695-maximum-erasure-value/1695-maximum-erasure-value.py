class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        max_score = 0
        elements_dic = {}
        cum_sum = 0
        for end in range(len(nums)):
            curr_num = nums[end]
            cum_sum+=curr_num
            if curr_num in elements_dic:
                elements_dic[curr_num] +=1
            else:
                elements_dic[curr_num] = 1
            while start < end and elements_dic[curr_num] >1:
                elements_dic[nums[start]]-=1
                cum_sum-=nums[start]
                start+=1
            
            max_score = max(max_score, cum_sum)
        return max_score
            
                         
        