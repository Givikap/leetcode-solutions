#include <cstdlib>
#include <ranges>
#include <unordered_map>
#include <vector>

class Solution {
public:
  long long minSumSquareDiff(std::vector<int> &nums1, std::vector<int> &nums2,
                             int k1, int k2) {
    int k = k1 + k2;

    long long diffSum = 0ll;
    int diffMax = 1;
    std::unordered_map<int, int> diffCounter;

    for (const auto &[num1, num2] : std::views::zip(nums1, nums2)) {
      int diff = abs(num1 - num2);
      diffSum += static_cast<long long>(diff);
      diffMax = std::max(diffMax, diff);
      ++diffCounter[diff];
    }

    if (diffSum <= static_cast<long long>(k))
      return 0ll;

    for (int diff = diffMax; diff > 0; --diff) {
      if (k == 0)
        break;

      int count = diffCounter[diff];
      if (count == 0)
        continue;

      if (k >= count) {
        diffCounter[diff] = 0;
        diffCounter[diff - 1] += count;
        k -= count;
      } else {
        diffCounter[diff] -= k;
        diffCounter[diff - 1] += k;
        k = 0;
      }
    }

    long long minSumSquareDiff = 0ll;
    for (const auto &[diff, count] : diffCounter)
      minSumSquareDiff += static_cast<long long>(diff) * diff * count;

    return minSumSquareDiff;
  }
};
