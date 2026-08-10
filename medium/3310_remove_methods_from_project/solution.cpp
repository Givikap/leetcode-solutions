#include <queue>
#include <vector>

class Solution {
public:
  std::vector<int>
  remainingMethods(int n, int k, std::vector<std::vector<int>> &invocations) {
    std::vector<std::vector<int>> calledMap(n);

    for (const auto &invocation : invocations)
      calledMap[invocation[0]].push_back(invocation[1]);

    std::vector<bool> suspicious(n, false);
    suspicious[k] = true;

    std::deque<int> dq = {k};
    while (!dq.empty()) {
      int a = dq.front();
      dq.pop_front();

      for (const int &b : calledMap[a]) {
        if (!suspicious[b]) {
          suspicious[b] = true;
          dq.push_back(b);
        }
      }
    }

    std::vector<int> methods;
    methods.reserve(n);

    for (const auto &invocation : invocations) {
      if (!suspicious[invocation[0]] && suspicious[invocation[1]]) {
        for (int a = 0; a < n; ++a)
          methods.push_back(a);

        break;
      }
    }

    if (methods.empty()) {
      for (int a = 0; a < n; ++a)
        if (!suspicious[a])
          methods.push_back(a);
    }

    return methods;
  }
};
