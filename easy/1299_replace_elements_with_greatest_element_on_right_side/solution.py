class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        max_element = -1

        for i in range(len(arr) - 1, -1, -1):
            arr[i], max_element = max_element, max(max_element, arr[i])

        return arr
