# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # have a pointer that reverses the current list
        # how can this be done in O(1) space

        # just hold references to two halfs of the list
        # need to do one loop to determine list or use slow and fast pointer

        # 1,2,3,4
        # slow = 2, fast = 3
        # fast = None (break out) so this will be two lists: 1,2 and 3,4

        # 1,2,3,4,5,6,7
        # slow = 2, fast = 3, slow = 3, fast = 5, slow = 4 fast = 7
        # slow + 1 indicates middle of the list
        slow = head # has referecne to what head is referencing 
        fast = head.next # same here 
        # starting fast ahead of slow gives you first middle . 
        # 1,2,3,4 -> slow = 2, instead of 3 (starting at the same place)
        # starting fast = slow gives you second middle . 
        # 1,2,3,4 -> slow = 2, instead of 3 (starting at the same place)
        # logic is true for an even list.
        # logic is true for an even list.

        # fast is not mutating anything, only used to detect middle of the linked list
        while fast and fast.next: # [2,4,6,7]
            slow = slow.next # slow = 4 head = 2, (iteration 2) slow = 6 head = 2
            fast = fast.next.next # fast = 6, fast = None

        # now reverse slow
        higher = slow.next # stored refernce to higher order of the array
        slow.next = None # mutating the original object that head also points to so now head will be affected
        # so after the middle first middle (even) or true middle (odd), it will point to None
        
        # now reverse the higher end of the list
        reversedHigh, cur = None, higher
        while cur: 
            temp = cur.next
            cur.next = reversedHigh
            reversedHigh = cur
            cur = temp
        
        first = head # set first to head so that head doesn't move
        while reversedHigh:
            # store the next variables for first (lower order)
            # and reversedHigh (higher order)
            temp1,temp2 = first.next, reversedHigh.next
            #[0, n-1, 1, n-2, 2, n-3, ...]
            # so first element in list .next ref = current reversedHigh
            first.next = reversedHigh # does [0, n-1,]
            reversedHigh.next = temp1 #[n-1, 1] ref
            # its doing two at the same time 
            first, reversedHigh = temp1, temp2
            
            # first itertaion: [1,2,3,4,6]

        
        