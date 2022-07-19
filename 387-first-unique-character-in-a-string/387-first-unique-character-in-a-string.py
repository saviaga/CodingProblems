class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dic_char = Counter(s)
        
        for i in range(len(s)):
            if dic_char[s[i]]==1:
                       return i
        return -1
        