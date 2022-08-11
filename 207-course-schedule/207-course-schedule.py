class Solution(object):
    def isCyclic(self, adj, visited,curr): #-1 cycle, 1 = visited, 
        
        if visited[curr] == 1: return False # if ith node is marked as visiting, then a cycle is found
        if visited[curr] == 2:  return True# if it is processed, then do not visit again

        visited[curr] = 1 # mark as visiting
        
        for j in adj[curr]: # visit all the neighbours
            if not self.isCyclic(adj, visited, j):
                return False
        
        visited[curr] = 2 # after visit all the neighbours, mark it as processed
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
        
#if node v has not been visited, then mark it as 0.
#if node v is being visited, then mark it as 1. If we find a vertex marked as 1 in DFS, then their is a ring.
#if node v has been visited, then mark it as 2. If a vertex was marked as 2, then no ring contains v or its successors.        