#include "../../utils/cpp/union_find.hpp"
#include <vector>

class Solution {
public:
  int minScore(int n, std::vector<std::vector<int>> &roads) {
    utils::UnionFind uf(n + 1);

    for (const std::vector<int> &road : roads) {
      if (uf.find(road[0]) != uf.find(road[1]))
        uf.merge(road[0], road[1]);
    }

    int minDistance = INT_MAX;

    for (const std::vector<int> &road : roads) {
      if (uf.find(1) == uf.find(road[0]))
        minDistance = std::min(minDistance, road[2]);
    }

    return minDistance;
  }
};
