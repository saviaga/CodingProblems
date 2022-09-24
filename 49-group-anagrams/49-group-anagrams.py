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
        result = []
        for k,value in dict_anagrams.items():
            result.append(value)
        return result
            
        
        