from utils.python.nodes import ListNode


class Solution:
    def getIntersectionNode(
        self, head_a: ListNode, head_b: ListNode
    ) -> ListNode | None:
        if not head_a or not head_b:
            return None

        p_a, p_b = head_a, head_b

        while p_a is not p_b:
            p_a = p_a.next if p_a else head_b
            p_b = p_b.next if p_b else head_a

        return p_a
