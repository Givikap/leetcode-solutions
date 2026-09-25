from utils.python.nodes import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        is_balanced = True

        def dfs(root: TreeNode | None, depth: int):
            if not root:
                return 0

            left_height = dfs(root.left, depth)
            right_height = dfs(root.right, depth)

            if abs(left_height - right_height) > 1:
                nonlocal is_balanced
                is_balanced = False

            return 1 + max(left_height, right_height)

        dfs(root, 1)

        return is_balanced
