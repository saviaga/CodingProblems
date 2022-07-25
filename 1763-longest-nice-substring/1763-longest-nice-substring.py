class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
      
        # Edge case
        if len(s) < 2:
            return ""
        
        nice = ""           # Store the longest nice substring
        unique = set(s)     # Store all unique letters
        
        for i in range(len(s)):
            
            if s[i].lower() in s and s[i].upper() in s:
                nice += s[i]
            else:
                leftPart = self.longestNiceSubstring(s[:i])
                rightPart = self.longestNiceSubstring(s[i+1:])
                
                return leftPart if len(leftPart) >= len(rightPart) else rightPart 
                
        return nice