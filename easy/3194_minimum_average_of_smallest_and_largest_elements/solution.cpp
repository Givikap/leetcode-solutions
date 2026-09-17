#include <algorithm>
#include <limits>
#include <ranges>
#include <vector>

class Solution {
public:
  double minimumAverage(std::vector<int> &nums) {
    std::ranges::sort(nums);

    size_t left = 0;
    size_t right = nums.size() - 1;

    double minAverage = std::numeric_limits<double>::max();

    while (left <= right)
      minAverage = std::min(
          minAverage, static_cast<double>(nums[left++] + nums[right--]) / 2.0);

    return minAverage;
  }
};
