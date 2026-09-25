from collections import Counter


class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        preference_counter = Counter(students)

        for sandwich in sandwiches:
            if preference_counter[sandwich] == 0:
                return preference_counter[not sandwich]

            preference_counter[sandwich] -= 1

        return 0
