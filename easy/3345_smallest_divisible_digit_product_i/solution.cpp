class Solution {
public:
  int smallestNumber(int n, int t) {
    while (true) {
      int nCopy = n++;
      int digitsProduct = 1;

      while (nCopy) {
        digitsProduct *= nCopy % 10;
        nCopy /= 10;
      }

      if (digitsProduct % t == 0)
        return n - 1;
    }

    return -1;
  }
};
