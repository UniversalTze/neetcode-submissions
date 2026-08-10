# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = None
        front = None
        while head is not None: 
            if front is not None:
                # when front of LL has been set,
                # we can now worry about what comes after it
                if head.val == val:
                    temp.next = head.next
                
            if front is None and head.val != val:
                # for setting the front value
                front = head

            if head.val != val:
                temp = head
            head = head.next


        return front
        