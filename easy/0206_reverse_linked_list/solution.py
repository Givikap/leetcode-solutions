from utils.python.nodes import ListNode


class Solution:
    def reverselist(self, head: ListNode | None) -> ListNode | None:
        prev = None

        while head:
            head.next, prev, head = prev, head, head.next

        return prev
