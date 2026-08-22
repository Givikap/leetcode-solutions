from typing import Optional, Tuple

from utils.python.nodes import TreeNode


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def solve(node: Optional[TreeNode]) -> Tuple[int]:
            if not node:
                return (0, 0)
            if not node.left and not node.right:
                return (node.val, 0)

            leftRobbed, leftNotRobbed = solve(node.left)
            rightRobbed, rightNotRobbed = solve(node.right)

            return (
                node.val + leftNotRobbed + rightNotRobbed,
                max(leftRobbed, leftNotRobbed)
                + max(rightRobbed, rightNotRobbed),
            )

        return max(solve(root))
