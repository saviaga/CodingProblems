class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        
        del_ceros=1
        longest=0
        start = 0
        
        for end in range(len(nums)):
            if nums[end]==0:
                del_ceros-=1
            while del_ceros<0:
                if nums[start]==0:
                    del_ceros+=1
                start+=1
            longest = max(longest,end-start)
            
        return longest
                
        