import os

# 文件是否存在
os.access("main.c", os.F_OK)
# 文件是否可读
os.access("main.c", os.R_OK)
# 文件是否可写
os.access("main.c", os.W_OK)
# 文件是否可执行
os.access("main.c", os.X_OK)

# 返回的都是布尔值
