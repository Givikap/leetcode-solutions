from utils.python.nodes import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode | None, target_sum: int) -> bool:
        if not root:
            return False

        stack = [(root, root.val)]

        while stack:
            node, curr_sum = stack.pop()

            if curr_sum == target_sum and not node.left and not node.right:
                return True

            if node.left:
                stack.append((node.left, curr_sum + node.left.val))
            if node.right:
                stack.append((node.right, curr_sum + node.right.val))

        return False
