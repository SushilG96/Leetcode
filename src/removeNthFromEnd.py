# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        rem = length - n
        cur = head
        run = 0
        while cur:
            if run == rem - 1:
                cur.next = cur.next.next
                break
            elif rem == 0:
                head = cur.next
                break
            cur = cur.next
            run += 1

        return head
