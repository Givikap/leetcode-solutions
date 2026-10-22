class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        occurences = [i for i, ch in enumerate(s) if ch == c]
        distances = [0] * len(s)

        right_i = 0

        left = float("-inf")
        right = occurences[right_i]

        for i in range(len(s)):
            distances[i] = min(i - left, right - i)

            if distances[i] == 0:
                left = right
                right_i += 1
                right = (
                    occurences[right_i]
                    if right_i < len(occurences)
                    else float("inf")
                )

        return distances
