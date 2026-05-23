# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

    
        # idea is two pointers. Where distance is n nodes apart
        # when fast pointer is at the end, slow one is at the node before 
        # the node that needs to be removed. thats the idea of this algo
        count = 0 # used to keep track of when second pointer should be started 
        first = head
        while count < n: # move first n steps forward 
            first = first.next
            count += 1
        second = dummy = ListNode() # left starts here, where we insert a additional node
        # this is so we can be at the node that needs to be updated 
        second.next = head
        while first: # move through end of linked list
            first = first.next
            second = second.next
        # second is at the pointer before the node that needs to be replaced 
        toreplacewith = second.next.next
        second.next = toreplacewith
        return dummy.next




        