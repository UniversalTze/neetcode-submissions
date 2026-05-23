# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(n * k) (aim for)
        # O(1) space

        # brute force: storing all nodes in an array, sorting array and then converting sorted array
        # into a linked list. O(N) space and O(N LOG N) Time. 

        # each linked list in array is sorted. 
        # the way to do it is to sort two lists and then continue to move through the linked lists until done
        if len(lists) == 0:
            return 
        if len(lists) == 1:  # item in list is already ordered.
            return lists[0] # first index
        # more than 1 item in the list
        head = None
        for index in range(1, len(lists)):
            # function call to merge 2 linked lists
            if index == 1: 
                head = self.mergeTwoLists(lists[index - 1], lists[index])
            else: 
                head = self.mergeTwoLists(head, lists[index])
    
        return head

    """
    Function used to merge two linked lists with the head of the list returned.
    """
    def mergeTwoLists(self, list1, list2): 
        # list 1 will hold the reference to the sorted list, while list 2 is the new list
        # that needs to be sorted.
        res = dummy = ListNode() # dummy is used to build the linked list.
        while list1 and list2: 
            if list1.val <= list2.val: 
                dummy.next = list1
                list1 = list1.next
            else: 
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        # if list1 exited the loop, list 2 is not None. If list2 exited the loop (None)
        # list1 is not None
        dummy.next = list1 if list2 is None else list2
        return res.next # holds the head of the list



        