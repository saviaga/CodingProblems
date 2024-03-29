class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def get_key(string):
            key = []
            
            for i in range(1,len(string)):
                key.append(str((ord(s[i])-ord(s[i-1]))%26)) #to count for ord(a)-ord(z)=-25%26=1
            key= ",".join(key)
            
            return key
                
     
        hashmap = collections.defaultdict(list)
        for s in strings:
            key = get_key(s)
            hashmap[key].append(s)
        return hashmap.values()
    
    #Time: O(N*K)
    #Space O(N*K)