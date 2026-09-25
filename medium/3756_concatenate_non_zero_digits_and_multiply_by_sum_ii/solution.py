class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)

        mod = 1000000007
        inv10 = 700000005

        pow10 = [1] * (n + 1)
        inv10pow = [1] * (n + 1)

        for i in range(1, n + 1):
            pow10[i] = pow10[i - 1] * 10 % mod
            inv10pow[i] = inv10pow[i - 1] * inv10 % mod

        count = [0] * (n + 1)
        prefixSums = [0] * (n + 1)
        digitsSums = [0] * (n + 1)

        for i in range(1, n + 1):
            digit = ord(s[i - 1]) - 48

            count[i] = count[i - 1] + (1 if digit else 0)
            prefixSums[i] = (
                prefixSums[i - 1]
                + (digit * inv10pow[count[i]] if digit else 0)
            ) % mod
            digitsSums[i] = digitsSums[i - 1] + digit

        results = []

        for l, r in queries:
            x = pow10[count[r + 1]] * (prefixSums[r + 1] - prefixSums[l]) % mod
            digitSum = digitsSums[r + 1] - digitsSums[l]

            results.append(x * digitSum % mod)

        return results
