class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        in_degree = [0] * (n + 1)
        out_degree = [0] * (n + 1)

        for a, b in trust:
            in_degree[b] += 1
            out_degree[a] += 1

        for person in range(1, n + 1):
            if in_degree[person] == n - 1 and out_degree[person] == 0:
                return person

        return -1
