class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_anagrams = defaultdict(list)
        
        for elem in strs:
            key = sorted(elem)
            dict_anagrams["".join(key)].append(elem)
    
        return dict_anagrams.values()
            
        
        