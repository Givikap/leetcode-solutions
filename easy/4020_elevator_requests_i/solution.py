class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        seconds = requests[0]

        for i in range(1, len(requests)):
            seconds += abs(requests[i] - requests[i - 1])

        return seconds
