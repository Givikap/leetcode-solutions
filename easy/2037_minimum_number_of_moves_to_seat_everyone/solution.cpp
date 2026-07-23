#include <vector>

class Solution {
public:
  int minMovesToSeat(std::vector<int> &seats, std::vector<int> &students) {
    std::sort(seats.begin(), seats.end());
    std::sort(students.begin(), students.end());

    int moves = 0;

    for (size_t i{}; i < seats.size(); ++i)
      moves += abs(seats[i] - students[i]);

    return moves;
  }
};
