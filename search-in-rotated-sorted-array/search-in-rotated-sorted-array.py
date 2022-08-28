class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left+right)//2
            print(mid)
            if nums[left]<= nums[mid]:
               
                if nums[left]<=target <= nums[mid]:
                    right = mid
                else:
                    left = mid+1            
            else:
               
                if nums[right]>=target >=nums[mid]:
                    left = mid
                
                else:
                    
                    right = mid -1
            
        return left if nums[left]==target else -1
                
        