from utils.python.nodes import TreeNode


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        stack = [root]
        range_sum = 0

        while stack:
            node = stack.pop()

            if low <= node.val <= high:
                range_sum += node.val

            if node.left and node.val > low:
                stack.append(node.left)
            if node.right and node.val < high:
                stack.append(node.right)

        return range_sum
