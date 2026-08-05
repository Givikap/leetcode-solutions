#include <string>

class Solution {
public:
  int minimumPushes(std::string word) {
    auto result = std::div(word.size(), 8);
    return ((result.quot << 2) + result.rem) * (result.quot + 1);
  }
};
