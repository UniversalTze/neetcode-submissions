class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # what we are given is an edge list
        # If we were going to use the list to find all nodes associated with 
        # one node, that would take O(N * E) as for every node we need to traverse every edge

        # But we can get it in O(N + E), the key is to build an adjacency list instead
        # of an edge list. Doing this we can see which nodes can get to each other
        # using BFS/DFS and a visit set/array. 
        # n represents how many nodes in the graph
        adjacen = [[] for _ in range(n)]
        for edge in edges:
            # given that its an undirected graph, down below is done.
            adjacen[edge[0]].append(edge[1])
            adjacen[edge[1]].append(edge[0])

        visit = set()

        def dfs(node):
            # run dfs to all possible connected components 
            # to this vertex has been visited, then return
            for neighbour in adjacen[node]:
                if neighbour not in visit:
                    visit.add(neighbour)
                    dfs(neighbour)
        
        components = 0
        for vertex in range(n):
            # loop through all vertices
            if vertex not in visit:
                visit.add(vertex)
                dfs(vertex)
                # each time it enters it find all connected vertices 
                # and treats it as one component
                components += 1 
        
        return components
        