class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        stack=[]
        intervals.sort()
        for elem in intervals:
            
            if stack:
                if stack[-1][1]>=elem[0]:
                    top=stack.pop()
                    new_beg = min(top[0],elem[0])
                    new_end = max(top[1],elem[1])
                    stack.append([new_beg,new_end])
                else:
                    stack.append(elem)
            else:
                stack.append(elem)
                
        return stack
        