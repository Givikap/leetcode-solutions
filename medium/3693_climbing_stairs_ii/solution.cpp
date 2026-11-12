#include <vector>

class Solution {
public:
  int climbStairs(int n, std::vector<int> &costs) {
    costs.insert(costs.begin(), 0);

    int oneHopCost = costs[static_cast<size_t>(n)];
    int twoHopCost = INT_MAX / 2;
    int threeHopCost = INT_MAX / 2;

    for (size_t i = static_cast<size_t>(n - 1); i != -1; --i) {
      int cost =
          costs[i] +
          std::min(oneHopCost + 1, std::min(twoHopCost + 4, threeHopCost + 9));
      threeHopCost = std::exchange(twoHopCost, std::exchange(oneHopCost, cost));
    }

    return oneHopCost;
  }
};
