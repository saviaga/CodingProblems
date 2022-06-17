class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_n1 = set(nums1)
        set_n2 = set(nums2)
        
        return set_n1.intersection(set_n2)