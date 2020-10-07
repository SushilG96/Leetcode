# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        # Find the length of linked list
        count = 0
        current_node = head
        while current_node:
            count += 1
            current_node = current_node.next
    
        if head is None or head.next is None:
            return head
        
        for _ in range(int(k%count)):
            tmp = head
            last_node = head
            while last_node.next.next:
                last_node = last_node.next
            
            head = last_node.next
            last_node.next.next = tmp
            last_node.next = None

        return head
