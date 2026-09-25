from utils.python.nodes import TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        stack = [(root, False)]
        left_leaves_sum = 0

        while stack:
            node, is_left = stack.pop()

            if not node.left and not node.right and is_left:
                left_leaves_sum += node.val

            if node.left:
                stack.append((node.left, True))
            if node.right:
                stack.append((node.right, False))

        return left_leaves_sum
