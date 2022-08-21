class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        
                
        def num_missing(i):
            return nums[i]-nums[0]-i
            
        start =0
        end =len(nums)-1
            
        while start<= end:
                mid = start+(end-start)//2
                if num_missing(mid)<k:
                    start = mid+1
                else:
                    end = mid-1
        
        return nums[start-1]+k - num_missing(start-1)
            
        