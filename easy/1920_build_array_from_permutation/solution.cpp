#include <vector>

class Solution {
public:
  std::vector<int> buildArray(std::vector<int> &nums) {
    std::vector<int> ans(nums.size());

    for (size_t i{}; i < nums.size(); ++i)
      ans[i] = nums[static_cast<size_t>(nums[i])];

    return ans;
  }
};
