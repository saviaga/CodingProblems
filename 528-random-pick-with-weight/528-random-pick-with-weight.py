class Solution:

    def __init__(self, w: List[int]):
        
        self.prefix_sum = []
        self.total = 0
        for elem in w:
            self.total+=elem
            self.prefix_sum.append(self.total)
        print(self.prefix_sum)
        

    def pickIndex(self) -> int:
        choice = random.randint(1,self.total)
        start = 0
        end = len(self.prefix_sum)-1
        
        while start < end:
            mid = (start+end)//2
            if self.prefix_sum[mid] < choice:
                start = mid+1
            else:
                end = mid
        return start
               
            
                


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()