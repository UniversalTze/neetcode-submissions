# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head # start them at the same head position
        fast = head # start at same head position
        # starting slow and fast at head gives you second medium index
        # e.g [1,2,3,4] -> slow will end at 3 when using slow = fast in beginning
        # if head is empty, it won't enter loop

        # fast.next ensure theres are nodes next to it.
        while fast and fast.next: # if fast.next is not true, we know we've reached the end of list and index hasn't taken us back
            # cycles mean that we get taken back to a certain index at .next (that's why the check is there)
            slow = slow.next
            fast = fast.next.next # can be none, just can't use .val or .next. 
            # that's why check fast. 
            if slow == fast:
                return True
    
        return False

        