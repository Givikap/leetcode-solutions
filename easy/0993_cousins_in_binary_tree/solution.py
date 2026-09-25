from utils.python.nodes import TreeNode


class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        depths = {}
        parents = {}

        stack = [(root, 0, -1)]
        while stack:
            node, depth, parent = stack.pop()

            depths[node.val] = depth
            parents[node.val] = parent

            if node.left:
                stack.append((node.left, depth + 1, node.val))
            if node.right:
                stack.append((node.right, depth + 1, node.val))

        return depths[x] == depths[y] and parents[x] != parents[y]
