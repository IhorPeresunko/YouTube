# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left = right = head
        i = 1
        while i <= n and right:
            right = right.next
            i += 1

        if not right:
            return head.next

        while right and right.next:
            right = right.next
            left = left.next

        left.next = left.next.next

        return head