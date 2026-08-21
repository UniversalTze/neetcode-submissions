# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # since there is no prev, need to utilise fast and slow pointers
        slow = fast = head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is not None: 
                fast = fast.next
        
        # slow is now in the middle
        # need to reverse the list from the middle,
        # so that slow starts from the other end
        prev = None
        while slow is not None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # now prev is the reversed list from halfway
        while prev is not None:
            if prev.val != head.val:
                return False
            prev = prev.next
            head = head.next
            
        return True


        