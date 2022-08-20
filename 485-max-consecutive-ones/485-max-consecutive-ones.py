class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
            max_count = 0
            count=0
            start = 0
            for end in range (len(nums)):
                
                if nums[end]==1:
                    count+=1
                    
                else:
                    
                    count=0
                    start=end+1
                max_count=max(max_count,count)   
                
                
            return max_count
                
                
                
            