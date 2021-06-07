# 1721. Swapping Nodes in a Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head, k):
        #         cur = head
        #         l = 0

        #         s = None
        #         while cur:
        #             l += 1
        #             if l == k:
        #                 start = cur.val
        #                 s = cur
        #             cur = cur.next
        #         cur = head
        #         run = l - k
        #         while cur and run:
        #             cur = cur.next
        #             run-=1
        #         if run == 0:
        #             s.val, cur.val = cur.val, s.val
        #         return head

        # to have a copy of the node

        tmp = []
        cur = head
        while cur:
            tmp.append(cur)
            cur = cur.next

        tmp[k - 1].val, tmp[-k].val = tmp[-k].val, tmp[k - 1].val
        return head
