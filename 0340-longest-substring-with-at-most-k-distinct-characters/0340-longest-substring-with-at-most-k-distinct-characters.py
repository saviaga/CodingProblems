class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        
        #s = "eceba" k=2
        dict_ch = {e:1,
                   b:1
                    }
        longest = 3 
        """
        start = 0
        end = 0
        
        dict_ch = {}
        longestsub = 0
        
        while end < len(s):
            
            #the char needs to be counted
            if s[end] in dict_ch:
                dict_ch[s[end]]+=1
            else:
                dict_ch[s[end]] = 1
            #check if the number of keys > k:
            #if this is true then reduce the size of window
            while len(dict_ch)>k:
                dict_ch[s[start]]-=1
                if dict_ch[s[start]] == 0:
                    del dict_ch[s[start]]
                start+=1
            #check the current size, and check if it is larger
            longestsub = max(longestsub,end-start+1)
            
            end+=1
            
        return longestsub 
            
        
                
            
        