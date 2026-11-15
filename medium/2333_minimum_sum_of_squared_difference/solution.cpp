#include <cstdlib>
#include <numeric>
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
    std::vector<int> diffCounter(100001zu, 0);

    for (const auto &[num1, num2] : std::views::zip(nums1, nums2)) {
      int diff = abs(num1 - num2);
      diffSum += static_cast<long long>(diff);
      diffMax = std::max(diffMax, diff);
      ++diffCounter[static_cast<size_t>(diff)];
    }

    if (diffSum <= static_cast<long long>(k))
      return 0ll;

    auto diffs = std::views::iota(1zu, static_cast<size_t>(diffMax + 1));

    for (const auto &diff : diffs | std::views::reverse) {
      if (k == 0)
        break;

      int count = diffCounter[diff];
      if (count == 0)
        continue;

      if (k >= count) {
        diffCounter[diff] = 0;
        diffCounter[diff - 1zu] += count;
        k -= count;
      } else {
        diffCounter[diff] -= k;
        diffCounter[diff - 1zu] += k;
        k = 0;
      }
    }

    return std::accumulate(
        diffs.begin(), diffs.end(), 0ll, [&](auto acc, const auto &diff) {
          return acc + static_cast<long long>(diff) * diff * diffCounter[diff];
        });
  }
};
