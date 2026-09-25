from utils.python.nodes import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        dummy = ListNode(-1)
        curr = dummy

        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            new_val = val1 + val2 + carry
            carry = new_val // 10
            new_val %= 10

            curr.next = ListNode(new_val)
            curr = curr.next

        return dummy.next
