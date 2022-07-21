class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        res = []
        for elem in nums:
            
            freq[elem] = freq.get(elem,0)+1  #time = O(N)  Space = 0(N)
        
        myheap = []
        for i,value in freq.items():
            heapq.heappush(myheap,(-1*value,i)) #(nlogn) #time O(NlogK) i keep heap of size K , here i keep of size N so O(Nlogn) Space O(k) or O(N)
                    
            
        print(myheap)  #KlogK if k elements in heap here KlogN soace O(1)
        for _ in range(k):
            freq,num = heapq.heappop(myheap)
            res.append(num)
        return res
        
        
            
        