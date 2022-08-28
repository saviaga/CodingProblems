class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right + 1) // 2
            if nums[mid] > nums[mid - 1]:
                left = mid
            else:
                right = mid - 1
        return left
            
        