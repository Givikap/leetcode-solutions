#include <algorithm>
#include <ranges>
#include <vector>

class Solution {
public:
  long long maxAlternatingSum(std::vector<int> &nums) {
    const size_t n = nums.size();

    for (auto &num : nums) {
      if (num < 0)
        num = -num;
    }

    std::ranges::sort(nums);

    long long score = 0LL;

    for (size_t left = 0, right = n - 1; left < right; ++left, --right) {
      score += static_cast<long long>(nums[right]) * nums[right];
      score -= static_cast<long long>(nums[left]) * nums[left];
    }

    if (n % 2 == 1)
      score += static_cast<long long>(nums[n / 2]) * nums[n / 2];

    return score;
  }
};
