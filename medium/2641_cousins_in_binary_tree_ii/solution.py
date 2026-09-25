from utils.python.nodes import TreeNode


class Solution:
    def replaceValueInTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return root

        level = [root]
        level_sum = root.val

        while level:
            next_level = []
            next_level_sum = 0

            for node in level:
                node.val = level_sum - node.val

                sibling_sum = node.left.val if node.left else 0
                sibling_sum += node.right.val if node.right else 0

                if node.left:
                    next_level_sum += node.left.val
                    node.left.val = sibling_sum
                    next_level.append(node.left)
                if node.right:
                    next_level_sum += node.right.val
                    node.right.val = sibling_sum
                    next_level.append(node.right)

            level = next_level
            level_sum = next_level_sum

        return root
