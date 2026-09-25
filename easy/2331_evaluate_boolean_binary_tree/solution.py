from utils.python.nodes import TreeNode


class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        if root.val <= 1:
            return bool(root.val)

        if root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(
                root.right
            )
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(
                root.right
            )
