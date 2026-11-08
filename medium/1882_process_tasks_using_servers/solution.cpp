#include <queue>
#include <vector>

class Solution {
public:
  std::vector<int> assignTasks(std::vector<int> &servers,
                               std::vector<int> &tasks) {
    const size_t n = tasks.size();

    std::priority_queue<std::pair<int, size_t>,
                        std::vector<std::pair<int, size_t>>,
                        std::greater<std::pair<int, size_t>>>
        serverHeap;
    for (size_t i{}; i < servers.size(); ++i)
      serverHeap.push({servers[i], i});

    std::deque<size_t> taskQueue;
    std::priority_queue<std::pair<size_t, size_t>,
                        std::vector<std::pair<size_t, size_t>>,
                        std::greater<std::pair<size_t, size_t>>>
        jobHeap;

    std::vector<int> ans(n, -1);

    for (size_t t{}; t < n || !taskQueue.empty(); ++t) {
      while (!jobHeap.empty() && jobHeap.top().first <= t) {
        auto [_, i] = jobHeap.top();
        jobHeap.pop();
        serverHeap.push({servers[i], i});
      }

      if (t < n)
        taskQueue.push_back(t);

      while (!serverHeap.empty() && !taskQueue.empty()) {
        auto [_, i] = serverHeap.top();
        serverHeap.pop();

        size_t j = taskQueue.front();
        taskQueue.pop_front();

        jobHeap.push({t + static_cast<size_t>(tasks[j]), i});
        ans[j] = static_cast<int>(i);
      }

      if (t >= n - 1 && serverHeap.empty() && !taskQueue.empty() &&
          !jobHeap.empty())
        t = jobHeap.top().first - 1;
    }

    return ans;
  }
};
