from utils.python.nodes import TreeNode


class Solution:
    def leafSimilar(
        self, root1: TreeNode | None, root2: TreeNode | None
    ) -> bool:
        leafs1 = []
        leafs2 = []

        for root, leafs in ((root1, leafs1), (root2, leafs2)):
            stack = [root]

            while stack:
                node = stack.pop()

                if not node.left and not node.right:
                    leafs.append(node.val)
                    continue

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return leafs1 == leafs2
