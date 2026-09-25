class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        numsSet = set()

        for num in arr:
            if num * 2 in numsSet or (num % 2 == 0 and num / 2 in numsSet):
                return True

            numsSet.add(num)

        return False
