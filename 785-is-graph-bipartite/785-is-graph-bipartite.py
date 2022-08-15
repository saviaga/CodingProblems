class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        N= len(graph)
        col = [-1]*N
        
        for i in range(N):
            if col[i]!=-1:
                continue
            q = deque()
            q.append((i,0))

            #bfs
            while q:
                    node,color = q.popleft()
                    if col[node] == -1:
                        col[node] = color
                        for ch in graph[node]:
                            q.append((ch,color^1))
                    if col[node]!=color:
                        return False
        return True
            
        