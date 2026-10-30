#include <bit>
#include <vector>

class Solution {
public:
  int uniqueXorTriplets(std::vector<int> &nums) {
    const size_t n = nums.size();

    if (n <= 2)
      return static_cast<int>(n);
    else
      return 1 << std::bit_width(n);
  }
};
