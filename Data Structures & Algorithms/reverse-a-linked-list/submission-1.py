# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head 
        # head is the current node of start of list 
        # 1 -> 2 -> 3 -> None
        # prev is none while 1 is cur
        # first iteration None <- 1 (1 is now end of list) 

        # Thus from this need to store a reference to Next before is set 
        # prev is set to so this can occur
        # prev = 1 and cur = 2
        # None <- 1 <- 2 and so on until
        # None <- 1 <- 2 <- 3 whixh is equivalent to 3-> 2 -> 1 -> None

        while cur is not None: 
            temp = cur.next
            cur.next = prev # setting next to previous (reversing list action) 
            prev = cur   # current node now is now as prev
            cur = temp # the next node reference in the original order linked list
            # end of the sequence
            # current node holds reference to the next node, while previous was the 
            # one we just visited
            # current is set as prev as it is the previous node to current node, which needs 
            # to be set as next (logic to reverse the list)

        return prev

        