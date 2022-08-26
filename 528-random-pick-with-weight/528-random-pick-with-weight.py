class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum=[]
        self.cum_sum=0
        for elem in w:
            self.cum_sum+=elem
            self.prefix_sum.append(self.cum_sum)
      
    def pickIndex(self) -> int:
        target = random.randint(1,self.cum_sum)
        for i,value in enumerate(self.prefix_sum):
            if target <= value:
                return i
       
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()