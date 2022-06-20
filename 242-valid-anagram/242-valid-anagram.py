class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        s_dic = Counter(s)
        
        
        for elem in t:
            if elem in s_dic:
                s_dic[elem]-=1
            else:
                s_dic[elem]+=1
            if s_dic[elem] ==0:
                del s_dic[elem]
        
        if  len(s_dic.keys())>0:
            return False
        return True
        