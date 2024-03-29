class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def combineHelper(curr,chosen):
           # print("chosen ",chosen,"nums ",curr)
            if len(chosen)==k:
                res.append(chosen[:])
                return
            for i in range(curr,n+1):
                #chose
                chosen.append(i)
                #explore
                combineHelper(i+1,chosen)
                #unchose
                chosen.pop()
        
        res = []
        combineHelper(1,[])
        return res