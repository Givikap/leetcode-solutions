#include <vector>

class Solution {
public:
  int stoneGameII(std::vector<int> &piles) {
    const size_t n = piles.size();

    std::vector<std::vector<std::vector<int>>> dp(
        2, std::vector<std::vector<int>>(n, std::vector<int>(n + 1, -1)));

    auto solve = [&](this auto self, size_t p, size_t i, size_t m) -> int {
      if (i >= n)
        return 0;
      if (dp[p][i][m] != -1)
        return dp[p][i][m];

      dp[p][i][m] = (p) ? 0 : INT_MAX;
      int stones = 0;

      for (size_t x = 1; x <= std::min(2 * m, n - i); ++x) {
        stones += piles[i + x - 1];

        if (p)
          dp[p][i][m] =
              std::max(dp[p][i][m], stones + self(0, i + x, std::max(m, x)));
        else
          dp[p][i][m] = std::min(dp[p][i][m], self(1, i + x, std::max(m, x)));
      }

      return dp[p][i][m];
    };

    return solve(1, 0, 1);
  }
};
