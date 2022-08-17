class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        def get_key(s):
            key = tuple()
            for i in range(1,len(s)):
                key+=((ord(s[i])-ord(s[i-1]))%26,)
            return key
                
     
        hashmap = collections.defaultdict(list)
        for s in strings:
            key = get_key(s)
            hashmap[key].append(s)
        return list(hashmap.values())
