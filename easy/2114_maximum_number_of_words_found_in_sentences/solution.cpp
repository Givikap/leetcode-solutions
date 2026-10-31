#include <algorithm>
#include <ranges>
#include <string>
#include <vector>

class Solution {
public:
  int mostWordsFound(std::vector<std::string> &sentences) {
    int maxWordCount = 0;

    for (const auto &sentence : sentences)
      maxWordCount =
          std::max(maxWordCount,
                   static_cast<int>(std::ranges::count(sentence, ' ')) + 1);

    return maxWordCount;
  }
};
