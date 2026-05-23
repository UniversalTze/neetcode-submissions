# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list 1 and list2 hold nodes the start of the list that points to other nodes. 
        res = copy = ListNode()
        while list1 and list2: 
            if list1.val <= list2.val:
                copy.next = list1
                list1 = list1.next
                copy = copy.next
            else:
                copy.next = list2
                list2 = list2.next
                copy = copy.next
        if list1:
            copy.next = list1
            copy = copy.next
        else:
            copy.next = list2
            copy = copy.next
        return res.next
        