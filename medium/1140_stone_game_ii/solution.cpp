#include <vector>

class Solution {
public:
  int stoneGameII(std::vector<int> &piles) {
    const size_t n = piles.size();

    std::vector<std::vector<int>> dp(n, std::vector<int>(n + 1, -1));

    std::vector<int> suffixSums(n, piles[n - 1]);
    for (size_t i = n - 2; i < -1; --i)
      suffixSums[i] = suffixSums[i + 1] + piles[i];

    auto solve = [&](this auto self, size_t i, size_t m) -> int {
      if (i >= n)
        return 0;
      if (i + 2 * m >= n)
        return suffixSums[i];
      if (dp[i][m] != -1)
        return dp[i][m];

      int stones = INT_MAX;
      for (size_t x = 1; x <= 2 * m; ++x)
        stones = std::min(stones, self(i + x, std::max(m, x)));

      return dp[i][m] = suffixSums[i] - stones;
    };

    return solve(0, 1);
  }
};
