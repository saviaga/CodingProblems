class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        dic_count = {}
        for elem in nums:
            if elem in dic_count:
                return True
            else:
                dic_count[elem] = 1
