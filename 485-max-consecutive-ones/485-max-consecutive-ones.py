class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            start=0
            end = 0
            max_c_ones = 0
            while end< len(nums) and start<len(nums):
           
                while start<len(nums) and  nums[start] == 0: #move start while there are 0
                    start+=1
                
                end=start
                #if it is not zero we can start countin 1s
                while end < len(nums) and  nums[end]==1:
                    end+=1
                
                max_c_ones= max(max_c_ones,end-start)
                start=end
            
            return max_c_ones