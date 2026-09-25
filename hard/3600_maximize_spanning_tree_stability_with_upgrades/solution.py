from utils.python import UnionFind


class Solution:
    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
        edges.sort(key=lambda edge: (-edge[3], -edge[2]))

        uf = UnionFind(n)
        mst = []

        for u, v, s, must in edges:
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst.append([u, v, s, must])
            elif must:
                return -1

        if len(mst) != n - 1:
            return -1

        mst.sort(key=lambda edge: (edge[3], edge[2]))

        for edge in mst:
            if not k or edge[3]:
                break

            edge[2] *= 2
            k -= 1

        return min(edge[2] for edge in mst)
