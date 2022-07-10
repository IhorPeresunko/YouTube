# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        mem = collections.defaultdict(int)
        dummy = ListNode(0)
        dummy.next = head

        cur = head
        while cur:
            mem[cur.val] += 1
            cur = cur.next
            
        cur = dummy
        while cur and cur.next:
            if mem[cur.next.val] > 1:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy.next