class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        #Aproach 1: Brute force
        #Two loops: first loop grabs element, second loop checks remaining elements that can form a pair
        #Time: O(n^2)
        #Space: O(1)
        
        #Approach 2: 
        #Store complements in dictionary
        #loop throuh the array and count the number of pairs
        #Time: 0(N)
        #Space O(N)
        
        dict_complements = collections.defaultdict(int)
        count = 0
        
        for elem in arr:
            compl = -elem%k
            if compl in dict_complements and dict_complements[compl]>=1:
                count+=1
                dict_complements[compl]-=1
            else:
                
                dict_complements[(elem%k)]+=1
        return count == len(arr) // 2
                
                
            
        