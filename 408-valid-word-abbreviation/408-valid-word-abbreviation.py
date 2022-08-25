class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        
        i=0
        j=0
        while i<len(abbr) and j<len(word):
            #if the chaacter is alphanumeric
            if abbr[i].isalpha():
                #if  chars at same position are different
                if abbr[i]!=word[j]:
                    return False
                #if they are equial continue comparing
                i+=1
                j+=1
            else:
                #if the char is a number
                #check if is a leading zero, if it is return False
                if abbr[i]=='0':
                    return False
                #if it is not a leading zero
                
                    #read the number
                temp=''
                while i<len(abbr) and abbr[i].isdigit():
                    temp+=abbr[i]
                    i+=1
                j+=int(temp)
        return i==len(abbr) and j==len(word)
            
                
        