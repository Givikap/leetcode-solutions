#include <functional>
#include <string>

class Solution {
public:
  bool validPalindrome(std::string s) {
    size_t left = 0;
    size_t right = s.size() - 1;

    std::function<bool(size_t, size_t)> isPalindrome = [&s](size_t l,
                                                            size_t r) -> bool {
      while (l < r) {
        if (s[l++] != s[r--])
          return false;
      }

      return true;
    };

    while (left < right) {
      if (s[left++] != s[right--])
        return isPalindrome(left, right + 1) || isPalindrome(left - 1, right);
    }

    return true;
  }
};
