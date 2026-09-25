from utils.python.nodes import TreeNode


class Solution:
    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        stack = [(root, root.val)]
        nums = []

        while stack:
            node, num = stack.pop()

            if not node.left and not node.right:
                nums.append(num)
                continue

            if node.left:
                stack.append((node.left, (num << 1) | node.left.val))
            if node.right:
                stack.append((node.right, (num << 1) | node.right.val))

        return sum(nums)
