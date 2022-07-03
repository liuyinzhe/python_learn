#include <algorithm>
#include <functional>
 
// 排序函数
extern "C" void sort(
  double array[], const unsigned int size) {
  std::sort(array, array + size, std::less<double>());
}

// 将 C++ 程序编译成 SO 动态连结文件
// g++ -Wall -Wextra -O -ansi -pedantic -fPIC -shared my_so2.cpp -o my_so2.so
