#include <vector>

class Solution {
public:
  int arithmeticTriplets(std::vector<int> &nums, int diff) {
    const size_t n = nums.size();

    int count = 0;

    for (size_t i{}; i < n; ++i) {
      for (size_t j = i + 1zu; j < n; ++j) {
        for (size_t k = j + 1zu; k < n; ++k) {
          if (nums[j] - nums[i] == diff && nums[k] - nums[j] == diff)
            ++count;
        }
      }
    }

    return count;
  }
};
