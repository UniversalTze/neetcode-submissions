class Node:
    # extra data structure for this question
    def __init__(self, key, val):
        self.value = val  # the mapped val
        self.key = key # only used for deleting
        self.nex = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # its a doubly linked list
        # item being indexed the least is at the front
        self.front = Node(0,0)
        # end keeps track of all the most recent node
        self.end = Node(0,0)

        # point the relevant references to each other
        self.front.nex = self.end
        self.end.prev = self.front
        self.cache = {}
        
    # Functions for the doubly linked list DS
    def insert(self, node: Node):
        previous = self.end.prev
        # setting up new node with the end of the DLL
        node.nex = self.end
        self.end.prev = node

        # set up the link between former last element to point to new node and vice versa
        previous.nex = node
        node.prev = previous
        
    def remove(self, node: Node):
        prev, after = node.prev, node.nex
        prev.nex = after
        after.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # reorganise node in DLL to move to the far rigth the last indexed item
        self.remove(node)
        self.insert(node)
        return self.cache[key].value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            remove(self.cache[key])
        add = Node(key, value)
        self.cache[key] = add
        self.insert(add)
        
        while len(self.cache) > self.cap:
            node = self.front.nex
            self.remove(self.cache[node.key])
            del self.cache[node.key]

        
