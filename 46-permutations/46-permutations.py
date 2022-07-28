class Solution(object):
    def permuteHelper(self,nums,chosen):
            if len(nums)==0:
                
                return self.res.append(chosen[:])
            else:
                
                for i in range(len(nums)):  
                    
                    #choose
                    element = nums[i]
                    chosen.append(element)
                    nums.remove(element)
                    #explore
                    self.permuteHelper(nums,chosen)
                    #unchose
                    nums.insert(i,element)
                    chosen.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        self.res = []            
        self.permuteHelper(nums,[])
        return self.res
        
        
                
           
            
                    
                   
                
                