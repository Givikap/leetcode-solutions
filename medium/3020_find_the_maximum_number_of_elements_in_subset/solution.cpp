#include <unordered_map>
#include <vector>

class Solution {
public:
  int maximumLength(std::vector<int> &nums) {
    std::unordered_map<int, int> numsCounter;
    for (const int &num : nums)
      ++numsCounter[num];

    int maxLen = 0;
    if (numsCounter.find(1) != numsCounter.end()) {
      maxLen = numsCounter[1];
      if (maxLen % 2 == 0)
        --maxLen;

      numsCounter.erase(1);
    }

    for (const auto &pair : numsCounter) {
      int num = pair.first;
      int currLen = 0;
      auto it = numsCounter.find(num);

      while (it != numsCounter.end() && it->second >= 2) {
        currLen += 2;

        if (num > INT_MAX / num) {
          it = numsCounter.end();
          break;
        }

        num *= num;
        it = numsCounter.find(num);
      }

      it = numsCounter.find(num);
      if (it != numsCounter.end() && it->second == 1)
        maxLen = std::max(maxLen, currLen + 1);
      else
        maxLen = std::max(maxLen, currLen - 1);
    }

    return maxLen;
  }
};
