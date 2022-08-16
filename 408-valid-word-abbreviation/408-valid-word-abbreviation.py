class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i=0
        j=0
        
        while i<len(abbr) and j<len(word):
            if abbr[i].isalpha():             
                if abbr[i]!=word[j]:
                    return False
                i+=1
                j+=1
            else:
                
                if abbr[i]=='0':
                    return False
                temp = ''
                
                while i<len(abbr) and abbr[i].isdigit():
                    temp+=abbr[i]
                
                    i+=1
                j+=int(temp)
        return i==len(abbr) and j==len(word)
                
                    
                
        