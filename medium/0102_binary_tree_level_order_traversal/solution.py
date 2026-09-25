from collections import deque

from utils.python.nodes import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []

        queue = deque([root])
        levels = []

        while queue:
            levels.append([])

            for _ in range(len(queue)):
                node = queue.popleft()
                levels[-1].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return levels
