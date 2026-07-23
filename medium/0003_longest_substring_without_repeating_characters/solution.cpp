#include <string>
#include <unordered_set>

class Solution {
public:
  int lengthOfLongestSubstring(std::string s) {
    int maxLen = 0;

    for (size_t left{}; left < s.size(); ++left) {
      std::unordered_set<char> window{s[left]};

      size_t right;
      for (right = left + 1; right < s.size(); ++right) {
        if (window.find(s[right]) == window.end())
          window.insert(s[right]);
        else
          break;
      }

      maxLen = std::max(maxLen, static_cast<int>(right - left));
    }

    return maxLen;
  }
};
