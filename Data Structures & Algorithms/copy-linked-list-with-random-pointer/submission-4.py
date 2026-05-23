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
        loop1 = head
        # use a look ahead set. if a pointer has been set to random, then remove it from the set
        # not everything needs to have a pointer to it tho.
        nodesMap = {}
        # use a map with with the node as head's node as the key as you loop through, as it's based on head's list
        """
        Hashing with built ins like strings, int, tuples are all value based. 
        If two objects have the same hashcodes after hashing, they must have equal value.
        In hashing, it uses __hash__ and __eq__ to generate a value. Using tuples, string and ints (built-ins)
        (immutable objects), python will just use the value to hash and check the equality of the hashes
        using. So if I have an Int object 3 and another int object 3, hash1 == hash2 as they are hashed on the same 
        value.  == (value based)

        If customed built objects, they are hashed using their id. So Node(1) and Node(1) will have different hashes as 
        they have different ids when they are created. These __hash__ and __eq__ methods are inherited from 
        from object by default. == (id based)
        """
        # cannot use value as multiple nodes share the same values,
        # but the object nodes are hashed differently. 
        # if node has not been created, then store it in a set, after creating it
        # it can be removed
        res = nextorder1 = Node(0)

        while loop1 is not None:
            if loop1 not in nodesMap:
                node = Node(loop1.val)
                nextorder1.next = node
                nodesMap[loop1] = node
            # nodes next can be created 
            else: 
                nextorder1.next = nodesMap[loop1]

            # Move the copied node pointer forward to the latest node added,
            # ensuring the `random` pointer is assigned to the correct node.
            # 1 iteration:
            # loop1 = 1 -> 2 -> 3, nextorder1 = 0 -> 1
            # second iteration (at this point in time):
            # loop1 = 1 (visited) -> 2 (current) -> 3, nextorder1 = 0 (visited) -> 1 (current) -> 2
            # Down below, set the random pointer for 1, so we need to move nextorder1 to synchronise
            # so that it can be set correctly. 
            nextorder1 = nextorder1.next
            random = loop1.random
            if random:
                if random in nodesMap:
                    nextorder1.random = nodesMap[loop1.random]
                else:
                    node = Node(random.val)
                    nextorder1.random = node
                    nodesMap[random] = node
            
            # move loop1 pointer forward
            loop1 = loop1.next
        
        return res.next


        
        
        