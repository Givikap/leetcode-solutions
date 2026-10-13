#include <algorithm>
#include <cmath>
#include <ranges>
#include <vector>

class Solution {
public:
  long long maxAlternatingSum(std::vector<int> &nums) {
    const size_t n = nums.size();

    std::ranges::sort(
        nums, [](const auto &a, const auto &b) { return abs(a) < abs(b); });

    long long score = 0l;

    for (size_t left = 0, right = n - 1; left < right; ++left, --right) {
      score += static_cast<long long>(nums[right]) *
               static_cast<long long>(nums[right]);
      score -= static_cast<long long>(nums[left]) *
               static_cast<long long>(nums[left]);
    }

    if (n % 2 == 1)
      score += static_cast<long long>(nums[n / 2]) *
               static_cast<long long>(nums[n / 2]);

    return score;
  }
};
