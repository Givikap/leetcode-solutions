#include <string>
#include <vector>

class Solution {
public:
  int maximumLengthSubstring(std::string s) {
    std::vector<int> charsCounter(26, 0);

    int maxLen = 0;

    for (size_t left{}, right{}; right < s.size(); ++right) {
      ++charsCounter[s[right] - 'a'];

      while (charsCounter[s[right] - 'a'] > 2)
        --charsCounter[s[left++] - 'a'];

      maxLen = std::max(maxLen, static_cast<int>(right - left + 1));
    }

    return maxLen;
  }
};
