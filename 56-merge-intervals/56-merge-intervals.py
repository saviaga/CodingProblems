class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res =[]
        intervals.sort(reverse=True)

        while intervals:
            
            current = intervals.pop()
            
            start = current[0]
            end = current[1]
            
            if intervals and (intervals[-1][0]<= end):
                next_i = intervals.pop()
                intervals.append([start,max(end,next_i[1])])

            else:
                res.append(current)
        return res
                
                