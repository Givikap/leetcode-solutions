#include <vector>

class RecentCounter {
public:
  RecentCounter() {
    left_ = 0;
    right_ = 0;
  }

  int ping(int t) {
    requests_.push_back(t);
    ++right_;

    while (left_ < right_ && requests_[left_] < requests_.back() - 3000)
      ++left_;

    return right_ - left_;
  }

private:
  std::vector<int> requests_;
  size_t left_;
  size_t right_;
};
