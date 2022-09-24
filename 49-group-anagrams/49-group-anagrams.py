class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_anagrams = defaultdict(list)
        
        for elem in strs:
            key = [0] * 26
            for ch in elem:
                key[ord(ch)-ord('a')]+=1
            dict_anagrams[tuple(key)].append(elem)
        
        return dict_anagrams.values()
            
        
        