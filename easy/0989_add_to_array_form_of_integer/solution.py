class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) - 1

        carry = 0

        while k or carry:
            if i == -1:
                num.append(-1)

                for j in range(len(num) - 1, 0, -1):
                    num[j] = num[j - 1]

                num[0] = 0
                i = 0

            num[i] += k % 10 + carry
            carry = num[i] // 10
            num[i] %= 10

            k //= 10
            i -= 1

        return num
