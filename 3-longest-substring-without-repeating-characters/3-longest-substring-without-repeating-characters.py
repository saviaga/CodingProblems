class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #Input: s = "abcabcbb"
        #Output: 3
        
        #s = "bbbbb"
        #output: 1
        
        #s = "pwwkew"
        #output: 3
        
        #s=""
        #output = 0
        
        #Approach 1: 
        # check each character(i)to see if it has a repeated characterf in position (i+1)
        #if it doesn't then increasize len_so_far by one
        #otherwhise check if longest > largest
        
        #Time 0(n^2)
        #Space O(1)
        
        #Approach 2:
        #use dictionary
        
        #s = "pwwkew"
        #       ^
        #chars = {p:0,w:1}
        #longest = end-start
        #
        #output: 3
        #1. loop thought the string and check if character not in dictionary
        #2. if not in dictionary, add it with key->number value->index
        #3. otherwise caluclate longest and start = current index+1
        #3.
        
        #Time O(N)
        #Space O(m) size of set worst case is N in case string has distinct caracters
        
        
        #{p:0,w:1,}
        chars = set()
        longest=0
        start = 0
        for end in range(len(s)):
                
            if s[end] in chars:
                while s[end] in chars:
                        chars.remove(s[start])
                        start+=1
            chars.add(s[end])
            longest= max(longest,len(chars))
            
             
        return longest
                
                
                
            
        