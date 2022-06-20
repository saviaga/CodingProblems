class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        rasom_dic = Counter(ransomNote)
        magazine_dic = Counter(magazine)
        
        for ch in ransomNote:
            if ch in magazine_dic:
                magazine_dic[ch]-=1
                if magazine_dic[ch]==0:
                    del  magazine_dic[ch]
            else:
                return False
        return True
        