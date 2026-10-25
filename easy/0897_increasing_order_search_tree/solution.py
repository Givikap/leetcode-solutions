from utils.python.nodes import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        def increasingBST(
            node: TreeNode | None, tail: TreeNode | None = None
        ) -> TreeNode | None:
            if not node:
                return tail

            temp = increasingBST(node.left, node)
            node.left = None
            node.right = increasingBST(node.right, tail)
            return temp

        return increasingBST(root)
