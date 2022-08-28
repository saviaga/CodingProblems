class Solution:
    def search(self, nums: List[int], target: int) -> int:
               
        start = 0
        end=len(nums)-1
        
        while start<end:
            
            mid=(start+end)//2
            if nums[start] <= nums[mid]:  #if the middle is bigger than the num at the start
                if nums[start] <= target <= nums[mid]: #if the num is bigger than start and less than mid (its at the left)
                    end = mid 
                else:
                    start = mid+1
            else:
                if nums[end] >= target >= nums[mid]: # it is at the right
                    start = mid
                else:
                    end = mid - 1
        return end if nums[end]==target else -1        