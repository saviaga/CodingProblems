class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dict_nums = {}
        res = []
        for elem in nums:
            if elem not in dict_nums:
                dict_nums[elem]=1
            else:
                dict_nums[elem]+=1
        for key,value in dict_nums.items():
           
            if value == 2:
                res.append(key)
                continue
        return res