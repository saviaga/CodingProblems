class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums=[]
        total = 0
        for weight in w:
            total+=weight
            self.prefix_sums.append(total)
        self.total = total
      
    def pickIndex(self) -> int:
        target = random.uniform(0,self.total)
        
        start= 0
        end = len(self.prefix_sums)-1
        while start < end: 
            mid = start + (end-start)//2
            if self.prefix_sums[mid] < target: 
                start = mid + 1
            else: 
                end = mid 

        return end
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()