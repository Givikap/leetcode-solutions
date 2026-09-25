from utils.python.nodes import TreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        stack = [(str(root.val), root)]
        paths = []

        while stack:
            path, node = stack.pop()

            if not node.left and not node.right:
                paths.append(path)
                continue

            if node.left:
                stack.append((f"{path}->{node.left.val}", node.left))
            if node.right:
                stack.append((f"{path}->{node.right.val}", node.right))

        return paths
