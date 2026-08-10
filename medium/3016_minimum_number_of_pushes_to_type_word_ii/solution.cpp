#include <algorithm>
#include <functional>
#include <string>
#include <vector>

class Solution {
public:
  int minimumPushes(std::string word) {
    std::vector<int> charsCounter(26, 0);
    for (const char &ch : word)
      ++charsCounter[ch - 'a'];

    std::sort(charsCounter.begin(), charsCounter.end(), std::greater<int>());

    int pushesCount = 0;
    int keysCount = 0;

    for (const int &count : charsCounter)
      pushesCount += ((keysCount++) / 8 + 1) * count;

    return pushesCount;
  }
};
