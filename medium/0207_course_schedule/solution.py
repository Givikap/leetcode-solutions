class Solution:
    def canFinish(
        self, num_courses: int, prerequisites: list[list[int]]
    ) -> bool:
        prerequisites_map = [[] for _ in range(num_courses)]

        for course, prerequisite in prerequisites:
            prerequisites_map[course].append(prerequisite)

        visited = [0] * num_courses

        for start in range(num_courses):
            stack = [start]

            while stack:
                course = stack[-1]

                if visited[course] == 0:
                    visited[course] = 1

                for prerequisite in prerequisites_map[course]:
                    if visited[prerequisite] == 0:
                        stack.append(prerequisite)
                        break
                    if visited[prerequisite] == 1:
                        return False
                else:
                    visited[course] = 2
                    stack.pop()

        return True
