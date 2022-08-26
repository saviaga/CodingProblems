class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def get_key(string):
            key = tuple()
            key = tuple((ord(s[i])-ord(s[i-1]))%26  for i in range(1,len(string)))
            
            return key
                
     
        hashmap = collections.defaultdict(list)
        for s in strings:
            key = get_key(s)
            hashmap[key].append(s)
        return hashmap.values()