class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        n = len(arr)

        visited = [0] * n

        stack = [start]
        while stack:
            i = stack.pop()
            visited[i] = 1

            if arr[i] == 0:
                return True

            left_i = i + arr[i]
            right_i = i - arr[i]

            if left_i < n and not visited[left_i]:
                stack.append(left_i)
            if right_i > -1 and not visited[right_i]:
                stack.append(right_i)

        return False
