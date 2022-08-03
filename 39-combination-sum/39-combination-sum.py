class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        
        def combineHelper(remain_sum,chosen,curr_start):
            
            if remain_sum==0:
                res.append(chosen[:])
                return
            elif remain_sum<0:
                return
            else:
                
                for i in range(curr_start,len(candidates)):
                    #chose
                    elem = candidates[i]
                    chosen.append(elem)

                    #explore
                    combineHelper(remain_sum-elem,chosen,i)
                    #unchose

                    chosen.pop()
        
        res = []
        combineHelper(target,[],0)
        return res        