from utils.python.nodes import ListNode


class Solution:
    def reorderlist(self, head: ListNode | None) -> None:
        slow = fast = head
        prev = None

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next

        prev.next = None
        prev = None

        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        curr = head
        inorder = head.next
        reverse = prev

        while reverse:
            curr.next = reverse
            curr, reverse = curr.next, reverse.next

            if inorder:
                curr.next = inorder
                curr, inorder = curr.next, inorder.next
