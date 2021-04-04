# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
def swapPairs(self, head):
    curr = head
    k = 0
    while curr:
        k += 1
        if k % 2 != 0 and curr.next:
            curr.val, curr.next.val = curr.next.val, curr.val
        curr = curr.next
    return head
