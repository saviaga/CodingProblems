class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def subsetsHelper(nums,chosen):
            
            if len(nums)==0:
                res.append(chosen[:])
              
            else:    
               
                    #chose (i would handle one option, should i keep it or not?)
                    elem = nums.pop()
                    
                    
                    #explore keeping my option
                    chosen.append(elem)
                    subsetsHelper(nums,chosen)
                   
                    
                    #explore withought this option
                    chosen.pop()
                    subsetsHelper(nums,chosen)
        
                    #unchoose:
                    nums.append(elem)
        
        res = []
        subsetsHelper(nums,[])
        return res
        