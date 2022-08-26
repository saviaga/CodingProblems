class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        
        lastlogTime = 0
        ans=[0]*n
        stack=[]
        
        for log in logs:
            log_id,action,timestamp = log.split(':')
            log_id = int(log_id)
            timestamp=int(timestamp)
            
            if action=='start':
                if stack:
                    ans[stack[-1]]+=timestamp-lastlogTime
                lastlogTime = timestamp
                stack.append(log_id)
            else:
                timestamp=timestamp+1
                ans[stack.pop()]+=timestamp-lastlogTime
                lastlogTime=timestamp
        return ans
            
        
                
                
                
            
           
            
             
        