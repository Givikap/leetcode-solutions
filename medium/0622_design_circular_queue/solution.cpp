#include <vector>

class MyCircularQueue {
public:
  MyCircularQueue(int k) {
    capacity = static_cast<size_t>(k);
    size = 0;

    buffer = std::vector<int>(capacity);

    front = 0;
    back = capacity - 1;
  }

  bool enQueue(int value) {
    if (isFull())
      return false;

    back = (back + 1) % capacity;
    buffer[back] = value;
    ++size;

    return true;
  }

  bool deQueue() {
    if (isEmpty())
      return false;

    front = (front + 1) % capacity;
    --size;

    return true;
  }

  int Front() { return !isEmpty() ? buffer[front] : -1; }

  int Rear() { return !isEmpty() ? buffer[back] : -1; }

  bool isEmpty() { return !static_cast<bool>(size); }

  bool isFull() { return size == capacity; }

private:
  size_t capacity;
  size_t size;

  std::vector<int> buffer;

  size_t front;
  size_t back;
};
