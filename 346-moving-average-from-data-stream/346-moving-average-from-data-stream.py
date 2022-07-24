class MovingAverage:

    def __init__(self, size: int):
        self.size =size
        self.queue= []
        

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)
        window_size= sum(queue[-size:])

        return window_size/min(len(queue),size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)