class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) != len(s1)+len(s2): return False
        
        T = [[False for x in range(len(s2)+1)] for y in range(len(s1)+1)]

        
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                l = i + j -1
                if i == 0 and j == 0:
                    T[i][j] = True
                
                elif i == 0:
                    T[i][j] = T[i][j-1] and (s3[l] == s2[j-1])
                         
                elif j == 0:
                    T[i][j] = T[i-1][j] and (s3[l] == s1[i-1])
                         
                else:
                
                    T[i][j] = T[i-1][j] and  (s3[l] == s1[i-1]) or  \
                              T[i][j-1] and (s3[l] == s2[j-1])               
                  
        return T[-1][-1]
                
        