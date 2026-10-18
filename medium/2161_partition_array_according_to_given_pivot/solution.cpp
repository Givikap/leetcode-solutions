#include <vector>

class Solution {
public:
  std::vector<int> pivotArray(std::vector<int> &nums, int pivot) {
    std::vector<int> smaller;
    int pivotsCount = 0;
    std::vector<int> larger;

    for (const auto &num : nums) {
      if (num < pivot)
        smaller.push_back(num);
      else if (num == pivot)
        ++pivotsCount;
      else
        larger.push_back(num);
    }

    nums.clear();
    nums.insert(nums.begin(), smaller.begin(), smaller.end());
    nums.insert(nums.begin() + smaller.size(), pivotsCount, pivot);
    nums.insert(nums.begin() + smaller.size() + pivotsCount, larger.begin(),
                larger.end());

    return nums;
  }
};
