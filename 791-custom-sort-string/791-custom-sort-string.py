class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        dic_count = collections.Counter(s)
        res = []
        
            
       
        for ch in order:
            if ch in dic_count:
                res.append(ch * dic_count[ch])
                dic_count[ch]-=dic_count[ch]
        
        for key in dic_count:
            res.append(key *dic_count[key])
    
        return "".join(res)
            
            