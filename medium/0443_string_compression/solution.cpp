#include <string>
#include <vector>

class Solution {
public:
  int compress(std::vector<char> &chars) {
    const size_t n = chars.size();

    size_t read{};
    size_t write{};

    while (read < n) {
      chars[write++] = chars[read++];

      int count = 1;

      while (read < n && chars[read - 1] == chars[read]) {
        ++read;
        ++count;
      }

      if (count > 1) {
        for (const char &digit : std::to_string(count))
          chars[write++] = digit;
      }
    }

    return static_cast<int>(write);
  }
};
