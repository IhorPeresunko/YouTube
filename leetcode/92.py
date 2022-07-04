# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev, cur = None, head
        
        for _ in range(left - 1):
            prev, cur = cur, cur.next
            
        connector_node, new_tail = prev, cur
        
        for _ in range(left - 1, right):
            next = cur.next
            
            cur.next = prev
            
            prev = cur
            cur = next
        
        if connector_node:
            connector_node.next = prev
        else:
            head = prev

        new_tail.next = next
        
        return head