from collections import deque

from utils.python.nodes import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        nodes_deque = deque([root])
        level_averages = []

        while nodes_deque:
            level_averages.append(0)
            level_size = len(nodes_deque)

            for _ in range(level_size):
                node = nodes_deque.popleft()

                level_averages[-1] += node.val

                if node.left:
                    nodes_deque.append(node.left)
                if node.right:
                    nodes_deque.append(node.right)

            level_averages[-1] /= level_size

        return level_averages
