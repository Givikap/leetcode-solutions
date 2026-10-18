#include <vector>

class Solution {
public:
  std::vector<int> pivotArray(std::vector<int> &nums, int pivot) {
    std::vector<int> pivotedNums;
    pivotedNums.reserve(nums.size());

    for (const auto &num : nums) {
      if (num < pivot)
        pivotedNums.push_back(num);
    }

    for (const auto &num : nums) {
      if (num == pivot)
        pivotedNums.push_back(num);
    }

    for (const auto &num : nums) {
      if (num > pivot)
        pivotedNums.push_back(num);
    }

    return pivotedNums;
  }
};
