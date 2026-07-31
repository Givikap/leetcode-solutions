#include <string>
#include <unordered_map>
#include <vector>

class Solution {
public:
  std::string frequencySort(std::string s) {
    std::unordered_map<char, size_t> frequencyMap;
    for (const char &ch : s)
      ++frequencyMap[ch];

    std::vector<std::pair<char, size_t>> frequencyPairs(frequencyMap.begin(),
                                                        frequencyMap.end());
    std::sort(
        frequencyPairs.begin(), frequencyPairs.end(),
        [](const std::pair<char, size_t> &a, const std::pair<char, size_t> &b) {
          return a.second > b.second;
        });

    s.clear();

    for (const auto &[ch, frequency] : frequencyPairs)
      s += std::string(frequency, ch);

    return s;
  }
};
