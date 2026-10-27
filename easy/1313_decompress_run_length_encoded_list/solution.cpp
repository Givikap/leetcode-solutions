#include <vector>

class Solution {
public:
  std::vector<int> decompressRLElist(std::vector<int> &nums) {
    std::vector<int> decompressedNums;

    for (size_t i{}; i < nums.size(); i += 2u) {
      for (int j = 0; j < nums[i]; ++j)
        decompressedNums.push_back(nums[i + 1]);
    }

    return decompressedNums;
  }
};
