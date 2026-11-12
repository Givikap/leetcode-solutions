#include <vector>

class Solution {
public:
  int climbStairs(int n, std::vector<int> &costs) {
    const size_t m = costs.size();

    std::vector<int> dp(m + 1zu, INT_MAX);
    dp[0zu] = 0;

    for (size_t i{}; i < m; ++i) {
      size_t maxJump = std::min(i + 4zu, m + 1zu);
      for (size_t j = i + 1zu; j < maxJump; ++j)
        dp[j] = std::min(dp[j], dp[i] + costs[j - 1zu] +
                                    static_cast<int>((j - i) * (j - i)));
    }

    return dp[m];
  }
};
