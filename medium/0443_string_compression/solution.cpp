#include <string>
#include <vector>

class Solution {
public:
  int compress(std::vector<char> &chars) {
    const size_t n = chars.size();

    int compressedCharsLen = 0;

    for (size_t right{}; right < n; ++right) {
      size_t left = right;
      while (right + 1 < n && chars[right] == chars[right + 1])
        ++right;

      chars[compressedCharsLen++] = chars[left];

      if (right - left + 1 > 1) {
        for (const char &digit : std::to_string(right - left + 1))
          chars[compressedCharsLen++] = digit;
      }
    }

    return compressedCharsLen;
  }
};
