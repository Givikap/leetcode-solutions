class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parentheses_list = []
        stack = [("(", n - 1, n)]

        while stack:
            parentheses, open_left, closed_left = stack.pop()

            if open_left == 0 and closed_left == 0:
                parentheses_list.append(f"{parentheses}")
                continue

            if open_left == 0:
                stack.append((f"{parentheses})", 0, closed_left - 1))
            elif closed_left > 1 and open_left < closed_left:
                stack.append((f"{parentheses})", open_left, closed_left - 1))
                stack.append((f"{parentheses}(", open_left - 1, closed_left))
            else:
                stack.append((f"{parentheses}(", open_left - 1, closed_left))

        return parentheses_list
