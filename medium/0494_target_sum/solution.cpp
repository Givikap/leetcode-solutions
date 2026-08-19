#include <numeric>
#include <unordered_map>
#include <vector>

class Solution {
public:
  int findTargetSumWays(std::vector<int> &nums, int target) {
    const size_t n = nums.size();
    const size_t offset =
        static_cast<size_t>(std::accumulate(nums.begin(), nums.end(), 0));

    std::vector<std::vector<int>> memo(n + 1,
                                       std::vector<int>(2 * offset + 1, -1));

    auto solve = [&](this auto &&self, int curr, size_t i) -> int {
      if (i == n)
        return curr == target ? 1 : 0;

      size_t j = static_cast<size_t>(curr) + offset;
      if (memo[i][j] != -1)
        return memo[i][j];

      memo[i][j] = self(curr + nums[i], i + 1) + self(curr - nums[i], i + 1);
      return memo[i][j];
    };

    return solve(0, 0);
  }
};
