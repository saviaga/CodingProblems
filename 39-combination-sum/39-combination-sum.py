class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        
        def combinationSum(remain_sum,chosen,curr_start):
            
            
            if remain_sum ==0:
               # make a deep copy of the current combination
                res.append(chosen[:])
                return
            elif remain_sum < 0:# exceed the sum, stop exploration.
                return 
               
            else:
                
                for i in range(curr_start,len(candidates)):
                #chose
                    elem = candidates[i]
                    chosen.append(elem)
                #explore
                    combinationSum(remain_sum- elem,chosen,i)
                #unchose
                    chosen.pop()
                    
        res = []
        combinationSum(target,[],0)
        return res
        