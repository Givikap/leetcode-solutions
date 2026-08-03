#include <string>
#include <vector>

class Solution {
public:
  std::string addSpaces(std::string s, std::vector<int> &spaces) {
    std::string sWithSpaces(s.size() + spaces.size(), ' ');

    for (size_t sReadIdx{}, sWriteIdx{}, spacesIdx{}; sReadIdx < s.size();
         ++sReadIdx, ++sWriteIdx) {
      if (spacesIdx < spaces.size() && sReadIdx == spaces[spacesIdx]) {
        ++sWriteIdx;
        ++spacesIdx;
      }

      sWithSpaces[sWriteIdx] = s[sReadIdx];
    }

    return sWithSpaces;
  }
};
