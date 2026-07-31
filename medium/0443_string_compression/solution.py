from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        read = 0
        write = 0

        while read < n:
            chars[write] = chars[read]
            write += 1
            read += 1

            count = 1

            while read < n and chars[read - 1] == chars[read]:
                read += 1
                count += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
