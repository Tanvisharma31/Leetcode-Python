// Last updated: 02/03/2026, 14:01:42
class KthLargest {
 public:
  KthLargest(int k, vector<int>& nums) : k(k) {
    for (const int num : nums)
      heapify(num);
  }

  int add(int val) {
    heapify(val);
    return minHeap.top();
  }

 private:
  const int k;
  priority_queue<int, vector<int>, greater<>> minHeap;

  void heapify(int val) {
    minHeap.push(val);
    if (minHeap.size() > k)
      minHeap.pop();
  }
};