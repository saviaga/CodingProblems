class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permuteHelper(numbers, chosen):
            if len(numbers)==0:
                res.append(chosen[:])
                
            else:
                for i in range(len(nums)):
                    #chose
                    c = nums[i]
                    chosen.append(c)
                    del nums[i]
                    #explore
                    permuteHelper(numbers,chosen)
                    nums.insert(i,c)
                    #unchoose
                    chosen.pop()
        
        
        
        res = []
        permuteHelper(nums,[])
        return res