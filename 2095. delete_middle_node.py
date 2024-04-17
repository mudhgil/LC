class Node:
    def __init__(self, val = 0, next = None):
        self.next = next
        self.val = val
    def del_mid(self, head):
        if not self.head:
            return self.head
        fast, slow = head.next.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
    