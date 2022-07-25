class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = 0
        max_sub = 0
        elements = {}
        
        for end in range(len(s)):
            char = s[end]
            if s[end] in elements:
                start = max(start,elements[char]+1)
            elements[char] = end
            max_sub = max(max_sub,end-start+1)
        return max_sub
        