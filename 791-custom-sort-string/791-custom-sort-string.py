class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        dic_s = collections.Counter(s)
        res = []
        for elem in order:
            if elem in dic_s:
                res.append(elem*dic_s[elem])
                dic_s[elem]-=dic_s[elem]
       
        for key,val in dic_s.items():
            
            res.append(key*val)
        return "".join(res)
        
         