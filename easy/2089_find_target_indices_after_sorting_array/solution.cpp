#include <algorithm>
#include <ranges>
#include <vector>

class Solution {
public:
  std::vector<int> targetIndices(std::vector<int> &nums, int target) {
    std::ranges::sort(nums);

    auto it = std::ranges::lower_bound(nums, target);

    std::vector<int> indices;
    if (it == nums.end() || *it != target)
      return indices;

    int i = static_cast<int>(std::distance(nums.begin(), it));

    do
      indices.push_back(i++);
    while (++it != nums.end() && *it == target);

    return indices;
  }
};
