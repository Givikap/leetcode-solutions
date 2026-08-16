#include <map>
#include <vector>

class Solution {
public:
  int findLHS(std::vector<int> &nums) {
    std::map<int, int> numsCounter;
    for (const int &num : nums)
      ++numsCounter[num];

    int maxLen = 0;

    for (auto it = numsCounter.begin(); it != numsCounter.end(); ++it) {
      if (next(it) != numsCounter.end() && next(it)->first - it->first == 1)
        maxLen = std::max(maxLen, it->second + next(it)->second);
    }

    return maxLen;
  }
};
