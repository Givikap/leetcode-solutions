#include <unordered_map>
#include <vector>

class Solution {
public:
  int findLHS(std::vector<int> &nums) {
    std::unordered_map<int, int> numsCounter;
    for (const int &num : nums)
      ++numsCounter[num];

    int maxLen = 0;

    for (const auto &[num, count] : numsCounter) {
      if (numsCounter.find(num + 1) != numsCounter.end())
        maxLen = std::max(maxLen, numsCounter[num] + numsCounter[num + 1]);
    }

    return maxLen;
  }
};
