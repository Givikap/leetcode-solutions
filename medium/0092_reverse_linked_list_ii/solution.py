from utils.python.nodes import ListNode


class Solution:
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        if left == right:
            return head

        curr = head
        prev = None

        for _ in range(left - 1):
            prev, curr = curr, curr.next

        before_reversed = prev
        reversed_start = curr
        prev = None

        for _ in range(right - left + 1):
            curr.next, prev, curr = prev, curr, curr.next

        reversed_start.next = curr

        if left == 1:
            return prev

        before_reversed.next = prev

        return head
