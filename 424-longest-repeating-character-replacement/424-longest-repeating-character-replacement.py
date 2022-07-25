class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start = 0
        count_freq = {}
        res = 0
        max_freq = 0
        for end in range(len(s)):
            char = s[end]
            #add char to frequencies
            count_freq[char] = 1+ count_freq.get(char,0)
            max_freq = max(max_freq,count_freq[char])
            #check the number of replacemets that we would have to do
            #if its not feasible shrink the window and eliminate that frequency
            if (end-start+1) - max_freq > k:
                count_freq[s[start]]-=1
                start+=1
                
            res = max(res,end-start+1)
        return res
        