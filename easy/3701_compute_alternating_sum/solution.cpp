#include <vector>

class Solution {
public:
  int alternatingSum(std::vector<int> &nums) {
    int sum = 0;

    for (size_t i = 0; i < nums.size(); i += 2)
      sum += nums[i];

    for (size_t i = 1; i < nums.size(); i += 2)
      sum -= nums[i];

    return sum;
  }
};
