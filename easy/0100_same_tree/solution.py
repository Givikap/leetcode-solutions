from utils.python.nodes import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            elif not (node1 and node2):
                return False
            elif node1.val != node2.val:
                return False
            else:
                stack.extend(
                    ((node1.left, node2.left), (node1.right, node2.right))
                )

        return True
