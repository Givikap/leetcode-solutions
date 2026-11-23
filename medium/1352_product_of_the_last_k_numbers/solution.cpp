#include <vector>

class ProductOfNumbers {
public:
  ProductOfNumbers() { productsStream_ = {1}; }

  void add(int num) {
    if (num == 0) {
      productsStream_ = {1};
      return;
    }

    productsStream_.push_back(productsStream_.back() * num);
  }

  int getProduct(int k) {
    size_t kIdx = productsStream_.size() - 1zu - static_cast<size_t>(k);
    if (kIdx > productsStream_.size())
      return 0;

    return productsStream_.back() / productsStream_[kIdx];
  }

private:
  std::vector<int> productsStream_;
};
