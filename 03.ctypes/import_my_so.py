from ctypes import cdll, c_double
 
# 加载 SO 动态连结文件
mydll = cdll.LoadLibrary('./my_so.so')
 
# 设置 SO 文件中 dist 函数的参数数据型态
mydll.dist.argtypes = [c_double, c_double, c_double, c_double]
 
# 设置 SO 文件中 dist 函数的传回值数据型态
mydll.dist.restype = c_double
 
# 呼叫 SO 文件中的 dist 函数
d = mydll.dist(1.0, 1.0, 4.0, 5.0)
print("dist =", d)
