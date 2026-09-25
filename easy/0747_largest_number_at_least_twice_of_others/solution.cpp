#include <algorithm>
#include <ranges>
#include <vector>

class Solution {
public:
  int dominantIndex(std::vector<int> &nums) {
    auto it = std::ranges::max_element(nums);

    for (const auto &num : nums) {
      if (num * 2 > *it && num != *it)
        return -1;
    }

    return static_cast<int>(std::distance(nums.begin(), it));
  }
};
