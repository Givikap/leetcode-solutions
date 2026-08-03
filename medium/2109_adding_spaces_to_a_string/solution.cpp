#include <string>
#include <vector>

class Solution {
public:
  std::string addSpaces(std::string s, std::vector<int> &spaces) {
    std::string sWithSpaces;
    sWithSpaces.reserve(s.size() + spaces.size());

    for (size_t sIdx{}, spacesIdx{}; sIdx < s.size(); ++sIdx) {
      if (spacesIdx < spaces.size() && sIdx == spaces[spacesIdx]) {
        sWithSpaces.push_back(' ');
        ++spacesIdx;
      }

      sWithSpaces.push_back(s[sIdx]);
    }

    return sWithSpaces;
  }
};
