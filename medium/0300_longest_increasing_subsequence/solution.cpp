#include <vector>

class Solution {
public:
  int lengthOfLIS(std::vector<int> &nums) {
    std::vector<int> dp(nums.size(), 1);

    for (size_t i{}; i < nums.size(); ++i) {
      for (size_t j = i - 1; j != -1; --j) {
        if (nums[j] < nums[i])
          dp[i] = std::max(dp[i], dp[j] + 1);
      }
    }

    return *max_element(dp.begin(), dp.end());
  }
};
