#include <algorithm>
#include <ranges>
#include <vector>

class Solution {
public:
  std::vector<int> targetIndices(std::vector<int> &nums, int target) {
    const size_t n = nums.size();

    std::ranges::sort(nums);

    int i = static_cast<int>(
        std::distance(nums.begin(), std::ranges::lower_bound(nums, target)));
    std::vector<int> indices;

    while (i < n && nums[i] == target)
      indices.push_back(i++);

    return indices;
  }
};
