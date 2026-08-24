class Solution {
public:
  bool checkDivisibility(int n) {
    int digitsSum = 0;
    int digitsProduct = 1;

    int nCopy = n;

    while (nCopy) {
      int digit = nCopy % 10;
      nCopy /= 10;

      digitsSum += digit;
      digitsProduct *= digit;
    }

    return n % (digitsSum + digitsProduct) == 0;
  }
};
