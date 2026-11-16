#include <string>

class Solution {
public:
  std::string freqAlphabets(std::string s) {
    const size_t n = s.size();

    std::string sDecrypted;

    for (size_t i{}; i < n; ++i) {
      if (i + 2zu < n && s[i + 2zu] == '#') {
        sDecrypted.push_back('`' + stoi(s.substr(i, 3)));
        i += 2zu;
      } else {
        sDecrypted.push_back('0' + s[i]);
      }
    }

    return sDecrypted;
  }
};
