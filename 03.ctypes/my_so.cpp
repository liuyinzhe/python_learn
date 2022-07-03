#include <cmath>
 
// 计算欧氏距离函数
extern "C" double dist(
  const double x1, const double y1,
  const double x2, const double y2) {
  return std::sqrt(std::pow(x1 - x2, 2) + std::pow(y1 - y2, 2));
}

// 将 C++ 程序编译成 SO 动态连结文件
// g++ -Wall -Wextra -O -ansi -pedantic -fPIC -shared my_so.cpp -o my_so.so
