from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone_keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = deque(c for c in phone_keyboard[digits[0]])

        for i in range(1, len(digits)):
            for _ in range(len(combinations)):
                combination = combinations.popleft()
                combinations.extend(
                    combination + c for c in phone_keyboard[digits[i]]
                )

        return list(combinations)
