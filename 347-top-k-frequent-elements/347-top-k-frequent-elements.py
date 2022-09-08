class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occurrences = collections.Counter(nums)
        priorityq = []
        
        for key,value in occurrences.items():
            heapq.heappush(priorityq,(value,key))
            if len(priorityq)>k:
                    heapq.heappop(priorityq)
        return [elem[1] for elem in priorityq]
            