# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        # cur is used to move through the list, so its going to be none.]
        # since we're reversing the list prev will hold the pointer to the start of the lost
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

            


        