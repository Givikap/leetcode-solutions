class Solution:
    def minInsertions(self, s: str) -> int:
        s = s.replace("))", "}")
        insertions = s.count(")")

        s = s.replace("}", ")")
        while "()" in s:
            s = s.replace("()", "")

        return insertions + s.count("(") + len(s)
