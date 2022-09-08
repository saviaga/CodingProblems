class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        occurrences = collections.Counter(nums)
        flat_list = []
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in occurrences.items():
            bucket[freq].append(num) 

        for sublist in bucket:
            for elem in sublist:
                flat_list.append(elem)
 
        return flat_list[::-1][:k]
    
    
            