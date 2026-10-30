#include <vector>

class Solution {
public:
  int uniqueXorTriplets(std::vector<int> &nums) {
    const size_t n = nums.size();
    const size_t maxXor = 2048zu;

    std::vector<bool> xorPairs(maxXor, false);
    std::vector<bool> xorTriplets(maxXor, false);

    for (size_t i{}; i < n; ++i) {
      for (size_t j = i; j < n; ++j)
        xorPairs[static_cast<size_t>(nums[i] ^ nums[j])] = true;
    }

    for (size_t x{}; x < maxXor; ++x) {
      if (!xorPairs[x])
        continue;

      for (const size_t &num : nums)
        xorTriplets[x ^ num] = true;
    }

    int xorCount = 0;
    for (size_t x{}; x < maxXor; ++x) {
      if (xorTriplets[x])
        ++xorCount;
    }

    return xorCount;
  }
};
