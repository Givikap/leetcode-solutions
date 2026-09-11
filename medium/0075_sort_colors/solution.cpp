#include <vector>

class Solution {
public:
  void sortColors(std::vector<int> &nums) {
    std::vector<int> colorsCounts(3, 0);

    for (const auto &num : nums)
      ++colorsCounts[static_cast<size_t>(num)];

    size_t color{};
    for (size_t i{}; i < nums.size(); ++i) {
      while (colorsCounts[color] == 0)
        ++color;

      nums[i] = color;
      --colorsCounts[color];
    }
  }
};
