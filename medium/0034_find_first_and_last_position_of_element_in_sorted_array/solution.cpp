#include <algorithm>
#include <ranges>
#include <vector>

class Solution {
public:
  std::vector<int> searchRange(std::vector<int> &nums, int target) {
    auto [start, end] = std::ranges::equal_range(nums, target);

    if (start == nums.end() || *start != target)
      return {-1, -1};

    return {static_cast<int>(start - nums.begin()),
            static_cast<int>(end - nums.begin()) - 1};
  }
};
