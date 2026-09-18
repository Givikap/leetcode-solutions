#include <algorithm>
#include <functional>
#include <vector>

class Solution {
public:
  int xorOperation(int n, int start) {
    std::vector<int> nums;
    nums.reserve(static_cast<size_t>(n));

    for (int i = 0; i < n; ++i)
      nums.push_back(start + 2 * i);

    return std::ranges::fold_left(nums, 0, std::bit_xor<int>());
  }
};
