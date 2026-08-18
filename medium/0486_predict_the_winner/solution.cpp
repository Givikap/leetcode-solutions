#include <vector>

class Solution {
public:
  bool predictTheWinner(std::vector<int> &nums) {
    const size_t n = nums.size();

    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));

    for (size_t i = n - 1; i != -1; --i) {
      for (size_t j = i; j < n; ++j) {
        if (i == j)
          dp[i][j] = nums[i];
        else
          dp[i][j] = std::max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
      }
    }

    return dp[0][n - 1] >= 0;
  }
};
