#include <vector>

class Solution {
public:
  std::vector<int> sortArrayByParityII(std::vector<int> &nums) {
    size_t evenIdx = 0;
    size_t oddIdx = 1;

    for (size_t i{}; i < nums.size(); ++i) {
      if (i % 2 == 0 && nums[i] % 2 == 1) {
        std::swap(nums[i--], nums[oddIdx]);
        oddIdx += 2;
      } else if (i % 2 == 1 && nums[i] % 2 == 0) {
        std::swap(nums[i--], nums[evenIdx]);
        evenIdx += 2;
      }
    }

    return nums;
  }
};
