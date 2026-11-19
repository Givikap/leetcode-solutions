class Solution {
public:
  bool isSameAfterReversals(int num) {
    auto reverseNum = [](int n) -> int {
      while (n && n % 10 == 0)
        n /= 10;

      int nReversed = 0;
      while (n) {
        nReversed = nReversed * 10 + n % 10;
        n /= 10;
      }

      return nReversed;
    };

    return reverseNum(reverseNum(num)) == num;
  }
};
