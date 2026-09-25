from utils.python.nodes import ListNode


class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        if fast:
            slow = slow.next

        while slow:
            if slow.val != prev.val:
                return False

            slow = slow.next
            prev = prev.next

        return True
