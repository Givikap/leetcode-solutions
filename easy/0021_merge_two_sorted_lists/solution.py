from utils.python.nodes import ListNode


class Solution:
    def mergeTwolists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        if not list1 and not list2:
            return None

        dummy = ListNode(-1)
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next

            curr = curr.next

        curr.next = list1 if list1 else list2

        return dummy.next
