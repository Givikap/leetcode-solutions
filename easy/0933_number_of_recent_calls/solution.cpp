#include <queue>

class RecentCounter {
public:
  RecentCounter() {}

  int ping(int t) {
    requests_.push(t);
    while (!requests_.empty() && requests_.front() < t - 3000)
      requests_.pop();

    return static_cast<int>(requests_.size());
  }

private:
  std::queue<int> requests_;
};
