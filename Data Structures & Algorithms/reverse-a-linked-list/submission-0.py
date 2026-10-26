# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # a -> b -> c

        if not head:
            return None
        

        curr = head
        prev = None

        while curr:
            tmp_curr = curr.next
            curr.next = prev

            prev = curr
            curr = tmp_curr
        
        return prev
            

            
