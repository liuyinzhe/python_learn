#include <algorithm>
#include <functional>
 
// 排序函数
extern "C" void sort(
  double array[], const unsigned int size) {
  std::sort(array, array + size, std::less<double>());
}
