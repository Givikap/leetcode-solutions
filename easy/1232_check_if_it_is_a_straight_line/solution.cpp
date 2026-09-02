#include <vector>

class Solution {
public:
  bool checkStraightLine(std::vector<std::vector<int>> &coordinates) {
    for (size_t i = 2; i < coordinates.size(); ++i) {
      if ((coordinates[i - 1][1] - coordinates[i - 2][1]) *
              (coordinates[i][0] - coordinates[i - 2][0]) !=
          (coordinates[i][1] - coordinates[i - 2][1]) *
              (coordinates[i - 1][0] - coordinates[i - 2][0]))
        return false;
    }

    return true;
  }
};
