#include <string>

class Solution {
public:
  std::string digitSum(std::string s, int k) {
    while (s.size() > static_cast<size_t>(k)) {
      std::string sNew;

      for (size_t i{}; i < s.size(); i += static_cast<size_t>(k)) {
        int digitSum = static_cast<int>(s[i] - '0');
        for (size_t j = std::min(i + static_cast<size_t>(k), s.size()) - 1zu;
             j > i; --j)
          digitSum += static_cast<int>(s[j] - '0');

        sNew += std::to_string(digitSum);
      }

      s = std::move(sNew);
    }

    return s;
  }
};
