class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        longest = 0
        dic_ind = {}
        for end in range(len(s)):
            char = s[end]
            
            if char in dic_ind:
                start = max(start,dic_ind[char]+1)
            dic_ind[char] = end
            
            longest = max(longest,end-start+1)
        return longest
        