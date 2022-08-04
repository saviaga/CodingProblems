class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def permuteHelper(nums,chosen):
            self.calls+=1
            if len(nums)==0:
               
                return res.append(chosen[:])
            else:
                #ABCD - > Choose A -> permute the rest of the elements BCD
                for i in range(len(nums)):  
                    
                    #choose
                    element = nums[i]
                    chosen.append(element) #Choose A
                    nums.remove(element)  # permute the rest of the elements BCD
                    #explore
                    permuteHelper(nums,chosen)
                    #unchose
                    nums.insert(i,element)  #unchosse c (send back to  string)
                    chosen.pop()
        
      
        res = []  
        self.calls = 0
        permuteHelper(nums,[])
        print(self.calls)
        return res
        
        #perm
                
           
            
                    
                   
                
                