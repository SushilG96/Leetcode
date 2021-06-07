# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        run = n // 2
        cur = head
        while run and cur:
            cur = cur.next
            run -= 1
        return cur
