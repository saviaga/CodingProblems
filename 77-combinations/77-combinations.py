class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        def combineHelper(first,chosen):
            
            if len(chosen) == k:
                res.append(chosen[:])
            
            else:
                for i in range(first, n+1):
                    #chose
                    chosen.append(i)
                    #explore
                    combineHelper(i+1,chosen)
                    #unchose
                    chosen.pop()
        res = []
        combineHelper(1,[])
        return res