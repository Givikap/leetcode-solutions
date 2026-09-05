#include <string>
#include <string_view>
#include <vector>

class Solution {
public:
  std::vector<int> vowelStrings(std::vector<std::string> &words,
                                std::vector<std::vector<int>> &queries) {
    auto isVowel = [](char ch) -> bool {
      constexpr std::string_view vowels = "aeiou";
      return vowels.find(ch) != std::string_view::npos;
    };

    std::vector<int> prefixSums(words.size() + 1, 0);

    for (size_t i = 1; i <= words.size(); ++i)
      prefixSums[i] =
          prefixSums[i - 1] + static_cast<int>(isVowel(words[i - 1].front()) &&
                                               isVowel(words[i - 1].back()));

    std::vector<int> results;
    results.reserve(queries.size());

    for (const auto &query : queries)
      results.push_back(prefixSums[query[1] + 1] - prefixSums[query[0]]);

    return results;
  }
};
