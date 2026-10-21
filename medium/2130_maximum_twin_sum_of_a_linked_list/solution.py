from utils.python.nodes import ListNode


class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        if not head:
            return 0
        if not head.next:
            return head.val

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head1 = head
        head2 = prev

        maxTwinSum = 0

        while head2:
            maxTwinSum = max(maxTwinSum, head1.val + head2.val)
            head1 = head1.next
            head2 = head2.next

        return maxTwinSum
