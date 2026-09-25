from utils.python.nodes import TreeNode


class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            else:
                root = root.left

        return None
