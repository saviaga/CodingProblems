class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        next_char = s[len(s)-1]
        result = hashmap[next_char]
        
        for i in range(len(s)-2,-1,-1):
            curr_char= s[i]
            next_char = s[i+1]
            if hashmap[curr_char] >= hashmap[next_char]:
                result+=hashmap[curr_char]
            else:
                result-=hashmap[curr_char]
        return result
                