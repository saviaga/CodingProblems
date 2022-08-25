class MovingAverage:

    def __init__(self, size: int):
        self.size =size
        self.queue= collections.deque([])
        self.window_sum = 0
        self.count = 0
        

    def next(self, val: int) -> float:
        self.count +=1 #count element added

        self.queue.append(val)
        if self.count > self.size:
            self.queue.popleft()
        

        return sum(self.queue)/min(self.size,self.count)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)