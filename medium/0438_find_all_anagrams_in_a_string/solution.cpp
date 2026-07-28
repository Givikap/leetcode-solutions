#include <string>
#include <vector>

class Solution {
public:
  std::vector<int> findAnagrams(std::string s, std::string p) {
    if (s.size() < p.size())
      return {};

    const size_t k = p.size();

    std::vector<int> sCharCounter(26, 0);
    std::vector<int> pCharCounter(26, 0);

    size_t i{};
    for (; i < k; ++i) {
      ++sCharCounter[s[i] - 'a'];
      ++pCharCounter[p[i] - 'a'];
    }

    std::vector<int> substrings;
    if (sCharCounter == pCharCounter)
      substrings.push_back(0);

    for (; i < s.size(); ++i) {
      --sCharCounter[s[i - k] - 'a'];
      ++sCharCounter[s[i] - 'a'];

      if (sCharCounter == pCharCounter)
        substrings.push_back(i - k + 1);
    }

    return substrings;
  }
};
