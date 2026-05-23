class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # given n nodes (labelled 0 to n - 1)
        # Lets say 4 nodes, 0, 1, 2, 3 and edges are undirected. 
        # [0,1] [1,2], [2,3] would be all that is needed to indicate a cycle. 
        # anymore edges, a cycle would then be introduced. 
        # so if len(edges) > n - 1
        
        # [0,1] [1,2], [2,3], [3,1] edges = 4 for n = 4, would lead to a cycle

        # convert edgelist TC = O(N * E) to adjacency list O(N + E)
        if len(edges) > n - 1: # no need to check further
            return False

        adjList = [[] for _ in range(n)]

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        # adjacency list built -> as its an undirected graph, it will 
        # hold the edge from where it came from. 
        # e.g [0,1],[1,2] (we're assuming that 0 is root as starting from smallest)
        # adjlist: [[1], [0, 2], [1]]. index[0] = [1] (which is neighbours for node 0)

        visit = set() # this is for the DFS to keep track of the nodes we've seen
        # this visit is important too as an edge case could be that there are no cycles, 
        # but not all nodes were visited, indicating an invalid tree as not all n nodes
        # make up that tree (seperate trees)
        
        # during dfs tho, as the adjList holds the edge from where it came from, 
        # we want to keep track of the parent, as not doing this will make the program 
        # think that a cycle has been found
        def dfs(curNode, parent, visited):
            if curNode in visited:
                # already seen this node and its not a parent, so 
                # return False as a cycle has occured. 
                return False
            visited.add(curNode)
            neighbours = adjList[curNode]
            for node in neighbours:
                if node == parent:
                    continue
                cycle = dfs(node, curNode, visited)
                if not cycle:
                    return False
            return True
        # start with 0 node and -1 as its parent, as we assume 0 is root. 
        # also check if len(visit) == number of nodes as this means that all nodes 
        # have been traversed. 
        return dfs(0, -1, visit) and len(visit) == n
        