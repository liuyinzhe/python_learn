# https://www.xiaoyuanjiu.com/108605.html

from ctypes import cdll, c_double
 
# 加载 DLL 动态连结函数库
mydll = cdll.LoadLibrary('./MyDLL.dll')
 
# 设置 DLL 文件中 dist 函数的参数数据型态
mydll.dist.argtypes = [c_double, c_double, c_double, c_double]
 
# 设置 DLL 文件中 dist 函数的传回值数据型态
mydll.dist.restype = c_double
 
# 呼叫 DLL 文件中的 dist 函数
d = mydll.dist(1.0, 1.0, 4.0, 5.0)
print("dist =", d)

