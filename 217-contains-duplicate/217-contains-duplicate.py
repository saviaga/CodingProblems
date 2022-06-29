class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dict_count = {}
        for elem in nums:
            if elem not in dict_count:
                dict_count[elem] = 1
            else:
                return True
        