# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        # dealt with empty lists
        dummy = node =  ListNode() # dummy is a node initalised with value 0 and so is node

        while list1 is not None and list2 is not None: # means an element in both lists
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        # edge case there may be remaining cases where list1 or list 2 is longer
        # if exits means one linked list is finished. Given it is ordered, 
        # the remaining elements in the linked list is larger than all elements in the linked list that finished. 
        node.next = list1 or list2
        # node is somewhere in the linked list
        print(node.val)
        return dummy.next # gets the first variable that node added 
                
            
             
            
    

        return result

        