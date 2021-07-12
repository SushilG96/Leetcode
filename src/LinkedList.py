class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after(self, pos, data):
        new_node = Node(data)
        count = 0
        cur = self.head

        while cur:
            cur = cur.next
            count += 1
            if count == pos:
                new_node.next = cur.next
                cur.next = new_node
                print(count)
                break

    def printll(self):
        cur = self.head

        while cur:
            print(cur.val, end="->")
            cur = cur.next
        print("Null")

    def isPalindrome(self, head):
        #         # Method 1
        #         cur = head
        #         s = ""
        #         while cur:
        #             s += str(cur.val)
        #             cur = cur.next
        #         return s == s[::-1]

        # Method 2
        stack = []
        cur = head

        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        while cur:
            data = stack.pop()
            if data != cur.val:
                return False
            cur = cur.next
        return True

    #    def reverse(self):
    #        pre = None
    #        cur = self.head
    #        while cur:
    #            # Storing the next node
    #            tmp = cur.next
    #
    #            cur.next = pre
    #
    #            pre = cur
    #
    #            cur = tmp
    #        return pre
    #
    def reverse(self):
        pre = None
        cur = self.head

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def hasCycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def removeNthFromEnd(self, n):
        cur = self.head
        l = 0
        while cur:
            l += 1
            cur = cur.next
        rem = l - n
        cur = self.head
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

    def swapNodes(self):
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
        cur = self.head
        while cur:
            tmp.append(cur)
            cur = cur.next

        tmp[k - 1].val, tmp[-k].val = tmp[-k].val, tmp[k - 1].val
        return head

    def middlenode(self):
        cur = self.head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        run = 0
        if n % 2 == 0:
            run = n // 2 + 1
        else:
            run = n // 2

        cur = self.head
        while run and cur:
            cur = cur.next
            run -= 1
        return cur.val


l1 = LinkedList()
l1.prepend(3)
l1.append(6)
l1.append(7)
l1.append(8)
l1.prepend(100)
l1.append(9)
l1.append(1)
l1.append(2)
l1.insert_after(5, 99)
l1.printll()
l1.reverse()
l1.printll()
print(l1.hasCycle())
print(l1.middlenode())
