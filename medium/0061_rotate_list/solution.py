from utils.python.nodes import ListNode


class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        list_len = 0

        curr = head
        while curr:
            back = curr
            curr = curr.next
            list_len += 1

        k = list_len - k % list_len - 1

        curr = head
        for _ in range(k):
            curr = curr.next

        back.next = head
        head = curr.next
        curr.next = None

        return head
