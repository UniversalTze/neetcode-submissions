# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            print(head)
            return False
        slow = head # have a slow pointer while head 
        fast = head.next # start it one pointer ahead

        while slow and fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
    
        return False

        