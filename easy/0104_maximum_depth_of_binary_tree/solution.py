from utils.python.nodes import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = -1

        while stack:
            node, depth = stack.pop()

            if depth > max_depth:
                max_depth = depth

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth
