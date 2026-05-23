# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # can't use head alone here as head is only a reference,
        # when it moves to the end of the list it becomes none.

        # thus will need a current pointer from the start and a pointer
        # that starts from the back and moves back up when being reversed
        if not head: # linked list is empty
            return None

        prev, cur = None, head
        # prev represents backside which will be reversed all the way back up
        # to the front (holds the reference to start of reversed linked list)
        while cur: # loops until cur is None
            temp = cur.next # store the next node to come
            cur.next = prev # store the next node to the previous. 
            # e.g [0, 1, 2], as 0 is first, next will point to none
            prev = cur
            cur = temp
            # prev then becomes current node 0 and cur becomes next
            # (1) which means 1 -> 0 -> None
            
            # cur is set to temp (which just holds the next in head)
        return prev
            
        