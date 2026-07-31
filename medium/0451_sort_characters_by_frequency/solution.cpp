#include <string>
#include <unordered_map>

class Solution {
public:
  std::string frequencySort(std::string s) {
    std::unordered_map<char, int> frequencyMap;
    for (const char &ch : s)
      ++frequencyMap[ch];

    std::sort(s.begin(), s.end(), [&](const char &a, const char &b) {
      if (frequencyMap[a] == frequencyMap[b])
        return a > b;

      return frequencyMap[a] > frequencyMap[b];
    });

    return s;
  }
};
