#include <algorithm>
#include <ranges>
#include <string>
#include <vector>

class Solution {
public:
  std::string shortestCompletingWord(std::string licensePlate,
                                     std::vector<std::string> &words) {
    std::vector<int> licensePlateCounter(26zu, 0);
    for (const auto &ch : licensePlate) {
      if (isalpha(ch))
        ++licensePlateCounter[static_cast<size_t>(tolower(ch) - 'a')];
    }

    std::string shortestWord = "";

    for (const auto &word : words) {
      std::vector<int> wordCounter(26zu, 0);
      for (const auto &ch : word)
        ++wordCounter[static_cast<size_t>(ch - 'a')];

      bool completing = true;

      for (size_t i{}; i < 26zu; ++i) {
        if (licensePlateCounter[i] > wordCounter[i]) {
          completing = false;
          break;
        }
      }

      if (completing &&
          (shortestWord.empty() || word.size() < shortestWord.size()))
        shortestWord = word;
    }

    return shortestWord;
  }
};
