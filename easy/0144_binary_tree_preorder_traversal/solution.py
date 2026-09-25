from collections import deque

from utils.python.nodes import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        values = []
        if not root:
            return values

        queue = deque([root])

        while queue:
            node = queue.popleft()
            values.append(node.val)

            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)

        return values
