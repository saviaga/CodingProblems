class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        curr_zeros = 0
        result = 0
        start = 0
        k=1

        for end in range(len(nums)):
            if nums[end]==0:
                k-=1
            while k<0:
                if nums[start]==0:
                    k+=1
                start+=1
            result = max(result,end-start+1)
        return result
            