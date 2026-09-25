class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        lines_count = 1
        remaining_line_width = 100

        for c in s:
            c_width = widths[ord(c) - 97]

            if remaining_line_width < c_width:
                lines_count += 1
                remaining_line_width = 100

            remaining_line_width -= c_width

        return [lines_count, 100 - remaining_line_width]
