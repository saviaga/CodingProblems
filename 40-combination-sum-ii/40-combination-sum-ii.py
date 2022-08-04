class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
       
        def combineHelper(remain_sum,chosen,curr_start):
            #print("remain",remain_sum,"curr",curr_start,"chosen",chosen,"remaining",candidates[curr_start:])
            if remain_sum==0:
                self.res.append(chosen[:])
                return
            elif remain_sum<0:
                return
            else:
                
                for i in range(curr_start,len(candidates)):
                    if i > curr_start and candidates[i] == candidates[i-1]:
                        continue
                        
                    #chose
                    elem = candidates[i]
                    chosen.append(elem)         
                    #explore
                    combineHelper(remain_sum-elem,chosen,i+1) #give this number another chance
                    #unchose

                    chosen.pop()
        

        
        self.res=[]
        combineHelper(target,[],0)
        return self.res
        