class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letters = {}
        for elem in magazine:
            if elem in letters.keys():
                letters[elem]+=1
            else:
                letters[elem]=1
        for elem in ransomNote:
            if elem not in letters.keys() or letters[elem]<=0:
                return False
            else:
                letters[elem]-=1
        return True
                