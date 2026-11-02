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
        ++licensePlateCounter[tolower(ch) - 97];
    }

    std::ranges::stable_sort(words, [](const auto &w1, const auto &w2) {
      return w1.size() < w2.size();
    });

    for (const auto &word : words) {
      bool completing = true;

      for (const auto &[i, count] :
           licensePlateCounter | std::views::enumerate) {
        if (std::ranges::count(word, static_cast<char>(97 + i)) < count) {
          completing = false;
          break;
        }
      }

      if (completing)
        return word;
    }

    return "";
  }
};
