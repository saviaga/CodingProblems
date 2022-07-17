class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = 0
        max_s = 0
        elements = {}
        for end in range(len(s)):
            char_end  = s[end]
            if char_end in elements:
                start = max(start,elements[char_end]+1)
            elements[char_end] = end
            max_s = max(max_s,end-start+1)
        return max_s
        