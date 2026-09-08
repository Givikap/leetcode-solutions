#include <vector>

class Solution {
public:
  int removeDuplicates(std::vector<int> &nums) {
    const size_t n = nums.size();

    size_t insert{};
    for (size_t read{}; read < n; ++insert) {
      nums[insert] = nums[read++];

      while (read + 1 < n && nums[read + 1] == nums[insert])
        ++read;
    }

    return static_cast<int>(insert);
  }
};
