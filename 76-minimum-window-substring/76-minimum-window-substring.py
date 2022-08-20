class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        countT={}
        window={}
        start = 0
        res = [-1,-1]
        reslen = float('inf')
        
        
        #save freq of T
        for c in t:
            countT[c] = 1+ countT.get(c,0)
        have,need =0,len(countT)
        
        for end in range(len(s)):
            ch = s[end]
            
            if ch in countT:
                window[ch]=1+window.get(ch,0)
            
                if window[ch]==countT[ch]:
                    have+=1
            while have==need:
                window_size = end-start+1
                if window_size < reslen:
                    res=[start,end]
                    reslen = window_size
                if s[start] in countT:
                    window[s[start]]-=1
                if s[start] in countT and window[s[start]] < countT[s[start]]:
                    have-=1
                start+=1
    
        start,end = res
        
        return s[start:end+1] if reslen!=float('inf') else ""
                
                
                
            
            
            
            
        
        
        