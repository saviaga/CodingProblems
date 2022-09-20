class Solution(object):
    
    def permuteHelper(self,nums,chosen):
        if len(nums)==0:
            return self.res.append(chosen[:])
        else:
            
            for i in range(len(nums)):
                #chose
                ch = nums[i]
                chosen.append(ch)
                #explore
                nums.remove(ch) 
                self.permuteHelper(nums,chosen)
                
            #unchose
                nums.insert(i,ch)
                chosen.pop()
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.permuteHelper(nums,[])
        return self.res
        