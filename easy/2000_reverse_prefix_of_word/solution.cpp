#include <algorithm>
#include <string>

class Solution {
public:
  std::string reversePrefix(std::string word, char ch) {
    auto it = std::find(word.begin(), word.end(), ch);

    if (it != word.end())
      std::reverse(word.begin(), it + 1);

    return word;
  }
};
