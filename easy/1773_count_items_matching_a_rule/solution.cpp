#include <string>
#include <vector>
class Solution {
public:
  int countMatches(std::vector<std::vector<std::string>> &items,
                   std::string ruleKey, std::string ruleValue) {
    size_t idx{};
    if (ruleKey == "color")
      idx = 1u;
    else if (ruleKey == "name")
      idx = 2u;

    int count = 0;

    for (const auto &item : items) {
      if (item[idx] == ruleValue)
        ++count;
    }

    return count;
  }
};
