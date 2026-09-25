from utils.python.nodes import ListNode


class Solution:
    def removeNthFromEnd(
        self, head: ListNode | None, n: int
    ) -> ListNode | None:
        if not head.next:
            return None

        fast = head

        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next

        fast = fast.next
        slow = head

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return head
