from utils.python.nodes import TreeNode


class Solution:
    def findMode(self, root: TreeNode | None) -> list[int]:
        modes = []
        mode_count = 0

        curr_val = -(10**5 + 1)
        curr_count = 0

        curr = root
        stack = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            node = stack.pop()

            if curr_val != node.val:
                curr_val = node.val
                curr_count = 1
            else:
                curr_count += 1

            if curr_count > mode_count:
                modes = [node.val]
                mode_count = curr_count
            elif curr_count == mode_count:
                modes.append(node.val)

            curr = node.right

        return modes
