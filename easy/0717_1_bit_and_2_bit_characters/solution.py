class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        pos = 0
        last_pos = None

        while pos < len(bits):
            last_pos = pos

            if bits[pos] == 0:
                pos += 1
            else:
                pos += 2

        return last_pos == len(bits) - 1
