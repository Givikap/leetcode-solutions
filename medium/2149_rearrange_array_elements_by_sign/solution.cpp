#include <vector>

class Solution {
public:
  std::vector<int> rearrangeArray(std::vector<int> &nums) {
    std::vector<int> rearrangedNums(nums.size());

    size_t positive = 0;
    size_t negative = 1;

    for (const int &num : nums) {
      if (num > 0) {
        rearrangedNums[positive] = num;
        positive += 2;
      } else {
        rearrangedNums[negative] = num;
        negative += 2;
      }
    }

    return rearrangedNums;
  }
};
