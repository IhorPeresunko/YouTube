# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        
        cur = fast = head
        while fast and fast.next:
            fast = fast.next.next
            cur = cur.next

        prev = None
        while cur:
            next = cur.next
            
            cur.next = prev
            
            prev = cur
            cur = next
            
        p1, p2 = head, prev
        
        while p1 and p2:
            res = max(res, p1.val + p2.val)
            
            p1 = p1.next
            p2 = p2.next
            
        return res
        
        
            