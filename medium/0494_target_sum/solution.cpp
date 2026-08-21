#include <numeric>
#include <vector>

class Solution {
public:
  int findTargetSumWays(std::vector<int> &nums, int target) {
    const int numsSum = std::accumulate(nums.begin(), nums.end(), 0);

    if ((numsSum + target) % 2 == 1 || abs(target) > numsSum)
      return 0;

    const size_t capacity = static_cast<size_t>(numsSum + target) / 2;

    std::vector<int> dp(capacity + 1, 0);
    dp[0] = 1;

    for (size_t i{}; i < nums.size(); ++i)
      for (size_t j = capacity; j != -1 && j >= static_cast<size_t>(nums[i]);
           --j)
        dp[j] += dp[j - static_cast<size_t>(nums[i])];

    return dp[capacity];
  }
};
