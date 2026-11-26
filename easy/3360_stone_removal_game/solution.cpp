class Solution {
public:
  bool canAliceWin(int n) {
    return (n >= 10 && n < 19) || (n >= 27 && n < 34) || (n >= 40 && n < 45) ||
           (n >= 49 && n < 52) || (n >= 53 && n < 55);
  }
};
