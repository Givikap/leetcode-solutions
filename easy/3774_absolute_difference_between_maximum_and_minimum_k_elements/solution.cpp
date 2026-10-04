#include <algorithm>
#include <cstdlib>
#include <ranges>
#include <vector>

class Solution {
public:
  int absDifference(std::vector<int> &nums, int k) {
    std::ranges::sort(nums);

    int smallestSum = 0;
    int largestSum = 0;

    for (size_t left{}, right = nums.size() - 1; left < static_cast<size_t>(k);
         ++left, --right) {
      smallestSum += nums[left];
      largestSum += nums[right];
    }

    return abs(largestSum - smallestSum);
  }
};
