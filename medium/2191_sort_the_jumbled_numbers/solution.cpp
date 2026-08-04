#include <vector>

class Solution {
public:
  std::vector<int> sortJumbled(std::vector<int> &mapping,
                               std::vector<int> &nums) {
    const size_t n = nums.size();

    std::vector<std::pair<int, size_t>> jumpledPairs(n);

    for (size_t i{}; i < n; ++i) {
      int num = nums[i];
      int jumbledNum = 0;

      if (num == 0) {
        jumbledNum = mapping[0];
      } else {
        int mul = 1;

        while (num) {
          jumbledNum += mapping[num % 10] * mul;
          num /= 10;
          mul *= 10;
        }
      }

      jumpledPairs[i] = {jumbledNum, i};
    }

    sort(jumpledPairs.begin(), jumpledPairs.end());

    std::vector<int> jumpledNums(n);
    for (size_t i{}; i < n; ++i)
      jumpledNums[i] = nums[jumpledPairs[i].second];

    return jumpledNums;
  }
};
