class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occurrences = collections.Counter(nums)
        heap = []
        print(occurrences)
        
        for key,value in occurrences.items():
            
            heapq.heappush(heap,(value,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [elem[1] for elem in heap]
        