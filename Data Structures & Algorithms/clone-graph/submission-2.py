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

        # append intial node to queue (first node to be assigned neighbours)
        # and create a new clone of that node
        queue = deque([node])
        nodesmap[node] = Node(node.val)

        while queue:
            beside = []
            checknode = queue.popleft()
            curNode = nodesmap[checknode] # grab new node from map
            for neighbour in checknode.neighbors:
                if neighbour not in nodesmap:
                    # if node has not been seen, create a mapping of old copy node -> new copy node
                    cop = Node(neighbour.val)
                    nodesmap[neighbour] = cop
                    beside.append(cop)
                    queue.append(neighbour)
                else:
                    # if it exists in map, grab it and append it to neighbour array
                    beside.append(nodesmap[neighbour])
            # assign neighbour to current graph node. 
            curNode.neighbors = beside
        return nodesmap[node]
