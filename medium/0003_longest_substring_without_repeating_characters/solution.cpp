#include <string>
#include <unordered_set>

class Solution {
public:
  int lengthOfLongestSubstring(std::string s) {
    std::unordered_set<char> window;
    int maxLen = 0;

    size_t left{};
    for (size_t right{}; right < s.size(); ++right) {
      while (window.find(s[right]) != window.end())
        window.erase(s[left++]);

      window.insert(s[right]);
      maxLen = std::max(maxLen, static_cast<int>(right - left + 1));
    }

    return maxLen;
  }
};
