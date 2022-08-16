class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums=[]
        prefix_sum = 0
        for weight in w:
            prefix_sum+=weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum
       # print("ccc",self.prefix_sums)
    def pickIndex(self) -> int:
        target = random.random()*self.total_sum
        print(target)
        # run a linear search to find the target zone
        for i, prefix_sum in enumerate(self.prefix_sums):
            if target < prefix_sum:
                return i
                
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()