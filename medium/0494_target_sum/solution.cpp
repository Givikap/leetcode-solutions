#include <unordered_map>
#include <vector>

class Solution {
public:
  int findTargetSumWays(std::vector<int> &nums, int target) {
    const size_t n = nums.size();

    std::unordered_map<size_t, std::unordered_map<int, int>> memo;

    auto solve = [&](this auto &&self, int curr, size_t i) -> int {
      if (i == n)
        return curr == target ? 1 : 0;

      auto it = memo[i].find(curr);
      if (it != memo[i].end())
        return it->second;

      memo[i][curr] = self(curr + nums[i], i + 1) + self(curr - nums[i], i + 1);
      return memo[i][curr];
    };

    return solve(0, 0);
  }
};
