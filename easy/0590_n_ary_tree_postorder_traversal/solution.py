from utils.python.nodes import Node


class Solution:
    def postorder(self, root: Node) -> list[int]:
        if not root:
            return []

        children = []
        stack = [root]

        while stack:
            node = stack.pop()

            children.append(node.val)
            stack.extend(node.children)

        children.reverse()
        return children
