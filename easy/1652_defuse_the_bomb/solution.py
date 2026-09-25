class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        code_len = len(code)

        if k == 0:
            return [0] * code_len

        decrypted_code = []

        if k > 0:
            k_sum = sum(code[i] for i in range(1, k + 1))
            i = (k + 1) % code_len
        else:
            k_sum = sum(code[i] for i in range(code_len + k, code_len))
            i = 0

        k = abs(k)

        for _ in range(code_len):
            decrypted_code.append(k_sum)
            k_sum += code[i] - code[i - k]
            i = (i + 1) % code_len

        return decrypted_code
