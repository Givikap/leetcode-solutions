from utils.python.nodes import TreeNode


class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        stack = []
        values = []

        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            values.append(curr.val)
            curr = curr.right

        return min(
            [abs(values[i] - values[i + 1]) for i in range(len(values) - 1)]
        )
