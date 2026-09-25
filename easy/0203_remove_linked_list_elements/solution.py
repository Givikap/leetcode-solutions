from utils.python.nodes import ListNode


class Solution:
    def removeElements(
        self, head: ListNode | None, val: int
    ) -> ListNode | None:
        curr = head

        while curr:
            if curr.next and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        if head and head.val == val:
            head = head.next

        return head
