class Solution:
    def missingNumber(self, arr: list[int]) -> int:
        step = int((arr[-1] - arr[0]) / len(arr))

        if step == 0:
            return arr[0]

        expected_arr = list(range(arr[0], arr[-1], step))

        for i in range(len(arr)):
            if arr[i] != expected_arr[i]:
                return expected_arr[i]

        return -1
