"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodesmap = {}
        # use a dfs/bfs to grow through neigbours
        # use a set to keep track of seen nodes
        # as there is no cycle in graph, if nodes has been seen we can break 
        # out of loop as all neighbours have been collected
        # empty neighbours
        queue = deque(node.neighbors)
        #nodesmap[node] = Node(node.val)
        if not node.neighbors:
            return Node(node.val)

        while queue:
            beside = []
            checknode = queue.popleft()
            if checknode not in nodesmap:
                newCop = Node(checknode.val)
                nodesmap[checknode] = newCop
            else:
                newCop = nodesmap[checknode]

            for neighbour in checknode.neighbors:
                if neighbour not in nodesmap:
                    cop = Node(neighbour.val)
                    nodesmap[neighbour] = cop
                    beside.append(cop)
                    queue.append(neighbour)
                else:
                    beside.append(nodesmap[neighbour])
            newCop.neighbors = beside
        return nodesmap[node]
