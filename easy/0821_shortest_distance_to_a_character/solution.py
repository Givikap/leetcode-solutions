class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)

        distances = [n] * n

        for i, ch in enumerate(s):
            if ch == c:
                distances[i] = 0

                left = i - 1
                distance = 1

                while left >= 0 and distances[left] > distance:
                    distances[left] = distance
                    left -= 1
                    distance += 1

                right = i + 1
                distance = 1

                while right < n and distances[right] > distance:
                    distances[right] = distance
                    right += 1
                    distance += 1

        return distances
