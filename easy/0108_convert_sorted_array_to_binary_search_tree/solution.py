from utils.python.nodes import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        mid = len(nums) // 2

        root = TreeNode(val=nums[mid])

        stack = [(root, 0, 0, mid)]
        if mid + 1 != len(nums):
            stack.append((root, 1, mid + 1, len(nums)))

        while stack:
            (
                node,
                side,
                start,
                end,
            ) = stack.pop()

            if start == end:
                continue

            mid = (start + end) // 2

            if side == 0:
                node.left = node = TreeNode(val=nums[mid])
            else:
                node.right = node = TreeNode(val=nums[mid])

            if start != mid:
                stack.append((node, 0, start, mid))
            if mid + 1 != end:
                stack.append((node, 1, mid + 1, end))

        return root
