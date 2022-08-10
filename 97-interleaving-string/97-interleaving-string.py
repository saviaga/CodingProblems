class Solution(object):
    def isInterleave(self, str1, str2, str3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(str3) != len(str1)+len(str2): return False
        
        T = [[False for x in range(len(str2)+1)] for y in range(len(str1)+1)]

        
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):
                l = i + j -1
                if i == 0 and j == 0:
                    T[i][j] = True
                
                elif i == 0:
                    T[i][j] = T[i][j-1] and (str3[l] == str2[j-1])
                         
                elif j == 0:
                    T[i][j] = T[i-1][j] and (str3[l] == str1[i-1])
                         
                else:
                
                    T[i][j] = T[i-1][j] and  (str3[l] == str1[i-1]) or  \
                              T[i][j-1] and (str3[l] == str2[j-1])               
                  
        return T[-1][-1]
                
        