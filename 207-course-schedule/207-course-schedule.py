class Solution(object):
    def isCyclic(self, adj, visited,curr): #-1 cycle, 1 = visited, 
        # if ith node is marked as being visited, then a cycle is found
        if visited[curr] == -1: return False
        if visited[curr] == 1:  return True# if it is done visted, then do not visit again

        visited[curr] = -1 # mark as being visited
        
        for j in adj[curr]: # visit all the neighbours
            if not self.isCyclic(adj, visited, j):
                return False
        
        visited[curr] = 1 # after visit all the neighbours, mark it as done visited
        return True
                
        
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in range(numCourses)]
        visited = [0]*numCourses
        
        for elem in prerequisites: #make adjacency matrix
            adj[elem[0]].append(elem[1])
        
        for i in range(numCourses): #   visit each node
                if not self.isCyclic(adj,visited,i):
                    return False
    
        return True
        
        