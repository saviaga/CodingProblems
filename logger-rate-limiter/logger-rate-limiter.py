class Logger(object):

    def __init__(self):
        self.mapping={}
        

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        "message,next_time->timestamp+10"
        
        if message in self.mapping:
            if timestamp < self.mapping[message]:
                return False
            else:
                self.mapping[message] = timestamp+10
                return True
        else:
           
            self.mapping[message] = timestamp+10
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)