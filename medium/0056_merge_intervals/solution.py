class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(reverse=True)
        merged_intervals = []

        curr = intervals.pop()
        while intervals:
            next = intervals.pop()

            if curr[1] >= next[0]:
                curr[1] = max(curr[1], next[1])
            else:
                merged_intervals.append(curr)
                curr = next

        merged_intervals.append(curr)
        return merged_intervals
