#include <vector>

class Solution {
public:
  int smallestIndex(std::vector<int> &nums) {
    auto digitsSum = [](int num) {
      int digitsSum = 0;

      while (num) {
        digitsSum += num % 10;
        num /= 10;
      }

      return digitsSum;
    };

    for (size_t i{}; i < nums.size(); ++i) {
      if (digitsSum(nums[i]) == static_cast<int>(i))
        return static_cast<int>(i);
    }

    return -1;
  }
};
