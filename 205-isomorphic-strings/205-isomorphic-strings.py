class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping_s_t = defaultdict(str)
        mapping_t_s = defaultdict(str)
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
                mapping_s_t[c1] = c2
                mapping_t_s[c2] = c1
            
            # Case 2: Ether mapping doesn't exist in one of the dictionaries or Mapping exists and
            # it doesn't match in either of the dictionaries or both            
            elif mapping_s_t[c1] != c2 or mapping_t_s[c2] != c1:
                return False
            
        return True        