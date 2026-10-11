#include <ranges>
#include <string>
#include <vector>

class Solution {
public:
  std::string decodeMessage(std::string key, std::string message) {
    std::vector<char> charsMap(26, ' ');

    for (size_t k{}, i{}; k < key.size() && i < 26u; ++k) {
      if (isalpha(key[k]) && charsMap[key[k] - 'a'] == ' ')
        charsMap[key[k] - 'a'] = static_cast<char>('a' + i++);
    }

    for (const auto &[i, ch] : message | std::views::enumerate) {
      if (isalpha(ch))
        message[i] = charsMap[ch - 'a'];
    }

    return message;
  }
};
