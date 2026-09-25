class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        stack = []
        times = [0] * n

        last_ts = 0

        for log in logs:
            fid, action, ts = log.split(":")

            fid = int(fid)
            ts = int(ts)

            if action == "start":
                if stack:
                    times[stack[-1]] += ts - last_ts

                stack.append(fid)
                last_ts = ts
            else:
                times[stack.pop()] += ts - last_ts + 1

                if stack:
                    last_ts = ts + 1

        return times
