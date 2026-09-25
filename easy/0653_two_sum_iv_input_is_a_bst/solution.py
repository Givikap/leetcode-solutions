from utils.python.nodes import TreeNode


class Solution:
    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        visited = set()

        stack = [root]
        while stack:
            node = stack.pop()

            if k - node.val in visited:
                return True
            else:
                visited.add(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False
