class Node:
    def __init__(
        self,
        val: int | None = None,
        children: list["Node"] | None = None,
    ):
        self.val = val
        self.children = children


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" | None = None):
        self.val = val
        self.next = next

    def __lt__(self, other: "ListNode"):
        return self.val < other.val


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode" | None = None,
        right: "TreeNode" | None = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_word = False
