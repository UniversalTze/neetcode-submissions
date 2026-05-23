class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # a tree is a valid graph that has no cycles
        # when a cycle is encountered -> It is no longer a tree

        # edgelist -> Going through an edgelist would be o(N * N * E), where E is an 
        # edge

        # construct an adjacency list. 
        # we know that in the tree we will have nodes from 0 up to N.
        """
        adjaList = [[]] * n 
        # above the empty is created once and its refernce is multiplied by 5
        # so you will have a list of arrays pointing to same object

        * is a data operation — it works on an already-existing value
        When Python sees [x] * n, it interprets that as "give me a list containing x, n times". 
        The * operator is defined on lists to mean repetition — and repetition in this context means 
        "repeat the element", not "repeat the construction of the element". 
        By the time * gets involved, x is already a fully formed object sitting in memory. 
        All * can do is refer to it multiple times.
        """
        """
        When Python sees [x for _ in range(n)], it interprets that as "execute this expression 
        and collect the result, n times". The comprehension is a mini program — 
        it has a loop, and x is the expression that gets run on each iteration. 
        Python doesn't know ahead of time what x will be; 
        it has to evaluate it fresh each time.
        """
        adjaList = [[] for _ in range(n)] 
    
        # each index in list, just means how many nodes can be reached as we 
        # have an undirected graph
        for edge in edges:
            # given its undirected graph, each node in the edges should be 
            # appened to the corresponding index in the adjaceny list
            adjaList[edge[0]].append(edge[1])
            adjaList[edge[1]].append(edge[0])
        traversed = set()
        """
        print(adjaList)
        # now need to do a dfs starting with first node
        def dfs(curNode, visited):
            if curNode not in visited:
                traversed.add(curNode)
                neighbours = adjaList[curNode]
                for node in neighbours:
                    if node in traversed:
                        continue
                    dfs(node, visited)
                    visited.remove(node)
            else:
                return False
        
        for index in range(n):
            dfs(index, visited)

        return True
        """
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        def dfs(node, par):
            if node in visit:
                return False

            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True

        return dfs(0, -1) and len(visit) == n
        