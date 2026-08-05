#include <vector>

class Solution {
public:
  int maxProduct(int n) {
    std::vector<int> digits;

    while (n) {
      digits.push_back(n % 10);
      n /= 10;
    }

    sort(digits.begin(), digits.end());

    return digits[digits.end() - digits.begin() - 2] * digits.back();
  }
};
