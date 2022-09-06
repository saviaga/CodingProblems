class TwoSum:

    def __init__(self):
        self.stack = []

    def add(self, number: int) -> None:
        self.stack.append(number)
        

    def find(self, value: int) -> bool:
        i = 0

        dic_nums = {}
        for i in range(len(self.stack)):
            if value - self.stack[i] in dic_nums:
                return True
            else:
                dic_nums[self.stack[i]] = i
            
        return False
            
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)