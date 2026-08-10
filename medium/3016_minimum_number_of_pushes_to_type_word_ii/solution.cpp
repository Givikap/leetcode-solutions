#include <queue>
#include <string>
#include <unordered_map>

class Solution {
public:
  int minimumPushes(std::string word) {
    std::unordered_map<char, int> charsCounter;
    for (const char &ch : word)
      ++charsCounter[ch];

    std::priority_queue<int> pq;
    for (const auto &[_, count] : charsCounter)
      pq.push(count);

    int pushesCount = 0;
    int keysCount = 0;

    while (!pq.empty()) {
      pushesCount += ((keysCount++) / 8 + 1) * pq.top();
      pq.pop();
    }

    return pushesCount;
  }
};
