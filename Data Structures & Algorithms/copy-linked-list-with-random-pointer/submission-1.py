"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # don't lose reference as the head of the list just yet. 
        loop1 = loop2 = head
        # use a look ahead set. if a pointer has been set to random, then remove it from the set
        # not everything needs to have a pointer to it tho.
        nodesMap = {}
        # if node has not been created, then store it in a set, after creating it
        # it can be removed
        res = nextorder1 = nextorder2 = Node(0)

        while loop1 is not None:
            if loop1 not in nodesMap:
                node = Node(loop1.val)
                nextorder1.next = node
                nodesMap[loop1] = node
            # nodes next can be created 
            else: 
                nextorder1.next = nodesMap[loop1]

            random = loop1.random

            if random:
                if random in nodesMap:
                    nextorder1.next.random = nodesMap[loop1.random]
                else:
                    node = Node(random.val)
                    nextorder1.next.random = node
                    nodesMap[random] = node
            
            loop1 = loop1.next
            nextorder1 = nextorder1.next
        
        return res.next


        
        
        