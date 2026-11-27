#include <algorithm>
#include <array>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::vector<int> twoOutOfThree(std::vector<int> &nums1,
                                 std::vector<int> &nums2,
                                 std::vector<int> &nums3) {
    std::unordered_map<int, std::array<int, 3>> numsCounter;

    for (const auto &num : nums1)
      ++numsCounter[num][0zu];
    for (const auto &num : nums2)
      ++numsCounter[num][1zu];
    for (const auto &num : nums3)
      ++numsCounter[num][2zu];

    std::vector<int> nums;

    for (const auto &[num, counter] : numsCounter) {
      if (std::ranges::count(counter, 0) <= 1)
        nums.push_back(num);
    }

    return nums;
  }
};
