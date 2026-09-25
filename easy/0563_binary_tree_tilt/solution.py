from utils.python.nodes import TreeNode


class Solution:
    def findTilt(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        stack1 = [root]
        stack2 = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        tilt = 0
        nodeSums = {}

        while stack2:
            node = stack2.pop()

            leftSum = nodeSums[node.left] if node.left else 0
            rightSum = nodeSums[node.right] if node.right else 0

            tilt += abs(leftSum - rightSum)
            nodeSums[node] = node.val + leftSum + rightSum

        return tilt
