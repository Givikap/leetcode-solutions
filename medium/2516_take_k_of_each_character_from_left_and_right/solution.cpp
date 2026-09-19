#include <string>
#include <vector>

class Solution {
public:
  int takeCharacters(std::string s, int k) {
    std::vector<int> charsCounter(3, 0);
    for (const auto &ch : s)
      ++charsCounter[static_cast<size_t>(ch - 'a')];

    for (size_t i{}; i < 3u; ++i) {
      if (charsCounter[i] < k)
        return -1;
    }

    std::vector<int> window(3, 0);
    size_t maxWindowLen = 0;

    for (size_t left = 0, right = 0; right < s.size(); ++right) {
      ++window[static_cast<size_t>(s[right] - 'a')];

      while (left <= right && (charsCounter[0] - window[0] < k) ||
             (charsCounter[1] - window[1] < k) ||
             (charsCounter[2] - window[2] < k))
        --window[static_cast<size_t>(s[left++] - 'a')];

      maxWindowLen = std::max(maxWindowLen, right - left + 1);
    }

    return static_cast<int>(s.size() - maxWindowLen);
  }
};
