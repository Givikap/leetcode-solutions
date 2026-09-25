from utils.python.nodes import ListNode


class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.next:
                temp = curr.next
                prev.next, curr.next, temp.next = temp, temp.next, curr

            prev = curr
            curr = curr.next

        return dummy.next
