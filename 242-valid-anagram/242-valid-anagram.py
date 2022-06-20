class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dic = Counter(s)
        t_dic = Counter(t)
        
        return s_dic == t_dic
        