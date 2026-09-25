from utils.python.nodes import TreeNode


class Solution:
    def createBinaryTree(
        self, descriptions: list[list[int]]
    ) -> TreeNode | None:
        nodesMap = {}
        parentless = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodesMap:
                nodesMap[parent] = TreeNode(val=parent)
                parentless.add(parent)

            if child not in nodesMap:
                nodesMap[child] = TreeNode(val=child)
            if child in parentless:
                parentless.remove(child)

            if isLeft:
                nodesMap[parent].left = nodesMap[child]
            else:
                nodesMap[parent].right = nodesMap[child]

        return nodesMap[parentless.pop()]
