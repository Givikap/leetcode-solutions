class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        paths_map = dict(paths)

        destination = paths[0][0]

        while destination in paths_map:
            destination = paths_map[destination]

        return destination
