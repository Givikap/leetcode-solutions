from utils.python.nodes import TreeNode


class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        curr = root
        stack = []

        values = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()
            values.append(node.val)
            curr = node.right

        return values[k - 1]
