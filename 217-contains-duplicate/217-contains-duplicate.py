class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        set_count = set()
        for elem in nums:
            if elem in set_count:
                return True
            set_count.add(elem)
        return False
