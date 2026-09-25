from utils.python.nodes import TreeNode


class Solution:
    def countNodes(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        height_left = 0
        height_right = 0

        curr = root
        while curr:
            curr = curr.left
            height_left += 1

        curr = root
        while curr:
            curr = curr.right
            height_right += 1

        if height_left == height_right:
            return 2**height_left - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
