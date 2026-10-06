class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openParenthesesCount = 0
        missingParenthesesCount = 0

        for c in s:
            if c == "(":
                openParenthesesCount += 1
            else:
                if openParenthesesCount > 0:
                    openParenthesesCount -= 1
                else:
                    missingParenthesesCount += 1

        return openParenthesesCount + missingParenthesesCount
