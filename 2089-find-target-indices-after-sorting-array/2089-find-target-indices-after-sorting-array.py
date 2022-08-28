class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
     
        
        left = 0
        right = len(nums)-1
        idx = []
        
        while left < right:
            mid = (left+right)//2
            if nums[mid]>=target:
                right = mid
            else:
                left = mid + 1
        if nums[left]!=target:
            return []
        
        idx.append(left)
        print(nums)
        print(left)
        left = left+1
        while left<len(nums) and nums[left]==target:
            idx.append(left)
            left+=1
        return idx