#include <vector>

class Solution {
public:
  int elevatorRequests(int n, std::vector<int> &requests) {
    int seconds = requests[0];

    for (size_t i = 1; i < requests.size(); ++i)
      seconds += abs(requests[i] - requests[i - 1]);

    return seconds;
  }
};
