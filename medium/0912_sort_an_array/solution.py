class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        n = len(nums)

        def siftDown(i: int) -> None:
            while True:
                left = 2 * i + 1
                right = 2 * i + 2

                largest = i

                if left < n and nums[left] > nums[largest]:
                    largest = left
                if right < n and nums[right] > nums[largest]:
                    largest = right

                if largest == i:
                    break

                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest

        def heapify():
            for i in range(n // 2 - 1, -1, -1):
                siftDown(i)

        heapify()

        for n in range(n - 1, -1, -1):
            nums[0], nums[n] = nums[n], nums[0]
            siftDown(0)

        return nums
