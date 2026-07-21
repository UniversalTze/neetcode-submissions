class Node:
    def __init__(self, key, val):
        self.value = val  # the mapped val
        self.key = key # only used for deleting
        self.nex = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # mapping holds the key -> Node (Node holds value)
        self.mapping = {}
        # need a way of accesing both sides of the doubly linked list
        # if you had just one pointer, you would lose the head, hence you
        # need a left and a right. Left is for removal, right is for insert.      
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.nex, self.right.prev = self.right, self.left

    def remove(self, node: Node):
        # removing node from doubly linked list
        prev, nxt = node.prev, node.nex
        prev.nex = nxt
        nxt.prev = prev
        

    def insert(self, node: Node):
        nxt = self.right
        prev = self.right.prev
        prev.nex = node
        nxt.prev = node
        node.nex = nxt
        node.prev = prev


    def get(self, key: int) -> int: 
        # rearranges our doubly linked list
        # ensures the key is the right tail of the linked list (most recent)
        # LHS is the least indexed element. (gets pushed out if something new is 
        # added and capacity overflows)
        if key not in self.mapping:
            return -1
        rearrange = self.mapping[key]
        self.remove(rearrange)
        self.insert(rearrange)
        return rearrange.value

    def put(self, key: int, value: int) -> None:
        if key in self.mapping:
            # need to be placed by a new node
            item = self.mapping[key]
            self.remove(item)
        new = Node(key, value)
        self.mapping[key] = new
        self.insert(new)

        while len(self.mapping) > self.cap:
            node = self.left.nex
            self.remove(node)
            del self.mapping[node.key]
        
        
        
            