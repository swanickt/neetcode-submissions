# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeInBetween(self, list1: Optional[ListNode], a: int, b: int, list2: Optional[ListNode]) -> Optional[ListNode]:

        i = 0
        prev = None
        curr = list1
        
        while i < b:
            prev, curr = curr, curr.next
            i += 1
            
            if i == a:
                a_prev = prev

        # at this point i == b, so curr = node b

        next_b = curr.next

        a_prev.next = list2

        prev, curr = None, list2
        while curr:
            prev, curr = curr, curr.next
        
        prev.next = next_b

        return list1



        