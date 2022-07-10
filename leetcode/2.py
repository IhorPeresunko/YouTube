# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = cur = ListNode(0)
        cur1 = l1
        cur2 = l2

        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val = l1_val + l2_val + carry
            
            carry = val // 10
            cur.next = ListNode(val % 10)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return head.next