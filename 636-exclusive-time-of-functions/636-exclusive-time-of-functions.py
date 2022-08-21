class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        lastlogTime = 0
        ans = [0]*n
        stack = []
        
        for log in logs:
            #actions[0]->id, actions[1]=>start/end, actions[2]->logtime
            log_id,status,timestamp = log.split(':')
            log_id,timestamp = int(log_id),int(timestamp)

            if status=='start':
                
                if stack:
                    ans[stack[-1]]+=timestamp-lastlogTime
                    lastlogTime = timestamp
                stack.append(log_id)
            else:
                    timestamp=timestamp+1 #to count for ending timestap at end of the time    
                    ans[stack.pop()]+=timestamp-lastlogTime     
                    lastlogTime = timestamp
                    
            
        return ans
                    
                
                
                
            
           
            
             
        