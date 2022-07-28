class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def permuteHelper(nums,chosen):
            if len(nums)==0:
                print(chosen)
                return res.append(chosen[:])
            else:
                
                for i in range(len(nums)):  
                    
                    #choose
                    element = nums[i]
                    chosen.append(element)
                    nums.remove(element)
                    #explore
                    permuteHelper(nums,chosen)
                    #unchose
                    nums.insert(i,element)
                    chosen.pop()
        res = []            
        permuteHelper(nums,[])
        return res
        
        
                
           
            
                    
                   
                
                