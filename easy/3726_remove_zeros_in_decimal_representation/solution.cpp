class Solution {
public:
  long long removeZeros(long long n) {
    long long m = 0;
    long long mul = 1;

    while (n) {
      long long digit = n % 10;
      n /= 10;

      if (digit) {
        m += digit * mul;
        mul *= 10;
      }
    }

    return m;
  }
};
