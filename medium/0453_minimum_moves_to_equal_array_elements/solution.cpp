#include <vector>

class Solution {
public:
  int minMoves(std::vector<int> &nums) {
    long long numsSum = 0;
    long long numsMin = LLONG_MAX;

    for (const long long &num : nums) {
      numsSum += num;
      numsMin = std::min(numsMin, num);
    }

    return static_cast<int>(numsSum -
                            numsMin * static_cast<long long>(nums.size()));
  }
};
