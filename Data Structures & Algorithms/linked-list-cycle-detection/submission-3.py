# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head # start them at the same head position
        fast = head # start at same head position
        # if head is empty, it won't enter loop

        # fast.next ensure theres are nodes next to it.
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
    
        return False

        