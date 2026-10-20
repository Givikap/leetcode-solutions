#include <algorithm>
#include <ranges>
#include <vector>

class Solution {
public:
  int totalNumbers(std::vector<int> &digits) {
    std::ranges::sort(digits);

    int count = 0;
    do {
      if (digits[0] != 0 && digits[2] % 2 == 0)
        ++count;

      reverse(digits.begin() + 3, digits.end());

    } while (std::ranges::next_permutation(digits).found);

    return count;
  }
};
